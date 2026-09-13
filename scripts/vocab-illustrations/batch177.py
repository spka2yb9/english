# -*- coding: utf-8 -*-
"""第177回。sub-/su-/sw-/sy-/ta- の語。so long as / stamp out の描き直しも含む。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def flag(x, y, s=1, cls='violet', pole=110):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-{pole}" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>'
            f'<path d="M5-{pole}h100l-24 30 24 30H5z" class="{cls} o"/></g>')

def dove(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse rx="52" ry="34" fill="#fffefd" class="o"/>'
            f'<circle cx="44" cy="-26" r="22" fill="#fffefd" class="o"/>'
            f'<path d="M62-32l26 8-26 10z" class="gold o"/>'
            f'<circle cx="48" cy="-32" r="3.4" class="ink"/>'
            f'<path d="M-10-24q40-56 76-30-30 14-40 46z" fill="#f2f6f8" class="o"/>'
            f'<path d="M-52 4l-46-16 44 34z" fill="#f2f6f8" class="o"/></g>')

def domino(x, y, r=0, s=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})">'
            f'<rect x="-18" y="-60" width="36" height="120" rx="5" class="{cls} o"/>'
            f'<path d="M-18 0h36" stroke="{TONES[cls][2]}" stroke-width="3" fill="none"/></g>')

# --- 第175/176回の描き直し ---------------------------------------------------

add('so long as', '条件の緑の板が続くあいだだけ橋がつながり、切れた先へは行けない',
    '〜する限りは＝so long as。', f'''
<path d="M0 300h600v100H0z" class="bluep"/>
{''.join(f'<rect x="{40+i*86}" y="250" width="70" height="26" rx="6" class="green o"/>' for i in range(4))}
{''.join(f'<g opacity="0.3"><rect x="{386+i*86}" y="250" width="70" height="26" rx="6" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g>' for i in range(2))}
{''.join(f'<path d="M{75+i*86} 276v24" stroke="{BRN}" stroke-width="8" fill="none"/>' for i in range(4))}
{person(160, 250, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{tick(160, 110, 0.6)}
{cross(450, 110, 0.6)}''')

add('stamp out', '燃え残った小さな火を、靴の裏で踏みつけて完全に消す',
    '根絶する、踏み消す＝stamp out。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<g opacity="0.45">{flame(310, 344, 0.42)}</g>
<g transform="translate(290 300)">
  <path d="M-100 30q-6-40 30-46l60-6 74 30v22z" fill="{INK}"/>
  <path d="M-100 30h164v16h-164z" fill="#1f2a38"/>
  <path d="M-30-16v-90q0-18 20-18h30v108z" fill="{BLUD}"/></g>
{''.join(f'<path d="M{368+i*22} {296-i*18}l16-20" fill="none" stroke="{GLD}" stroke-width="5"/>' for i in range(2))}
{cross(500, 150, 0.7)}''')

# --- 下位の集団・見出し -------------------------------------------------------

add('subculture', '大きな集まりの中に、服装も好みも違う小さな集まりがある',
    '下位文化、サブカルチャー＝subculture。', f'''
<g transform="translate(300 200)"><path d="M-260-150h520v300h-520z" fill="#f1efe8" class="o"/></g>
{''.join(head(80 + (i % 5) * 92, 120 + (i // 5) * 110, 28, 'teal', 'short') for i in range(10) if not (i in (6, 7, 8)))}
<g transform="translate(430 260)">
  <path d="M-120-70h240v140h-240z" class="violetp o"/>
  {''.join(head(-76 + i * 76, 0, 28, 'violet', h) for i, h in enumerate(['cap', 'bun', 'bob']))}</g>
{ring(430, 260, 0, True)}''')

add('subheading', '大きな見出しの下に、ひと回り小さな見出しが段をつけて並ぶ',
    '小見出し＝subheading。', f'''
<g transform="translate(300 200)">
  <path d="M-230-150h460v300h-460z" class="paper"/>
  <rect x="-190" y="-116" width="300" height="30" rx="15" fill="{INK}"/>
  <rect x="-160" y="-52" width="180" height="20" rx="10" class="coral"/>
  {''.join(f'<rect x="-160" y="{-16+i*24}" width="{300-(i%2)*60}" height="10" rx="5" fill="{MUTED}"/>' for i in range(2))}
  <rect x="-160" y="50" width="180" height="20" rx="10" class="coral"/>
  {''.join(f'<rect x="-160" y="{86+i*24}" width="{300-(i%2)*60}" height="10" rx="5" fill="{MUTED}"/>' for i in range(2))}</g>
{''.join(f'<path d="M{100} {148+i*102}h-30" fill="none" stroke="{CRL}" stroke-width="0"/>' for i in range(2))}
{''.join(ring(140, 148 + i * 102, 0, True) for i in range(0))}''')

add('sublet', '借りている部屋の鍵を、さらに別の人へ貸し渡す',
    '又貸しする、又貸し＝sublet.', f'''
{house(300, 150, 0.52, 'coral')}
{person(120, 350, 1.05, 1, 'violet', 'blue', 'give', 'bun', 'smile')}
{person(300, 350, 1.05, 1, 'teal', 'green', 'give', 'short', 'smile')}
{person(480, 350, 1.05, -1, 'coral', 'gold', 'reach', 'bob', 'smile')}
{''.join(f'<g transform="translate({{}} 250)"><circle r="14" fill="none" stroke="{GLD}" stroke-width="6"/><path d="M14 0h44" stroke="{GLD}" stroke-width="7" fill="none"/><path d="M46 0v14h10V0z" fill="{GLD}"/></g>'.format(x) for x in (210, 390))}
{''.join(f'<path d="M{{}} 290h40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(x) for x in (170, 350))}''', arrow=True)

# --- 従属 --------------------------------------------------------------------

add('subordinate', '組織図の上の箱の下につながり、その指示を受ける立場にいる人',
    '部下、下位の＝subordinate。', f'''
<g transform="translate(300 130)"><rect x="-70" y="-46" width="140" height="92" rx="10" class="teal o"/>
  {head(0, 0, 26, 'teal', 'short')}</g>
<path d="M300 176v44M180 220h240M180 220v34M420 220v34" fill="none" stroke="{MUTED}" stroke-width="5"/>
{''.join(f'<g transform="translate({{}} 310)"><rect x="-70" y="-46" width="140" height="92" rx="10" class="tealp o"/>{{}}</g>'.format(x, head(0, 0, 26, 'coral', h)) for x, h in [(180, 'bob'), (420, 'bun')])}
{ring(180, 310, 84, True)}''')

add('subordination', '上から下へ向かう矢印だけがあり、下から上への線はない',
    '従属、下位に置くこと＝subordination。', f'''
<g transform="translate(300 100)"><rect x="-90" y="-46" width="180" height="92" rx="10" class="teal o"/></g>
{''.join(f'<path d="M300 150L{{}} 250" fill="none" stroke="{INK}" stroke-width="6" marker-end="url(#ar)"/>'.format(x) for x in (150, 300, 450))}
{''.join(f'<rect x="{{}}" y="260" width="120" height="80" rx="10" class="tealp o"/>'.format(x - 60) for x in (150, 300, 450))}
<g opacity="0.28"><path d="M120 250L260 150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="9 8"/></g>
{cross(110, 190, 0.5)}''', arrow=True)

add('subsection', '条文の番号の下に、さらに細かい枝番号の項がぶら下がる',
    '小区分、(条文の)項＝subsection。', f'''
<g transform="translate(300 200)">
  <path d="M-230-150h460v300h-460z" class="paper"/>
  <circle cx="-190" cy="-104" r="14" class="teal"/>
  <rect x="-160" y="-114" width="280" height="20" rx="10" fill="{INK}"/>
  {''.join(f'<g><circle cx="-140" cy="{-46+i*52}" r="11" class="coral"/><rect x="-116" y="{-55+i*52}" width="{220-(i%2)*50}" height="18" rx="9" fill="{MUTED}"/></g>' for i in range(3))}
  {''.join(f'<g><circle cx="-96" cy="{110}" r="9" class="coralp o"/><rect x="-74" y="{102}" width="180" height="16" rx="8" fill="{MUTED}"/></g>' for i in range(1))}</g>
{ring(200, 250, 0, True)}''')

add('subsequent to', '時間の線の上で、最初の印より後ろ側の出来事に目印がつく',
    '〜のあとに＝subsequent to。', f'''
<path d="M60 220h480" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
<circle cx="220" cy="220" r="18" class="teal o"/>
<path d="M220 150v140" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{''.join(f'<circle cx="{{}}" cy="220" r="18" class="coral o"/>'.format(340 + i * 100) for i in range(2))}
{arc(250, 150, 460, 150, 46, CRL, True, 5)}
{''.join(f'<path d="M{{}} 220v-14" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(100 + i * 80) for i in range(6))}''', arrow=True)

add('subset', '大きな円の内側に、そのうちの一部だけを囲む小さな円がある',
    '部分集合、一部＝subset。', f'''
<circle cx="300" cy="200" r="160" class="tealp o"/>
<circle cx="250" cy="210" r="80" class="coralp o"/>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="13" class="coral"/>'.format(x, y) for x, y in [(220, 180), (270, 200), (240, 250), (285, 245)])}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="13" class="teal"/>'.format(x, y) for x, y in [(380, 130), (400, 230), (340, 300), (300, 100)])}''')

# --- 沈下・微妙さ ------------------------------------------------------------

add('subsidence', '地面がへこんで沈み、その上の家が片側へ傾く',
    '地盤沈下＝subsidence。', f'''
<path d="M0 300h240q60 90 120 0h240v100H0z" fill="#cbb896" class="o"/>
<g opacity="0.28"><path d="M0 300h600" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/></g>
<g transform="translate(300 344) rotate(13)">{house(0, 0, 0.8, 'coral')}</g>
{''.join(f'<path d="M{{}} 250v46" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(x) for x in (230, 370))}
{''.join(f'<path d="M{{}} 360q20 14 40 0" fill="none" stroke="{BRN}" stroke-width="4"/>'.format(60 + i * 420) for i in range(2))}''', arrow=True)

add('subtlety', '並んだ二つの色は、目をこらしてやっと分かるほどのわずかな違い',
    '微妙さ、繊細さ＝subtlety。', f'''
<rect x="90" y="110" width="180" height="180" rx="10" fill="#238b83" stroke="{INK}" stroke-width="2.5"/>
<rect x="330" y="110" width="180" height="180" rx="10" fill="#26938a" stroke="{INK}" stroke-width="2.5"/>
<g transform="translate(300 330)">
  <circle r="38" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M26 26l34 34" stroke="{BRN}" stroke-width="12" stroke-linecap="round" fill="none"/></g>
{''.join(f'<path d="M{{}} 70v22" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(180 + i * 240) for i in range(2))}
<path d="M180 60h240" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>''')

# --- 成功・次々・苦しむ -------------------------------------------------------

add('succeed in', '難所をいくつも越えて、目ざしていた頂の旗にたどり着く',
    '〜に成功する＝succeed in。', f'''
<path d="M0 360L160 200l80 70 140-180 220 270z" fill="#d8cdb6" class="o"/>
{flag(460, 160, 0.6, 'coral', 110)}
{person(400, 190, 0.95, 1, 'teal', 'blue', 'up', 'cap', 'smile')}
<path d="M70 350q80-90 150-70t170-110" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 11" marker-end="url(#ar)"/>
{tick(120, 120, 0.8)}''', arrow=True)

add('successively', '倒れたドミノが次の一枚を倒し、それが次々に続いていく',
    '続けて、次々と＝successively。', f'''
{table(352)}
{''.join(domino(90 + i * 34, 280, -70 + i * 6, 0.8, 'teal') for i in range(4))}
{''.join(domino(260 + i * 60, 240, 0, 0.9, 'teal') for i in range(5))}
{''.join(f'<path d="M{{}} 140h40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(200 + i * 70) for i in range(4))}''', arrow=True)

add('suffer from', '長引く痛みに耐えかね、頭を抱えてうずくまる',
    '(病気などに)苦しむ＝suffer from。', f'''
<g transform="translate(300 340)">
  <path d="M-80 0v-110q80-30 160 0V0z" class="teal o"/>
  <path d="M-80-110q-20-60 30-70M80-110q20-60-30-70" fill="none" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>
  <circle cx="0" cy="-166" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-38-174q4-40 38-40 32 0 38 38-20-18-38-8-20-10-38 10z" fill="{HAIR}"/>
  <path d="M-22-166l18 8M22-166l-18 8" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-12-140q12-12 24 0" fill="none" stroke="{INK}" stroke-width="3"/></g>
{''.join(f'<path d="M{int(300+90*math.cos(math.radians(a)))} {int(174+90*math.sin(math.radians(a)))}l{int(30*math.cos(math.radians(a)))} {int(30*math.sin(math.radians(a)))}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for a in (-150, -120, -60, -30))}''')

add('suffocation', 'ガラスをかぶせたろうそくが、空気を失って炎が消える',
    '窒息＝suffocation。', f'''
{table(352)}
{split()}
<g transform="translate(150 300)">
  <path d="M-26 0q-4-90 0-100h52q4 10 0 100z" fill="#f0e6d2" class="o"/>
  <path d="M0-100v-12" stroke="{INK}" stroke-width="3" fill="none"/>
  {flame(0, -110, 0.3)}</g>
<g transform="translate(450 300)">
  <path d="M-26 0q-4-90 0-100h52q4 10 0 100z" fill="#f0e6d2" class="o"/>
  <path d="M0-100v-12" stroke="{INK}" stroke-width="3" fill="none"/>
  <path d="M0-118q12-14 0-26" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="7 7"/>
  <path d="M-70 10v-180a70 70 0 0 1 140 0V10z" fill="#ffffff" fill-opacity="0.34" stroke="{INK}" stroke-width="4"/></g>
{arc(260, 160, 340, 160, 44, MUTED, True, 4)}
{cross(540, 120, 0.5)}''', arrow=True)

# --- 要約・上位・超自然 -------------------------------------------------------

add('sum up', 'いくつも並んだ項目をひとまとめにして、一行の結論に落とす',
    '要約する、まとめる＝sum up。', f'''
{''.join(f'<rect x="80" y="{{}}" width="{{}}" height="20" rx="10" fill="{MUTED}"/>'.format(80 + i * 44, 260 - (i % 3) * 60) for i in range(4))}
<path d="M60 70h20M60 250h20" fill="none" stroke="{INK}" stroke-width="5"/>
<path d="M60 70v180" fill="none" stroke="{INK}" stroke-width="5"/>
{arc(380, 150, 430, 170, 46, MUTED, True, 5)}
<rect x="360" y="270" width="200" height="26" rx="13" class="teal"/>
{''.join(f'<path d="M{{}} 160h60" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}''', arrow=True)

add('superior to', '同じ台に並べた二つのうち、片方が一段高い位置に置かれる',
    '〜より優れている＝superior to。', f'''
<g transform="translate(300 330)">
  <path d="M-200 0v-60h180v60z" fill="{STONE}" class="o"/>
  <path d="M20 0v-140h180v140z" fill="{STONE}" class="o"/></g>
<circle cx="190" cy="240" r="44" class="tealp o"/>
<circle cx="410" cy="160" r="52" class="teal o"/>
<path d="M410 90V60M190 180v-30" fill="none" stroke="{MUTED}" stroke-width="0"/>
{tick(500, 100, 0.7)}
<path d="M120 240h-50M120 160h-50" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>
<path d="M84 160v80" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

add('supernatural', 'ふれてもいないのに物が宙に浮き、向こうが透けて見える影が立つ',
    '超自然の＝supernatural。', f'''
{table(352)}
<g opacity="0.45">
  <path d="M420 330q-40-140 0-190 34-42 70 0 40 50 0 190z" class="violetp o"/>
  <circle cx="440" cy="190" r="7" class="ink"/><circle cx="474" cy="190" r="7" class="ink"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-26" y="-20" width="52" height="40" rx="6" class="gold o"/></g>'.format(x, y, r) for x, y, r in [(150, 180, -12), (230, 130, 14), (200, 240, 8)])}
{''.join(f'<path d="M{{}} {{}}v34" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(x, y + 26) for x, y in [(150, 180), (230, 130), (200, 240)])}
{''.join(spark(300 + i * 40, 100 + (i % 2) * 40, 0.6, 'violet') for i in range(2))}''')

add('superpower', 'いくつも並ぶ国の旗の中で、ひとつだけがずば抜けて大きい',
    '超大国、超能力＝superpower。', f'''
{''.join(flag(80 + i * 90, 330, 0.42, 'tealp', 140) for i in range(3))}
{flag(390, 330, 1.15, 'coral', 240)}
{ring(430, 190, 0, True)}
{''.join(f'<path d="M{{}} 350h40" fill="none" stroke="{BRN}" stroke-width="6" stroke-linecap="round"/>'.format(60 + i * 90) for i in range(3))}''')

add('superstition', '黒い猫が前を横切っただけで、人が立ち止まって引き返す',
    '迷信＝superstition。', f'''
<path d="M40 350h520" fill="none" stroke="{STONE}" stroke-width="26" stroke-linecap="round"/>
{beast(300, 330, 0.34, '#2f3542', 1)}
{person(140, 350, 1.15, 1, 'teal', 'blue', 'up', 'short', 'sad')}
{arc(200, 230, 90, 250, 60, MUTED, True, 5)}
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(180 + i * 22, 160 - i * 14) for i in range(2))}''', arrow=True)

# --- 納入・抑圧・追加料金 -----------------------------------------------------

add('supplier', '工場から箱を積んだ荷が、注文した店へ運びこまれる',
    '納入業者、供給元＝supplier。', f'''
<g transform="translate(120 306)">
  <path d="M-90 0v-110h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-60-110v-40h30v40M10-110v-56h30v56" fill="{MUTED}" class="o"/>
  <path d="M-60-70h120v40h-120z" class="tealp o"/></g>
<g transform="translate(480 306)">
  <path d="M-90 0v-100h180V0z" fill="#fffefd" class="o"/>
  <path d="M-104-100h208l-16-36h-176z" class="coral o"/>
  <path d="M-50-60h100v60h-100z" class="coralp o"/></g>
{''.join(box(250 + i * 70, 250, 60, 46, 14, 'gold') for i in range(2))}
{arc(220, 200, 400, 200, 60, MUTED, True, 5)}''', arrow=True)

add('suppression', '声を上げようとする人を、上から大きな手が押さえつけて黙らせる',
    '抑圧、鎮圧／情報の握りつぶし＝suppression。', f'''
{hand(300, 120, 1)}
{''.join(head(180 + i * 120, 320, 30, 'teal', 'short', 'sad') for i in range(3))}
{''.join(f'<path d="M{{}} 260v-40" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="9 8"/>'.format(180 + i * 120) for i in range(3))}
{''.join(f'<path d="M{{}} 200v34" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"/>'.format(180 + i * 120) for i in range(3))}
{''.join(cross(180 + i * 120, 210, 0.3) for i in range(3))}''', arrow=True)

add('surcharge', '元の料金に、あとから追加の分が上乗せされる',
    '追加料金＝surcharge。', f'''
<g transform="translate(300 220)">
  <path d="M-160-120h320v240h-320z" class="paper"/>
  <rect x="-120" y="-80" width="200" height="26" rx="13" fill="{MUTED}"/>
  <rect x="-120" y="-20" width="140" height="26" rx="13" class="coral"/>
  <path d="M-130 34h260" fill="none" stroke="{INK}" stroke-width="4"/>
  <rect x="-120" y="52" width="240" height="30" rx="15" fill="{INK}"/>
  <path d="M-150-20h20M-140-30v20" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/></g>
{''.join(coin(500, 140 + i * 46, 20) for i in range(2))}
{arc(470, 120, 400, 190, 50, GLDD, True, 4)}''', arrow=True)

# --- 測量・かかりやすい・疑う ---------------------------------------------------

add('surveyor', '三脚に据えた測量機をのぞき、建物の位置と高さを測る',
    '測量士、建物調査士＝surveyor。', f'''
{building(450, 330, 0.9, 'coral')}
<g transform="translate(180 330)">
  <path d="M0-90l-46 90M0-90l46 90M0-90v90" stroke="{BRN}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M-34-130h68v40h-68z" fill="{MUTED}" class="o"/>
  <path d="M34-120h44v20H34z" fill="{INK}"/></g>
{person(110, 350, 1.0, 1, 'teal', 'blue', 'think', 'cap', 'smile')}
<path d="M230 214h150" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"/>
<path d="M540 120v210" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

add('susceptible', '同じ粒が飛んでくると、備えのない人だけが影響を受けてしまう',
    '影響を受けやすい、かかりやすい＝susceptible。', f'''
{split()}
{person(150, 350, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
{person(450, 350, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(450 240)">
  <path d="M-56-70h112v80q0 56-56 84-56-28-56-84z" class="bluep o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="9" class="coral o"/>'.format(80 + (i % 3) * 34, 130 + (i // 3) * 34) for i in range(6))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="9" class="coral o"/>'.format(380 + (i % 3) * 34, 130 + (i // 3) * 34) for i in range(6))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="8" class="coral"/>'.format(130 + i * 24, 250 + (i % 2) * 20) for i in range(3))}
{cross(150, 120, 0.4)}{tick(450, 120, 0.5)}''')

add('suspicious of', '差し出された品を受け取らず、細めた目でじっと疑ってみる',
    '〜を疑っている＝suspicious of。', f'''
{person(470, 350, 1.15, -1, 'coral', 'blue', 'give', 'short', 'smile')}
<g transform="translate(340 230)"><rect x="-46" y="-36" width="92" height="72" rx="8" class="gold o"/></g>
<g transform="translate(160 340)">
  <path d="M-70 0v-120q70-30 140 0V0z" class="teal o"/>
  <path d="M-70-120l-16 50M70-120q26 20 10 50" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
  <circle cx="0" cy="-166" r="32" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-36-174q4-38 36-38 30 0 36 36-20-16-36-6-18-10-36 8z" fill="{HAIR}"/>
  <path d="M-22-160h18M4-160h18" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-12-138h24" fill="none" stroke="{INK}" stroke-width="3"/></g>
<path d="M230 200h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>
<g transform="translate(160 110)">
  <path d="M-20-30q0-22 20-22t20 22q0 14-20 22v10" fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round"/>
  <circle cy="26" r="6" fill="{MUTED}"/></g>''', arrow=True)

# --- 持続・糧・揺れ ----------------------------------------------------------

add('sustainability', '一本切ったら一本植える。木の数が減らずに続いていく',
    '持続可能性＝sustainability。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
{tree(130, 320, 1.2)}{tree(300, 320, 1.2)}
<g transform="translate(470 320)">
  <path d="M0 0v-46" stroke="{GRND}" stroke-width="7" fill="none"/>
  <path d="M0-30q-34-4-38-34 34-4 38 34z" class="green o"/>
  <path d="M0-40q34-4 38-34-34-4-38 34z" class="green o"/></g>
<g transform="translate(300 130)"><path d="M-160 0a160 70 0 1 0 60-54" fill="none" stroke="{GRN}" stroke-width="7" marker-end="url(#ar)"/></g>
<g transform="translate(200 250) rotate(-30)"><path d="M-10 0h20v60h-20z" fill="{BRN}"/><path d="M-34-30h68v30h-68z" fill="{MUTED}" class="o"/></g>''', arrow=True)

add('sustenance', '一日を支えるだけのパンと水が、皿の上に用意されている',
    '栄養、糧＝sustenance。', f'''
{table(320)}
<g transform="translate(210 312)"><ellipse rx="100" ry="24" fill="#fffefd" class="o"/></g>
<g transform="translate(210 280)">
  <path d="M-70 30q-10-60 24-70 8-24 46-24t46 24q34 10 24 70z" fill="#d9a45e" class="o"/>
  <path d="M-70 30h140v18h-140z" fill="#b9813f" class="o"/></g>
<g transform="translate(430 270)">
  <path d="M-50 60l10-120h80l10 120z" fill="#fffefd" class="o"/>
  <path d="M-38 0h76l8 60h-92z" class="bluep"/>
  <path d="M-50 60l10-120h80l10 120z" fill="none" class="o"/></g>
{''.join(spark(120 + i * 380, 130, 0.6, 'gold') for i in range(2))}''')

add('sway', '風を受けた木が大きく左右に揺れ、幹がしなる',
    '揺れる／(意見を)動かす＝sway。', f'''
<g transform="translate(300 340) rotate(14)">{tree(0, 0, 1.9)}</g>
<g opacity="0.28" transform="translate(300 340) rotate(-14)">{tree(0, 0, 1.9)}</g>
{''.join(f'<path d="M40 {{}}q90-24 180 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>'.format(90 + i * 50) for i in range(3))}
<g transform="translate(300 90)"><path d="M-70 0q70-40 140 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/></g>''', arrow=True)

# --- 一蹴・甘く・すばやく -----------------------------------------------------

add('sweep aside', 'ほうきで、行く手にあったものをまとめて脇へ払いのける',
    '一蹴する、押しのける＝sweep aside。', f'''
{person(150, 350, 1.2, 1, 'teal', 'blue', 'hold', 'short', 'flat')}
<g transform="translate(250 280) rotate(32)">
  <path d="M-8-110h16v130h-16z" fill="{BRN}" class="o"/>
  <path d="M-34 20q34 46 68 0z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-26+i*13} 40v30" stroke="#c9a464" stroke-width="5" fill="none"/>' for i in range(5))}</g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-26" y="-20" width="52" height="40" rx="6" class="goldp o"/></g>'.format(x, y, r) for x, y, r in [(420, 300, 20), (470, 250, -14), (520, 310, 32), (500, 190, 8)])}
{arc(330, 250, 460, 200, 60, CRL, True, 6)}''', arrow=True)

add('sweeten', 'カップに角砂糖を落とすと、しかめ面が笑顔に変わる',
    '甘くする、(条件を)よくする＝sweeten。', f'''
{table(352)}
<g transform="translate(330 290)">
  <path d="M-70-60h140v60a50 50 0 0 1-50 50h-40a50 50 0 0 1-50-50z" fill="#fffefd" class="o"/>
  <path d="M70-40q44 0 44 40t-44 40" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-60-30h120v30a44 44 0 0 1-44 44h-32a44 44 0 0 1-44-44z" fill="#c88f4e"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-20" y="-20" width="40" height="40" rx="5" fill="#fffefd" class="o"/></g>'.format(320 + i * 14, 130 + i * 50, -10 + i * 20) for i in range(2))}
{head(120, 180, 40, 'teal', 'short', 'sad')}
{head(500, 180, 40, 'teal', 'short', 'smile')}
{arc(180, 120, 440, 120, 50, MUTED, True, 5)}''', arrow=True)

add('sweetness', 'はちみつがとろりと落ち、口にした人の顔がほころぶ',
    '甘さ、やさしさ＝sweetness。', f'''
{table(352)}
<g transform="translate(200 200) rotate(24)">
  <path d="M-40-70h80v110a24 24 0 0 1-24 24h-32a24 24 0 0 1-24-24z" class="goldp o"/>
  <path d="M-22-92h44v22h-44z" class="gold o"/></g>
<path d="M250 250q10 50 0 90" fill="none" stroke="{GLD}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(250 348)"><ellipse rx="70" ry="18" class="gold o"/></g>
{head(440, 230, 50, 'coral', 'bob', 'smile')}
{''.join(spark(370 + i * 40, 130 + (i % 2) * 30, 0.7, 'gold') for i in range(2))}''')

add('swiftly', '走り抜けた人のうしろに、速さを示す線が何本も引かれる',
    'すばやく＝swiftly。', f'''
{person(400, 350, 1.3, 1, 'teal', 'blue', 'walk', 'cap', 'smile')}
{''.join(f'<path d="M{{}} {{}}h110" fill="none" stroke="{MUTED}" stroke-width="{{}}" stroke-linecap="round"/>'.format(80 + (i % 2) * 40, 180 + i * 42, 8 - i) for i in range(4))}
{arc(200, 120, 480, 120, 40, TEA, True, 6)}''', arrow=True)

add('swirl', '水面の上で流れが渦を巻き、中心へ吸いこまれていく',
    '渦を巻く、渦＝swirl。', f'''
<path d="M0 60h600v340H0z" class="bluep"/>
<g transform="translate(300 220)">
  <path d="M0 0a30 30 0 1 1 26 16 70 70 0 1 1-88-24 120 120 0 1 1 174 60" fill="none" stroke="{BLU}" stroke-width="12" stroke-linecap="round"/>
  <path d="M0 0a54 54 0 1 0 52 30" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(40 + i * 120, 100 + (i % 2) * 250) for i in range(5))}''')

# --- 音節・授業計画・象徴 -----------------------------------------------------

add('syllable', '一つの語が、手をたたく回数どおりの音のかたまりに分かれる',
    '音節＝syllable。', f'''
<g opacity="0.3"><rect x="180" y="90" width="240" height="30" rx="15" fill="{MUTED}"/></g>
{''.join(f'<rect x="{{}}" y="190" width="110" height="70" rx="12" class="teal o"/>'.format(90 + i * 140) for i in range(3))}
{''.join(f'<g transform="translate({{}} 320)">{{}}</g>'.format(145 + i * 140, hand(0, 0, 1)) for i in range(3))}
{''.join(f'<path d="M{{}} 130v40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(145 + i * 140) for i in range(3))}''', arrow=True)

add('syllabus', '週ごとに学ぶ内容が、一覧表の形で並んでいる',
    '授業計画、シラバス＝syllabus。', f'''
<g transform="translate(300 200)">
  <path d="M-230-150h460v300h-460z" class="paper"/>
  <path d="M-230-150h460v50h-460z" class="teal o"/>
  {''.join(f'<path d="M-230 {-100+i*50}h460" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for i in range(1, 5))}
  <path d="M-130-150v300" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
  {''.join(f'<circle cx="-180" cy="{-76+i*50}" r="14" class="coralp o"/>' for i in range(5))}
  {''.join(f'<rect x="-100" y="{-86+i*50}" width="{260-(i%3)*60}" height="18" rx="9" fill="{MUTED}"/>' for i in range(5))}</g>''')

add('symbolism', '一羽の白い鳩が、平和という目に見えない意味を背負って示す',
    '象徴性、象徴主義＝symbolism。', f'''
{dove(200, 190, 1.3)}
{arc(330, 180, 420, 180, 50, MUTED, True, 5)}
<g transform="translate(480 200)">
  <path d="M0 44q-56-42-56-78 0-30 30-30 16 0 26 20 10-20 26-20 30 0 30 30 0 36-56 78z" class="coralp o"/></g>
{''.join(spark(130 + i * 40, 310 + (i % 2) * 20, 0.6, 'gold') for i in range(2))}''', arrow=True)

add('synthesise', 'いくつもの材料を一つにまとめ、まったく新しいものを作り出す',
    '合成する、(情報を)統合する＝synthesise。', f'''
{''.join(f'<circle cx="110" cy="{{}}" r="34" class="{{}} o"/>'.format(90 + i * 110, c) for i, c in enumerate(['coral', 'green', 'blue']))}
{''.join(f'<path d="M150 {{}}L300 200" fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"/>'.format(90 + i * 110) for i in range(3))}
<g transform="translate(370 200)">
  <path d="M-40-90h80v50l58 96a20 20 0 0 1-18 30h-160a20 20 0 0 1-18-30l58-96z" fill="#fffefd" class="o"/>
  <path d="M-96 46l30-50h132l30 50a20 20 0 0 1-18 40h-156a20 20 0 0 1-18-40z" class="violetp"/></g>
{''.join(spark(370 + (i * 2 - 1) * 80, 70, 0.7, 'gold') for i in range(2))}''', arrow=True)

# --- 大衆紙・先細り・考慮 -----------------------------------------------------

add('tabloid', '紙面いっぱいの大きな見出しと写真が目を引く大衆紙',
    'タブロイド紙、大衆紙＝tabloid。', f'''
<g transform="translate(300 200)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <rect x="-170" y="-120" width="340" height="50" rx="8" fill="{INK}"/>
  <rect x="-170" y="-54" width="220" height="34" rx="8" class="coral"/>
  <path d="M-170 0h190v130h-190z" class="tealp o"/>
  <circle cx="-100" cy="40" r="26" class="teal o"/>
  <path d="M-150 130q60-80 120 0z" class="teal o"/>
  {''.join(f'<rect x="44" y="{6+i*28}" width="126" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}</g>''')

add('tail off', 'まっすぐ太かった線が、先へ行くほど細くなって消えていく',
    '次第に減る、しりすぼみになる＝tail off。', f'''
{''.join(f'<path d="M{60+i*70} 200h70" fill="none" stroke="{TEA}" stroke-width="{26-i*4}" stroke-linecap="round"/>' for i in range(6))}
<g opacity="0.3"><path d="M480 200h60" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/></g>
{''.join(f'<rect x="{{}}" y="{{}}" width="50" height="{{}}" rx="6" class="tealp o"/>'.format(70 + i * 80, 330 - (120 - i * 22), 120 - i * 22) for i in range(6))}''')

add('take account of', '天秤に、忘れずにもうひとつの重りも載せて判断する',
    '〜を考慮に入れる＝take account of。', f'''
{scales(300, 320, 0, 1.0)}
{''.join(f'<rect x="{{}}" y="176" width="40" height="34" rx="6" class="teal o"/>'.format(130 + i * 44) for i in range(2))}
<g transform="translate(420 190)"><rect x="-24" y="-20" width="48" height="40" rx="6" class="coral o"/></g>
{arc(470, 90, 424, 150, 40, CRL, True, 5)}
{tick(520, 300, 0.6)}''', arrow=True)

add('take for granted', '毎日そこにある水道の水に、だれも目を向けなくなる',
    '当然のことと思う、ありがたみを忘れる＝take for granted。', f'''
<g transform="translate(210 200)">
  <path d="M-110 0h100v-60h60" fill="none" stroke="{MUTED}" stroke-width="20" stroke-linecap="round"/>
  <circle cx="-10" cy="-60" r="20" class="blue o"/></g>
{''.join(drop(260, 230 + i * 34, 1.2, 'blue') for i in range(3))}
{person(450, 350, 1.2, -1, 'teal', 'blue', 'walk', 'short', 'smile')}
<g transform="translate(430 200)"><path d="M-30 0q30-22 60 0-30 22-60 0z" fill="#fffefd" class="o"/><circle r="10" class="ink"/>
  <path d="M-34-22l68 44" stroke="{CRL}" stroke-width="7" stroke-linecap="round" fill="none"/></g>''')

add('take into account', '検討の一覧に、忘れていた項目を書き加えてから考える',
    '〜を考慮に入れる＝take into account。', f'''
<g transform="translate(270 210)">
  <path d="M-160-130h320v260h-320z" class="paper"/>
  {''.join(f'<g><rect x="-130" y="{-100+i*44}" width="16" height="16" rx="3" fill="none" stroke="{MUTED}" stroke-width="3"/><rect x="-104" y="{-102+i*44}" width="{210-(i%3)*50}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(4))}
  <g><rect x="-130" y="76" width="16" height="16" rx="3" class="coral o"/><rect x="-104" y="74" width="180" height="14" rx="7" class="coral"/></g></g>
{arc(500, 160, 400, 290, 60, CRL, True, 5)}
<g transform="translate(520 120)"><rect x="-40" y="-24" width="80" height="48" rx="8" class="coralp o"/></g>''', arrow=True)

add('take issue with', '相手の資料の一行だけを指さし、そこに異議を唱える',
    '〜に異議を唱える＝take issue with。', f'''
<g transform="translate(330 200)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  {''.join(f'<rect x="-140" y="{-104+i*48}" width="{280-(i%3)*60}" height="16" rx="8" fill="{MUTED}"/>' for i in range(5))}
  <rect x="-150" y="-8" width="300" height="34" rx="17" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{hand(120, 210, 1)}
{line(168, 210, 220, 205, CRL, False, 5)}
{''.join(f'<path d="M{{}} {{}}q14 12 0 24" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(110 + i * 16, 110 + i * 16) for i in range(2))}''', arrow=True)

# --- 思い切る・好きになる・買収 -------------------------------------------------

add('take the plunge', '高い台のふちで一瞬ためらい、思い切って水へ飛びこむ',
    '思い切ってやる＝take the plunge。', f'''
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(120 300)"><path d="M-70 0v-190h180v30h-150V0z" fill="{STONE}" class="o"/></g>
<g opacity="0.28">{person(150, 140, 0.95, 1, 'teal', 'blue', 'stand', 'short', 'flat')}</g>
<g transform="translate(370 210) rotate(48)">{person(0, 0, 1.05, 1, 'teal', 'blue', 'up', 'short', 'smile')}</g>
{arc(200, 120, 360, 190, 70, MUTED, True, 5)}
{''.join(f'<path d="M{{}} 306q22-14 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(380 + i * 60) for i in range(3))}''', arrow=True)

add('take to', '初めて手にした道具なのに、すぐに気に入って使いこなす',
    '好きになる、なじむ＝take to。', f'''
{person(220, 350, 1.3, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(290 240) rotate(-20)">
  <path d="M-10-70h20v110a24 24 0 1 1-20-22z" class="goldd o"/></g>
<g transform="translate(300 100)">
  <path d="M0 26q-34-26-34-48 0-18 18-18 10 0 16 12 6-12 16-12 18 0 18 18 0 22-34 48z" class="coralp o"/></g>
{''.join(spark(430 + i * 40, 170 + (i % 2) * 40, 0.7, 'gold') for i in range(2))}
{clock(120, 130, 32, 12, 2)}''')

add('takeover', '店の看板が外され、別の会社の看板に掛け替えられる',
    '企業買収、乗っ取り＝takeover。', f'''
{split()}
{''.join(f'<g transform="translate({{}} 340)"><path d="M-100 0v-120h200V0z" fill="#fffefd" class="o"/><path d="M-114-120h228l-18-40h-192z" class="{{}} o"/><path d="M-50-80h100v50h-100z" class="{{}}p o"/></g>'.format(x, c, c) for x, c in [(150, 'teal'), (450, 'violet')])}
<g opacity="0.28" transform="translate(250 120) rotate(22)"><path d="M-60-24h120v48h-120z" class="teal o"/></g>
<g transform="translate(450 130)"><path d="M-70-26h140v52h-140z" class="violet o"/></g>
{arc(260, 180, 340, 180, 44, MUTED, True, 5)}
{''.join(coin(300, 290 + i * 0, 20) for i in range(1))}''', arrow=True)

finish(__file__)
