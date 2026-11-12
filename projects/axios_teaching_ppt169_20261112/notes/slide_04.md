请看大屏幕上的系统架构全景图。
我们在 client/src 目录下并没有将成百上千行代码堆死在一个 request.js 里，而是采用了清晰的分层解耦设计：
底层是独立的工具模块，如基于 AbortController 的 cancel.ts、基于计数器模型的 loading.ts、失败退避重试的 retry.ts；
核心层 request.ts 负责将这些独立工具像插拔插件一样挂载到 Axios 的请求和响应拦截器上；
顶层的业务 API 模块则只关心输入参数与输出类型，实现完全的职责分离。