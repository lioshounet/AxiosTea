现在进入 TypeScript 架构重构部分。
我们在 request.ts 里面加了 cancelDuplicate、showLoading 这些自定义配置。
很多初学者如果不会写声明合并，在 TS 项目里就会满屏报红，说 AxiosRequestConfig 上不存在这些属性，于是只能无奈地写 (config as any)。
在企业级规范中，这是绝对不被允许的！
我们在 types/axios.d.ts 里使用了 declare module 'axios' 的声明合并技术。
直接扩展了官方的 AxiosRequestConfig 接口，不仅杜绝了 any，而且团队所有人在写代码时都能享受到完整的中文智能提示。