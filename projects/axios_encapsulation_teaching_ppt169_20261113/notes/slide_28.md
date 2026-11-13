很多同学在给 Axios 扩展自定义参数（如 showLoading、retry）时，因为 TypeScript 报错找不到属性，直接随手写一个 (config as any)，这是非常不规范的。
在企业级 TypeScript 架构中，标准做法是使用“模块扩充 (Module Augmentation)”。
在 axios.d.ts 中通过 declare module 'axios' 重新打开 AxiosRequestConfig 接口声明。
TypeScript 的类型系统会自动将我们定义的属性与 Axios 原生的 headers、timeout 等属性深度合并。
从此在调用 request({ retry: 3, showLoading: false }) 时，IDE 会提供极其精准的智能代码补全和严格的类型检查。