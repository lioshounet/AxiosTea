请大家看屏幕上的代码实现。
首先，Axios 官方在 v0.22.0 之后已经明确废弃了传统的 CancelToken，全面推荐使用标准的 AbortController。
我们在 addPendingRequest 中获取生成好的 requestKey。
如果 Map 里已经存在，直接拿出 controller 并调用 abort()，Axios 底层便会立即抛出 CanceledError 中断 XHR/Fetch；
接着我们 new 一个新的 AbortController，将其 signal 属性直接赋值给 config.signal，并存入 Map 备用。