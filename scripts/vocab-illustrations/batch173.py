# -*- coding: utf-8 -*-
"""第173回。m-/n-/o-/p- の前半。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def flag(x, y, s=1, cls='violet', pole=110):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-{pole}" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>'
            f'<path d="M5-{pole}h100l-24 30 24 30H5z" class="{cls} o"/></g>')

def bucket(x, y, s=1, hole=False):
    h = f'<circle cx="20" cy="40" r="12" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>' if hole else ''
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-70-60h140l-20 120h-100z" class="tealp o"/>'
            f'<path d="M-70-60q70-24 140 0" fill="none" stroke="{INK}" stroke-width="3"/>{h}</g>')

def nail(x, y, r=0, s=1):
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})">'
            f'<path d="M-6 0h12v70l-6 14-6-14z" fill="{MUTED}" class="o"/>'
            f'<ellipse cy="-2" rx="16" ry="6" fill="{MUTED}" class="o"/></g>')

# --- 和らげる・近代化 ---------------------------------------------------------

add('mitigate', '落ちてくる重い箱の下に厚いクッションを敷き、衝撃を和らげる',
    '(悪影響を)和らげる、軽減する＝mitigate。', f'''
{box(300, 120, 150, 100, 34, 'gold')}
{line(300, 190, 300, 250, MUTED, True, 5)}
<g transform="translate(300 320)">
  <path d="M-160-40q160-40 320 0v40h-320z" class="violetp o"/>
  <path d="M-160-40q160-40 320 0" fill="none" stroke="{VIO}" stroke-width="4"/></g>
{''.join(f'<path d="M{140+i*40} 268q16-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{tick(510, 180, 0.7)}''', arrow=True)

add('modernisation', '古びた低い家が取り壊され、同じ場所に新しい高い建物が建つ',
    '近代化＝modernisation。', f'''
{split()}
<g opacity="0.85">{house(150, 330, 0.9, 'coral')}</g>
{''.join(f'<path d="M{110+i*40} 240l6 22" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{tower(450, 330, 1.05, 'teal', 6)}
{arc(250, 200, 340, 190, 46, MUTED, True, 5)}''', arrow=True)

# --- 死亡率・母 --------------------------------------------------------------

add('mortality', '並んだ十の人影のうち、いくつかが色を失って灰色になる',
    '死亡率、死すべき運命＝mortality。', f'''
{''.join(head(70 + (i % 5) * 116, 150 + (i // 5) * 150, 34, 'teal', 'short') for i in range(10) if i not in (2, 7, 9))}
{''.join(f'<g opacity="0.32">{head(70 + (i % 5) * 116, 150 + (i // 5) * 150, 34, "blue", "short")}</g>' for i in (2, 7, 9))}
{''.join(cross(70 + (i % 5) * 116, 150 + (i // 5) * 150, 0.5) for i in (2, 7, 9))}''')

add('motherhood', '母親が腕の中に赤ん坊を抱き、頭をそっと支えている',
    '母であること、母性＝motherhood。', f'''
<g transform="translate(300 330)">
  <path d="M-90 0v-150q90-40 180 0V0z" class="coral o"/>
  <path d="M-90-150l-20 60q60 40 120 10" fill="none" stroke="{SKIN}" stroke-width="24" stroke-linecap="round"/>
  <circle cx="0" cy="-198" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-38-206q4-44 38-44 32 0 38 42-20-18-38-8-20-12-38 10z" fill="{HAIR}"/>
  <circle cx="-12" cy="-200" r="3" class="ink"/><circle cx="12" cy="-200" r="3" class="ink"/>
  <path d="M-10-186q10 9 20 0" fill="none" stroke="{INK}" stroke-width="2.4"/>
  <g transform="translate(28 -104) rotate(20)">
    <path d="M-46-16q46-22 92 0 10 34-10 44h-72q-20-10-10-44z" class="goldp o"/>
    <circle cx="-46" cy="-24" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <circle cx="-54" cy="-26" r="2.4" class="ink"/><circle cx="-38" cy="-26" r="2.4" class="ink"/>
    <path d="M-52-16q8 6 14 0" fill="none" stroke="{INK}" stroke-width="2"/></g></g>
{''.join(spark(120 + i * 360, 120, 0.7, 'gold') for i in range(2))}''')

# --- じっくり考える・互いに -----------------------------------------------------

add('mull over', 'あごに手を当てた人の頭の上を、いくつかの案がゆっくり回っている',
    'じっくり考える＝mull over。', f'''
{person(190, 350, 1.25, 1, 'teal', 'blue', 'think', 'short', 'flat')}
<g transform="translate(400 170)">
  <path d="M-130 0a130 70 0 1 0 4-24" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 11" marker-end="url(#ar)"/>
  {''.join(f'<rect x="{-104+i*70}" y="-20" width="52" height="40" rx="8" class="{c} o"/>' for i, c in enumerate(['coral', 'gold', 'green', 'violet']))}</g>
<circle cx="250" cy="220" r="12" fill="#fffefd" class="o"/>
<circle cx="228" cy="250" r="8" fill="#fffefd" class="o"/>
{clock(120, 150, 36, 2, 20)}''', arrow=True)

add('mutually', '二人が同じ品をそれぞれ相手へ渡し、行き来が両方向になる',
    '互いに＝mutually。', f'''
{person(140, 340, 1.2, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(460, 340, 1.2, -1, 'coral', 'green', 'give', 'bob', 'smile')}
<path d="M220 160h160" fill="none" stroke="{TEA}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M380 230H220" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"/>
<g transform="translate(300 120)"><rect x="-28" y="-22" width="56" height="44" rx="7" class="teal o"/></g>
<g transform="translate(300 272)"><rect x="-28" y="-22" width="56" height="44" rx="7" class="coral o"/></g>''', arrow=True)

# --- 確定・絞り込み・僅差 -----------------------------------------------------

add('nail down', 'ぐらついていた板にくぎを打ちこみ、もう動かないようにする',
    '(細部を)はっきり決める、確定する＝nail down。', f'''
{table(352)}
<g transform="translate(300 300)"><path d="M-190-34h380v34h-380z" fill="#c9a464" class="o"/></g>
{nail(190, 234, 0, 1.0)}{nail(410, 234, 0, 1.0)}
<g transform="translate(300 160) rotate(-26)">
  <path d="M-11 0h22v130h-22z" fill="{BRN}" class="o"/>
  <path d="M-44-36h88v36h-88z" fill="{MUTED}" class="o"/></g>
{''.join(f'<path d="M{210+i*18} {212-i*12}l14-18" fill="none" stroke="{GLD}" stroke-width="5"/>' for i in range(2))}
{tick(500, 200, 0.8)}''')

add('narrow down', 'たくさんの候補が漏斗を通り、下から出てくるのはごくわずか',
    '絞り込む＝narrow down。', f'''
{''.join(f'<circle cx="{100+(i%6)*80}" cy="{70+(i//6)*44}" r="18" class="{c} o"/>' for i, c in enumerate(['teal','coral','gold','green','violet','blue','teal','coral','gold','green','violet','blue']))}
<g transform="translate(300 230)">
  <path d="M-190-50h380l-160 90v70h-60v-70z" fill="#fffefd" class="o"/>
  <path d="M-190-50h380l-22 24h-336z" class="tealp"/></g>
<circle cx="300" cy="350" r="20" class="coral o"/>
<circle cx="240" cy="360" r="14" class="teal o"/>''')

add('narrowly', 'ゴールの線で、二人の差はほんのわずかしかない',
    'かろうじて、僅差で＝narrowly。', f'''
<path d="M420 60v300" fill="none" stroke="{INK}" stroke-width="6"/>
{''.join(f'<rect x="{402+(i%2)*18}" y="{70+i*20}" width="18" height="18" fill="{INK}"/>' for i in range(14))}
{person(390, 340, 1.2, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{person(310, 340, 1.2, 1, 'coral', 'green', 'walk', 'bob', 'sad')}
<path d="M330 120h100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
{ring(370, 120, 22, True)}''', arrow=True)

# --- 国有化・帰化・中和 -------------------------------------------------------

add('nationalisation', '会社の建物に立っていた旗が、国の旗に替わる',
    '国有化＝nationalisation。', f'''
{split()}
{building(150, 330, 0.9, 'teal')}
{flag(150, 190, 0.6, 'teal', 120)}
{building(450, 330, 0.9, 'teal')}
{flag(450, 190, 0.6, 'coral', 120)}
{arc(260, 150, 340, 150, 44, MUTED, True, 5)}''', arrow=True)

add('naturalisation', '手続きの印を受けたあと、新しい国の旗を手にする',
    '帰化＝naturalisation。', f'''
{person(140, 340, 1.2, 1, 'teal', 'blue', 'carry', 'short', 'smile')}
<g transform="translate(230 230) rotate(-10)">
  <path d="M-46-60h92v120h-92z" class="bluep o"/>
  <circle cx="0" cy="-16" r="20" class="blue o"/>
  <circle cx="24" cy="30" r="20" class="coralp o"/>
  <circle cx="24" cy="30" r="12" fill="none" stroke="{CRL}" stroke-width="3"/></g>
{arc(320, 190, 400, 190, 46, MUTED, True, 5)}
{person(480, 340, 1.2, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{flag(480, 210, 0.66, 'coral', 150)}''', arrow=True)

add('neutralisation', '酸の赤い液と塩基の青い液を合わせると、どちらでもない色になる',
    '中和、無力化＝neutralisation。', f'''
{table(352)}
{''.join(f'<g transform="translate({{}} 230)"><path d="M-34-70h68v82a34 34 0 0 1-68 0z" fill="#fffefd" class="o"/><path d="M-34-10h68v22a34 34 0 0 1-68 0z" class="{{}}"/></g>'.format(x, c) for x, c in [(120, 'coral'), (250, 'blue')])}
{''.join(f'<path d="M{{}} 180q30 40 70 44" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(x) for x in (140, 270))}
<g transform="translate(440 280)">
  <path d="M-16-90h32v48l52 88a14 14 0 0 1-12 22h-112a14 14 0 0 1-12-22l52-88z" fill="#fffefd" class="o"/>
  <path d="M-58 26l16-28h84l16 28a14 14 0 0 1-12 40h-92a14 14 0 0 1-12-40z" class="violetp"/></g>''', arrow=True)

add('neutron', '原子核の中で、プラスでもマイナスでもない粒がまざっている',
    '中性子＝neutron。', f'''
<g transform="translate(300 200)">
  <circle r="150" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 11"/>
  {''.join(f'<circle cx="{x}" cy="{y}" r="34" class="coralp o"/><path d="M{x-14} {y}h28M{x} {y-14}v28" stroke="{CRL}" stroke-width="6" fill="none" stroke-linecap="round"/>' for x, y in [(-56, -34), (40, 44)])}
  {''.join(f'<circle cx="{x}" cy="{y}" r="34" class="tealp o"/>' for x, y in [(46, -44), (-40, 46), (0, 0)])}
  {''.join(f'<circle cx="{x}" cy="{y}" r="34" fill="none" class="o"/>' for x, y in [(46, -44), (-40, 46), (0, 0)])}</g>
{ring(300, 200, 34, False, 'teal')}
<circle cx="480" cy="90" r="20" class="tealp o"/>
{line(460, 100, 330, 180, MUTED, True, 3)}''', arrow=True)

add('normalise', '大きく乱れていた波形が、標準の線にそって静かな形に戻る',
    '正常化する＝normalise。', f'''
<path d="M60 200h480" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
<path d="M70 200q20-110 40 0t40-90 40 90 40-60 40 60" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>
<path d="M310 200q20-30 40 0t40 0 40-14 40 14 40 0" fill="none" stroke="{GRN}" stroke-width="6" stroke-linecap="round"/>
{arc(270, 110, 330, 110, 40, MUTED, True, 4)}
{tick(500, 310, 0.7)}''', arrow=True)

# --- 反対・ふと浮かぶ・条件 -----------------------------------------------------

add('object to', '進もうとする案の前に手を挙げて立ち、そこで止める',
    '反対する、異議を唱える＝object to。', f'''
{doc(140, 200, 130, 170, 3)}
{line(220, 200, 280, 200, MUTED, False, 6)}
{hand(330, 200, 1)}
{person(440, 340, 1.25, -1, 'coral', 'blue', 'reach', 'short', 'flat')}
{''.join(f'<path d="M{{}} {{}}q14 10 0 22" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(370 + i * 16, 120 + i * 14) for i in range(3))}''', arrow=True)

add('occur to', '歩いている人の頭の上に、小さな星のひらめきが不意に浮かぶ',
    '(考えが)ふと浮かぶ＝occur to。', f'''
{person(240, 350, 1.3, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
<g transform="translate(330 120)">
  <path d="M-86-46h172v92h-172z" fill="#fffefd" class="o" rx="20"/>
  {''.join(spark(-40 + i * 40, 0, 1.0, 'gold') for i in range(3))}</g>
<circle cx="250" cy="200" r="13" fill="#fffefd" class="o"/>
<circle cx="228" cy="232" r="9" fill="#fffefd" class="o"/>''')

add('on condition that', '鍵を渡す手に、これを満たせばという条件の札が結びつけてある',
    '〜という条件で＝on condition that。', f'''
{hand(150, 200, 1)}
<g transform="translate(300 200)">
  <circle r="26" fill="none" stroke="{GLD}" stroke-width="9"/>
  <path d="M26 0h90" stroke="{GLD}" stroke-width="11" fill="none"/>
  <path d="M92 0v22h14V0zM68 0v18h12V0z" fill="{GLD}"/></g>
<path d="M300 226v50" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g transform="translate(300 330) rotate(-6)">
  <path d="M-110-50h220v100h-220z" class="paper"/>
  {''.join(f'<rect x="-86" y="{{}}" width="{{}}" height="10" rx="5" fill="{MUTED}"/>'.format(-30 + i * 30, 160 - i * 50) for i in range(2))}
  {tick(70, 0, 0.4)}</g>
{ring(300, 200, 78, True)}''')

# --- 開放・稼働・選ぶ ---------------------------------------------------------

add('openness', '扉も窓も大きく開け放たれ、中がそのまま見える家',
    '開放性、率直さ＝openness。', f'''
<g transform="translate(300 330)">
  <path d="M-150 0v-170h300V0z" fill="#fffefd" class="o"/>
  <path d="M-170-170L0-268l170 98z" class="corald o"/>
  <path d="M-40 0v-110h80V0z" fill="#fffaf1" class="o"/>
  <path d="M-40-110l-46-24v130l46-20M40-110l46-24v130l-46-20" class="coral o"/>
  <path d="M-120-140h64v60h-64zM56-140h64v60H56z" fill="#fffaf1" class="o"/>
  <path d="M-120-140l-40-20v104l40-18M56-140l40-20v104l-40-18" class="coralp o"/></g>
{sun(90, 80, 40)}
{''.join(f'<path d="M{{}} 200q20-16 40 0" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(430 + i * 50) for i in range(2))}''')

add('operative', '稼働中のランプがともり、機械がいま実際に動いている',
    '有効な、稼働中の＝operative。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M-160-100h320v200h-320z" class="teal o"/>
  <circle cx="-100" cy="-56" r="24" class="greenp o"/>
  <circle cx="-100" cy="-56" r="12" class="green"/>
  <path d="M-40-70h180v50h-180zM-40 10h180v50h-180z" class="tealp o"/></g>
{''.join(f'<path d="M{{}} {{}}q14-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(490 + i * 20, 150 - i * 14) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}l18-20" fill="none" stroke="{GRN}" stroke-width="5" stroke-linecap="round"/>'.format(150 + i * 0, 110 + i * 26) for i in range(2))}
{tick(120, 210, 0.6)}''')

add('opt for', '並んだ二つのうち、片方だけを選び取って手元に置く',
    '〜のほうを選ぶ＝opt for。', f'''
{split()}
<g opacity="0.3"><rect x="70" y="140" width="160" height="140" rx="12" class="teal o"/></g>
<rect x="370" y="140" width="160" height="140" rx="12" class="coral o"/>
{hand(450, 340, 1)}
{tick(450, 90, 0.8)}
{''.join(f'<path d="M{{}} 330h-20" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (150,))}
{cross(150, 90, 0.6)}''')

add('opt out', '列に並んでいた一人が、自分から脇へ外れて参加をやめる',
    '(制度から)抜ける、参加しないことを選ぶ＝opt out。', f'''
{''.join(head(90 + i * 80, 230, 28, 'teal', 'short') for i in range(4))}
{head(430, 230, 28, 'teal', 'bob')}
<path d="M118 230h284" fill="none" stroke="{TEA}" stroke-width="6"/>
<g transform="translate(300 350)">{head(0, 0, 28, 'coral', 'bun')}</g>
{arc(300, 268, 300, 316, -46, CRL, True, 5)}
{cross(500, 120, 0.6)}''', arrow=True)

# --- 最適化・独創・抗議 -------------------------------------------------------

add('optimisation', '遠回りだった経路が、むだのない最短の道筋に引き直される',
    '最適化＝optimisation。', f'''
<circle cx="90" cy="300" r="22" class="teal o"/>
<circle cx="510" cy="110" r="22" class="coral o"/>
<path d="M90 300q40-130 150-90t60 130 120-30 90-90" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 11"/>
<path d="M112 288L488 122" fill="none" stroke="{GRN}" stroke-width="8" stroke-linecap="round"/>
{tick(160, 120, 0.7)}''')

add('optimise', 'つまみを回して設定を合わせると、効率の針が上へ振れる',
    '最適化する＝optimise。', f'''
<g transform="translate(170 250)">
  <circle r="90" fill="#fffefd" class="o"/>
  <circle r="62" class="tealp o"/>
  <path d="M0 0v-58" stroke="{INK}" stroke-width="12" stroke-linecap="round" fill="none" transform="rotate(40)"/>
  {''.join(f'<path d="M0-92v-16" transform="rotate({a})" stroke="{MUTED}" stroke-width="4" fill="none"/>' for a in range(-60, 61, 30))}</g>
{hand(170, 250, 1)}
<g transform="translate(440 280)">
  <path d="M-130 0A130 130 0 0 1 130 0z" fill="#fffefd" class="o"/>
  <path d="M0 0L92-80" stroke="{GRN}" stroke-width="10" stroke-linecap="round" fill="none"/>
  <circle r="12" class="ink"/></g>
{arc(280, 200, 370, 190, 50, MUTED, True, 4)}''', arrow=True)

add('originality', 'そっくりな絵が並ぶ中に、まったく違う一枚が混じる',
    '独創性＝originality。', f'''
{''.join(f'<g transform="translate({{}} 200)"><path d="M-52-66h104v132h-104z" fill="#fffefd" class="o"/><circle cy="-14" r="26" class="tealp o"/><path d="M-34 50q34-46 68 0z" class="tealp o"/></g>'.format(90 + i * 116) for i in range(3))}
<g transform="translate(438 200)">
  <path d="M-52-66h104v132h-104z" fill="#fffefd" class="o"/>
  {star(0, 0, 0.8, 'coral') if False else ''}
  <path d="M0-48l14 26 30 4-22 22 6 30-28-14-28 14 6-30-22-22 30-4z" class="coral o"/></g>
{ring(438, 200, 82, True)}
<g transform="translate(554 200)"><path d="M-52-66h104v132h-104z" fill="#fffefd" class="o"/><circle cy="-14" r="26" class="tealp o"/></g>''')

add('outcry', '大勢が声を上げ、掲げた札をそろえて強く抗議する',
    '抗議の声、激しい非難＝outcry。', f'''
{''.join(person(90 + i * 110, 350, 1.05, 1, c, 'blue', 'up', h, 'sad') for i, (c, h) in enumerate([('teal', 'short'), ('coral', 'bob'), ('green', 'bun'), ('violet', 'cap'), ('gold', 'short')]))}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-40" y="-30" width="80" height="60" rx="6" class="coral o"/></g>'.format(90 + i * 110, 110 + (i % 2) * 26, -8 + i * 5) for i in range(5))}
{''.join(f'<path d="M{{}} {{}}q12 10 0 20" fill="none" stroke="{CRL}" stroke-width="4"/>'.format(40 + i * 130, 220 + (i % 2) * 20) for i in range(4))}''')

# --- 成長・長生き・法外 -------------------------------------------------------

add('outgrow', '去年の服が体に合わなくなり、そでも丈も足りない',
    '成長して合わなくなる＝outgrow。', f'''
{split()}
{person(150, 340, 0.95, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(450, 340, 1.4, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(450 250)">
  <path d="M-60-30h120v46h-120z" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="10 9"/></g>
{''.join(f'<path d="M{{}} {{}}l14 16" fill="none" stroke="{CRL}" stroke-width="4"/>'.format(390 + i * 120, 250) for i in range(2))}
{arc(250, 200, 340, 180, 46, MUTED, True, 4)}''', arrow=True)

add('outlive', '二本のろうそくのうち片方が燃え尽きても、もう一方はまだともり続ける',
    'より長生きする＝outlive。', f'''
{table(346)}
<g transform="translate(190 300)">
  <path d="M-30 0q-4-30 0-42h60q4 12 0 42z" fill="#f0e6d2" class="o"/>
  <path d="M0-42v-12" stroke="{INK}" stroke-width="3" fill="none"/>
  <path d="M0-58q14-18 0-32" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="7 7"/></g>
<g transform="translate(410 300)">
  <path d="M-30 0q-4-140 0-160h60q4 20 0 160z" fill="#f0e6d2" class="o"/>
  <path d="M0-160v-16" stroke="{INK}" stroke-width="3" fill="none"/>
  {flame(0, -170, 0.32)}</g>
{''.join(f'<path d="M{{}} 120h44" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(220 + i * 0) for i in range(1))}
{cross(190, 160, 0.5)}
{tick(500, 160, 0.6)}''', arrow=True)

add('outrageous', '値札の数字を見た人が、あまりの高さに飛び上がって驚く',
    'とんでもない、法外な＝outrageous。', f'''
{table(346)}
<g transform="translate(400 240)">
  <path d="M-110-100h220v200h-220z" class="paper"/>
  <rect x="-80" y="-40" width="160" height="34" rx="17" class="coral"/>
  {''.join(f'<rect x="-80" y="{{}}" width="{{}}" height="14" rx="7" fill="{MUTED}"/>'.format(-80, 110) for _ in range(1))}
  {''.join(f'<rect x="-80" y="{{}}" width="{{}}" height="14" rx="7" fill="{MUTED}"/>'.format(20 + i * 28, 130 - i * 40) for i in range(2))}</g>
{person(150, 340, 1.2, 1, 'teal', 'blue', 'up', 'short', 'sad')}
{''.join(f'<path d="M{{}} {{}}l16-22" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>'.format(90 + i * 24, 140 - i * 12) for i in range(3))}
{''.join(f'<path d="M{{}} {{}}l-16-22" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>'.format(230 - i * 24, 140 - i * 12) for i in range(3))}''')

add('overwhelmingly', '賛成の山が反対の山を圧倒し、比べものにならないほど高い',
    '圧倒的に＝overwhelmingly。', f'''
{bar(120, 340, [120, 10], 130, 90, 2.3, ['teal', 'coralp'])}
{''.join(f'<path d="M{{}} {{}}h100" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(110, 64) for _ in range(1))}
{tick(170, 100, 0.7)}
{cross(405, 300, 0.5)}''')

# --- 酸化・粒子 --------------------------------------------------------------

add('oxidation', '銀色だった釘が、空気にさらされて赤茶けたさびに覆われる',
    '酸化＝oxidation。', f'''
{split()}
{table(346)}
<g transform="translate(150 290) rotate(-70)">
  <path d="M-12 0h24v130l-12 24-12-24z" fill="{MUTED}" class="o"/>
  <ellipse cy="-4" rx="30" ry="11" fill="{MUTED}" class="o"/></g>
<g transform="translate(450 290) rotate(-70)">
  <path d="M-12 0h24v130l-12 24-12-24z" fill="#a2603a" class="o"/>
  <ellipse cy="-4" rx="30" ry="11" fill="#a2603a" class="o"/>
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="6" fill="#7d4527"/>'.format(-8 + (i % 2) * 12, 20 + i * 24) for i in range(4))}</g>
{arc(260, 150, 340, 150, 44, MUTED, True, 4)}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="8" fill="none" stroke="{BLU}" stroke-width="3"/>'.format(300 + (i - 1) * 40, 90) for i in range(3))}''', arrow=True)

add('particle', '大きな塊を砕いていくと、最後にはごく小さな粒だけが残る',
    '粒子＝particle。', f'''
{table(352)}
<g transform="translate(110 280)"><path d="M-70-70h140v140h-140z" fill="{STONE}" class="o"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M-26-22h52v44h-52z" fill="{STONE}" class="o"/></g>'.format(x, y, r) for x, y, r in [(270, 250, 14), (300, 310, -22), (240, 320, 30)])}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="{STONE}" class="o"/>'.format(430 + (i % 4) * 24, 280 + (i // 4) * 26, 4 + i % 3) for i in range(12))}
{arc(200, 200, 240, 200, 34, MUTED, True, 4)}
{arc(360, 200, 410, 210, 34, MUTED, True, 4)}
{ring(468, 292, 66, True)}''', arrow=True)

# --- 偽る・気を失う・給与 -----------------------------------------------------

add('pass off', 'よくできた偽物に本物のラベルを貼り、そのまま相手へ渡す',
    '(にせ物を)本物と偽る＝pass off。', f'''
{person(150, 340, 1.15, 1, 'coral', 'blue', 'give', 'short', 'flat')}
<g transform="translate(320 230)">
  <path d="M-70-80h140v160h-140z" class="goldp o"/>
  <path d="M-70-80h140v160h-140z" fill="none" class="o"/>
  <g transform="rotate(-8)"><path d="M-56-50h112v54h-112z" fill="#fffefd" class="o"/>
    <circle cx="-26" cy="-22" r="16" class="coralp o"/>
    <path d="M0-34h44v10H0zM0-16h32v10H0z" fill="{MUTED}"/></g></g>
{person(490, 340, 1.15, -1, 'teal', 'green', 'reach', 'bob', 'smile')}
{arc(400, 190, 460, 200, 40, MUTED, True, 4)}
{cross(180, 130, 0.5)}''', arrow=True)

add('pass out', '立っていた人が力を失い、その場に崩れるように倒れる',
    '気を失う＝pass out。', f'''
<g opacity="0.28">{person(150, 340, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'flat')}</g>
<g transform="translate(380 330) rotate(74)">{person(0, 0, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'sad')}</g>
{arc(220, 230, 320, 280, 50, MUTED, True, 5)}
{''.join(f'<path d="M{{}} {{}}l-10 16" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(460 + i * 22, 160 + i * 18) for i in range(3))}
{''.join(f'<path d="M{{}} 120q14 14 0 28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(500 + i * 20) for i in range(2))}''', arrow=True)

add('payroll', '名前の並んだ名簿にそって、一人ずつに給与の袋が配られる',
    '給与支払い名簿、人件費＝payroll。', f'''
<g transform="translate(180 200)">
  <path d="M-110-140h220v280h-220z" class="paper"/>
  {''.join(f'<rect x="-84" y="{{}}" width="{{}}" height="12" rx="6" fill="{MUTED}"/>'.format(-110 + i * 46, 120 - (i % 3) * 26) for i in range(5))}
  {''.join(f'<circle cx="-96" cy="{{}}" r="8" class="teal"/>'.format(-104 + i * 46) for i in range(5))}</g>
{''.join(f'<g transform="translate(430 {{}})"><path d="M-46-30h92v60h-92z" fill="#f0e6d2" class="o"/>{{}}</g>'.format(110 + i * 80, coin(0, 0, 15)) for i in range(3))}
{''.join(f'<path d="M300 {{}}h80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(110 + i * 80) for i in range(3))}''', arrow=True)

# --- 絶えず・しつこく・関係する -------------------------------------------------

add('perpetually', '水車が止まることなく回り続け、水が絶えず流れ落ちる',
    '絶えず、いつも＝perpetually。', f'''
<g transform="translate(280 220)">
  <circle r="130" fill="none" stroke="{BRN}" stroke-width="14"/>
  {''.join(f'<g transform="rotate({a})"><path d="M-18-130h36v-34h-36z" fill="#c9a464" class="o"/><path d="M0 0v-130" stroke="{BRN}" stroke-width="8" fill="none"/></g>' for a in range(0, 360, 45))}
  <circle r="18" fill="{BRN}" class="o"/></g>
<path d="M40 90h180" fill="none" stroke="{BLU}" stroke-width="18" stroke-linecap="round"/>
{''.join(drop(220 + i * 12, 110 + i * 26, 1.1, 'blue') for i in range(3))}
<path d="M280 360h280" fill="none" stroke="{BLU}" stroke-width="18" stroke-linecap="round"/>
<g transform="translate(500 140)"><path d="M-44 0a44 44 0 1 1 16 34" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="10 9" marker-end="url(#ar)"/></g>''', arrow=True)

add('persistently', '閉じた扉を、返事があるまで何度も何度もたたき続ける',
    'しつこく、粘り強く＝persistently。', f'''
<g transform="translate(410 380)">
  <path d="M-110-320h220v320h-220z" fill="#e8ddc9" class="o"/>
  <path d="M-84-296h168v276h-168z" class="teal o"/>
  <circle cx="62" cy="-160" r="10" class="goldp o"/></g>
{person(170, 350, 1.3, 1, 'coral', 'blue', 'reach', 'short', 'flat')}
<g opacity="0.3">{hand(268, 170, 1)}</g>
<g opacity="0.55">{hand(272, 220, 1)}</g>
{hand(276, 268, 1)}
{''.join(f'<path d="M{{}} {{}}q16 14 0 30" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(320 + i * 20, 150 + i * 22) for i in range(3))}''')

add('pertain', 'いくつも並ぶ札のうち、線がつながっているのは一枚だけ',
    '(pertain to で)関係する、当てはまる＝pertain。', f'''
<circle cx="130" cy="200" r="52" class="teal o"/>
{''.join(f'<rect x="380" y="{{}}" width="150" height="60" rx="8" class="{{}} o"/>'.format(60 + i * 100, c) for i, c in enumerate(['tealp', 'coral', 'tealp']))}
<path d="M182 200L380 190" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>
<g opacity="0.28">
  <path d="M182 200L380 100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
  <path d="M182 200L380 290" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g>
{cross(340, 100, 0.4)}{cross(340, 300, 0.4)}''')

# --- 悲観・段階的廃止・つなぎ合わせ ---------------------------------------------

add('pessimism', '半分入ったコップを見て、残りの半分が空だと暗い顔をする',
    '悲観、悲観主義＝pessimism。', f'''
<g transform="translate(380 230)">
  <path d="M-70 110l12-200h116l12 200z" fill="#fffefd" class="o"/>
  <path d="M-58 10h116l8 100h-132z" class="bluep"/>
  <path d="M-70 110l12-200h116l12 200z" fill="none" class="o"/>
  <path d="M-64 10h128" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"/></g>
{ring(380, 170, 80, True)}
{person(140, 350, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
{''.join(f'<path d="M{{}} {{}}q12 12 0 24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(210 + i * 18, 160 + i * 14) for i in range(2))}''')

add('phase out', '並んだ数が段を追うごとに減っていき、最後にはひとつも残らない',
    '段階的に廃止する＝phase out。', f'''
{''.join(f'<circle cx="{{}}" cy="{{}}" r="18" class="teal o"/>'.format(60 + (i % 4) * 44, 120 + (i // 4) * 46) for i in range(8))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="18" class="teal o"/>'.format(240 + (i % 2) * 44, 120 + (i // 2) * 46) for i in range(4))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="18" class="teal o"/>'.format(400, 120 + i * 46) for i in range(1))}
<g opacity="0.3"><circle cx="520" cy="120" r="18" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/></g>
{''.join(f'<path d="M{{}} 300h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(150 + i * 130) for i in range(3))}''', arrow=True)

add('piece together', '割れた器の破片を拾い集め、もとの形に組み直す',
    '継ぎ合わせて再構成する＝piece together。', f'''
{split()}
{table(352)}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="{{}}" class="bluep o"/></g>'.format(x, y, r, p) for x, y, r, p in [
  (90, 270, 16, 'M-40-24h70l6 40-66 16z'), (180, 310, -26, 'M-30-20h50l6 30-50 14z'),
  (120, 190, 34, 'M-26-18h44l4 26-42 12z'), (210, 230, -12, 'M-22-16h38l4 24-38 10z')])}
<g transform="translate(440 280)">
  <path d="M-90-40q90-30 180 0-10 80-90 80t-90-80z" class="bluep o"/>
  <path d="M-40-48v110M40-52v112M-90-14h180" fill="none" stroke="{BLU}" stroke-width="3" stroke-dasharray="8 7"/></g>
{arc(260, 190, 340, 200, 44, MUTED, True, 4)}''', arrow=True)

# --- はっきり・厚板・軽く見せる -------------------------------------------------

add('plainly', 'ぼやけた印の隣に、輪郭のはっきりした同じ印が置かれている',
    'はっきりと／飾らずに＝plainly。', f'''
{split()}
<g opacity="0.3"><circle cx="150" cy="200" r="80" class="teal"/>
  <circle cx="150" cy="200" r="94" class="teal" opacity="0.3"/>
  <circle cx="150" cy="200" r="108" class="teal" opacity="0.2"/></g>
<circle cx="450" cy="200" r="80" class="teal o"/>
{cross(150, 340, 0.5)}
{tick(450, 340, 0.6)}''')

add('plank', '厚みのある一枚の板が、木目を見せて横たわる',
    '厚板、(政策の)柱＝plank。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-230-40h460v54h-460z" fill="#c9a464" class="o"/>
  <path d="M-230 14h460v26h-460z" fill="#a0764a" class="o"/>
  {''.join(f'<path d="M{{}} -30q40 14 0 34" fill="none" stroke="#a0764a" stroke-width="3"/>'.format(-190 + i * 90) for i in range(5))}</g>''')

add('play down', '大きかった問題を、手ぶりで小さなものに見せかける',
    '(重要性を)軽く見せる、過小に扱う＝play down。', f'''
<g opacity="0.3"><circle cx="300" cy="180" r="120" class="coral"/></g>
<circle cx="300" cy="200" r="40" class="coral o"/>
{hand(150, 200, 1)}
{hand(450, 200, -1)}
{''.join(f'<path d="M{{}} 200h{{}}" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(x, d) for x, d in [(200, 40), (400, -40)])}
{person(90, 350, 0.9, 1, 'teal', 'blue', 'stand', 'short', 'smile')}''', arrow=True)

add('pointless', '底に穴の開いたバケツへ、いくら水を注いでも溜まらない',
    '無意味な、むだな＝pointless。', f'''
{bucket(300, 230, 1.2, True)}
<g transform="translate(200 90) rotate(40)">
  <path d="M-30-50h60v90a22 22 0 0 1-22 22h-16a22 22 0 0 1-22-22z" class="bluep o"/></g>
{''.join(drop(270 + i * 10, 110 + i * 22, 1.0, 'blue') for i in range(3))}
{''.join(drop(324, 310 + i * 26, 1.0, 'blue') for i in range(2))}
{cross(490, 150, 0.7)}''')

# --- 両極・独占欲 ------------------------------------------------------------

add('polarity', '磁石の両端が、それぞれ反対の性質を持って引きも反発もする',
    '両極性、対立＝polarity。', f'''
<g transform="translate(300 200)">
  <path d="M-160-60h140v120h-140z" class="coral o"/>
  <path d="M20-60h140v120H20z" class="blue o"/></g>
{''.join(f'<path d="M{{}} {{}}q30-40 60 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>'.format(140 + i * 80, 110 - i * 0) for i in range(1))}
<path d="M120 320h120M180 260v120" fill="none" stroke="{CRL}" stroke-width="10" stroke-linecap="round"/>
<path d="M360 320h120" fill="none" stroke="{BLU}" stroke-width="10" stroke-linecap="round"/>''')

add('possessive', '自分のものを腕の中に抱えこみ、差し出された手に渡そうとしない',
    '独占欲の強い＝possessive。', f'''
<g transform="translate(230 330)">
  <path d="M-80 0v-140q80-34 160 0V0z" class="coral o"/>
  <path d="M-80-140q-20 60 50 74 60 12 110-14" fill="none" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>
  <circle cx="0" cy="-186" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-34-194q4-38 34-38 28 0 34 36-18-16-34-6-16-10-34 8z" fill="{HAIR}"/>
  <circle cx="-11" cy="-188" r="3" class="ink"/><circle cx="11" cy="-188" r="3" class="ink"/>
  <path d="M-10-172q10-8 20 0" fill="none" stroke="{INK}" stroke-width="2.4"/>
  <rect x="-44" y="-120" width="88" height="64" rx="8" class="gold o"/></g>
{hand(470, 250, -1)}
{cross(470, 130, 0.6)}''')

finish(__file__)
