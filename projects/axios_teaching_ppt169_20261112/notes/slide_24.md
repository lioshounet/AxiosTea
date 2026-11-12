文件名解析是前端下载里面一个历史悠久的深水区。
很多同学写下载，导出出来的文件名全是乱码，或者一遇到中文就变成下划线或者空串。
原因有两个：
第一，跨域时前端找不到 Content-Disposition，因为后端 CORS 没加 exposedHeaders: ['Content-Disposition']！
第二，现代后端按照 RFC 5987 标准，会返回 filename*=UTF-8''xxx。
我们的 download.ts 正则优先解析 UTF-8 编码串，解码出最真实的中文字符，彻底告别乱码。