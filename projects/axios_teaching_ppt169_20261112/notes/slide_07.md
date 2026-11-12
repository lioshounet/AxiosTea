很多初学者经常抱怨：为什么 Axios 拿到的数据总有一层 data，我们要写 res.data.data 甚至 res.data.data.list？
这就是统一数据解包解决的第一个实际体验问题。
我们在 response 拦截器中判断如果服务端返回的结构含有 code === 200 或 code === 0，就直接 return data.data。
如果返回 code !== 200（比如余额不足、密码错误），拦截器自动弹窗提醒并 Promise.reject，页面层直接省略了大量的 if-else 样板代码。