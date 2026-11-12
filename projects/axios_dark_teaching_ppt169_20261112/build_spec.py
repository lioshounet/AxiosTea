# -*- coding: utf-8 -*-
import os

project_dir = "c:/Users/Administrator/Desktop/Axios/projects/axios_dark_teaching_ppt169_20261112"

spec_lock_content = """<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- format: PPT 16:9
- viewBox: 0 0 1280 720

## communication
- primary_language: zh-CN
- audience: Vue.js 前端开发者、TypeScript 学习者、全栈架构师及大厂前端求职者
- objective: 专注于 Axios 工业级深度封装本身与后端 Express 实际接口的真实联动，全面讲透请求与响应双向拦截器、双 Token 无感并发刷新、AbortController 请求指纹防重、并发安全计数器 Loading、指数退避重试以及 Blob 文件流异常反解的底层全链路机理，包含 7 个深度代码解析页面
- core_message: Axios 工业级深度封装：从单点请求工具到生产级全生命周期网络控制中枢，以双向切面治理为基石，以前后端紧密联动为保障
- consumption_mode: presentation

## mode
- mode: custom
- mode_references: instructional, showcase
- mode_behavior: 以 instructional 教学渐进为骨干，结合 showcase 动态抓包联动演练，层层解析 Axios 封装切面与 Node.js Express 后端对应接口，包含多个详细的代码解析页面。

## visual_style
- visual_style: dark-tech

## colors
- background: #0B0F19
- secondary_bg: #1E293B
- primary: #38BDF8
- accent: #F59E0B
- secondary_accent: #10B981
- body_text: #F8FAFC
- secondary_text: #94A3B8
- divider: #334155

## typography
- font_family: "Microsoft YaHei", Consolas, monospace
- title_family: "Microsoft YaHei", Arial, sans-serif
- body_family: "Microsoft YaHei", Consolas, monospace
- title: 44
- subtitle: 28
- body: 20
- annotation: 16
- footnote: 14

## icons
- library: tabler-outline
- stroke_width: 2
- inventory: code, terminal-2, shield-lock, refresh, ban, loader, alert-triangle, file-download

## page_rhythm
- P01: anchor
- P02: breathing
- P03: dense
- P04: anchor
- P05: dense
- P06: dense
- P07: dense
- P08: dense
- P09: dense
- P10: dense
- P11: dense
- P12: dense
- P13: breathing
- P14: dense
- P15: dense
- P16: dense
- P17: dense
- P18: dense
- P19: dense
- P20: dense
- P21: dense
- P22: dense
- P23: dense
- P24: dense
- P25: dense
- P26: dense
- P27: dense
- P28: dense
- P29: dense
- P30: anchor

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
"""

with open(os.path.join(project_dir, "spec_lock.md"), "w", encoding="utf-8") as f:
    f.write(spec_lock_content.strip() + "\n")
print("[OK] Written spec_lock.md")

slides_spec = [
    (1, "封面 · Axios 工业级深度封装与后端联动架构实训", "建立对企业级全栈网络中枢的整体认知与学习目标", "cover", "anchor"),
    (2, "课程体系大纲：为什么网络层封装是企业级前端的核心基石？", "从单点请求调用跃迁至全局全生命周期切面治理认知", "overview", "breathing"),
    (3, "原生裸用缺陷剖析：大型复杂应用下 Axios 的七大致命痛点", "深刻认识原生网络层脆弱性，明确本次重构与封装的现实诉求", "pain_points", "dense"),
    (4, "总体架构设计：TS + Axios 工业级分层解耦网络层全景拓扑", "建立四层分层模型（API服务层、封装核心层、通用工具层、Mock服务层）的宏观全局观", "architecture", "anchor"),
    (5, "核心要点一 · 实例基线：baseURL、全局超时与实例隔离红线", "掌握 Axios 实例配置安全原则，理解为什么必须与全局默认对象及业务主实例隔离", "instance_baseline", "dense"),
    (6, "核心要点一 · 管道切面：Axios 双向洋葱模型生命周期流转图", "理解请求拦截器与响应拦截器的切面拦截机制", "pipeline_onion", "dense"),
    (7, "【代码解析 1】request.ts 核心实例创建与双向拦截器装配源码", "看透 service 实例初始化与拦截器插件化挂载实现细节", "code_core_setup", "dense"),
    (8, "核心要点一 · 数据解包：统一剥离业务外壳与前后端状态契约联动", "掌握在响应拦截器中自动化解包 res.data.data 与业务状态码过滤", "data_unwrapping", "dense"),
    (9, "核心要点二 · 双Token机制：Access Token (15s) + Refresh Token (7d)", "理解长短凭证安全互补的设计哲学与前后端鉴权边界", "dual_token_concept", "dense"),
    (10, "核心要点二 · 拦截切入：HTTP 401 触发无感刷新状态流转全景", "厘清从捕获 401 到刷新成功重发请求的闭环流程", "token_refresh_flow", "dense"),
    (11, "【代码解析 2】isRefreshing 互斥锁与 retryQueue 挂起队列核心实现", "深度精读高并发场景下防死锁互斥锁与未决 Promise 队列的优雅实现", "code_refresh_lock", "dense"),
    (12, "核心要点二 · 泳道图解：多接口并发 401 时的安全排队与批量 Replay", "直观感知高并发网络波动时请求队列的暂存与并发重放过程", "concurrency_swimlane", "dense"),
    (13, "架构避坑指南：refreshService 轻量实例隔离 vs 递归主实例死锁", "树立架构安全红线，严防在拦截器中直接递归调用自身导致的调用栈溢出", "refresh_isolation", "breathing"),
    (14, "核心要点三 · 防重复提交：手抖连击、重复点击与并发冲突危害", "深刻理解前端主动拦截重复网络包在金融交易与表单提交场景下的重要性", "cancel_necessity", "dense"),
    (15, "核心要点三 · 唯一指纹：四维哈希生成算法 (Method+URL+Params+Data)", "掌握基于请求元数据构建高可靠唯一哈希指纹的技术方案", "fingerprint_algorithm", "dense"),
    (16, "【代码解析 3】cancel.ts 唯一指纹哈希与 Map 注册表管理源码剖析", "精读基于 AbortController 与 Map 的请求控制器注册与撤销源码", "code_cancel_manager", "dense"),
    (17, "核心要点三 · 场景扩展：SPA 路由守卫自动清空与页面主动中断", "掌握在页面跳转及大文件耗时查询时的主动取消最佳实践", "route_cancel_clean", "dense"),
    (18, "核心要点四 · Loading缺陷：并发异步请求下的遮罩提前关闭现场", "通过精准时序缺陷复现，认识单布尔值控制 Loading 的致命漏洞", "loading_flaw_timeline", "dense"),
    (19, "【代码解析 4】loading.ts Counter Pattern 计数器与防抖延时源码", "掌握并发安全计数器模型与 200ms 防抖消除闪烁的落地实现", "code_loading_counter", "dense"),
    (20, "核心要点四 · 精准控制：自定义 loadingTarget 与 silent 静默请求", "掌握接口粒度级别的高级控制参数配置方式", "loading_fine_grained", "dense"),
    (21, "核心要点五 · 容错边界：网络异常分类与自动重试策略边界划分", "明确哪些错误应当重试（超时、503）与哪些绝不能重试（400、401、403）", "error_retry_boundary", "dense"),
    (22, "核心要点五 · 智能退避：指数退避算法 (Exponential Backoff) 原理", "理解避免重试风暴引发服务端二次雪崩的数学退避曲线", "exponential_backoff", "dense"),
    (23, "【代码解析 5】retry.ts 基于 Promise 延时链与重试计数器拦截器注入", "精读通过 AxiosRequestConfig 元数据实现重试次数递增与延时重发的实现", "code_retry_interceptor", "dense"),
    (24, "后端联动验证：Node.js Express 503 重启模拟与实战抓包复现", "结合 Express 后端真实接口，完成网络异常下的重试全链路验证", "backend_503_simulation", "dense"),
    (25, "核心要点六 · Blob深坑：二进制流下载的典型技术壁垒与乱码", "认识常规 a 标签模拟点击在跨域、鉴权及文件名中文乱码时的限制", "blob_download_barriers", "dense"),
    (26, "核心要点六 · RFC 5987：解析 Content-Disposition 与 UTF-8 编码", "攻克标准 HTTP 头中 filename*=utf-8'' 中文文件名的标准解码算法", "rfc5987_decoding", "dense"),
    (27, "【代码解析 6】download.ts 破解大厂深坑：Blob 内嵌 JSON 错误反解", "掌握通过 FileReader 或 text() 异步探测并提取服务端真实报错的黑科技", "code_blob_fallback", "dense"),
    (28, "【代码解析 7】TypeScript 架构进阶：axios.d.ts 声明合并扩展配置", "掌握 TypeScript 模块扩充 (Module Augmentation) 技巧，实现配置项强类型提示", "code_ts_augmentation", "dense"),
    (29, "端到端强类型守卫：泛型 request<T>() 包装与业务接口契约", "完成 API 函数与返回数据结构的无缝类型推导闭环", "generic_request_contract", "dense"),
    (30, "课程全景技术图谱总结、架构进阶指南与 GitHub 源码仓库", "巩固全套工业级网络层封装核心要点，明确后续工程化演进路径", "course_summary_ending", "anchor")
]

design_spec_content = f"""# Design Specification: Axios 工业级深度封装与后端联动架构实训 (Dark Tech Console)

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
"""

for s in slides_spec:
    num, title, move, viz, rhythm = s
    design_spec_content += f"""### Slide {num:02d} - {title}
- **Audience move**: {move}
- **Relationships**: order={num}, layout={viz}, rhythm={rhythm}
- **Visual format**: {viz}
- **Key points**: 围绕 Axios 工业级深度封装与 Node.js 后端联动展开，注重深色控制台代码展示与真实网络时序排查。

"""

design_spec_content += """## X. Speaker Notes Requirements
- 每页 PPT 均配备详尽的讲师授课逐字稿讲义。
- 重点突出大厂高频面试点、架构设计哲学、踩坑避坑指南与后端 Express 抓包联动实操指引。
- 讲义内容与代码片段逐行对应，引导学员从浅入深吃透核心切面。
"""

with open(os.path.join(project_dir, "design_spec.md"), "w", encoding="utf-8") as f:
    f.write(design_spec_content.strip() + "\n")
print("[OK] Written design_spec.md")

