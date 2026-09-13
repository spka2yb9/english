# -*- coding: utf-8 -*-
"""第174回。p-/q-/r- の中盤。narrowly の描き直しも含む。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def flag(x, y, s=1, cls='violet', pole=110):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-{pole}" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>'
            f'<path d="M5-{pole}h100l-24 30 24 30H5z" class="{cls} o"/></g>')

def crown(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-70 30l-14-70 44 30 40-48 40 48 44-30-14 70z" class="gold o"/>'
            f'<path d="M-70 30h140v18h-140z" class="goldd o"/></g>')

def star(x, y, s=1, cls='gold'):
    pts = []
    for i in range(10):
        a = math.radians(-90 + i * 36)
        r = 46 * s if i % 2 == 0 else 19 * s
        pts.append(f'{x + r*math.cos(a):.1f} {y + r*math.sin(a):.1f}')
    return f'<path d="M{"L".join(pts)}z" class="{cls} o"/>'

# --- 第173回の描き直し -------------------------------------------------------

add('narrowly', 'ゴールの線で二人が並び、先着はほんのわずかな差だった',
    'かろうじて、僅差で＝narrowly。', f'''
<path d="M300 40v320" fill="none" stroke="{INK}" stroke-width="6"/>
{''.join(f'<rect x="{282+(i%2)*18}" y="{50+i*22}" width="18" height="22" fill="{INK}"/>' for i in range(14))}
{person(280, 350, 1.25, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{person(180, 350, 1.25, 1, 'coral', 'green', 'walk', 'bob', 'sad')}
<path d="M198 110h84" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
{ring(240, 110, 26, True)}
{tick(460, 200, 0.8)}''', arrow=True)

# --- 姿勢・前提 --------------------------------------------------------------

add('posture', '背筋を伸ばして立つ姿と、背中の丸まった姿を並べて比べる',
    '姿勢／(政治的な)構え＝posture。', f'''
{split()}
{person(150, 350, 1.4, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<path d="M150 200v-100" fill="none" stroke="{GRN}" stroke-width="5" stroke-dasharray="10 9"/>
{tick(150, 80, 0.6)}
<g transform="translate(450 350)">
  <path d="M-14-8l-7 8M14-8l7 8" fill="none" stroke="{BLUD}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-34-104q40-30 70-6l-8 102h-56z" fill="{TEA}" class="o" transform="rotate(12 0 -60)"/>
  <circle cx="24" cy="-136" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-8-142q4-34 32-34t32 32q-16-14-32-6-16-8-32 8z" fill="{HAIR}"/>
  <circle cx="16" cy="-134" r="3" class="ink"/><circle cx="34" cy="-134" r="3" class="ink"/>
  <path d="M18-120q10 6 18 0" fill="none" stroke="{INK}" stroke-width="2.2"/></g>
<path d="M450 220q20-60 0-110" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="10 9"/>
{cross(450, 80, 0.5)}''')

add('precondition', '扉の手前に一つの関門があり、そこを越えないと先へ進めない',
    '前提条件＝precondition。', f'''
<g transform="translate(490 380)">
  <path d="M-80-140h160v140h-160z" fill="#e8ddc9" class="o"/>
  <path d="M-58-122h116v122h-116z" class="teal o"/>
  <circle cx="40" cy="-58" r="9" class="goldp o"/></g>
<g transform="translate(300 306)">
  <path d="M-16 0v-120h16v120z" fill="{MUTED}"/>
  <path d="M0-110h150v24H0z" class="coral o"/>
  {''.join(f'<path d="M{20+i*40} -110v24" stroke="#fffefd" stroke-width="10" fill="none"/>' for i in range(3))}</g>
{person(120, 350, 1.15, 1, 'teal', 'blue', 'walk', 'short', 'flat')}
{line(180, 240, 260, 240, MUTED, True, 5)}
<g transform="translate(300 160)">{tick(0, 0, 0.5)}</g>''', arrow=True)

add('prerequisite', '番号の順に箱を通らないと、最後の箱にはたどり着けない',
    '前提条件、必須の要件＝prerequisite。', f'''
{''.join(f'<g transform="translate({{}} 200)"><rect x="-56" y="-50" width="112" height="100" rx="10" class="{{}} o"/></g>'.format(100 + i * 140, c) for i, c in enumerate(['tealp', 'tealp', 'teal']))}
{''.join(f'<circle cx="{{}}" cy="120" r="20" class="gold o"/>'.format(100 + i * 140) for i in range(3))}
{''.join(f'<path d="M{{}} 200h56" fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"/>'.format(162 + i * 140) for i in range(2))}
<g transform="translate(510 200)"><rect x="-40" y="-50" width="80" height="100" rx="10" class="coral o"/></g>
{''.join(f'<circle cx="{{}}" cy="284" r="{{}}" class="{{}}"/>'.format(100 + i * 140, 8, 'ink') for i in range(0))}''', arrow=True)

# --- 押し進める・民営化・収益 ---------------------------------------------------

add('press ahead', '向かい風を受けながらも、体を前に倒して先へ進み続ける',
    '押し進める、強行する＝press ahead。', f'''
{''.join(f'<path d="M560 {{}}q-90-26-180 0t-180 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>'.format(80 + i * 50) for i in range(5))}
<g transform="translate(300 350) rotate(-16)">{person(0, 0, 1.4, 1, 'teal', 'blue', 'walk', 'short', 'flat')}</g>
{''.join(f'<path d="M{{}} {{}}l-40 8" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(540, 160 + i * 70) for i in range(2))}
{arc(340, 260, 470, 250, 50, GRN, True, 5)}''', arrow=True)

add('privatisation', '国の旗が立っていた建物に、会社の旗が掲げ直される',
    '民営化＝privatisation。', f'''
{split()}
{building(150, 330, 0.9, 'teal')}
{flag(150, 190, 0.6, 'coral', 120)}
{building(450, 330, 0.9, 'teal')}
{flag(450, 190, 0.6, 'violet', 120)}
{arc(260, 150, 340, 150, 44, MUTED, True, 5)}''', arrow=True)

add('profitability', '売上の柱から費用の分を差し引くと、大きな残りが手元に残る',
    '収益性＝profitability。', f'''
<path d="M60 344h460" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<rect x="100" y="80" width="120" height="264" rx="8" class="tealp o"/>
<rect x="100" y="230" width="120" height="114" rx="8" class="coralp o"/>
{arc(260, 160, 340, 170, 50, MUTED, True, 5)}
<rect x="390" y="80" width="120" height="150" rx="8" class="teal o"/>
{''.join(coin(450, 300 - i * 30, 20) for i in range(2))}
<path d="M80 80h40M80 230h40" fill="none" stroke="{MUTED}" stroke-width="3"/>''', arrow=True)

# --- すぐに・比例して・扶養 -----------------------------------------------------

add('promptly', '合図のベルが鳴ったその場ですぐに手が挙がる',
    'すぐに、きっかり＝promptly。', f'''
<g transform="translate(160 170)">
  <path d="M-70 60q0-110 70-110t70 110z" class="gold o"/>
  <path d="M-84 60h168v20h-168z" class="goldd o"/>
  <path d="M0-50v-24" stroke="{INK}" stroke-width="6" fill="none"/>
  <circle cy="92" r="14" class="goldd o"/></g>
{''.join(f'<path d="M{{}} {{}}q22-20 0-40" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(270 + i * 22, 190 - i * 14) for i in range(2))}
{person(430, 350, 1.3, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{clock(530, 110, 40, 12, 0)}''')

add('proportionally', '大きな円には大きな取り分、小さな円には小さな取り分が対応する',
    '比例して、割合に応じて＝proportionally。', f'''
{''.join(f'<circle cx="{{}}" cy="130" r="{{}}" class="teal o"/>'.format(110 + i * 160, 26 + i * 26) for i in range(3))}
{''.join(f'<rect x="{{}}" y="{{}}" width="70" height="{{}}" rx="8" class="coral o"/>'.format(75 + i * 160, 330 - (30 + i * 40), 30 + i * 40) for i in range(3))}
{''.join(f'<path d="M{{}} {{}}v{{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(110 + i * 160, 160 + i * 26, 70 - i * 26) for i in range(3))}
<path d="M40 336h500" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>''')

add('provide for', '食卓に人数分の食事を並べ、家族の暮らしを支える',
    '扶養する、(法が)定める＝provide for。', f'''
{table(290)}
{''.join(f'<g transform="translate({{}} 282)"><ellipse rx="46" ry="14" fill="#fffefd" class="o"/><ellipse rx="24" ry="7" class="goldp"/></g>'.format(140 + i * 110) for i in range(3))}
{''.join(head(140 + i * 110, 190, 26, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('coral', 'bob'), ('green', 'bun')]))}
{person(480, 340, 1.15, -1, 'violet', 'blue', 'carry', 'cap', 'smile')}
<g transform="translate(430 250)"><path d="M-34-18h68l-8 40h-52z" class="goldp o"/></g>''')

add('provided that', '分かれ道の一方に条件の札が下がり、それを満たせばそちらへ進める',
    '〜という条件で、もし〜なら＝provided that。', f'''
<path d="M300 400L250 220h100z" fill="#d8cdb6"/>
<path d="M250 220L120 80h60L300 210z" fill="#d8cdb6"/>
<path d="M250 220L470 90h60L300 212z" fill="#d8cdb6"/>
<g transform="translate(440 200) rotate(-6)">
  <path d="M-80-44h160v88h-160z" class="paper"/>
  {''.join(f'<rect x="-58" y="{{}}" width="{{}}" height="10" rx="5" fill="{MUTED}"/>'.format(-26 + i * 26, 116 - i * 40) for i in range(2))}
  {tick(50, 0, 0.36)}</g>
{person(300, 380, 0.9, 1, 'teal', 'blue', 'point', 'short', 'smile')}
{arc(330, 290, 420, 250, 50, MUTED, True, 4)}''', arrow=True)

# --- 挑発・やってのける・切り抜ける ---------------------------------------------

add('provocative', '目の前で赤い布をひらひらさせ、相手をわざと怒らせようとする',
    '挑発的な、議論を呼ぶ＝provocative。', f'''
{person(150, 350, 1.2, 1, 'teal', 'blue', 'give', 'short', 'smile')}
<g transform="translate(300 210) rotate(-12)">
  <path d="M-70-60h140q10 70-20 120h-100q-30-50-20-120z" class="coral o"/>
  <path d="M-70-60h140" fill="none" stroke="{CRLD}" stroke-width="4"/></g>
{beast(490, 340, 0.5, '#6b5a4a', -1)}
{''.join(f'<path d="M{{}} {{}}q14 12 0 24" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(430 + i * 18, 150 + i * 16) for i in range(3))}''')

add('pull off', 'ぐらつく綱の上を最後まで渡りきり、向こう岸へたどり着く',
    '(難しいことを)やってのける＝pull off。', f'''
<g transform="translate(300 250)">
  <path d="M-260 0h520" fill="none" stroke="{BRN}" stroke-width="7"/>
  <path d="M-260 0v-70M260 0v-70" fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round"/></g>
{person(430, 250, 1.1, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<g opacity="0.28">{person(180, 250, 1.0, 1, 'teal', 'blue', 'up', 'short', 'flat')}</g>
{arc(220, 170, 400, 160, 50, MUTED, True, 4)}
{tick(520, 120, 0.8)}
<path d="M0 360h600" fill="none" stroke="{MUTED}" stroke-width="0"/>''', arrow=True)

add('pull through', '寝ついていた人が体を起こし、ふたたび自分の足で立つ',
    '(重病・危機を)切り抜ける＝pull through。', f'''
{split()}
<g transform="translate(150 300)">
  <path d="M-110 0v-60h220v60z" fill="#fffefd" class="o"/>
  <path d="M-110-60h50v-40h-50z" class="bluep o"/>
  <path d="M-60-48q60-20 170 0v-12H-60z" class="blue o"/>
  {head(-84, -76, 20, 'blue', 'short', 'sad')}</g>
{person(450, 350, 1.25, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{arc(250, 200, 350, 200, 46, MUTED, True, 5)}
{''.join(spark(500 + i * 0, 110 + i * 40, 0.7, 'gold') for i in range(2))}''', arrow=True)

# --- 句読点・浄化 ------------------------------------------------------------

add('punctuation', '並んだ語の列の切れ目に、点と丸の記号が置かれる',
    '句読点、句読法＝punctuation。', f'''
{''.join(f'<rect x="{{}}" y="110" width="{{}}" height="26" rx="13" fill="{INK}"/>'.format(60 + i * 100, 70 - (i % 2) * 16) for i in range(3))}
<circle cx="330" cy="130" r="11" class="coral"/>
{''.join(f'<rect x="{{}}" y="110" width="{{}}" height="26" rx="13" fill="{INK}"/>'.format(370 + i * 100, 70 - (i % 2) * 16) for i in range(2))}
<g transform="translate(535 130)"><circle r="11" class="coral"/><path d="M0 11q-8 14-16 18" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/></g>
{''.join(f'<rect x="{{}}" y="250" width="{{}}" height="26" rx="13" fill="{INK}"/>'.format(60 + i * 100, 70 - (i % 2) * 16) for i in range(4))}
<g transform="translate(470 250)"><circle r="11" class="coral"/><circle cy="40" r="11" class="coral"/></g>
{ring(330, 130, 30, True)}{ring(535, 136, 34, True)}{ring(470, 270, 34, True)}''')

add('purification', '濁った水がろ過の層を通り、下では澄んだ水になって出てくる',
    '浄化、精製＝purification。', f'''
<g transform="translate(300 110)">
  <path d="M-90-60h180v90h-180z" fill="#b0a48f" class="o"/></g>
<g transform="translate(300 220)">
  <path d="M-110-60h220v120h-220z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M-110 {{}}h220" fill="none" stroke="{MUTED}" stroke-width="8"/>'.format(-30 + i * 30) for i in range(3))}
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="6" fill="{STONE}"/>'.format(-92 + (i % 8) * 26, -44 + (i // 8) * 62) for i in range(16))}</g>
<g transform="translate(300 340)">
  <path d="M-90-40h180v70h-180z" class="bluep o"/></g>
{''.join(drop(300, 176 + i * 0, 1.0, 'blue') for i in range(1))}
{line(300, 292, 300, 310, MUTED, True, 4)}
{tick(500, 330, 0.6)}
{cross(500, 90, 0.5)}''', arrow=True)

add('purify', '濁った水を布で丁寧にこし、澄んだ水だけを別の器に移す',
    '浄化する、精製する＝purify。', f'''
{table(352)}
<g transform="translate(200 140) rotate(26)">
  <path d="M-40-70h80v100a30 30 0 0 1-60 0z" fill="#fffefd" class="o"/>
  <path d="M-40-10h80v30a30 30 0 0 1-60 0z" fill="#b0a48f"/></g>
<g transform="translate(330 220)">
  <path d="M-90-20h180l-70 60h-40z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{{}} -20v34" stroke="{MUTED}" stroke-width="3" fill="none"/>'.format(-60 + i * 40) for i in range(4))}</g>
<g transform="translate(330 310)">
  <path d="M-60-40h120v50a20 20 0 0 1-20 20h-80a20 20 0 0 1-20-20z" fill="#fffefd" class="o"/>
  <path d="M-60-10h120v20a20 20 0 0 1-20 20h-80a20 20 0 0 1-20-20z" class="bluep"/></g>
{''.join(drop(330, 264 + i * 0, 1.0, 'blue') for i in range(1))}
{tick(500, 180, 0.7)}''')

add('purposely', 'ぶつかったわけではなく、指でわざとコップを押して倒す',
    'わざと、故意に＝purposely。', f'''
{table(330)}
<g transform="translate(360 300) rotate(78)">
  <path d="M-44 0l10-110h68l10 110z" fill="#fffefd" class="o"/></g>
{''.join(drop(430 + i * 22, 290 + (i % 2) * 16, 1.0, 'blue') for i in range(3))}
{hand(180, 230, 1)}
{line(230, 240, 290, 260, CRL, False, 5)}
{person(90, 350, 1.0, 1, 'coral', 'blue', 'point', 'short', 'smile')}
<g opacity="0.28"><path d="M300 300l10-110h68l10 110z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g>''', arrow=True)

# --- 伝える・提案する・静か -----------------------------------------------------

add('put across', '図を指して説明すると、相手の頭の中にその形がそのまま浮かぶ',
    '(考えを)分かるように伝える＝put across。', f'''
{person(120, 350, 1.15, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<g transform="translate(280 210)">
  <path d="M-80-80h160v160h-160z" class="paper"/>
  <path d="M-46 46l46-76 46 76z" class="coral o"/></g>
<g transform="translate(470 160)">
  <path d="M-70-60h140v120h-140z" fill="#fffefd" class="o"/>
  <path d="M-40 34l40-66 40 66z" class="coral o"/></g>
{head(470, 320, 30, 'green', 'bob')}
<circle cx="470" cy="250" r="12" fill="#fffefd" class="o"/>
{arc(370, 170, 390, 170, 34, MUTED, True, 4)}''', arrow=True)

add('put forward', 'まとめた案の紙を、テーブルの向こうへすっと押し出す',
    '(案を)提出する、提案する＝put forward。', f'''
{table(300)}
{person(120, 350, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
<g opacity="0.28">{doc(230, 250, 90, 60, 2)}</g>
{doc(340, 250, 96, 66, 2)}
{arc(250, 210, 330, 210, 44, MUTED, True, 5)}
{''.join(head(470 + i * 0, 200, 28, 'coral', 'bob') for i in range(1))}''', arrow=True)

add('quiet', '物音ひとつしない部屋で、口もとに指を当てて静けさを示す',
    '静かな、おとなしい／静けさ＝quiet。', f'''
<g transform="translate(300 200)">
  <path d="M-240-160h480v320h-480z" fill="#f2f4f1" class="o"/></g>
{person(300, 340, 1.3, 1, 'teal', 'blue', 'think', 'short', 'flat')}
<path d="M300 232v-16" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
{''.join(f'<g transform="translate({{}} {{}})"><path d="M-28 0q28-26 56 0" fill="none" stroke="{MUTED}" stroke-width="5"/></g>'.format(x, y) for x, y in [(110, 120), (490, 120)])}
{''.join(cross(x, 120, 0.4) for x in (110, 490))}''')

# --- 波及・信頼関係・発疹 -------------------------------------------------------

add('ramification', '一つの出来事から枝が分かれ、その先でさらに何本にも分かれていく',
    '(複雑な)波及効果、影響＝ramification。', f'''
<circle cx="80" cy="200" r="40" class="coral o"/>
{''.join(f'<path d="M120 200L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="5"/>'.format(250, 110 + i * 90) for i in range(3))}
{''.join(f'<circle cx="270" cy="{{}}" r="24" class="teal o"/>'.format(110 + i * 90) for i in range(3))}
{''.join(f'<path d="M294 {{}}L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(110 + i * 90, 420, 60 + i * 90 + j * 46) for i in range(3) for j in range(2))}
{''.join(f'<circle cx="436" cy="{{}}" r="16" class="tealp o"/>'.format(60 + i * 90 + j * 46) for i in range(3) for j in range(2))}''')

add('rapport', '打ち解けた二人の間に、暖かい色の橋がかかる',
    '打ち解けた関係、信頼関係＝rapport。', f'''
{person(130, 340, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(470, 340, 1.2, -1, 'coral', 'green', 'stand', 'bob', 'smile')}
<g transform="translate(300 230)">
  <path d="M-140 40q140-120 280 0" fill="none" stroke="{GLD}" stroke-width="16" stroke-linecap="round"/>
  {''.join(f'<path d="M{{}} {{}}v34" stroke="{GLDD}" stroke-width="7" fill="none" stroke-linecap="round"/>'.format(-100 + i * 50, 6 + abs(i - 2) * 8) for i in range(5))}</g>
<g transform="translate(300 110)">
  <path d="M0 26q-34-26-34-48 0-18 18-18 10 0 16 12 6-12 16-12 18 0 18 18 0 22-34 48z" class="coralp o"/></g>''')

add('rash', 'うでの一面に、赤い小さな粒が広がって出ている',
    '発疹、湿疹／軽率な＝rash。', f'''
<g transform="translate(280 220)">
  <path d="M-190 80q40-130 160-150 120-20 190 40" fill="none" stroke="{SKIN}" stroke-width="76" stroke-linecap="round"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" class="coral o"/>'.format(150 + (i % 6) * 44 + (i // 6) * 18, 180 + (i // 6) * 34 - (i % 6) * 12, 7 + (i % 3)) for i in range(18))}
<g transform="translate(90 120)">
  <circle r="44" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M32 32l36 36" stroke="{BRN}" stroke-width="14" stroke-linecap="round" fill="none"/></g>''')

# --- 視聴率・根拠・行間 -------------------------------------------------------

add('ratings', '番組の人気を示す数字が折れ線で上がり、星の数で評価される',
    '視聴率、評価＝ratings。', f'''
<g transform="translate(230 200)">
  <path d="M-170-130h340v260h-340z" fill="#fffefd" class="o"/>
  <path d="M-170-130h340v34h-340z" class="teal o"/>
  <path d="M-140 80L-60 20 20 50 100-40 150-70" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M-140 100h300M-140 100v-160" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
{''.join(star(490, 90 + i * 74, 0.62, 'gold' if i < 3 else 'goldp') for i in range(4))}''')

add('rationale', '結論の板を、その下に立つ何本もの柱が理屈で支えている',
    '根拠、論理的な理由づけ＝rationale。', f'''
<g transform="translate(300 130)">
  <path d="M-180-60h360v80h-360z" class="teal o"/></g>
{''.join(f'<path d="M{{}} 150v170h50V150z" fill="{STONE}" class="o"/>'.format(120 + i * 120) for i in range(3))}
{''.join(f'<path d="M{{}} 330h80" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>'.format(105 + i * 120) for i in range(3))}
{''.join(f'<path d="M{{}} 200v60" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}
{''.join(tick(145 + i * 120, 250, 0.4) for i in range(3))}''')

add('read between the lines', '文の行と行のあいだに、うっすらと別の意味が浮かんで見える',
    '行間を読む、言外の意味を察する＝read between the lines。', f'''
<g transform="translate(290 200)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  {''.join(f'<rect x="-170" y="{{}}" width="{{}}" height="14" rx="7" fill="{INK}"/>'.format(-110 + i * 56, 340 - (i % 3) * 70) for i in range(5))}
  {''.join(f'<rect x="-150" y="{{}}" width="{{}}" height="10" rx="5" fill="{VIO}" opacity="0.42"/>'.format(-82 + i * 56, 240 - (i % 2) * 60) for i in range(4))}</g>
<g transform="translate(520 120)">
  <path d="M-46 0q46-34 92 0-46 34-92 0z" fill="#fffefd" class="o"/>
  <circle r="16" class="ink"/></g>
{line(500, 160, 430, 210, MUTED, True, 4)}''', arrow=True)

# --- 反論・すらすら・参照 -----------------------------------------------------

add('rebut', '相手が出した札に対して、すぐ自分の札を返して言い返す',
    '反論する、言い返す＝rebut。', f'''
{person(120, 350, 1.15, 1, 'coral', 'blue', 'give', 'short', 'flat')}
{person(490, 350, 1.15, -1, 'teal', 'green', 'give', 'bob', 'flat')}
<g transform="translate(230 190)"><rect x="-46" y="-36" width="92" height="72" rx="8" class="coral o"/></g>
<g transform="translate(390 250)"><rect x="-46" y="-36" width="92" height="72" rx="8" class="teal o"/></g>
{arc(270, 160, 350, 170, 46, CRL, True, 5)}
{arc(350, 300, 270, 290, -46, TEA, True, 5)}''', arrow=True)

add('reel off', '巻いてあった紙をひと息に繰り出し、長々と並べていく',
    'すらすら並べ立てる＝reel off。', f'''
{person(120, 350, 1.2, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(200 230)">
  <circle r="40" fill="#f0e6d2" class="o"/><circle r="12" class="ink"/></g>
<g transform="translate(390 250)">
  <path d="M-150-40h300v90h-300z" class="paper"/>
  {''.join(f'<rect x="-126" y="{{}}" width="{{}}" height="10" rx="5" fill="{MUTED}"/>'.format(-24 + i * 26, 250 - i * 40) for i in range(3))}
  <path d="M150-40a14 45 0 0 1 0 90" fill="#f7f2e8" class="o"/></g>
{arc(240, 180, 420, 180, 50, MUTED, True, 5)}''', arrow=True)

add('refer to', '本のページを開いて、そこに書かれた一行を指し示す',
    '言及する、参照する＝refer to。', f'''
{table(346)}
{book(300, 240, 1.3, 'teal')}
<g transform="translate(340 236)"><rect x="-46" y="-8" width="92" height="16" rx="8" class="coral"/></g>
{hand(430, 300, -1)}
{line(420, 270, 390, 240, MUTED, True, 4)}
{person(110, 350, 1.0, 1, 'teal', 'blue', 'point', 'short', 'smile')}''', arrow=True)

add('refute', '相手の主張の板を、確かな証拠の書類で突き崩して×にする',
    '論破する、誤りだと示す＝refute。', f'''
<g transform="translate(200 200) rotate(-14)">
  <path d="M-110-80h220v160h-220z" class="coralp o"/>
  {''.join(f'<rect x="-84" y="{{}}" width="{{}}" height="12" rx="6" fill="{CRL}"/>'.format(-46 + i * 34, 168 - (i % 2) * 50) for i in range(3))}</g>
{cross(200, 200, 1.2)}
{doc(450, 210, 150, 190, 4)}
{arc(380, 190, 300, 190, 50, TEA, True, 6)}
{tick(450, 350, 0.6)}''', arrow=True)

# --- 補強・関係・再生可能 -----------------------------------------------------

add('reinforcement', 'たわんだ棚の下に新しい支柱を足して、しっかり持ちこたえさせる',
    '補強、強化＝reinforcement。', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-110-20q110 50 220 0v24q-110 50-220 0z" fill="#c9a464" class="o"/>
  <path d="M-110 4v130M110 4v130" stroke="{BRN}" stroke-width="14" fill="none" stroke-linecap="round"/></g>
<g transform="translate(450 200)">
  <path d="M-110-20h220v24h-220z" fill="#c9a464" class="o"/>
  <path d="M-110 4v130M110 4v130M0 4v130" stroke="{BRN}" stroke-width="14" fill="none" stroke-linecap="round"/>
  <path d="M-90 40L-10 100M90 40L10 100" stroke="{BRN}" stroke-width="9" fill="none" stroke-linecap="round"/></g>
{arc(260, 150, 340, 150, 44, MUTED, True, 4)}
{tick(450, 360, 0.6)}''', arrow=True)

add('relate to', '別々に見えた二つの丸が、一本の線でつながっていると分かる',
    '関係がある、共感できる＝relate to。', f'''
<circle cx="160" cy="200" r="70" class="teal o"/>
<circle cx="440" cy="200" r="70" class="coral o"/>
<path d="M230 200h140" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
{''.join(f'<path d="M{{}} {{}}q14-16 0-32" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(290 + i * 20, 150 - i * 0) for i in range(2))}
{head(160, 330, 26, 'teal', 'short')}
{head(440, 330, 26, 'coral', 'bob')}''')

add('relevant to', '中心の題に近い札だけが手もとに残り、関係のない札は外に置かれる',
    '〜に関係のある＝relevant to。', f'''
<circle cx="300" cy="200" r="66" class="teal o"/>
{ring(300, 200, 130, True)}
{''.join(f'<rect x="{{}}" y="{{}}" width="60" height="40" rx="6" class="tealp o"/>'.format(x, y) for x, y in [(230, 60), (360, 90), (370, 260), (210, 280)])}
{''.join(f'<g opacity="0.32"><rect x="{{}}" y="{{}}" width="60" height="40" rx="6" fill="{MUTED}"/></g>'.format(x, y) for x, y in [(40, 90), (510, 60), (40, 300), (510, 300)])}
{''.join(cross(70 + i * 470, 200, 0.4) for i in range(2))}''')

add('renewable', '太陽と風で回る発電が、使っても尽きずにまた元へ戻る',
    '再生可能な＝renewable。', f'''
{sun(120, 110, 44)}
<g transform="translate(430 306)">
  <path d="M-10 0v-170h20V0z" fill="#fffefd" class="o"/>
  {''.join(f'<g transform="translate(0 -170) rotate({{}})"><path d="M0-10l-120-14 120 34z" class="tealp o"/></g>'.format(a) for a in (0, 120, 240))}
  <circle cy="-170" r="12" class="ink"/></g>
<g transform="translate(180 280)">
  <path d="M-60-40h120v70h-120z" class="bluep o"/>
  {''.join(f'<path d="M{{}} -40v70" stroke="{BLU}" stroke-width="3" fill="none"/>'.format(-36 + i * 24) for i in range(4))}</g>
<g transform="translate(300 170)">
  <path d="M-90 0a90 90 0 1 0 34-70" fill="none" stroke="{GRN}" stroke-width="8" stroke-dasharray="0" marker-end="url(#ar)"/></g>''', arrow=True)

# --- 放棄・余波・訴える -------------------------------------------------------

add('renounce', '身につけていた冠を自分から外し、台の上に置いて立ち去る',
    '(権利・信条を)公に捨てる＝renounce。', f'''
<g transform="translate(400 300)"><path d="M-90 0v-40h180v40z" fill="{STONE}" class="o"/></g>
{crown(400, 230, 0.7)}
{person(150, 350, 1.25, -1, 'teal', 'blue', 'walk', 'short', 'flat')}
{arc(330, 190, 220, 210, 60, MUTED, True, 5)}
<g opacity="0.3">{crown(220, 180, 0.55)}</g>''', arrow=True)

add('repercussion', '落とした石の波紋が遠くまで届き、岸の舟まで揺らす',
    '(思わぬ)影響、余波＝repercussion。', f'''
<path d="M0 180h600v220H0z" class="bluep"/>
{''.join(f'<ellipse cx="150" cy="290" rx="{{}}" ry="{{}}" fill="none" stroke="{BLU}" stroke-width="{{}}"/>'.format(50 + i * 70, 16 + i * 22, 5 - i * 0.6) for i in range(5))}
<circle cx="150" cy="290" r="15" fill="{STONE}" class="o"/>
{line(150, 60, 150, 240, MUTED, True, 4)}
<g transform="translate(490 270) rotate(10)">
  <path d="M-70 0h140l-24 36h-92z" class="coral o"/>
  <path d="M-10 0v-70h60l-52 24" fill="{GLDP}" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q10 12 0 24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(540 + i * 16, 180 - i * 12) for i in range(2))}''', arrow=True)

add('resort to', 'いつもの扉が閉ざされ、やむなく非常用のハンドルに手をかける',
    '(やむなく)〜に訴える＝resort to。', f'''
{split()}
<g transform="translate(150 250)">
  <path d="M-70-130h140v190h-140z" class="teal o"/>
  <circle cx="44" cy="0" r="9" class="goldp o"/></g>
{cross(150, 170, 0.8)}
<g transform="translate(450 220)">
  <path d="M-80-90h160v180h-160z" class="coralp o"/>
  <path d="M-56-66h112v132h-112z" fill="#fffefd" class="o"/>
  <path d="M-30 0h60v20h-60z" class="coral o"/>
  <path d="M0 20v40" stroke="{CRLD}" stroke-width="10" fill="none"/></g>
{hand(450, 330, 1)}
{arc(250, 140, 380, 150, 50, MUTED, True, 5)}''', arrow=True)

# --- 再編・原因と結果 ---------------------------------------------------------

add('restructure', '組織図の箱を外して並べ替え、つながり方をつくり直す',
    '再編する、組織を作り直す＝restructure。', f'''
{split()}
<g transform="translate(150 190)">
  <rect x="-40" y="-110" width="80" height="46" rx="6" class="teal o"/>
  <path d="M0-64v30M-70-34h140M-70-34v30M70-34v30" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <rect x="-110" y="-4" width="80" height="46" rx="6" class="tealp o"/>
  <rect x="30" y="-4" width="80" height="46" rx="6" class="tealp o"/>
  <rect x="-40" y="66" width="80" height="46" rx="6" class="tealp o"/>
  <path d="M-70 42v24h70" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
<g transform="translate(450 190)">
  <rect x="-40" y="-110" width="80" height="46" rx="6" class="teal o"/>
  <path d="M0-64v40M-110-24h220M-110-24v30M0-24v30M110-24v30" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <rect x="-150" y="6" width="80" height="46" rx="6" class="coralp o"/>
  <rect x="-40" y="6" width="80" height="46" rx="6" class="coralp o"/>
  <rect x="70" y="6" width="80" height="46" rx="6" class="coralp o"/></g>
{arc(260, 110, 340, 110, 44, MUTED, True, 5)}''', arrow=True)

add('result from', '目の前の結果から線をたどっていくと、その手前にある原因に行き着く',
    '〜が原因で生じる＝result from。', f'''
<circle cx="470" cy="200" r="66" class="coral o"/>
<circle cx="130" cy="200" r="50" class="teal o"/>
<path d="M400 200H196" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round" marker-end="url(#ar)"/>
{''.join(f'<path d="M{{}} 330h60" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}
<g transform="translate(130 330)"><path d="M-46-14h92v28h-92z" class="tealp o"/></g>
<g transform="translate(470 330)"><path d="M-56-14h112v28h-112z" class="coralp o"/></g>''', arrow=True)

add('result in', '原因から線をたどると、その先に生まれた結果へ行き着く',
    '結果として〜をもたらす＝result in。', f'''
<circle cx="130" cy="200" r="50" class="teal o"/>
<circle cx="470" cy="200" r="66" class="coral o"/>
<path d="M196 200h204" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round" marker-end="url(#ar)"/>
<g transform="translate(130 330)"><path d="M-46-14h92v28h-92z" class="tealp o"/></g>
<g transform="translate(470 330)"><path d="M-56-14h112v28h-112z" class="coralp o"/></g>''', arrow=True)

# --- 学び直し・正当・日常 -----------------------------------------------------

add('retrain', '前の仕事の道具を置き、新しい道具の使い方を一から学び直す',
    '再教育する、学び直す＝retrain。', f'''
{split()}
{table(352)}
<g opacity="0.3" transform="translate(150 250)">
  <path d="M-10-60h20v90h-20z" fill="{BRN}"/><path d="M-40 30h80v22h-80z" fill="{MUTED}"/></g>
{cross(150, 130, 0.6)}
{person(420, 350, 1.2, 1, 'teal', 'blue', 'hold', 'cap', 'smile')}
<g transform="translate(470 250) rotate(-14)">
  <path d="M-40-60h80v120h-80z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="-26" y="{{}}" width="{{}}" height="8" rx="4" fill="{MUTED}"/>'.format(-36 + i * 24, 52 - (i % 2) * 18) for i in range(3))}</g>
{arc(250, 170, 340, 190, 50, MUTED, True, 5)}''', arrow=True)

add('rightful', '名札と持ち主の名が一致し、品がもとの持ち主の手に戻る',
    '正当な権利をもつ＝rightful。', f'''
{person(450, 350, 1.2, -1, 'teal', 'blue', 'reach', 'short', 'smile')}
<g transform="translate(440 200)"><rect x="-40" y="-24" width="80" height="48" rx="6" class="tealp o"/></g>
<g transform="translate(240 210)">
  <rect x="-70" y="-46" width="140" height="92" rx="10" class="gold o"/>
  <path d="M-40-70h80v24h-80z" fill="#fffefd" class="o"/>
  <rect x="-30" y="-64" width="60" height="10" rx="5" fill="{MUTED}"/></g>
{arc(320, 170, 400, 180, 46, GRN, True, 5)}
{tick(120, 200, 0.8)}''', arrow=True)

add('routinely', 'カレンダーのどの日にも、同じ時刻の同じ印がついている',
    '日常的に、いつものように＝routinely。', f'''
<g transform="translate(280 200)">
  <path d="M-220-150h440v300h-440z" fill="#fffefd" class="o"/>
  <path d="M-220-150h440v50h-440z" class="teal o"/>
  {''.join(f'<path d="M{{}} -100v250" fill="none" stroke="{MUTED}" stroke-width="2.5"/>'.format(-220 + c * 88) for c in range(1, 5))}
  {''.join(f'<path d="M-220 {{}}h440" fill="none" stroke="{MUTED}" stroke-width="2.5"/>'.format(-100 + r * 84) for r in range(1, 3))}
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="18" class="coralp o"/>'.format(-176 + c * 88, -58 + r * 84) for c in range(5) for r in range(3))}</g>
{clock(540, 90, 40, 9, 0)}''')

# --- 印税・統治・守る ---------------------------------------------------------

add('royalty', '本が一冊売れるたび、そのたびに著者のもとへ小銭が入る',
    '印税、使用料／王族＝royalty。', f'''
{''.join(f'<g transform="translate({{}} 250)"><path d="M-40-56h80v112h-80z" class="{{}} o"/><path d="M-44-56h10v112h-10z" fill="{BRN}"/></g>'.format(90 + i * 90, c) for i, c in enumerate(['teal', 'coral', 'green']))}
{''.join(f'<path d="M{{}} 160q30-40 60 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(100 + i * 90) for i in range(3))}
{person(480, 350, 1.15, -1, 'violet', 'blue', 'reach', 'bun', 'smile')}
{''.join(coin(390 + i * 30, 160 - (i % 2) * 26, 17) for i in range(3))}''', arrow=True)

add('rule over', '玉座に座った王のもとに、領地の丘がすべて収まっている',
    '統治する＝rule over。', f'''
{''.join(f'<g transform="translate({{}} 340)"><path d="M-80 0q20-54 80-54t80 54z" class="greenp o"/></g>'.format(110 + i * 190) for i in range(3))}
<g transform="translate(300 250)">
  <path d="M-70 0v-40h140V0z" class="goldd o"/>
  <path d="M-56-40v-110h112v110z" class="gold o"/></g>
{sit(300, 250, 1.05, 1, 'violet', 'blue', 'short', 'flat', 'lap')}
{crown(300, 110, 0.5)}
{''.join(f'<path d="M300 180L{{}} 300" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(110 + i * 190) for i in range(3))}''')

add('safeguard', '大切な品に丈夫なおおいをかぶせ、鍵をかけて守る',
    '守る／安全策＝safeguard。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-130-60h260v100h-260z" fill="#dfe6ea" class="o"/>
  <path d="M-100-40h200v80h-200z" fill="#fffefd" class="o"/>
  <circle cy="0" r="30" class="gold o"/></g>
<g transform="translate(300 170)">
  <circle cy="-30" r="34" fill="none" stroke="{GLD}" stroke-width="12"/>
  <path d="M-44 0h88v58h-88z" class="gold o"/>
  <circle cy="26" r="9" class="ink"/></g>
{''.join(spark(120 + i * 360, 140, 0.7, 'gold') for i in range(2))}''')

finish(__file__)
