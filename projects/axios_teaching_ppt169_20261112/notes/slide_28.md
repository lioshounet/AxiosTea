很多同学在学 Axios 封装时，最大的痛苦就是没有配套的后端环境，只能用 mockjs 拦截。
但 mockjs 是在浏览器内存里伪造的，根本无法模拟真实的 HTTP 401 状态码、无法模拟真实的网络断开连接、也无法模拟 responseType: blob 下的真实二进制流。
为此，我们用纯 JavaScript 编写了一个小巧精悍的 Node.js Express 后端。
不仅完美对应所有的前端用例，而且延时接口甚至可以监听客户端的 req.on('close')，直观证明 AbortController 确实成功终止了服务端的等待。