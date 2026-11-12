# -*- coding: utf-8 -*-
import os

project_dir = "c:/Users/Administrator/Desktop/Axios/projects/axios_teaching_ppt169_20261112"
svg_dir = os.path.join(project_dir, "svg_output")
notes_dir = os.path.join(project_dir, "notes")
os.makedirs(svg_dir, exist_ok=True)
os.makedirs(notes_dir, exist_ok=True)

# Helper for XML escaping
def esc(txt):
    return str(txt).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# Global base svg generator
def make_svg_wrapper(slide_num, page_role, content_xml):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" data-pptx-page-role="{page_role}">
  <!-- Background Paper Layer -->
  <rect id="bg-canvas-{slide_num:02d}" width="1280" height="720" fill="#FAF9F5" data-pptx-role="background"/>
  <!-- Decorative Cut Paper Sheets -->
  <path id="deco-sheet-1-{slide_num:02d}" d="M 0,0 L 380,0 C 330,160 440,240 360,400 C 280,540 380,640 300,720 L 0,720 Z" fill="#F1EFE8" opacity="0.6" data-pptx-role="decoration"/>
  <path id="deco-sheet-2-{slide_num:02d}" d="M 0,0 L 200,0 C 160,180 260,280 180,460 C 120,580 200,640 160,720 L 0,720 Z" fill="#8F2D56" opacity="0.05" data-pptx-role="decoration"/>
{content_xml}
  <!-- Footer Group -->
  <g id="footer-group-{slide_num:02d}" data-pptx-bounds="60 670 1160 30">
    <text x="60" y="688" font-size="14" font-family="'Microsoft YaHei', Arial" fill="#6C757D">Axios 工业级深度封装与 TypeScript 架构实战</text>
    <text x="1220" y="688" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#8F2D56" text-anchor="end">{slide_num:02d} / 30</text>
  </g>
</svg>"""

def make_header(slide_num, badge_text, title_text, kicker_text):
    badge_w = max(200, len(badge_text) * 16 + 40)
    return f"""  <!-- Header Group -->
  <g id="header-group-{slide_num:02d}" data-pptx-bounds="60 44 1160 144">
    <rect x="60" y="44" width="{badge_w}" height="28" rx="14" fill="#8F2D56"/>
    <text x="{60 + badge_w // 2}" y="63" font-size="14" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{esc(badge_text)}</text>
    <text x="60" y="118" font-size="34" font-family="'Microsoft YaHei', Arial" font-weight="bold" fill="#0F172A">{esc(title_text)}</text>
    <text x="60" y="152" font-size="16" font-family="'Microsoft YaHei', Arial" fill="#6C757D">{esc(kicker_text)}</text>
  </g>"""

print("Helper definitions loaded.")

