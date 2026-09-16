# -*- coding: utf-8 -*-
"""第42回: plus42 の100語（e〜h）。数字と基礎語・機能語が多い。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

# --- この回で使う小物 --------------------------------------------------------

def counters(n, cx=300, cy=278, cls='gold', dx=64, dy=64, r=22):
    """数えるための丸いもの。いちばん下の列を cy に合わせる。"""
    cols = 4 if n > 4 else n
    rows = (n + cols - 1) // cols
    return ''.join(
        f'<circle cx="{cx + (i % cols - (cols - 1) / 2) * dx:.0f}" '
        f'cy="{cy - (rows - 1 - i // cols) * dy:.0f}" r="{r}" class="{cls} o"/>'
        for i in range(n))

def rods(n, x0=None, top=52, h=244, cls='teal'):
    """10のまとまりを表す棒。x0 省略時は中央そろえ。"""
    if x0 is None:
        x0 = 300 - (n - 1) * 31
    g = []
    for i in range(n):
        cx = x0 + i * 62
        g.append(f'<rect x="{cx-23}" y="{top}" width="46" height="{h}" rx="14" class="paper"/>')
        g.append(''.join(f'<circle cx="{cx}" cy="{top + 16 + j * 23}" r="9" class="{cls}"/>' for j in range(10)))
        g.append(f'<rect x="{cx-23}" y="{top}" width="46" height="{h}" rx="14" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    return ''.join(g)

def tens_ones(t, o, cls='teal'):
    """10の棒 t 本と、ばらの o 個。"""
    g = rods(t, 200 if t == 1 else None, cls=cls) if t else ''
    if o:
        g += counters(o, 420 if t else 300, 278, cls, 56, 56)
    return g

def flagpole(x, y, h=74, cls='coral'):
    return (f'<path d="M{x:.0f} {y:.0f}v-{h}" fill="none" stroke="{BRN}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M{x:.0f} {y-h:.0f}h54l-17 16 17 16h-54z" class="{cls} o"/>')

def stair(n, span=420.0, rise=190.0, x0=90, y0=352, cls='gold'):
    """n段の階段。いちばん上に人と旗。順序を数える絵に使う。"""
    w = span / n
    h = min(38.0, rise / n)
    d = f'M{x0} {y0}'
    for _ in range(n):
        d += f'v-{h:.0f}h{w:.0f}'
    d += f'v{h * n:.0f}H{x0}z'
    topy = y0 - n * h
    return (f'<path d="{d}" class="{cls}p o"/>'
            + person(x0 + n * w - w * 0.7, topy, min(0.85, w / 68), 1, 'teal', 'blue', 'up', 'short', 'smile')
            + flagpole(x0 + n * w - w * 0.15, topy, 74))

def plank(x, y, w=300, d=16, cls='gold'):
    return f'<path d="M{x-w/2} {y}h{w}v{d}h-{w}z" class="{cls}d o"/>'

def shelf(x, y, w=300, cls='gold'):
    return (plank(x, y, w, 16, cls)
            + f'<path d="M{x-w/2+24} {y+16}v18M{x+w/2-24} {y+16}v18" fill="none" stroke="#a0764a" stroke-width="7"/>')

def tumbler(x, y, w=56, h=84, level=0.6, cls='blue'):
    """コップ。(x,y)は底の中心。level を 1 にすると縁いっぱい。"""
    tw = w * 0.78
    lw = tw + (w - tw) * level
    return (f'<path d="M{x-w/2} {y-h}h{w}l-{(w-tw)/2:.0f} {h}h-{tw:.0f}z" fill="#eef6fb" class="o"/>'
            f'<path d="M{x-lw/2:.0f} {y-h*level:.0f}h{lw:.0f}l-{lw*0.22:.0f} {h*level:.0f}h-{lw*0.56:.0f}z" class="{cls}p"/>'
            f'<path d="M{x-w/2} {y-h}h{w}l-{(w-tw)/2:.0f} {h}h-{tw:.0f}z" fill="none" stroke="{INK}" stroke-width="2.5"/>')

def letter(x, y, s=1, cls='gold'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-46-30h92v60h-92z" class="{cls}p o"/>'
            f'<path d="M-46-30l46 34 46-34" fill="none" stroke="{INK}" stroke-width="3"/></g>')

def heart(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 32C-40 4-50-14-50-30-50-50-26-58 0-32 26-58 50-50 50-30 50-14 40 4 0 32z" class="{cls} o"/></g>')

def lens(x, y, r=52):
    return (f'<g stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none">'
            f'<circle cx="{x}" cy="{y}" r="{r}" class="bluep"/>'
            f'<path d="M{x + r*0.72:.0f} {y + r*0.72:.0f}l{r*0.8:.0f} {r*0.8:.0f}"/></g>')

def suitcase(x, y, w=104, h=72, cls='coral'):
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M{-w/2} {-h/2}h{w}v{h}h-{w}z" class="{cls} o"/>'
            f'<path d="M{-w/2} {-3}h{w}" fill="none" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M-18 {-h/2}v-16h36v16" fill="none" stroke="{INK}" stroke-width="6"/></g>')

def soccer(x, y, r=38):
    p = ' '.join(f'{x + r*0.52*math.cos(math.radians(a)):.0f} {y + r*0.52*math.sin(math.radians(a)):.0f}'
                 for a in range(-90, 270, 72))
    sp = ''.join(f'<path d="M{x + r*0.52*math.cos(math.radians(a)):.0f} {y + r*0.52*math.sin(math.radians(a)):.0f}'
                 f'L{x + r*math.cos(math.radians(a+36)):.0f} {y + r*math.sin(math.radians(a+36)):.0f}" '
                 f'stroke="{INK}" stroke-width="3" fill="none"/>' for a in range(-90, 270, 72))
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fffefd" class="o"/><path d="M{p}z" class="ink"/>{sp}'

def umbrella(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-84 0q22-58 84-58t84 58q-42-18-84-6-42-12-84 6z" class="{cls} o"/>'
            f'<path d="M0-50v70q0 18-20 18" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/></g>')

def pot(x, y, w=122, h=78, cls='coral'):
    """植木鉢。(x,y)は底の中心。"""
    bw = w * 0.68
    return (f'<path d="M{x-w/2} {y-h}h{w}l-{(w-bw)/2:.0f} {h}h-{bw:.0f}z" fill="#fffdf6" class="o"/>'
            f'<path d="M{x-w/2} {y-h}h{w}v16h-{w}z" class="{cls} o"/>')

def key_(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{GLDD}" stroke-width="9" stroke-linecap="round">'
            f'<circle cx="0" cy="-22" r="17"/>'
            f'<path d="M0-5v52M0 22h20M0 40h14"/></g>')

def cat(x, y, s=1, fill='#9aa7b1'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-84 0q-16-56 26-66 44-10 72 8t46 58z" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M-84 0q-44-8-34-48" fill="none" stroke="{fill}" stroke-width="15" stroke-linecap="round"/>'
            f'<path d="M-74-52q-20-14-6-40 16-24 40-10 24 14 10 42z" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M-56-88l-4-30 24 20zM-18-92l6-30 18 26z" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="-46" cy="-62" r="4" class="ink"/><circle cx="-24" cy="-64" r="4" class="ink"/>'
            f'<path d="M-40-48q4 6 10 0" fill="none" stroke="{INK}" stroke-width="2.5"/></g>')

def frog(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse rx="48" ry="32" class="green o"/>'
            f'<circle cx="-28" cy="-32" r="19" class="green o"/><circle cx="28" cy="-32" r="19" class="green o"/>'
            f'<circle cx="-28" cy="-38" r="6" class="ink"/><circle cx="28" cy="-38" r="6" class="ink"/>'
            f'<path d="M-46 8q46 30 92 0" fill="none" stroke="{GRND}" stroke-width="3"/>'
            f'<path d="M-48 30q-4 22-22 26M48 30q4 22 22 26" fill="none" stroke="{GRND}" stroke-width="8" stroke-linecap="round"/></g>')

def bird(x, y, s=1, cls='blue', dash=False):
    d = ' stroke-dasharray="8 8"' if dash else ''
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{INK}" stroke-width="2.5"{d}>'
            f'<path d="M-34 0q34-26 68 0-30 20-68 0z" class="{cls}"/>'
            f'<path d="M-6-6q10-34 46-40-4 30-26 42z" class="bluep"/>'
            f'<path d="M-2 8q-6 22-30 30 2-24 16-32z" class="{cls}"/>'
            f'<path d="M32-6l24-9-24-9z" fill="{CRL}" stroke="{CRL}"/></g>')

# --- 絵 ---------------------------------------------------------------------

add('egg', 'フライパンの上で焼けている目玉焼きと、となりに置かれた殻つきの卵',
    '卵＝egg。白身と黄身に分かれた目玉焼きが卵そのもの。', f'''
<g transform="translate(280 196)">
  <ellipse rx="152" ry="98" fill="#6b7680" class="o"/>
  <ellipse rx="136" ry="84" fill="#39424c"/>
  <path d="M34-8q-16-26-58-24-48 4-58 34-8 26 34 30 60 6 82-40z" fill="#fffefd" class="o"/>
  <circle cx="12" cy="-2" r="30" class="gold o"/>
  <circle cx="4" cy="-12" r="9" fill="#fff3c4"/>
</g>
<path d="M432 196h118" fill="none" stroke="#6b7680" stroke-width="26" stroke-linecap="round"/>
<ellipse cx="120" cy="306" rx="30" ry="38" fill="#fffefd" class="o"/>
<path d="M96 282q12-16 26-18" fill="none" stroke="{MUTED}" stroke-width="3"/>
<path d="M60 386h480" class="a"/>''')

add('eight', '木のテーブルの上に、金色の丸いコインが8つ並んでいる',
    '8＝eight。', f'''
{table(300)}
{counters(8)}
<path d="M60 386h480" class="a"/>''')

add('eighteen', '10のまとまりの棒が1本と、ばらのコインが8つ並んでいる',
    '18＝eighteen。10と8に分けて数える。', f'''
{table(300)}
{tens_ones(1, 8)}
<path d="M60 386h480" class="a"/>''')

add('eighth', '8段の階段を上りきったところに立ち、旗のそばで両手を上げている',
    '8番目の＝eighth。順番の8つめ。', f'''
{stair(8)}
''')

add('eighty', '10のまとまりの棒が8本、テーブルの上に並んでいる',
    '80＝eighty。10が8つ分。', f'''
{table(300)}
{rods(8)}
<path d="M60 386h480" class="a"/>''')

add('eleven', '10のまとまりの棒が1本と、ばらのコインが1つ置かれている',
    '11＝eleven。10と1。', f'''
{table(300)}
{tens_ones(1, 1)}
<path d="M60 386h480" class="a"/>''')

add('eleventh', '11段の階段を上りきったところに立ち、旗のそばで両手を上げている',
    '11番目の＝eleventh。順番の11番め。', f'''
{stair(11)}
''')

add('else', '棚に並んだ3つの箱を前に、1つの箱を丸で囲み、そこへ点線の矢印がのびている',
    'ほかのもの・別の＝else。なにか else で別のものを指す。', f'''
{shelf(300, 250, 330)}
{box(196, 214, 76, 60, 20, 'teal')}
{box(300, 214, 76, 60, 20, 'violet')}
{box(404, 214, 76, 60, 20, 'coral')}
{ring(404, 214, 62, False, 'coral')}
{person(110, 356, 1.05, 1, 'green', 'blue', 'point', 'short', 'smile')}
{arc(200, 148, 396, 148, 66, MUTED, True, 4)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('email', 'ノートパソコンの画面へ封筒が飛んでいくところ',
    '電子メール＝email。メールを送る動詞にもなる。', f'''
{table(330)}
<g transform="translate(410 330)">
  <path d="M-140 0h280l26 26h-332z" fill="#c3cbd1" class="o"/>
  <path d="M-110 0v-150h220V0z" fill="#5a6773" class="o"/>
  <path d="M-96-14v-122h192v122z" fill="#e1edfb" class="o"/>
</g>
<g transform="rotate(-12 200 180)">{letter(200, 180, 1.1, 'gold')}</g>
{arc(232, 214, 348, 254, 86, MUTED, True, 4)}
{spark(140, 120, 0.9)}''', arrow=True)

add('empathy', '悲しそうな人に寄り添って肩へ手を添え、二人の間にハートが浮かんでいる',
    '共感・思いやり＝empathy。相手の気持ちを自分のことのように感じること。', f'''
{person(206, 356, 1.1, 1, 'blue', 'blue', 'stand', 'bob', 'sad')}
{person(364, 358, 1.05, -1, 'coral', 'violet', 'give', 'short', 'smile')}
{heart(288, 190, 0.95, 'coral')}
{ring(288, 188, 66, True)}
<path d="M60 386h480" class="a"/>''')

add('employees', '会社の前に並んだ3人が、胸に社員証をつけている',
    '従業員・社員＝employees。雇われて働く人たち。', f'''
{building(440, 330, 1.05, 'teal')}
{''.join(person(118 + i * 92, 358 - (i % 2) * 8, 0.92, 1, c, 'blue', 'stand', h, 'smile')
         for i, (c, h) in enumerate([('coral', 'short'), ('violet', 'bob'), ('gold', 'bun')]))}
{''.join(f'<rect x="{110 + i * 92}" y="{292 - (i % 2) * 8}" width="18" height="24" rx="3" class="paper"/>'
         for i in range(3))}
<path d="M60 386h480" class="a"/>''')

add('end', '道が遮断機で行き止まりになり、終点の旗が立っている',
    '終わり・端＝end。道が終わる場所。', f'''
<path d="M-20 356L200 246h200l200 110z" fill="#e8e2d4" class="o"/>
{''.join(f'<path d="M300 {268 + i * 26}v20" stroke="#fffefd" stroke-width="7" stroke-dasharray="10 8" fill="none"/>'
         for i in range(3))}
<g transform="translate(300 246)">
  <path d="M-250 0h500v26h-500z" fill="#fffefd" class="o"/>
  <path d="M-230-4h70l-34 34h-70zM-90-4h70l-34 34h-70zM50-4h70l-34 34h-70zM150-4h70l-34 34h-70z" class="coral o"/>
  <path d="M-232 26v44M232 26v44" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
</g>
{flagpole(536, 220, 88)}
<path d="M60 386h480" class="a"/>''')

add('enjoy', 'いすに腰かけて飲み物を手にし、目を細めてくつろいでいる',
    '楽しむ・満喫する＝enjoy。', f'''
{sit(238, 352, 1.2, 1, 'teal', 'blue', 'bob', 'smile', 'lap')}
<ellipse cx="404" cy="300" rx="64" ry="18" class="paper"/>
<path d="M404 310v52" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
{tumbler(404, 286, 46, 64, 0.7, 'coral')}
{sun(520, 116, 44)}
{spark(432, 196, 1.2)}
{spark(120, 170, 0.9)}''')

add('enough', '瓶が点線のところまでちょうど満たされ、となりに緑のチェックがある',
    '十分な・十分に＝enough。足りている状態。', f'''
{jar(300, 330, 1.15, 0.84, 'teal')}
<path d="M242 240h116" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"/>
{tick(520, 150, 1.2)}
<path d="M60 386h480" class="a"/>''')

add('evening', '山の向こうに沈みかけた太陽、灯りのついた家、ともった街灯',
    '夕方・晩＝evening。日が沈むころ。', f'''
{sun(430, 196, 48)}
<path d="M-20 306q140-84 300-26 160 58 340-30v150H-20z" class="greenp o"/>
{house(180, 330, 0.9, 'coral')}
<circle cx="470" cy="196" r="54" fill="#fff0c5"/>
<g transform="translate(470 352)">
  <path d="M0 0v-172" fill="none" stroke="#6b7680" stroke-width="10"/>
  <path d="M-32-172h64l-16-30h-32z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>''')

add('ever', '左にのびた時間の軸に過去の出来事が並び、右端の時計へ点線が弧を描いている',
    '今までに・かつて＝ever。これまでに一度でも、という意味。', f'''
{''.join(f'<circle cx="{90 + i * 96}" cy="300" r="12" class="blue"/>' for i in range(4))}
<path d="M40 300h420" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>
{clock(520, 218, 60, 10, 2)}
{arc(70, 282, 466, 224, 96, VIO, True, 4)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('every', 'カレンダーの升目すべてにチェックが入り、上の繰り返し矢印が回っている',
    '毎〜・すべての＝every。どの一つにも当てはまる。', f'''
{''.join(f'<rect x="{56 + (i % 7) * 70}" y="{104 + (i // 7) * 62}" width="54" height="46" rx="8" class="paper"/>' for i in range(21))}
{''.join(tick(83 + (i % 7) * 70, 128 + (i // 7) * 62, 0.42) for i in range(21))}
<path d="M36 84q264-70 528 0" fill="none" stroke="{VIO}" stroke-width="5" stroke-dasharray="10 9" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>''', arrow=True)

add('everybody', '広場にたくさんの人が集まり、何人かは両手を上げている',
    'みんな・だれでも＝everybody。その場の全員。', f'''
{tree(524, 300, 1.1)}
{person(120, 300, 0.72, 1, 'violet', 'blue', 'up', 'bun', 'smile')}
{person(232, 296, 0.7, 1, 'gold', 'blue', 'stand', 'short', 'smile')}
{person(344, 300, 0.72, -1, 'blue', 'blue', 'up', 'short', 'smile')}
{person(178, 358, 1.0, 1, 'coral', 'violet', 'up', 'bob', 'smile')}
{person(310, 352, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(444, 358, 1.0, -1, 'green', 'blue', 'up', 'bun', 'smile')}
<path d="M60 386h480" class="a"/>''')

add('everyone', '広間の座席にたくさんの人が並んで座り、前を見ている',
    'みんな・だれでも＝everyone。everybody とほぼ同じ。', f'''
<path d="M0 130h600v270H0z" fill="#f5f1fb"/>
<path d="M0 296h600v104H0z" fill="#e7e2f2"/>
<path d="M300 6l-200 200h400z" fill="#fff0c5"/>
{''.join(head(70 + i * 118, 132, 20, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('coral', 'bob'), ('gold', 'bun'), ('violet', 'short'), ('blue', 'bob')]))}
{''.join(head(122 + i * 118, 216, 24, c, h) for i, (c, h) in enumerate([('gold', 'bun'), ('teal', 'short'), ('blue', 'bob'), ('coral', 'short'), ('violet', 'bun')]))}
{''.join(head(66 + i * 118, 292, 30, c, h) for i, (c, h) in enumerate([('violet', 'bob'), ('green', 'short'), ('coral', 'bun'), ('teal', 'bob'), ('gold', 'short')]))}
''', ground=False)

add('everything', 'テーブルの上に、本・コップ・箱・花・紙などいろいろな物がのっている',
    'すべてのこと・何もかも＝everything。', f'''
{table(320)}
{book(150, 266, 0.85, 'teal')}
{tumbler(252, 320, 52, 74, 0.7)}
{box(344, 290, 76, 60, 20, 'gold')}
{flower(432, 280, 0.85, 'coral')}
{doc(524, 262, 92, 116, 3)}
<path d="M60 386h480" class="a"/>''')

add('exam', '机に向かって答案用紙に書き込み、壁の時計が時間を刻んでいる',
    '試験・テスト＝exam。', f'''
{sit(170, 320, 1.15, 1, 'blue', 'blue', 'short', 'neutral', 'lap')}
<g transform="translate(392 300)">
  <path d="M-150 0h300v22h-300z" fill="#c9a464" class="o"/>
  <path d="M-132 22v72M132 22v72" fill="none" stroke="#a0764a" stroke-width="12" stroke-linecap="round"/>
</g>
{doc(400, 254, 132, 86, 3)}
<path d="M470 232l52-42" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
{clock(516, 116, 48, 2, 10)}
<path d="M60 386h480" class="a"/>''')

add('example', '板の前に立ち、4つ並んだ丸のうち1つを指し棒で指している',
    '例・実例＝example。代表として示すもの。', f'''
<g transform="translate(372 200)">
  <path d="M-172-116h344v232h-344z" fill="#fffefd" class="o"/>
  {''.join(f'<circle cx="{-102 + i * 70}" cy="-14" r="26" class="{c} o"/>' for i, c in enumerate(['blue', 'teal', 'violet', 'gold']))}
  {ring(-32, -14, 46, False, 'coral')}
</g>
{person(140, 356, 1.05, 1, 'green', 'blue', 'point', 'short', 'smile')}
<path d="M60 386h480" class="a"/>''')

add('excited', '両足を地面から離して飛び上がり、両手を上げて目を丸くしている',
    'わくわくした・興奮した＝excited。人が感じる側。', f'''
{person(300, 284, 1.2, 1, 'coral', 'blue', 'up', 'bob', 'surprised')}
{spark(150, 132, 0.8)}
{spark(190, 176, 0.8)}
{spark(468, 122, 0.9)}
{spark(430, 168, 0.9)}
{''.join(f'<path d="M{196 + i * 42} 328h30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>' for i in range(5))}''')

add('exciting', 'ジェットコースターが急な下り坂を滑り降り、後ろに速さの線がのびている',
    'わくわくさせる・刺激的な＝exciting。物事が人を興奮させる側。', f'''
<path d="M30 96q140-56 210 34 60 76 130 106 76 32 200 6" fill="none" stroke="{INK}" stroke-width="9"/>
<path d="M180 148v190M340 236v120M470 288v78" fill="none" stroke="{MUTED}" stroke-width="7"/>
{''.join(f'<path d="M{132 + i * 26} {150 + i * 34}h-84" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
<g transform="translate(316 226) rotate(26)">
  <path d="M-74-28h148v56h-148z" class="coral o"/>
  <circle cx="-44" cy="32" r="13" class="ink"/><circle cx="44" cy="32" r="13" class="ink"/>
</g>
{head(292, 178, 18, 'teal', 'short')}
{head(354, 186, 18, 'gold', 'bob')}
''', ground=False)

add('explain', '図の前に立ち、指し棒で1つの箱を指して説明している',
    '説明する・解説する＝explain。', f'''
<g transform="translate(384 196)">
  <path d="M-172-112h344v224h-344z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="{-134 + i * 100}" y="-66" width="72" height="56" rx="10" class="{c}p o"/>' for i, c in enumerate(['blue', 'teal', 'violet']))}
  {''.join(f'<path d="M{-62 + i * 100} -38h34" fill="none" stroke="{INK}" stroke-width="5" marker-end="url(#ar)"/>' for i in range(2))}
</g>
{person(150, 356, 1.05, 1, 'teal', 'blue', 'point', 'short', 'smile')}
{arc(212, 268, 264, 216, 40, MUTED, True, 4)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('extension cord', '壁のコンセントから長いコードがのび、たわんで離れたランプにつながる',
    '延長コード＝extension cord。', f'''
<g transform="translate(66 214)">
  <path d="M-42-48h84v96h-84z" class="paper"/>
  <path d="M-14-32h28v13h-28zM-14 6h28v13h-28z" fill="{INK}"/>
</g>
<path d="M108 200q56 66 118 24 62-42 112 18 40 44 88 8" fill="none" stroke="{VIO}" stroke-width="12" stroke-linecap="round"/>
<path d="M186 322q-24-30 4-46 26-14 22 20" fill="none" stroke="{VIO}" stroke-width="11" stroke-linecap="round"/>
<path d="M400 300l-40 80h240l-40-80z" fill="#fff0c5"/>
<g transform="translate(470 326)">
  <path d="M-72 0h144v18h-144z" fill="#c3cbd1" class="o"/>
  <path d="M-6 0v-92" fill="none" stroke="#8a97a3" stroke-width="10"/>
  <path d="M-72-92h144l-32-62h-80z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>''')

add('eye', 'まぶた・虹彩・瞳が大きく描かれた目のクローズアップ',
    '目・視線＝eye。', f'''
<g transform="translate(300 208)">
  <path d="M-180 0q180-142 360 0-180 142-360 0z" fill="#fffefd" class="o"/>
  <circle r="64" class="bluep o"/>
  <circle r="28" class="ink"/>
  <circle cx="-22" cy="-24" r="11" fill="#fffdf6"/>
  <path d="M-180 0q180-142 360 0" fill="none" stroke="{INK}" stroke-width="5"/>
  {''.join(f'<path d="M{-56 + i * 38} -44l{-10 + i * 8} -46" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>' for i in range(4))}
  <path d="M-160-88q160-74 320 0" fill="none" stroke="{HAIR}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>''')

add('fact', '書類を虫めがねでのぞき、緑のチェックがついている',
    '事実・実際のこと＝fact。確かめられたこと。', f'''
{doc(300, 196, 200, 240, 5)}
{lens(392, 250, 58)}
{tick(126, 130, 1.6)}
<path d="M60 386h480" class="a"/>''')

add('family', '家の前に、大人と子どもが手をつないで並んでいる',
    '家族・一家＝family。', f'''
{house(504, 300, 0.85, 'coral')}
{person(120, 356, 1.05, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
{person(230, 356, 1.05, 1, 'coral', 'violet', 'hold', 'bob', 'smile')}
{person(320, 356, 0.7, 1, 'gold', 'blue', 'hold', 'short', 'smile')}
{person(402, 356, 0.7, 1, 'violet', 'blue', 'hold', 'bun', 'smile')}
<path d="M60 386h480" class="a"/>''')

add('fan heater', '箱型のヒーターの前で手をかざし、温かい風の波が立ちのぼっている',
    'ファンヒーター＝fan heater。温風を送る暖房器具。', f'''
<g transform="translate(340 300)">
  <path d="M-100-70h200v140h-200z" fill="#eef2f4" class="o"/>
  {''.join(f'<rect x="-72" y="{-48 + j * 30}" width="144" height="16" rx="8" class="gold o"/>' for j in range(4))}
</g>
{''.join(f'<path d="M{310 + i * 30} 212q-16-24 0-40t0-40" fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
{person(140, 356, 1.1, 1, 'violet', 'blue', 'give', 'bob', 'smile')}
<path d="M60 386h480" class="a"/>''')

add('faraway', '岸から手をかざして遠くを見ており、水平線の先に小さな島が浮かんでいる',
    '遠くの・遠い＝faraway。', f'''
<path d="M0 230h600v176H0z" fill="#dbeaf8"/>
<ellipse cx="500" cy="240" rx="58" ry="12" class="greenp o"/>
<g transform="translate(500 240)"><path d="M0 0v-56" fill="none" stroke="#8b6437" stroke-width="7"/>{tree(0, 0, 0.45)}</g>
{''.join(f'<path d="M{24 + i * 80} {296 + (i % 2) * 30}q20-14 40 0" fill="none" stroke="{BLU}" stroke-width="4"/>' for i in range(7))}
<path d="M0 320q160-46 300-16 140 30 300-30v126H0z" fill="#e1f3e5" class="o"/>
{person(180, 356, 1.1, 1, 'teal', 'blue', 'point', 'short', 'smile')}
{arc(236, 254, 470, 236, 46, MUTED, True, 4)}''', arrow=True)

add('fast', '車が道を猛スピードで走り、後ろに長い速度線が何本ものびている',
    '速い・速く＝fast。', f'''
<g transform="translate(348 294)">
  <path d="M-150 0q-12-46 34-52l34-36h84l40 36h28q30 8 28 52z" class="coral o"/>
  <path d="M-66-88h70v36h-100z" class="bluep o"/>
  <circle cx="-92" cy="6" r="26" fill="#3f4a55" class="o"/><circle cx="94" cy="6" r="26" fill="#3f4a55" class="o"/>
  <circle cx="-92" cy="6" r="10" fill="#c3cbd1"/><circle cx="94" cy="6" r="10" fill="#c3cbd1"/>
</g>
{''.join(f'<path d="M40 {214 + i * 44}h150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
<path d="M60 386h480" class="a"/>''')

add('father', '赤ちゃんをベビーカーに乗せて、後ろから押している父親',
    '父・父親＝father。', f'''
{person(236, 356, 1.15, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
<path d="M256 306l-58 22" fill="none" stroke="#5a6773" stroke-width="10" stroke-linecap="round"/>
<g transform="translate(410 292)">
  <path d="M-90-18h180v44h-180z" class="blue o"/>
  <path d="M-90-18q6-60 90-60t90 60z" class="bluep o"/>
  <circle cx="-52" cy="44" r="24" fill="#3f4a55" class="o"/><circle cx="52" cy="44" r="20" fill="#3f4a55" class="o"/>
  <circle cx="-52" cy="44" r="9" fill="#c3cbd1"/><circle cx="52" cy="44" r="8" fill="#c3cbd1"/>
  <circle cx="0" cy="-30" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<path d="M60 386h480" class="a"/>''')

FAVORITE = f'''
{shelf(300, 250, 340)}
{box(196, 214, 76, 60, 20, 'blue')}
{box(404, 214, 76, 60, 20, 'violet')}
{box(300, 214, 76, 60, 20, 'gold')}
{ring(300, 212, 66, False, 'coral')}
{heart(300, 110, 0.85)}
<path d="M60 386h480" class="a"/>'''

add('favorite', '棚に並んだ3つの箱のうち真ん中だけが丸で囲まれ、上にハートが浮かんでいる',
    'お気に入りの＝favorite。', FAVORITE)

add('favourite', '棚に並んだ3つの箱のうち真ん中だけが丸で囲まれ、上にハートが浮かんでいる',
    'お気に入りの＝favourite。favorite のイギリス綴り。', FAVORITE)

add('feeling', '胸のあたりにハートが浮かび、うれしそうな顔をした人',
    '気持ち・感情＝feeling。', f'''
{person(300, 356, 1.2, 1, 'violet', 'blue', 'hold', 'bob', 'smile')}
{heart(300, 246, 0.75, 'coral')}
{ring(300, 242, 58, True)}
{spark(158, 176, 0.9)}
{spark(444, 176, 0.9)}''')

add('festival', '屋台の提灯と花火、集まった人たちでにぎわう祭り',
    '祭り・音楽祭＝festival。', f'''
<g transform="translate(190 330)">
  <path d="M-110 0v-96h220V0z" fill="#fffdf6" class="o"/>
  <path d="M-130-96h260l-34-44h-192z" class="coral o"/>
  {''.join(f'<path d="M{-126 + i * 52} -96h30v-16h-30z" class="goldp o"/>' for i in range(5))}
  {''.join(f'<path d="M{-70 + i * 70} 0v-96" fill="none" stroke="{INK}" stroke-width="4"/>' for i in range(3))}
</g>
{''.join(f'<g transform="translate({112 + i * 92} 138)"><path d="M0 0v36" fill="none" stroke="{INK}" stroke-width="3"/><ellipse cy="62" rx="20" ry="24" class="gold o"/></g>' for i in range(3))}
<g stroke="{VIO}" stroke-width="4" fill="none">
  {''.join(f'<path d="M{440 + 60 * math.cos(math.radians(a)):.0f} {76 + 60 * math.sin(math.radians(a)):.0f}L{440 + 92 * math.cos(math.radians(a)):.0f} {76 + 92 * math.sin(math.radians(a)):.0f}"/>' for a in range(0, 360, 45))}
</g>
{person(430, 358, 0.95, 1, 'violet', 'blue', 'up', 'bob', 'smile')}
{person(524, 356, 0.9, -1, 'gold', 'blue', 'up', 'short', 'smile')}
<path d="M60 386h480" class="a"/>''')

add('fetch', '投げたボールをくわえて、犬が飼い主のところへ走ってくる',
    '取ってくる・連れてくる＝fetch。行って持って帰ってくる。', f'''
{person(140, 356, 1.1, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{beast(372, 328, 0.55, '#8a6a46', -1)}
<circle cx="278" cy="298" r="15" class="coral o"/>
{arc(300, 262, 168, 250, 70, MUTED, True, 4)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('few', '8つ並んだ区切りのうち、硬貨が入っているのは3つだけ',
    '少しの・少数の＝few。数えられるものに使う。', f'''
{''.join(f'<rect x="{72 + i * 62}" y="258" width="48" height="48" rx="10" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>' for i in range(8))}
{''.join(coin(96 + i * 62, 282, 19) for i in range(3))}
<path d="M60 386h480" class="a"/>''')

add('fifteen', '10のまとまりの棒が1本と、ばらのコインが5つ並んでいる',
    '15＝fifteen。10と5。', f'''
{table(300)}
{tens_ones(1, 5)}
<path d="M60 386h480" class="a"/>''')

add('fifth', '5段の階段を上りきったところに立ち、旗のそばで両手を上げている',
    '5番目の＝fifth。順番の5つめ。', f'''
{stair(5)}
''')

add('fifty', '10のまとまりの棒が5本、テーブルの上に並んでいる',
    '50＝fifty。10が5つ分。', f'''
{table(300)}
{rods(5)}
<path d="M60 386h480" class="a"/>''')

add('fill', '水差しから瓶へ水が注がれ、瓶がいっぱいになっていく',
    'いっぱいにする・満たす＝fill。', f'''
<g transform="translate(250 138) rotate(34)">
  <path d="M-54-46h108v92h-108z" class="blue o"/>
  <path d="M-54-46q-34 46 0 92" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M54-30l42 12-42 12z" class="blue o"/>
</g>
<path d="M304 178q14 60-24 106" fill="none" stroke="{BLU}" stroke-width="9" stroke-dasharray="14 10" marker-end="url(#ar)"/>
{jar(400, 340, 1.15, 0.66, 'blue')}
{''.join(f'<path d="M{286 + i * 34} 250q-6 12 0 20" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>' for i in range(2))}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('find', '草むらを虫めがねでのぞいて、落ちていた鍵を見つけている',
    '見つける＝find。さがして見つける。', f'''
{''.join(f'<path d="M{56 + i * 62} 356q-8-30 6-44" fill="none" stroke="{GRN}" stroke-width="5" stroke-linecap="round"/>' for i in range(9))}
{key_(352, 306, 1.15)}
{lens(352, 246, 56)}
{spark(430, 250, 1.0)}
{person(158, 356, 1.15, 1, 'blue', 'blue', 'point', 'cap', 'smile')}
<path d="M60 386h480" class="a"/>''')

add('fire station', '大きな車庫の前に、はしごを積んだ消防車が止まっている消防署',
    '消防署＝fire station。', f'''
<g transform="translate(166 320)">
  <path d="M-140 0v-140h280V0z" fill="#fffdf6" class="o"/>
  <path d="M-156-140L0-238l156 98z" class="coral o"/>
  <path d="M-104 0v-112h208V0z" fill="#e4eaee" class="o"/>
  {''.join(f'<path d="M{-104 + i * 42} 0v-112" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(6))}
  <path d="M-104-112h208" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g transform="translate(438 300)">
  <path d="M-150-72h204v72h-204z" class="coral o"/>
  <path d="M54-48h70v48h-70z" class="coral o"/>
  <circle cx="-100" cy="6" r="24" fill="#3f4a55" class="o"/><circle cx="76" cy="6" r="24" fill="#3f4a55" class="o"/>
  <circle cx="-100" cy="6" r="9" fill="#c3cbd1"/><circle cx="76" cy="6" r="9" fill="#c3cbd1"/>
  <path d="M-138-92l96-72" fill="none" stroke="#c9a464" stroke-width="12" stroke-linecap="round"/>
  {''.join(f'<path d="M{-128 + i * 24} {-84 + i * 18}l20-10" fill="none" stroke="#c9a464" stroke-width="7" stroke-linecap="round"/>' for i in range(5))}
</g>
<path d="M60 386h480" class="a"/>''')

add('fisherman', '桟橋に立って釣り糸をたらし、魚がかかっている',
    '漁師・釣り人＝fisherman。', f'''
<path d="M0 246h600v154H0z" fill="#dbeaf8"/>
{''.join(f'<path d="M{20 + i * 78} {292 + (i % 2) * 28}q20-14 40 0" fill="none" stroke="{BLU}" stroke-width="4"/>' for i in range(7))}
<path d="M-20 300h300v18H-20z" fill="#c9a464" class="o"/>
<path d="M20 318v66M240 318v66" fill="none" stroke="#a0764a" stroke-width="12" stroke-linecap="round"/>
{person(150, 300, 1.05, 1, 'gold', 'blue', 'point', 'cap', 'smile')}
<path d="M226 236l96 30" fill="none" stroke="#6b7680" stroke-width="8" stroke-linecap="round"/>
<path d="M322 266q6 60 98 46" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(430 300)">
  <path d="M-46 0q46-30 92 0-46 30-92 0z" class="blue o"/>
  <path d="M-46 0l-30-18 4 22-4 18 30-18z" class="blue o"/>
  <circle cx="24" cy="-6" r="4" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>''')

add('five', '木のテーブルの上に、金色の丸いコインが5つ並んでいる',
    '5＝five。', f'''
{table(300)}
{counters(5)}
<path d="M60 386h480" class="a"/>''')

add('flip-flops', '砂浜にビーチサンダルが左右一足、脱ぎ置かれている',
    'ビーチサンダル＝flip-flops。', f'''
<path d="M0 330h600v70H0z" fill="#f2e4bc"/>
<g transform="translate(238 300) rotate(-10)">
  <ellipse rx="44" ry="76" class="coral o"/>
  <path d="M-8-56l-26 22M-8-56l26 22" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
<g transform="translate(392 306) rotate(8)">
  <ellipse rx="44" ry="76" class="coral o"/>
  <path d="M-8-56l-26 22M-8-56l26 22" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
{sun(520, 116, 44)}
<ellipse cx="130" cy="352" rx="18" ry="12" fill="#fffefd" class="o"/>''')

add('floor', '板張りの床にラグとボールが置かれ、奥の壁には窓がある',
    '床＝floor。建物の階の意味にもなる。', f'''
<path d="M0 0h600v156H0z" fill="#f4eee2"/>
<path d="M0 156h600v244H0z" fill="#f9f3e6"/>
{''.join(f'<path d="M0 {182 + i * 34}h600" fill="none" stroke="#dccdb0" stroke-width="4"/>' for i in range(7))}
<path d="M0 156h600" fill="none" stroke="{INK}" stroke-width="6"/>
<g transform="translate(440 84)">
  <path d="M-74-70h148v106h-148z" fill="#e1edfb" class="o"/>
  <path d="M0-70v106M-74-22h148" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g transform="translate(150 322)">
  <ellipse rx="104" ry="40" class="coralp o"/>
  <ellipse rx="66" ry="22" fill="none" stroke="{CRL}" stroke-width="3"/>
</g>
{soccer(404, 336, 28)}
<path d="M60 386h480" class="a"/>''', ground=False)

add('flower', '植木鉢から3本の花が咲き、蜂が近づいている',
    '花・草花＝flower。', f'''
{pot(300, 356, 132, 84, 'coral')}
{''.join(f'<g transform="translate({226 + i * 74} 232)">{flower(0, 0, 0.95, c)}</g>' for i, c in enumerate(['coral', 'gold', 'violet']))}
<g transform="translate(470 176)">
  <ellipse rx="18" ry="12" class="gold o" transform="rotate(-24)"/>
  <ellipse cx="-4" cy="-18" rx="16" ry="10" class="goldp o"/>
  <ellipse cx="-4" cy="18" rx="16" ry="10" class="goldp o"/>
  <path d="M-18 0h-24" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<path d="M60 386h480" class="a"/>''')

add('follow', '前を歩く人を、もう一人があとから同じ道について歩いている',
    'ついていく・従う＝follow。', f'''
{person(128, 356, 1.05, 1, 'coral', 'blue', 'walk', 'bob', 'smile')}
{person(336, 356, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{''.join(f'<ellipse cx="{214 + i * 46}" cy="{344 - (i % 2) * 12}" rx="15" ry="9" fill="{MUTED}"/>' for i in range(2))}
{arc(200, 258, 300, 258, 44, MUTED, True, 4)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('food', 'テーブルに皿とスープの器、パン、飲み物が並んでいる',
    '食べ物・食事＝food。', f'''
{table(310)}
<g transform="translate(176 286)">
  <ellipse rx="96" ry="26" class="paper"/>
  <ellipse rx="66" ry="16" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-40-14q40-24 80 0-40 20-80 0z" class="coral o"/>
</g>
<g transform="translate(340 276)">
  <path d="M-56-24h112l-16 60h-80z" fill="#e1edfb" class="o"/>
  <ellipse cy="-24" rx="56" ry="14" class="bluep o"/>
</g>
<g transform="translate(470 306)">
  <path d="M-54 0q-6-46 54-46t54 46z" class="goldp o"/>
  <path d="M-30-30l24 16M4-40l20 22M30-30l14 18" fill="none" stroke="{GLDD}" stroke-width="3"/>
</g>
{tumbler(546, 310, 44, 64, 0.7)}
<path d="M60 386h480" class="a"/>''')

add('food processor', 'フードプロセッサーの容器に野菜が落ち、中の刃が回っている',
    'フードプロセッサー＝food processor。食材を刻む調理器具。', f'''
<g transform="translate(344 320)">
  <path d="M-92-56h184v56h-184z" class="blue o"/>
  {''.join(f'<circle cx="{-54 + i * 36}" cy="-28" r="12" class="bluep o"/>' for i in range(4))}
  <path d="M-72-56v-108h144v108z" fill="#eaf4fb" class="o"/>
  <path d="M-72-164h144l-10-30h-124z" class="bluep o"/>
  <path d="M0-108v-46M-32-154h64l-32 42z" class="gold o"/>
</g>
{''.join(f'<circle cx="{286 + i * 42}" cy="{106 + (i % 2) * 22}" r="21" class="{c} o"/>' for i, c in enumerate(['coral', 'gold', 'green', 'coral']))}
{arc(300, 122, 336, 176, 40, MUTED, True, 4)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('foot', 'かかとから足指までの裸足と、となりに点線で描いた足あと',
    '足＝foot。くるぶしから下の部分。', f'''
<g transform="translate(260 290)">
  <path d="M-44-160q-24 66-24 108 0 54 62 54 42 0 62-32 14-24 42-26 22-2 22-18t-24-16q-42 0-74-26-32-26-46-44z" fill="{SKIN}" class="o"/>
  <ellipse cx="86" cy="66" rx="14" ry="10" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="56" cy="70" rx="12" ry="9" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <ellipse cx="26" cy="72" rx="10" ry="8" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8">
  <path d="M430 130q-24 66-24 108 0 54 62 54 42 0 62-32 14-24 42-26"/>
</g>
<path d="M60 386h480" class="a"/>''')

add('football', 'サッカーボールがゴールネットへ向かって飛んでいく',
    'サッカー（英）・フットボール＝football。', f'''
<g transform="translate(470 296)">
  <path d="M-96 0v-132h192V0" fill="none" stroke="#fffefd" stroke-width="13"/>
  <path d="M-96 0v-132h192V0" fill="none" stroke="{INK}" stroke-width="5"/>
  {''.join(f'<path d="M{-72 + i * 36} -132v132M-96 {-108 + j * 36}h192" fill="none" stroke="{MUTED}" stroke-width="2"/>' for i in range(5) for j in range(1, 4))}
</g>
{person(104, 356, 1.1, 1, 'teal', 'blue', 'point', 'short', 'smile')}
{soccer(244, 306, 40)}
{arc(300, 286, 388, 262, 56, MUTED, True, 4)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('for', '雨の中で、片方の人がもう片方に傘をさしかけている',
    '〜のために＝for。だれかのためにする場面。', f'''
{''.join(f'<path d="M{56 + i * 74} {72 + (i % 3) * 58}v26" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>' for i in range(8))}
{person(238, 356, 1.05, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(332, 356, 0.95, 1, 'gold', 'violet', 'stand', 'bob', 'smile')}
{umbrella(296, 212, 1.0, 'coral')}
<path d="M60 386h480" class="a"/>''')

add('forget', 'ベンチに鍵を置き忘れて立ち去り、頭の上には鍵と×の吹き出し',
    '忘れる・忘れ物をする＝forget。', f'''
{plank(232, 330, 264, 18)}
<path d="M120 348v36M344 348v36" fill="none" stroke="#a0764a" stroke-width="10" stroke-linecap="round"/>
{key_(232, 302, 0.9)}
{person(452, 356, 1.1, 1, 'violet', 'blue', 'walk', 'short', 'smile')}
<g transform="translate(452 190)">{cloud(0, 0, 0.9, 'blue')}</g>
{key_(428, 178, 0.8)}
{cross(482, 178, 0.9)}
<path d="M60 386h480" class="a"/>''')

add('forty', '10のまとまりの棒が4本、テーブルの上に並んでいる',
    '40＝forty。10が4つ分。', f'''
{table(300)}
{rods(4)}
<path d="M60 386h480" class="a"/>''')

add('forwards', '体を前に向けて歩き、進む先へ大きな矢印がのびている',
    '前方へ・前へ＝forwards。進む向き。', f'''
{person(276, 356, 1.15, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{''.join(f'<path d="M{84 + i * 42} {300 + i * 26}h-58" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
{arrowline([(340, 236), (524, 236)], CRL, 8)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('four', '木のテーブルの上に、金色の丸いコインが4つ並んでいる',
    '4＝four。', f'''
{table(300)}
{counters(4)}
<path d="M60 386h480" class="a"/>''')

add('fourteen', '10のまとまりの棒が1本と、ばらのコインが4つ並んでいる',
    '14＝fourteen。10と4。', f'''
{table(300)}
{tens_ones(1, 4)}
<path d="M60 386h480" class="a"/>''')

add('fourth', '4段の階段を上りきったところに立ち、旗のそばで両手を上げている',
    '4番目の＝fourth。順番の4つめ。', f'''
{stair(4)}
''')

add('friend', '肩を組み合って並び、いっしょに笑っている二人',
    '友だち・友人＝friend。', f'''
{person(206, 356, 1.15, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
{person(360, 356, 1.15, -1, 'coral', 'violet', 'hold', 'bob', 'smile')}
<path d="M232 268q92-46 152 0" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
{heart(300, 152, 0.7)}
<path d="M60 386h480" class="a"/>''')

add('friendly', '笑顔で手のひらを見せて手を差し出し、そばにハートが浮かんでいる',
    '友好的な・親切な＝friendly。', f'''
{person(258, 356, 1.15, 1, 'green', 'blue', 'give', 'short', 'smile')}
{hand(372, 278, 1)}
{heart(486, 216, 0.7)}
{spark(160, 176, 0.9)}
<path d="M60 386h480" class="a"/>''')

add('from', '左手前の家が点線の丸で囲まれ、封書がもう一方の家へ飛んでいく',
    '〜から＝from。出発点・起点を表す。', f'''
{house(120, 300, 0.9, 'teal')}
{ring(120, 234, 98, True)}
{letter(300, 190, 1.1, 'gold')}
{arc(232, 214, 404, 214, 66, MUTED, True, 4)}
{house(520, 300, 0.9, 'violet')}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('front', '正面から見た家。玄関へ続く道があり、手前に車が止まっている',
    '前・前面＝front。建物の正面。', f'''
{house(320, 300, 1.25, 'coral')}
<path d="M252 400l28-100h80l28 100z" fill="#e8e2d4" class="o"/>
{arrowline([(320, 392), (320, 336)], CRL, 7)}
<g transform="translate(96 340) scale(0.72)">
  <path d="M-150 0q-12-46 34-52l34-36h84l40 36h28q30 8 28 52z" class="blue o"/>
  <path d="M-66-88h70v36h-100z" class="bluep o"/>
  <circle cx="-92" cy="6" r="26" fill="#3f4a55" class="o"/><circle cx="94" cy="6" r="26" fill="#3f4a55" class="o"/>
</g>
<path d="M60 386h480" class="a"/>''', arrow=True)

add('fruit', 'かごにりんご・オレンジ・ぶどう・バナナが盛られている',
    '果物＝fruit。', f'''
<g transform="translate(300 296)">
  <path d="M-142-34h284l-26 78h-232z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-124 + i * 32} -34v78" fill="none" stroke="#a0764a" stroke-width="4"/>' for i in range(9))}
</g>
<circle cx="206" cy="248" r="40" class="coral o"/>
<path d="M206 208v-18" fill="none" stroke="{BRN}" stroke-width="6"/>
<path d="M206 200q22-16 34 0-22 12-34 0z" class="green o"/>
<circle cx="296" cy="240" r="36" class="gold o"/>
<g fill="none" stroke="{VIO}" stroke-width="4">
  {''.join(f'<circle cx="{374 + (i % 3 - 1) * 22}" cy="{256 + i // 3 * 22}" r="15" class="violet o"/>' for i in range(9))}
</g>
<path d="M420 250q52-46 84-4-30 40-84 4z" class="gold o"/>
<path d="M424 248q52-30 80-2" fill="none" stroke="{GLDD}" stroke-width="3"/>
<path d="M60 386h480" class="a"/>''')

add('full', 'グラスが縁までいっぱいで、水がこぼれ落ちている',
    'いっぱいの・満ちた＝full。入りきらないほど。', f'''
{tumbler(300, 322, 78, 108, 1.0)}
<ellipse cx="300" cy="330" rx="72" ry="14" class="bluep o"/>
{''.join(f'<path d="M{338 + i * 22} {244 + i * 14}q-8 14 0 22" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>' for i in range(2))}
<path d="M60 386h480" class="a"/>''')

add('funny', '体をそらして大笑いし、そばのびっくり箱から顔が飛び出している',
    'おかしい・笑える＝funny。', f'''
{person(198, 356, 1.2, 1, 'gold', 'blue', 'hold', 'bob', 'smile')}
{spark(104, 172, 0.8)}
{spark(140, 214, 0.8)}
<g transform="translate(430 326)">
  <path d="M-68-68h136v68h-136z" class="violet o"/>
  <path d="M-46-68q10-42 46-32t40 32" fill="none" stroke="{MUTED}" stroke-width="9"/>
</g>
{face(430, 184, 40, 'grin')}
<path d="M60 386h480" class="a"/>''')

add('game', 'テーブルをはさんで二人が盤に向かい、さいころを振って遊んでいる',
    'ゲーム・試合・遊び＝game。', f'''
{table(330)}
<g transform="translate(300 306) rotate(-7)">
  <path d="M-140-72h280v144h-280z" class="paper"/>
  {''.join(f'<path d="M{-140 + i * 35} -72v144" fill="none" stroke="{MUTED}" stroke-width="2"/>' for i in range(1, 8))}
  {''.join(f'<path d="M-140 {-72 + i * 36}h280" fill="none" stroke="{MUTED}" stroke-width="2"/>' for i in range(1, 4))}
  <circle cx="-70" cy="-36" r="14" class="teal o"/><circle cx="0" cy="0" r="14" class="coral o"/>
  <circle cx="70" cy="36" r="14" class="violet o"/><circle cx="-35" cy="36" r="14" class="gold o"/>
</g>
<g transform="translate(150 296)">
  <path d="M-24-24h48v48h-48z" class="paper"/>
  {''.join(f'<circle cx="{x}" cy="{y}" r="5" class="ink"/>' for x, y in [(-10, -10), (10, 10), (0, 0)])}
</g>
{person(112, 356, 1.0, 1, 'teal', 'blue', 'point', 'short', 'smile')}
{person(492, 356, 1.0, -1, 'coral', 'violet', 'point', 'bob', 'smile')}
<path d="M60 386h480" class="a"/>''')

add('garden', '柵で囲った庭に花が並び、じょうろと蝶がいる',
    '庭・庭園＝garden。', f'''
{''.join(f'<g transform="translate({40 + i * 58} 302)"><path d="M0 0v-72" fill="none" stroke="#c9a464" stroke-width="12"/><path d="M-14-56h28l-8-26h-12z" class="gold o"/></g>' for i in range(10))}
{''.join(f'<path d="M{40 + i * 58} -66h58" fill="none" stroke="#a0764a" stroke-width="8"/>' for i in range(9))}
{''.join(f'<g transform="translate({90 + i * 90} 348)">{flower(0, 0, 0.85, c)}</g>' for i, c in enumerate(['coral', 'gold', 'violet', 'coral']))}
<g transform="translate(510 316)">
  <path d="M-46-34h92v58h-92z" fill="#8a97a3" class="o"/>
  <path d="M46-24l52-30" fill="none" stroke="#8a97a3" stroke-width="12" stroke-linecap="round"/>
  <path d="M-46-34q-26 0-26-22" fill="none" stroke="#8a97a3" stroke-width="10" stroke-linecap="round"/>
</g>
<g transform="translate(430 200)">
  <ellipse rx="22" ry="16" class="violet o" transform="rotate(-30)"/>
  <ellipse rx="22" ry="16" class="violetp o" transform="rotate(30)"/>
  <path d="M0 0v18" fill="none" stroke="{INK}" stroke-width="3"/>
</g>''')

add('garment', 'ハンガーにかけた1着の衣服と、ぶら下がった値札',
    '衣服・衣類1点＝garment。', f'''
<path d="M180 96h240" fill="none" stroke="#8b6437" stroke-width="10" stroke-linecap="round"/>
<g transform="translate(300 250)">
  <path d="M0-108l-10-12q-16-22 10-22t10 22l-10 12" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-68-64L0-104l68 40" fill="none" stroke="#8b6437" stroke-width="10" stroke-linecap="round"/>
  <path d="M-52-60q52-26 104 0l26 44-38 22v72h-80v-72l-38-22z" class="coral o"/>
  <path d="M-30-56v132" fill="none" stroke="{CRLD}" stroke-width="3"/>
  <rect x="66" y="-34" width="38" height="26" rx="5" class="paper"/>
  <path d="M66-22h38" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
''')

add('geography', '台にのった地球儀と、となりに置かれた方位磁針',
    '地理・地理学＝geography。', f'''
<g transform="translate(268 226)">
  <circle r="112" class="bluep o"/>
  <ellipse rx="46" ry="112" fill="none" stroke="{BLUD}" stroke-width="2.5"/>
  <ellipse rx="112" ry="112" fill="none" stroke="{BLUD}" stroke-width="2.5"/>
  <path d="M-112 0h224M-104-56h208M-104 56h208" fill="none" stroke="{BLUD}" stroke-width="2.5"/>
  <path d="M-72-52q40-32 74-6t-12 46-56 8-22-22z" class="green"/>
  <path d="M34 24q44-14 62 12t-24 40-52-14z" class="green"/>
  <path d="M-56 58q22 12 26 34" fill="none" stroke="{GRND}" stroke-width="3"/>
</g>
<path d="M268 338v0" fill="none"/>
<g transform="translate(268 340)">
  <path d="M-60 0h120" fill="none" stroke="#8b6437" stroke-width="14" stroke-linecap="round"/>
  <path d="M0-14v-16" fill="none" stroke="#8b6437" stroke-width="12"/>
</g>
<g transform="translate(500 300)">
  <circle r="64" fill="#fffefd" class="o"/>
  <circle r="52" fill="none" stroke="{MUTED}" stroke-width="2"/>
  <path d="M0-46l14 40-14 52-14-52z" class="coral o"/>
  <path d="M0-46l14 40h-28z" class="ink"/>
  <path d="M-30-30h60M-30 30h60" fill="none" stroke="{MUTED}" stroke-width="2"/>
</g>
<path d="M60 386h480" class="a"/>''')

add('get', '棚の上の箱へ手をのばして、取り出そうとしている',
    '手に入れる・着く＝get。手をのばして取る。', f'''
{shelf(300, 210, 320)}
{box(360, 174, 80, 62, 22, 'gold')}
{person(240, 356, 1.2, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{arrowline([(344, 148), (312, 190)], CRL, 6, True)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('girl', '風船を手にした女の子が、にこにこしながら立っている',
    '女の子・少女＝girl。', f'''
{person(286, 356, 0.85, 1, 'coral', 'blue', 'up', 'bob', 'smile')}
<g transform="translate(236 148)">
  <ellipse rx="32" ry="40" class="violet o"/>
  <path d="M0 40q-12 42 8 84" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
{soccer(470, 330, 26)}
{spark(404, 196, 0.9)}
<path d="M60 386h480" class="a"/>''')

add('give', '箱を相手に手渡し、二人の手の間に点線の矢印がのびている',
    '与える・渡す＝give。', f'''
{person(178, 356, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(434, 356, 1.15, -1, 'coral', 'violet', 'give', 'bob', 'smile')}
{box(306, 252, 78, 62, 22, 'gold')}
{arc(242, 236, 370, 236, 50, MUTED, True, 4)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('glass', '窓から差し込む光と、窓台にのせた水の入ったグラス',
    'ガラス・コップ＝glass。', f'''
<path d="M180 250h240l-96 148H92z" fill="#fff0c5"/>
<g transform="translate(300 160)">
  <path d="M-122-92h244v184h-244z" fill="#e1edfb" class="o"/>
  <path d="M0-92v184M-122 0h244" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-122-92h244v184h-244z" fill="none" stroke="{INK}" stroke-width="11"/>
</g>
{plank(300, 250, 300, 18)}
{tumbler(376, 250, 56, 78, 0.62)}
<path d="M60 386h480" class="a"/>''')

add('glasses', '顏にかけた眼鏡。レンズには光が反射している',
    '眼鏡＝glasses。', f'''
{face(300, 186, 92, 'smile')}
<g stroke="{INK}" stroke-width="7" fill="none">
  <rect x="196" y="132" width="92" height="70" rx="26" class="bluep"/>
  <rect x="312" y="132" width="92" height="70" rx="26" class="bluep"/>
  <path d="M288 162h24"/>
  <path d="M196 152l-44-18M404 152l44-18"/>
</g>
{spark(226, 152, 0.7)}
<path d="M60 386h480" class="a"/>''')

add('goes', '朝、家から出て歩いていく人。壁の時計は8時を指している',
    '行く＝goes。主語が he や she のときの go の形。', f'''
{house(136, 300, 0.9, 'teal')}
{suitcase(456, 336, 82, 60, 'blue')}
{person(392, 356, 1.15, 1, 'blue', 'blue', 'walk', 'short', 'smile')}
{''.join(f'<ellipse cx="{276 + i * 44}" cy="{342 - (i % 2) * 12}" rx="15" ry="9" fill="{MUTED}"/>' for i in range(2))}
{clock(520, 112, 48, 8, 0)}
{sun(80, 80, 40)}
<path d="M60 386h480" class="a"/>''')

add('going', 'スーツケースを引いて、飛行機の方へ歩き出そうとしている',
    '行くこと＝going。be going to で〜する予定。', f'''
<g transform="translate(478 122) scale(0.55) rotate(-14)">
  <path d="M-30-14L-96-92h30l86 78zM-30 14l-66 78h30l86-78z" class="teal o"/>
  <path d="M-120-2q0-18 24-20h150l44-30h22l-16 30h30q22 0 22 22t-22 22h-30l16 30h-22l-44-30H-96q-24-2-24-24z" class="teal o"/>
</g>
{person(206, 356, 1.15, 1, 'blue', 'violet', 'carry', 'bob', 'smile')}
{suitcase(292, 336, 96, 66, 'coral')}
{arrowline([(348, 356), (438, 356)], MUTED, 6)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('golfer', 'クラブを振りきってボールを打ち、グリーンの旗が見えている',
    'ゴルファー・ゴルフをする人＝golfer。', f'''
{person(210, 356, 1.15, 1, 'gold', 'blue', 'give', 'cap', 'smile')}
<path d="M298 288L418 330" fill="none" stroke="#8a97a3" stroke-width="10" stroke-linecap="round"/>
<path d="M410 322l30 12-8 20-26-14z" class="ink"/>
{soccer(468, 330, 22)}
<path d="M468 348h-16" fill="none" stroke="{GLDD}" stroke-width="5"/>
<g transform="translate(548 300)">
  <path d="M0 0v-104" fill="none" stroke="#8b6437" stroke-width="7"/>
  <path d="M0-104h44l-14 14 14 14h-44z" class="coral o"/>
</g>
<path d="M126 190a110 110 0 0 1 90 60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
<path d="M60 386h480" class="a"/>''')

add('gone', '扉の開いた空の鳥かごと、遠くへ飛び去っていく鳥',
    'いなくなった・行ってしまった＝gone。', f'''
<g transform="translate(210 310)">
  <path d="M-92-60q0-118 92-118t92 118" fill="#fffefd" class="o"/>
  <path d="M-92 0h184v-60h-184z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{-70 + i * 28} -60v60" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(6))}
  {''.join(f'<path d="M{-70 + i * 30} -60q0-70 70-70t70 70" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(1, 5))}
  <path d="M-92-60v-56q0-30 30-52" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
{bird(210, 210, 1.0, 'blue', True)}
{bird(452, 132, 1.05, 'blue')}
{''.join(f'<path d="M{378 + i * 26} {154 + i * 12}h-46" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>' for i in range(3))}
<path d="M60 386h480" class="a"/>''')

add('goodbye', '別れのあいさつに、二人が手を振り合っている',
    'さようなら＝goodbye。', f'''
{person(234, 356, 1.15, 1, 'coral', 'blue', 'up', 'bob', 'smile')}
{person(392, 356, 1.15, -1, 'teal', 'blue', 'up', 'short', 'smile')}
{suitcase(492, 336, 84, 60, 'gold')}
{arc(268, 214, 358, 214, 46, MUTED, True, 4)}
<path d="M60 386h480" class="a"/>''', arrow=True)

GRAY = f'''
{cloud(200, 116, 1.2, 'blue')}
<g transform="translate(228 316)">{cat(0, 0, 0.95, '#9aa7b1')}</g>
{''.join(f'<ellipse cx="{424 + (i % 3) * 56}" cy="{356 - (i // 3) * 22}" rx="30" ry="20" fill="#c3cbd1" class="o"/>' for i in range(6))}
<path d="M60 386h480" class="a"/>'''

add('gray', '灰色の猫と灰色の雲、足もとには灰色の石がころがっている',
    '灰色の・灰色＝gray。', GRAY)

add('great', '大きな山の頂上に立って両手を上げ、そばに旗がはためいている',
    'すばらしい・大きな・偉大な＝great。', f'''
<path d="M-20 356L210 60l120 160 70-70 220 206z" fill="#e4eaee" class="o"/>
<path d="M210 60l120 160-60 40-60-40z" fill="#f6f9fb"/>
{tree(130, 356, 0.8)}
{person(282, 176, 0.7, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{flagpole(226, 168, 66)}
{spark(430, 130, 1.1)}
{spark(150, 200, 0.9)}
<path d="M60 386h480" class="a"/>''')

add('green', '緑の草の上に緑の木が並び、緑のカエルが鳴いている',
    '緑の・緑＝green。', f'''
<path d="M0 306h600v94H0z" fill="#bfe4cb"/>
{tree(110, 330, 1.1)}
{tree(500, 336, 1.25)}
{frog(300, 330, 0.95)}
{''.join(f'<path d="M{216 + i * 84} 356q-6-30 6-44" fill="none" stroke="{GRND}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
<path d="M60 386h480" class="a"/>''')

add('grey', '灰色の猫と灰色の雲、足もとには灰色の石がころがっている',
    '灰色の・灰色＝grey。gray のイギリス綴り。', GRAY)

add('griddle', '平らな鉄板でパンケーキを焼き、へらで返そうとしている',
    '平らな鉄板＝griddle。', f'''
<g transform="translate(300 306)">
  <path d="M-186-28h372v28h-372z" fill="#4b5563" class="o"/>
  <path d="M-170-30h340v10h-340z" fill="#6b7680"/>
  <path d="M-186 0v34M186 0v34" fill="none" stroke="#6b7680" stroke-width="14" stroke-linecap="round"/>
</g>
{''.join(f'<ellipse cx="{196 + i * 104}" cy="{272}" rx="44" ry="22" class="goldp o"/>' for i in range(3))}
{''.join(f'<path d="M{196 + i * 104} 236q-10-24 4-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>' for i in range(3))}
<path d="M462 232l74 40" fill="none" stroke="#8a97a3" stroke-width="10" stroke-linecap="round"/>
<path d="M462 232l-46-6 10 30 40 14z" class="ink"/>
<path d="M60 386h480" class="a"/>''')

add('grinder', '豆をひくひき器。ハンドルが回り、下の引き出しに粉がたまる',
    'ひき器・研削機＝grinder。', f'''
<g transform="translate(300 306)">
  <path d="M-92-104h184v104h-184z" fill="#8b6437" class="o"/>
  <path d="M-62-38h124v44h-124z" class="paper"/>
  <path d="M-62-38h124v44h-124z" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M0-104v-34" fill="none" stroke="#6b7680" stroke-width="10"/>
  <path d="M0-138h58q22 0 22 22" fill="none" stroke="#6b7680" stroke-width="12" stroke-linecap="round"/>
  <path d="M80-116v24" fill="none" stroke="#6b7680" stroke-width="12" stroke-linecap="round"/>
</g>
{''.join(f'<ellipse cx="{262 + i * 34}" cy="{160 - (i % 2) * 22}" rx="16" ry="11" fill="#6b4a2a" transform="rotate({-20 + i * 24} {262 + i * 34} {160 - (i % 2) * 22})"/>' for i in range(3))}
<path d="M340 152a52 52 0 0 1 34 40" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9" marker-end="url(#ar)"/>
<path d="M270 344h60q14 0 14 14t-14 14h-60z" fill="#6b4a2a" class="o"/>
<path d="M60 386h480" class="a"/>''', arrow=True)

add('ground floor', '3階建ての建物で、いちばん下の階が点線の丸に囲まれている',
    '1階（英）・地上階＝ground floor。', f'''
<g transform="translate(300 350)">
  <path d="M-116 0v-312h232V0z" fill="#fffdf6" class="o"/>
  {''.join(f'<rect x="{-88 + c * 62}" y="{-286 + f * 96}" width="46" height="38" class="teal p o"/>' for f in range(2) for c in range(3))}
  <path d="M-34-96h68v96h-68z" class="teald o"/>
  {''.join(f'<rect x="{-88 + c * 62}" y="-86" width="46" height="38" class="teal p o"/>' if c != 1 else '' for c in range(3))}
</g>
{ring(300, 300, 92, True)}
{person(150, 356, 1.05, 1, 'coral', 'blue', 'walk', 'short', 'smile')}
<path d="M60 386h480" class="a"/>''')

add('group', '4人が肩を寄せて小さなかたまりになり、まわりを点線が囲んでいる',
    '集団・グループ＝group。', f'''
{person(226, 356, 1.0, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
{person(336, 356, 1.0, -1, 'coral', 'violet', 'hold', 'bob', 'smile')}
{person(168, 306, 0.78, 1, 'violet', 'blue', 'stand', 'bun', 'smile')}
{person(392, 306, 0.78, -1, 'gold', 'blue', 'stand', 'short', 'smile')}
{ring(282, 268, 178, True)}
<path d="M60 386h480" class="a"/>''')

add('grow', '小さな芽から大きな草へ、育っていく様子を上向きの矢印で示している',
    '育つ・育てる・増える＝grow。', f'''
{pot(150, 356, 104, 70, 'coral')}
<g transform="translate(150 286)">
  <path d="M0 0q-4-28 6-44" fill="none" stroke="{GRND}" stroke-width="7"/>
  <path d="M4-42q-26-6-32-26 26-4 34 18z" class="green o"/>
  <path d="M6-28q26-8 34-28-28-2-38 22z" class="green o"/>
</g>
{pot(430, 356, 132, 84, 'green')}
<g transform="translate(430 272)">
  <path d="M0 0q-8-96 12-150" fill="none" stroke="{GRND}" stroke-width="10"/>
  {''.join(f'<path d="M{6 - i * 12} {-30 - i * 34}q-30-12-32-40 32-2 38 30z" class="green o"/>' for i in range(3))}
  {''.join(f'<path d="M{12 + i * 8} {-44 - i * 34}q30-12 32-40-32-2-38 30z" class="green o"/>' for i in range(3))}
</g>
{arc(220, 250, 380, 130, 70, GRN, True, 5)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('guess', '布をかぶせた物を見ながら考えこみ、頭の上には何かの形が浮かんでいる',
    '推測する・当てる＝guess。', f'''
{table(320)}
<g transform="translate(390 320)">
  <path d="M-76 0q-12-76 76-76t76 76z" class="violet o"/>
  <path d="M-76 0h152" fill="none" stroke="{VIOD}" stroke-width="4"/>
</g>
{person(160, 356, 1.1, 1, 'teal', 'blue', 'think', 'short', 'smile')}
<g transform="translate(400 140)">{cloud(0, 0, 0.95, 'blue')}</g>
<circle cx="386" cy="128" r="24" class="goldp o"/>
<path d="M374 128h24" fill="none" stroke="{MUTED}" stroke-width="4"/>
{spark(452, 176, 0.8)}
<path d="M60 386h480" class="a"/>''')

add('gym', 'ダンベルを棚に並べた筋トレの部屋で、バーベルを持ち上げている',
    'ジム＝gym。訓練用の器具がある部屋。', f'''
<g transform="translate(474 320)">
  <path d="M-84-46h168v18h-168z" fill="#6b7680" class="o"/>
  <path d="M-84-28v28M84-28v28" fill="none" stroke="#6b7680" stroke-width="10"/>
  {''.join(f'<g transform="translate({-56 + i * 56} -60)"><path d="M-22 0h44" stroke="#8a97a3" stroke-width="9"/><path d="M-26-14h12v28h-12zM14-14h12v28h-12z" class="blue o"/></g>' for i in range(3))}
</g>
{person(240, 356, 1.2, 1, 'coral', 'blue', 'up', 'short', 'smile')}
<g transform="translate(240 214)">
  <path d="M-72 0h144" fill="none" stroke="#6b7680" stroke-width="10"/>
  <path d="M-96-16h26v32h-26zM70-16h26v32h-26z" class="blue o"/>
</g>
<path d="M60 386h480" class="a"/>''')

add('gymnasium', '体育館のコートから、バスケットゴールめがけて球が飛んでいる',
    '体育館・屋内運動場＝gymnasium。', f'''
<path d="M0 0h600v256H0z" fill="#f2f6f8"/>
<path d="M0 256h600v144H0z" fill="#e8e2d4"/>
{''.join(f'<path d="M0 {288 + i * 44}h600" fill="none" stroke="#d6cdb8" stroke-width="3"/>' for i in range(3))}
<g transform="translate(430 84)">
  <path d="M-72-52h144v92h-144z" fill="#fffdf6" class="o"/>
  <rect x="-26" y="-10" width="52" height="34" fill="none" stroke="{CRL}" stroke-width="6"/>
  <circle cy="62" r="34" fill="none" stroke="{CRL}" stroke-width="7"/>
  {''.join(f'<path d="M{-24 + i * 12} 96l-6 34M{24 - i * 12} 96l6 34" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for i in range(4))}
</g>
{person(190, 356, 1.2, 1, 'teal', 'blue', 'up', 'bun', 'smile')}
<circle cx="300" cy="196" r="30" class="coral o"/>
<path d="M270 196h60M300 166v60" fill="none" stroke="{INK}" stroke-width="3"/>
{arc(300, 226, 388, 150, 54, MUTED, True, 4)}
''', ground=False)

add('gymnastics', '平均台の上で両手を横にのばし、バランスをとっている',
    '体操・体操競技＝gymnastics。', f'''
<g transform="translate(300 302)">
  <path d="M-152 0h304v18h-304z" fill="#c9a464" class="o"/>
  <path d="M-112 18v64M112 18v64" fill="none" stroke="#a0764a" stroke-width="13" stroke-linecap="round"/>
</g>
{person(300, 302, 1.05, 1, 'violet', 'violet', 'stand', 'bun', 'smile')}
<path d="M232 226h136" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<path d="M232 226q-70-40-96-118" fill="none" stroke="{VIO}" stroke-width="6" stroke-dasharray="12 9"/>
<path d="M300 302l-46-12" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
{spark(150, 128, 0.9)}
<path d="M60 386h480" class="a"/>''')

add('had', 'いまは空のカップ。点線で満たされていたころの形と、過去へ戻る矢印',
    '持っていた＝had。have の過去形で、昔の状態を表す。', f'''
{table(320)}
{tumbler(280, 320, 58, 84, 0.0)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8">
  <path d="M432 236h58l-10 84h-38z"/>
  <path d="M436 258h50l-6 62h-38z"/>
</g>
<path d="M480 300h-96" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>
{clock(516, 128, 44, 3, 10)}
<path d="M60 386h480" class="a"/>''', arrow=True)

add('hair', '長い髪をたらした頭と、となりのくし',
    '髪・毛＝hair。', f'''
<g transform="translate(272 158)">
  <path d="M-104 60q-26-140 104-140t104 140v156q-30-32-34-94-32 26-70 26t-70-26q-4 62-34 94z" fill="{HAIR}" class="o"/>
  <circle r="84" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-84-14q10-76 84-76t84 76q-32-40-84-40t-84 40z" fill="{HAIR}"/>
  <path d="M-96 118l-18 142M96 118l18 142" fill="none" stroke="{HAIR}" stroke-width="22" stroke-linecap="round"/>
  <circle cx="-30" cy="-16" r="8" class="ink"/><circle cx="30" cy="-16" r="8" class="ink"/>
  <path d="M-26 32q26 24 52 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<g transform="translate(478 300) rotate(14)">
  <path d="M-16-92h32v122h-32z" fill="#8b6437" class="o"/>
  <path d="M-40 30h80v22h-80z" fill="#8b6437" class="o"/>
  {''.join(f'<path d="M{-28 + i * 14} 52v34" fill="none" stroke="#8b6437" stroke-width="8" stroke-linecap="round"/>' for i in range(5))}
</g>
{spark(160, 130, 0.9)}
''')

add('pestle', 'すり鉢に入れた粒を、すりこぎでつぶしている',
    'すりこぎ・乳棒＝pestle。', f'''
<g transform="translate(300 320)">
  <path d="M-96-72h192q-10 74-96 74t-96-74z" fill="#d7cdbb" class="o"/>
  <ellipse cy="-72" rx="96" ry="26" fill="#efe7d8" class="o"/>
  {''.join(f'<circle cx="{-52 + (i % 4) * 34}" cy="{-62 + (i // 4) * 24}" r="9" fill="#8b6437"/>' for i in range(8))}
</g>
<g transform="translate(360 240) rotate(26)">
  <path d="M0 0v-150" fill="none" stroke="#c9a464" stroke-width="28" stroke-linecap="round"/>
  <circle cy="-166" r="30" fill="#c9a464" stroke="{INK}" stroke-width="2.5"/>
  <path d="M0 0v-150" fill="none" stroke="{INK}" stroke-width="0"/>
</g>
{''.join(f'<circle cx="{430 + i * 26}" cy="{112 - (i % 2) * 22}" r="7" fill="#8b6437"/>' for i in range(3))}
<path d="M60 386h480" class="a"/>''')

add('walrus', '氷の上にのったセイウチ。長い牙とひげが目立っている',
    'セイウチ＝walrus。', f'''
<path d="M0 236h600v164H0z" fill="#cfe4f5"/>
{''.join(f'<path d="M{20 + i * 80} {280 + (i % 2) * 30}q20-14 40 0" fill="none" stroke="{BLU}" stroke-width="4"/>' for i in range(7))}
<path d="M104 344q64-66 196-62t196 62z" fill="#eef6fb" class="o"/>
<g transform="translate(318 322)">
  <path d="M-134 0q-24-74 62-90 96-18 150 12 44 24 26 64-18 36-96 36-106 0-142-22z" fill="#8b6a4a" class="o"/>
  <circle cx="-64" cy="-96" r="40" fill="#8b6a4a" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-96-124l-10-28 30 14zM-34-124l10-28-30 14z" fill="#8b6a4a" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-84-84q-6 56-14 76M-44-84q2 58 10 78" fill="none" stroke="#fffefd" stroke-width="12" stroke-linecap="round"/>
  <path d="M-84-84q-6 56-14 76M-44-84q2 58 10 78" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
  {''.join(f'<path d="M{-62 + i * 14} -62l{-10 + i * 5} -22" fill="none" stroke="{INK}" stroke-width="2.5"/>' for i in range(4))}
  <circle cx="-78" cy="-104" r="5" class="ink"/><circle cx="-46" cy="-104" r="5" class="ink"/>
  <path d="M-128 6q-42 22-22 44 32 10 54-18z" fill="#8b6a4a" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(500 96)">
  <path d="M-40 0q40-28 80 0-40 24-80 0z" class="blue o"/>
  <path d="M-40 0l-28-16 4 20-4 16 28-16z" class="blue o"/>
</g>''')

finish(__file__)
