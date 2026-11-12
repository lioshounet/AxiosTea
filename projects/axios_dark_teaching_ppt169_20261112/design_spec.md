# Design Specification: Axios 工业级深度封装与后端联动架构实训 (Dark Tech Console)

## I. Core Parameters
- canvas: ppt169 (1280x720)
- page_count: 30
- visual_style: dark-tech
- mode: custom (instructional + showcase)
- delivery_purpose: presentation
- speaker_notes: enabled (proactive)
- custom_animations: disabled
- narration_audio: disabled

## II. Audience & Intent
- Target Audience: Vue.js 前端开发者、TypeScript 学习者、全栈架构师及大厂前端求职者
- Communication Intent: 专注于 Axios 工业级深度封装本身与后端 Express 实际接口的真实联动，全面讲透请求与响应双向拦截器、双 Token 无感并发刷新、AbortController 请求指纹防重、并发安全计数器 Loading、指数退避重试以及 Blob 文件流异常反解的底层全链路机理，包含 7 个深度代码解析页面。
- Audience Outcome: 深入掌握 Axios 核心架构原理与模块化解耦封装，打通前端 TypeScript 请求层与后端鉴权、容错、流传输的交互闭环，具备工业级网络中枢的架构设计能力。
- Core Message: Axios 工业级深度封装：从单点请求工具到生产级全生命周期网络控制中枢，以双向切面治理为基石，以前后端紧密联动为保障。

## III. Visual Style & Color System
- Style: dark-tech (极客深色终端代码控制台风格)
- Palette:
  - Background: #0B0F19 (深邃黑蓝底色)
  - Secondary Background (Cards): #1E293B (暗蓝悬浮卡片)
  - Primary Accent: #38BDF8 (天青蓝 / 高亮青)
  - Accent: #F59E0B (琥珀黄 / 警示金)
  - Secondary Accent: #10B981 (翡翠绿 / 成功绿)
  - Body Text: #F8FAFC (清爽白)
  - Secondary Text: #94A3B8 (板岩灰)
  - Divider / Stroke: #334155 (暗色精准边框线)

## IV. Typography System
- Font Family: "Microsoft YaHei", Consolas, monospace
- Title Family: "Microsoft YaHei", Arial, sans-serif
- Body Family: "Microsoft YaHei", Consolas, monospace
- Scale:
  - Title: 44
  - Subtitle: 28
  - Body: 20
  - Annotation: 16
  - Footnote: 14

## V. Layout & Rhythm
- Canvas ViewBox: 0 0 1280 720
- Visual Rhythms:
  - Anchor: P01, P04, P30
  - Breathing: P02, P13
  - Dense & Code Deep Dive: P03, P05-P12, P14-P29

## VI. Icon & Decorative Vocabulary
- Library: tabler-outline
- Stroke Width: 2px
- Technical Visuals: Code Blocks with syntax highlight, Concurrency Swimlanes, Pipeline Steppers, Comparison Panels, Terminal Windows

## VII. Animation & Interaction Design
- Transitions: Fade
- Interactions: Visual code block window with traffic dots (red, yellow, green), interactive packet tracing console mockup

## VIII. Resource Manifest
- Sources:
  - client/src/utils/request.ts
  - client/src/utils/cancel.ts
  - client/src/utils/loading.ts
  - client/src/utils/retry.ts
  - client/src/utils/download.ts
  - client/src/utils/token.ts
  - server/index.js
  - README.md

## IX. Content Outline & Page Specifications
### Slide 01 - 封面 · Axios 工业级深度封装与后端联动架构实训
- **Audience move**: 建立对企业级全栈网络中枢的整体认知与学习目标
- **Relationships**: order=1, layout=cover, rhythm=anchor
- **Visual format**: cover
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 02 - 课程体系大纲：为什么网络层封装是企业级前端的核心基石？
- **Audience move**: 从单点请求调用跃迁至全局全生命周期切面治理认知
- **Relationships**: order=2, layout=overview, rhythm=breathing
- **Visual format**: overview
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 03 - 原生裸用缺陷剖析：大型复杂应用下 Axios 的七大致命痛点
- **Audience move**: 深刻认识原生网络层脆弱性，明确本次重构与封装的现实诉求
- **Relationships**: order=3, layout=pain_points, rhythm=dense
- **Visual format**: pain_points
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 04 - 总体架构设计：TS + Axios 工业级分层解耦网络层全景拓扑
- **Audience move**: 建立四层分层模型（API服务层、封装核心层、通用工具层、Mock服务层）的宏观全局观
- **Relationships**: order=4, layout=architecture, rhythm=anchor
- **Visual format**: architecture
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 05 - 核心要点一 · 实例基线：baseURL、全局超时与实例隔离红线
- **Audience move**: 掌握 Axios 实例配置安全原则，理解为什么必须与全局默认对象及业务主实例隔离
- **Relationships**: order=5, layout=instance_baseline, rhythm=dense
- **Visual format**: instance_baseline
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 06 - 核心要点一 · 管道切面：Axios 双向洋葱模型生命周期流转图
- **Audience move**: 理解请求拦截器与响应拦截器的切面拦截机制
- **Relationships**: order=6, layout=pipeline_onion, rhythm=dense
- **Visual format**: pipeline_onion
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 07 - 【代码解析 1】request.ts 核心实例创建与双向拦截器装配源码
- **Audience move**: 看透 service 实例初始化与拦截器插件化挂载实现细节
- **Relationships**: order=7, layout=code_core_setup, rhythm=dense
- **Visual format**: code_core_setup
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 08 - 核心要点一 · 数据解包：统一剥离业务外壳与前后端状态契约联动
- **Audience move**: 掌握在响应拦截器中自动化解包 res.data.data 与业务状态码过滤
- **Relationships**: order=8, layout=data_unwrapping, rhythm=dense
- **Visual format**: data_unwrapping
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 09 - 核心要点二 · 双Token机制：Access Token (15s) + Refresh Token (7d)
- **Audience move**: 理解长短凭证安全互补的设计哲学与前后端鉴权边界
- **Relationships**: order=9, layout=dual_token_concept, rhythm=dense
- **Visual format**: dual_token_concept
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 10 - 核心要点二 · 拦截切入：HTTP 401 触发无感刷新状态流转全景
- **Audience move**: 厘清从捕获 401 到刷新成功重发请求的闭环流程
- **Relationships**: order=10, layout=token_refresh_flow, rhythm=dense
- **Visual format**: token_refresh_flow
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 11 - 【代码解析 2】isRefreshing 互斥锁与 retryQueue 挂起队列核心实现
- **Audience move**: 深度精读高并发场景下防死锁互斥锁与未决 Promise 队列的优雅实现
- **Relationships**: order=11, layout=code_refresh_lock, rhythm=dense
- **Visual format**: code_refresh_lock
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 12 - 核心要点二 · 泳道图解：多接口并发 401 时的安全排队与批量 Replay
- **Audience move**: 直观感知高并发网络波动时请求队列的暂存与并发重放过程
- **Relationships**: order=12, layout=concurrency_swimlane, rhythm=dense
- **Visual format**: concurrency_swimlane
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 13 - 架构避坑指南：refreshService 轻量实例隔离 vs 递归主实例死锁
- **Audience move**: 树立架构安全红线，严防在拦截器中直接递归调用自身导致的调用栈溢出
- **Relationships**: order=13, layout=refresh_isolation, rhythm=breathing
- **Visual format**: refresh_isolation
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 14 - 核心要点三 · 防重复提交：手抖连击、重复点击与并发冲突危害
- **Audience move**: 深刻理解前端主动拦截重复网络包在金融交易与表单提交场景下的重要性
- **Relationships**: order=14, layout=cancel_necessity, rhythm=dense
- **Visual format**: cancel_necessity
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 15 - 核心要点三 · 唯一指纹：四维哈希生成算法 (Method+URL+Params+Data)
- **Audience move**: 掌握基于请求元数据构建高可靠唯一哈希指纹的技术方案
- **Relationships**: order=15, layout=fingerprint_algorithm, rhythm=dense
- **Visual format**: fingerprint_algorithm
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 16 - 【代码解析 3】cancel.ts 唯一指纹哈希与 Map 注册表管理源码剖析
- **Audience move**: 精读基于 AbortController 与 Map 的请求控制器注册与撤销源码
- **Relationships**: order=16, layout=code_cancel_manager, rhythm=dense
- **Visual format**: code_cancel_manager
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 17 - 核心要点三 · 场景扩展：SPA 路由守卫自动清空与页面主动中断
- **Audience move**: 掌握在页面跳转及大文件耗时查询时的主动取消最佳实践
- **Relationships**: order=17, layout=route_cancel_clean, rhythm=dense
- **Visual format**: route_cancel_clean
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 18 - 核心要点四 · Loading缺陷：并发异步请求下的遮罩提前关闭现场
- **Audience move**: 通过精准时序缺陷复现，认识单布尔值控制 Loading 的致命漏洞
- **Relationships**: order=18, layout=loading_flaw_timeline, rhythm=dense
- **Visual format**: loading_flaw_timeline
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 19 - 【代码解析 4】loading.ts Counter Pattern 计数器与防抖延时源码
- **Audience move**: 掌握并发安全计数器模型与 200ms 防抖消除闪烁的落地实现
- **Relationships**: order=19, layout=code_loading_counter, rhythm=dense
- **Visual format**: code_loading_counter
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 20 - 核心要点四 · 精准控制：自定义 loadingTarget 与 silent 静默请求
- **Audience move**: 掌握接口粒度级别的高级控制参数配置方式
- **Relationships**: order=20, layout=loading_fine_grained, rhythm=dense
- **Visual format**: loading_fine_grained
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 21 - 核心要点五 · 容错边界：网络异常分类与自动重试策略边界划分
- **Audience move**: 明确哪些错误应当重试（超时、503）与哪些绝不能重试（400、401、403）
- **Relationships**: order=21, layout=error_retry_boundary, rhythm=dense
- **Visual format**: error_retry_boundary
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 22 - 核心要点五 · 智能退避：指数退避算法 (Exponential Backoff) 原理
- **Audience move**: 理解避免重试风暴引发服务端二次雪崩的数学退避曲线
- **Relationships**: order=22, layout=exponential_backoff, rhythm=dense
- **Visual format**: exponential_backoff
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 23 - 【代码解析 5】retry.ts 基于 Promise 延时链与重试计数器拦截器注入
- **Audience move**: 精读通过 AxiosRequestConfig 元数据实现重试次数递增与延时重发的实现
- **Relationships**: order=23, layout=code_retry_interceptor, rhythm=dense
- **Visual format**: code_retry_interceptor
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 24 - 后端联动验证：Node.js Express 503 重启模拟与实战抓包复现
- **Audience move**: 结合 Express 后端真实接口，完成网络异常下的重试全链路验证
- **Relationships**: order=24, layout=backend_503_simulation, rhythm=dense
- **Visual format**: backend_503_simulation
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 25 - 核心要点六 · Blob深坑：二进制流下载的典型技术壁垒与乱码
- **Audience move**: 认识常规 a 标签模拟点击在跨域、鉴权及文件名中文乱码时的限制
- **Relationships**: order=25, layout=blob_download_barriers, rhythm=dense
- **Visual format**: blob_download_barriers
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 26 - 核心要点六 · RFC 5987：解析 Content-Disposition 与 UTF-8 编码
- **Audience move**: 攻克标准 HTTP 头中 filename*=utf-8'' 中文文件名的标准解码算法
- **Relationships**: order=26, layout=rfc5987_decoding, rhythm=dense
- **Visual format**: rfc5987_decoding
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 27 - 【代码解析 6】download.ts 破解大厂深坑：Blob 内嵌 JSON 错误反解
- **Audience move**: 掌握通过 FileReader 或 text() 异步探测并提取服务端真实报错的黑科技
- **Relationships**: order=27, layout=code_blob_fallback, rhythm=dense
- **Visual format**: code_blob_fallback
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 28 - 【代码解析 7】TypeScript 架构进阶：axios.d.ts 声明合并扩展配置
- **Audience move**: 掌握 TypeScript 模块扩充 (Module Augmentation) 技巧，实现配置项强类型提示
- **Relationships**: order=28, layout=code_ts_augmentation, rhythm=dense
- **Visual format**: code_ts_augmentation
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 29 - 端到端强类型守卫：泛型 request<T>() 包装与业务接口契约
- **Audience move**: 完成 API 函数与返回数据结构的无缝类型推导闭环
- **Relationships**: order=29, layout=generic_request_contract, rhythm=dense
- **Visual format**: generic_request_contract
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

### Slide 30 - 课程全景技术图谱总结、架构进阶指南与 GitHub 源码仓库
- **Audience move**: 巩固全套工业级网络层封装核心要点，明确后续工程化演进路径
- **Relationships**: order=30, layout=course_summary_ending, rhythm=anchor
- **Visual format**: course_summary_ending
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

## X. Speaker Notes Requirements
- 每页 PPT 均配备详尽的讲师授课逐字稿讲义。
- 重点突出大厂高频面试点、架构设计哲学、踩坑避坑指南与后端 Express 抓包联动实操指引。
- 讲义内容与代码片段逐行对应，引导学员从浅入深吃透核心切面。
