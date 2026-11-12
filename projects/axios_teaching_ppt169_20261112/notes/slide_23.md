很多同学经常问：下载文件直接用 a 标签的 href 或者 window.open 不就行了吗，为什么要大费周章用 Axios 去下载 Blob？
核心原因有两个：
第一，企业的导出接口通常是受保护的，必须在 HTTP Header 携带 Authorization: Bearer <Token>。window.open 根本无法在 Header 里加 Token！
第二，如果下载过程中数据库挂了，或者用户导出的数据量过大服务端报错，window.open 会直接在新标签页显示一个白屏或者生硬的 JSON，前端无法进行错误拦截和友好提示。