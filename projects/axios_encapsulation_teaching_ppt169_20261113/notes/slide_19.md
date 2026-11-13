这段源码展示了著名的“计数器模型 (Counter Pattern)”。
我们声明一个全局变量 loadingCount，初始值为 0。
当第一个请求发出时，loadingCount 从 0 变成 1，立即开启遮罩；
后续请求到达时，只让 loadingCount++，不再重复创建遮罩；
当请求响应或者报错时，调用 hideLoading 让 loadingCount--；
只有当最后一个请求完成，loadingCount 彻底归零时，才真正调用 loadingInstance.close() 关闭遮罩！
这就彻底保证了无论有多少个并发异步请求，遮罩都能精准守护整个加载周期。