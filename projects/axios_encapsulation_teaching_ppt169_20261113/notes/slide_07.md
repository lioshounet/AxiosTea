请大家看屏幕上的核心源码。
我们在创建 service 实例时配置了通用的 baseURL 与 10 秒超时。
在请求拦截器中，我们做了三件事：
第一，检查本地是否存在 Token，通过 config.headers.set 安全注入 Bearer Token；
第二，判断当前接口是否开启防重复提交，调用 addPendingRequest 注册请求指纹；
第三，判断是否开启 Loading，调用 showLoading 递增计数器。
每一项功能都可以通过自定义配置项关闭，体现了极佳的灵活性。