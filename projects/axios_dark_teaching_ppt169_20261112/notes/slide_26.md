请看大屏幕上的 RFC 5987 标准。
现代浏览器和后端框架在处理非 ASCII 字符（如中文文件名）时，遵循的是 RFC 5987 协议标准。
服务端会在响应头中返回：filename*=utf-8''%E7%94%A8%E6%88%B7...
我们在 extractFileName 函数中使用正则表达式，优先匹配 filename*=utf-8'' 后面的内容，并使用 decodeURIComponent 进行解码。
如果匹配不到，再降级去匹配普通的 filename="fallback.xlsx"。这样无论在什么浏览器或操作系统上，导出的中文文件名都绝对不会出现任何乱码！