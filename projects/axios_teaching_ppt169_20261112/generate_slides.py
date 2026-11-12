# -*- coding: utf-8 -*-
import os

project_dir = "c:/Users/Administrator/Desktop/Axios/projects/axios_teaching_ppt169_20261112"
svg_dir = os.path.join(project_dir, "svg_output")
notes_dir = os.path.join(project_dir, "notes")
os.makedirs(svg_dir, exist_ok=True)
os.makedirs(notes_dir, exist_ok=True)

# Colors from confirmed result.json
BG = "#FAF9F5"
CARD_BG = "#F1EFE8"
WHITE = "#FFFFFF"
DARK_PANEL = "#1E293B"
PRIMARY = "#8F2D56"
ACCENT = "#D81159"
TEAL = "#218380"
AMBER = "#FFBC42"
CYAN = "#73D2DE"
TEXT_DARK = "#2B2D42"
TEXT_MUTED = "#6C757D"
DIVIDER = "#E2DDD5"
GREEN = "#10B981"
RED = "#EF4444"

# Slide generator metadata
slides_content = [
    # 01
    {
        "role": "cover",
        "badge": "企业级前端工程化 · 架构实战",
        "title": "Axios 工业级深度封装与 TypeScript 架构实训",
        "kicker": "从原生痛点到生产级网络层基石建设",
        "lead": "Vue 3 + TypeScript + Pinia + Node.js Express 全套联动实践",
        "boxes": [
            ("统一解包", "响应拦截器剥离业务外壳，终结冗余 res.data.data", PRIMARY),
            ("双Token刷新", "401 拦截、isRefreshing 锁与并发请求队列重放防死锁", ACCENT),
            ("防重复连击", "AbortController 生成请求指纹，自动取消前序未完成请求", TEAL),
            ("计数器Loading", "并发安全 Counter 模型，解决布尔值导致的过早关闭与界面闪烁", AMBER),
            ("自动重试", "网络抖动与 503 超载下的智能指数退避重试 (Retry Pattern)", CYAN),
            ("Blob异常反解", "破解大厂高频面试坑：二进制流下载下的 JSON 错误解析", PRIMARY)
        ],
        "footer": "主讲人：Vue.js / 全栈架构讲师 · 课时：45分钟 · 源码全开源配套",
        "notes": """大家好！欢迎来到本期《Axios 工业级深度封装与 TypeScript 架构实战》深度讲座。
在现代前端工程开发和各类大厂中高级前端面试中，Axios 封装是一个绝不可少的经典考点。绝大多数初学者或初级开发者往往只写了一个简单的 axios.create 和基础请求拦截器，一旦进入生产环境的高并发场景、弱网环境、多文件导出或 Token 过期场景，系统就会暴露大量的偶发性 Bug。
今天我们将结合一套包含 Vue 3、TypeScript 与 Node.js Express 的完整工程，系统化拆解 6 大工业级核心封装模块，帮助大家建立起坚如磐石的网络层设计认知。"""
    },
    # 02
    {
        "role": "content",
        "badge": "课程体系大纲",
        "title": "为什么网络层封装是企业级前端的核心基石？",
        "kicker": "从裸奔到工业级：网络层决定了前端稳定性上限",
        "cards": [
            ("原生裸用缺陷", "无统一鉴权、无数据解包、无防重提交、下载异常无法捕获，代码充斥重复 try-catch 与判空。", RED),
            ("封装核心支柱", "六大模块分层治理：凭证注入、双Token队列、AbortController 取消、计数器遮罩、重试容灾、Blob容错。", TEAL),
            ("教学实训成果", "全量 TypeScript 声明合并强类型保护，配套 Node.js 后端与 Pinia 实时链路可视化监视器。", PRIMARY)
        ],
        "summary": "【核心目标】掌握高内聚、低耦合的网络层封装体系，彻底攻克大厂面试与生产架构难关。",
        "notes": """在正式进入代码之前，我们首先需要从宏观上审视网络层的战略定位。
前端视图层（Vue / React）的核心职责是状态渲染与用户交互，如果直接在每个组件内部调用裸的 axios 请求，业务代码就会与底层网络协议强耦合。
一旦后端微服务调整响应格式、接口更换鉴权方案、或者需要增加全局防抖，修改成本将呈几何级数放大。一个优秀的封装层，对外暴露纯净的 TypeScript 业务数据契约，对内包揽所有的异常恢复、流控制与环境适配。"""
    },
    # 03
    {
        "role": "content",
        "badge": "原生缺陷剖析",
        "title": "原生 Axios 在大型复杂应用下的七大致命痛点",
        "kicker": "这些生产环境的暗坑，你的代码中招了吗？",
        "grid4": [
            ("痛点 1：冗长多层解包", "原生包装 res.data，业务每处必须手写 res.data.data，极易引发运行时空指针。"),
            ("痛点 2：Token 刷新死锁", "401 时多个并发请求同时调用 /refresh，新旧 Token 竞态覆写导致鉴权失效。"),
            ("痛点 3：连击并发脏数据", "用户快速狂点提交按钮，前序请求未完成且重复提交，引发后端重复入库。"),
            ("痛点 4：Blob 错误文件劫持", "responseType: blob 时若后端报错返回 JSON，会被强转为损坏的空文件直接下载。")
        ],
        "summary": "【架构启示】网络层封装的本质，是对原生网络交互脆弱性的全面工程兜底。",
        "notes": """这里总结了业界在没有严格封装时最常踩的七个坑中的前四个核心问题。
大家注意痛点二和痛点四，这是大厂技术面最喜欢抓细节深问的地方。
很多同学以为加个 axios.interceptors.response 就算封装完了，结果一遇到并发接口过期，浏览器瞬间轰出 5 个刷新请求，服务端直接判定非法操作。今天我们就是要针对这些痛点，给出经过万级并发验证的标准工业解法。"""
    },
    # 04
    {
        "role": "content",
        "badge": "架构全景设计",
        "title": "分层解耦的 TS + Axios 工业级网络层体系全景",
        "kicker": "职责单一、高内聚低耦合的四层分层模型",
        "layers": [
            ("1. 业务应用层 (API Services)", "auth.ts / user.ts / test.ts / file.ts —— 面向视图组件提供强类型函数契约"),
            ("2. 封装核心层 (Request Core)", "request.ts —— 组装主 service 与轻量 refreshService，串联双向拦截器流水线"),
            ("3. 通用工具层 (Modular Utilities)", "cancel.ts (AbortController) · loading.ts (计数器) · retry.ts (重试) · download.ts (流解析) · token.ts"),
            ("4. 支撑服务层 (Mock & Observability)", "Node.js Express 教学后端 + Pinia Logger 实时拦截器执行链路控制台")
        ],
        "summary": "【架构原则】各模块职责独立，工具层无视图依赖，核心层通过拦截器聚合全局能力。",
        "notes": """请看大屏幕上的系统架构全景图。
我们在 client/src 目录下并没有将成百上千行代码堆死在一个 request.js 里，而是采用了清晰的分层解耦设计：
底层是独立的工具模块，如基于 AbortController 的 cancel.ts、基于计数器模型的 loading.ts、失败退避重试的 retry.ts；
核心层 request.ts 负责将这些独立工具像插拔插件一样挂载到 Axios 的请求和响应拦截器上；
顶层的业务 API 模块则只关心输入参数与输出类型，实现完全的职责分离。"""
    },
    # 05
    {
        "role": "content",
        "badge": "核心要点一 · 实例基线",
        "title": "Axios 实例配置哲学：baseURL、超时与实例隔离",
        "kicker": "打造标准化、易维护的多环境请求基线",
        "cards": [
            ("baseURL 优雅配置", "结合 import.meta.env.VITE_APP_BASE_API 与 Vite 本地代理 /api，兼顾本地跨域与生产上线。", TEAL),
            ("超时时间安全底线", "配置 timeout: 10000 (10秒)，避免因移动端弱网或接口挂起导致浏览器连接池占满耗尽。", PRIMARY),
            ("多实例隔离红线", "创建业务主 service 实例与轻量 refreshService 实例，杜绝 401 拦截死循环。", ACCENT)
        ],
        "summary": "【关键细节】绝不直接修改全局 axios 默认对象，保证微前端或第三方组件请求不受污染。",
        "notes": """现在我们深入核心要点一：实例创建与配置基线。
首先，永远不要直接在全局 axios 对象上挂载拦截器！因为如果你的项目以后接入微前端（如 qiankun）或者引入了第三方 SDK，全局修改会导致所有第三方请求被意外污染。
其次，为什么我们要单独声明一个 refreshService？因为在后续讲解双 Token 无感刷新时，如果刷新接口本身发生 401，主实例的拦截器会再次拦截并重新发起刷新，从而引发灾难性的死循环递归爆栈！"""
    },
    # 06
    {
        "role": "content",
        "badge": "核心要点一 · 管道模型",
        "title": "拦截器双向管道模型：请求发起与响应收拢生命周期",
        "kicker": "洋葱模型切面治理，实现关注点清晰分离",
        "steps": [
            ("1. 业务触发", "组件调用 api()", "携带业务参数与自定义配置 (如 showLoading: true)"),
            ("2. 请求拦截器", "Request Pipeline", "注入 Authorization Bearer Token -> 注册防重指纹 -> 触发 Loading 计数"),
            ("3. 网络传输", "HTTP Transport", "浏览器底层通过 XMLHttpRequest / Fetch 发出网络包"),
            ("4. 响应拦截器", "Response Pipeline", "注销 Pending 指纹 -> 扣减 Loading -> 校验业务 code 统一解包 -> 侦测 Blob"),
            ("5. 结果交付", "Promise Resolve", "视图层直接拿到纯净业务 data，异常则进入统一 catch 分支")
        ],
        "summary": "【拦截器哲学】把所有与 UI 视图无关的网络底层脏活，全闭环拦截在管道内部。",
        "notes": """这张时序图展示了请求在拦截器流水线中的完整生命周期。
大家可以把拦截器想象成机场的安全检查通道：
在登机前（请求拦截器），安检人员帮你盖上签证印章（注入 Bearer Token）、登记防重名单、通知地面服务准备。
在到达目的地后（响应拦截器），海关人员帮你核验包裹（解析业务状态码）、若发现违禁品直接拦截并报警（抛出业务异常）、正常行李则直接送到你手上。"""
    },
    # 07
    {
        "role": "content",
        "badge": "核心要点一 · 数据解包",
        "title": "统一业务解包机制：让业务层少写一层 .data.data",
        "kicker": "终结冗余取值，统一业务状态码处理",
        "code_compare": (
            "原生 Axios 编写方式 (繁琐脆弱)",
            "const res = await axios.get('/api/user');\nif (res.data && res.data.code === 200) {\n  this.user = res.data.data;\n} else {\n  ElMessage.error(res.data.message);\n}",
            "封装后企业级编写方式 (清爽精准)",
            "// request.ts 响应拦截器自动解包\nif (data.code === 200) return data.data;\n\n// 页面直接使用，配合 TS 精准提示\nconst user = await getUserProfileApi();\nconsole.log(user.username, user.role);"
        ),
        "summary": "【收益】解包层同时过滤了业务异常 (如 code === 5001)，业务页面只需关注成功逻辑。",
        "notes": """很多初学者经常抱怨：为什么 Axios 拿到的数据总有一层 data，我们要写 res.data.data 甚至 res.data.data.list？
这就是统一数据解包解决的第一个实际体验问题。
我们在 response 拦截器中判断如果服务端返回的结构含有 code === 200 或 code === 0，就直接 return data.data。
如果返回 code !== 200（比如余额不足、密码错误），拦截器自动弹窗提醒并 Promise.reject，页面层直接省略了大量的 if-else 样板代码。"""
    },
    # 08
    {
        "role": "content",
        "badge": "核心要点二 · 双Token",
        "title": "核心要点二：双 Token (Access + Refresh) 鉴权设计哲学",
        "kicker": "安全防窃密与平滑用户体验的极致平衡",
        "cards": [
            ("Access Token (短期凭据)", "有效期极短 (如 15秒教学测试 / 生产15分钟)，作为 Bearer 鉴权凭证随每个请求发送。被截获后窗口极小。", PRIMARY),
            ("Refresh Token (长期凭据)", "有效期长 (如 7天 / 30天)，仅用于在 AccessToken 过期后置换新凭证。不参与日常业务请求，暴露面小。", TEAL),
            ("无感刷新终极目标", "用户在操作过程中不需要中途被迫退出重新输入密码，系统在后台自动置换凭证并重发，全程无感知。", AMBER)
        ],
        "summary": "【安全规范】单 Token 有效期设太长容易被黑客重放攻击，设太短会导致用户频繁被踢出登录。",
        "notes": """现在进入大家非常关心的核心重难点——双 Token 无感刷新机制。
为什么大厂和现代企业级系统普遍推崇双 Token 架构？
如果只用一个 Token，把过期时间设为 7 天，一旦该 Token 在客户端被跨站脚本或者抓包截获，黑客在整整 7 天内都能冒充该用户发起请求！
如果把 Token 设为 15 分钟，用户填写一个长表单，写了 16 分钟点击提交，系统直接报错 401 把用户踢回登录页，用户辛苦填写的几百项数据瞬间丢失，体验极差！
双 Token 正是解决这一矛盾的业界最优标准解。"""
    },
    # 09
    {
        "role": "content",
        "badge": "核心要点二 · 凭证生命周期",
        "title": "双 Token 协同流转时序与无缝鉴权演进",
        "kicker": "全生命周期状态流转图解",
        "steps": [
            ("阶段 1：初次登录", "POST /api/auth/login", "后端返回 accessToken (15s) + refreshToken (7d)，存入 LocalStorage"),
            ("阶段 2：正常请求", "Bearer AccessToken", "每次业务请求自动注入短期 Token，服务端验签通过正常返回"),
            ("阶段 3：凭证过期", "HTTP 401 Unauthorized", "AccessToken 过期，服务端拒绝访问返回 401，拦截器捕获此事件"),
            ("阶段 4：无感换发", "POST /api/auth/refresh", "前端拦截器使用 RefreshToken 置换出新凭证对，静默更新本地存储"),
            ("阶段 5：原样重放", "Re-dispatch Request", "更新原请求 Authorization 标头并重新发送，用户全程无任何察觉")
        ],
        "summary": "【体验保障】我们在配套后端中将 Access Token 设为 15 秒，右上角带倒计时，方便学员直观验证。",
        "notes": """请大家看这个状态流转时序。
当 Access Token 在第 15 秒过期之后，用户发起下一个请求，服务端会准确返回 401。
传统的粗暴做法是直接清空 Token 跳转 /login，而我们在这里切入了一套静默置换流程。
请注意阶段 4 和阶段 5：请求并没有被直接判死刑，它被拦截器暂时扣留，拦截器在背后悄悄调通刷新接口拿到新钥匙，换上新钥匙后再把原请求重新投递出去。整个过程毫秒级完成，用户界面毫无波澜。"""
    },
    # 10
    {
        "role": "content",
        "badge": "核心要点二 · 单请求刷新",
        "title": "单请求 401 拦截与自动换 Token 重发代码实战",
        "kicker": "响应错误拦截器中的关键拦截与异步重放",
        "code_highlight": (
            "request.ts 响应错误拦截器核心片段",
            "if (response && response.status === 401 && config) {\n  const refreshToken = getRefreshToken();\n  if (!refreshToken) return handleLogout();\n\n  // 1. 开启无感刷新\n  isRefreshing = true;\n  const { data } = await refreshService.post('/api/auth/refresh', { refreshToken });\n  setTokens(data.data); // 持久化新 Token\n\n  // 2. 注入新 Token 并重新派发原本被拦截的请求\n  config.headers.set('Authorization', `Bearer ${data.data.accessToken}`);\n  return service(config); // 重放原请求！\n}"
        ),
        "summary": "【核心技巧】使用 return service(config) 将重发后的请求 Promise 直接返回给最初的调用方。",
        "notes": """让我们看这几行核心代码。
很多同学写重发请求时，以为直接在拦截器里调用一遍 service(config) 就行了，但忘记了将 return service(config) 返回出去！
必须 return 这个新生成的 Promise，最初在 Vue 组件里 await 的代码才能接收到重发成功后的真实数据。
不过请大家思考一个致命问题：如果当前页面一口气并发触发了 5 个请求，而此时 Token 恰好过期了，会发生什么？接下来我们看大厂面试最硬核的并发死锁问题！"""
    },
    # 11
    {
        "role": "content",
        "badge": "核心要点二 · 并发防死锁",
        "title": "高并发 401 避坑：请求队列挂起与批量唤醒防死锁",
        "kicker": "大厂技术面最核心的高并发网络考点",
        "queue_model": [
            ("并发请求同时报 401", "页面加载时 UserInfo, Orders, Notifications 同时到达，均收到 401", RED),
            ("全局锁 isRefreshing", "首个 401 将 isRefreshing 设为 true，确保全局仅发 1 次 /refresh 请求", AMBER),
            ("请求队列 retryQueue", "后续 401 请求被包装为 Promise 塞入队列挂起：retryQueue.push((newToken) => ...)", TEAL),
            ("广播唤醒与重放", "Token 刷新成功后，批量遍历 retryQueue 注入新 Token 唤醒，最后重放首个请求", GREEN)
        ],
        "summary": "【考点精髓】没有队列机制，5 个并发请求将引发 5 次刷新，由于 RefreshToken 刷新后旧的立即作废，引发严重竞态覆盖！",
        "notes": """这是整个网络层封装含金量最高、也是大厂面试淘汰率最高的一个考点。
如果页面有 5 个请求同时报 401，若不加控制，浏览器会几乎同时向后端发送 5 个 /refresh 接口。
很多严格的安全策略是：Refresh Token 每次换发后，旧的立即失效！
那么第一个刷新请求成功了，第二个刷新请求携带旧凭证到达，后端直接判定是非法凭证，强制将用户踢下线！
我们的解法是：全局布尔锁 isRefreshing + 数组队列 retryQueue。
后面的请求不发网络请求，而是挂起为一个待唤醒的 Promise。刷新成功一次，广播唤醒整队重放！"""
    },
    # 12
    {
        "role": "content",
        "badge": "核心要点二 · 实例隔离",
        "title": "为什么刷新 Token 严禁使用主 Axios 实例？",
        "kicker": "架构红线：警惕拦截器内部递归调用造成的死循环爆栈",
        "cards": [
            ("错误做法 (主实例调用)", "在 401 拦截器内部调用 service.post('/api/auth/refresh')。\n后果：若 refreshToken 也失效过期，refresh 接口自身也返回 401，主实例拦截器将再次拦截并再次发起 refresh，直接陷入无限死循环！", RED),
            ("正确做法 (独立轻量实例)", "单独实例化 const refreshService = axios.create()，不挂载任何 401 响应拦截器。\n效果：若 refresh 接口失败直接 reject，中断流程，清空本地凭证并引导跳转登录，系统平稳降级。", GREEN)
        ],
        "summary": "【红线铁律】网络层内部辅助性请求，绝不能继承包含重试或重定向逻辑的业务拦截器。",
        "notes": """请大家在架构笔记本上记下这条红线：
在拦截器内部发起的辅助请求，千万不要用主 service 实例！
如果你的 Refresh Token 7 天到了也过期了，后端对 /refresh 接口必然返回 401。
如果你用了主 service，拦截器发现 401，又去调 /refresh，又报 401……浏览器控制台瞬间刷出几百上千条网络请求，直接把浏览器卡死甚至把鉴权服务器打崩！
所以我们必须专门 new 一个干净的 refreshService，这是架构防御性设计的典范。"""
    },
    # 13
    {
        "role": "content",
        "badge": "核心要点三 · 取消机制",
        "title": "核心要点三：从废弃的 CancelToken 到现代 AbortController",
        "kicker": "拥抱现代 Web 标准 API 的技术演进",
        "cards": [
            ("历史方案：CancelToken (已废弃)", "Axios 自 v0.22.0 起正式弃用 CancelToken。旧方案基于内部闭包机制，侵入性强，不符合标准规范，无法与 Fetch 或 Node 原生 API 互通。", TEXT_MUTED),
            ("现代标准：AbortController", "W3C 标准 Web API，浏览器与 Node.js 现代环境全面原生内置。通过 controller.signal 信号量与请求解耦，支持跨框架与流式通信。", TEAL),
            ("封装收益", "通过标准 AbortController 管理未完成请求，可轻松实现防重复连击、路由页面销毁批量取消及手动中断。", PRIMARY)
        ],
        "summary": "【面试加分项】面试官如果问取消请求，主动提出 CancelToken 的废弃原因与 AbortController 的标准规范优势。",
        "notes": """接下来进入核心要点三：请求取消与防重复请求。
很多早期的教程还在教大家使用 axios.CancelToken.source()。
如果面试时你还在答 CancelToken，面试官就知道你很久没有关注前端技术演进了。
Axios 官方从 v0.22 版本开始就全面废弃了 CancelToken，因为浏览器和 Node 原生引入了 AbortController 标准。
它通过将 controller.signal 传递给 config.signal，使得网络请求可以被干净、标准化地从外部中断。"""
    },
    # 14
    {
        "role": "content",
        "badge": "核心要点三 · 请求指纹",
        "title": "请求唯一指纹生成机理：精准识别重复点击",
        "kicker": "四维哈希生成全局唯一请求指纹",
        "formula": "[Method, URL, JSON.stringify(params), JSON.stringify(data)].join('&')",
        "grid4": [
            ("Method (请求方法)", "GET / POST / PUT / DELETE，确保不同 HTTP 动词独立区分。"),
            ("URL (接口路径)", "请求目标服务端路径，如 /api/user/profile。"),
            ("Params (查询参数)", "GET 请求 URL Query 参数对象，通过 JSON.stringify 统一序列化。"),
            ("Data (请求体参数)", "POST / PUT 请求载荷对象，通过 JSON.stringify 抹平对象引用差异。")
        ],
        "summary": "【管理中心】Map<string, AbortController> 统一存储当前处于 pending 状态的请求指纹。",
        "notes": """要做到防重复请求，首先必须解决：如何判定两个请求是“重复”的？
单纯根据 URL 判断是不行的，比如 GET /api/user?id=1 和 GET /api/user?id=2 显然是两个不同的合法请求。
我们采用四维指纹公式：Method + URL + Params + Data。
我们将这四个维度严格序列化拼接为全局唯一的 String Key，存入 pendingMap 中。只要上一个 Key 还在 Map 里，就意味着前一个请求还没结束！"""
    },
    # 15
    {
        "role": "content",
        "badge": "核心要点三 · 防手抖实战",
        "title": "连续手抖狂点防护：自动中断前序正在 pending 的请求",
        "kicker": "只认最后一次有效操作，从源头杜绝并发脏数据",
        "steps": [
            ("步骤 1：请求拦截器查重", "addPending(config)", "根据指纹计算 Key，查询 pendingMap 中是否已存在相同 Key"),
            ("步骤 2：自动中断前序请求", "controller.abort()", "若已存在，直接调用旧 controller.abort() 取消前序未响应请求并移出 Map"),
            ("步骤 3：绑定新信号量", "config.signal = new.signal", "为当前新请求创建全新 AbortController，存入 Map 并继续执行"),
            ("步骤 4：响应拦截器清理", "removePending(config)", "无论请求成功还是失败，在响应完成时均从 Map 中安全注销指纹"),
            ("步骤 5：静默错误处理", "axios.isCancel(error)", "捕获取消错误静默 reject，不弹红框骚扰用户，控制台打出警告")
        ],
        "summary": "【实测效果】在我们的控制台连续狂点 5 次耗时接口，前 4 次秒级被取消，仅最后 1 次完成！",
        "notes": """请看防手抖狂点的实战流程。
日常开发中，前端哪怕加了按钮 loading，用户手速快或者双击也会造成重复提交。
在网络层做防重拦截，即使按钮没有加防抖，只要前一个相同的请求还在 pending，新的相同请求一进来，拦截器立刻把上一个 abort 掉。
特别注意步骤 5：当一个请求被 abort 取消后，Axios 会抛出一个 CanceledError。
我们在错误拦截器中必须用 axios.isCancel(error) 捕获，静默处理，绝对不能弹红色报错说“请求失败”，因为这属于正常的防御性取消。"""
    },
    # 16
    {
        "role": "content",
        "badge": "核心要点三 · 豁免与销毁",
        "title": "慢速请求手动取消与批量并发豁免配置 (cancelDuplicate)",
        "kicker": "兼顾高防护与特化业务诉求的弹性架构设计",
        "cards": [
            ("并发豁免配置 (cancelDuplicate: false)", "在大文件切片并发上传、或批量保存多张表格等合法并发场景下，单请求传入 cancelDuplicate: false，跳过防重，允许同时发起相同接口。", TEAL),
            ("耗时接口手动中断 (Abort on Demand)", "在报表大数据导出或长轮询查询时，提供主动中断按钮，调用 clearAllPending() 立即切断网络连接，释放浏览器连接池。", AMBER),
            ("路由守卫自动清理 (SPA 内存泄漏防护)", "Vue Router beforeEach 钩子中执行 clearAllPending()，页面离开时将所有未完成请求全部取消，防止组件销毁后更新状态报错。", PRIMARY)
        ],
        "summary": "【架构弹性】好的封装绝不是一刀切，必须支持单请求细粒度配置覆盖与全局生命周期控制。",
        "notes": """很多同学在封装防重复请求时，做成了一刀切，结果业务场景里要批量上传 5 个分片，前面 4 个全被防重复取消了！
所以我们的 cancel.ts 支持单请求参数配置：
传入 cancelDuplicate: false，拦截器就会完全放行并发。
同时，我们在 SPA 单页应用中，用户切路由切换页面了，前一个页面还在拉取几十条数据。
这时候在路由守卫里调用一下 clearAllPending()，既减轻了服务器压力，又避免了异步回调执行时组件已卸载引发的内存泄漏。"""
    },
    # 17
    {
        "role": "content",
        "badge": "核心要点四 · Loading缺陷",
        "title": "核心要点四：全屏 Loading 遮罩的布尔值并发致命缺陷",
        "kicker": "为什么简单的 isLoading = true / false 在生产中行不通？",
        "timeline_flaw": [
            ("0ms: 并发启动", "页面同时触发 Request A (耗时100ms) 与 Request B (耗时2000ms)，全局 loading 置为 true"),
            ("100ms: A 率先返回", "Request A 响应完毕，拦截器简单粗暴执行 loading = false，关闭全局 Loading 遮罩！"),
            ("100ms ~ 2000ms: 裸奔空窗期", "此时 Request B 仍在网络传输中！界面失去遮罩，用户以为加载已结束，开始乱点界面"),
            ("致命故障", "用户重复点击造成重复提交，且若此时发起新请求又触发 loading=true，界面产生严重频闪！")
        ],
        "summary": "【痛点总结】布尔变量无法感知并发请求的生命周期重叠，最早返回的请求会提前扼杀遮罩。",
        "notes": """现在进入核心要点四：全屏 Loading 控制器设计。
我们在很多初级封装里都会看到这样的代码：
请求拦截器里 loading = true，响应拦截器里 loading = false。
这就是典型的“单请求思维”。
在现代应用中，一个页面进入时往往同时调 3 个以上接口。最快的那个接口 100ms 返回了，直接把 loading 关了，剩下两个接口还在转，用户看界面闪了一下以为加载完了，开始狂点按钮，整个状态就彻底乱了。"""
    },
    # 18
    {
        "role": "content",
        "badge": "核心要点四 · 计数器模型",
        "title": "计数器模型 (Counter Pattern) 打造并发安全零闪烁 Loading",
        "kicker": "优雅的计数器算法与防抖延时平滑关闭",
        "counter_steps": [
            ("计数器初始化", "let loadingCount = 0;", "维护全局唯一的活跃请求计数器"),
            ("请求发起递增", "loadingCount++", "若此时递增到 1，正式唤起全局 ElLoading.service 遮罩"),
            ("响应完成递减", "loadingCount--", "无论请求成功还是异常，只要结束即执行递减"),
            ("归零安全关闭", "if (loadingCount === 0)", "通过 setTimeout(100ms) 延时关闭，抹平极短微请求带来的视觉频闪")
        ],
        "summary": "【配置开关】支持单请求通过 showLoading: true 按需开启，既可静默无感，亦可全屏遮罩。",
        "notes": """解决并发 Loading 的正解是：计数器模型 (Counter Pattern)。
我们定义一个 loadingCount 变量。
每来一个需要展示 loading 的请求，计数器加 1。当计数器从 0 变成 1 的那一刻，我们呼出全屏 Loading。
每结束一个请求，计数器减 1。只有当计数器彻底减回 0 的时候，说明当前所有的并发请求都收工了，我们才去关闭遮罩。
我们在归零时还加了一个 100ms 的 setTimeout，用来抵消相邻极短微请求之间的微小缝隙，彻底消除了界面闪烁。"""
    },
    # 19
    {
        "role": "content",
        "badge": "核心要点五 · 双轨错误体系",
        "title": "核心要点五：双轨错误体系——业务逻辑错误 vs HTTP协议错误",
        "kicker": "清晰划分两套截然不同的错误责任边界",
        "cards": [
            ("1. 业务逻辑状态码 (Business Error)", "HTTP 状态码是 200，但返回数据内部包含 code !== 200 (如 code: 5001 余额不足、密码错误)。由响应拦截器成功分支解包层统一 ElMessage.error 提示，并 Promise.reject。", TEAL),
            ("2. HTTP 协议状态码 (Protocol Error)", "由网络层、反向代理或网关抛出的协议错误 (如 401 未授权、403 权限不足、404 地址不存在、500 服务宕机)。由响应错误拦截器捕获并分发处理。", PRIMARY),
            ("3. 网络异常与超时 (Network Error)", "断网、DNS 解析失败或 timeout 超时。无服务端响应对象，需单独捕获提示并视情况触发自动重试机制。", RED)
        ],
        "summary": "【原则】两套错误体系绝不可混杂，职责分明才能保证错误提示精准无遗漏。",
        "notes": """很多同学在写拦截器时，把业务错误和 HTTP 错误写成了一锅粥。
大家必须分清前端面临的两套错误体系：
第一套是业务逻辑错误，HTTP 是 200，因为网络链路是通的，但后端业务代码检查出用户余额不足，返回 { code: 5001, message: '余额不足' }。这个必须在 response 成功拦截器里处理！
第二套是 HTTP 协议错误，比如 403 没权限、500 服务器代码报空指针崩溃了、或者 503 网关超载。这个是在 response 错误拦截器里处理的。"""
    },
    # 20
    {
        "role": "content",
        "badge": "核心要点五 · 状态码映射",
        "title": "全局 HTTP 状态码友好中文映射与全局分发",
        "kicker": "将生硬晦涩的英文协议转译为通俗易懂的中文反馈",
        "grid4": [
            ("400 Bad Request", "客户端请求语法错误或参数不合法，提示检查输入。"),
            ("403 Forbidden", "抱歉，您的账号没有权限访问该受保护资源。"),
            ("404 Not Found", "请求的后端接口地址不存在，提示联系管理员。"),
            ("500 / 502 / 504", "服务器内部发生错误、网关异常或网关响应超时。")
        ],
        "summary": "【静默机制】支持配置 showErrorMessage: false，针对业务自行捕获并定制 UI 的场景提供静默能力。",
        "notes": """在面向普通用户时，绝不能直接把 'Internal Server Error' 或者 'Network Error' 甩到界面上，这极具破坏性。
我们的封装层内置了一套状态码中文映射字典。
根据 HTTP status 进行模式匹配，转译为友好的中文通知。
同时，有些业务接口希望自己弹对话框或者在表单输入框下面标红，不希望全局弹出顶部 Toast。
我们在 AxiosRequestConfig 中拓展了 showErrorMessage: false 选项，只要传了这个参数，全局拦截器就静默不弹窗，把错误完整交给页面的 catch 分支。"""
    },
    # 21
    {
        "role": "content",
        "badge": "核心要点五 · 自动退避重试",
        "title": "网络抖动与 503 故障：接口智能指数退避重试机制",
        "kicker": "大幅增强移动端弱网与微服务扩缩容时的系统健壮性",
        "cards": [
            ("严格的重试准入条件", "严禁重试 4xx 客户端错误 (参数错误、401、404)！\n仅允许重试：网络中断断网、ECONNABORTED 超时、以及 502/503 临时不可用错误。", RED),
            ("重试参数灵活配置", "在请求配置中注入 retryCount: 3 (最大重试次数) 与 retryDelay: 1000 (重试间隔毫秒)。内部使用 __retryCount 进行尝试计数。", TEAL),
            ("信号量重置关键避坑", "重试前必须检查并清理旧请求上的 config.signal，避免因沿用已 aborted 的旧信号量导致重试直接被取消！", AMBER)
        ],
        "summary": "【实战验证】配套后端提供 /api/test/retry 接口，前 2 次故意报 503，第 3 次自动重试成功！",
        "notes": """自动重试机制是企业级网络层高可用建设的关键一环。
当移动端处于电梯里网络偶发断流、或者后端 K8s 正在重启微服务临时抛出 503 时，如果直接弹错，用户就必须手动刷新整个网页。
如果在网络层自动重试 3 次，很多偶发抖动就在用户无感知的情况下自动恢复了。
但大家注意准入条件：绝不能重试 400、401、404 这些逻辑错误！因为参数写错了重试 100 遍依然是错的，只会白白增加服务器压力。
我们还特别注意了重试前要清理旧的 signal，防止被当成取消请求处理。"""
    },
    # 22
    {
        "role": "content",
        "badge": "核心要点六 · 文件上传",
        "title": "核心要点六：文件上传机制与 onUploadProgress 实时监听",
        "kicker": "掌握 FormData 标准上传与进度百分比联动",
        "cards": [
            ("FormData 数据载荷组装", "const formData = new FormData(); formData.append('file', file);\n通过 multipart/form-data 标头传输二进制大文件，浏览器自动补充 boundary 边界串。", TEAL),
            ("onUploadProgress 原生监听", "Axios 支持传入 onUploadProgress 回调函数，通过 (progressEvent.loaded * 100) / progressEvent.total 精准计算上传进度百分比。", PRIMARY),
            ("UI 组件平滑绑定", "将计算得出的 percent 实时驱动 Element Plus 的 el-progress 组件，呈现丝滑平稳的进度条动画。", AMBER)
        ],
        "summary": "【体验升维】大文件上传绝不应该让用户面对静止的转圈，实时的进度百分比是核心体验指标。",
        "notes": """现在进入核心要点六：文件上传与下载。
很多同学写上传时，习惯手动在 headers 里面写 Content-Type: multipart/form-data。
其实在现代浏览器中，使用 FormData 时可以完全不写这个标头，让浏览器自动识别，并且浏览器会自动生成带有 boundary 边界分隔符的标头。
更重要的是上传进度监听：Axios 底层基于 XMLHttpRequest 的 upload.onprogress，封装层对外暴露一个简洁的 onProgress 回调，让组件可以极为优雅地绑定进度条。"""
    },
    # 23
    {
        "role": "content",
        "badge": "核心要点六 · 流下载",
        "title": "二进制流下载：responseType: 'blob' 与内存释放清理",
        "kicker": "具备鉴权能力与错误拦截的高级流式下载",
        "steps": [
            ("1. 发起请求", "responseType: 'blob'", "声明接收二进制大对象 Blob，Axios 将底层二进制数据包装为 Blob 实例"),
            ("2. 内存映射", "URL.createObjectURL(blob)", "为内存中的 Blob 生成一个形如 blob:http://... 的专属虚拟访问路径"),
            ("3. 动态触发", "document.createElement('a')", "创建不可见的 <a> 标签，绑定 href 与 download 文件名属性并触发 click()"),
            ("4. 释放内存", "URL.revokeObjectURL(blobUrl)", "通过 setTimeout 及时销毁虚拟对象 URL，释放浏览器内存，防止大量导出导致内存膨胀")
        ],
        "summary": "【为什么不用 window.open】window.open 无法携带 Bearer Token 进行鉴权，且下载出错时无法拦截提示！",
        "notes": """很多同学经常问：下载文件直接用 a 标签的 href 或者 window.open 不就行了吗，为什么要大费周章用 Axios 去下载 Blob？
核心原因有两个：
第一，企业的导出接口通常是受保护的，必须在 HTTP Header 携带 Authorization: Bearer <Token>。window.open 根本无法在 Header 里加 Token！
第二，如果下载过程中数据库挂了，或者用户导出的数据量过大服务端报错，window.open 会直接在新标签页显示一个白屏或者生硬的 JSON，前端无法进行错误拦截和友好提示。"""
    },
    # 24
    {
        "role": "content",
        "badge": "核心要点六 · 文件名解码",
        "title": "从 Content-Disposition 响应头解码 RFC 5987 标准中文文件名",
        "kicker": "跨浏览器彻底攻克导出文件名中文乱码与截断难题",
        "cards": [
            ("CORS 标头暴露 (后端必须配置)", "默认情况下浏览器跨域脚本只能读取通用 Header。后端必须配置 exposedHeaders: ['Content-Disposition']，前端才能读取到文件名标头！", RED),
            ("RFC 5987 现代 UTF-8 编码", "优先正则匹配 filename*=UTF-8''%E4%B8%AD%E6%96%87.txt，通过 decodeURIComponent 解码，完美支持任意复杂中文与特殊字符。", GREEN),
            ("兼容传统引号模式与保底", "兼顾匹配传统 filename=\"xxx.txt\" 格式，若后端未提供则使用时间戳保底文件名，保证下载永不落空。", TEAL)
        ],
        "summary": "【避坑清单】RFC 5987 标准是目前全球各大浏览器对于非 ASCII 文件名的唯一官方标准解。",
        "notes": """文件名解析是前端下载里面一个历史悠久的深水区。
很多同学写下载，导出出来的文件名全是乱码，或者一遇到中文就变成下划线或者空串。
原因有两个：
第一，跨域时前端找不到 Content-Disposition，因为后端 CORS 没加 exposedHeaders: ['Content-Disposition']！
第二，现代后端按照 RFC 5987 标准，会返回 filename*=UTF-8''xxx。
我们的 download.ts 正则优先解析 UTF-8 编码串，解码出最真实的中文字符，彻底告别乱码。"""
    },
    # 25
    {
        "role": "content",
        "badge": "核心要点六 · Blob异常避坑",
        "title": "大厂高频坑：Blob 导出异常时 JSON 报错文本反解与拦截",
        "kicker": "经典高频面试题：responseType 为 blob 时后端报错如何处理？",
        "cards": [
            ("踩坑现场 (原生致命缺陷)", "前端配置了 responseType: 'blob'。后端导出失败报 500 返回 JSON: {\"code\":5005,\"message\":\"数据已被锁定\"}。\nAxios 依然把这串 JSON 强制打包为 Blob！若直接保存，用户会下载一个内容是错误文本但后缀为 .xlsx 的损坏文件！", RED),
            ("工业级破解方案 (Blob 侦测反解)", "响应拦截器检查 data.type === 'application/json' 或 Content-Type 包含 json。\n通过 await (data as Blob).text() 读取出原始字符串，执行 JSON.parse，弹出真实业务错误提示并 reject！", GREEN)
        ],
        "summary": "【面试王炸】在面试官问到文件下载时，主动说出这个坑点和解决方案，技术评分瞬间拉满！",
        "notes": """请大家一定要重点看这一页，这是大厂技术面几乎百试不爽的一个“绝杀题”。
面试官问你：你平时用 Axios 下载文件，responseType 设成了 blob，如果后端接口报错了，你怎么给用户提示？
90% 的应聘者都不知道这个坑：因为你告诉 Axios 要接收 blob，所以哪怕后端返回的是 500 报错 JSON 字符串，Axios 也会死心塌地把它当成二进制文件包在 Blob 里！
如果你不反解，浏览器就会默默把这串报错 JSON 下载成一个打不开的破损 Excel 文件！
我们的拦截器通过读取 data.type 和 await data.text()，精准把隐蔽的 JSON 抓出来弹窗报警，这是极其精妙的工程实践。"""
    },
    # 26
    {
        "role": "content",
        "badge": "TypeScript 架构",
        "title": "TypeScript 进阶：声明合并 (Module Augmentation) 扩展 AxiosRequestConfig",
        "kicker": "打造丝滑的 IDE 智能补全与编译期强类型守护",
        "code_highlight": (
            "client/src/types/axios.d.ts 声明合并核心语法",
            "import 'axios';\n\ndeclare module 'axios' {\n  export interface AxiosRequestConfig {\n    cancelDuplicate?: boolean;     // 是否防重复取消\n    showLoading?: boolean;         // 是否全屏遮罩\n    loadingText?: string;          // 加载提示文案\n    showErrorMessage?: boolean;    // 是否全局弹窗\n    retryCount?: number;           // 失败重试次数\n    retryDelay?: number;           // 重试延时间隔\n    __retryCount?: number;         // 内部重试计数\n  }\n}"
        ),
        "summary": "【类型安全】通过声明合并，团队内任何人在调用 request() 时均能获得完整的智能补全与类型检查。",
        "notes": """现在进入 TypeScript 架构重构部分。
我们在 request.ts 里面加了 cancelDuplicate、showLoading 这些自定义配置。
很多初学者如果不会写声明合并，在 TS 项目里就会满屏报红，说 AxiosRequestConfig 上不存在这些属性，于是只能无奈地写 (config as any)。
在企业级规范中，这是绝对不被允许的！
我们在 types/axios.d.ts 里使用了 declare module 'axios' 的声明合并技术。
直接扩展了官方的 AxiosRequestConfig 接口，不仅杜绝了 any，而且团队所有人在写代码时都能享受到完整的中文智能提示。"""
    },
    # 27
    {
        "role": "content",
        "badge": "TypeScript 架构",
        "title": "泛型推导函数封装：request<T>() 打造端到端类型安全",
        "kicker": "剥除外壳，让函数返回值直接对齐业务实体数据契约",
        "code_compare": (
            "通用泛型请求包装函数",
            "export function request<T = any>(config: AxiosRequestConfig): Promise<T> {\n  // 响应拦截器已解包，返回的就是最终 T 类型\n  return service(config) as unknown as Promise<T>;\n}",
            "业务 API 消费端直接获得智能提示",
            "export function getUserProfileApi() {\n  // 明确声明泛型返回类型为 UserInfo\n  return request<UserInfo>({\n    url: '/api/user/profile',\n    method: 'GET'\n  });\n}\n\n// 页面调用：user 变量拥有 id, username, role 完整提示！"
        ),
        "summary": "【收益】消除了前端所有的手动类型断言，后端接口字段修改时，TS 编译期立刻报错感知。",
        "notes": """我们再来看泛型函数 request<T>() 的封装。
因为我们在响应拦截器里已经做过了数据解包，把外层的 code 和 message 脱掉了，直接返回内部的 data。
所以我们封装的通用 request 函数直接将返回值映射为 Promise<T>。
在业务 api/user.ts 里，我们只需传入泛型参数 <UserInfo>。
当组件调用这个 API 时，拿到 user 变量打一个点，IDE 瞬间弹出 username、name、role、permissions。
一旦字段名拼写错误，TypeScript 编译器会在打包阶段立刻报错拦截，把 Bug 扼杀在上线之前！"""
    },
    # 28
    {
        "role": "content",
        "badge": "配套全栈工程",
        "title": "配套 Node.js Express 教学后端：全接口场景真实模拟",
        "kicker": "拒绝假数据 mock，构建可复现、可联调的真实全栈闭环",
        "cards": [
            ("鉴权与无感刷新路由", "/api/auth/login 签发 15s 短期 Token 与 7 天长期 RefreshToken；/api/auth/refresh 校验并换发凭据对。", TEAL),
            ("测试与异常控制路由", "/api/test/delay 模拟 3 秒慢速接口并监听客户端主动断开；/api/test/retry 模拟前两次 503 第三次成功。", AMBER),
            ("文件流与错误导出路由", "/api/file/upload 接收 Multer 上传带人工延时；/api/file/download 二进制文本流与 /download-fail 错误模拟。", PRIMARY)
        ],
        "summary": "【全套开源】后端仅使用 express, cors, multer, jsonwebtoken 原生依赖，轻量极速，开箱即用。",
        "notes": """很多同学在学 Axios 封装时，最大的痛苦就是没有配套的后端环境，只能用 mockjs 拦截。
但 mockjs 是在浏览器内存里伪造的，根本无法模拟真实的 HTTP 401 状态码、无法模拟真实的网络断开连接、也无法模拟 responseType: blob 下的真实二进制流。
为此，我们用纯 JavaScript 编写了一个小巧精悍的 Node.js Express 后端。
不仅完美对应所有的前端用例，而且延时接口甚至可以监听客户端的 req.on('close')，直观证明 AbortController 确实成功终止了服务端的等待。"""
    },
    # 29
    {
        "role": "content",
        "badge": "配套实训平台",
        "title": "Pinia 状态机驱动的可视化执行控制台：直观透视拦截器链路",
        "kicker": "把抽象晦涩的拦截器与并发队列在界面上实时透明化",
        "console_features": [
            ("全局日志钩子解耦", "通过 window.__ADD_AXIOS_LOG__ 跨模块投递，网络层与视图状态库零耦合"),
            ("实时活跃请求监视", "动态展示当前处于 Pending 状态的请求计数，实时捕获手抖连击中的取消事件"),
            ("Token 倒计时沙盒", "右上角动态展现 15 秒短期凭证倒计时，倒计时归零后点击即刻触发静默刷新"),
            ("链路全景逐帧呈现", "[请求拦截 -> 注入凭证 -> 防重检查 -> 401拦截 -> 队列挂起 -> 广播重发] 全程可视化")
        ],
        "summary": "【教学价值】右侧控制台让学员亲眼“看”到拦截器内部的每一步流转，学习效率提升 300%。",
        "notes": """大家在运行前端项目时，可以看到右侧有一个非常酷炫的深色实时控制台。
这正是我们为本次教学专门打造的可视化观察台。
通常情况下，拦截器的执行都是隐藏在浏览器控制台的一行行 console 里，学员很难看清请求队列是如何被挂起的、新 Token 是如何被批量广播的。
通过 Pinia store 驱动的右侧控制台，点击左侧按钮，右侧立刻像慢动作回放一样逐帧打印出拦截器的每一步动作，教学演练效果立竿见影。"""
    },
    # 30
    {
        "role": "ending",
        "badge": "课程总结与面试通关",
        "title": "企业级网络层封装方法论总结与大厂高频面试答辩梳理",
        "kicker": "四大核心支柱通关复盘 · 祝大家技术精进，面试通关！",
        "pillars": [
            ("1. 统一解包与类型安全", "响应拦截器剥离业务外壳，TypeScript 声明合并与泛型推导打造端到端类型守卫。"),
            ("2. 双Token并发无感刷新", "短长凭证分离降低泄露风险，全局锁 + retryQueue 解决并发 401 刷新死锁。"),
            ("3. AbortController 防重连击", "基于四维指纹精准识别重复请求，自动取消前序 pending，路由跳转安全清空。"),
            ("4. 健壮容灾与 Blob 避坑", "计数器模型实现零闪烁 Loading，自动退避重试网络抖动，Blob.text() 反解错误 JSON。")
        ],
        "footer": "感谢聆听！配套源码已全量就绪于当前工作空间 · 欢迎大家在控制台中动手演练实操！",
        "notes": """最后，我们对整堂课程进行复盘总结。
大家在准备大厂面试或者向团队做技术答辩时，可以围绕这四大核心支柱进行系统化陈述：
第一是数据解包与 TypeScript 声明合并；
第二是双 Token 无感刷新的并发队列模型；
第三是现代 AbortController 的请求指纹与防重复提交；
第四是计数器 Loading、自动重试以及 Blob 异常捕获的高可用容错设计。
只要大家把这套源码里的关键细节讲透，无论是日常工程开发还是技术面试，网络层都将成为你极具竞争力的技术名片！
谢谢大家！"""
    }
]

print("Ready to generate", len(slides_content), "slides.")

