我们再来看泛型函数 request<T>() 的封装。
因为我们在响应拦截器里已经做过了数据解包，把外层的 code 和 message 脱掉了，直接返回内部的 data。
所以我们封装的通用 request 函数直接将返回值映射为 Promise<T>。
在业务 api/user.ts 里，我们只需传入泛型参数 <UserInfo>。
当组件调用这个 API 时，拿到 user 变量打一个点，IDE 瞬间弹出 username、name、role、permissions。
一旦字段名拼写错误，TypeScript 编译器会在打包阶段立刻报错拦截，把 Bug 扼杀在上线之前！