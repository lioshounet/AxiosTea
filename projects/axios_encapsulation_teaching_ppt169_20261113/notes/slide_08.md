很多同学经常抱怨：为什么 Axios 拿到的数据总有一层 data，我们要写 res.data.data 甚至 res.data.data.list？
这就是统一数据解包解决的实际痛点。
我们在响应拦截器中判断如果服务端返回的 code === 200，就直接 return data，把包裹在外层的 code、message 剥离掉。
如果 code !== 200（比如余额不足、密码错误），拦截器自动弹窗提醒并 Promise.reject，业务页面只需直接关注成功数据即可。