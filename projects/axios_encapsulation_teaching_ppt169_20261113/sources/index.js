const express = require('express');
const cors = require('cors');
const multer = require('multer');
const jwt = require('jsonwebtoken');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 3000;
const JWT_SECRET = 'axios_teaching_secret_key_2026';
const REFRESH_SECRET = 'axios_teaching_refresh_key_2026';

// 确保 uploads 目录存在
const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir, { recursive: true });
}

// 中间件配置
// 注意：必须通过 exposedHeaders 暴露 Content-Disposition，前端才能读取到自定义下载文件名！
app.use(cors({
  origin: '*',
  exposedHeaders: ['Content-Disposition']
}));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 静态文件服务
app.use('/uploads', express.static(uploadDir));

// 简单请求日志
app.use((req, res, next) => {
  const time = new Date().toLocaleTimeString();
  console.log(`[${time}] ${req.method} ${req.url}`);
  next();
});

// ======================== 1. 认证模块 (Auth) ========================

// 模拟用户登录
// 为了演示无感刷新 Token，我们将 Access Token 有效期设为 15 秒！
app.post('/api/auth/login', (req, res) => {
  const { username, password } = req.body;

  if (username === 'admin' && password === '123456') {
    const userInfo = { id: 1001, username: 'admin', role: 'teacher', name: 'Vue/Axios 讲师' };
    
    // access_token: 短期有效 (15秒用于教学演示)
    const accessToken = jwt.sign(userInfo, JWT_SECRET, { expiresIn: '15s' });
    // refresh_token: 长期有效 (7天)
    const refreshToken = jwt.sign({ id: userInfo.id }, REFRESH_SECRET, { expiresIn: '7d' });

    return res.json({
      code: 200,
      message: '登录成功！(注意：AccessToken 仅有 15s 有效期，用于演示无感刷新)',
      data: {
        accessToken,
        refreshToken,
        expiresIn: 15,
        userInfo
      }
    });
  }

  return res.status(400).json({
    code: 4001,
    message: '用户名或密码错误 (默认账号: admin, 密码: 123456)'
  });
});

// 无感刷新 Token 接口
app.post('/api/auth/refresh', (req, res) => {
  const { refreshToken } = req.body;
  if (!refreshToken) {
    return res.status(401).json({
      code: 401,
      message: '未提供 refreshToken'
    });
  }

  try {
    const decoded = jwt.verify(refreshToken, REFRESH_SECRET);
    const userInfo = { id: decoded.id, username: 'admin', role: 'teacher', name: 'Vue/Axios 讲师' };

    // 签发新的 access_token 和 refresh_token
    const newAccessToken = jwt.sign(userInfo, JWT_SECRET, { expiresIn: '15s' });
    const newRefreshToken = jwt.sign({ id: userInfo.id }, REFRESH_SECRET, { expiresIn: '7d' });

    console.log('>>> [服务端] 成功刷新 Token！签发新 Access Token');
    return res.json({
      code: 200,
      message: 'Token 刷新成功！',
      data: {
        accessToken: newAccessToken,
        refreshToken: newRefreshToken,
        expiresIn: 15
      }
    });
  } catch (err) {
    console.error('>>> [服务端] Refresh Token 失效或过期:', err.message);
    return res.status(401).json({
      code: 401,
      message: 'Refresh Token 无效或已过期，请重新登录'
    });
  }
});

// JWT 校验中间件
function verifyToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({
      code: 401,
      message: '请求未携带有效 Token (Authorization: Bearer <token>)'
    });
  }

  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    console.log(`>>> [服务端] Token 校验失败 [${err.name}]: ${err.message}`);
    return res.status(401).json({
      code: 401,
      message: 'Token 已过期或无效，触发前端 401 拦截'
    });
  }
}

// 受保护的用户信息接口
app.get('/api/user/profile', verifyToken, (req, res) => {
  res.json({
    code: 200,
    message: '获取受保护的用户信息成功',
    data: {
      userId: req.user.id,
      username: req.user.username,
      name: req.user.name,
      role: req.user.role,
      loginTime: new Date().toISOString(),
      permissions: ['user:view', 'user:edit', 'file:upload', 'file:download']
    }
  });
});

// ======================== 2. 请求控制与测试接口 ========================

// 模拟慢速/耗时接口 (用于测试 AbortController 取消重复请求/手动取消请求)
app.get('/api/test/delay', (req, res) => {
  const delay = parseInt(req.query.delay || '3000', 10);
  console.log(`>>> [服务端] 收到延迟请求，将等待 ${delay}ms 后响应...`);

  const timer = setTimeout(() => {
    res.json({
      code: 200,
      message: `延迟 ${delay}ms 的请求成功响应！`,
      data: {
        respondedAt: new Date().toLocaleTimeString(),
        duration: delay
      }
    });
  }, delay);

  // 如果客户端主动断开连接（如 AbortController 取消请求）
  req.on('close', () => {
    if (!res.writableEnded) {
      clearTimeout(timer);
      console.log('>>> [服务端] 检测到客户端已主动断开连接 (Request Aborted)');
    }
  });
});

// 模拟业务逻辑错误 (HTTP 状态码是 200，但业务状态码 code !== 200)
app.get('/api/test/business-error', (req, res) => {
  res.json({
    code: 5001,
    message: '【业务状态码异常】当前账户余额不足，扣费失败！',
    data: null
  });
});

// 模拟 HTTP 状态码错误 (403, 404, 500 等)
app.get('/api/test/http-error', (req, res) => {
  const status = parseInt(req.query.status || '500', 10);
  const statusMessages = {
    400: 'Bad Request (客户端请求语法错误)',
    403: 'Forbidden (无权访问该资源)',
    404: 'Not Found (请求的接口地址不存在)',
    500: 'Internal Server Error (服务器内部错误)',
    502: 'Bad Gateway (网关错误)'
  };

  res.status(status).json({
    code: status,
    message: `【HTTP ${status} 错误】${statusMessages[status] || '未知错误'}`
  });
});

// 模拟请求重试接口 (前 2 次故意报错 503，第 3 次成功返回)
const retryMap = new Map();
app.get('/api/test/retry', (req, res) => {
  const clientId = req.query.clientId || 'default';
  const count = (retryMap.get(clientId) || 0) + 1;
  retryMap.set(clientId, count);

  console.log(`>>> [服务端] 重试测试 [clientId: ${clientId}], 第 ${count} 次请求`);

  if (count < 3) {
    return res.status(503).json({
      code: 503,
      message: `【服务暂时不可用】第 ${count} 次请求失败，请自动重试...`
    });
  }

  // 第 3 次成功并重置计数
  retryMap.delete(clientId);
  res.json({
    code: 200,
    message: `恭喜！在第 ${count} 次重试时成功响应！`,
    data: {
      attemptCount: count,
      successTime: new Date().toLocaleTimeString()
    }
  });
});

// ======================== 3. 文件上传与下载 ========================

// 配置文件上传
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, uploadDir);
  },
  filename: function (req, file, cb) {
    const ext = path.extname(file.originalname);
    const basename = path.basename(file.originalname, ext);
    cb(null, `${basename}-${Date.now()}${ext}`);
  }
});
const upload = multer({ storage });

// 文件上传接口 (带人工延时以便前端观察 progress 进度条)
app.post('/api/file/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ code: 400, message: '请选择要上传的文件' });
  }

  // 延时 800ms 返回结果，增强教学演示效果
  setTimeout(() => {
    res.json({
      code: 200,
      message: '文件上传成功！',
      data: {
        originalName: req.file.originalname,
        filename: req.file.filename,
        size: req.file.size,
        mimetype: req.file.mimetype,
        url: `/uploads/${req.file.filename}`
      }
    });
  }, 800);
});

// 文件下载接口 (正确二进制流下载)
app.get('/api/file/download', (req, res) => {
  const fileName = 'Axios封装教学指南.txt';
  const content = `===========================================
      Axios 封装核心教学与实践指南
===========================================

1. 基础封装结构:
   - axios.create 实例
   - 请求拦截器 (Request Interceptor): 注入 Token、加载动画、取消重复请求
   - 响应拦截器 (Response Interceptor): 数据解包、统一业务状态码处理、统一错误提示

2. 高级特性:
   - AbortController 请求取消机制
   - 双 Token 无感刷新机制 (Access Token + Refresh Token)
   - 文件上传进度监听 (onUploadProgress)
   - Blob 文件流下载与文件名解析 (Content-Disposition)
   - Blob 报错兼容 (将 Blob 转回 JSON 提示错误信息)
   - 接口请求失败自动重试机制

生成时间: ${new Date().toLocaleString()}
`;

  // 必须配置 Content-Disposition，并支持中文编码 (RFC 5987 标准)
  const encodedName = encodeURIComponent(fileName);
  res.setHeader('Content-Type', 'text/plain; charset=utf-8');
  res.setHeader(
    'Content-Disposition',
    `attachment; filename="${encodedName}"; filename*=UTF-8''${encodedName}`
  );
  res.send(content);
});

// 文件下载失败接口 (模拟服务端导出异常，返回 JSON 错误)
// 用于教学：前端在 responseType: 'blob' 时如何正确解析出 JSON 错误并弹出错误提示！
app.get('/api/file/download-fail', (req, res) => {
  res.status(500).json({
    code: 5005,
    message: '【导出失败】数据库当前处于维护状态，导出报表失败！'
  });
});

// 启动服务器
app.listen(PORT, () => {
  console.log(`===============================================`);
  console.log(`🚀 [Node.js 后端服务已启动]`);
  console.log(`📡 服务地址: http://localhost:${PORT}`);
  console.log(`===============================================`);
});

