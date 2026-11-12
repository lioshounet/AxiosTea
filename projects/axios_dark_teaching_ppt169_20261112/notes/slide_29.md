请看大屏幕上的类型闭环全景。
经过前面响应拦截器的统一解包，service 返回的数据已经不再是原生繁琐的 AxiosResponse，而是直接的业务核心数据 data。
我们封装通用泛型函数 export function request<T = any>(config): Promise<T>。
业务 API 函数在调用时只需传入泛型参数，如 request<UserInfo>({ url: '/user' })。
业务组件在消费时直接拿到 UserInfo 类型，IDE 会自动补全字段，如果拼写错误或者后端少返回了字段，在 npm run type-check 阶段就会直接报错拦截，彻底消灭上线后的线上崩溃！