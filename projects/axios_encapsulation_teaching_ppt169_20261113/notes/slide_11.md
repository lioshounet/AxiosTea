这段代码是整个 Axios 封装最值钱的核心实现，大厂面试常要求现场手写。
大家看 else 分支：我们返回了一个既没有 resolve 也没有 reject 的 new Promise！
这个 Promise 的 resolve 触发权被移交给了 retryQueue 数组中的闭包回调函数。
由于 Promise 状态未决，外部业务调用的 await 就会一直处于挂起等待状态。
直到 then 回调中执行了 retryQueue.forEach(cb => cb(newToken))，所有被挂起的请求才会瞬间被唤醒并重发，对业务层完全透明！