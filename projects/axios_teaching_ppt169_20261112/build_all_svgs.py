# -*- coding: utf-8 -*-
import os
import sys

# Add skills scripts to path for text_measure
sys.path.append("D:/Zpan/ppt-master/skills/ppt-master/scripts")
from text_measure import wrap_text

sys.path.append("c:/Users/Administrator/Desktop/Axios/projects/axios_teaching_ppt169_20261112")
import slides_data_config as cfg

project_dir = "c:/Users/Administrator/Desktop/Axios/projects/axios_teaching_ppt169_20261112"
svg_dir = os.path.join(project_dir, "svg_output")
notes_dir = os.path.join(project_dir, "notes")
os.makedirs(svg_dir, exist_ok=True)
os.makedirs(notes_dir, exist_ok=True)

def esc(txt):
    if txt is None:
        return ""
    return str(txt).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def wrap_lines(text, max_w, size=15.0, family="'Microsoft YaHei', Arial"):
    clean_fam = family.replace("'", "").split(",")[0].strip()
    try:
        lines, _, _ = wrap_text(text, size=size, max_width=max_w, family=clean_fam)
        return lines
    except Exception:
        # fallback simple wrap
        avg_w = size * 0.9
        max_chars = int(max_w / avg_w)
        res = []
        for i in range(0, len(text), max_chars):
            res.append(text[i:i+max_chars])
        return res

def render_header(s, page_num):
    badge = esc(s.get("badge", "企业级前端工程化 · 架构实战"))
    title = esc(s.get("title", ""))
    kicker = esc(s.get("kicker", ""))
    
    # Calculate title lines if long - strictly use anchor 28 for subtitle / content title
    t_lines = wrap_lines(s.get("title", ""), 1140, size=28.0, family="'Microsoft YaHei', Arial")
    
    h_svg = f'''  <!-- Header Group -->
  <g id="header-group" data-pptx-bounds="60 42 1160 138">
    <rect x="60" y="42" width="260" height="28" rx="14" fill="#8F2D56"/>
    <text x="190" y="61" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{badge}</text>
'''
    if len(t_lines) == 1:
        h_svg += f'''    <text x="60" y="106" font-size="28" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#0F172A">{esc(t_lines[0])}</text>
    <text x="60" y="146" font-size="16" font-family="'Microsoft YaHei', Arial" fill="#6C757D">{kicker}</text>
  </g>
'''
    else:
        l0 = esc(t_lines[0])
        l1 = esc(t_lines[1]) if len(t_lines) > 1 else ""
        h_svg += f'''    <text x="60" y="98" font-size="24" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#0F172A">
      <tspan x="60" dy="0">{l0}</tspan>
      <tspan x="60" dy="32">{l1}</tspan>
    </text>
    <text x="60" y="160" font-size="15" font-family="'Microsoft YaHei', Arial" fill="#6C757D">{kicker}</text>
  </g>
'''
    return h_svg

def render_footer(page_num):
    pg_str = f"{page_num:02d} / 30"
    return f'''  <!-- Footer Group -->
  <g id="footer-group" data-pptx-bounds="60 670 1160 30">
    <text x="60" y="688" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#6C757D">Vue 3 + TS 工业级 Axios 深度封装实战 · 全栈教学课程</text>
    <text x="1220" y="688" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56" text-anchor="end">{pg_str}</text>
  </g>
'''

def render_summary(s):
    sum_txt = s.get("summary", "")
    if not sum_txt:
        return ""
    lines = wrap_lines(sum_txt, 1100, size=15.0, family="'Microsoft YaHei', Arial")
    tspan_str = ""
    for idx, l in enumerate(lines[:2]):
        dy = 0 if idx == 0 else 22
        tspan_str += f'<tspan x="90" dy="{dy}">{esc(l)}</tspan>'
    
    return f'''  <!-- Summary Banner -->
  <g id="summary-banner" data-pptx-bounds="60 580 1160 76">
    <rect x="60" y="584" width="1160" height="72" rx="14" fill="#E2DDD5"/>
    <rect x="60" y="580" width="1160" height="72" rx="14" fill="#F1EFE8" stroke="#E2DDD5" stroke-width="1"/>
    <text x="90" y="618" font-size="15" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56">
      {tspan_str}
    </text>
  </g>
'''

def render_slide(s):
    p_num = s["num"]
    stype = s["type"]
    
    # Common backgrounds
    bg_svg = '''  <!-- Background Paper Layer -->
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <!-- Decorative Cut Paper Sheets -->
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
'''
    
    if stype == "cover":
        # Slide 1 cover
        return render_cover(s)
    elif stype == "three_col":
        return render_three_col(s)
    elif stype == "four_quadrant":
        return render_four_quadrant(s)
    elif stype == "four_layers":
        return render_four_layers(s)
    elif stype == "pipeline":
        return render_pipeline(s)
    elif stype == "two_col_code":
        return render_two_col_code(s)
    elif stype == "code_highlight":
        return render_code_highlight(s)
    elif stype == "queue_swimlane":
        return render_queue_swimlane(s)
    elif stype == "two_col_compare":
        return render_two_col_compare(s)
    elif stype == "timeline_flaw":
        return render_timeline_flaw(s)
    elif stype == "ending":
        return render_ending(s)
    else:
        return render_three_col(s)

def render_cover(s):
    # Slide 1 refined
    badge = esc(s.get("badge", ""))
    title = esc(s.get("title", ""))
    kicker = esc(s.get("kicker", ""))
    
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="cover">
  <!-- Background Paper Layer -->
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <!-- Decorative Cut Paper Sheets -->
  <path id="deco-sheet-1" d="M 0,0 L 400,0 C 350,180 480,260 380,440 C 300,580 420,680 320,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 220,0 C 180,200 280,320 190,500 C 130,620 220,680 180,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
  <!-- Header Group -->
  <g id="header-group" data-pptx-bounds="60 48 1160 144">
    <rect x="60" y="48" width="240" height="30" rx="15" fill="#8F2D56"/>
    <text x="180" y="68" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{badge}</text>
    <text x="60" y="126" font-size="44" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#0F172A">{title}</text>
    <text x="60" y="166" font-size="20" font-family="'Microsoft YaHei', Arial" fill="#6C757D">{kicker}</text>
  </g>

  <!-- 6 Feature Cards in Paper-cut Style -->
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

  <g id="card-06" data-pptx-bounds="850 355 370 135">
    <rect x="860" y="359" width="360" height="131" rx="12" fill="#E2DDD5"/>
    <rect x="860" y="355" width="360" height="131" rx="12" fill="#FFFFFF" stroke="#8F2D56" stroke-width="1.5"/>
    <rect x="878" y="368" width="28" height="28" rx="6" fill="#8F2D56"/>
    <text x="892" y="388" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">06</text>
    <text x="916" y="389" font-size="20" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56">Blob下载与异常反解</text>
    <text x="878" y="424" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      <tspan x="878" dy="0">RFC 5987 文件名 UTF-8 解码，</tspan>
      <tspan x="878" dy="22">后端报错时反解 Blob 内嵌 JSON 错误信息。</tspan>
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
</svg>'''

def render_three_col(s):
    cards = s.get("cards", [])
    colors = ["#8F2D56", "#218380", "#D81159"]
    role = s.get("role", "content")
    
    cards_svg = ""
    xs = [60, 460, 860]
    for i, c in enumerate(cards[:3]):
        c_title, c_desc, c_col = c[0], c[1], c[2] if len(c) > 2 else colors[i % len(colors)]
        x = xs[i]
        cid = f"card-0{i+1}"
        
        # Wrap card title to prevent overflow beyond 360px bounds
        t_lines = wrap_lines(c_title, 260, size=18.0, family="'Microsoft YaHei', Arial")
        if len(t_lines) == 1:
            title_svg = f'<text x="{x+60}" y="232" font-size="18" font-family="\'Microsoft YaHei\', Arial" font-weight="bold" fill="{c_col}">{esc(t_lines[0])}</text>'
        else:
            title_svg = f'''<text x="{x+60}" y="222" font-size="15" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="{c_col}">
      <tspan x="{x+60}" dy="0">{esc(t_lines[0])}</tspan>
      <tspan x="{x+60}" dy="19">{esc(t_lines[1])}</tspan>
    </text>'''
            
        # Wrap description text
        lines = wrap_lines(c_desc, 310, size=14.0, family="'Microsoft YaHei', Arial")
        tspans = ""
        for li, line in enumerate(lines[:8]):
            dy = 0 if li == 0 else 22
            tspans += f'<tspan x="{x+24}" dy="{dy}">{esc(line)}</tspan>'
            
        cards_svg += f'''  <!-- Column {i+1} Card -->
  <g id="{cid}" data-pptx-bounds="{x} 190 360 375">
    <rect x="{x}" y="194" width="360" height="371" rx="14" fill="#E2DDD5"/>
    <rect x="{x}" y="190" width="360" height="371" rx="14" fill="#FFFFFF" stroke="{c_col}" stroke-width="1.5"/>
    <rect x="{x+20}" y="210" width="32" height="32" rx="8" fill="{c_col}"/>
    <text x="{x+36}" y="232" font-size="16" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">0{i+1}</text>
    {title_svg}
    <line x1="{x+20}" y1="258" x2="{x+340}" y2="258" stroke="#E2DDD5" stroke-width="1"/>
    <text x="{x+24}" y="290" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      {tspans}
    </text>
  </g>
'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
{render_header(s, s["num"])}
{cards_svg}
{render_summary(s)}
{render_footer(s["num"])}
</svg>'''

def render_four_quadrant(s):
    cards = s.get("cards", [])
    colors = ["#D81159", "#8F2D56", "#FFBC42", "#218380"]
    role = s.get("role", "content")
    
    positions = [
        (60, 190, 560, 180),
        (660, 190, 560, 180),
        (60, 385, 560, 180),
        (660, 385, 560, 180)
    ]
    
    cards_svg = ""
    for i, c in enumerate(cards[:4]):
        c_title, c_desc, c_col = c[0], c[1], c[2] if len(c) > 2 else colors[i % len(colors)]
        x, y, w, h = positions[i]
        cid = f"quad-card-0{i+1}"
        
        lines = wrap_lines(c_desc, 490, size=14.0, family="'Microsoft YaHei', Arial")
        tspans = ""
        for li, line in enumerate(lines[:4]):
            dy = 0 if li == 0 else 22
            tspans += f'<tspan x="{x+24}" dy="{dy}">{esc(line)}</tspan>'
            
        cards_svg += f'''  <!-- Quadrant {i+1} Card -->
  <g id="{cid}" data-pptx-bounds="{x} {y} {w} {h}">
    <rect x="{x}" y="{y+4}" width="{w}" height="{h-4}" rx="12" fill="#E2DDD5"/>
    <rect x="{x}" y="{y}" width="{w}" height="{h-4}" rx="12" fill="#FFFFFF" stroke="{c_col}" stroke-width="1.5"/>
    <rect x="{x+20}" y="{y+16}" width="28" height="28" rx="6" fill="{c_col}"/>
    <text x="{x+34}" y="{y+36}" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">0{i+1}</text>
    <text x="{x+58}" y="{y+37}" font-size="18" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="{c_col}">{esc(c_title)}</text>
    <text x="{x+24}" y="{y+75}" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      {tspans}
    </text>
  </g>
'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
{render_header(s, s["num"])}
{cards_svg}
{render_summary(s)}
{render_footer(s["num"])}
</svg>'''

def render_four_layers(s):
    layers = s.get("layers", [])
    colors = ["#8F2D56", "#218380", "#D81159", "#73D2DE"]
    role = s.get("role", "content")
    
    layers_svg = ""
    for i, l in enumerate(layers[:4]):
        l_title, l_desc = l[0], l[1]
        c_col = colors[i % len(colors)]
        y = 190 + i * 94
        lid = f"layer-row-0{i+1}"
        
        # Safe text wrap for description
        lines = wrap_lines(l_desc, 720, size=14.0, family="'Microsoft YaHei', Arial")
        if len(lines) > 1:
            desc_text = f'''<text x="430" y="{y+36}" font-size="13" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      <tspan x="430" dy="0">{esc(lines[0])}</tspan>
      <tspan x="430" dy="20">{esc(lines[1])}</tspan>
    </text>'''
        else:
            desc_text = f'''<text x="430" y="{y+46}" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">{esc(lines[0])}</text>'''

        layers_svg += f'''  <!-- Layer {i+1} Strip -->
  <g id="{lid}" data-pptx-bounds="60 {y} 1160 84">
    <rect x="60" y="{y+4}" width="1160" height="80" rx="12" fill="#E2DDD5"/>
    <rect x="60" y="{y}" width="1160" height="80" rx="12" fill="#FFFFFF" stroke="{c_col}" stroke-width="1.5"/>
    <rect x="76" y="{y+16}" width="330" height="48" rx="8" fill="{c_col}" opacity="0.12"/>
    <rect x="76" y="{y+16}" width="8" height="48" rx="4" fill="{c_col}"/>
    <text x="96" y="{y+46}" font-size="17" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="{c_col}">{esc(l_title)}</text>
    {desc_text}
  </g>
'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
{render_header(s, s["num"])}
{layers_svg}
{render_summary(s)}
{render_footer(s["num"])}
</svg>'''

def render_pipeline(s):
    steps = s.get("steps", [])
    n_steps = len(steps)
    colors = ["#8F2D56", "#D81159", "#218380", "#FFBC42", "#73D2DE"]
    
    if n_steps == 5:
        w_step = 216
        gap = 20
        x_start = 60
    elif n_steps == 4:
        w_step = 275
        gap = 20
        x_start = 60
    else:
        w_step = 360
        gap = 40
        x_start = 60
        
    steps_svg = ""
    for i, step in enumerate(steps):
        x = x_start + i * (w_step + gap)
        s_title, s_sub, s_desc = step[0], step[1], step[2] if len(step) > 2 else ""
        c_col = colors[i % len(colors)]
        sid = f"pipe-step-0{i+1}"
        
        lines = wrap_lines(s_desc, w_step - 30, size=13.0, family="'Microsoft YaHei', Arial")
        tspans = ""
        for li, line in enumerate(lines[:6]):
            dy = 0 if li == 0 else 20
            tspans += f'<tspan x="{x+15}" dy="{dy}">{esc(line)}</tspan>'
            
        steps_svg += f'''  <!-- Step {i+1} Card -->
  <g id="{sid}" data-pptx-bounds="{x} 190 {w_step} 370">
    <rect x="{x}" y="194" width="{w_step}" height="366" rx="12" fill="#E2DDD5"/>
    <rect x="{x}" y="190" width="{w_step}" height="366" rx="12" fill="#FFFFFF" stroke="{c_col}" stroke-width="1.5"/>
    <circle cx="{x+28}" cy="222" r="14" fill="{c_col}"/>
    <text x="{x+28}" y="227" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">0{i+1}</text>
    <text x="{x+50}" y="228" font-size="16" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="{c_col}">{esc(s_title)}</text>
    <rect x="{x+15}" y="250" width="{w_step-30}" height="30" rx="6" fill="#F1EFE8"/>
    <text x="{x+w_step/2}" y="270" font-size="13" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#2B2D42" text-anchor="middle">{esc(s_sub)}</text>
    <line x1="{x+15}" y1="295" x2="{x+w_step-15}" y2="295" stroke="#E2DDD5" stroke-width="1"/>
    <text x="{x+15}" y="325" font-size="13" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      {tspans}
    </text>
  </g>
'''
        # Arrow connector between cards
        if i < n_steps - 1:
            ax = x + w_step + 4
            steps_svg += f'''  <path id="arrow-{i+1}" d="M {ax},360 L {ax+10},368 L {ax},376 Z" fill="{c_col}" opacity="0.8" data-pptx-role="decoration"/>\n'''

    role = s.get("role", "content")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
{render_header(s, s["num"])}
{steps_svg}
{render_summary(s)}
{render_footer(s["num"])}
</svg>'''

def render_two_col_code(s):
    lt = esc(s.get("left_title", "Before"))
    lc = s.get("left_code", "")
    rt = esc(s.get("right_title", "After"))
    rc = s.get("right_code", "")
    role = s.get("role", "content")
    
    def render_code_box(x, y, w, h, title, code_str, cid, border_col):
        raw_lines = code_str.strip().split("\n")
        code_tspans = ""
        for idx, line in enumerate(raw_lines[:12]):
            dy = 0 if idx == 0 else 22
            # Line number + code
            code_tspans += f'<tspan x="{x+20}" dy="{dy}"><tspan fill="#6C757D">{idx+1:2d} </tspan><tspan fill="#E2E8F0">{esc(line)}</tspan></tspan>'
            
        return f'''  <!-- Code Card {cid} -->
  <g id="{cid}" data-pptx-bounds="{x} {y} {w} {h}">
    <rect x="{x}" y="{y+4}" width="{w}" height="{h-4}" rx="12" fill="#E2DDD5"/>
    <rect x="{x}" y="{y}" width="{w}" height="{h-4}" rx="12" fill="#2B2D42" stroke="{border_col}" stroke-width="1.5"/>
    <!-- Window Bar -->
    <rect x="{x}" y="{y}" width="{w}" height="36" rx="12" fill="#1E1E2E"/>
    <circle cx="{x+20}" cy="{y+18}" r="5" fill="#EF4444"/>
    <circle cx="{x+35}" cy="{y+18}" r="5" fill="#F59E0B"/>
    <circle cx="{x+50}" cy="{y+18}" r="5" fill="#10B981"/>
    <text x="{x+w/2}" y="{y+23}" font-size="13" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#CBD5E1" text-anchor="middle">{title}</text>
    <!-- Code Area -->
    <text x="{x+20}" y="{y+68}" font-size="13" font-family="'Microsoft YaHei', Consolas, monospace">
      {code_tspans}
    </text>
  </g>
'''

    left_svg = render_code_box(60, 190, 560, 375, lt, lc, "code-box-left", "#8F2D56")
    right_svg = render_code_box(660, 190, 560, 375, rt, rc, "code-box-right", "#218380")
    
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
{render_header(s, s["num"])}
{left_svg}
{right_svg}
{render_summary(s)}
{render_footer(s["num"])}
</svg>'''

def render_code_highlight(s):
    code_str = s.get("code", "")
    role = s.get("role", "content")
    raw_lines = code_str.strip().split("\n")
    code_tspans = ""
    for idx, line in enumerate(raw_lines[:13]):
        dy = 0 if idx == 0 else 24
        # syntax highlight comments
        c_fill = "#A0AEC0" if line.strip().startswith("//") or line.strip().startswith("/*") else "#E2E8F0"
        code_tspans += f'<tspan x="85" dy="{dy}"><tspan fill="#64748B">{idx+1:2d}  </tspan><tspan fill="{c_fill}">{esc(line)}</tspan></tspan>'
        
    code_box = f'''  <!-- Code Highlight Container -->
  <g id="code-main-container" data-pptx-bounds="60 190 1160 375">
    <rect x="60" y="194" width="1160" height="371" rx="14" fill="#E2DDD5"/>
    <rect x="60" y="190" width="1160" height="371" rx="14" fill="#2B2D42" stroke="#8F2D56" stroke-width="1.5"/>
    <rect x="60" y="190" width="1160" height="36" rx="14" fill="#1E1E2E"/>
    <circle cx="85" cy="208" r="5" fill="#EF4444"/>
    <circle cx="100" cy="208" r="5" fill="#F59E0B"/>
    <circle cx="115" cy="208" r="5" fill="#10B981"/>
    <text x="640" y="213" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#CBD5E1" text-anchor="middle">TypeScript 源码实现 · 核心切面</text>
    <text x="85" y="260" font-size="14" font-family="'Microsoft YaHei', Consolas, monospace">
      {code_tspans}
    </text>
  </g>
'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
{render_header(s, s["num"])}
{code_box}
{render_summary(s)}
{render_footer(s["num"])}
</svg>'''

def render_queue_swimlane(s):
    # Slide 11: Queue Swimlane
    items = s.get("items", [])
    role = s.get("role", "content")
    
    lanes_svg = ""
    boxes = [
        ("阶段一：主请求 401 触发", "Req #1 请求返回 401\n切入响应拦截器分支\n触发 handleTokenRefresh()", "#8F2D56", 60),
        ("阶段二：isRefreshing 互斥锁", "判断 isRefreshing === false\n立即置为 true 锁定状态\n调用 /api/auth/refresh 刷新", "#D81159", 355),
        ("阶段三：并发请求队列挂起", "Req #2, #3, #4 并发到达\n发现 isRefreshing === true\n返回未决 Promise 压入 retryQueue", "#FFBC42", 650),
        ("阶段四：全队列批量 Replay", "新 Token 换回成功\n遍历 retryQueue(newToken)\n批量完成重发并交付页面", "#218380", 945)
    ]
    
    for i, b in enumerate(boxes):
        title, text, col, x = b
        
        # Wrap title
        t_lines = wrap_lines(title, 205, size=15.0, family="'Microsoft YaHei', Arial")
        if len(t_lines) == 1:
            title_svg = f'<text x="{x+50}" y="230" font-size="15" font-family="\'Microsoft YaHei\', Arial" font-weight="bold" fill="{col}">{esc(t_lines[0])}</text>'
        else:
            title_svg = f'''<text x="{x+50}" y="222" font-size="13" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="{col}">
      <tspan x="{x+50}" dy="0">{esc(t_lines[0])}</tspan>
      <tspan x="{x+50}" dy="18">{esc(t_lines[1])}</tspan>
    </text>'''
            
        paragraphs = text.split("\n")
        all_lines = []
        for p in paragraphs:
            if not p.strip(): continue
            all_lines.extend(wrap_lines(p, 230, size=13.0, family="'Microsoft YaHei', Arial"))
            
        tspans = ""
        for li, line in enumerate(all_lines[:6]):
            dy = 0 if li == 0 else 22
            tspans += f'<tspan x="{x+18}" dy="{dy}">{esc(line)}</tspan>'
            
        lanes_svg += f'''  <!-- Swimlane Step {i+1} -->
  <g id="lane-step-0{i+1}" data-pptx-bounds="{x} 190 275 375">
    <rect x="{x}" y="194" width="275" height="371" rx="14" fill="#E2DDD5"/>
    <rect x="{x}" y="190" width="275" height="371" rx="14" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>
    <rect x="{x+16}" y="210" width="28" height="28" rx="6" fill="{col}"/>
    <text x="{x+30}" y="230" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">0{i+1}</text>
    {title_svg}
    <line x1="{x+16}" y1="255" x2="{x+259}" y2="255" stroke="#E2DDD5" stroke-width="1"/>
    <text x="{x+18}" y="295" font-size="13" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      {tspans}
    </text>
  </g>
'''
        if i < 3:
            ax = x + 277
            lanes_svg += f'''  <path id="lane-arrow-{i+1}" d="M {ax},360 L {ax+8},368 L {ax},376 Z" fill="{col}" opacity="0.8" data-pptx-role="decoration"/>\n'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
{render_header(s, s["num"])}
{lanes_svg}
{render_summary(s)}
{render_footer(s["num"])}
</svg>'''

def render_two_col_compare(s):
    # Slide 12 or 25
    lt = esc(s.get("left_title", "Anti-pattern"))
    lx = s.get("left_text", "")
    lc = s.get("left_color", "#8F2D56")
    rt = esc(s.get("right_title", "Best Practice"))
    rx = s.get("right_text", "")
    rc = s.get("right_color", "#218380")
    role = s.get("role", "content")
    
    def render_card(x, y, w, h, title, text, col, cid):
        paragraphs = text.split("\n")
        all_lines = []
        for p in paragraphs:
            if not p.strip(): continue
            all_lines.extend(wrap_lines(p, w - 60, size=14.0, family="'Microsoft YaHei', Arial"))
            
        tspans = ""
        for idx, line in enumerate(all_lines[:12]):
            dy = 0 if idx == 0 else 24
            tspans += f'<tspan x="{x+24}" dy="{dy}">{esc(line)}</tspan>'
            
        return f'''  <!-- Compare Card {cid} -->
  <g id="{cid}" data-pptx-bounds="{x} {y} {w} {h}">
    <rect x="{x}" y="{y+4}" width="{w}" height="{h-4}" rx="14" fill="#E2DDD5"/>
    <rect x="{x}" y="{y}" width="{w}" height="{h-4}" rx="14" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>
    <rect x="{x+20}" y="{y+20}" width="{w-40}" height="40" rx="8" fill="{col}" opacity="0.12"/>
    <rect x="{x+20}" y="{y+20}" width="8" height="40" rx="4" fill="{col}"/>
    <text x="{x+40}" y="{y+46}" font-size="18" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="{col}">{title}</text>
    <line x1="{x+20}" y1="{y+75}" x2="{x+w-20}" y2="{y+75}" stroke="#E2DDD5" stroke-width="1"/>
    <text x="{x+24}" y="{y+110}" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      {tspans}
    </text>
  </g>
'''

    left_svg = render_card(60, 190, 560, 375, lt, lx, lc, "compare-card-left")
    right_svg = render_card(660, 190, 560, 375, rt, rx, rc, "compare-card-right")
    
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
{render_header(s, s["num"])}
{left_svg}
{right_svg}
{render_summary(s)}
{render_footer(s["num"])}
</svg>'''

def render_timeline_flaw(s):
    # Slide 17: Timeline flaw
    role = s.get("role", "content")
    flaws_svg = f'''  <!-- Visual Timeline Diagram -->
  <g id="timeline-visual" data-pptx-bounds="60 190 1160 375">
    <rect x="60" y="194" width="1160" height="371" rx="14" fill="#E2DDD5"/>
    <rect x="60" y="190" width="1160" height="371" rx="14" fill="#FFFFFF" stroke="#8F2D56" stroke-width="1.5"/>
    
    <!-- Timeline Title -->
    <text x="85" y="230" font-size="18" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56">时序对比：并发请求下的 Loading 状态劫持现场</text>
    <line x1="85" y1="248" x2="1195" y2="248" stroke="#E2DDD5" stroke-width="1"/>
    
    <!-- Request Bars -->
    <text x="85" y="285" font-size="14" font-family="'Microsoft YaHei', Consolas, monospace" font-weight="bold" fill="#2B2D42">请求 A (耗时 100ms)</text>
    <rect x="260" y="270" width="220" height="24" rx="6" fill="#8F2D56" opacity="0.8"/>
    <text x="370" y="287" font-size="12" font-family="'Microsoft YaHei', Arial" fill="#FFFFFF" text-anchor="middle">执行中 (100ms 完成)</text>
    
    <text x="85" y="335" font-size="14" font-family="'Microsoft YaHei', Consolas, monospace" font-weight="bold" fill="#2B2D42">请求 B (耗时 300ms)</text>
    <rect x="260" y="320" width="540" height="24" rx="6" fill="#218380" opacity="0.8"/>
    <text x="530" y="337" font-size="12" font-family="'Microsoft YaHei', Arial" fill="#FFFFFF" text-anchor="middle">执行中 (300ms 完成)</text>

    <text x="85" y="385" font-size="14" font-family="'Microsoft YaHei', Consolas, monospace" font-weight="bold" fill="#2B2D42">请求 C (耗时 500ms)</text>
    <rect x="260" y="370" width="860" height="24" rx="6" fill="#FFBC42" opacity="0.8"/>
    <text x="690" y="387" font-size="12" font-family="'Microsoft YaHei', Arial" fill="#FFFFFF" text-anchor="middle">执行中 (500ms 完成)</text>
    
    <line x1="85" y1="415" x2="1195" y2="415" stroke="#E2DDD5" stroke-dasharray="4 4" stroke-width="1"/>
    
    <!-- Contrast 1: Single Boolean -->
    <text x="85" y="450" font-size="15" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#D81159">单布尔值致命缺陷：</text>
    <text x="240" y="450" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">100ms 请求 A 完成时直接调用 loading.close()，导致遮罩过早消失！请求 B/C 仍在执行中，用户以为加载完毕重复狂点。</text>

    <!-- Contrast 2: Counter Pattern -->
    <text x="85" y="495" font-size="15" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#218380">计数器模型完美解法：</text>
    <text x="240" y="495" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">请求 A/B/C 发起时 counter = 3；A 完成 counter=2；B 完成 counter=1；直到 500ms C 完成 counter=0 时才关闭遮罩！</text>
  </g>
'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{role}">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 380,0 C 330,180 460,260 360,440 C 280,580 400,680 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 200,0 C 160,200 260,320 170,500 C 120,620 200,680 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
{render_header(s, s["num"])}
{flaws_svg}
{render_summary(s)}
{render_footer(s["num"])}
</svg>'''

def render_ending(s):
    # Slide 30
    badge = esc(s.get("badge", "总结回顾 · 架构进阶"))
    title = esc(s.get("title", "课程全景回顾与进阶学习指南"))
    kicker = esc(s.get("kicker", "掌握网络层工业级封装，奠定前端架构坚实基石"))
    pillars = s.get("pillars", [
        ("实例与切面隔离", "主 service 与 refreshService 隔离，拦截器双向管道精准解耦"),
        ("高并发无感刷新", "401 拦截 + isRefreshing 互斥锁 + retryQueue 并发队列重发"),
        ("全链路容错与兜底", "AbortController 防重复 + 计数器 Loading + 指数退避重试 + Blob 流反解"),
        ("TypeScript 架构工程", "AxiosRequestConfig 模块扩展声明合并 + 泛型业务契约安全")
    ])
    
    pillars_svg = ""
    xs = [60, 355, 650, 945]
    colors = ["#8F2D56", "#D81159", "#218380", "#FFBC42"]
    for i, p in enumerate(pillars[:4]):
        p_title, p_desc = p[0], p[1]
        col = colors[i]
        x = xs[i]
        
        t_lines = wrap_lines(p_title, 195, size=15.0, family="'Microsoft YaHei', Arial")
        if len(t_lines) == 1:
            title_svg = f'<text x="{x+56}" y="232" font-size="15" font-family="\'Microsoft YaHei\', Arial" font-weight="bold" fill="{col}">{esc(t_lines[0])}</text>'
        else:
            title_svg = f'''<text x="{x+56}" y="222" font-size="13" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="{col}">
      <tspan x="{x+56}" dy="0">{esc(t_lines[0])}</tspan>
      <tspan x="{x+56}" dy="18">{esc(t_lines[1])}</tspan>
    </text>'''
            
        lines = wrap_lines(p_desc, 235, size=14.0, family="'Microsoft YaHei', Arial")
        tspans = ""
        for li, line in enumerate(lines[:5]):
            dy = 0 if li == 0 else 22
            tspans += f'<tspan x="{x+18}" dy="{dy}">{esc(line)}</tspan>'
            
        pillars_svg += f'''  <!-- Pillar {i+1} -->
  <g id="ending-pillar-0{i+1}" data-pptx-bounds="{x} 190 275 300">
    <rect x="{x}" y="194" width="275" height="296" rx="14" fill="#E2DDD5"/>
    <rect x="{x}" y="190" width="275" height="296" rx="14" fill="#FFFFFF" stroke="{col}" stroke-width="1.5"/>
    <rect x="{x+16}" y="210" width="32" height="32" rx="8" fill="{col}"/>
    <text x="{x+32}" y="232" font-size="16" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">0{i+1}</text>
    {title_svg}
    <line x1="{x+16}" y1="258" x2="{x+259}" y2="258" stroke="#E2DDD5" stroke-width="1"/>
    <text x="{x+18}" y="295" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      {tspans}
    </text>
  </g>
'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="ending">
  <rect id="bg-canvas" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <path id="deco-sheet-1" d="M 0,0 L 400,0 C 350,180 480,260 380,440 C 300,580 420,680 320,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2" d="M 0,0 L 220,0 C 180,200 280,320 190,500 C 130,620 220,680 180,720 L 0,720 Z" fill="#8F2D56" opacity="0.06" data-pptx-role="decoration"/>
  
  <!-- Header Group -->
  <g id="header-group" data-pptx-bounds="60 42 1160 140">
    <rect x="60" y="42" width="240" height="30" rx="15" fill="#8F2D56"/>
    <text x="180" y="62" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{badge}</text>
    <text x="60" y="118" font-size="44" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#0F172A">{title}</text>
    <text x="60" y="158" font-size="20" font-family="'Microsoft YaHei', Arial" fill="#6C757D">{kicker}</text>
  </g>

{pillars_svg}

  <!-- Q&A and Resources Banner -->
  <g id="ending-banner" data-pptx-bounds="60 515 1160 140">
    <rect x="60" y="519" width="1160" height="136" rx="14" fill="#E2DDD5"/>
    <rect x="60" y="515" width="1160" height="136" rx="14" fill="#F1EFE8" stroke="#8F2D56" stroke-width="1.5"/>
    <text x="90" y="555" font-size="20" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56">🎓 课后实操建议与答疑互动 (Q&amp;A)</text>
    <text x="90" y="590" font-size="15" font-family="'Microsoft YaHei', Arial" fill="#2B2D42">
      <tspan x="90" dy="0">1. 克隆代码仓库并在本地运行 npm run dev 与 node server/index.js 进行抓包复现验证；</tspan>
      <tspan x="90" dy="25">2. 动手为请求库扩展自定义加密拦截器或离线请求持久化缓存功能，巩固切面编程思维！</tspan>
    </text>
    <text x="90" y="635" font-size="14" font-family="'Microsoft YaHei', Consolas, monospace" font-weight="bold" fill="#6C757D">GitHub Repository: https://github.com/teaching-demo/axios-enterprise-ts</text>
  </g>

  <!-- Footer Group -->
  <g id="footer-group" data-pptx-bounds="60 675 1160 30">
    <text x="60" y="692" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#6C757D">感谢大家的聆听！祝愿各位同学在技术架构之路上越走越稳！</text>
    <text x="1220" y="692" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56" text-anchor="end">30 / 30</text>
  </g>
</svg>'''

def generate_notes_total(slides):
    notes_content = "# Axios 工业级深度封装与 TypeScript 架构实训 讲师逐字稿讲义\n\n"
    for s in slides:
        num = s["num"]
        title = s.get("title", "")
        note_txt = s.get("notes", "").strip()
        notes_content += f"## Slide {num:02d} - {title}\n\n{note_txt}\n\n---\n\n"
        
        # also write individual note file
        n_file = os.path.join(notes_dir, f"slide_{num:02d}.md")
        with open(n_file, "w", encoding="utf-8") as f:
            f.write(f"# Slide {num:02d}: {title}\n\n{note_txt}\n")
            
    total_file = os.path.join(notes_dir, "total.md")
    with open(total_file, "w", encoding="utf-8") as f:
        f.write(notes_content)
    print(f"[OK] Generated notes/total.md and individual notes in {notes_dir}")

def generate_slides(start_num, end_num):
    import subprocess
    for s in cfg.slides_data:
        num = s["num"]
        if start_num <= num <= end_num:
            svg_content = render_slide(s)
            svg_path = os.path.join(svg_dir, f"slide_{num:02d}.svg")
            with open(svg_path, "w", encoding="utf-8") as f:
                f.write(svg_content)
            print(f"[OK] Rendered slide_{num:02d}.svg")
            
    # Automatically run compact_svg_styles to normalize typography defaults
    try:
        compact_script = "D:/Zpan/ppt-master/skills/ppt-master/scripts/compact_svg_styles.py"
        if os.path.exists(compact_script):
            subprocess.run([sys.executable, compact_script, svg_dir, "--inplace"], check=True)
            print("[OK] Normalized SVG typography with compact_svg_styles")
    except Exception as e:
        print(f"[WARN] compact_svg_styles failed: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=30)
    parser.add_argument("--notes", action="store_true")
    args = parser.parse_args()
    
    generate_slides(args.start, args.end)
    if args.notes:
        generate_notes_total(cfg.slides_data)
