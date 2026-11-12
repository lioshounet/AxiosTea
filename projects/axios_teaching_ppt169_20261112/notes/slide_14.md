要做到防重复请求，首先必须解决：如何判定两个请求是“重复”的？
单纯根据 URL 判断是不行的，比如 GET /api/user?id=1 和 GET /api/user?id=2 显然是两个不同的合法请求。
我们采用四维指纹公式：Method + URL + Params + Data。
我们将这四个维度严格序列化拼接为全局唯一的 String Key，存入 pendingMap 中。只要上一个 Key 还在 Map 里，就意味着前一个请求还没结束！