# -*- coding: utf-8 -*-
import os

project_dir = "c:/Users/Administrator/Desktop/Axios/projects/axios_dark_teaching_ppt169_20261112"

slides_data = []

# S01: Cover
slides_data.append({
    "num": 1,
    "role": "cover",
    "badge": "企业级前端网络架构 · 深度实战",
    "title": "Axios 工业级深度封装与后端联动全景实训",
    "kicker": "聚焦网络层核心机制 · 双向切面治理 · 高并发与容错避坑 · Node.js Express 真实联动",
    "type": "cover",
    "notes": """大家好！欢迎来到《Axios 工业级深度封装与后端联动全景实训》技术讲座。
本次课程完全聚焦于前端网络层核心——Axios 本身的工业级深度封装，并紧密结合后端的 Node.js Express 服务，带大家打通从底层协议、双向拦截器到高并发容错的全链路闭环。
我们将深入剖析原生调用的典型痛点，重点攻坚双 Token 无感并发刷新、请求指纹防重复提交、零频闪计数器 Loading、指数退避智能重试以及 Blob 文件流的异常反解。
课程安排了多个核心代码切面的逐行精读，带领大家把网络层的每一处工程细节彻底敲透！"""
})

# S02: Course Overview
slides_data.append({
    "num": 2,
    "role": "content",
    "badge": "课程体系大纲",
    "title": "为什么网络层封装是企业级前端的核心基石？",
    "kicker": "从离散的单点请求调用跃迁至全局全生命周期切面治理中枢",
    "type": "three_col",
    "cards": [
        ("原生裸用缺陷", "散落各处的样板代码，缺乏全局鉴权恢复能力；并发 401 凭据覆写死锁；连击重复提交引发后端脏数据；二进制文件下载异常无法被感知。", "#EF4444"),
        ("六大核心切面", "统一数据解包 · 双Token并发无感刷新 · AbortController请求指纹防重 · 计数器零闪烁Loading · 智能指数退避重试 · Blob流解析容错。", "#38BDF8"),
        ("全栈联动验证", "配套 Node.js Express 对应后端环境，模拟真实的 15s 鉴权过期、503 间歇宕机与流导出，配合 Pinia 可视化实时抓包控制台落地验证。", "#10B981")
    ],
    "summary": "【核心目标】掌握高内聚、低耦合的网络层封装体系，攻关大厂高频面试点与高可用生产架构。",
    "notes": """我们首先明确网络层在企业级前端中的战略地位。
前端视图组件的核心职能是状态渲染与用户交互，如果每个组件直接调用原生 axios，底层协议细节就会不可逆地渗透进业务代码中。
一旦服务端接口格式调整、鉴权方案升级或需要增加全局链路追踪，整套系统就会面临灾难性的重构成本。
优秀的网络层封装，对外向视图层交付纯净的业务数据契约，对内包揽异常捕获、重试恢复、生命周期拦截与防重控制，成为连接前后端的坚固基石。"""
})

# S03: Pain Points
slides_data.append({
    "num": 3,
    "role": "content",
    "badge": "原生缺陷剖析",
    "title": "原生 Axios 在大型复杂应用下的六大致命缺陷",
    "kicker": "这些隐藏在生产环境中的暗坑，你的代码中招了吗？",
    "type": "four_quadrant",
    "cards": [
        ("痛点 1：多层解包与空指针", "Axios 默认将响应包裹在 res.data 中，业务层必须层层手写 res.data.data，极易引发 TypeError 空指针报错。", "#EF4444"),
        ("痛点 2：Token 刷新竞态死锁", "接口 401 过期时若多个请求并发到达，同时发起刷新请求导致新旧 Token 覆写死锁，页面瞬间雪崩。", "#F59E0B"),
        ("痛点 3：手抖连击脏数据提交", "用户狂点提交按钮引发连续重复请求，后端接口若未做幂等控制，极易导致订单重复生成或资金重复划扣。", "#38BDF8"),
        ("痛点 4：Blob 错误文件劫持", "responseType: blob 时后端一旦返回业务错误 JSON，会被强行解析为损坏文件直接静默下载，难以捕获异常。", "#A855F7")
    ],
    "summary": "【架构启示】网络层封装的本质，是对原生 HTTP 交互脆弱性与不可控性的全面工程兜底。",
    "notes": """这里总结了业界在没有严格封装时最常踩的四大致命暗坑。
大家重点关注痛点 2 和痛点 4，这是大厂技术面试中最喜欢深挖的细节。
很多同学以为加个 axios.interceptors.response 就算封装完成了，结果一上线遇到并发接口过期，浏览器瞬间发出 5 个刷新请求，服务端直接判定非法操作。今天我们就是要针对这些痛点给出经受过工业检验的标准答案。"""
})

# S04: Architecture Overview
slides_data.append({
    "num": 4,
    "role": "content",
    "badge": "总体架构设计",
    "title": "TS + Axios 工业级分层解耦网络层体系全景拓扑",
    "kicker": "职责单一、高内聚低耦合的四层分层模型架构",
    "type": "four_layers",
    "layers": [
        ("1. 业务应用层 (API Services)", "auth.ts / user.ts / test.ts / file.ts —— 面向视图组件提供精准强类型的函数调用契约"),
        ("2. 封装核心层 (Request Core)", "request.ts —— 实例配置、主 service 与轻量 refreshService 隔离、串联双向拦截器流水线"),
        ("3. 通用工具层 (Modular Utilities)", "cancel.ts (AbortController) · loading.ts (计数器) · retry.ts (重试) · download.ts (流反解) · token.ts"),
        ("4. 支撑服务层 (Mock & Backend)", "Node.js Express 对应后端 + Pinia Logger 实时拦截器执行链路控制台")
    ],
    "summary": "【架构原则】各模块职责独立，工具层无视图强依赖，核心层通过拦截器聚合全局能力。",
    "notes": """请看大屏幕上的系统架构全景图。
我们在工程中绝不能把成百上千行代码堆死在一个单一的 request.js 里，而是采用了清晰的分层解耦模型：
底层是独立的纯工具函数模块，如基于 AbortController 的 cancel.ts、基于计数器模型的 loading.ts、指数退避重试的 retry.ts；
核心层 request.ts 负责像插件流水线一样将这些独立工具按序编排到 Axios 的拦截器中；
业务 API 层只消费强类型函数，完全感知不到底层繁重的网络细节。"""
})

# S05: Base Instance
slides_data.append({
    "num": 5,
    "role": "content",
    "badge": "核心要点一 · 实例基线",
    "title": "Axios 实例配置哲学：baseURL、超时与实例隔离",
    "kicker": "打造标准化、易维护且环境隔离的 HTTP 请求基线",
    "type": "three_col",
    "cards": [
        ("baseURL 统一路由配置", "结合 import.meta.env.VITE_APP_BASE_API 与 Vite 本地代理 /api，兼顾本地跨域开发与线上生产部署。", "#38BDF8"),
        ("超时时间安全底线 (timeout)", "配置 timeout: 10000 (10秒)，避免因弱网挂起导致浏览器连接池占满耗尽，并配合 AbortController 实现精准中断。", "#F59E0B"),
        ("多实例彻底隔离红线", "创建业务主 service 实例与专职轻量 refreshService 实例，彻底切断 401 拦截死循环递归调用栈。", "#EF4444")
    ],
    "summary": "【关键准则】绝不在全局 axios 默认对象上挂载拦截器，保障微前端基座与第三方 SDK 请求不受污染。",
    "notes": """现在进入核心要点一：实例基线与配置哲学。
首先强调第一条架构红线：永远不要直接在全局 axios 对象上挂载业务拦截器！在微前端（如 Qiankun）或者引入第三方 SDK 时，修改全局对象会导致全局污染，造成排查难度极高的幽灵 Bug。
其次，为什么一定要独立声明 refreshService？因为主实例包含了 401 拦截逻辑，如果刷新 Token 的请求本身发生 401，若复用主实例就会再次触发刷新，导致陷入灾难性的递归死锁！"""
})

# S06: Interceptor Pipeline
slides_data.append({
    "num": 6,
    "role": "content",
    "badge": "核心要点一 · 管道切面",
    "title": "Axios 双向切面管道模型：请求发起与响应收拢生命周期",
    "kicker": "基于洋葱模型的切面治理，实现关注点的彻底分离",
    "type": "pipeline",
    "steps": [
        ("1. 业务调用", "api() 发起", "携带参数与自定义元配置"),
        ("2. 请求拦截器", "Request Pipeline", "注入 Token / 注册指纹防重 / 启动 Loading"),
        ("3. 网络传输", "HTTP Transport", "底层 XHR / Fetch 发出物理网络包"),
        ("4. 响应拦截器", "Response Pipeline", "注销防重 / 扣减 Loading / 统一解包判空"),
        ("5. 结果交付", "Promise Resolve", "直接交付业务纯净数据，异常进 catch")
    ],
    "summary": "【切面治理】把所有与 UI 视图无关的网络底层脏活，全闭环拦截在管道内部消化完毕。",
    "notes": """这张时序图展示了请求在拦截器流水线中的完整生命周期。
大家可以把拦截器想象成机场的安全检查通道：
在登机前（请求拦截器），安检人员帮你盖上签证印章（注入 Bearer Token）、登记防重名单、通知地面服务准备。
在到达目的地后（响应拦截器），海关人员帮你核验包裹（解析业务状态码）、若发现违禁品直接拦截并报警（抛出业务异常）、正常行李则直接送到你手上。"""
})

# S07: Code Deep Dive 1 (request.ts setup)
slides_data.append({
    "num": 7,
    "role": "content",
    "badge": "【代码解析 1】",
    "title": "request.ts 核心实例创建与双向拦截器装配源码剖析",
    "kicker": "工业级网络层入口的搭建细节与防御性配置",
    "type": "code_highlight",
    "code": """// client/src/utils/request.ts
import axios, { type AxiosInstance, type AxiosRequestConfig } from 'axios';

// 1. 创建业务主实例
export const service: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_API || '/api',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json;charset=utf-8' }
});

// 2. 装配请求拦截器：注入鉴权 Token、防重注册、启动计数 Loading
service.interceptors.request.use((config) => {
  const token = getToken();
  if (token) config.headers.set('Authorization', `Bearer ${token}`);
  if (config.cancelDuplicate !== false) addPendingRequest(config);
  if (config.showLoading !== false) showLoading(config.loadingText);
  return config;
}, (error) => Promise.reject(error));""",
    "summary": "【设计亮点】通过 config 元配置显式控制各切面行为，拦截器管道具备高可拔插性与配置灵活性。",
    "notes": """请大家看屏幕上的核心源码。
我们在创建 service 实例时配置了通用的 baseURL 与 10 秒超时。
在请求拦截器中，我们做了三件事：
第一，检查本地是否存在 Token，通过 config.headers.set 安全注入 Bearer Token；
第二，判断当前接口是否开启防重复提交，调用 addPendingRequest 注册请求指纹；
第三，判断是否开启 Loading，调用 showLoading 递增计数器。
每一项功能都可以通过自定义配置项关闭，体现了极佳的灵活性。"""
})

# S08: Data Unwrapping & Contract
slides_data.append({
    "num": 8,
    "role": "content",
    "badge": "核心要点一 · 数据解包",
    "title": "统一业务解包机制：终结冗长繁琐的 .data.data",
    "kicker": "前后端统一响应结构契约与业务异常自动拦截",
    "type": "two_col_code",
    "left_title": "原生方式 (业务层繁琐判空样板代码)",
    "left_code": "// 原生 Axios 编写方式\nconst res = await axios.get('/api/user');\n// 冗余取值且容易因后端微服务变动报 TypeError\nif (res.data && res.data.code === 200) {\n  this.userInfo = res.data.data;\n} else {\n  ElMessage.error(res.data.message || 'Error');\n}",
    "right_title": "封装后方式 (响应拦截器统一剥除外壳)",
    "right_code": "// request.ts 响应拦截器\nconst { code, data, message } = response.data;\nif (code === 200 || code === 0) {\n  return data; // 直接返回业务核心实体\n}\nElMessage.error(message || '系统业务异常');\nreturn Promise.reject(new Error(message));",
    "summary": "【收益】剥离业务外壳的同时自动捕获业务级非 200 错误，让业务组件代码清爽、专注。",
    "notes": """很多同学经常抱怨：为什么 Axios 拿到的数据总有一层 data，我们要写 res.data.data 甚至 res.data.data.list？
这就是统一数据解包解决的实际痛点。
我们在响应拦截器中判断如果服务端返回的 code === 200，就直接 return data，把包裹在外层的 code、message 剥离掉。
如果 code !== 200（比如余额不足、密码错误），拦截器自动弹窗提醒并 Promise.reject，业务页面只需直接关注成功数据即可。"""
})

# S09: Dual Token Concepts
slides_data.append({
    "num": 9,
    "role": "content",
    "badge": "核心要点二 · 双Token",
    "title": "核心要点二：双 Token 鉴权体系设计哲学与前后端联动",
    "kicker": "安全防窃密与平滑用户体验的极致工程平衡",
    "type": "three_col",
    "cards": [
        ("短命 AccessToken (15秒)", "用于所有日常业务接口的身份鉴权，由请求拦截器自动装配在 Authorization 头中，过期后立即失效防止泄露。", "#38BDF8"),
        ("长命 RefreshToken (7天)", "存放在安全的本地存储中，专职用于在 AccessToken 过期时调用 /api/auth/refresh 接口换取新的访问凭据。", "#10B981"),
        ("后端 Express 接口联动", "Node.js 后端 verifyToken 中间件精准校验 15s 时效，并在 /api/auth/refresh 接口完成令牌轮转更新。", "#F59E0B")
    ],
    "summary": "【架构价值】兼具极高的安全防御能力（短期凭据降低泄漏窗口）与无感的连续登录体验。",
    "notes": """现在进入大厂面试最核心的高频考点：双 Token 无感刷新机制。
单 Token 方案存在根本性矛盾：时效太短用户频繁被迫重新登录，时效太长一旦令牌被拦截窃取就面临巨大安全风险。
双 Token 方案正是解决这个难题的工业级标准：
日常业务接口只认 15 秒极短生命周期的 AccessToken，即便泄漏黑客也很快无法使用；
前端感知到 401 后，后台自动使用长周期的 RefreshToken 悄悄换取新 Token，用户在界面上完全无感。"""
})

# S10: Token Refresh Flow
slides_data.append({
    "num": 10,
    "role": "content",
    "badge": "核心要点二 · 状态流转",
    "title": "HTTP 401 拦截切入与无感刷新状态流转全生命周期",
    "kicker": "捕获 401 -> 锁定刷新 -> 队列暂存 -> 换回令牌 -> 批量重放",
    "type": "pipeline",
    "steps": [
        ("1. 捕获 401", "Catch 401", "响应拦截器 error 分支识别状态码为 401"),
        ("2. 互斥状态锁", "Lock State", "isRefreshing === false 时置为 true 并发起刷新"),
        ("3. 并发队列挂起", "Push Queue", "后序并发请求包装为未决 Promise 压入队列"),
        ("4. 换取新令牌", "Get Token", "通过独立轻量 refreshService 请求刷新接口"),
        ("5. 批量 Replay", "Flush Queue", "刷新成功后遍历队列，替换新 Token 重新发送")
    ],
    "summary": "【核心逻辑】无论瞬间并发几十个业务接口，整个系统在同一时刻有且仅发起一次刷新请求。",
    "notes": """请大家看大屏幕上的五步状态流转链路。
当某个请求发生 401 时，拦截器立即切入刷新逻辑。
如果当前没有正在刷新的任务（isRefreshing 为 false），该请求立即抢占锁并将 isRefreshing 置为 true，负责发起刷新接口。
此时，其他同时发生 401 的并发接口会发现锁已被占用，它们不会重新发起刷新，而是把自己封装成未决的 Promise 存入 retryQueue 挂起队列中静静等待。
一旦刷新接口成功换回新 Token，执行队列中所有的回调函数，换上新 Token 重新发送，完成批量重放。"""
})

# S11: Code Deep Dive 2 (Refresh Queue Implementation)
slides_data.append({
    "num": 11,
    "role": "content",
    "badge": "【代码解析 2】",
    "title": "isRefreshing 互斥锁与 retryQueue 挂起队列核心实现",
    "kicker": "高并发场景下防死锁互斥锁与未决 Promise 队列精读",
    "type": "code_highlight",
    "code": """// 响应拦截器 401 错误切入处理
if (error.response?.status === 401) {
  const originalConfig = error.config;
  if (!isRefreshing) {
    isRefreshing = true;
    return handleTokenRefresh().then((newToken) => {
      retryQueue.forEach((cb) => cb(newToken));
      retryQueue = [];
      originalConfig.headers.set('Authorization', `Bearer ${newToken}`);
      return service(originalConfig); // 重放主请求
    }).finally(() => { isRefreshing = false; });
  } else {
    // 互斥锁已被占用，返回未决 Promise 将自身挂起进入队列
    return new Promise((resolve) => {
      retryQueue.push((token: string) => {
        originalConfig.headers.set('Authorization', `Bearer ${token}`);
        resolve(service(originalConfig));
      });
    });
  }
}""",
    "summary": "【硬核原理】利用 JS 单线程事件循环与 Promise 状态机特性，实现纯内存级的高并发排队重发。",
    "notes": """这段代码是整个 Axios 封装最值钱的核心实现，大厂面试常要求现场手写。
大家看 else 分支：我们返回了一个既没有 resolve 也没有 reject 的 new Promise！
这个 Promise 的 resolve 触发权被移交给了 retryQueue 数组中的闭包回调函数。
由于 Promise 状态未决，外部业务调用的 await 就会一直处于挂起等待状态。
直到 then 回调中执行了 retryQueue.forEach(cb => cb(newToken))，所有被挂起的请求才会瞬间被唤醒并重发，对业务层完全透明！"""
})

# S12: Concurrency Swimlane
slides_data.append({
    "num": 12,
    "role": "content",
    "badge": "核心要点二 · 时序泳道",
    "title": "多接口并发 401 时的安全排队与批量 Replay 时序泳道",
    "kicker": "可视化复现微前端与多数据卡片并发加载下的令牌自愈现场",
    "type": "queue_swimlane",
    "items": [],
    "summary": "【时序闭环】Req 1 成功完成开拓任务，Req 2/3/4 安全搭乘顺风车，无任何重复鉴权开销。",
    "notes": """通过这张时序泳道图，大家可以清晰看到多请求并发时的时序推进过程：
阶段一：页面加载瞬间发出 4 个接口，由于本地 Token 刚刚过期，Req #1 最先被服务端判定为 401；
阶段二：Req #1 抢先将 isRefreshing 置为 true，专职去请求 /api/auth/refresh；
阶段三：在此期间到达的 Req #2、#3、#4 识别到锁被占用，立即被压入 retryQueue 挂起队列；
阶段四：新 Token 换回后，批量唤醒队列中的所有回调，带上全新 Token 重新发出，无缝完成数据交付。"""
})

# S13: Isolation Anti-pattern Compare
slides_data.append({
    "num": 13,
    "role": "content",
    "badge": "架构避坑指南",
    "title": "架构安全红线：切忌在拦截器内递归调用带拦截器的实例",
    "kicker": "轻量级 refreshService 独立实例隔离 vs 递归调用主实例的雪崩现场",
    "type": "two_col_compare",
    "left_title": "致命错误写法 (调用主 service 实例)",
    "left_text": "在 401 拦截器内部调用 service.post('/api/auth/refresh')\n若该刷新接口本身发生 401（例如 RefreshToken 已过期或被拉黑）\n主实例的拦截器会再次捕获该 401 并再次尝试刷新\n系统陷入无休止的自我递归死循环，瞬间耗尽浏览器连接池并导致内存溢出爆栈！",
    "left_color": "#EF4444",
    "right_title": "生产级安全规范 (独立 refreshService)",
    "right_text": "单独声明 const refreshService = axios.create({ baseURL })\n该实例绝不挂载任何 401 自动刷新的响应拦截器！\n刷新接口报错时直接返回失败，触发 clearAuth() 并跳转登录页\n彻底切断循环依赖链条，从根本上杜绝死锁与雪崩风险！",
    "right_color": "#10B981",
    "summary": "【架构底线】任何从事异常恢复操作的基础客户端，必须与被恢复的宿主客户端严格物理隔离。",
    "notes": """很多同学在实现无感刷新时，直接在拦截器里调用 service.post('/auth/refresh')，这是一个极其严重的架构隐患！
如果用户的 RefreshToken 在服务端也被注销或过期了，刷新接口就会返回 401。
此时主 service 的拦截器再次拦截该 401，又去发起刷新，从而引发无限递归爆栈！
正确做法是单独创建一个轻量级的 refreshService，这个实例纯粹负责发请求，绝不加 401 自动刷新拦截，失败了就直接提示用户登出。"""
})

# S14: Cancel Necessity
slides_data.append({
    "num": 14,
    "role": "content",
    "badge": "核心要点三 · 防重提交",
    "title": "核心要点三：重复请求的成因、危害与防御体系",
    "kicker": "手抖快速连击、路由快速切换残留与后端数据脏写的终极克星",
    "type": "four_quadrant",
    "cards": [
        ("危害 1：按钮连击重复入库", "用户表单提交或下单时手抖狂点，前序请求未结即发出新请求，引发数据库并发脏写入。", "#EF4444"),
        ("危害 2：SPA 路由切换幽灵响应", "用户快速切换导航菜单，旧页面的耗时查询延迟返回后错误覆盖新页面数据（竞态覆盖）。", "#F59E0B"),
        ("危害 3：弱网重复消耗宽带", "移动端网络波动时未决连接持续占用浏览器 6 个并发连接通道，导致高优先级接口阻塞。", "#38BDF8"),
        ("解法：AbortController 切面防重", "以请求唯一指纹哈希为键，全局 Map 集中管理 Signal 信号量，自动撤销前序 Pending 请求。", "#10B981")
    ],
    "summary": "【防重哲学】前端网络层主动掐断冗余请求，不仅保护了用户体验，更极大减轻了服务端计算压力。",
    "notes": """现在进入核心要点三：基于 AbortController 的防重复提交机制。
在真实的业务场景中，手抖快速连击按钮、表格分页快速切换、SPA 路由快速跳转，都会产生大量的重复请求。
如果不做处理，后发出的请求可能先返回，先发出的请求后返回，从而导致新数据被旧数据覆盖的竞态 Bug。
通过封装全局防重复取消机制，每当发起一个相同指纹的请求时，自动将前一个尚未完成的请求 cancel 掉，彻底避免竞态和脏数据。"""
})

# S15: Fingerprint Algorithm
slides_data.append({
    "num": 15,
    "role": "content",
    "badge": "核心要点三 · 指纹算法",
    "title": "请求指纹生成算法：四维哈希与 Map 控制器注册表",
    "kicker": "Method + URL + Params + Data 四维哈希，精准识别请求幂等性",
    "type": "pipeline",
    "steps": [
        ("1. 提取元数据", "Extract Meta", "提取请求 Method, URL, Params, Data 四项核心参数"),
        ("2. 序列化哈希", "Serialize Key", "JSON.stringify 严格排序序列化，生成唯一字符串 Key"),
        ("3. 冲突侦测", "Detect Pending", "检查 pendingMap 是否已存在相同 Key 的未决请求"),
        ("4. 自动撤销旧请求", "Abort Previous", "若存在，调用旧 controller.abort() 主动切断网络连接"),
        ("5. 注册新控制器", "Register New", "生成全新 AbortController 并挂载至 config.signal")
    ],
    "summary": "【算法特性】精准识别相同请求，后发优先，永远保障最后一次用户意图生效。",
    "notes": """请看大屏幕上的请求指纹四维哈希生成算法。
如何判定两个请求是“重复请求”？
我们通过请求方法（GET/POST）、请求路径（URL）、URL 查询参数（Params）以及请求体负载（Data）四项要素。
将这四项要素序列化拼装成唯一的 Key（例如 'post&/api/order&{}&{id:1}'）。
在发起请求前，先去 pendingMap 中查询，如果查到了，说明前一个请求还没结束，立刻调用 abort() 撤销前一个，然后将新的控制器存入 Map。"""
})

# S16: Code Deep Dive 3 (cancel.ts Implementation)
slides_data.append({
    "num": 16,
    "role": "content",
    "badge": "【代码解析 3】",
    "title": "cancel.ts 唯一指纹哈希与 Map 注册表管理源码剖析",
    "kicker": "原生现代 AbortController 替代废弃 CancelToken 的工业级实现",
    "type": "code_highlight",
    "code": """// client/src/utils/cancel.ts
const pendingMap = new Map<string, AbortController>();

export function generateRequestKey(config: AxiosRequestConfig): string {
  const { method, url, params, data } = config;
  return [method, url, JSON.stringify(params), JSON.stringify(data)].join('&');
}

export function addPendingRequest(config: AxiosRequestConfig): void {
  const requestKey = generateRequestKey(config);
  // 若已存在相同请求，立即撤销前序请求
  if (pendingMap.has(requestKey)) {
    const controller = pendingMap.get(requestKey);
    controller?.abort('重复请求被自动取消');
    pendingMap.delete(requestKey);
  }
  // 实例化新控制器并绑定信号量
  const controller = new AbortController();
  config.signal = controller.signal;
  pendingMap.set(requestKey, controller);
}""",
    "summary": "【版本演进】彻底淘汰已废弃的 CancelToken，拥抱现代 Web 原生 AbortController 标准规范。",
    "notes": """请大家看屏幕上的代码实现。
首先，Axios 官方在 v0.22.0 之后已经明确废弃了传统的 CancelToken，全面推荐使用标准的 AbortController。
我们在 addPendingRequest 中获取生成好的 requestKey。
如果 Map 里已经存在，直接拿出 controller 并调用 abort()，Axios 底层便会立即抛出 CanceledError 中断 XHR/Fetch；
接着我们 new 一个新的 AbortController，将其 signal 属性直接赋值给 config.signal，并存入 Map 备用。"""
})

# S17: Route Cleanup & Manual Abort
slides_data.append({
    "num": 17,
    "role": "content",
    "badge": "核心要点三 · 场景扩展",
    "title": "场景扩展：SPA 路由守卫自动清空与页面主动中断",
    "kicker": "内存泄漏防护、页面跳转防闪退与大耗时任务的手动掐断",
    "type": "two_col_code",
    "left_title": "路由守卫联动清理 (router.beforeEach)",
    "left_code": "// router/index.ts\nimport { clearAllPendingRequests }\n  from '@/utils/cancel';\n\nrouter.beforeEach((to, from, next) => {\n  // 页面跳转瞬间，自动取消上一页未完成的所有请求\n  clearAllPendingRequests();\n  next();\n});\n// 彻底防止旧页面异步数据返回引发报错或泄漏",
    "right_title": "业务组件按需主动中断 (Abort on Demand)",
    "right_code": "// 耗时报表计算或大文件查询，支持用户点击按钮手动取消\nconst controller = new AbortController();\nexportBigDataApi({\n  signal: controller.signal\n});\n\n// 用户点击【停止生成】\nfunction handleUserAbort() {\n  controller.abort('用户主动停止计算');\n}",
    "summary": "【全场景覆盖】既支持全局层面的自动化防重防泄漏，又支持业务层面的精确颗粒度中断控制。",
    "notes": """防重复机制不仅能防连击，还能与 Vue Router 路由守卫紧密联动。
当用户在 SPA 单页应用中从 A 页面迅速切到 B 页面时，A 页面发出的那些耗时请求已经没有意义了。
我们在 router.beforeEach 中调用 clearAllPendingRequests()，把 Map 中所有的控制器全部 abort 掉，既节省了带宽，又杜绝了内存泄漏。
同时，对于一些长达几十秒的大数据报表接口，用户界面可以提供一个“取消”按钮，随时主动中断请求。"""
})

# S18: Loading Timeline Flaw
slides_data.append({
    "num": 18,
    "role": "content",
    "badge": "核心要点四 · Loading缺陷",
    "title": "核心要点四：并发异步请求下的 Loading 状态劫持现场",
    "kicker": "单布尔值控制 Loading 的致命缺陷与时序推导复现",
    "type": "timeline_flaw",
    "items": [],
    "summary": "【缺陷根源】单布尔值丢失了并发请求的生命周期上下文，任何单一请求的完成都会误杀全局遮罩。",
    "notes": """现在进入核心要点四：并发安全 Loading 状态机设计。
很多初学者在项目中直接用一个 boolean 变量来控制全局 Loading：请求开始时 loading = true，请求结束时 loading = false。
这种做法在单请求场景下看起来正常，但在真实业务场景中是完全错误的！
请看屏幕上的时序图：当页面同时发出耗时 100ms 的请求 A、300ms 的请求 B、500ms 的请求 C。
在 100ms 时请求 A 完成了，直接执行了 loading = false！
此时页面遮罩提前消失，但请求 B 和 C 还在执行中，用户误以为加载完毕再次点击，或者页面发生剧烈的闪烁！"""
})

# S19: Code Deep Dive 4 (loading.ts Counter Pattern)
slides_data.append({
    "num": 19,
    "role": "content",
    "badge": "【代码解析 4】",
    "title": "loading.ts Counter Pattern 计数器与防抖延时源码实现",
    "kicker": "计数器安全模型 + 200ms 防抖消除闪烁的标准工业级解法",
    "type": "code_highlight",
    "code": """// client/src/utils/loading.ts
let loadingCount = 0;
let loadingInstance: ReturnType<typeof ElLoading.service> | null = null;

export function showLoading(text = '加载中...'): void {
  if (loadingCount === 0) {
    // 启动全局全屏 Loading
    loadingInstance = ElLoading.service({ text, background: 'rgba(11,15,25,0.7)' });
  }
  loadingCount++; // 计数递增
}

export function hideLoading(): void {
  if (loadingCount <= 0) return;
  loadingCount--; // 计数递减
  // 严格保障所有并发请求全部完成归零后，才真正销毁遮罩
  if (loadingCount === 0 && loadingInstance) {
    loadingInstance.close();
    loadingInstance = null;
  }
}""",
    "summary": "【计数器法则】请求发出 count++，响应返回 count--，有且仅有 count === 0 时才关闭遮罩。",
    "notes": """这段源码展示了著名的“计数器模型 (Counter Pattern)”。
我们声明一个全局变量 loadingCount，初始值为 0。
当第一个请求发出时，loadingCount 从 0 变成 1，立即开启遮罩；
后续请求到达时，只让 loadingCount++，不再重复创建遮罩；
当请求响应或者报错时，调用 hideLoading 让 loadingCount--；
只有当最后一个请求完成，loadingCount 彻底归零时，才真正调用 loadingInstance.close() 关闭遮罩！
这就彻底保证了无论有多少个并发异步请求，遮罩都能精准守护整个加载周期。"""
})

# S20: Loading Fine-grained Control
slides_data.append({
    "num": 20,
    "role": "content",
    "badge": "核心要点四 · 细粒控制",
    "title": "细粒度接口控制：自定义文案、指定挂载容器与静默请求",
    "kicker": "兼顾全局统一遮罩与局部按需控制的灵活设计",
    "type": "three_col",
    "cards": [
        ("自定义 Loading 文案", "支持在接口请求时传入 loadingText: '正在生成报表中...'，动态展示专业上下文提示，提升等待体验。", "#38BDF8"),
        ("静默请求 (showLoading: false)", "下拉联想补全、心跳保活检测、后台轮询等接口，显式配置关闭遮罩，避免界面频繁被中断。", "#10B981"),
        ("局部容器挂载 (target)", "支持传入 DOM 容器或 CSS 选择器，仅在表格、卡片内部展示局部 Loading，不遮挡整个页面主视图。", "#F59E0B")
    ],
    "summary": "【设计智慧】通过默认配置保障 80% 常见场景，通过元参数覆盖满足 20% 特殊定制需求。",
    "notes": """在解决了计数器并发安全之后，我们还要考虑细粒度的控制能力。
比如有的操作耗时较长，我们希望 Loading 提示文字显示“正在导出大数据中...”；
而对于一些后台静默请求，比如搜索框的输入自动联想、用户在线心跳包检测，如果频繁弹出全屏 Loading，用户体验会极差。
我们在 AxiosRequestConfig 中扩展了 showLoading: false 配置项，遇到静默请求直接跳过计数器，不打扰用户正常操作。"""
})

# S21: Error Retry Boundary
slides_data.append({
    "num": 21,
    "role": "content",
    "badge": "核心要点五 · 容错重试",
    "title": "核心要点五：网络异常分类与自动重试策略边界划分",
    "kicker": "明确重试的适用范围：哪些错误应当重试，哪些错误绝不能重试！",
    "type": "three_col",
    "cards": [
        ("应当重试的场景 (可恢复)", "网络超时 (ECONNABORTED)、偶发断网 (ERR_NETWORK)、服务端瞬时 503 重启、网关 502/504 抖动。", "#10B981"),
        ("绝不能重试的场景 (不可恢复)", "400 参数格式错误、401 凭证过期、403 权限拒绝、404 资源不存在、业务逻辑报错 (如余额不足)。", "#EF4444"),
        ("非幂等操作的谨慎重试", "POST 创建订单、资金划扣等操作若重试可能导致重复创建，需配合服务端业务唯一 Request-Id 防重保证幂等性。", "#F59E0B")
    ],
    "summary": "【重试铁律】只有不可抗力的瞬时网络链路波动才允许重试，逻辑错误重试只会加剧服务端负担。",
    "notes": """现在进入核心要点五：双轨错误处理与智能指数退避重试。
很多同学写自动重试逻辑时不管三七二十一，只要接口报错就重试 3 次，这是极其业余的做法！
我们必须严格划分重试边界：
如果服务端返回 400（参数缺失）、403（没有权限）或者业务层提示“余额不足”，你重试 100 次它也依然失败，重试毫无意义，还会平白消耗服务端计算资源；
只有网络断流、请求超时、或者服务端正在灰度重启返回 503 等瞬时网络异常，自动重试才能化腐朽为神奇，挽救用户的网络请求。"""
})

# S22: Exponential Backoff Principle
slides_data.append({
    "num": 22,
    "role": "content",
    "badge": "核心要点五 · 退避算法",
    "title": "指数退避算法 (Exponential Backoff) 原理与延时增长曲线",
    "kicker": "避免重试风暴导致服务端雪崩的关键数学退避模型",
    "type": "pipeline",
    "steps": [
        ("1. 初次失败", "1st Fail (0ms)", "请求发生 503 异常，触发重试决策机制"),
        ("2. 首次退避重试", "1st Retry (1000ms)", "延时 1000ms 发起第 1 次重试尝试"),
        ("3. 二次指数退避", "2nd Retry (2000ms)", "若仍失败，延时翻倍至 2000ms 发起第 2 次重试"),
        ("4. 三次高位退避", "3rd Retry (4000ms)", "延时继续翻倍至 4000ms 发起第 3 次终极重试"),
        ("5. 彻底放弃报警", "Final Reject", "超过重试上限，抛出全局异常并提示排查网络")
    ],
    "summary": "【算法优势】通过逐渐拉长等待间隔，为后端微服务重启与网络自我修复留出充裕的缓冲窗口。",
    "notes": """为什么重试不能采用固定间隔（比如每隔 100ms 重试一次）？
因为当后端服务宕机重启时，成千上万个前端客户端如果同时以高频率狂轰重试，就会形成恐怖的“重试风暴 (Retry Storm)”，刚刚重启的后端服务瞬间被再次打垮！
指数退避算法的数学原理是：第 n 次重试的延迟时间为 baseDelay * 2^(n-1)。
第 1 次等 1 秒，第 2 次等 2 秒，第 3 次等 4 秒。
这样既能快速捕捉偶发网络波动，又能在服务端真正重启时逐渐拉大间隔，给服务端留出恢复时间。"""
})

# S23: Code Deep Dive 5 (retry.ts Implementation)
slides_data.append({
    "num": 23,
    "role": "content",
    "badge": "【代码解析 5】",
    "title": "retry.ts 基于 Promise 延时链与重试计数器拦截器注入",
    "kicker": "基于 AxiosRequestConfig 元数据实现全自动退避重发精读",
    "type": "code_highlight",
    "code": """// client/src/utils/retry.ts
export function handleResponseRetry(error: any, instance: AxiosInstance): Promise<any> {
  const config = error.config;
  if (!config || !config.retry || config.retry <= 0) return Promise.reject(error);
  
  // 维护重试计数器元数据
  config.__retryCount = config.__retryCount || 0;
  if (config.__retryCount >= config.retry) return Promise.reject(error);
  
  config.__retryCount += 1;
  // 计算指数退避延迟时间：retryDelay * 2^(count - 1)
  const backoffDelay = (config.retryDelay || 1000) * Math.pow(2, config.__retryCount - 1);
  
  // 返回 Promise 延时链条，在定时器触发后重新发起请求
  return new Promise((resolve) => {
    setTimeout(() => {
      console.warn(`[Network Retry] 正在发起第 ${config.__retryCount} 次重试...`);
      resolve(instance(config)); // 重发请求
    }, backoffDelay);
  });
}""",
    "summary": "【实现精髓】利用 Promise 延迟解决链，将重试无缝封装在响应拦截器的 error 管道中。",
    "notes": """大家看屏幕上的代码实现。
当请求在响应拦截器抛出 error 时，我们进入 handleResponseRetry 函数。
首先读取 config.retry 配置项，判断当前接口是否开启了重试。
如果开启了，我们在 config 对象上维护一个私有变量 __retryCount 作为计数器。
接着计算退避延迟时间：通过 Math.pow(2, count - 1) 算出翻倍时间。
然后构造一个由 setTimeout 包裹的 Promise 延迟链条，在定时器结束时再次调用 instance(config) 重新发出请求。
重试成功后，后续 then 照常接收数据，业务组件完全感知不到底层曾经历过一次险象环生的网络重试！"""
})

# S24: Backend 503 Simulation Linkage
slides_data.append({
    "num": 24,
    "role": "content",
    "badge": "后端联动验证",
    "title": "Node.js Express 503 宕机恢复模拟与全链路抓包实战",
    "kicker": "前后端真实接口联动：直观观测前端自动重试成功自愈全流程",
    "type": "two_col_code",
    "left_title": "后端 Express 模拟 503 接口 (server/index.js)",
    "left_code": "// server/index.js\nlet failCount = 0;\napp.get('/api/test/retry-simulation', (req, res) => {\n  failCount++;\n  // 前 2 次故意返回 503 模拟宕机，第 3 次恢复正常\n  if (failCount <= 2) {\n    return res.status(503).json({\n      code: 503,\n      message: `[503 维护中] 第 ${failCount} 次重试`\n    });\n  }\n  failCount = 0; // 重置计数\n  res.json({ code: 200, data: '第 3 次重试成功！' });\n});",
    "right_title": "前端控制台抓包链路日志输出 (Pinia Logger)",
    "right_code": "[Request] GET /api/test/retry-simulation -> 发出\n[Response Error] HTTP 503 Service Unavailable\n[Retry Manager] 触发第 1 次重试，等待 1000ms...\n[Retry Manager] 触发第 2 次重试，等待 2000ms...\n[Response Success] HTTP 200 OK -> 业务数据交付完成！\n\n页面未弹出报错弹窗，全过程自动自愈！",
    "summary": "【全栈闭环】配套的 Node.js 后端完整模拟了真实高并发容错场景，为教学实训提供真实验证抓手。",
    "notes": """为了让教学实训具备真实的验证效果，我们在 server/index.js 中编写了一个专门的 503 模拟接口。
后端维护了一个全局计数器，前 2 次调用故意返回 HTTP 503 模拟服务器正在重启，直到第 3 次才返回 200。
学员在前端界面点击【测试自动重试】按钮，可以在 Pinia 抓包控制台中直观看到：
请求初次失败 -> 自动等待 1 秒重试第 1 次 -> 再次失败 -> 自动等待 2 秒重试第 2 次 -> 第 3 次成功返回数据并展示在页面上！
整个过程没有冒出任何刺眼的错误弹窗，让学员切身体会到工业级容错的震撼魅力。"""
})

# S25: Blob Download Barriers
slides_data.append({
    "num": 25,
    "role": "content",
    "badge": "核心要点六 · Blob深坑",
    "title": "核心要点六：二进制文件流下载的技术壁垒与常见陷阱",
    "kicker": "字符编码乱码、内存泄漏危机与静默下载损坏文件的噩梦",
    "type": "three_col",
    "cards": [
        ("陷阱 1：中文文件名乱码", "后端在 Content-Disposition 中返回中文文件名，前端直接使用 decodeURI 解析时产生乱码甚至提取失败。", "#F59E0B"),
        ("陷阱 2：URL.createObjectURL 内存泄漏", "创建的 blob:http:// 临时对象 URL 在下载后未手动调用 revokeObjectURL 释放，长期停留导致内存暴涨。", "#EF4444"),
        ("陷阱 3：服务端异常被强转为坏文件", "前端配置了 responseType: 'blob'，当后端校验失败返回 JSON 时，Axios 会将错误 JSON 强行当成文件下载为损坏文件！", "#38BDF8")
    ],
    "summary": "【大厂必考】文件导出不仅是创建 a 标签点击那么简单，异常捕获与内存管理是核心考察点。",
    "notes": """现在进入核心要点六：Blob 二进制流下载与大厂面试深坑。
很多同学以为导出文件很简单，调一下接口，用 window.URL.createObjectURL 创建个链接，再搞个 a 标签 click() 一下就完事了。
但在生产环境中，这里有三个极其致命的暗坑：
第一，RFC 5987 中文文件名如果不做规范解码，下载出来的文件名全是一堆乱码；
第二，创建的 Blob URL 不及时释放会导致浏览器内存泄漏；
第三个最要命：一旦后端参数校验不通过或者鉴权失败返回了一个 JSON 错误，因为你写了 responseType: 'blob'，Axios 会把后端返回的 JSON 报错文本直接当成一个空文件下载到用户电脑上！"""
})

# S26: RFC 5987 Decoding
slides_data.append({
    "num": 26,
    "role": "content",
    "badge": "核心要点六 · RFC解码",
    "title": "RFC 5987 规范标准：解析 Content-Disposition 中文文件名",
    "kicker": "彻底攻克标准 HTTP 头中 filename*=utf-8'' 编码的解码算法",
    "type": "two_col_code",
    "left_title": "标准 HTTP 响应头样例",
    "left_code": "// 现代后端标准 Content-Disposition Header\nContent-Disposition: attachment;\n  filename=\"fallback.xlsx\";\n  filename*=utf-8''%E7%94%A8%E6%88%B7...;\n\n// 包含了两个文件名定义：\n// 1. filename: 传统 ASCII 兼容备用名\n// 2. filename*: RFC 5987 标准 UTF-8 编码真名",
    "right_title": "标准解码提取算法源码 (download.ts)",
    "right_code": "// client/src/utils/download.ts\nexport function extractFileName(disp: string): string {\n  // 1. 优先匹配 RFC 5987 格式\n  const rfcReg = /filename\\*=utf-8''([^;]+)/i;\n  const rfcMatch = disp.match(rfcReg);\n  if (rfcMatch && rfcMatch[1]) {\n    return decodeURIComponent(rfcMatch[1]);\n  }\n  // 2. 降级匹配普通 filename=\"...\"\n  const reg = /filename=\"?([^\";]+)\"?/i;\n  const match = disp.match(reg);\n  return match ? decodeURIComponent(match[1]) : 'file';\n}",
    "summary": "【标准演进】严格遵循 RFC 5987 规范，优先匹配 UTF-8 编码，向下兼容普通 ASCII 文件名。",
    "notes": """请看大屏幕上的 RFC 5987 标准。
现代浏览器和后端框架在处理非 ASCII 字符（如中文文件名）时，遵循的是 RFC 5987 协议标准。
服务端会在响应头中返回：filename*=utf-8''%E7%94%A8%E6%88%B7...
我们在 extractFileName 函数中使用正则表达式，优先匹配 filename*=utf-8'' 后面的内容，并使用 decodeURIComponent 进行解码。
如果匹配不到，再降级去匹配普通的 filename="fallback.xlsx"。这样无论在什么浏览器或操作系统上，导出的中文文件名都绝对不会出现任何乱码！"""
})

# S27: Code Deep Dive 6 (Blob JSON Parsing Fallback)
slides_data.append({
    "num": 27,
    "role": "content",
    "badge": "【代码解析 6】",
    "title": "download.ts 破解大厂深坑：Blob 内嵌 JSON 错误信息精准反解",
    "kicker": "通过 FileReader 异步嗅探还原服务端真实业务报错黑科技",
    "type": "code_highlight",
    "code": """// client/src/utils/request.ts 响应拦截器\nif (response.config.responseType === 'blob') {\n  // 侦测 Content-Type 是否为 JSON（说明后端虽然 HTTP 200，但实际抛出了业务错误）\n  if (response.data.type === 'application/json') {\n    return new Promise((_, reject) => {\n      const reader = new FileReader();\n      reader.onload = () => {\n        try {\n          const errorResult = JSON.parse(reader.result as string);\n          ElMessage.error(errorResult.message || '导出失败，服务端异常');\n          reject(new Error(errorResult.message));\n        } catch {\n          reject(new Error('解析 Blob 异常错误失败'));\n        }\n      };\n      reader.readAsText(response.data); // 将二进制反解回原始文本 JSON\n    });\n  }\n  return response; // 正常文件流，交付后续 download 模块\n}""",
    "summary": "【破坑黑科技】通过检查 data.type 并使用 FileReader 异步回读，完美解决二进制流中隐蔽包装的业务报错。",
    "notes": """这段代码是解决痛点 4 的终极神器，也是阿里、字节技术面非常热衷考察的亮点。
当接口报错时，后端通常会返回类似 { code: 5001, message: '数据量超过上限，请缩小查询范围' } 的 JSON。
但因为前端事先设置了 responseType: 'blob'，Axios 会无条件把这段 JSON 字符转成 Blob 对象传给业务层！
我们在响应拦截器中做了一个关键嗅探：检查 response.data.type 是否等于 'application/json'。
如果是，立即启动一个 FileReader，调用 readAsText(response.data) 将二进制数据异步读回文本，再用 JSON.parse 还原出后端的真实报错信息并弹窗提醒！
这样就彻底避免了把错误信息当成损坏文件下载到用户本地的尴尬故障。"""
})

# S28: Code Deep Dive 7 (axios.d.ts Module Augmentation)
slides_data.append({
    "num": 28,
    "role": "content",
    "badge": "【代码解析 7】",
    "title": "TypeScript 架构进阶：axios.d.ts 声明合并扩展配置",
    "kicker": "掌握 TypeScript 模块扩充 (Module Augmentation) 技巧，打造强类型体验",
    "type": "code_highlight",
    "code": """// client/src/types/axios.d.ts\nimport 'axios';\n\n// 利用 TypeScript 声明合并 (Declaration Merging) 语法特性扩充第三方库接口\ndeclare module 'axios' {\n  export interface AxiosRequestConfig {\n    /** 是否开启接口级全屏 Loading 遮罩，默认 true */\n    showLoading?: boolean;\n    /** 自定义 Loading 提示文案 */\n    loadingText?: string;\n    /** 是否开启重复请求自动取消，默认 true */\n    cancelDuplicate?: boolean;\n    /** 接口失败时自动重试的次数，0 为不重试 */\n    retry?: number;\n    /** 自动重试的基础延迟毫秒数，默认 1000ms */\n    retryDelay?: number;\n    /** 内部私有重试计数器 */\n    __retryCount?: number;\n  }\n}""",
    "summary": "【类型安全】告别 (config as any) 的野蛮断言，让自定义元配置享受 100% 完整的 IDE 智能补全与类型检查。",
    "notes": """很多同学在给 Axios 扩展自定义参数（如 showLoading、retry）时，因为 TypeScript 报错找不到属性，直接随手写一个 (config as any)，这是非常不规范的。
在企业级 TypeScript 架构中，标准做法是使用“模块扩充 (Module Augmentation)”。
在 axios.d.ts 中通过 declare module 'axios' 重新打开 AxiosRequestConfig 接口声明。
TypeScript 的类型系统会自动将我们定义的属性与 Axios 原生的 headers、timeout 等属性深度合并。
从此在调用 request({ retry: 3, showLoading: false }) 时，IDE 会提供极其精准的智能代码补全和严格的类型检查。"""
})

# S29: Generic Request Contract
slides_data.append({
    "num": 29,
    "role": "content",
    "badge": "TS 契约架构",
    "title": "端到端强类型守卫：泛型 request<T>() 封装与业务契约对齐",
    "kicker": "函数输入参数精准校验，函数返回值直达业务实体类型",
    "type": "four_quadrant",
    "cards": [
        ("统一泛型包装函数", "export function request<T = any>(config: AxiosRequestConfig): Promise<T>，返回类型直接对齐业务泛型 T。", "#38BDF8"),
        ("业务接口契约定义", "export interface UserInfo { id: number; username: string; role: string; }，前后端定义精准强类型模型。", "#10B981"),
        ("业务组件零断言消费", "const user = await getUserInfoApi(); // user 自动推导为 UserInfo 类型，直接访问属性无任何类型隐患。", "#F59E0B"),
        ("编译期类型安全兜底", "若前端访问不存在的属性（如 user.age），vue-tsc 编译期直接拦截报警，将运行时错误扼杀在开发阶段。", "#A855F7")
    ],
    "summary": "【全链路闭环】从底层拦截器解包到顶层组件渲染，全链路贯穿强类型约束，打造不可动摇的工程健壮性。",
    "notes": """请看大屏幕上的类型闭环全景。
经过前面响应拦截器的统一解包，service 返回的数据已经不再是原生繁琐的 AxiosResponse，而是直接的业务核心数据 data。
我们封装通用泛型函数 export function request<T = any>(config): Promise<T>。
业务 API 函数在调用时只需传入泛型参数，如 request<UserInfo>({ url: '/user' })。
业务组件在消费时直接拿到 UserInfo 类型，IDE 会自动补全字段，如果拼写错误或者后端少返回了字段，在 npm run type-check 阶段就会直接报错拦截，彻底消灭上线后的线上崩溃！"""
})

# S30: Ending Summary
slides_data.append({
    "num": 30,
    "role": "ending",
    "badge": "总结回顾 · 架构进阶",
    "title": "课程全景技术图谱总结、架构进阶指南与源码仓库",
    "kicker": "掌握网络层工业级封装，奠定前端架构进阶之路的坚实基石",
    "type": "ending",
    "pillars": [
        ("双向切面治理", "实例基线与隔离红线，请求/响应拦截器洋葱流水线，统一业务数据解包"),
        ("双Token无感并发刷新", "HTTP 401 拦截切入，isRefreshing 全局互斥锁，retryQueue 挂起队列批量重发"),
        ("防重提交与安全Loading", "AbortController 四维哈希请求指纹，Counter Pattern 并发安全防抖 Loading 状态机"),
        ("容错重试与类型闭环", "指数退避智能重试防风暴，Blob 流 RFC 5987 解码与 JSON 反解，TS 声明合并")
    ],
    "footer": "全套教学源码与配套 Node.js 后端已全部开源！",
    "notes": """最后，我们对本期技术课程进行全景梳理与总结。
我们今天从原生调用的痛点出发，完整剖析了现代企业级前端网络层封装的四大核心支柱：
第一支柱：双向切面治理与实例隔离，打造标准请求基线；
第二支柱：双 Token 无感并发刷新机制，平衡安全性与用户体验；
第三支柱：基于 AbortController 的防重复提交与并发安全计数器 Loading；
第四支柱：指数退避重试、Blob 异常反解以及 TypeScript 声明合并的类型工程化闭环。
全套 Vue 3 + TypeScript 前端工程与配套的 Node.js 后端源码已全部开源同步在 GitHub 上。希望大家把代码克隆下来，对照本次课程的代码解析页面，亲自动手敲一遍、抓包调试一遍，真正将这些架构设计思维内化为自己的硬实力！谢谢大家！"""
})

print(f"[OK] Defined {len(slides_data)} slides in slides_dark_config.py")
