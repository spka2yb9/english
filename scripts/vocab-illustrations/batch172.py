# -*- coding: utf-8 -*-
"""第172回。i-/j-/k-/l-/m- の前半。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def target(x, y, r=90):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="{r-i*r/3:.0f}" class="{c} o"/>'
                   for i, c in enumerate(['coralp', 'coral', 'corald']))

def arrow_obj(x, y, r=0, s=1):
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})">'
            f'<path d="M-150 0h150" stroke="{BRN}" stroke-width="7" fill="none" stroke-linecap="round"/>'
            f'<path d="M0 0l-30-16v32z" class="ink"/>'
            f'<path d="M-150 0l-24-16M-150 0l-24 16" stroke="{CRL}" stroke-width="6" fill="none" stroke-linecap="round"/></g>')

def die(x, y, s=1, pips=3):
    P = {1: [(0, 0)], 3: [(-16, -16), (0, 0), (16, 16)], 5: [(-16, -16), (16, -16), (0, 0), (-16, 16), (16, 16)]}
    d = ''.join(f'<circle cx="{a}" cy="{b}" r="6" class="ink"/>' for a, b in P[pips])
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<rect x="-30" y="-30" width="60" height="60" rx="10" fill="#fffefd" class="o"/>{d}</g>')

# --- しるし・惰性・うつる -----------------------------------------------------

add('indicative', '空をおおう黒い雲が、雨が来ることを示すしるしになる',
    '示している＝indicative。', f'''
{cloud(190, 130, 1.9, 'violet')}
{''.join(drop(130 + i * 34, 230 + (i % 2) * 20, 1.2, 'blue') for i in range(5))}
{arc(330, 180, 430, 180, 50, MUTED, True, 5)}
<g transform="translate(490 200)">
  <path d="M0-80q40 50 40 78a40 40 0 1 1-80 0q0-28 40-78z" class="bluep o"/></g>''', arrow=True)

add('inertia', '重い箱を押しても、その場から少しも動こうとしない',
    '惰性、変わろうとしない性質＝inertia。', f'''
{table(346)}
{box(390, 250, 190, 150, 46, 'gold')}
{person(170, 340, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'sad')}
{''.join(f'<path d="M240 {230+i*36}h40" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"/>' for i in range(2))}
<g opacity="0.3"><path d="M300 300h-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/></g>
{''.join(f'<path d="M{200+i*16} {170-i*12}q12-12 0-24" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{cross(500, 130, 0.6)}''', arrow=True)

add('infectious', '一人のあくびが、次の人、その次の人へと次々にうつっていく',
    '感染性の、(感情が)人にうつる＝infectious。', f'''
{''.join(f'<g transform="translate({100+i*140} 230)"><circle r="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
         f'<path d="{HAIRS["short"]}" transform="translate(0 108) scale(1.9)" fill="{HAIR}"/>'
         f'<circle cx="-16" cy="-8" r="4" class="ink"/><circle cx="16" cy="-8" r="4" class="ink"/>'
         f'<ellipse cy="22" rx="14" ry="18" class="ink"/></g>' for i in range(4))}
{''.join(f'<path d="M{156+i*140} 190q34-40 74 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>' for i in range(3))}''', arrow=True)

add('influencer', '一人の発信が画面を通じて、たくさんの人へ一度に広がる',
    'インフルエンサー、影響力のある発信者＝influencer。', f'''
<g transform="translate(160 190)">
  <path d="M-100-90h200v180h-200z" fill="#fffefd" class="o"/>
  <path d="M-100-90h200v34h-200z" class="teal o"/>
  {head(0, 20, 34, 'coral', 'bob')}</g>
{''.join(f'<path d="M270 190L{430} {{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(80 + i * 62) for i in range(5))}
{''.join(head(470, 80 + i * 62, 24, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('blue', 'bun'), ('gold', 'cap'), ('violet', 'short')]))}''')

add('informally', 'かしこまったネクタイ姿ではなく、くだけた普段着で気楽に話す',
    '非公式に、くだけた形で＝informally。', f'''
{split()}
<g opacity="0.34">{person(150, 340, 1.25, 1, 'blue', 'blue', 'stand', 'short', 'flat')}
<path d="M143 258l-8 46 14 20 14-22-8-44z" class="coral o"/></g>
{cross(150, 110, 0.6)}
{person(440, 340, 1.25, 1, 'coral', 'gold', 'point', 'cap', 'smile')}
{tick(440, 110, 0.7)}''')

# --- 言い張る・強まる・わざと ---------------------------------------------------

add('insist on', '断られても、同じ紙を何度でも相手の前に差し出し続ける',
    '強く求める、言い張る＝insist on。', f'''
{person(150, 340, 1.2, 1, 'teal', 'blue', 'give', 'short', 'flat')}
{person(470, 340, 1.2, -1, 'coral', 'green', 'give', 'bob', 'sad')}
<g opacity="0.28">{doc(260, 220, 80, 100, 3)}</g>
<g opacity="0.55">{doc(290, 205, 80, 100, 3)}</g>
{doc(325, 190, 84, 106, 3)}
{''.join(f'<path d="M{{}} {{}}h40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(230 + i * 20, 280 - i * 20) for i in range(3))}''', arrow=True)

add('intensification', '同じ色の面が、右へ行くほど濃く強くなっていく',
    '激化、強化＝intensification。', f'''
{''.join(f'<rect x="{{}}" y="120" width="90" height="160" rx="8" fill="{{}}" stroke="{INK}" stroke-width="2.5"/>'.format(60 + i * 100, c) for i, c in enumerate(['#fde9e3', '#f6b3a6', '#ef8a76', '#e86452', '#b74338']))}
{arc(100, 100, 500, 100, 40, MUTED, True, 5)}
{''.join(f'<path d="M{{}} 320q{{}} 20 {{}} 0" fill="none" stroke="{CRL}" stroke-width="{{}}"/>'.format(70 + i * 100, 40, 80, 3 + i * 2) for i in range(5))}''', arrow=True)

add('intentionally', '狙いを定めて放った矢が、的の中心にぴたりと当たる',
    'わざと、意図的に＝intentionally。', f'''
{target(420, 200, 110)}
{arrow_obj(420, 200, 0, 1.0)}
{person(110, 340, 1.15, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<path d="M150 200h100" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"/>
{ring(420, 200, 132, True)}''')

# --- 入れ替え・妨げ・いつも ---------------------------------------------------

add('interchangeable', '二つの部品はどちらを差しても同じように機械が動く',
    '取り替えのきく、互換性のある＝interchangeable。', f'''
{split()}
{''.join(f'<g transform="translate({{}} 230)"><path d="M-80-70h160v140h-160z" class="teal o"/><path d="M-40-40h80v80h-80z" fill="#fffaf1" class="o"/></g>'.format(x) for x in (150, 450))}
<g transform="translate(150 230)"><path d="M-34-34h68v68h-68z" class="coral o"/></g>
<g transform="translate(450 230)"><path d="M-34-34h68v68h-68z" class="gold o"/></g>
{tick(150, 360, 0.6)}{tick(450, 360, 0.6)}
<g transform="translate(300 90)">
  <path d="M-70-20h140" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>
  <path d="M70 20h-140" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/></g>''', arrow=True)

add('interfere with', '流れていた水路に石が投げ込まれ、その先の流れが乱れる',
    '妨げる、じゃまをする＝interfere with。', f'''
<g transform="translate(300 220)">
  <path d="M-250-50h500v100h-250z" fill="none"/>
  <path d="M-250-50h500v100h-500z" class="bluep o"/></g>
{''.join(f'<path d="M{{}} 200q22-14 44 0" fill="none" stroke="{BLU}" stroke-width="5"/>'.format(-230 + 300 + i * 50) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}q22-16 44 0t44 4" fill="none" stroke="{BLU}" stroke-width="5"/>'.format(370 + i * 20, 200 + (i % 2) * 26 - 10) for i in range(3))}
<g transform="translate(330 220) rotate(14)"><path d="M-40-36h80v72h-80z" fill="{STONE}" class="o"/></g>
{line(330, 70, 330, 150, MUTED, True, 5)}
{''.join(f'<path d="M{{}} {{}}l14-16" fill="none" stroke="{CRL}" stroke-width="4"/>'.format(400 + i * 22, 160 - i * 10) for i in range(2))}''', arrow=True)

add('invariably', '何度さいころを振っても、出る目は決まって同じになる',
    '決まって、いつも＝invariably。', f'''
{table(340)}
{''.join(die(120 + i * 120, 250, 1.2, 3) for i in range(4))}
{''.join(f'<path d="M{{}} 150q30-40 60 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(150 + i * 120) for i in range(3))}
{tick(300, 360, 0.6)}''', arrow=True)

# --- 調整・専門語・共同 -------------------------------------------------------

add('iron out', 'しわの寄った布にアイロンをかけ、引っかかりのない平らな面にする',
    '(問題を)片づける、調整する＝iron out。', f'''
{table(340)}
<g transform="translate(300 300)">
  <path d="M-250 0h500v-30h-500z" fill="#fffefd" class="o"/>
  <path d="M-250-30h180v-14h-180z" fill="#fffefd" class="o"/></g>
<path d="M330 268q30-26 58 0t58 0 58 0" fill="none" stroke="{MUTED}" stroke-width="5"/>
<path d="M60 270h180" fill="none" stroke="{MUTED}" stroke-width="5"/>
<g transform="translate(290 230)">
  <path d="M-70 40h140l-24-70h-92z" class="teal o"/>
  <path d="M-56-30h112v-24h-112z" class="teald o"/>
  <path d="M-30-54q30-40 60 0" fill="none" stroke="{INK}" stroke-width="8"/></g>
{''.join(f'<path d="M{{}} 190q14-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(180 + i * 24) for i in range(2))}''')

add('jargon', '同じ仕事の二人には通じる記号が、外の人にはまったく読めない',
    '専門用語、業界用語＝jargon。', f'''
{head(120, 200, 34, 'teal', 'short')}
{head(280, 200, 34, 'teal', 'bob')}
<g transform="translate(200 100)">
  <path d="M-70-40h140v72h-24l-14 22-10-22h-92z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="{{}}" y="{{}}" width="14" height="14" rx="3" fill="{VIO}" transform="rotate({{}} {{}} {{}})"/>'.format(-50 + (i % 4) * 26, -22 + (i // 4) * 24, 18 * (i % 3), -43 + (i % 4) * 26, -15 + (i // 4) * 24) for i in range(8))}</g>
{tick(200, 280, 0.6)}
{head(480, 220, 40, 'coral', 'bun')}
<g transform="translate(480 100)">
  <path d="M-24-40q0-30 26-30t26 30q0 20-26 30v16" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="2" cy="34" r="7" fill="{MUTED}"/></g>
<path d="M340 200h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('jointly', '二人が両側から同じ一つの荷を持ち、力を合わせて運ぶ',
    '共同で＝jointly。', f'''
{person(160, 340, 1.2, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{person(440, 340, 1.2, -1, 'coral', 'green', 'up', 'bob', 'smile')}
{box(300, 160, 200, 110, 40, 'gold')}
{''.join(f'<path d="M{{}} 200l{{}} -28" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>'.format(x, d) for x, d in [(210, 24), (390, -24)])}
{''.join(spark(300 + (i * 2 - 1) * 130, 70, 0.7, 'gold') for i in range(2))}''')

add('jot down', '思いついたことを、小さなメモ帳にさっと走り書きする',
    'さっと書き留める＝jot down。', f'''
{table(340)}
<g transform="translate(290 260)">
  <path d="M-110-80h220v160h-220z" class="paper" transform="rotate(-6)"/>
  {''.join(f'<path d="M{{}} {{}}q20-14 40 0t40 0" fill="none" stroke="{MUTED}" stroke-width="5" transform="rotate(-6)"/>'.format(-84, -40 + i * 34) for i in range(3))}
  <path d="M-110-80h220" fill="none" stroke="{MUTED}" stroke-width="0"/></g>
<g transform="translate(400 150) rotate(34)">
  <path d="M-9-90h18v130l-9 26-9-26z" class="teal o"/></g>
{''.join(spark(130 + i * 30, 110 + (i % 2) * 26, 0.7, 'gold') for i in range(2))}''')

# --- 伏せる・開始・血縁 -------------------------------------------------------

add('keep back', '書類の一枚だけを後ろ手に隠したまま、残りを相手に渡す',
    '(情報を)伏せる＝keep back。', f'''
{person(200, 340, 1.3, 1, 'teal', 'blue', 'give', 'short', 'flat')}
<g transform="translate(120 250) rotate(16)">{doc(0, 0, 84, 108, 3)}</g>
{ring(120, 250, 72, True)}
{doc(340, 200, 90, 116, 3)}
{person(490, 340, 1.15, -1, 'coral', 'green', 'reach', 'bob', 'smile')}
{arc(300, 180, 400, 190, 50, MUTED, True, 4)}''', arrow=True)

add('kick off', 'ボールを蹴り出したその瞬間から、試合が動き始める',
    '始まる、始める＝kick off。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<path d="M300 300v100M240 300a60 40 0 0 0 120 0" fill="none" stroke="#ffffff" stroke-width="5"/>
{person(220, 350, 1.3, 1, 'teal', 'blue', 'walk', 'cap', 'smile')}
<g transform="translate(350 320)">
  <circle r="34" fill="#fffefd" class="o"/>
  <path d="M0-20l18 14-7 22h-22l-7-22z" class="ink"/></g>
{arc(390, 290, 520, 190, 70, MUTED, True, 5)}
{''.join(spark(140 + i * 30, 110 + (i % 2) * 24, 0.7, 'gold') for i in range(2))}''', arrow=True)

add('kinship', '家系図の線をたどると、二人が同じ祖先につながっている',
    '血縁関係、親近感＝kinship。', f'''
{head(300, 90, 30, 'gold', 'bun')}
<path d="M300 130v40M170 170h260M170 170v40M430 170v40" fill="none" stroke="{MUTED}" stroke-width="5"/>
{head(170, 240, 28, 'teal', 'short')}
{head(430, 240, 28, 'teal', 'bob')}
<path d="M170 280v40M430 280v40" fill="none" stroke="{MUTED}" stroke-width="5"/>
{head(170, 350, 26, 'coral', 'cap')}
{head(430, 350, 26, 'coral', 'bun')}
<path d="M200 350h200" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="12 10"/>''')

add('knock out', '勝ち上がり表で、一方の名がその場で消されて先へ進めなくなる',
    'ノックアウトする、敗退させる＝knock out。', f'''
<g transform="translate(300 200)">
  {''.join(f'<rect x="-250" y="{{}}" width="120" height="46" rx="8" class="{{}} o"/>'.format(-140 + i * 100, c) for i, c in enumerate(['teal', 'coral', 'green', 'violet']))}
  <path d="M-130-118h40v100h-40M-130 82h40V-18" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <path d="M-130 82h40v-100h-40" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <rect x="-70" y="-52" width="120" height="46" rx="8" class="teal o"/>
  <rect x="-70" y="48" width="120" height="46" rx="8" class="green o"/></g>
{cross(360, 246, 0.8)}
{cross(110, 260, 0.7)}''')

# --- 暴言・定める・至る -------------------------------------------------------

add('lash out', '突然、とげのついた言葉のかたまりを周囲へ放つ',
    '激しく非難する、突然殴りかかる＝lash out。', f'''
{person(160, 340, 1.3, 1, 'coral', 'blue', 'point', 'short', 'sad')}
<g transform="translate(380 190)">
  <path d="M0-110l24 40 44-24-16 46 48 12-40 30 34 36-48 2 6 48-38-28-30 34-16-46-46 14 18-44-46-18 42-26-28-40 48-6z" class="coral o"/></g>
{''.join(head(520, 130 + i * 90, 24, 'teal', 'short', 'sad') for i in range(1))}
{head(520, 320, 24, 'green', 'bob', 'sad')}
{arc(220, 200, 300, 190, 46, CRL, True, 5)}''', arrow=True)

add('lay down', '石の板に刻んだ規則を、みなの前の地面にきちんと据える',
    '(規則を)定める、置く＝lay down。', f'''
{''.join(head(80 + i * 80, 120, 24, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('blue', 'bun')]))}
<g transform="translate(360 280)">
  <path d="M-130-90h260v130h-260z" fill="{STONE}" class="o"/>
  {''.join(f'<rect x="-104" y="{{}}" width="{{}}" height="12" rx="6" fill="{MUTED}"/>'.format(-64 + i * 36, 208 - (i % 3) * 44) for i in range(3))}</g>
{hand(360, 120, 1)}
{line(360, 170, 360, 208, MUTED, True, 5)}
<path d="M180 330h400" fill="none" stroke="{BRN}" stroke-width="8"/>''', arrow=True)

add('lead up to', '小さな段が積み重なって、最後の大きな出来事へとつながる',
    '〜に至る、〜の前段階となる＝lead up to。', f'''
{''.join(f'<rect x="{{}}" y="{{}}" width="80" height="{{}}" rx="6" class="tealp o"/>'.format(50 + i * 90, 320 - 34 - i * 34, 34 + i * 34) for i in range(4))}
<g transform="translate(500 220)">
  <path d="M-70 100v-160h140v160z" class="coral o"/>
  {spark(0, -86, 1.1, 'gold')}</g>
{arc(90, 260, 450, 130, 90, MUTED, True, 5)}''', arrow=True)

# --- 賃貸・合法 --------------------------------------------------------------

add('lease', '決まった期間だけという帯つきの契約書と、その部屋の鍵を受け取る',
    '賃貸契約、賃貸する＝lease。', f'''
{table(340)}
{doc(220, 230, 190, 230, 3)}
<g transform="translate(220 300)">
  <path d="M-80-16h160v32h-160z" class="tealp o"/>
  <path d="M-80 0h160" fill="none" stroke="{TEA}" stroke-width="4" stroke-dasharray="10 9"/></g>
<g transform="translate(440 220)">
  <circle r="26" fill="none" stroke="{GLD}" stroke-width="9"/>
  <path d="M26 0h74" stroke="{GLD}" stroke-width="11" fill="none"/>
  <path d="M78 0v22h14V0zM56 0v18h12V0z" fill="{GLD}"/></g>
{house(470, 130, 0.42, 'coral')}''')

add('legalisation', '×の札が外され、同じ行いが法の枠の内側に入って✓になる',
    '合法化＝legalisation。', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-100-90h200v180h-200z" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 11"/>
  <circle cx="0" cy="130" r="30" class="coral o"/></g>
{cross(150, 200, 0.8)}
<g transform="translate(450 200)">
  <path d="M-100-90h200v180h-200z" fill="none" stroke="{TEA}" stroke-width="6"/>
  <circle r="30" class="coral o"/></g>
{tick(450, 340, 0.7)}
{arc(260, 160, 330, 160, 44, MUTED, True, 4)}''', arrow=True)

add('legislate', '議場で条文を一行ずつ書き足し、法の本を作り上げる',
    '法律を制定する＝legislate。', f'''
{table(320)}
{''.join(sit(120 + i * 100, 320, 0.86, 1, c, 'blue', h, 'flat') for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('violet', 'bun')]))}
{''.join(chair(114 + i * 100, 320, 0.8, 'gold', 1) for i in range(3))}
<g transform="translate(450 230)">
  <path d="M-90-100h180v200h-180z" fill="#fffefd" class="o"/>
  <path d="M-96-100h14v200h-14z" class="teald o"/>
  {''.join(f'<rect x="-62" y="{{}}" width="{{}}" height="10" rx="5" fill="{MUTED}"/>'.format(-70 + i * 34, 130 - (i % 3) * 34) for i in range(5))}</g>
<g transform="translate(530 120) rotate(34)">
  <path d="M-8-70h16v104l-8 20-8-20z" class="teal o"/></g>''')

add('legitimacy', '公の印が押された証書が、しっかりした土台の上に立つ',
    '正当性、合法性＝legitimacy。', f'''
<g transform="translate(300 340)"><path d="M-180-40h360v40h-360z" fill="{STONE}" class="o"/>
  <path d="M-150-70h300v30h-300z" fill="{STONE}" class="o"/></g>
{doc(300, 190, 220, 250, 4)}
<g transform="translate(300 250)">
  <circle r="52" class="coralp o"/><circle r="34" fill="none" stroke="{CRL}" stroke-width="5"/>
  <path d="M-18 0l12 16 26-32" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>
{''.join(spark(140 + i * 320, 110, 0.8, 'gold') for i in range(2))}''')

# --- 漏らす・てこ・責任 -------------------------------------------------------

add('let on', '封をしたはずの手紙の口から、中身が少しだけのぞいてしまう',
    '(秘密を)漏らす、そぶりを見せる＝let on。', f'''
{table(340)}
<g transform="translate(280 250)">
  <path d="M-140-90h280v180h-280z" fill="#fffefd" class="o"/>
  <path d="M-140-90l140 100 140-100" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-140-90h280l-70 50h-140z" class="goldp o"/></g>
<g transform="translate(340 210) rotate(-14)">
  <path d="M-50-56h100v112h-100z" class="paper"/>
  {''.join(f'<rect x="-34" y="{{}}" width="{{}}" height="8" rx="4" fill="{MUTED}"/>'.format(-34 + i * 24, 68 - (i % 2) * 22) for i in range(3))}</g>
{''.join(f'<path d="M{{}} {{}}q12-14 0-26" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(440 + i * 20, 150 - i * 12) for i in range(2))}
{person(120, 340, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'sad')}''')

add('leverage', '長い棒をてこにして、手では動かない大きな石を持ち上げる',
    '交渉での強み、てこの力／活用する＝leverage。', f'''
{table(360)}
<g transform="translate(300 300)"><path d="M-30 40l30-60 30 60z" fill="{BRN}" class="o"/></g>
<g transform="translate(300 240) rotate(-16)">
  <path d="M-240-10h480v20h-480z" fill="{BRN}" class="o"/></g>
<g transform="translate(112 290)"><path d="M-56-50h112v100h-112z" fill="{STONE}" class="o"/></g>
{hand(490, 300, -1)}
{arc(500, 250, 500, 320, -40, MUTED, True, 4)}
{arc(120, 220, 120, 160, 30, GRN, True, 4)}''', arrow=True)

add('liability', '自分の名の札がついた重りが足に結ばれ、身動きが取りにくい',
    '法的責任、不利になるもの＝liability。', f'''
{person(300, 300, 1.3, 1, 'teal', 'blue', 'walk', 'short', 'sad')}
<g transform="translate(320 340)">
  <path d="M-20 0v24" stroke="{MUTED}" stroke-width="6" fill="none"/>
  <path d="M-80 24h120v50h-120z" fill="{STONE}" class="o"/>
  <path d="M-60 34h50v10h-50z" fill="{MUTED}"/></g>
{''.join(f'<path d="M{{}} {{}}q12-12 0-24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(210 + i * 16, 190 - i * 12) for i in range(2))}
{doc(470, 180, 120, 150, 3)}
{arc(430, 200, 360, 300, 60, CRL, True, 4)}''', arrow=True)

add('liable for', '割れた品の請求書が、まっすぐその人あてに届く',
    '〜に法的責任がある＝liable for。', f'''
<g transform="translate(140 250)">
  <path d="M-46 0q6 46 46 46t46-46z" class="corald o"/>
  <path d="M-18 0l10 40M14 0l-8 42" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M50 4l30-16M-50 4l-30-16" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{doc(310, 200, 120, 150, 3)}
<g transform="translate(310 250)"><circle r="26" class="coralp o"/>
  <path d="M-8-12h16v18h-16z" class="coral"/></g>
{person(490, 340, 1.2, -1, 'teal', 'blue', 'reach', 'short', 'sad')}
{arc(200, 200, 250, 190, 40, MUTED, True, 4)}
{arc(370, 190, 440, 200, 40, CRL, True, 5)}''', arrow=True)

# --- 自由・血統・流動性 -------------------------------------------------------

add('liberalism', '囲いの柵が開かれ、中にいた人がそれぞれ好きな方向へ進んでいく',
    '自由主義＝liberalism。', f'''
<g transform="translate(300 250)">
  <path d="M-200 80v-140M-140 80v-140M140 80v-140M200 80v-140" fill="none" stroke="{MUTED}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-200-40h60M140-40h60M-200 10h60M140 10h60" fill="none" stroke="{MUTED}" stroke-width="9" stroke-linecap="round"/></g>
{person(300, 340, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{''.join(f'<path d="M300 200L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(x, y) for x, y in [(90, 90), (300, 50), (510, 90)])}''', arrow=True)

add('lineage', '同じ家の顔が、世代をまたいで一本の線でつながっていく',
    '血統、系譜＝lineage。', f'''
{''.join(f'<g>{{}}</g>'.format(head(300, 70 + i * 90, 30, c, h)) for i, (c, h) in enumerate([('gold', 'bun'), ('teal', 'short'), ('coral', 'bob'), ('violet', 'cap')]))}
{''.join(f'<path d="M300 {{}}v30" fill="none" stroke="{MUTED}" stroke-width="6"/>'.format(112 + i * 90) for i in range(3))}
{''.join(f'<path d="M240 {{}}h120" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(70 + i * 90) for i in range(4))}
<path d="M140 60v300" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-end="url(#ar)"/>''', arrow=True)

add('liquidity', '固まった氷はすぐ使えないが、水ならその場で注いで使える',
    '流動性、すぐ現金にできること＝liquidity。', f'''
{split()}
{table(346)}
<g transform="translate(150 280)">
  <path d="M-60-60h120v120h-120z" fill="#dff1f8" class="o"/>
  <path d="M-40-40h44v44h-44zM10 6h44v44H10z" fill="#ffffff" opacity="0.7"/></g>
{cross(150, 130, 0.6)}
<g transform="translate(430 250)">
  <path d="M-70-60h30v70a40 40 0 0 0 80 0v-70h30v70a70 70 0 0 1-140 0z" fill="#fffefd" class="o"/>
  <path d="M-40 30a40 40 0 0 0 80 0v-24h-80z" class="bluep"/></g>
{''.join(drop(470 + i * 14, 310 + i * 20, 1.0, 'blue') for i in range(2))}
{tick(510, 130, 0.6)}''')

# --- 暮らす・切望・抜け穴 -----------------------------------------------------

add('live off', '一本の木になる実だけを取って、その人の暮らしがまかなわれる',
    '〜で生活する、〜に寄生する＝live off。', f'''
{tree(180, 330, 1.7)}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="14" class="coral o"/>'.format(x, y) for x, y in [(140, 190), (200, 160), (230, 220), (160, 240)])}
{person(430, 340, 1.2, -1, 'teal', 'blue', 'carry', 'short', 'smile')}
<g transform="translate(400 250)">
  <path d="M-40-24h80l-10 60h-60z" class="goldp o"/>
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="11" class="coral o"/>'.format(-18 + i * 18, -4) for i in range(3))}</g>
{arc(250, 200, 350, 220, 60, MUTED, True, 4)}''', arrow=True)

add('long for', '遠い水平線の向こうにある故郷の家を思い、そちらへ手を伸ばす',
    '切望する＝long for。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h600" fill="none" stroke="{BLU}" stroke-width="5"/>
{house(470, 244, 0.42, 'coral')}
{person(150, 350, 1.3, 1, 'teal', 'blue', 'reach', 'bob', 'sad')}
{''.join(f'<path d="M{{}} {{}}q16-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(240 + i * 20, 190 - i * 14) for i in range(3))}
<g transform="translate(150 120)">
  <path d="M0 26q-34-26-34-48 0-18 18-18 10 0 16 12 6-12 16-12 18 0 18 18 0 22-34 48z" class="coralp o"/></g>''')

add('loophole', '高い塀の下にひとつだけ小さな穴があり、そこをすり抜けていく',
    '(法律などの)抜け穴＝loophole。', f'''
<g transform="translate(300 200)">
  <path d="M-240-150h480v300h-480z" fill="{STONE}" class="o"/>
  {''.join(f'<path d="M-240 {{}}h480" fill="none" stroke="#a9b3ba" stroke-width="4"/>'.format(-100 + i * 50) for i in range(5))}
  <path d="M-30 150q0-70 30-70t30 70z" fill="#fffaf1" class="o"/></g>
{person(130, 340, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'flat')}
{arc(180, 300, 420, 300, 40, MUTED, True, 5)}
{ring(300, 320, 66, True)}''', arrow=True)

# --- 拡大・間に合わせ・巧みな動き -----------------------------------------------

add('magnification', '虫めがねを通すと、小さな印がはるかに大きく見える',
    '拡大、倍率＝magnification。', f'''
{table(346)}
<g transform="translate(150 290)">
  <path d="M-90-40h180v60h-180z" class="paper"/>
  {''.join(f'<rect x="{{}}" y="-24" width="12" height="12" rx="2" fill="{INK}"/>'.format(-70 + i * 22) for i in range(6))}</g>
<g transform="translate(420 190)">
  <circle r="130" fill="#ffffff" fill-opacity="0.4" stroke="{INK}" stroke-width="9"/>
  {''.join(f'<rect x="{{}}" y="-26" width="40" height="40" rx="5" fill="{INK}"/>'.format(-88 + i * 60) for i in range(3))}
  <path d="M-92 92l-70 70" stroke="{BRN}" stroke-width="24" stroke-linecap="round" fill="none"/></g>''')

add('make do with', '傘がないので、代わりに新聞紙を頭にかざして雨をしのぐ',
    '(不十分なもので)間に合わせる＝make do with。', f'''
{''.join(f'<path d="M{{}} {{}}l-12 26" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>'.format(70 + i * 50, 60 + (i % 3) * 34) for i in range(10))}
{person(300, 350, 1.3, 1, 'teal', 'blue', 'up', 'short', 'flat')}
<g transform="translate(300 160) rotate(-8)">
  <path d="M-90-36h180v60h-180z" class="paper"/>
  {''.join(f'<rect x="-70" y="{{}}" width="{{}}" height="8" rx="4" fill="{MUTED}"/>'.format(-20 + i * 20, 140 - i * 40) for i in range(2))}</g>
<g opacity="0.28" transform="translate(500 180)">
  <path d="M-70 0a70 70 0 0 1 140 0z" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/>
  <path d="M0 0v90q0 20 20 20" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/></g>
{cross(500, 90, 0.5)}''')

add('manoeuvre', '狭い二台の間へ、車体をうまく回しながら入れていく',
    '巧みな動き、策略／巧みに動かす＝manoeuvre。', f'''
{''.join(f'<g transform="translate({{}} 300)"><path d="M-80 0v-56h160V0z" class="tealp o"/><circle cx="-46" cy="6" r="16" class="ink"/><circle cx="46" cy="6" r="16" class="ink"/></g>'.format(x) for x in (110, 490))}
<g transform="translate(300 290) rotate(-22)">
  <path d="M-80 0v-40l30-26h100l30 26V0z" class="coral o"/>
  <circle cx="-46" cy="6" r="16" class="ink"/><circle cx="46" cy="6" r="16" class="ink"/></g>
<path d="M300 120q-90 30-60 90t60 50" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="11 10" marker-end="url(#ar)"/>
{''.join(f'<path d="M{{}} 348v-8" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(190 + i * 220) for i in range(2))}''', arrow=True)

# --- 計画・値下げ・物質主義 ---------------------------------------------------

add('map out', '地図の上に、通る道を一本ずつ細かく線で引いていく',
    '綿密に計画する＝map out。', f'''
{table(346)}
<g transform="translate(290 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-160 120L-60 40 20 80 100-40 170-10" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="10" class="coral o"/>'.format(x, y) for x, y in [(-160, 120), (-60, 40), (20, 80), (100, -40), (170, -10)])}
  <path d="M-190-110q40 30 80 0t80 10" fill="none" stroke="{GRN}" stroke-width="4"/></g>
<g transform="translate(430 130) rotate(34)">
  <path d="M-8-80h16v120l-8 22-8-22z" class="teal o"/></g>''')

add('mark down', '値札の元の数字に線を引いて消し、それより安い値をつけ直す',
    '値下げする、評価を下げる＝mark down。', f'''
{table(346)}
<g transform="translate(280 220)">
  <path d="M-120-90h240v180h-240z" class="paper"/>
  {''.join(f'<rect x="-80" y="{{}}" width="{{}}" height="18" rx="9" fill="{MUTED}"/>'.format(-60, 0) for _ in range(0))}
  <rect x="-80" y="-64" width="160" height="24" rx="12" fill="{MUTED}"/>
  <path d="M-96-52h192" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round"/>
  <rect x="-60" y="14" width="120" height="30" rx="15" class="coral"/></g>
{arc(300, 120, 300, 200, -60, CRL, True, 5)}
<g transform="translate(460 150) rotate(32)">
  <path d="M-8-70h16v110l-8 20-8-20z" class="coral o"/></g>''', arrow=True)

add('materialism', '買い集めた品の山の上に登り、まだ上へ積み重ねようとする',
    '物質主義＝materialism。', f'''
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-44" y="-34" width="88" height="68" rx="8" class="{{}} o"/></g>'.format(x, y, r, c)
         for x, y, r, c in [(180, 340, 0, 'teal'), (270, 344, -6, 'coral'), (360, 340, 4, 'gold'),
                            (222, 276, 5, 'violet'), (312, 272, -4, 'green'), (266, 208, 2, 'blue')])}
{person(266, 176, 1.0, 1, 'coral', 'violet', 'up', 'short', 'smile')}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-30" y="-24" width="60" height="48" rx="6" class="gold o"/></g>'.format(x, y, r) for x, y, r in [(450, 110, 14), (500, 180, -10)])}
{arc(450, 140, 320, 130, 50, MUTED, True, 4)}''', arrow=True)

# --- 意味・議事録・的外れ -----------------------------------------------------

add('mean', '辞書で語を引くと、その語が指す中身が絵になって現れる',
    '意味する／意地悪な／平均＝mean。', f'''
{table(346)}
{book(190, 250, 1.15, 'teal')}
{arc(310, 190, 380, 190, 46, MUTED, True, 5)}
<g transform="translate(470 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffefd" class="o"/>
  {house(0, 50, 0.52, 'coral')}</g>
{ring(470, 240, 112, True)}''', arrow=True)

add('minutes', '会議で出た発言が、その場でノートに一行ずつ書き留められる',
    '議事録＝minutes。', f'''
{table(300)}
{''.join(sit(130 + i * 96, 300, 0.84, 1, c, 'blue', h, 'flat') for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('violet', 'bun')]))}
{''.join(chair(124 + i * 96, 300, 0.78, 'gold', 1) for i in range(3))}
{''.join(f'<g transform="translate({{}} 140)"><path d="M-34-20h68v34h-14l-8 14-6-14h-40z" fill="#fffefd" class="o"/><path d="M-20-4h40" stroke="{MUTED}" stroke-width="5" fill="none"/></g>'.format(130 + i * 96) for i in range(3))}
<g transform="translate(470 250)">
  <path d="M-80-90h160v180h-160z" class="paper"/>
  {''.join(f'<rect x="-58" y="{{}}" width="{{}}" height="9" rx="4.5" fill="{MUTED}"/>'.format(-62 + i * 30, 116 - (i % 3) * 30) for i in range(5))}</g>
{''.join(f'<path d="M{{}} 160h{{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(170 + i * 96, 60) for i in range(1))}''', arrow=True)

add('miss the point', '的の中心ではなく、ふちの外の何もない所を熱心に指している',
    '論点を取り違える＝miss the point。', f'''
{target(400, 200, 100)}
{person(130, 340, 1.2, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<path d="M180 200h250" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<path d="M180 200q120-110 300-60" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>
{cross(520, 110, 0.6)}
{ring(400, 200, 18, True)}''', arrow=True)

add('mistakenly', '手に取った鍵が合わず、思い違いのまま別の鍵を差し込もうとする',
    '誤って、思い違いで＝mistakenly。', f'''
<g transform="translate(400 220)">
  <path d="M-90-140h180v280h-180z" class="teal o"/>
  <circle cx="52" cy="0" r="10" class="goldp o"/>
  <path d="M40-40h24v24h-24z" fill="#fffaf1" class="o"/></g>
<g transform="translate(230 200) rotate(20)">
  <circle r="26" fill="none" stroke="{CRL}" stroke-width="9"/>
  <path d="M26 0h80" stroke="{CRL}" stroke-width="11" fill="none"/>
  <path d="M84 0v22h14V0z" fill="{CRL}"/></g>
{person(110, 340, 1.05, 1, 'teal', 'blue', 'reach', 'short', 'flat')}
{cross(330, 110, 0.7)}''')

finish(__file__)
