# -*- coding: utf-8 -*-
"""第117回。体の部位・症状・手当ての道具。
部位は「大きな顔や体を描いて矢印でそこを指す」型でそろえる。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))

def bighead(x=250, y=210, r=130):
    """正面向きの大きな顔。部位を指すための土台。"""
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M0-{r}q{r*0.82} 0 {r*0.82} {r*0.72}q0 {r*0.86}-{r*0.82} {r*0.86}'
            f'q-{r*0.82} 0-{r*0.82}-{r*0.86}q0-{r*0.72} {r*0.82}-{r*0.72}z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-{r*0.86}-{r*0.3}q4-{r*0.86} {r*0.86}-{r*0.86}t{r*0.86} {r*0.86}q-{r*0.3}-{r*0.24}-{r*0.86}-{r*0.1}'
            f'q-{r*0.4}-{r*0.2}-{r*0.86} {r*0.1}z" fill="{HAIR}" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="-{r*0.34}" cy="-{r*0.1}" r="{r*0.075}" fill="{INK}"/>'
            f'<circle cx="{r*0.34}" cy="-{r*0.1}" r="{r*0.075}" fill="{INK}"/>'
            f'<path d="M-{r*0.3} {r*0.36}q{r*0.3} {r*0.2} {r*0.6} 0" fill="none" stroke="{INK}" stroke-width="{r*0.05}" stroke-linecap="round"/>'
            f'</g>')

def point(x1, y1, x2, y2):
    return f'<g class="a" marker-end="url(#ar)"><path d="M{x1} {y1}L{x2} {y2}"/></g>'

# --- 顔まわりの部位 ---------------------------------------------------------
add('jaw', '顔の下半分のあごの骨の輪郭が線でなぞられている', f'''
{bighead()}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M144 208q0 108-144 108T-44 208" transform="translate(0 0)"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M146 208q-4 106-146 106"/>
</g>
{point(470, 300, 380, 288)}''', arrow=True, ground=False)

add('chin', 'あごの先だけが丸く示されている', f'''
{bighead()}
<circle cx="250" cy="318" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
{point(470, 344, 292, 326)}''', arrow=True, ground=False)

add('forehead', '額に手のひらが当てられている', f'''
{bighead()}
<path d="M170 128q80-34 160 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
{hand(400, 126, -1)}
{point(490, 96, 430, 116)}''', arrow=True, ground=False)

add('eyebrow', '片方のまゆ毛が濃く描かれている', f'''
{bighead()}
<g fill="{HAIR}" stroke="{INK}" stroke-width="2">
  <path d="M186 172q28-18 56-2l-4 14q-24-12-50 2z"/>
  <path d="M262 170q28-16 56 2l-2 14q-26-14-50-2z"/>
</g>
<circle cx="214" cy="176" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
{point(452, 132, 244, 166)}''', arrow=True, ground=False)

add('eyelid', '片目が閉じられ、まぶたが下りている', f'''
{bighead()}
<path d="M180 194q34-4 62 4-30 12-62-4z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
<path d="M180 198q32 12 62 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<circle cx="211" cy="198" r="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
{point(452, 150, 246, 186)}''', arrow=True, ground=False)

add('eyelash', '目のふちに細いまつ毛が並んでいる', f'''
{bighead()}
<g fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round">
  <path d="M182 186l-12-14M198 180l-8-16M214 178l-2-18M230 180l6-16M246 186l12-14"/>
  <path d="M270 186l-12-14M286 180l-8-16M302 178l-2-18M318 180l6-16M334 186l12-14"/>
</g>
<circle cx="214" cy="184" r="36" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
{point(456, 134, 248, 172)}''', arrow=True, ground=False)

add('nostril', '鼻の下の二つの穴が示されている', f'''
{bighead()}
<path d="M250 200v42q0 12-14 14" fill="none" stroke="{SKINL}" stroke-width="4" stroke-linecap="round"/>
<g fill="{INK}">
  <ellipse cx="236" cy="258" rx="9" ry="6"/><ellipse cx="264" cy="258" rx="9" ry="6"/>
</g>
<ellipse cx="250" cy="258" rx="34" ry="18" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
{point(468, 234, 292, 254)}''', arrow=True, ground=False)

add('gum', '開いた口の中で歯を支えるピンクの歯ぐきが見えている', f'''
<g transform="translate(300 200)">
  <path d="M-160 0q0-90 160-90t160 90q0 90-160 90T-160 0z" fill="{SKINL}" class="o"/>
  <path d="M-130 0q0-70 130-70t130 70q0 70-130 70T-130 0z" fill="#8b3a3a" class="o"/>
  <path d="M-124-14q10-52 124-52t124 52q-14 24-124 24T-124-14z" fill="#f0a6a6" class="o"/>
  <path d="M-124 14q10 52 124 52t124-52q-14-24-124-24T-124 14z" fill="#f0a6a6" class="o"/>
  <g fill="#fffefd" stroke="{INK}" stroke-width="2">
''' + ''.join(f'<rect x="{-108+i*27}" y="-26" width="22" height="26" rx="5"/>' for i in range(8)) + ''.join(f'<rect x="{-108+i*27}" y="0" width="22" height="26" rx="5"/>' for i in range(8)) + f'''
  </g>
</g>
{point(470, 108, 396, 158)}''', arrow=True, ground=False)

add('collarbone', '胸の上部を横切る二本の鎖骨', f'''
<g transform="translate(300 210)">
  <path d="M0-130q46 0 46 44 0 30-20 44 70 20 70 80v72h-192v-72q0-60 70-80-20-14-20-44 0-44 46-44z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round">
    <path d="M-6-6q-30 16-72 12M6-6q30 16 72 12"/>
  </g>
  <circle r="8" class="coral o"/>
</g>
{point(500, 120, 400, 200)}''', arrow=True, ground=False)

add('fingernail', '指の先のつめが示されている', f'''
<g transform="translate(300 220) rotate(-20)">
  <path d="M-150 40q-20-40 20-56l180-30q40-8 46 24t-34 42l-180 32q-24 4-32-12z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse cx="86" cy="-20" rx="34" ry="24" fill="#fbe3d6" stroke="{SKINL}" stroke-width="3" transform="rotate(-10 86 -20)"/>
  <path d="M60-32q26-12 52 4" fill="none" stroke="{SKINL}" stroke-width="3"/>
</g>
{point(500, 90, 418, 156)}''', arrow=True, ground=False)

add('waist', '胴のいちばん細いところにベルトが巻かれている', f'''
<g transform="translate(300 200)">
  <path d="M-70-140h140q10 60-30 92 44 22 44 78v130h-168v-130q0-56 44-78-40-32-30-92z" fill="{TONES['teal'][1]}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-46-40h92v22h-92z" fill="#5b4a3c" class="o"/>
  <rect x="-14" y="-44" width="28" height="30" rx="4" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
</g>
{point(500, 128, 372, 156)}''', arrow=True, ground=False)

add('thigh', '脚の膝から上の太い部分が示されている', f'''
<g transform="translate(300 60)">
  <path d="M-60 0h120v60q0 40-14 70l-10 40h-72l-10-40q-14-30-14-70z" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-56 170h48l10 90h-48zM8 170h48l-10 90h-48z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse cx="-30" cy="170" rx="26" ry="10" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="32" cy="170" rx="26" ry="10" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<ellipse cx="270" cy="150" rx="46" ry="60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
{point(486, 120, 322, 144)}''', arrow=True, ground=False)

add('shin', '膝から下、すねの前面が示されている', f'''
<g transform="translate(300 40)">
  <path d="M-54 0h108v90h-108z" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="2.5"/>
  <ellipse cx="-26" cy="96" rx="26" ry="14" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="28" cy="96" rx="26" ry="14" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-50 96h48l8 156h-48zM6 96h48l-8 156H0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-52 252h58v20h-70q-10 0-10-10t22-10z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M52 252H-6v20h70q10 0 10-10t-22-10z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3" transform="translate(0 0)"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M268 150v134"/>
</g>
{point(478, 190, 300, 210)}''', arrow=True, ground=False)

add('rib', 'かご状に胸を囲むあばら骨', f'''
<g transform="translate(300 200)">
  <path d="M0-140v230" stroke="#e8e0cf" stroke-width="20" stroke-linecap="round" fill="none"/>
  <path d="M0-140v230" stroke="{INK}" stroke-width="2.5" fill="none"/>
  <g fill="none" stroke="#e8e0cf" stroke-width="15" stroke-linecap="round">
''' + ''.join(f'<path d="M-4 {-116+i*32}q-{80+i*6} 6-{74+i*8} {46+i*4}"/><path d="M4 {-116+i*32}q{80+i*6} 6 {74+i*8} {46+i*4}"/>' for i in range(6)) + f'''
  </g>
  <g fill="none" stroke="{INK}" stroke-width="2.5">
''' + ''.join(f'<path d="M-4 {-116+i*32}q-{80+i*6} 6-{74+i*8} {46+i*4}"/><path d="M4 {-116+i*32}q{80+i*6} 6 {74+i*8} {46+i*4}"/>' for i in range(6)) + f'''
  </g>
</g>''', ground=False)

add('pelvis', '腰まわりの鉢のような形をした骨盤', f'''
<g transform="translate(300 210)">
  <path d="M-24-100h48v70h-48z" fill="#e8e0cf" class="o"/>
  <path d="M-24-40q-90-30-120 26-30 58 24 86 44 22 66-24 12-24 30-24t30 24q22 46 66 24 54-28 24-86-30-56-120-26z" fill="#e8e0cf" class="o"/>
  <path d="M-96 6q-24 18-8 44 24 24 48-6" fill="none" stroke="#c9bfa8" stroke-width="5"/>
  <path d="M96 6q24 18 8 44-24 24-48-6" fill="none" stroke="#c9bfa8" stroke-width="5"/>
  <path d="M-20 60h40v34h-40z" fill="#d8cfb8" class="o"/>
</g>''', ground=False)

add('artery', '心臓から太い血管が枝分かれして出ている', f'''
<g transform="translate(280 200)">
  <path d="M0 60q-70-50-70-104 0-40 34-40 22 0 36 22 14-22 36-22 34 0 34 40 0 54-70 104z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="17" stroke-linecap="round">
  <path d="M300 120q60-60 130-30M296 236q56 70 140 46M258 250q-50 60-120 44M244 122q-56-54-124-26"/>
</g>
<g fill="none" stroke="#f7c7bd" stroke-width="7" stroke-linecap="round">
  <path d="M300 120q60-60 130-30M296 236q56 70 140 46"/>
</g>
{point(514, 74, 442, 96)}''', arrow=True, ground=False)

add('intestine', '腹の中で長く折り返しながら続く腸', f'''
<g transform="translate(300 210)">
  <ellipse rx="160" ry="130" fill="#fbe3d6" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="#e8a98f" stroke-width="26" stroke-linecap="round" stroke-linejoin="round">
    <path d="M-96-70h180v46h-160v46h160v46h-180"/>
  </g>
  <g fill="none" stroke="#c98a70" stroke-width="4">
    <path d="M-96-70h180v46h-160v46h160v46h-180"/>
  </g>
</g>''', ground=False)

add('thyroid', 'のどの下にある蝶の形をした腺', f'''
<g transform="translate(300 210)">
  <path d="M-80-140h160v90q0 40-80 40t-80-40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-110 10h220v130h-220z" fill="{TONES['teal'][1]}" stroke="{INK}" stroke-width="2.5"/>
  <g class="coral o">
    <path d="M-8-30h16v56h-16z"/>
    <path d="M-8-24q-46-24-58 18-10 40 26 46 34 4 32-38z"/>
    <path d="M8-24q46-24 58 18 10 40-26 46-34 4-32-38z"/>
  </g>
</g>
{point(500, 112, 380, 176)}''', arrow=True, ground=False)

# --- 症状 -------------------------------------------------------------------
add('sneeze', '顔を伏せてくしゃみをし、しぶきが飛んでいる', f'''
{bighead(230, 210)}
<path d="M198 292q32-16 64 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
{hand(160, 300, 1)}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M356 262l50-20M360 288l56 4M350 236l40-44"/>
</g>
<g fill="{TONES['blue'][0]}">
  <circle cx="430" cy="232" r="6"/><circle cx="452" cy="264" r="5"/><circle cx="440" cy="300" r="6"/>
  <circle cx="472" cy="216" r="4"/><circle cx="482" cy="288" r="4"/>
</g>''', ground=False)

add('cough', '口に手を当ててせきをしている', f'''
{bighead(240, 200)}
<ellipse cx="240" cy="272" rx="26" ry="20" fill="{INK}"/>
{hand(330, 274, -1)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M400 250q28-14 56-2M404 282q30-6 56 8M394 218q26-22 54-16"/>
</g>''', ground=False)

add('sniff', '鼻をすすっていて鼻の下に線が上がっている', f'''
{bighead(250, 210)}
<path d="M250 200v44q0 12-14 14" fill="none" stroke="{SKINL}" stroke-width="4" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M232 290v-24M268 290v-24"/>
</g>
{hand(408, 272, -1)}''', arrow=True, ground=False)

add('yawn', '大きく口を開けてあくびをしている', f'''
{bighead(250, 200)}
<ellipse cx="250" cy="286" rx="40" ry="52" fill="#8b3a3a" stroke="{INK}" stroke-width="3"/>
<path d="M216 254q34-12 68 0" fill="none" stroke="#fffefd" stroke-width="8"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M420 156q14-14 28-2M418 200q18-10 30 4M424 244q16-6 26 8"/>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M448 96q22-4 22 16t-22 16 22 16"/>
</g>''', ground=False)

add('hiccup', '体がびくっと跳ねてしゃっくりが出ている', f'''
{person(260, 340, 1.1, 1, 'gold', 'blue', 'stand', 'short', 'neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M180 190l-26-16M180 220l-30 6M340 190l26-16M340 220l30 6"/>
</g>
<g transform="translate(430 160)">
  <ellipse rx="58" ry="42" fill="#fffefd" class="o"/>
  <path d="M-30 34l-16 26 34-14z" fill="#fffefd" class="o"/>
  <path d="M-26-8q26-22 52 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-14 16h28" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round" fill="none"/>
</g>''', ground=True)

add('shiver', '寒さで身を縮めて震えている', f'''
{person(280, 340, 1.1, 1, 'blue', 'blue', 'stand', 'bob', 'sad')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M186 200q-14-12-4-24M182 240q-16-10-6-24M374 200q14-12 4-24M378 240q16-10 6-24"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M470 130v40M450 150h40M456 136l28 28M484 136l-28 28"/>
  <path d="M120 180v34M103 197h34M108 185l24 24M132 185l-24 24"/>
</g>''', ground=True)

add('sweat', '汗が額から流れ落ちている', f'''
{bighead(260, 210)}
{drop(300, 96, 1.4, 'blue')}
{drop(200, 108, 1.2, 'blue')}
{drop(340, 140, 1.1, 'blue')}
{drop(160, 168, 1.0, 'blue')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M420 160q16-12 30 0M424 210q16-12 30 0"/>
</g>''', ground=False)

add('itch', '腕をかいていて、かゆみの印が出ている', f'''
{person(240, 340, 1.1, 1, 'green', 'blue', 'reach', 'short', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M330 208q14-14 28 0t28 0M330 234q14-14 28 0t28 0"/>
</g>
<g fill="{TONES['coral'][0]}">
  <circle cx="404" cy="196" r="5"/><circle cx="418" cy="222" r="5"/><circle cx="400" cy="248" r="5"/>
</g>''', ground=True)

add('ache', '腰を押さえて鈍い痛みに顔をしかめている', f'''
{person(250, 344, 1.1, 1, 'teal', 'blue', 'hold', 'short', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M330 248q22-6 34 8M340 276q24-2 34 14M318 220q24-12 40 0"/>
</g>
<g transform="translate(430 150)">
  <path d="M0-40l14 26 28 4-20 22 6 28-28-14-28 14 6-28-20-22 28-4z" class="coralp o"/>
</g>''', ground=True)

add('sting', 'ハチが腕を刺し、その場所が赤くなっている', f'''
{person(230, 344, 1.05, 1, 'gold', 'blue', 'reach', 'bob', 'sad')}
<circle cx="330" cy="212" r="18" class="coralp o"/>
<circle cx="330" cy="212" r="7" class="coral o"/>
<g transform="translate(404 176)">
  <ellipse rx="30" ry="20" class="gold o"/>
  <g fill="{INK}"><path d="M-14-18q10 36 0 36zM6-20q10 40 0 40z"/></g>
  <ellipse cx="-26" cy="-4" rx="12" ry="10" fill="{INK}"/>
  <g fill="#fffefd" stroke="{INK}" stroke-width="2" opacity="0.8">
    <ellipse cx="4" cy="-24" rx="24" ry="12" transform="rotate(-20 4 -24)"/>
  </g>
  <path d="M30 4l16 8" stroke="{INK}" stroke-width="4" stroke-linecap="round" fill="none"/>
</g>
{point(372, 196, 344, 206)}''', arrow=True, ground=True)

add('swell', '足首が腫れて太くなり、元の細さと比べられている', f'''
<g transform="translate(190 60)">
  <path d="M-26 0h52v150h-52z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-26 150h52v22h-52z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-26 172h74q12 0 12 12t-12 12h-86q-10 0-10-12t22-12z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(400 60)">
  <path d="M-26 0h52v96h-52z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-56 96q0-14 30-14t30 14q22 24 22 50t-52 26-52-26 22-50z" fill="#f7bda0" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-52 172h74q12 0 12 12t-12 12h-86q-10 0-10-12t22-12z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M256 180h74"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M452 130l22-14M456 164l26 2M446 196l20 20"/>
</g>''', arrow=True, ground=False)

add('bruise', '膝に青黒いあざができている', f'''
<g transform="translate(300 70)">
  <path d="M-54 0h108v96h-108z" fill="{TONES['blue'][1]}" stroke="{INK}" stroke-width="2.5"/>
  <ellipse cx="-26" cy="104" rx="28" ry="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="28" cy="104" rx="28" ry="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-52 104h48l8 150h-48zM6 104h48l-8 150H0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(274 174)">
  <ellipse rx="28" ry="22" fill="#6b5a9e" opacity="0.85"/>
  <ellipse rx="18" ry="13" fill="#3f3466" opacity="0.9"/>
</g>
{point(486, 138, 312, 168)}''', arrow=True, ground=False)

add('limp', '片足をかばって引きずるように歩いている', f'''
{person(280, 340, 1.15, 1, 'coral', 'blue', 'walk', 'short', 'sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M338 316q20-8 30 6M344 342q22-4 30 12"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" stroke-linecap="round">
  <path d="M150 372h300"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 300h-60"/></g>''', arrow=True, ground=True)

add('scar', '腕に細長い傷あとが残っている', f'''
<g transform="translate(300 210) rotate(-14)">
  <path d="M-180 30q-16-36 20-48l300-30q40-4 44 26t-36 34l-300 32q-20 2-28-14z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(300 190) rotate(-14)">
  <path d="M-70 0h140" stroke="#d98878" stroke-width="7" stroke-linecap="round" fill="none"/>
  <g stroke="#d98878" stroke-width="4" stroke-linecap="round">
    <path d="M-56-10v20M-28-11v22M0-11v22M28-11v22M56-10v20"/>
  </g>
</g>
{point(470, 100, 372, 156)}''', arrow=True, ground=False)

add('blister', 'かかとに水ぶくれができている', f'''
<g transform="translate(280 200) rotate(-8)">
  <path d="M-90-40h60v130h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-90 90h140q16 0 16 16t-16 16h-160q-14 0-14-16t34-16z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-90 60q-34 4-34 30t34 32z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(166 264)">
  <ellipse rx="30" ry="24" fill="#fce8dc" stroke="{TONES['coral'][2]}" stroke-width="3.5"/>
  <ellipse cx="-8" cy="-8" rx="10" ry="7" fill="#fffefd"/>
</g>
{point(80, 168, 142, 240)}''', arrow=True, ground=False)

# --- 手当ての道具 -----------------------------------------------------------
add('bandage', '腕にぐるぐると包帯が巻かれている', f'''
<g transform="translate(300 200) rotate(-16)">
  <path d="M-190 30q-14-34 20-46l320-32q40-4 44 26t-38 34l-320 34q-18 2-26-16z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(300 188) rotate(-16)">
  <g fill="#fffefd" stroke="{INK}" stroke-width="2.5">
''' + ''.join(f'<path d="M{-90+i*30} -46h30l-6 92h-30z"/>' for i in range(6)) + f'''
  </g>
  <path d="M84-40l40 18-46 12z" fill="#fffefd" class="o"/>
</g>''', ground=False)

add('plaster', '切り傷にばんそうこうが貼られている', f'''
<g transform="translate(280 210) rotate(-10)">
  <path d="M-170 26q-14-30 18-42l280-26q36-4 40 22t-34 30l-280 28q-16 2-24-12z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(290 194) rotate(-10)">
  <path d="M-80-30h160q16 0 16 30t-16 30H-80q-16 0-16-30t16-30z" fill="#e0c48a" class="o"/>
  <rect x="-34" y="-20" width="68" height="40" rx="5" fill="#fdf6ea" class="o"/>
  <g fill="#c9a464">
    <circle cx="-14" cy="-6" r="3"/><circle cx="2" cy="4" r="3"/><circle cx="18" cy="-6" r="3"/>
    <circle cx="-14" cy="10" r="3"/><circle cx="18" cy="10" r="3"/>
  </g>
</g>
{point(470, 108, 372, 158)}''', arrow=True, ground=False)

add('syringe', '目盛りのついた注射器と針', f'''
<g transform="translate(300 200) rotate(-18)">
  <path d="M-150-26h200v52h-200z" fill="#eef4f8" class="o"/>
  <path d="M-150-26h60v52h-60z" fill="#cfe0ec"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5">
''' + ''.join(f'<path d="M{-100+i*24} -26v14"/>' for i in range(9)) + f'''
  </g>
  <path d="M-150-38h14v76h-14z" fill="{MUTED}" class="o"/>
  <path d="M-208-12h58v24h-58z" fill="{MUTED}" class="o"/>
  <path d="M-230-30h22v60h-22z" fill="{MUTED}" class="o"/>
  <path d="M50-14h26v28H50z" fill="#8f9aa6" class="o"/>
  <path d="M76-4h84v8H76z" fill="{MUTED}" stroke="{INK}" stroke-width="2"/>
  <path d="M160-4l22 4-22 4z" fill="{MUTED}" stroke="{INK}" stroke-width="2"/>
</g>
{drop(500, 118, 1.0)}''', ground=False)

add('stretcher', '担架に人が寝かされ、二人が両端を運んでいる', f'''
<g>
  <path d="M110 250h380v20H110z" fill="#8f9aa6" class="o"/>
  <path d="M130 250v40M470 250v40" stroke="{MUTED}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M170 244h260v-24H170z" fill="#e6eef4" class="o"/>
  <ellipse cx="200" cy="216" r="0" />
  <circle cx="204" cy="212" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M226 220h180v24H226z" class="bluep o"/>
</g>
{person(96, 330, 0.66, 1, 'coral', 'blue', 'carry', 'short', 'neutral')}
{person(504, 330, 0.66, -1, 'coral', 'blue', 'carry', 'cap', 'neutral')}''', ground=True)

add('wheelchair', '車輪の大きな車いすに人が座っている', f'''
<g transform="translate(300 220)">
  <circle cx="30" cy="60" r="74" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="30" cy="60" r="58" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <g stroke="{MUTED}" stroke-width="3" fill="none">
''' + ''.join(f'<path d="M30 60l{58*__import__("math").cos(a*3.14159/180):.0f} {58*__import__("math").sin(a*3.14159/180):.0f}" transform="translate(0 0)"/>' for a in range(0,360,30)) + f'''
  </g>
  <circle cx="30" cy="60" r="10" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="-86" cy="96" r="24" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-86 72v-40h96" stroke="{MUTED}" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M-70 20h110v14h-110z" class="teald o"/>
  <path d="M40 20v-96h16v96z" class="teald o"/>
  <path d="M56-76h26v10H56z" fill="{MUTED}" class="o"/>
</g>
<g>
  <circle cx="332" cy="120" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M306 146h52l10 78h-72z" class="coral o"/>
  <path d="M240 226h68v22h-68z" class="blued o"/>
  <path d="M232 226h24v34h-24z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>''', ground=True)

add('crutch', '松葉づえを両脇にはさんで立っている', f'''
{person(300, 344, 1.05, 1, 'green', 'blue', 'stand', 'short', 'neutral')}
<g stroke="{MUTED}" stroke-width="9" stroke-linecap="round" fill="none">
  <path d="M214 200v148M386 200v148"/>
  <path d="M198 200h32M370 200h32"/>
  <path d="M214 200l-10-24M214 200l10-24M386 200l-10-24M386 200l10-24"/>
  <path d="M198 250h32M370 250h32"/>
</g>
<g fill="{TONES['coral'][1]}" stroke="{INK}" stroke-width="2.5">
  <rect x="196" y="170" width="36" height="16" rx="8"/>
  <rect x="368" y="170" width="36" height="16" rx="8"/>
</g>''', ground=True)

add('capsule', '半分ずつ色の違うカプセル薬が数個', f'''
<g transform="translate(240 190) rotate(-24)">
  <path d="M-80-30h80v60h-80q-30 0-30-30t30-30z" class="coral o"/>
  <path d="M0-30h80q30 0 30 30t-30 30H0z" fill="#fdf6ea" class="o"/>
</g>
<g transform="translate(390 268) rotate(14)">
  <path d="M-64-24h64v48h-64q-24 0-24-24t24-24z" class="blue o"/>
  <path d="M0-24h64q24 0 24 24t-24 24H0z" fill="#fdf6ea" class="o"/>
</g>
<g transform="translate(170 300) rotate(6) scale(0.8)">
  <path d="M-64-24h64v48h-64q-24 0-24-24t24-24z" class="green o"/>
  <path d="M0-24h64q24 0 24 24t-24 24H0z" fill="#fdf6ea" class="o"/>
</g>''', ground=False)

add('ointment', '軟膏のチューブから指に薬を出している', f'''
<g transform="translate(240 210) rotate(-18)">
  <path d="M-40-100h80v150q0 26-40 26t-40-26z" fill="#eef4f8" class="o"/>
  <path d="M-40-100h80v-46q0-16-18-16h-44q-18 0-18 16z" fill="#cfe0ec" class="o"/>
  <path d="M-16-162h32v-22h-32z" fill="{MUTED}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-20-184h40v-16h-40z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30 20h60M-30 46h60"/></g>
</g>
{hand(410, 250, -1)}
<path d="M354 202q26-8 40 8" fill="none" stroke="#fdf6ea" stroke-width="12" stroke-linecap="round"/>
<path d="M354 202q26-8 40 8" fill="none" stroke="{MUTED}" stroke-width="3"/>''', ground=False)

add('thermometer', '体温計の目盛りが高いところまで上がっている', f'''
{thermometer(300, 320, 0.86, 1.1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M410 110q18-12 34 0M414 156q20-10 34 4"/>
</g>
{point(470, 190, 396, 178)}''', arrow=True, ground=False)

add('gauze', '折りたたまれた四角いガーゼが袋から出ている', f'''
<g transform="translate(300 220)">
  <path d="M-140-70h180v150h-180z" fill="#e6eef4" class="o"/>
  <path d="M-140-70h180v-16h-180z" fill="#cfe0ec" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="6 6"><path d="M-140-56h180"/></g>
  <g fill="#fffefd" stroke="{INK}" stroke-width="2.5">
    <path d="M-10-40h150v110h-150z"/>
    <path d="M14-24h150v110H14z"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="1.6">
''' + ''.join(f'<path d="M{20+i*16} -24v110"/>' for i in range(10)) + ''.join(f'<path d="M14 {-18+i*16}h150"/>' for i in range(8)) + f'''
  </g>
</g>''', ground=False)

add('sling', '腕を布でつって首から下げている', f'''
{person(280, 350, 1.15, -1, 'blue', 'blue', 'stand', 'short', 'neutral')}
<g>
  <path d="M244 200l84 26 24 84q4 22-30 22h-84q-24 0-20-24z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><path d="M232 268h124"/></g>
  <path d="M252 196q-24-50 30-52" fill="none" stroke="{TONES['gold'][0]}" stroke-width="9" stroke-linecap="round"/>
  <path d="M330 226q26-48-16-78" fill="none" stroke="{TONES['gold'][0]}" stroke-width="9" stroke-linecap="round"/>
</g>
{point(470, 250, 384, 272)}''', arrow=True, ground=True)

add('splint', '折れた指に添え木が当てられ、テープで留められている', f'''
<g transform="translate(300 220) rotate(-14)">
  <path d="M-170 30q-14-32 18-42l260-26q36-4 40 22t-34 30l-260 28q-16 2-24-12z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse cx="120" cy="-14" rx="34" ry="26" fill="#fbe3d6" stroke="{SKINL}" stroke-width="3"/>
</g>
<g transform="translate(320 190) rotate(-14)">
  <path d="M-80-26h180v20h-180z" fill="#cfd6dd" class="o"/>
  <path d="M-80 18h180v20h-180z" fill="#cfd6dd" class="o"/>
  <g fill="#e0c48a" stroke="{INK}" stroke-width="2">
    <rect x="-56" y="-36" width="26" height="82" rx="4"/>
    <rect x="20" y="-36" width="26" height="82" rx="4"/>
  </g>
</g>
{point(470, 96, 380, 152)}''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
