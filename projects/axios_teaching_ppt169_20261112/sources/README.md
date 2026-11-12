# Axios 工业级深度封装教学与演练平台 (Vue 3 + TypeScript + Node.js)

本项目专为 **Vue 3 + TypeScript 进阶教学与大厂面试准备** 打造，前端工程已**全量采用 TypeScript 进行强类型重构**，并搭配对应的 **Node.js (Express) 后端服务**。

---

## 🌟 项目亮点与核心教学点

1. **全面 TypeScript 强类型支持**：
   - **Axios 声明合并 (Module Augmentation)**：在 `types/axios.d.ts` 扩展 `AxiosRequestConfig`，支持 `cancelDuplicate`、`showLoading`、`retryCount`、`retryDelay` 等属性的代码补全与类型检查；
   - **泛型数据自动解包**：封装 `request<T>(config): Promise<T>`，在响应拦截器中完成业务解包，使调用方获得精准的类型推导；
   - **Vue 组件全量 `<script setup lang="ts">`**：严格的类型安全。
2. **双 Token 无感刷新机制 (Dual Token Silent Refresh)**：
   - 短期 `Access Token` (演示设为 15 秒) + 长期 `Refresh Token` (7天)；
   - 拦截器捕获 `401` 并开启刷新锁；
   - **请求队列挂起重发**：并发请求下只调用一次刷新接口，防止 Token 刷新死锁与竞态覆盖；
   - 刷新失败自动清除凭据并引导登录重定向。
3. **基于 AbortController 的防重复请求与手动取消**：
   - 采用标准 Web API `AbortController` (替代已废弃的 CancelToken)；
   - 依据 `[Method + URL + Params + Data]` 生成唯一请求指纹；
   - 连续快速点击时自动取消未完成的前序请求，同时支持单请求配置豁免与页面跳转批量取消。
4. **并发安全的计数器 Loading 控制器 (Counter Pattern)**：
   - 解决同时发起多个并发请求时，第一个响应提前关闭 Loading 遮罩导致页面闪烁的问题；
   - 支持单请求通过 `showLoading: true` 独立控制。
5. **统一错误体系与接口自动重试 (Retry Pattern)**：
   - 严格区分 **业务逻辑状态码** (`code !== 200`，如余额不足) 与 **HTTP 协议状态码** (401/403/404/500)；
   - 针对超时、网络抖动及服务端临时 503 错误，实现 **可配置的自动重试机制** (`retryCount` 与 `retryDelay`)。
6. **文件流下载与 Blob 异常捕获 (经典高频面试题)**：
   - `onUploadProgress` 实时进度监听；
   - `responseType: 'blob'` 结合 RFC 5987 标准从 `Content-Disposition` 解析 UTF-8 文件名；
   - **核心避坑点**：当后端导出失败返回 JSON 错误时，前端拦截器自动将 Blob 二进制转换为 JSON 提取真实错误信息，避免下载出损坏的文件。
7. **配套实时日志观察台 (Request Console)**：
   - 前端右侧内置可视化请求链路监视器，直观展示拦截器执行、请求指纹、Token 换发等全过程。

---

## 📁 目录结构 (全量 TypeScript)

```text
Axios/
├── client/                     # Vue 3 + TypeScript 前端工程
│   ├── src/
│   │   ├── types/              # TypeScript 核心类型定义与声明扩展
│   │   │   ├── api.ts          # 通用响应泛型 ApiResponse<T> 与各类实体类型
│   │   │   └── axios.d.ts      # Axios 模块扩展声明 (AxiosRequestConfig 属性扩展)
│   │   ├── utils/              # 核心封装层 (TypeScript)
│   │   │   ├── request.ts      # Axios 核心实例、拦截器与泛型 request<T>()
│   │   │   ├── cancel.ts       # 基于 AbortController 的防重复/取消管理器
│   │   │   ├── loading.ts      # 并发安全的全屏 Loading 计数器 (Counter Pattern)
│   │   │   ├── retry.ts        # 失败请求自动退避重试逻辑
│   │   │   ├── download.ts     # Blob 文件流下载与 RFC 5987 文件名解析
│   │   │   └── token.ts        # 双 Token 本地存储工具
│   │   ├── api/                # 模块化 API 统一管理 (带泛型返回类型)
│   │   │   ├── auth.ts         # 登录与 Token 刷新接口
│   │   │   ├── user.ts         # 受保护的用户信息接口
│   │   │   ├── file.ts         # 文件上传与二进制下载接口
│   │   │   └── test.ts         # 慢速、业务错误、HTTP错误、重试测试接口
│   │   ├── stores/             # Pinia 状态库 (TypeScript 版)
│   │   │   ├── user.ts         # 用户鉴权与 Token 管理
│   │   │   └── logger.ts       # 实时执行日志
│   │   ├── components/
│   │   │   └── RequestConsole.vue  # 教学专用的实时日志控制台 (<script setup lang="ts">)
│   │   ├── App.vue             # 多 Tab 交互测试工作台 (<script setup lang="ts">)
│   │   ├── main.ts             # 应用入口
│   │   └── vite-env.d.ts       # 全局环境变量与 Window 钩子声明
│   ├── tsconfig.json           # TypeScript 编译配置 (支持 bundler 模式与路径别名)
│   ├── tsconfig.node.json
│   ├── vite.config.ts          # Vite 配置
│   └── package.json
├── server/                     # Node.js 后端服务 (Express JavaScript)
│   ├── index.js                # 后端全套 API 实现 (JWT 校验、延时模拟、流下载、Multer上传)
│   ├── uploads/                # 上传文件临时存储目录
│   └── package.json
├── start.bat                   # Windows 一键启动脚本
├── package.json                # 根目录快速启动配置
└── README.md                   # 深度教学说明文档
```

---

## 🚀 快速上手与运行

### 方式一：Windows 用户一键启动
双击运行根目录下的 `start.bat` 即可同时启动后端和前端服务。

### 方式二：命令行启动

1. **启动后端服务 (Node.js 端口 3000)**：
   ```bash
   cd server
   npm start
   ```

2. **启动前端服务 (Vue 3 + TS 端口 5173)**：
   ```bash
   cd client
   npm run dev
   ```

3. **执行 TypeScript 类型检查与构建**：
   ```bash
   cd client
   npm run type-check   # 运行 vue-tsc 严格类型检查
   npm run build        # 类型检查 + Vite 打包
   ```

4. **浏览器访问**：
   打开浏览器访问 [http://localhost:5173](http://localhost:5173)。

> **默认测试账号**：用户名 `admin`，密码 `123456`

---

## 💡 TypeScript 核心封装教学要点

### 1. 模块声明合并扩展 `AxiosRequestConfig`
在 `src/types/axios.d.ts` 中通过声明合并为请求配置增加类型提示：
```typescript
import 'axios';

declare module 'axios' {
  export interface AxiosRequestConfig {
    cancelDuplicate?: boolean;     // 防重复请求
    showLoading?: boolean;         // 显示 Loading
    loadingText?: string;          // 加载文本
    showErrorMessage?: boolean;    // 显示错误弹窗
    retryCount?: number;           // 重试次数
    retryDelay?: number;           // 重试间隔
    __retryCount?: number;         // 当前重试计数
  }
}
```

### 2. 泛型数据解包方法 `request<T>()`
在 `src/utils/request.ts` 中：
```typescript
export function request<T = any>(config: AxiosRequestConfig): Promise<T> {
  return service(config) as unknown as Promise<T>;
}
```
业务层调用示例：
```typescript
// 自动推导出 res 类型为 UserInfo，代码提示与补全极其精准
const res = await request<UserInfo>({
  url: '/api/user/profile',
  method: 'GET'
});
console.log(res.username, res.role);
```
