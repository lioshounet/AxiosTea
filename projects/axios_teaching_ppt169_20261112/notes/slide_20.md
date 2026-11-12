在面向普通用户时，绝不能直接把 'Internal Server Error' 或者 'Network Error' 甩到界面上，这极具破坏性。
我们的封装层内置了一套状态码中文映射字典。
根据 HTTP status 进行模式匹配，转译为友好的中文通知。
同时，有些业务接口希望自己弹对话框或者在表单输入框下面标红，不希望全局弹出顶部 Toast。
我们在 AxiosRequestConfig 中拓展了 showErrorMessage: false 选项，只要传了这个参数，全局拦截器就静默不弹窗，把错误完整交给页面的 catch 分支。