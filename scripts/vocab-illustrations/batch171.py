# -*- coding: utf-8 -*-
"""第171回。f-/g-/h-/i- の前半。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def ring_obj(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle r="22" fill="none" stroke="{GLD}" stroke-width="9"/>'
            f'<path d="M-11-24l11-18 11 18z" class="goldp o"/></g>')

def gear(x, y, r=54, teeth=8, cls='teal'):
    t = ''.join(f'<rect x="-9" y="{-r-14}" width="18" height="18" rx="3" transform="rotate({i*360/teeth})"/>' for i in range(teeth))
    return (f'<g transform="translate({x} {y})"><g class="{cls} o">{t}</g>'
            f'<circle r="{r}" class="{cls} o"/><circle r="{r*0.34}" fill="#fffaf1" class="o"/></g>')

def axis(x0=70, y0=300, w=460):
    return f'<path d="M{x0} {y0}h{w}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'

def star(x, y, s=1, cls='gold'):
    pts = []
    for i in range(10):
        a = math.radians(-90 + i * 36)
        r = 46 * s if i % 2 == 0 else 19 * s
        pts.append(f'{x + r*math.cos(a):.1f} {y + r*math.sin(a):.1f}')
    return f'<path d="M{"L".join(pts)}z" class="{cls} o"/>'

# --- 婚約・起動・消える -------------------------------------------------------

add('fiancee', '指輪をはめた左手を見せる女性が、婚約相手と並んで立つ',
    '婚約者(女性)＝fiancée。fiancé(男性)と対になる語です。', f'''
{person(200, 340, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(420, 340, 1.25, -1, 'coral', 'green', 'reach', 'bob', 'smile')}
{ring_obj(330, 200, 1.5)}
{ring(420, 250, 84, True, 'coral')}
<g transform="translate(310 100)">
  <path d="M0 26q-34-26-34-48 0-18 18-18 10 0 16 12 6-12 16-12 18 0 18 18 0 22-34 48z" class="coralp o"/></g>''', key='fiancée')

add('fire up', 'スイッチを入れると機械に火花が散り、いっせいに動き出す',
    '(機械を)起動する、奮い立たせる＝fire up。', f'''
{table(340)}
<g transform="translate(330 250)">
  <path d="M-130-90h260v180h-260z" class="teal o"/>
  <circle cx="-60" cy="-20" r="34" fill="#fffefd" class="o"/>
  <path d="M-60-20v-24" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path d="M30-50h80v46H30zM30 10h80v46H30z" class="tealp o"/></g>
<g transform="translate(140 240)">
  <path d="M-26 0h52v70h-52z" fill="{MUTED}" class="o"/>
  <path d="M0 0v-40" stroke="{INK}" stroke-width="10" stroke-linecap="round" fill="none"/></g>
{''.join(spark(250 + i * 70, 100 + (i % 2) * 30, 1.0, 'gold') for i in range(4))}
{''.join(f'<path d="M{480+i*18} {190+i*14}q14 12 0 26" fill="none" stroke="{GLD}" stroke-width="5"/>' for i in range(2))}''')

add('fizzle out', '勢いよく散っていた火花が、先へ行くほど小さくなって消えてしまう',
    '尻すぼみに終わる＝fizzle out。', f'''
<path d="M70 300q120-140 260-140t190 90" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/>
{''.join(spark(90 + i * 66, 290 - [0, 60, 100, 124, 136, 140, 138][i], 1.3 - i * 0.19, 'gold') for i in range(6))}
<g opacity="0.3">{spark(486, 172, 0.16, 'gold')}</g>
{''.join(f'<path d="M{500+i*18} {188+i*12}q10-12 0-24" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(2))}
{cross(548, 150, 0.5)}''')

add('flare up', 'おさまりかけていた小さな火が、急にまた大きく燃え上がる',
    '(争い・炎症が)再燃する＝flare up。', f'''
{split()}
<g opacity="0.5">{flame(150, 330, 0.32)}</g>
{''.join(f'<path d="M{124+i*22} 250q10-12 0-24" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(2))}
{flame(440, 350, 1.35)}
{arc(240, 200, 340, 190, 50, CRL, True, 5)}
{''.join(f'<path d="M{{}} {{}}l16-22" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>'.format(530 + i * 0, 120 + i * 30) for i in range(3))}''', arrow=True)

# --- やり通す・払う ----------------------------------------------------------

add('follow through', '振り始めたバットを途中で止めず、最後まで振り抜く',
    '最後までやり通す＝follow through。', f'''
{person(240, 340, 1.35, 1, 'teal', 'blue', 'reach', 'cap', 'smile')}
<g opacity="0.28" transform="translate(300 180) rotate(-70)"><path d="M-8 0h16v160h-16z" fill="{BRN}"/></g>
<g opacity="0.28" transform="translate(300 180) rotate(-20)"><path d="M-8 0h16v160h-16z" fill="{BRN}"/></g>
<g transform="translate(300 180) rotate(46)"><path d="M-10 0h20v170h-10z" fill="{BRN}" class="o"/></g>
<path d="M240 90a140 140 0 0 1 140 130" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 11" marker-end="url(#ar)"/>
{tick(500, 120, 0.9)}''', arrow=True)

add('fork out', '渋い顔のまま、財布から札束を取り出して手渡す',
    '(しぶしぶ)大金を払う＝fork out。', f'''
{person(170, 340, 1.25, 1, 'teal', 'blue', 'give', 'short', 'sad')}
<g transform="translate(250 250) rotate(-12)">
  <path d="M-56-40h112v80h-112z" fill="{BRN}" class="o"/>
  <path d="M-56-6h112" fill="none" stroke="#6a5040" stroke-width="4"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M-40-22h80v44h-80z" class="greenp o"/><circle r="10" fill="none" stroke="{GRN}" stroke-width="3"/></g>'.format(x, y, r) for x, y, r in [(360, 190, -10), (400, 236, 8), (440, 176, 16)])}
{hand(520, 220, -1)}
{arc(300, 190, 430, 200, 60, MUTED, True, 4)}
{''.join(f'<path d="M{{}} {{}}q12-12 0-24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(120 + i * 18, 170 - i * 12) for i in range(2))}''', arrow=True)

# --- 調合・不屈・断片 ---------------------------------------------------------

add('formulation', 'いくつもの材料を決まった割合で混ぜ、一つの処方にまとめる',
    '表現のしかた、定式化／調合＝formulation。', f'''
{table(340)}
{''.join(f'<g transform="translate({{}} 200)"><path d="M-24-60h48v70a24 24 0 0 1-48 0z" fill="#fffefd" class="o"/><path d="M-24-4h48v10a24 24 0 0 1-48 0z" class="{{}}"/></g>'.format(90 + i * 62, c) for i, c in enumerate(['coral', 'green', 'violet']))}
{''.join(f'<path d="M{{}} 230q20 30 60 34" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(100 + i * 62) for i in range(3))}
<g transform="translate(420 290)">
  <path d="M-16-100h32v54l52 90a14 14 0 0 1-12 22h-112a14 14 0 0 1-12-22l52-90z" fill="#fffefd" class="o"/>
  <path d="M-58 26l18-30h80l18 30a14 14 0 0 1-12 40h-92a14 14 0 0 1-12-40z" class="tealp"/></g>
{doc(540, 130, 84, 110, 3)}''', arrow=True)

add('fortitude', '強い横風の中でも、足を踏ん張って一歩も引かずに立ち続ける',
    '不屈の精神、我慢強さ＝fortitude。', f'''
{''.join(f'<path d="M40 {{}}q90-24 180 0t180 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>'.format(90 + i * 46) for i in range(5))}
{person(330, 350, 1.45, -1, 'teal', 'blue', 'stand', 'short', 'flat')}
<g transform="translate(330 350)"><path d="M-70 0h140" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}l40 10" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(70, 150 + i * 70) for i in range(2))}''', arrow=True)

add('fragmentation', '一枚だった板が砕けて、大小の破片に散らばる',
    '断片化、分裂＝fragmentation。', f'''
{split()}
<g transform="translate(150 200)"><path d="M-100-80h200v160h-200z" class="teal o"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M{{}}z" class="teal o"/></g>'.format(x, y, r, p) for x, y, r, p in [
  (390, 140, 12, 'M-40-30h60l10 40-50 20z'), (470, 200, -24, 'M-30-24h44l6 34-40 14z'),
  (400, 250, 30, 'M-26-20h36l8 30-36 12z'), (500, 120, -14, 'M-20-16h28l6 24-28 10z'),
  (470, 300, 20, 'M-24-18h32l6 26-32 10z'), (360, 320, -30, 'M-18-14h24l4 20-24 8z')]) }
{arc(260, 160, 320, 170, 44, MUTED, True, 4)}''', arrow=True)

# --- 率直・摩擦・じょうご -----------------------------------------------------

add('frank', '飾りのない一直線の吹き出しで思ったままを伝え、相手もうなずいて受け取る',
    '率直な、ざっくばらんな＝frank。', f'''
{person(150, 340, 1.2, 1, 'teal', 'blue', 'point', 'short', 'smile')}
{person(460, 340, 1.2, -1, 'coral', 'green', 'stand', 'bob', 'smile')}
<g transform="translate(310 160)">
  <path d="M-90-56h180v112h-24l-16 26-14-26h-126z" fill="#fffefd" class="o"/>
  <path d="M-60-10h120" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g>
{tick(510, 150, 0.7)}''')

add('friction', '二つの面をこすり合わせると、境目に熱と火花が生まれる',
    '摩擦、あつれき＝friction。', f'''
<g transform="translate(300 140)"><path d="M-200-60h400v90h-400z" fill="{STONE}" class="o"/></g>
<g transform="translate(300 260)"><path d="M-200-30h400v90h-400z" fill="{STONE}" class="o"/></g>
{''.join(spark(130 + i * 68, 200, 0.9, 'coral') for i in range(6))}
{line(120, 110, 250, 110, INK, False, 6)}
{line(480, 290, 350, 290, INK, False, 6)}
{''.join(f'<path d="M{{}} {{}}q14-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(500 + i * 20, 180 - i * 14) for i in range(2))}''', arrow=True)

add('funnel', '広い口のじょうごを使って、細い口の瓶へこぼさず注ぎ入れる',
    'じょうご、流し込む＝funnel。', f'''
{table(346)}
<g transform="translate(300 180)">
  <path d="M-110-60h220l-88 100v70h-44v-70z" fill="#fffefd" class="o"/>
  <path d="M-110-60h220l-20 22h-180z" class="bluep"/></g>
<g transform="translate(300 300)">
  <path d="M-16-70h32v20l30 30v60a14 14 0 0 1-14 14h-64a14 14 0 0 1-14-14v-60l30-30z" fill="#fffefd" class="o"/>
  <path d="M-62 10h124v40a14 14 0 0 1-14 14h-96a14 14 0 0 1-14-14z" class="bluep"/></g>
<g transform="translate(150 80) rotate(40)">
  <path d="M-30-50h60v90a22 22 0 0 1-22 22h-16a22 22 0 0 1-22-22z" class="tealp o"/></g>
{''.join(drop(240 + i * 12, 90 + i * 22, 1.0, 'blue') for i in range(3))}''')

# --- 準備・一般化・先んじる ---------------------------------------------------

add('gear up', 'ヘルメットと靴とかばんを身につけ、出発の支度を整える',
    '準備を整える＝gear up。', f'''
{person(300, 340, 1.4, 1, 'teal', 'blue', 'stand', 'cap', 'smile')}
{''.join(f'<g opacity="0.3" transform="translate({{}} {{}})">{{}}</g>'.format(x, y, o) for x, y, o in [
  (110, 120, f'<path d="M-36 20q0-44 36-44t36 44z" class="bluep o"/>'),
  (110, 240, f'<path d="M-40-16h80v32h-80z" fill="{BRN}" stroke="{INK}" stroke-width="2.5"/>'),
  (110, 330, f'<path d="M-40 14q0-34 30-34h20l30 20v14z" fill="{INK}"/>')])}
{''.join(f'<path d="M160 {{}}h80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(y) for y in (120, 240, 330))}
{tick(500, 140, 0.9)}
<g transform="translate(470 300)"><path d="M-44-30h88v70h-88z" fill="{BRN}" class="o"/>
  <path d="M-20-30q20-22 40 0" fill="none" stroke="{BRN}" stroke-width="8"/></g>''', arrow=True)

add('generalisation', 'たった数個の例を見ただけで、全体をひとつの色で塗ってしまう',
    '一般化、大ざっぱな決めつけ＝generalisation。', f'''
{''.join(f'<circle cx="{{}}" cy="150" r="26" class="coral o"/>'.format(90 + i * 64) for i in range(3))}
{arc(240, 200, 340, 200, 46, MUTED, True, 5)}
<g transform="translate(450 220)">
  <path d="M-120-110h240v220h-240z" class="coralp o"/>
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="20" class="coral o"/>'.format(-80 + (i % 3) * 80, -70 + (i // 3) * 74) for i in range(9))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="20" class="teal o"/>'.format(x, y) for x, y in [(410, 150), (490, 224)])}
{ring(410, 150, 32, True)}{ring(490, 224, 32, True)}''', arrow=True)

add('get ahead', '同じ階段を上る中で、一人だけ数段先へ進んでいる',
    '先んじる、出世する＝get ahead。', f'''
{''.join(f'<path d="M{{}} 350v-{{}}h90v{{}}z" fill="{STONE}" class="o"/>'.format(40 + i * 90, 40 + i * 56, 40 + i * 56) for i in range(5))}
{person(140, 310, 0.78, 1, 'teal', 'blue', 'walk', 'short', 'flat')}
{person(230, 254, 0.78, 1, 'green', 'blue', 'walk', 'bob', 'flat')}
{person(450, 142, 0.9, 1, 'coral', 'violet', 'up', 'short', 'smile')}
{ring(450, 90, 60, True)}
{arc(280, 220, 400, 130, 60, MUTED, True, 4)}''', arrow=True)

# --- 逃れる・引き起こす -------------------------------------------------------

add('get away with', '割った窓を後ろに残したまま、とがめられずに歩き去っていく',
    '(悪いことをして)罰を受けずにすむ＝get away with。', f'''
<g transform="translate(150 180)">
  <path d="M-90-100h180v200h-180z" fill="#eaf1f6" class="o"/>
  <path d="M-90-100l84 80-64 54 74 66M90-100l-88 86 84 54-42 60" fill="none" stroke="{INK}" stroke-width="3"/></g>
{person(400, 340, 1.2, 1, 'teal', 'blue', 'walk', 'cap', 'smile')}
{arc(300, 250, 470, 250, 60, MUTED, True, 5)}
<g transform="translate(300 110)">
  <path d="M-26 16q-6-26 14-34 22-8 32 12 8 18-12 26z" fill="{MUTED}"/>
  <path d="M-26 16l-22 18" stroke="{MUTED}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
{cross(300, 110, 0.7)}''', arrow=True)

add('give rise to', '一つの出来事から、いくつもの結果が枝分かれして生まれる',
    '〜を引き起こす＝give rise to。', f'''
<g transform="translate(120 200)"><circle r="56" class="coral o"/></g>
{''.join(f'<path d="M182 200Q300 {{}} 430 {{}}" fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"/>'.format(200 + (i - 1) * 90, 90 + i * 110) for i in range(3))}
{''.join(f'<circle cx="470" cy="{{}}" r="38" class="teal o"/>'.format(90 + i * 110) for i in range(3))}''', arrow=True)

# --- 取りかかる・同調・沈む ---------------------------------------------------

add('go about', '道具を順に並べ、いつもの手順どおりに仕事へ取りかかる',
    '(仕事に)取りかかる＝go about。', f'''
{table(320)}
{''.join(f'<g transform="translate({{}} 290)">{{}}</g>'.format(120 + i * 80, o) for i, o in enumerate([
  f'<path d="M-8-70h16v70h-16z" fill="{BRN}" class="o"/><path d="M-26-90h52v22h-52z" fill="{MUTED}" class="o"/>',
  f'<path d="M-30-16h60v16h-60z" fill="{MUTED}" class="o"/><path d="M-8-60h16v44h-16z" fill="{BRN}" class="o"/>',
  f'<circle cy="-26" r="26" fill="none" stroke="{MUTED}" stroke-width="8"/><path d="M-6 0h12v-14h-12z" fill="{MUTED}"/>']))}
{''.join(f'<circle cx="{{}}" cy="120" r="18" class="tealp o"/><text>{{}}</text>'.format(120 + i * 80, i) for i in range(3))}
{''.join(f'<path d="M{{}} 120h44" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(142 + i * 80) for i in range(2))}
{person(440, 330, 1.2, -1, 'teal', 'blue', 'reach', 'short', 'smile')}''', arrow=True)

add('go along with', '前を行く人が選んだ道に、後ろの人も同じ向きで付いていく',
    '(意見・計画に)同調する、従う＝go along with。', f'''
<path d="M60 330q160-120 480-130" fill="none" stroke="{STONE}" stroke-width="46" stroke-linecap="round"/>
{person(430, 250, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{person(280, 300, 1.05, 1, 'coral', 'green', 'walk', 'bob', 'smile')}
{person(140, 340, 1.05, 1, 'violet', 'gold', 'walk', 'bun', 'smile')}
{arc(180, 250, 400, 170, 50, MUTED, True, 4)}''', arrow=True)

add('go under', '会社の建物が水面の下へ沈んでいく',
    '(会社が)倒産する、沈む＝go under。', f'''
<path d="M0 190h600v210H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 196q22-12 44 0t44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 380)">
  <path d="M-90 0v-210h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-104-210L0-268l104 58z" class="teal o"/>
  {''.join(f'<rect x="{{}}" y="{{}}" width="30" height="24" class="tealp o"/>'.format(-64 + (i % 3) * 46, -182 + (i // 3) * 44) for i in range(6))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="none" stroke="#ffffff" stroke-width="3"/>'.format(x, y, r) for x, y, r in [(210, 150, 10), (230, 110, 7), (250, 80, 5)])}
{line(460, 120, 460, 260, MUTED, True, 5)}''', arrow=True)

# --- 文法 --------------------------------------------------------------------

add('grammar', '語のブロックを決まった枠の順に並べると、一つの文になる',
    '文法＝grammar。', f'''
<g transform="translate(300 180)">
  {''.join(f'<path d="M{{}} -40h{{}}v80h-{{}}z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>'.format(-240 + i * 130, 110, 110) for i in range(4))}</g>
{''.join(f'<rect x="{{}}" y="150" width="94" height="60" rx="8" class="{{}} o"/>'.format(68 + i * 130, c) for i, c in enumerate(['teal', 'coral', 'gold', 'violet']))}
<path d="M60 290h480" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
{''.join(f'<path d="M{{}} 290v-14" fill="none" stroke="{INK}" stroke-width="5"/>'.format(60 + i * 160) for i in range(4))}
{tick(300, 350, 0.7)}''')

add('grammatical', '正しい順に並んだ語の列には丸、順が崩れた列には×がつく',
    '文法の、文法にかなった＝grammatical。', f'''
{split()}
{''.join(f'<rect x="{{}}" y="140" width="52" height="56" rx="8" class="{{}} o"/>'.format(40 + i * 62, c) for i, c in enumerate(['teal', 'coral', 'gold', 'violet']))}
{tick(150, 270, 0.9)}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-26" y="-28" width="52" height="56" rx="8" class="{{}} o"/></g>'.format(x, y, r, c) for x, y, r, c in [(360, 170, -18, 'teal'), (424, 140, 22, 'coral'), (486, 180, -30, 'gold'), (540, 146, 14, 'violet')])}
{cross(450, 270, 0.9)}''')

# --- 止まる・好きになる -------------------------------------------------------

add('grind to a halt', 'かみ合っていた歯車に物が挟まり、回転がじりじりと止まる',
    '徐々に止まる、機能しなくなる＝grind to a halt。', f'''
{gear(220, 200, 78, 10, 'teal')}
{gear(400, 260, 58, 8, 'blue')}
<g transform="translate(310 222) rotate(24)"><path d="M-16-40h32v80h-32z" fill="{STONE}" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}l16-18" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(316 + i * 18, 150 - i * 12) for i in range(3))}
<g transform="translate(140 90)"><path d="M-36 0a36 36 0 1 1 12 26" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="10 9" marker-end="url(#ar)"/></g>
{cross(500, 120, 0.7)}''', arrow=True)

add('grow on', '最初は気に入らなかったものが、日がたつにつれて好きになっていく',
    'だんだん好きになってくる＝grow on。', f'''
{''.join(f'<g transform="translate({{}} 300)"><path d="M-44-60h88v60h-88z" class="violet o"/></g>'.format(100 + i * 160) for i in range(3))}
{head(100, 170, 34, 'teal', 'short', 'sad')}
{head(260, 170, 34, 'teal', 'short', 'flat')}
{head(420, 170, 34, 'teal', 'short', 'smile')}
{''.join(f'<path d="M{{}} 170h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(146 + i * 160) for i in range(2))}
{clock(530, 170, 40, 3, 30)}''', arrow=True)

add('harden', 'どろりとした液が時間とともに固まり、たたいても崩れない塊になる',
    '固くする、固くなる＝harden。', f'''
{split()}
{table(346)}
<g transform="translate(150 300)">
  <path d="M-80 0q-6-40 30-46 10-30 44-22 34 8 30 40 20 8 16 28z" class="goldp o"/></g>
<g transform="translate(450 300)">
  <path d="M-70-70h140v70h-140z" class="gold o"/>
  <path d="M-70-70h140" fill="none" stroke="{GLDD}" stroke-width="4"/></g>
<g transform="translate(440 160) rotate(-24)">
  <path d="M-10 0h20v110h-20z" fill="{BRN}" class="o"/>
  <path d="M-40-34h80v34h-80z" fill="{MUTED}" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}l14-16" fill="none" stroke="{GLD}" stroke-width="5"/>'.format(500 + i * 16, 250 - i * 12) for i in range(2))}
{arc(240, 220, 340, 220, 44, MUTED, True, 4)}''', arrow=True)

# --- 発言権・タカ ------------------------------------------------------------

add('have a say in', '円卓につく全員に一枚ずつ札があり、自分の札を場に出せる',
    '〜について発言権がある＝have a say in。', f'''
<g transform="translate(300 230)"><ellipse rx="200" ry="110" fill="#c9a464" class="o"/>
  <ellipse rx="170" ry="88" fill="none" stroke="{BRN}" stroke-width="4"/></g>
{''.join(f'<g transform="translate({{}} {{}})">{{}}</g>'.format(x, y, head(0, 0, 26, c, h)) for x, y, c, h in [
  (110, 210, 'teal', 'short'), (300, 100, 'green', 'bob'), (490, 210, 'blue', 'bun'), (300, 350, 'gold', 'cap')])}
{''.join(f'<rect x="{{}}" y="{{}}" width="46" height="30" rx="5" class="coral o"/>'.format(x, y) for x, y in [(170, 216), (277, 168), (384, 216), (277, 262)])}
{ring(300, 230, 60, True)}''')

add('hawk', '幅の広い翼を張り、鋭いくちばしのタカが空を舞う',
    'タカ、(政治の)強硬派＝hawk。', f'''
{''.join(cloud(110 + i * 240, 90, 0.9, 'blue') for i in range(2))}
<g transform="translate(300 210)">
  <path d="M-20 0q-60-70-190-60 70 20 96 60-70 4-96 40 90-16 150 10z" fill="#8b6437" class="o"/>
  <path d="M20 0q60-70 190-60-70 20-96 60 70 4 96 40-90-16-150 10z" fill="#8b6437" class="o"/>
  <ellipse rx="34" ry="52" fill="#a0764a" class="o"/>
  <circle cx="0" cy="-58" r="26" fill="#a0764a" class="o"/>
  <path d="M20-62l30 10-30 12z" class="gold o"/>
  <circle cx="10" cy="-68" r="4" class="ink"/>
  <path d="M0 52l-14 34M0 52l14 34" stroke="{GLDD}" stroke-width="7" fill="none" stroke-linecap="round"/></g>''')

# --- 時を指す副詞 ------------------------------------------------------------

add('henceforth', '時間の線の上で、今この印から右側だけが新しい色に切り替わる',
    '今後は＝henceforth。', f'''
{axis(60, 220, 480)}
<path d="M300 220h240" fill="none" stroke="{TEA}" stroke-width="14" stroke-linecap="round"/>
<path d="M300 140v160" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>
<circle cx="300" cy="220" r="14" class="coral o"/>
{''.join(f'<path d="M{{}} 220v-16" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(100 + i * 80) for i in range(6))}
{arc(320, 120, 500, 120, 40, TEA, True, 5)}''', arrow=True)

add('hitherto', '時間の線の上で、今この印までの左側だけが塗られている',
    'これまで＝hitherto。', f'''
{axis(60, 220, 480)}
<path d="M60 220h240" fill="none" stroke="{TEA}" stroke-width="14" stroke-linecap="round"/>
<path d="M300 140v160" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>
<circle cx="300" cy="220" r="14" class="coral o"/>
{''.join(f'<path d="M{{}} 220v-16" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(100 + i * 80) for i in range(6))}
{arc(280, 120, 100, 120, 40, TEA, True, 5)}''', arrow=True)

add('hereby', '署名して判を押したその場で、書面が効力を持つ',
    'これによって、ここに＝hereby。', f'''
{table(330)}
{doc(280, 230, 210, 250, 4)}
<g transform="translate(300 300)"><path d="M-70 0q40-30 70-2t60-16" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></g>
<g transform="translate(430 160) rotate(30)">
  <path d="M-9-90h18v130l-9 24-9-24z" class="teal o"/>
  <path d="M-9 40h18" fill="none" stroke="{INK}" stroke-width="3"/></g>
<g transform="translate(200 220)"><circle r="34" class="coralp o"/><circle r="22" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{spark(180, 110, 1.0, 'gold')}{spark(430, 320, 0.8, 'gold')}''')

# --- 理想 --------------------------------------------------------------------

add('idealism', '足もとの地面から遠く離れた高い星へ、まっすぐ手を伸ばす',
    '理想主義＝idealism。', f'''
{star(430, 90, 1.3)}
{person(190, 350, 1.3, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{line(250, 180, 370, 110, MUTED, True, 5)}
<path d="M40 360h520" fill="none" stroke="{BRN}" stroke-width="8"/>
{''.join(f'<path d="M{{}} 300q10-18 0-36" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(330 + i * 30) for i in range(2))}''', arrow=True)

add('idealist', '星を描いた旗を高くかかげ、理想を信じる人が先頭に立つ',
    '理想主義者＝idealist。', f'''
{person(250, 350, 1.35, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<g transform="translate(310 120)">
  <path d="M0 220V-40" stroke="{BRN}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <path d="M6-40h140l-30 44 30 44H6z" class="violet o"/>
  {star(76, 8, 0.6, 'goldp')}</g>
{''.join(head(80 + i * 0, 330, 24, 'coral', 'bob') for i in range(1))}
{head(470, 330, 24, 'green', 'bun')}''')

add('ideally', '実際の形の横に、点線で描いた理想の形が重ねて示される',
    '理想を言えば、できれば＝ideally。', f'''
<g transform="translate(200 220)">
  <path d="M-90 90q-20-90 20-130 30-30 70-10l20 140z" class="teal o"/></g>
<g transform="translate(420 220)">
  <path d="M-90 90v-180h180v180z" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 11"/>
  {star(0, 0, 0.9, 'goldp')}</g>
{arc(300, 180, 330, 180, 36, MUTED, True, 4)}
{''.join(f'<path d="M{{}} 90q10-16 0-30" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(500 + i * 22) for i in range(2))}''', arrow=True)

# --- 必須・帝国・暗黙 ---------------------------------------------------------

add('imperative', '持ち物の一覧で、一つだけ赤い印がつき、これだけは外せないと示される',
    '絶対に必要な、必須のこと＝imperative。', f'''
<g transform="translate(300 200)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  {''.join(f'<rect x="-130" y="{{}}" width="{{}}" height="12" rx="6" fill="{MUTED}"/>'.format(-104 + i * 56, 190 - (i % 3) * 40) for i in range(5))}
  {''.join(f'<rect x="-150" y="{{}}" width="16" height="16" rx="3" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(-106 + i * 56) for i in range(5))}</g>
<g transform="translate(150 256)"><rect x="-8" y="-8" width="16" height="16" rx="3" class="coral o"/></g>
<g transform="translate(170 256)"><path d="M120 0h60" fill="none" stroke="{CRL}" stroke-width="0"/></g>
{ring(300, 256, 44, True)}
<g transform="translate(500 90)"><path d="M-8-40h16v52h-16z" class="coral"/><circle cy="30" r="9" class="coral"/></g>''')

add('imperial', '王冠のもとに、離れた土地のどれにも同じ旗が立っている',
    '帝国の＝imperial。', f'''
<g transform="translate(300 90)">
  <path d="M-70 30l-14-70 44 30 40-48 40 48 44-30-14 70z" class="gold o"/>
  <path d="M-70 30h140v18h-140z" class="goldd o"/></g>
{''.join(f'<g transform="translate({{}} 330)"><path d="M-70 0q20-50 70-50t70 50z" class="greenp o"/><path d="M0-46v-70" stroke="{BRN}" stroke-width="6" fill="none"/><path d="M4-116h54l-16 22 16 22H4z" class="violet o"/></g>'.format(110 + i * 190) for i in range(3))}
{''.join(f'<path d="M300 150L{{}} 216" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(110 + i * 190) for i in range(3))}''')

add('implicitly', '何も書かれていない吹き出しなのに、相手にはちゃんと伝わってうなずく',
    '暗黙のうちに＝implicitly。', f'''
{person(150, 340, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(460, 340, 1.2, -1, 'coral', 'green', 'stand', 'bob', 'smile')}
<g transform="translate(300 160)">
  <path d="M-90-56h180v112h-30l-18 26-12-26h-120z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/></g>
{arc(390, 150, 430, 200, 40, MUTED, True, 4)}
<g transform="translate(500 190)"><path d="M-24 0q24 22 48 0" fill="none" stroke="{GRN}" stroke-width="6" stroke-linecap="round"/></g>''', arrow=True)

# --- 押しつけ・貧困・影響されやすい -------------------------------------------

add('imposition', '大きな手が上から規則の板を押しつけ、下の人が縮こまる',
    '(税・規則の)課すこと、無理な頼み＝imposition。', f'''
{hand(300, 90, 1)}
<g transform="translate(300 200)">
  <path d="M-150-40h300v80h-300z" class="violet o"/>
  {''.join(f'<rect x="{{}}" y="-14" width="70" height="10" rx="5" fill="#fffefd"/>'.format(-120 + i * 90) for i in range(3))}</g>
{''.join(f'<path d="M{{}} 246v22" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"/>'.format(200 + i * 100) for i in range(3))}
{''.join(head(200 + i * 100, 340, 26, 'teal', 'short', 'sad') for i in range(3))}''', arrow=True)

add('impoverishment', 'かつて重かった財布の中身が空になり、家も傾いていく',
    '貧困化＝impoverishment。', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-60-46h120v92h-120z" fill="{BRN}" class="o"/>
  <path d="M-60-4h120" fill="none" stroke="#6a5040" stroke-width="4"/>
  {''.join(f'<circle cx="{{}}" cy="-70" r="16" class="gold o"/>'.format(-34 + i * 34) for i in range(3))}</g>
<g transform="translate(450 200)">
  <path d="M-60-46h120v92h-120z" fill="{BRN}" class="o"/>
  <path d="M-60-4h120" fill="none" stroke="#6a5040" stroke-width="4"/></g>
{house(150, 350, 0.5, 'coral')}
<g transform="translate(450 350) rotate(-10)">{house(0, 0, 0.5, 'coral')}</g>
{arc(260, 160, 340, 160, 44, MUTED, True, 4)}''', arrow=True)

add('impressionable', 'やわらかい粘土に、軽く押しただけで形がくっきり残る',
    '影響を受けやすい＝impressionable。', f'''
{table(346)}
<g transform="translate(300 290)">
  <path d="M-140-50q140-40 280 0v50h-280z" class="goldp o"/>
  <path d="M-60-40q-10 34 26 36 40 2 34-40" fill="none" stroke="{GLDD}" stroke-width="5"/>
  <circle cx="70" cy="-16" r="22" fill="none" stroke="{GLDD}" stroke-width="5"/></g>
{hand(160, 160, 1)}
{line(200, 210, 220, 250, MUTED, True, 4)}
<g transform="translate(420 150)"><circle r="26" class="coral o"/></g>
{line(420, 186, 400, 234, MUTED, True, 4)}''', arrow=True)

# --- 過程・理論・傾向 ---------------------------------------------------------

add('in the course of', '一本に伸びた時間の帯の、始まりと終わりの間に出来事の印がつく',
    '〜の間に、〜の過程で＝in the course of。', f'''
<g transform="translate(300 200)">
  <path d="M-230-34h460v68h-460z" class="tealp o"/>
  <path d="M-230-34v68M230-34v68" fill="none" stroke="{TEA}" stroke-width="8"/></g>
{''.join(f'<circle cx="{{}}" cy="200" r="18" class="coral o"/>'.format(160 + i * 100) for i in range(3))}
{''.join(f'<path d="M{{}} 160v-40" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(160 + i * 100) for i in range(3))}
<path d="M70 290h460" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

add('in theory', '紙の上の設計図では完璧なのに、組み上げた実物は傾いている',
    '理論上は＝in theory。', f'''
{split()}
<g transform="translate(150 190)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <path d="M-60-40h120v120h-120z" fill="none" stroke="{BLU}" stroke-width="5"/>
  <path d="M-60-40l60-46 60 46" fill="none" stroke="{BLU}" stroke-width="5"/></g>
{tick(150, 340, 0.7)}
<g transform="translate(450 250) rotate(-13)">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
  <path d="M-80-70L0-128l80 58z" class="teald o"/></g>
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(530 + i * 0, 140 + i * 26) for i in range(2))}''')

add('inclination', '坂の上に置かれた球が、自然に低いほうへ転がろうとする',
    '傾向、意向／傾き＝inclination。', f'''
<path d="M40 340L520 160v180H40z" fill="#d8cdb6" class="o"/>
<circle cx="440" cy="150" r="36" class="teal o"/>
<g opacity="0.3"><circle cx="330" cy="192" r="36" class="teal"/><circle cx="220" cy="234" r="36" class="teal"/></g>
{arc(400, 120, 200, 200, 60, MUTED, True, 5)}
<path d="M40 340h120" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<path d="M160 340L280 295" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''', arrow=True)

# --- 合わない・食い違い・組み入れ ---------------------------------------------

add('incompatible', '形の違うプラグと差し込み口がどうしてもはまらない',
    '両立しない、互換性のない＝incompatible。', f'''
<g transform="translate(210 210)">
  <path d="M-90-60h90v120h-90z" class="teal o"/>
  <path d="M0-34h50v24H0zM0 10h50v24H0z" class="teald o"/></g>
<g transform="translate(410 210)">
  <path d="M90-60H0v120h90z" class="coral o"/>
  <circle cx="-24" cy="-22" r="16" fill="#fffaf1" class="o"/>
  <circle cx="-24" cy="22" r="16" fill="#fffaf1" class="o"/></g>
{cross(300, 330, 0.9)}
{''.join(f'<path d="M{{}} {{}}l14-16" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(286 + i * 16, 130 - i * 12) for i in range(3))}''')

add('inconsistency', '同じ型から出てくるはずの品の中に、一つだけ形の違うものが混じる',
    '一貫性のなさ、矛盾＝inconsistency。', f'''
<g transform="translate(300 90)">
  <path d="M-110-50h220v100h-220z" fill="{MUTED}" class="o"/>
  <path d="M-40 50h80v20h-80z" fill="{MUTED}"/></g>
{''.join(f'<rect x="{{}}" y="260" width="66" height="70" rx="8" class="teal o"/>'.format(60 + i * 92) for i in range(3))}
<g transform="translate(371 296) rotate(18)"><path d="M-40-40l52 8 24 48-56 20z" class="coral o"/></g>
{''.join(f'<rect x="{{}}" y="260" width="66" height="70" rx="8" class="teal o"/>'.format(428 + i * 92) for i in range(1))}
{ring(371, 292, 62, True)}
{''.join(f'<path d="M{{}} 160v60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>'.format(93 + i * 92) for i in range(5))}''')

add('incorporation', '別々だった部品が、一つの本体の中に組み入れられて収まる',
    '組み入れ、法人化＝incorporation。', f'''
{split()}
<g transform="translate(140 200)">
  <path d="M-90-90h180v180h-180z" class="teal o"/>
  <path d="M-46-46h92v92h-92z" fill="#fffaf1" class="o"/></g>
<g transform="translate(140 200)"><path d="M-40-40h80v80h-80z" class="coral o" opacity="0"/></g>
<g transform="translate(270 320)"><path d="M-38-38h76v76h-38z" class="coral o"/><path d="M-38-38h76v76h-76z" class="coral o"/></g>
<g transform="translate(460 200)">
  <path d="M-90-90h180v180h-180z" class="teal o"/>
  <path d="M-46-46h92v92h-92z" fill="#fffaf1" class="o"/>
  <path d="M-40-40h80v80h-80z" class="coral o"/></g>
{arc(330, 250, 420, 230, 60, MUTED, True, 4)}''', arrow=True)

add('indefinitely', '終わりの印がないまま、線が右へどこまでも伸び続ける',
    '無期限に＝indefinitely。', f'''
{axis(60, 220, 420)}
<path d="M60 220h400" fill="none" stroke="{TEA}" stroke-width="14" stroke-linecap="round"/>
<path d="M470 220h20M506 220h20M542 220h20" fill="none" stroke="{TEA}" stroke-width="14" stroke-linecap="round"/>
<path d="M60 150v140" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
<g opacity="0.35"><path d="M470 150v140" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="10 9"/></g>
{cross(470, 110, 0.5)}''')

finish(__file__)
