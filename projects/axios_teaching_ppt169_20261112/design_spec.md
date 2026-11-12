<!-- ppt-master-schema: design-spec/v1 -->
# axios_teaching - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | axios_teaching |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 30 |
| Primary Language | zh-CN |
| Target Audience | Vue.js 前端开发者、中高级全栈学员、大厂面试备战者及高校师生 |
| Communication Intent | 系统化拆解 Axios 企业级封装的六大核心要点，从原生痛点出发建立工业级架构认知，讲透双Token刷新、防重复取消、Blob异常解析等硬核技术机理 |
| Desired Audience Outcome | 彻底掌握 Axios 拦截器设计思想、TypeScript 声明合并与泛型推导、双 Token 队列并发重放模型以及高健壮性的文件流与异常重试体系 |
| Core Message / Ask / Action | 企业级网络层封装：以统一解包为基石、以双Token无感刷新与AbortController防重复为核心、以全链路TS类型安全与Blob异常容错为保障 |
| Delivery Context | 技术讲座 / 课程教学 / 架构实训，时长约 30-45 分钟，配套全套前后端源码与可视化控制台 |
| Artifact Afterlife | 作为团队标准网络层技术规范、全栈教学讲义及大厂前端面试通关指南 |
| Reading Mode | presentation |
| Content Strategy | 保持技术事实与架构机理高度严谨，代码片段与流程框图对照，重点突出大厂高频考点与避坑实战 |
| Design Style | 剪纸艺术立体风格 (paper-cut)，层次分明的切纸层叠阴影与高对比模块化卡片布局 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — 遵循逐页中文专业技术讲师演讲备注文档 |
| Custom Animations | disabled — 采用纯净静态高质量排版交付 |
| Narration Audio | disabled — 静态教研演示文稿 |
| Created Date | 2026-11-12 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280×720 |
| viewBox | `0 0 1280 720` |
| Margins | 左/右 60px, 上/下 48px |
| Content Area | 1160×624 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Visual style**: paper-cut
- **Theme**: 剪纸微质感技术讲堂 (Paper-cut Craftsmanship & Modern Tech)
- **Tone**: 层次丰富、严谨透气、色彩明快、富有工程质感

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FAF9F5 | 温暖纯净的浅色纸张底层背景 |
| Secondary background | #F1EFE8 | 次级切纸面板层底色，用于形成立体卡片叠层 |
| Primary | #8F2D56 | 深紫红色，用于页面主标题、顶级章节标签及关键概念强化 |
| Accent | #D81159 | 洋红高光，用于醒目标注、警示重点及交互焦点 |
| Secondary accent | #218380 | 深水青蓝，用于次级重点、架构节点、核心接口及正面成功标识 |
| Body text | #2B2D42 | 深炭灰，用于高易读性正文、代码文本与架构描述 |
| Secondary text | #6C757D | 中灰，用于边注、副标题、参数说明及辅助说明 |
| Divider | #E2DDD5 | 细腻剪纸边界线与网格分界 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 稳健醒目、字重厚实、层级分明 | Microsoft YaHei | Arial | sans-serif |
| Body | 现代清晰、代码高易读、等宽精确 | Microsoft YaHei | Fira Code | monospace |

- **Title stack**: "Microsoft YaHei", Arial, sans-serif
- **Body stack**: "Microsoft YaHei", "Fira Code", Consolas, monospace

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Title | 44 |
| Subtitle | 28 |
| Body | 20 |
| Annotation | 16 |
| Footnote | 14 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 严格遵循自顶向下的信息层级（顶栏胶囊定位 -> 大号观点标题 -> 核心结构卡片 -> 底部总结或代码提示）
- **Composition tendency**: 采用剪纸风格的叠层卡片系统（Layered Paper Surfaces），通过多层色块组合表达逻辑递进关系
- **Cross-page continuity**: 顶部统一技术分类胶囊徽章（如【架构全景】、【核心要点】、【大厂避坑】），底部页码与版心基线完全对齐
- **Spacing posture**: 呼吸感留白与高信息密度并重，卡片间距 24px，避免元素拥挤
- **Spacing anchors**: 60px, 24px, 24px, 12px, 1.4

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| icons/tabler-outline/shield-lock.svg | 安全鉴权、Token 令牌、权限保护场景 |
| icons/tabler-outline/refresh.svg | 自动无感刷新、重试机制、数据循环场景 |
| icons/tabler-outline/ban.svg | AbortController 取消、防重复点击、连接中断场景 |
| icons/tabler-outline/loader.svg | 全局 Loading 遮罩、并发计数器场景 |
| icons/tabler-outline/alert-triangle.svg | 业务状态码异常、HTTP 状态报错场景 |
| icons/tabler-outline/file-download.svg | Blob 二进制下载、文件名解析场景 |
| icons/tabler-outline/code.svg | TypeScript 声明合并与泛型推导场景 |
| icons/tabler-outline/terminal-2.svg | Node.js 后端与控制台交互抓包场景 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## IX. Content Outline

### Slide 01 - 课程封面 (Cover & Title)

- **Audience move**: 开启技术探索 -> 明确课程目标与实战体系
- **Relationships**: title -> subtitle -> metadata
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: Axios 工业级深度封装与 TypeScript 架构实战
- **Core message**: 构建生产级高健壮性前端网络层基石
- **Content**:
  - 主讲内容：Vue 3 + TypeScript + Pinia + Node.js 全栈联动
  - 核心要点：统一解包 · 双Token无感刷新 · AbortController防重复 · 计数器Loading · 自动重试 · Blob下载避坑
  - 实训目标：从源码机理剖析到工业级生产落地，打通大厂高频面试核心考点

### Slide 02 - 课程总览 (Course Syllabus)

- **Audience move**: 被动接收 -> 建立系统化学习全景视界
- **Relationships**: pain_points -> core_modules -> outcome
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 为什么网络层封装是企业级前端的核心基石？
- **Core message**: 网络层决定了前端系统的稳定性上限与业务开发效率
- **Content**:
  - 原生痛点剖析：代码冗余、鉴权死锁、重复提交、类型丢失、下载损坏
  - 六大模块演进：从单一请求实例到全生命周期控制器的蜕变
  - 全栈实训闭环：Vue 3 前端 + Node.js 后端 + 可视化实时抓包控制台

### Slide 03 - 原生缺陷 (Axios Pain Points)

- **Audience move**: 习以为常 -> 惊觉原生直接裸用的严重隐患
- **Relationships**: defect_1, defect_2, defect_3, defect_4 [contrast]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 原生 Axios 在大型复杂应用下的七大致命痛点
- **Core message**: 未封装的原生网络请求在生产环境中充满脆弱性
- **Content**:
  - 冗余解包：每个请求均须手动 res.data.data 判空，极易引发运行时空指针
  - 鉴权死锁：Token 过期并发请求时重复调用刷新接口，引发凭证错乱覆盖
  - 防重缺失：弱网或用户连击时造成多次重复提交与服务端脏数据
  - 流错误劫持：responseType: 'blob' 时服务端报错被强转为 Blob 造成破损下载

### Slide 04 - 架构全景 (System Architecture)

- **Audience move**: 微观零散 -> 建立分层解耦的整体系统观
- **Relationships**: layer_1 -> layer_2 -> layer_3 -> layer_4 [parent]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 分层解耦的 TS + Axios 工业级网络层体系全景
- **Core message**: 四层架构设计，职责单一，高内聚低耦合
- **Content**:
  - 业务应用层：模块化 API (auth / user / test / file) 强类型契约
  - 封装核心层：request.ts 核心拦截器流水线与泛型推导
  - 通用工具层：cancel.ts, loading.ts, retry.ts, download.ts, token.ts 独立解耦
  - 支撑服务层：Node.js Express Mock 后端服务实现闭环验证

### Slide 05 - 基础配置 (Instance Configuration)

- **Audience move**: 模糊感知 -> 掌握实例配置最佳实践
- **Relationships**: concept -> code_spec
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 核心要点一：Axios 实例配置哲学与环境变量集成
- **Core message**: 规范的实例基线是请求安全与多环境部署的前提
- **Content**:
  - baseURL 规范：结合 Vite 开发代理与生产环境变量实现无感路由
  - 超时与编码：配置 10000ms 超时底线与 application/json 字符集
  - 实例隔离策略：主业务 service 实例与轻量 refreshService 严格隔离

### Slide 06 - 拦截器模型 (Interceptor Pipeline)

- **Audience move**: 黑盒执行 -> 洞悉请求与响应拦截器流转全貌
- **Relationships**: step1 -> step2 -> step3 -> step4 -> step5 [order]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 拦截器双向管道模型：请求发起与响应收拢生命周期
- **Core message**: 洋葱模型流转，实现切面关注点分离
- **Content**:
  - 请求拦截器：动态注入 Bearer 鉴权 Token、登记防重指纹、激活全局 Loading
  - 响应拦截器：注销 Pending 指纹、统一业务解包、捕获 Blob 异常、分发全局提示
  - 错误拦截器：捕获 401 触发无感刷新队列、网络重试判定与 HTTP 状态码映射

### Slide 07 - 统一解包 (Data Unwrapping)

- **Audience move**: 繁琐编写 -> 享受自动解包带来的极致清爽
- **Relationships**: raw_approach vs wrapped_approach [contrast]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 统一业务解包机制：让业务层少写一层 .data.data
- **Core message**: 在网络层抹平数据封装外壳，将业务逻辑归还给视图
- **Content**:
  - 业务状态判断：校验 code === 200 直接解包返回内部真正的 data.data
  - 异常自动拦截：当 code !== 200 时自动触发 ElMessage 并进入 Promise.reject
  - 业务收益：业务调用端代码精简 50%，根除多层取值报错风险

### Slide 08 - 双Token理念 (Dual Token Concepts)

- **Audience move**: 单凭证思维 -> 领悟双 Token 安全与体验的平衡
- **Relationships**: token_a, token_b -> security_principle
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 核心要点二：双 Token (Access + Refresh) 鉴权设计哲学
- **Core message**: 通过长短凭据分离实现高安全性与无缝用户体验的统一
- **Content**:
  - Access Token：短期有效 (演示设为15秒/生产15分钟)，承载鉴权，泄露损失小
  - Refresh Token：长期有效 (7天)，仅在凭证失效时用于向认证中心安全换发
  - 存储与防篡改：规范本地 LocalStorage 存储与安全传输标头

### Slide 09 - Token流转时序 (Token Lifecycle)

- **Audience move**: 静态认知 -> 掌握凭据时序状态跃迁
- **Relationships**: state1 -> state2 -> state3 -> state4 [order]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 双 Token 协同流转时序与无缝鉴权演进
- **Core message**: 全生命周期状态流转图解
- **Content**:
  - 正常态：请求携带 Bearer AccessToken 顺利通行
  - 过期态：AccessToken 过期，服务端校验失败返回 HTTP 401
  - 换发态：拦截器捕获 401 启动刷新锁，调用 /refresh 置换新凭证
  - 恢复态：新凭证持久化入库，历史请求携带新 Token 重新派发

### Slide 10 - 单请求刷新 (Silent Refresh Single)

- **Audience move**: 抽象流程 -> 掌握单请求 401 拦截重发代码落地
- **Relationships**: logic_steps -> code_implementation
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 单请求 401 拦截与自动换 Token 重发实战
- **Core message**: 响应错误拦截器中的无感拦截与重放机制
- **Content**:
  - 状态捕获：在 error.response.status === 401 分支切入
  - 异步置换：使用 RefreshToken 异步请求刷新端点
  - 原样重放：更新 config.headers['Authorization'] 并 return service(config)

### Slide 11 - 并发重放防死锁 (Concurrent Refresh Queue)

- **Audience move**: 单线思维 -> 掌握并发竞态与请求队列挂起重放
- **Relationships**: requests -> lock -> queue -> broadcast [order]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 高并发 401 避坑：请求队列挂起与批量唤醒防死锁
- **Core message**: 大厂面试最核心考点：并发 401 队列重放模型
- **Content**:
  - 并发危机：页面同时发起 5 个请求全部报 401，若并发刷新导致凭证覆写失效
  - 标志位锁：isRefreshing 全局锁保证同一时刻仅发起一次刷新网络请求
  - 队列挂起：其余请求包装为待执行 Promise 压入 retryQueue
  - 广播重发：刷新成功后遍历队列，批量注入新 Token 并重放所有等待请求

### Slide 12 - 刷新实例隔离 (Refresh Service Isolation)

- **Audience move**: 忽视细节 -> 警惕刷新接口报 401 导致的递归死循环
- **Relationships**: bad_practice vs good_practice [contrast]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 为什么刷新 Token 严禁使用主 Axios 实例？
- **Core message**: 架构安全红线：切忌在拦截器内递归调用带拦截器的实例
- **Content**:
  - 致命缺陷：若 refresh 接口失效报 401，主实例拦截器将再次拦截刷新，引发死循环爆栈
  - 隔离方案：创建独立的 refreshService，不挂载 401 重试拦截器
  - 失败处理：换发失败直接清空凭证并弹窗引导跳转登录页

### Slide 13 - 取消机制演进 (Cancellation Evolution)

- **Audience move**: 了解历史 -> 把握现代标准 AbortController 替代路线
- **Relationships**: legacy_cancel vs modern_abort [contrast]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 核心要点三：从废弃的 CancelToken 到现代 AbortController
- **Core message**: 遵循 Web 标准规范的请求取消技术演进
- **Content**:
  - 历史局限：CancelToken 自 Axios v0.22.0 起被废弃，侵入性强且非标准
  - 现代标准：AbortController 为浏览器和 Node 原生规范，通过 signal 信号量通信
  - 生态兼容：统一 Fetch 与 Axios 的取消范式，支持流式传输与跨框架通用

### Slide 14 - 请求指纹算法 (Request Fingerprint)

- **Audience move**: 粗糙判重 -> 掌握四维请求唯一指纹哈希算法
- **Relationships**: formula -> inputs -> unique_key
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 请求唯一指纹生成机理：精准识别重复点击
- **Core message**: 基于请求上下文生成全局唯一请求签名
- **Content**:
  - 核心维度：Method + URL + Params + Data 四元组严格组合
  - 序列化保真：通过 JSON.stringify 抹平对象引用差异
  - 映射中心：维护 Map<string, AbortController> 记录当前活跃的请求

### Slide 15 - 防手抖连击实战 (Auto Abort Duplicate)

- **Audience move**: 知晓原理 -> 实现前端防手抖自动取消实战
- **Relationships**: req1_start -> req2_arrival -> req1_aborted -> req2_finish [order]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 连续手抖狂点防护：自动中断前序正在 pending 的请求
- **Core message**: 只保留最后一次有效请求，从源头杜绝并发脏数据
- **Content**:
  - 拦截器检查：发起请求时若 Map 中已存在相同 Key，执行 controller.abort()
  - 新请求接管：生成新的 AbortController 并绑定至 config.signal
  - 静默抛出：通过 axios.isCancel(error) 捕获后静默处理，严禁向用户弹红框报错

### Slide 16 - 并发豁免与清理 (Cancel Duplicate Exemption)

- **Audience move**: 一刀切思维 -> 兼顾灵活豁免与页面销毁内存清理
- **Relationships**: feature_exemption, feature_clear [membership]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 慢速请求手动取消与批量并发豁免配置 (cancelDuplicate)
- **Core message**: 兼顾高防护与特化业务诉求的弹性配置
- **Content**:
  - 并发豁免：批量上传分片、多表单同时保存时传入 cancelDuplicate: false 允许并发
  - 手动取消：暴露 clearAllPending() 接口供界面取消按钮随时中断耗时查询
  - 路由守卫集成：页面跳转前批量清空未完成请求，防止组件销毁后状态错乱

### Slide 17 - Loading闪烁痛点 (Loading Boolean Flaw)

- **Audience move**: 盲目使用 -> 洞察传统布尔值 Loading 在并发下的致命闪烁
- **Relationships**: reqA, reqB -> flaw_point -> visual_glitch
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 核心要点四：全屏 Loading 遮罩的布尔值并发致命缺陷
- **Core message**: 为什么简单的 is_loading = true / false 在生产中行不通？
- **Content**:
  - 时序缺陷：A 请求 100ms 先返回，直接把 loading 置为 false
  - 界面闪烁：B (1000ms) 与 C (2000ms) 仍在进行，用户遮罩提前消失且重复点击失效
  - 用户困扰：界面高频抽搐闪烁，大幅降低系统专业感

### Slide 18 - 计数器Loading算法 (Counter Loading Pattern)

- **Audience move**: 发现问题 -> 掌握计数器模型与微延时防闪烁方案
- **Relationships**: count_up -> count_down -> zero_threshold [order]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 计数器模型 (Counter Pattern) 打造并发安全零闪烁 Loading
- **Core message**: 高并发安全的全局加载状态控制器设计
- **Content**:
  - 计数器算法：loadingCount 记录正在执行的请求数，请求发起递增、结束递减
  - 开启准则：loadingCount === 0 时唤起全局 ElLoading 遮罩
  - 微延时防抖：归 0 时通过 setTimeout(100ms) 关闭，抹平超快速请求造成的闪屏

### Slide 19 - 双轨错误分类 (Dual Error Architecture)

- **Audience move**: 混为一谈 -> 明确区分业务状态码与 HTTP 协议状态码
- **Relationships**: business_error vs http_error [contrast]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 核心要点五：双轨错误体系——业务逻辑错误 vs HTTP协议错误
- **Core message**: 规范前后端接口协议与网络错误分流治理
- **Content**:
  - 业务状态码体系：HTTP 状态码是 200，但 body.code !== 200 (如积分不足、账号锁定)
  - HTTP 协议错误体系：网络异常、401 未授权、403 拒绝访问、500 服务宕机
  - 分流治理：业务错误在响应拦截器处理，协议错误在响应错误拦截器处理

### Slide 20 - 错误码中文映射 (HTTP Status Mapping)

- **Audience move**: 生硬英文 -> 打造友好贴心的全局错误转译字典
- **Relationships**: err400, err403, err404, err500 [membership]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 全局 HTTP 状态码友好中文映射与全局分发
- **Core message**: 统一拦截器友好错误映射方案
- **Content**:
  - 400/403/404/500/502/503/504 对应常见场景精准转译为通俗中文
  - 网络超时处理：捕获 ECONNABORTED 与 timeout 提示检查网络
  - 静默控制：支持在请求配置中传入 showErrorMessage: false 跳过全局弹窗

### Slide 21 - 自动退避重试 (Auto Retry Pattern)

- **Audience move**: 被动报错 -> 掌握弱网与 503 故障的自动指数重试
- **Relationships**: condition_check -> retry_execution [order]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 网络抖动与 503 故障：接口智能指数退避重试机制
- **Core message**: 大幅提升移动端弱网与微服务重启时的系统健壮性
- **Content**:
  - 严格重试准则：严禁重试 4xx 客户端错误；仅重试超时、断网与 502/503 临时不可用
  - 重试计数器：通过 config.__retryCount 追踪当前尝试次数
  - 退避延迟：通过 Promise 与 setTimeout 实现间隔 retryDelay 毫秒后自动重新派发

### Slide 22 - 文件上传与进度 (Upload & Progress)

- **Audience move**: 黑盒等待 -> 实现带实时百分比进度的文件上传
- **Relationships**: formdata_spec -> progress_callback
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 核心要点六：文件上传机制与 onUploadProgress 实时监听
- **Core message**: 掌握 FormData 上传与原生进度事件监听
- **Content**:
  - FormData 规范：以 multipart/form-data 传输二进制文件
  - 进度回调：读取 progressEvent.loaded 与 total 计算百分比
  - UI 联动：无缝绑定 Element Plus 进度条组件呈现平滑动画

### Slide 23 - 文件流下载 (Blob Download Stream)

- **Audience move**: 简单 a 标签 -> 掌握 Axios 二进制流安全下载与内存管理
- **Relationships**: fetch_blob -> create_url -> trigger_click -> revoke_url [order]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 二进制流下载：responseType: 'blob' 与内存释放清理
- **Core message**: 具备鉴权能力与错误拦截的高级下载实现
- **Content**:
  - 为什么不用 window.open：无法在 Header 中携带 Bearer Token，且无法拦截报错
  - Blob 对象 URL：通过 window.URL.createObjectURL(blob) 生成内存映射
  - 及时释放内存：触发动态 a 标签点击后，必须通过 revokeObjectURL 释放浏览器内存

### Slide 24 - 文件名解码 (Content-Disposition Parsing)

- **Audience move**: 乱码困扰 -> 掌握 RFC 5987 标准 UTF-8 文件名解析
- **Relationships**: regex_match -> decode_step -> fallback_name
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 从 Content-Disposition 响应头解码 RFC 5987 标准中文文件名
- **Core message**: 彻底终结跨浏览器文件导出中文乱码与截断问题
- **Content**:
  - CORS 暴露标头：后端必须配置 exposedHeaders: ['Content-Disposition']
  - RFC 5987 规范：优先匹配 filename*=UTF-8'' 编码字符串并 decodeURIComponent
  - 保底方案：兼容标准 filename="xxx" 并设置通用保底下载文件名

### Slide 25 - Blob异常捕获 (Blob Error Parsing Trap)

- **Audience move**: 踩坑中招 -> 破解大厂高频面试经典坑：Blob 包装 JSON 报错
- **Relationships**: trap_scene vs solution_mechanism [contrast]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 大厂高频坑：Blob 导出异常时 JSON 报错文本反解与拦截
- **Core message**: 防止下载出包含错误 JSON 的破损伪文件
- **Content**:
  - 致命陷阱：后端报 500 返回 JSON，因前端设置 responseType: blob，被强制打包为 Blob
  - 原生后果：用户下载到一个内容为 {"code":5005,"message":"失败"} 的损坏 xlsx 文件
  - 破解方案：侦测 data.type === 'application/json'，调用 blob.text() 反解为 JSON 弹窗提示

### Slide 26 - TS声明扩展 (TypeScript Module Augmentation)

- **Audience move**: 类型丢失 -> 运用声明合并让 AxiosRequestConfig 拥有全属性提示
- **Relationships**: declaration_code -> ide_autocomplete
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: TypeScript 进阶：声明合并 (Module Augmentation) 扩展 AxiosRequestConfig
- **Core message**: 打造丝滑的 IDE 智能补全与编译期强类型守护
- **Content**:
  - 模块扩展语法：通过 declare module 'axios' 扩展 AxiosRequestConfig
  - 自定义属性补全：cancelDuplicate, showLoading, retryCount, showErrorMessage
  - 工程价值：全团队获得一致的代码提示，杜绝拼写错误导致的隐蔽 Bug

### Slide 27 - 泛型解包推导 (Generic Request Method)

- **Audience move**: 手动断言 -> 封装泛型 request<T>() 享受自动类型推导
- **Relationships**: generic_definition -> api_consumer
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 泛型推导函数封装：request<T>() 打造端到端类型安全
- **Core message**: 让返回值类型直接精确到业务载荷数据结构
- **Content**:
  - 泛型契约设计：封装 export function request<T = any>(config): Promise<T>
  - 类型自动解包：响应拦截器剥除外层 code/message，返回值直接为 T
  - 页面无缝消费：调用 const user = await getUserProfileApi() 获得完整 UserInfo 提示

### Slide 28 - 后端接口配套 (Node.js Mock Server)

- **Audience move**: 前端独角戏 -> 全套 Node.js Express 对应后端环境
- **Relationships**: auth_apis, test_apis, file_apis [membership]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 配套 Node.js Express 教学后端：全接口场景真实模拟
- **Core message**: 构建可复现、可联调、可测试的教学实训闭环
- **Content**:
  - 鉴权接口：POST /api/auth/login 签发 15s 短期 Token 与 7 天 RefreshToken
  - 测试控制接口：延时 delay (支持断开监听)、业务异常 5001、重试 503
  - 文件接口：Multer 单文件带延时上传、Blob 文本流下载与错误导出接口

### Slide 29 - 可视化控制台 (Real-time Logger Console)

- **Audience move**: 枯燥调试 -> 通过 Pinia 实时链路监视器直观理解每个阶段
- **Relationships**: store_dispatch -> console_stream
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: Pinia 状态机驱动的可视化执行控制台：直观透视拦截器链路
- **Core message**: 让抽象的底层拦截器与并发队列在界面上实时可见
- **Content**:
  - 全局钩子联动：通过 window.__ADD_AXIOS_LOG__ 跨模块解耦投递日志
  - 实时指标监控：即时展示 Pending 活跃计数与 AccessToken 倒计时
  - 全链路记录：直观对比请求发出、凭证注入、防重拦截、无感重发与错误分发

### Slide 30 - 总结与面试 (Summary & Interview Review)

- **Audience move**: 融会贯通 -> 提炼网络层封装方法论与大厂面试答辩秘籍
- **Relationships**: pillar1, pillar2, pillar3 [membership]
- **Composition**: 现代剪纸分栏卡片布局，顶部放置胶囊标签，中央为核心对比/代码区，底部为架构总结
- **Title**: 企业级网络层封装方法论总结与大厂高频面试答辩梳理
- **Core message**: 四大核心支柱与面试考点通关复盘
- **Content**:
  - 高频题一：双 Token 无感刷新并发 401 时如何保证只刷新一次并有序重发？
  - 高频题二：如何用 AbortController 基于请求指纹实现重复提交自动拦截？
  - 高频题三：responseType 为 blob 时后端报错，如何防止下载出破损文件？
  - 高频题四：并发多个请求时，如何通过计数器模型设计零闪烁的全局 Loading？

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under notes/
- **Content**: 详细的技术讲师中文逐字讲稿，包含理论推导、关键代码踩坑要点与答辩话术
- **Total duration**: 35-45 minutes
- **Notes style**: 专业、严谨、循序渐进的工程技术讲堂风格
- **Presentation purpose**: 系统化拆解 Axios 企业级封装的六大核心要点
