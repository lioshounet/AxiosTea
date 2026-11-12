现在进入核心要点六：文件上传与下载。
很多同学写上传时，习惯手动在 headers 里面写 Content-Type: multipart/form-data。
其实在现代浏览器中，使用 FormData 时可以完全不写这个标头，让浏览器自动识别，并且浏览器会自动生成带有 boundary 边界分隔符的标头。
更重要的是上传进度监听：Axios 底层基于 XMLHttpRequest 的 upload.onprogress，封装层对外暴露一个简洁的 onProgress 回调，让组件可以极为优雅地绑定进度条。