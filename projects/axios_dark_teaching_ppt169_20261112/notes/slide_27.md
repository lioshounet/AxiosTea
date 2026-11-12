这段代码是解决痛点 4 的终极神器，也是阿里、字节技术面非常热衷考察的亮点。
当接口报错时，后端通常会返回类似 { code: 5001, message: '数据量超过上限，请缩小查询范围' } 的 JSON。
但因为前端事先设置了 responseType: 'blob'，Axios 会无条件把这段 JSON 字符转成 Blob 对象传给业务层！
我们在响应拦截器中做了一个关键嗅探：检查 response.data.type 是否等于 'application/json'。
如果是，立即启动一个 FileReader，调用 readAsText(response.data) 将二进制数据异步读回文本，再用 JSON.parse 还原出后端的真实报错信息并弹窗提醒！
这样就彻底避免了把错误信息当成损坏文件下载到用户本地的尴尬故障。