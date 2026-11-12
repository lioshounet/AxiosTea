接下来进入核心要点三：请求取消与防重复请求。
很多早期的教程还在教大家使用 axios.CancelToken.source()。
如果面试时你还在答 CancelToken，面试官就知道你很久没有关注前端技术演进了。
Axios 官方从 v0.22 版本开始就全面废弃了 CancelToken，因为浏览器和 Node 原生引入了 AbortController 标准。
它通过将 controller.signal 传递给 config.signal，使得网络请求可以被干净、标准化地从外部中断。