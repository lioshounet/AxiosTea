大家看屏幕上的代码实现。
当请求在响应拦截器抛出 error 时，我们进入 handleResponseRetry 函数。
首先读取 config.retry 配置项，判断当前接口是否开启了重试。
如果开启了，我们在 config 对象上维护一个私有变量 __retryCount 作为计数器。
接着计算退避延迟时间：通过 Math.pow(2, count - 1) 算出翻倍时间。
然后构造一个由 setTimeout 包裹的 Promise 延迟链条，在定时器结束时再次调用 instance(config) 重新发出请求。
重试成功后，后续 then 照常接收数据，业务组件完全感知不到底层曾经历过一次险象环生的网络重试！