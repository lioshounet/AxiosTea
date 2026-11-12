# -*- coding: utf-8 -*-
sample_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="cover">
  <!-- Background Paper Layer -->
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <!-- Decorative Cut Paper Sheets -->
  <path id="deco-sheet-1" d="M 0,0 L 400,0 C 350,180 480,260 380,440 C 300,580 420,680 320,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 220,0 C 180,200 280,320 190,500 C 130,620 220,680 180,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
  <!-- Header Group -->
  <g id="header-group" data-pptx-bounds="60 48 1160 144">
    <!-- Header Badge -->
    <rect x="60" y="48" width="240" height="30" rx="15" fill="#8F2D56"/>
    <text x="180" y="68" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">企业级前端工程化 · 架构实战</text>
    
    <!-- Main Title -->
    <text x="60" y="126" font-size="44" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#0F172A">Axios 工业级深度封装与 TypeScript 架构实训</text>
    <text x="60" y="166" font-size="20" font-family="'Microsoft YaHei', Arial" fill="#6C757D">从原生痛点到生产级网络层基石建设 · Vue 3 + TS + Pinia + Node.js 全栈闭环</text>
  </g>

  <!-- 6 Feature Cards in Paper-cut Style -->
  <!-- Card 1 -->
  <g id="card-01" data-pptx-bounds="60 205 360 135">
    <rect x="60" y="209" width="360" height="131" rx="12" fill="#E2DDD5"/>
    <rect x="60" y="205" width="360" height="131" rx="12" fill="#FFFFFF" stroke="#8F2D56" stroke-width="1.5"/>
    <rect x="78" y="218" width="28" height="28" rx="6" fill="#8F2D56"/>
    <text x="92" y="238" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">01</text>
    <text x="116" y="239" font-size="20" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56">统一数据解包</text>
    <text x="78" y="274" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      <tspan x="78" dy="0">响应拦截器剥离业务外壳，</tspan>
      <tspan x="78" dy="22">终结冗长繁琐且易空指针的 res.data.data 报错。</tspan>
    </text>
  </g>

  <!-- Card 2 -->
  <g id="card-02" data-pptx-bounds="460 205 360 135">
    <rect x="460" y="209" width="360" height="131" rx="12" fill="#E2DDD5"/>
    <rect x="460" y="205" width="360" height="131" rx="12" fill="#FFFFFF" stroke="#D81159" stroke-width="1.5"/>
    <rect x="478" y="218" width="28" height="28" rx="6" fill="#D81159"/>
    <text x="492" y="238" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">02</text>
    <text x="516" y="239" font-size="20" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#D81159">双Token无感刷新</text>
    <text x="478" y="274" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      <tspan x="478" dy="0">401 拦截切入、isRefreshing 全局锁与</tspan>
      <tspan x="478" dy="22">并发请求队列挂起重发，杜绝凭据竞态覆盖死锁。</tspan>
    </text>
  </g>

  <!-- Card 3 -->
  <g id="card-03" data-pptx-bounds="860 205 360 135">
    <rect x="860" y="209" width="360" height="131" rx="12" fill="#E2DDD5"/>
    <rect x="860" y="205" width="360" height="131" rx="12" fill="#FFFFFF" stroke="#218380" stroke-width="1.5"/>
    <rect x="878" y="218" width="28" height="28" rx="6" fill="#218380"/>
    <text x="892" y="238" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">03</text>
    <text x="916" y="239" font-size="20" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#218380">AbortController防重复</text>
    <text x="878" y="274" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      <tspan x="878" dy="0">四维哈希生成唯一请求指纹，</tspan>
      <tspan x="878" dy="22">自动取消前序 pending 请求，彻底防御手抖连击。</tspan>
    </text>
  </g>

  <!-- Card 4 -->
  <g id="card-04" data-pptx-bounds="60 355 360 135">
    <rect x="60" y="359" width="360" height="131" rx="12" fill="#E2DDD5"/>
    <rect x="60" y="355" width="360" height="131" rx="12" fill="#FFFFFF" stroke="#FFBC42" stroke-width="1.5"/>
    <rect x="78" y="368" width="28" height="28" rx="6" fill="#FFBC42"/>
    <text x="92" y="388" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">04</text>
    <text x="116" y="389" font-size="20" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#B45309">计数器Loading模型</text>
    <text x="78" y="424" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      <tspan x="78" dy="0">基于 Counter Pattern 并发安全模型，</tspan>
      <tspan x="78" dy="22">解决单布尔值导致的过早关闭与页面严重频闪。</tspan>
    </text>
  </g>

  <!-- Card 5 -->
  <g id="card-05" data-pptx-bounds="460 355 360 135">
    <rect x="460" y="359" width="360" height="131" rx="12" fill="#E2DDD5"/>
    <rect x="460" y="355" width="360" height="131" rx="12" fill="#FFFFFF" stroke="#73D2DE" stroke-width="1.5"/>
    <rect x="478" y="368" width="28" height="28" rx="6" fill="#0284C7"/>
    <text x="492" y="388" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">05</text>
    <text x="516" y="389" font-size="20" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#0284C7">智能指数退避重试</text>
    <text x="478" y="424" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      <tspan x="478" dy="0">针对网络偶发断流、超时及 503 重启，</tspan>
      <tspan x="478" dy="22">配置化自动延迟重试，大幅提升系统高可用健壮性。</tspan>
    </text>
  </g>

  <!-- Card 6 -->
  <g id="card-06" data-pptx-bounds="860 355 360 135">
    <rect x="860" y="359" width="360" height="131" rx="12" fill="#E2DDD5"/>
    <rect x="860" y="355" width="360" height="131" rx="12" fill="#FFFFFF" stroke="#8F2D56" stroke-width="1.5"/>
    <rect x="878" y="368" width="28" height="28" rx="6" fill="#8F2D56"/>
    <text x="892" y="388" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">06</text>
    <text x="916" y="389" font-size="20" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56">Blob下载与异常反解</text>
    <text x="878" y="424" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      <tspan x="878" dy="0">RFC 5987 文件名 UTF-8 解码，</tspan>
      <tspan x="878" dy="22">后端报错时反解 Blob 内嵌 JSON 错误，破除大厂坑。</tspan>
    </text>
  </g>

  <!-- Bottom Banner Card -->
  <g id="bottom-banner" data-pptx-bounds="60 505 1160 88">
    <rect x="60" y="509" width="1160" height="84" rx="14" fill="#E2DDD5"/>
    <rect x="60" y="505" width="1160" height="84" rx="14" fill="#F1EFE8" stroke="#E2DDD5" stroke-width="1"/>
    <text x="90" y="538" font-size="16" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56">🛠️ 教学全栈实训闭环套件：</text>
    <text x="90" y="568" font-size="14" font-family="'Microsoft YaHei', Consolas, monospace" fill="#2B2D42">Vue 3 + 全量 TypeScript 严格声明合并 + Pinia 实时链路可视化监视器 + 原生 Node.js Express 对应后端</text>
  </g>

  <!-- Footer Group -->
  <g id="footer-group" data-pptx-bounds="60 670 1160 30">
    <text x="60" y="688" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#6C757D">主讲人：Vue.js / 全栈架构讲师 · 课时：45分钟 · 源码全开源配套</text>
    <text x="1220" y="688" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56" text-anchor="end">01 / 30</text>
  </g>
</svg>
"""

out_path = "c:/Users/Administrator/Desktop/Axios/projects/axios_teaching_ppt169_20261112/svg_output/slide_01.svg"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(sample_svg)
print("Updated slide_01.svg")
