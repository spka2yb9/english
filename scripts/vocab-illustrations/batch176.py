# -*- coding: utf-8 -*-
"""第176回。sn-/so-/sp-/st-/su- の語。shriek / signify の描き直しも含む。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def pie_slices(x, y, r, n, cls='gold'):
    g = [f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls} o"/>']
    for i in range(n):
        a = math.radians(i * 360 / n - 90)
        g.append(f'<path d="M{x} {y}L{x+r*math.cos(a):.0f} {y+r*math.sin(a):.0f}" stroke="{INK}" stroke-width="3" fill="none"/>')
    return ''.join(g)

def bread(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-90 40q-14-80 30-92 10-30 60-30t60 30q44 12 30 92z" fill="#d9a45e" class="o"/>'
            f'<path d="M-90 40h180v22h-180z" fill="#b9813f" class="o"/></g>')

# --- 第175回の描き直し -------------------------------------------------------

add('shriek', '大きく口を開けて叫び、鋭い線が四方へ飛び散る',
    '金切り声をあげる、悲鳴＝shriek。', f'''
<g transform="translate(300 220)">
  <circle r="86" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-84-34q6-62 84-62t84 62q-36-28-84-18-46-10-84 18z" fill="{HAIR}"/>
  <path d="M-40-12l26 12M40-12l-26 12" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <ellipse cy="46" rx="28" ry="34" class="ink"/></g>
{''.join(f'<path d="M{int(300+150*math.cos(math.radians(a)))} {int(220+150*math.sin(math.radians(a)))}l{int(46*math.cos(math.radians(a)))} {int(46*math.sin(math.radians(a)))}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for a in range(-180, 181, 30))}''')

add('signify', '掲げられた赤い旗が「止まれ」という決まった意味を伝える',
    '意味する、示す＝signify。', f'''
<g transform="translate(140 306)">
  <path d="M0 0v-200" stroke="{BRN}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <path d="M6-200h120l-30 36 30 36H6z" class="coral o"/></g>
{arc(300, 180, 380, 180, 50, MUTED, True, 5)}
<g transform="translate(470 200)">
  <circle r="96" class="coral o"/>
  <circle r="74" fill="none" stroke="#fffefd" stroke-width="8"/>
  {hand(0, 6, 1)}</g>''', arrow=True)

# --- 支障・目的・条件 ---------------------------------------------------------

add('snag', 'すべっていた糸が、途中の出っぱりに引っかかって止まる',
    '思わぬ支障、引っかかり＝snag。', f'''
<path d="M40 200h240" fill="none" stroke="{TEA}" stroke-width="9" stroke-linecap="round"/>
<g transform="translate(300 200)">
  <path d="M-20 0q20-40 40 0t40 0" fill="none" stroke="{TEA}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-12-60v54" stroke="{MUTED}" stroke-width="11" fill="none" stroke-linecap="round"/>
  <ellipse cx="-12" cy="-62" rx="16" ry="7" fill="{MUTED}" class="o"/></g>
<g opacity="0.3"><path d="M380 200h180" fill="none" stroke="{MUTED}" stroke-width="9" stroke-dasharray="10 9"/></g>
{''.join(f'<path d="M{330+i*20} {150-i*14}l14-18" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(2))}
{cross(500, 300, 0.6)}''')

add('so as to', '高い枝の実に手が届くよう、わざわざはしごを持ってきて掛ける',
    '〜するために＝so as to。', f'''
{tree(420, 340, 1.6)}
<circle cx="400" cy="140" r="22" class="coral o"/>
<g transform="translate(320 340) rotate(-18)">
  <path d="M-26 0v-230M26 0v-230" stroke="{BRN}" stroke-width="11" fill="none" stroke-linecap="round"/>
  {''.join(f'<path d="M-26 {-30-i*40}h52" stroke="{BRN}" stroke-width="9" fill="none" stroke-linecap="round"/>' for i in range(5))}</g>
{person(160, 350, 1.1, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
{arc(220, 210, 320, 180, 60, MUTED, True, 4)}''', arrow=True)

add('so long as', '条件の緑の帯が続いているあいだだけ、橋を渡っていける',
    '〜する限りは＝so long as。', f'''
<g transform="translate(300 260)">
  <path d="M-250-20h340v40h-340z" class="greenp o"/>
  <g opacity="0.3"><path d="M90-20h160v40H90z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/></g>
  <path d="M-250 20v40M90 20v40M250 20v40" stroke="{MUTED}" stroke-width="8" fill="none" stroke-linecap="round"/></g>
{person(140, 240, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{tick(200, 130, 0.6)}
{cross(470, 130, 0.6)}
<g transform="translate(390 320)"><path d="M-40 0h80" fill="none" stroke="{MUTED}" stroke-width="0"/></g>''')

add('so to speak', '言葉の代わりに、たとえの絵をそっと差し出して言い換える',
    'いわば＝so to speak。', f'''
{person(140, 350, 1.2, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<g transform="translate(360 190)">
  <path d="M-140-100h280v170h-40l-24 32-18-32h-198z" fill="#fffefd" class="o"/>
  {beast(0, 40, 0.34, '#c08b3e', 1)}
  <path d="M-120-80q-10 22 10 26M-92-80q-10 22 10 26" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  <path d="M92-80q-10 22 10 26M120-80q-10 22 10 26" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/></g>''')

# --- 社会主義・やわらかさ・独奏 -------------------------------------------------

add('socialism', 'ひとつのパイが、集まった全員に同じ大きさで切り分けられる',
    '社会主義＝socialism。', f'''
{pie_slices(300, 210, 130, 6, 'gold')}
{''.join(head(70 + i * 92, 350, 24, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('coral', 'bob'), ('green', 'bun'), ('blue', 'cap'), ('violet', 'short'), ('gold', 'bob')]))}
{''.join(f'<path d="M{int(300+140*math.cos(math.radians(-90+i*60)))} {int(210+140*math.sin(math.radians(-90+i*60)))}L{70+i*92} {318}" fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="7 7"/>' for i in range(6))}''')

add('softness', '指で押すとへこみ、離すとまた戻るやわらかなクッション',
    'やわらかさ＝softness。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-150-60q60-30 150-30t150 30q20 60 0 90h-300q-20-30 0-90z" class="violetp o"/>
  <path d="M-30-70q30 40 60 0" fill="none" stroke="{VIO}" stroke-width="0"/>
  <path d="M-40-72q40 44 80 0" fill="{VIOP}" stroke="{VIO}" stroke-width="4"/></g>
{hand(300, 130, 1)}
{line(300, 182, 300, 208, MUTED, True, 4)}
{''.join(f'<path d="M{{}} {{}}q12-14 0-26" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(470 + i * 20, 220 - i * 14) for i in range(2))}''', arrow=True)

add('soloist', '暗い舞台でひとりだけに光が当たり、その人の演奏が響く',
    '独奏者、独唱者＝soloist。', f'''
<g transform="translate(300 200)"><path d="M-250-150h500v300h-500z" fill="#3b4557"/></g>
<path d="M300 50L200 350h200z" fill="#fff6d8" opacity="0.55"/>
{person(300, 350, 1.25, 1, 'coral', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(346 262) rotate(-30)">
  <path d="M-10-60h20v96a26 26 0 1 1-20-25z" class="goldd o"/></g>
{''.join(f'<g opacity="0.28">{head(90 + i * 420, 330, 26, "blue", "short")}</g>' for i in range(2))}
{''.join(f'<path d="M{{}} {{}}q14-16 0-30" fill="none" stroke="#fff6d8" stroke-width="4"/>'.format(420 + i * 20, 160 - i * 12) for i in range(2))}''')

# --- 支払い能力・溶媒・すっぱい -------------------------------------------------

add('solvency', '天秤にのせた資産が負債より重く、支払える側に傾く',
    '支払い能力＝solvency。', f'''
{scales(300, 320, -12, 1.0)}
{''.join(coin(160 + i * 28, 180 - (i // 3) * 26, 16) for i in range(6))}
<g transform="translate(400 210)">{doc(0, 0, 76, 56, 2)}</g>
{tick(510, 130, 0.7)}''')

add('solvent', '角砂糖が水の中で溶けて消え、液に混ざってしまう',
    '溶媒／支払い能力のある＝solvent。', f'''
{table(352)}
{''.join(f'<g transform="translate({{}} 250)"><path d="M-60-80l10 160h100l10-160z" fill="#fffefd" class="o"/><path d="M-46-10h92l6 90h-104z" class="bluep"/><path d="M-60-80l10 160h100l10-160z" fill="none" class="o"/></g>'.format(x) for x in (150, 450))}
<g transform="translate(150 210)"><rect x="-22" y="-22" width="44" height="44" rx="5" fill="#fffefd" class="o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="5" fill="#ffffff"/>'.format(430 + (i % 3) * 20, 250 + (i // 3) * 24) for i in range(6))}
{arc(250, 170, 350, 170, 46, MUTED, True, 4)}''', arrow=True)

add('sour', 'レモンをひと口かじって、思わず顔をすぼめる',
    'すっぱい／(関係が)険悪になる＝sour。', f'''
<g transform="translate(300 220)">
  <circle r="100" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-98-36q8-64 98-64t98 64q-42-28-98-20-52-8-98 20z" fill="{HAIR}"/>
  <path d="M-52-10q18-16 36 0M16-10q18-16 36 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-26 54q26-26 52 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-54 34q14 10 28 0M26 34q14 10 28 0" fill="none" stroke="{SKINL}" stroke-width="3"/></g>
<g transform="translate(470 300) rotate(-20)">
  <ellipse rx="60" ry="42" class="gold o"/>
  <path d="M56-6q16 4 16 10-16 6-16 0z" class="goldd o"/></g>
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{GLD}" stroke-width="5"/>'.format(120 + i * 22, 120 - i * 14) for i in range(2))}''')

# --- 道具・専門化・説明 -------------------------------------------------------

add('spade', '刃の広いすきを土に突き立てて、掘り返す',
    'すき、シャベル＝spade。', f'''
<path d="M0 300h600v100H0z" fill="#5b4636"/>
<g transform="translate(300 210) rotate(16)">
  <path d="M-10-160h20v170h-20z" fill="{BRN}" class="o"/>
  <path d="M-40-190h80v34h-80z" fill="{BRN}" class="o"/>
  <path d="M-46 10h92l-10 90q-36 24-72 0z" fill="{MUTED}" class="o"/></g>
<g transform="translate(150 330)"><path d="M-60-16q60-24 120 0-20 26-60 26t-60-26z" fill="#3f3126"/></g>
{''.join(f'<path d="M{{}} 350q20 12 40 0" fill="none" stroke="#3f3126" stroke-width="4"/>'.format(400 + i * 60) for i in range(2))}''')

add('specialisation', '広い分野の中から一つの区画だけを選び、そこを深く掘り下げる',
    '専門化、専攻＝specialisation。', f'''
<g transform="translate(300 160)">
  {''.join(f'<rect x="{{}}" y="{{}}" width="76" height="60" rx="6" class="{{}} o"/>'.format(-230 + (i % 6) * 78, -60 + (i // 6) * 68, 'coral' if i == 8 else 'tealp') for i in range(12))}</g>
<path d="M340 200v130" fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round" marker-end="url(#ar)"/>
{''.join(f'<path d="M{{}} {{}}h{{}}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>'.format(280, 250 + i * 34, 120) for i in range(3))}
{ring(340, 130, 54, True)}''', arrow=True)

add('spell out', '省略せず、一文字ずつを大きく並べてはっきり示す',
    'はっきり説明する、一語一語述べる＝spell out。', f'''
<g opacity="0.3"><rect x="60" y="100" width="180" height="30" rx="15" fill="{MUTED}"/></g>
{arc(160, 170, 300, 200, 50, MUTED, True, 5)}
{''.join(f'<rect x="{{}}" y="240" width="60" height="80" rx="8" class="teal o"/>'.format(90 + i * 82) for i in range(6))}
{''.join(f'<path d="M{{}} 340v14" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(120 + i * 82) for i in range(6))}
{person(480, 150, 0.8, -1, 'coral', 'blue', 'point', 'short', 'smile')}''', arrow=True)

# --- けが・芽・噴出 ----------------------------------------------------------

add('sprain', 'ひねった足首が腫れ、そこを手で押さえて痛がる',
    'ねんざする、ねんざ＝sprain。', f'''
<g transform="translate(300 250)">
  <path d="M-30-160q30-20 60 0v130l70 20v40h-160v-50z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-10" cy="-10" r="44" class="coralp"/>
  <circle cx="-10" cy="-10" r="44" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{''.join(f'<path d="M{int(290+70*math.cos(math.radians(a)))} {int(240+70*math.sin(math.radians(a)))}l{int(26*math.cos(math.radians(a)))} {int(26*math.sin(math.radians(a)))}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for a in (-140, -100, -60, 200, 160))}
{hand(440, 250, -1)}
{line(420, 250, 370, 245, MUTED, True, 4)}''', arrow=True)

add('sprout', '土の中の種から、小さな芽が顔を出して伸び始める',
    '芽を出す、芽＝sprout。', f'''
<path d="M0 280h600v120H0z" fill="#5b4636"/>
<g transform="translate(300 280)">
  <path d="M0 40v-40" stroke="{GRND}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M0 0v-60" stroke="{GRND}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M0-40q-46-6-50-44 44-6 50 44z" class="green o"/>
  <path d="M0-52q46-6 50-44-44-6-50 44z" class="green o"/>
  <ellipse cy="46" rx="24" ry="18" fill="#b9813f" class="o"/></g>
{''.join(f'<path d="M{{}} 330q20 12 40 0" fill="none" stroke="#3f3126" stroke-width="4"/>'.format(60 + i * 130) for i in range(4))}
{sun(500, 90, 40)}''')

add('spurt', '細い管の口から、水が勢いよく一気に噴き出す',
    'ほとばしる、急な伸び＝spurt。', f'''
<g transform="translate(150 260)">
  <path d="M-110 0h140v40h-140z" fill="{MUTED}" class="o"/>
  <path d="M30-10h40v60H30z" fill="{MUTED}" class="o"/></g>
<path d="M220 270q90-90 200-70t150 80" fill="none" stroke="{BLU}" stroke-width="26" stroke-linecap="round"/>
{''.join(drop(320 + i * 60, 160 + (i % 2) * 22, 1.2, 'blue') for i in range(3))}
{''.join(f'<path d="M{{}} {{}}l18-22" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(230 + i * 18, 220 - i * 16) for i in range(2))}''')

# --- 安定・利害・古い ---------------------------------------------------------

add('stabilisation', 'ぐらついていた塔に支えが入り、もう揺れなくなる',
    '安定化＝stabilisation。', f'''
{split()}
<g transform="translate(150 340) rotate(-9)">
  {''.join(f'<rect x="-40" y="{{}}" width="80" height="46" rx="6" class="tealp o"/>'.format(-50 - i * 52) for i in range(5))}</g>
{''.join(f'<path d="M{{}} {{}}q14-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(240 + i * 16, 130 - i * 12) for i in range(2))}
<g transform="translate(450 340)">
  {''.join(f'<rect x="-40" y="{{}}" width="80" height="46" rx="6" class="teal o"/>'.format(-50 - i * 52) for i in range(5))}
  <path d="M-42-40L-110 0M42-40L110 0" stroke="{BRN}" stroke-width="14" fill="none" stroke-linecap="round"/></g>
{tick(450, 60, 0.6)}''')

add('stakeholder', 'ひとつの事業を囲んで、関わる人がそれぞれ持ち分の札を手にする',
    '利害関係者＝stakeholder。', f'''
<g transform="translate(300 210)">
  <path d="M-80-70h160v140h-160z" class="teal o"/>
  <path d="M-92-70L0-130l92 60z" class="teald o"/></g>
{''.join(f'<g transform="translate({{}} {{}})">{{}}</g>'.format(x, y, head(0, 0, 26, c, h)) for x, y, c, h in [
  (90, 120, 'coral', 'short'), (510, 120, 'green', 'bob'), (90, 330, 'blue', 'bun'), (510, 330, 'gold', 'cap')])}
{''.join(f'<rect x="{{}}" y="{{}}" width="44" height="30" rx="5" class="{{}}p o"/>'.format(x, y, c) for x, y, c in [
  (150, 106, 'coral'), (406, 106, 'green'), (150, 316, 'blue'), (406, 316, 'gold')])}
{''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(x1, y1, x2, y2) for x1, y1, x2, y2 in [
  (196, 122, 220, 150), (404, 122, 380, 150), (196, 330, 220, 280), (404, 330, 380, 280)])}''')

add('stale', '固くなって割れ目の入ったパンが、皿の上に残されている',
    '(パンなどが)古くなった／新鮮味のない＝stale。', f'''
{table(352)}
<g transform="translate(300 290)">
  <ellipse rx="150" ry="34" fill="#fffefd" class="o"/></g>
{bread(300, 250, 0.95)}
<g transform="translate(300 250)">
  <path d="M-30-40l10 36-24 20M40-30l-14 40 22 20" fill="none" stroke="#8a5c2b" stroke-width="5"/></g>
{''.join(f'<path d="M{{}} {{}}q12-14 0-26" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(470 + i * 20, 210 - i * 14) for i in range(2))}
{clock(120, 130, 40, 11, 50)}''')

add('stamina', '長い道のりを走り続けても、残り体力の目盛りがまだ高い',
    '持久力、スタミナ＝stamina。', f'''
<path d="M40 350q120-40 260-40t260 40" fill="none" stroke="{STONE}" stroke-width="26" stroke-linecap="round"/>
{person(360, 330, 1.25, 1, 'teal', 'blue', 'walk', 'cap', 'smile')}
{''.join(f'<path d="M{{}} {{}}l-26 6" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(280 - i * 30, 300 + i * 10) for i in range(3))}
<g transform="translate(300 90)">
  <path d="M-160-24h320v48h-320z" fill="#fffefd" class="o"/>
  <path d="M-152-16h276v32h-276z" class="green"/></g>
{''.join(f'<path d="M{{}} 90v0" fill="none"/>'.format(x) for x in (0,))}''')

# --- 踏み消す・擁護・譲らない ---------------------------------------------------

add('stamp out', '燃え残った小さな火を、靴で踏みつけて完全に消す',
    '根絶する、踏み消す＝stamp out。', f'''
<g opacity="0.42">{flame(300, 340, 0.5)}</g>
<g transform="translate(290 250)">
  <path d="M-70 30q0-56 50-56h34l52 34v22z" fill="{INK}"/>
  <path d="M-70 30h136v14h-136z" fill="#1f2a38"/>
  <path d="M-14-26v-90" stroke="{BLUD}" stroke-width="26" fill="none" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{GLD}" stroke-width="5"/>'.format(380 + i * 20, 300 - i * 16) for i in range(2))}
{cross(490, 160, 0.7)}''')

add('stand up for', '責められている人の前に立ち、その盾になって守る',
    '(人・信念を)擁護する、味方する＝stand up for。', f'''
{person(490, 350, 1.2, -1, 'coral', 'blue', 'point', 'short', 'sad')}
{person(300, 350, 1.3, -1, 'teal', 'green', 'up', 'short', 'flat')}
<g opacity="0.6">{person(180, 350, 1.05, 1, 'violet', 'gold', 'stand', 'bob', 'sad')}</g>
{''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>'.format(430, 150 + i * 40, 370, 175 + i * 40) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}l-26 20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>'.format(350, 165 + i * 44) for i in range(2))}''')

add('stand your ground', '押されても足を線から動かさず、その場に踏みとどまる',
    '立場を譲らない＝stand your ground。', f'''
<path d="M300 60v300" fill="none" stroke="{CRL}" stroke-width="6" stroke-dasharray="14 12"/>
{person(340, 350, 1.35, -1, 'teal', 'blue', 'stand', 'short', 'flat')}
{hand(180, 220, 1)}
{''.join(f'<path d="M{{}} {{}}h46" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(226, 200 + i * 50) for i in range(2))}
{''.join(f'<path d="M{{}} 350h20" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>'.format(320 + i * 40) for i in range(2))}
{tick(490, 120, 0.7)}''', arrow=True)

# --- 標準化・観点・主食 -------------------------------------------------------

add('standardisation', 'ばらばらの大きさだった品が、どれも同じ規格の形にそろう',
    '標準化、規格統一＝standardisation。', f'''
{split()}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="{{}}" y="{{}}" width="{{}}" height="{{}}" rx="6" class="tealp o"/></g>'.format(x, y, r, -w / 2, -h / 2, w, h) for x, y, r, w, h in [
  (100, 150, 8, 90, 60), (210, 130, -12, 60, 80), (110, 290, -6, 110, 50), (220, 280, 14, 70, 70)])}
{''.join(f'<rect x="{{}}" y="{{}}" width="80" height="70" rx="6" class="teal o"/>'.format(340 + (i % 2) * 110, 120 + (i // 2) * 130) for i in range(4))}
{arc(270, 90, 330, 90, 40, MUTED, True, 5)}''', arrow=True)

add('standpoint', '同じ立体でも、見る位置が変わればまったく別の形に見える',
    '観点、立場＝standpoint。', f'''
<g transform="translate(300 200)">
  <path d="M-60-70h120v140h-120z" class="teal o"/>
  <path d="M-60-70l40-40h120l-40 40z" class="tealp o"/>
  <path d="M60-70l40-40v140l-40 40z" class="teald o"/></g>
{head(90, 320, 28, 'coral', 'short')}
{head(510, 320, 28, 'green', 'bob')}
{line(130, 300, 220, 250, MUTED, True, 4)}
{line(470, 300, 380, 250, MUTED, True, 4)}
<g transform="translate(90, 100)"><rect x="-40" y="-30" width="80" height="60" rx="6" class="tealp o"/></g>
<g transform="translate(510 100)"><path d="M-40-30h60l20 20v40h-80z" class="teald o"/></g>
{''.join(f'<path d="M{{}} 220v-70" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(x) for x in (90, 510))}''', arrow=True)

add('staple', '食卓のまん中に、毎日欠かさず並ぶ主食が置かれている',
    '主要な、定番の／主食＝staple。', f'''
{table(300)}
<g transform="translate(300 292)"><ellipse rx="110" ry="26" fill="#fffefd" class="o"/></g>
{bread(300, 250, 1.0)}
{''.join(f'<g transform="translate({{}} 292)"><ellipse rx="44" ry="12" fill="#fffefd" class="o"/><ellipse rx="22" ry="6" class="{{}}p"/></g>'.format(x, c) for x, c in [(100, 'green'), (500, 'coral')])}
{ring(300, 250, 130, True)}
{''.join(spark(120 + i * 360, 120, 0.6, 'gold') for i in range(2))}''')

# --- 飢え・静止・法令 ---------------------------------------------------------

add('starvation', '皿には何も載っておらず、やせ細った人がうなだれる',
    '飢餓、餓死＝starvation。', f'''
{table(300)}
<g transform="translate(390 292)">
  <ellipse rx="90" ry="22" fill="#fffefd" class="o"/>
  <ellipse rx="48" ry="12" fill="none" stroke="{MUTED}" stroke-width="2.5"/></g>
<g transform="translate(170 300)">
  <path d="M-10-12l-6 12M10-12l6 12" fill="none" stroke="{BLUD}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-30-96q30-12 60 0l-8 84h-44z" fill="{TEA}" class="o"/>
  <path d="M-30-96l-20 46M30-96l20 44" fill="none" stroke="{SKIN}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="0" cy="-122" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-30-130q4-32 30-32 24 0 30 30-16-14-30-6-14-8-30 8z" fill="{HAIR}"/>
  <circle cx="-9" cy="-122" r="2.6" class="ink"/><circle cx="9" cy="-122" r="2.6" class="ink"/>
  <path d="M-9-106q9-8 18 0" fill="none" stroke="{INK}" stroke-width="2.2"/></g>
{''.join(f'<path d="M{{}} {{}}q12 12 0 24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(240 + i * 18, 160 + i * 14) for i in range(2))}''')

add('static', '振り子が真下で止まったまま、まったく動かない',
    '静止した、変化のない／雑音＝static。', f'''
<g transform="translate(300 90)">
  <path d="M-140 0h280" stroke="{BRN}" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M0 0v190" stroke="{MUTED}" stroke-width="6" fill="none"/>
  <circle cy="216" r="36" class="teal o"/></g>
<g opacity="0.22">
  <path d="M300 90l-120 150M300 90l120 150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/>
  <circle cx="180" cy="246" r="30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
  <circle cx="420" cy="246" r="30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g>
{cross(120, 330, 0.5)}{cross(480, 330, 0.5)}''')

add('statute', '番号のついた条文がまとめられ、一冊の法令集になっている',
    '制定法、法令＝statute。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M-120-110h240v220h-240z" fill="#fffefd" class="o"/>
  <path d="M-128-110h18v220h-18z" class="violetd o"/>
  {''.join(f'<g transform="translate(-84 {{}})"><circle r="10" class="violet"/><rect x="24" y="-7" width="{{}}" height="14" rx="7" fill="{MUTED}"/></g>'.format(-70 + i * 44, 150 - (i % 3) * 40) for i in range(5))}</g>
<g transform="translate(300 100)">
  <path d="M-60 20l-12-40 40 24 32-40 32 40 40-24-12 40z" class="gold o" transform="scale(0.5)"/></g>''')

# --- 由来・退く・介入 ---------------------------------------------------------

add('stem from', '一本の太い幹から枝が伸び、どの枝もその幹に行き着く',
    '〜に由来する＝stem from。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(300 340)">
  <path d="M-24 0v-120h48V0z" fill="{BRN}" class="o"/>
  <path d="M-16-120L-140-230M16-120L140-230M0-120v-120" stroke="{BRN}" stroke-width="14" fill="none" stroke-linecap="round"/>
  <circle cx="-140" cy="-240" r="40" class="greenp o"/>
  <circle cx="140" cy="-240" r="40" class="greenp o"/>
  <circle cx="0" cy="-260" r="40" class="greenp o"/></g>
{''.join(f'<path d="M{{}} {{}}L300 240" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(x, y) for x, y in [(180, 120), (420, 120), (300, 100)])}''', arrow=True)

add('step down', '演壇に立っていた人が、自分から段を降りて席へ戻る',
    '(地位を)辞任する、退く＝step down。', f'''
<g transform="translate(200 340)">
  <path d="M-90 0v-60h180v60z" fill="{STONE}" class="o"/>
  <path d="M-60-60v-50h150v50z" fill="{STONE}" class="o"/></g>
<g opacity="0.28">{person(230, 230, 1.0, 1, 'violet', 'blue', 'up', 'short', 'flat')}</g>
{person(440, 350, 1.15, 1, 'violet', 'blue', 'walk', 'short', 'flat')}
{arc(290, 200, 410, 240, 60, MUTED, True, 5)}''', arrow=True)

add('step in', '言い合う二人の間に、もう一人が割って入って止める',
    '割って入る、介入する＝step in。', f'''
{person(110, 350, 1.15, 1, 'coral', 'blue', 'up', 'short', 'sad')}
{person(490, 350, 1.15, -1, 'green', 'blue', 'up', 'bob', 'sad')}
{person(300, 350, 1.3, 1, 'teal', 'violet', 'point', 'bun', 'flat')}
{hand(230, 200, -1)}{hand(370, 200, 1)}
{arc(300, 110, 300, 200, 0, MUTED, True, 5)}''', arrow=True)

add('step up', '同じ作業の量を一段ずつ増やし、前より高い段へ上げる',
    '強化する、増やす＝step up。', f'''
{''.join(f'<rect x="{{}}" y="{{}}" width="90" height="{{}}" rx="6" class="teal o"/>'.format(60 + i * 110, 330 - (60 + i * 70), 60 + i * 70) for i in range(4))}
{arc(100, 240, 460, 80, 70, MUTED, True, 5)}
<path d="M40 336h500" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>''', arrow=True)

# --- 続ける・硬さ・烙印 -------------------------------------------------------

add('stick with', '新しい道具に目もくれず、使い慣れた一本をそのまま使い続ける',
    'やり続ける、〜のままでいく＝stick with。', f'''
{person(200, 350, 1.25, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(254 250) rotate(-16)">
  <path d="M-9-80h18v120h-18z" fill="{BRN}" class="o"/>
  <path d="M-30 40h60v26h-60z" fill="{MUTED}" class="o"/></g>
<g opacity="0.28" transform="translate(470 250)">
  {''.join(f'<g transform="translate({{}} 0)"><path d="M-8-60h16v90h-16z" fill="{MUTED}"/><path d="M-24 30h48v20h-48z" fill="{MUTED}"/></g>'.format(-50 + i * 50) for i in range(3))}</g>
{cross(470, 130, 0.6)}
{tick(200, 130, 0.6)}''')

add('stiffness', '力を加えても曲がらない板の横で、同じ力で別の板はしなる',
    'こわばり、硬さ＝stiffness。', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-110-16h220v32h-220z" fill="#c9a464" class="o"/>
  <path d="M-110 16v34M110 16v34" stroke="{BRN}" stroke-width="10" fill="none"/></g>
{hand(150, 100, 1)}
{line(150, 140, 150, 170, MUTED, True, 4)}
<g transform="translate(450 210)">
  <path d="M-110-24q110 70 220 0v32q-110 70-220 0z" fill="#e0d0ae" class="o"/>
  <path d="M-110 22v30M110 22v30" stroke="{BRN}" stroke-width="10" fill="none"/></g>
{hand(450, 100, 1)}
{line(450, 140, 450, 180, MUTED, True, 4)}
{tick(150, 320, 0.6)}''', arrow=True)

add('stigma', '人の背に大きな×のレッテルが貼られ、周りが距離を取る',
    '汚名、負のレッテル＝stigma。', f'''
{person(220, 350, 1.35, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(220 250) rotate(-8)">
  <path d="M-56-46h112v92h-112z" class="paper"/>
  {cross(0, 0, 0.8)}</g>
{''.join(head(450 + i * 0, 180 + i * 130, 26, 'coral', 'bob') for i in range(2))}
{''.join(f'<path d="M{{}} {{}}l30-6" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(400, 180 + i * 130) for i in range(2))}''', arrow=True)

# --- 静けさ・刺激・明記 -------------------------------------------------------

add('stillness', '風のない湖面は鏡のように平らで、岸の木も揺れない',
    '静けさ、動きのなさ＝stillness。', f'''
<path d="M0 230h600v170H0z" class="bluep"/>
<path d="M0 230h600" fill="none" stroke="{BLU}" stroke-width="4"/>
{tree(450, 230, 1.1)}
<g transform="translate(450 230) scale(1 -1)" opacity="0.32">{tree(0, 0, 1.1)}</g>
{sun(110, 110, 40)}
<g opacity="0.32"><circle cx="110" cy="330" r="40" class="goldp"/></g>
{''.join(f'<path d="M{{}} 300h60" fill="none" stroke="{BLU}" stroke-width="3"/>'.format(180 + i * 90) for i in range(2))}''')

add('stimulation', '差しこまれた光と電気を受けて、眠っていた芽が反応する',
    '刺激＝stimulation。', f'''
<g transform="translate(340 320)">
  <path d="M0 40v-90" stroke="{GRND}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M0-30q-46-6-50-44 44-6 50 44z" class="green o"/>
  <path d="M0-42q46-6 50-44-44-6-50 44z" class="green o"/>
  <ellipse cy="44" rx="50" ry="20" fill="#b9813f" class="o"/></g>
{sun(120, 110, 42)}
{''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(190, 150 + i * 30, 280, 210 + i * 20) for i in range(2))}
{bolt(500, 150, 1.3)}
{line(480, 200, 400, 250, GLD, False, 5)}
{''.join(spark(300 + i * 40, 200 - (i % 2) * 26, 0.6, 'gold') for i in range(2))}''', arrow=True)

add('stipulate', '契約書の一項に印をつけ、その条件をはっきり書き込む',
    '(契約などで)明記する＝stipulate。', f'''
{table(352)}
<g transform="translate(280 230)">
  <path d="M-150-110h300v220h-300z" class="paper"/>
  {''.join(f'<rect x="-120" y="{{}}" width="{{}}" height="12" rx="6" fill="{MUTED}"/>'.format(-80 + i * 40, 230 - (i % 3) * 50) for i in range(4))}
  <rect x="-120" y="40" width="200" height="14" rx="7" class="coral"/>
  <rect x="-140" y="34" width="250" height="26" rx="13" fill="none" stroke="{CRL}" stroke-width="4"/></g>
<g transform="translate(470 140) rotate(34)">
  <path d="M-9-90h18v130l-9 24-9-24z" class="coral o"/></g>''')

add('stipulation', '契約書から一本の線が伸び、その先に条件の札が下がっている',
    '条件、規定＝stipulation。', f'''
{doc(170, 210, 190, 240, 4)}
<path d="M266 220h100" fill="none" stroke="{MUTED}" stroke-width="5"/>
<g transform="translate(450 250) rotate(-6)">
  <path d="M-100-60h200v120h-200z" class="goldp o"/>
  {''.join(f'<rect x="-76" y="{{}}" width="{{}}" height="12" rx="6" fill="{GLDD}"/>'.format(-34 + i * 32, 140 - i * 44) for i in range(2))}
  {tick(60, 0, 0.36)}</g>
<circle cx="366" cy="220" r="10" class="gold o"/>''')

# --- かき立てる・争い・独立 -----------------------------------------------------

add('stir up', '鍋をぐるぐるかき混ぜると、沈んでいたものが一気に舞い上がる',
    '(感情や騒ぎを)かき立てる＝stir up。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-110-50h220v80a40 40 0 0 1-40 40h-140a40 40 0 0 1-40-40z" fill="#cfd6db" class="o"/>
  <path d="M-100-40h200v66a30 30 0 0 1-30 30h-140a30 30 0 0 1-30-30z" class="coralp"/>
  <path d="M-136-50h26M110-50h26" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/></g>
<g transform="translate(320 170) rotate(20)">
  <path d="M-8-100h16v190h-16z" fill="{BRN}" class="o"/></g>
<g transform="translate(300 250)"><path d="M-70 0a70 34 0 1 0 26-26" fill="none" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" class="coral o"/>'.format(210 + i * 50, 160 - (i % 2) * 34, 8 + i % 3) for i in range(4))}''', arrow=True)

add('strife', '一本の綱を両側から引き合い、どちらも譲らずにもめ続ける',
    '争い、対立＝strife。', f'''
<path d="M80 230h440" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
{person(150, 350, 1.25, -1, 'coral', 'blue', 'reach', 'short', 'sad')}
{person(450, 350, 1.25, 1, 'teal', 'green', 'reach', 'bob', 'sad')}
<path d="M300 190v80" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="10 9"/>
{''.join(f'<path d="M{{}} 130h{{}}" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(x, d) for x, d in [(260, -70), (340, 70)])}''', arrow=True)

add('strike out', '所属していた輪から離れ、自分ひとりで新しい道へ踏み出す',
    '新たに独り立ちする＝strike out。', f'''
{ring(170, 220, 120, True, 'teal')}
{''.join(head(120 + (i % 2) * 100, 170 + (i // 2) * 100, 26, 'teal', 'short') for i in range(4))}
{person(450, 350, 1.2, 1, 'coral', 'blue', 'walk', 'short', 'smile')}
{arc(300, 250, 400, 280, 50, MUTED, True, 5)}
<path d="M340 360h240" fill="none" stroke="{STONE}" stroke-width="22" stroke-linecap="round"/>''', arrow=True)

add('stronghold', '厚い石壁と塔にかこまれた砦が、高い丘の上に構えている',
    '拠点、地盤＝stronghold。', f'''
<path d="M0 330q140-70 300-70t300 70v70H0z" class="greenp o"/>
<g transform="translate(300 290)">
  <path d="M-150 0v-130h300V0z" fill="{STONE}" class="o"/>
  <path d="M-150-130v-30h34v-18h34v18h40v-18h34v18h40v-18h34v18h34v30z" fill="{STONE}" class="o"/>
  <path d="M-190 0v-190h44V0zM146 0v-190h44V0z" fill="#b5bec4" class="o"/>
  <path d="M-196-190h56v-24h-56zM140-190h56v-24h-56z" fill="#a1abb2" class="o"/>
  <path d="M-30 0v-70h60V0z" class="corald o"/></g>''')

# --- 部会・潜在意識 ----------------------------------------------------------

add('subcommittee', '大きな会議体の中から、少人数の小さな部会が切り出される',
    '小委員会＝subcommittee。', f'''
<g transform="translate(230 200)">
  <path d="M-180-140h360v280h-360z" fill="#f1efe8" class="o"/>
  {''.join(head(-140 + (i % 4) * 92, -90 + (i // 4) * 92, 26, 'teal', 'short') for i in range(12))}</g>
<g transform="translate(480 220)">
  <path d="M-90-80h180v160h-180z" class="coralp o"/>
  {''.join(head(-42 + (i % 2) * 84, -34 + (i // 2) * 70, 24, 'coral', 'bob') for i in range(4))}</g>
{arc(330, 120, 420, 130, 50, MUTED, True, 5)}''', arrow=True)

add('subconscious', '水面の上に出ているのはごく一部で、大半は水の下に沈んでいる',
    '潜在意識の、潜在意識＝subconscious。', f'''
<path d="M0 160h600v240H0z" class="bluep"/>
<path d="M0 160h600" fill="none" stroke="{BLU}" stroke-width="5"/>
<path d="M300 40l70 120H230z" fill="#eaf4f8" class="o"/>
<path d="M230 160h140l70 190q-140 60-280 0z" fill="#cfe6f0" class="o"/>
{''.join(f'<path d="M{{}} 172q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(30 + i * 100) for i in range(2))}
{''.join(f'<path d="M{{}} 172q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(450 + i * 80) for i in range(2))}
{head(120, 90, 30, 'teal', 'short')}
{line(160, 100, 230, 110, MUTED, True, 4)}''', arrow=True)

finish(__file__)
