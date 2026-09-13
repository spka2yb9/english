# -*- coding: utf-8 -*-
"""第146回。mo-/n-/o- の形容詞と、身のまわりの名詞。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
BRN='#8b6437'
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')
def split():
    return f'<path d="M300 20v360" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" fill="none"/>'
def coin(x, y, r=20):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="gold o"/>'
            f'<circle cx="{x}" cy="{y}" r="{r*0.62}" fill="none" stroke="{TONES["gold"][2]}" stroke-width="2.5"/>')
def cross(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["coral"][0]}" stroke-width="{9*s}" stroke-linecap="round">'
            f'<path d="M{x-26*s} {y-26*s}l{52*s} {52*s}M{x+26*s} {y-26*s}l{-52*s} {52*s}"/></g>')
def tick(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["green"][0]}" stroke-width="{9*s}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x-30*s} {y}l{22*s} {24*s} {42*s}-{52*s}"/></g>')
def doc(x, y, w=100, h=130, lines=4):
    g = [f'<g transform="translate({x} {y})"><path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" class="paper"/>']
    for i in range(lines):
        g.append(f'<rect x="{-w/2+14}" y="{-h/2+22+i*(h-50)/max(lines,1):.0f}" width="{w-28-(i%3)*16}" height="8" rx="4" fill="{MUTED}"/>')
    g.append('</g>')
    return ''.join(g)
def head(x, y, r=22, shirt='teal', hair='short'):
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 108) scale({r/24:.2f})" fill="{HAIR}"/>'
            f'<circle cx="{-r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<circle cx="{r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<path d="M{-r*0.3:.0f} {r*0.35:.0f}q{r*0.3:.0f} {r*0.3:.0f} {r*0.6:.0f} 0" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{-r*1.1:.0f} {r*1.5:.0f}q{r*1.1:.0f}-{r*0.6:.0f} {r*2.2:.0f} 0l-{r*0.3:.0f} {r*1.2:.0f}h-{r*1.6:.0f}z" fill="{TONES[shirt][0]}" class="o"/></g>')
def word(x, y, n=5, w=26, cls=None, bad=-1):
    """文字は描けないので、語を四角の並びで表す。bad の位置だけ形を崩す。"""
    g = [f'<g transform="translate({x} {y})">']
    for i in range(n):
        cx = -(n-1)*w/2 + i*w
        if i == bad:
            g.append(f'<rect x="{cx-9}" y="-11" width="18" height="22" rx="4" fill="{TONES["coral"][0]}" transform="rotate(18 {cx} 0)"/>')
        else:
            g.append(f'<rect x="{cx-9}" y="-11" width="18" height="22" rx="4" fill="{cls or INK}"/>')
    g.append('</g>')
    return ''.join(g)

GLD, GLDP, GLDD = TONES['gold']
CRL, CRLP, CRLD = TONES['coral']
GRN, GRNP, GRND = TONES['green']
BLU, BLUP, BLUD = TONES['blue']
TEA, TEAP, TEAD = TONES['teal']
VIO, VIOP, VIOD = TONES['violet']

def spark(x, y, s=1, cls='gold'):
    return (f'<path d="M{x} {y-16*s}l{5*s} {11*s} {11*s} {5*s}-{11*s} {5*s}-{5*s} {11*s}'
            f'-{5*s}-{11*s}-{11*s}-{5*s} {11*s}-{5*s}z" class="{cls} o"/>')

def ring(x, y, r=64, dash=False, cls='coral'):
    d = ' stroke-dasharray="11 10"' if dash else ''
    c = MUTED if dash else TONES[cls][0]
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="4"{d}/>'

def warn(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0-44l44 76h-88z" class="gold o"/>'
            f'<path d="M0-16v22" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cy="18" r="4" class="ink"/></g>')

def bottle(x, y, s=1, cls='green'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-30 0v-70q0-16 12-24v-24h36v24q12 8 12 24V0z" class="{cls} o"/>'
            f'<path d="M-18-118h36v14h-36z" class="{cls}d o"/></g>')

def clock(x, y, s=1, h=2, m=0):
    ah = math.radians(h*30 + m*0.5 - 90); am = math.radians(m*6 - 90)
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="52" fill="#fffefd" class="o"/>'
            f'<path d="M0 0l{40*math.cos(am):.0f} {40*math.sin(am):.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M0 0l{26*math.cos(ah):.0f} {26*math.sin(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle r="4" class="ink"/></g>')

# --- 大きさ・重み --------------------------------------------------------------

add('momentous', 'それまでの流れを変える、歴史に残る一手', f'''
{table(310)}
{doc(210, 200, 190, 220, 4)}
<path d="M150 250h120" stroke="{CRL}" stroke-width="7" fill="none" stroke-linecap="round"/>
<g transform="translate(320 170) rotate(34)"><path d="M-8-90h16l6 120-14 26-14-26z" class="teal o"/></g>
{''.join(spark(x, y, 1.2) for x, y in [(410,100),(500,160),(452,240)])}
{head(516, 292, 26, 'gold', 'bun')}''')

add('monumental', '見上げるほど大きな記念の像', f'''
<g transform="translate(300 306)">
  <path d="M-110 0v-40h220V0z" fill="#c3cbd1" class="o"/>
  <path d="M-70-40v-60h140v60z" fill="#d5dbde" class="o"/>
  <path d="M-40-100v-120h80v120z" fill="#e2e7e9" class="o"/>
  <circle cy="-252" r="34" fill="#e2e7e9" class="o"/>
  <path d="M-40-220q0-40 40-40t40 40" fill="#e2e7e9" class="o"/>
</g>
{head(120, 300, 18, 'teal', 'short')}
{head(480, 300, 18, 'coral', 'bob')}''')

add('monotonous', '同じものが延々と続いて、あくびが出る', f'''
{''.join(f'<rect x="{50+i*54}" y="150" width="40" height="90" rx="6" class="tealp o"/>' for i in range(8))}
<path d="M498 195h60" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/>
{head(160, 320, 26, 'coral', 'short')}
<ellipse cx="160" cy="332" rx="11" ry="14" fill="{INK}"/>
<path d="M200 288q16-16 6-34" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('more or less', 'ぴったりではないが、だいたい同じ大きさ', f'''
<rect x="80" y="130" width="130" height="150" rx="10" class="teal o"/>
<rect x="390" y="140" width="140" height="140" rx="10" class="teal o"/>
<g fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round">
  <path d="M256 180q22-24 44 0t44 0"/><path d="M256 232q22-24 44 0t44 0"/></g>''')

add('motionless', 'まわりが動いても、じっと動かない', f'''
{person(300, 306, 1.3, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M120 160h70M100 200h90M120 240h70M410 160h70M410 200h90M410 240h70"/></g>
<g transform="translate(360 170)"><path d="M0 0q-30-28-6-44 18-12 6 14 8-26 26-18 22 10-26 48z" class="coral o"/></g>
{head(70, 300, 22, 'violet', 'bob')}
{head(530, 300, 22, 'gold', 'short')}''')

add('mournful', 'うつむいて、静かに涙をこぼす', f'''
{cloud(180, 110, 1.3, 'blue')}
{''.join(f'<path d="M{130+i*44} 170v34" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>' for i in range(5))}
{person(330, 306, 1.3, 1, 'violet', 'blue', 'stand', 'bob', 'sad')}
{drop(300, 196, 1.2)}
{drop(360, 202, 1.0)}''')

add('muffled', '毛布ごしに聞くと、音がこもって弱くなる', f'''
<g transform="translate(96 200)"><path d="M-40-40h34l56-46v172l-56-46h-34z" class="teal o"/></g>
{''.join(f'<path d="M160 {200-40-i*26}q{40+i*26} {40+i*26} 0 {(40+i*26)*2}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for i in range(3))}
<g transform="translate(330 200)"><path d="M-34-140h68v280h-68z" class="violetp o"/>
  {''.join(f'<path d="M-34 {-120+i*40}h68" fill="none" stroke="{VIOD}" stroke-width="3"/>' for i in range(7))}</g>
{''.join(f'<path d="M382 {200-20-i*18}q{20+i*18} {20+i*18} 0 {(20+i*18)*2}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>' for i in range(2))}
{head(510, 250, 28, 'blue', 'short')}''')

add('mundane', 'とくべつな日ではない、いつもの食器と洗いもの', f'''
{split()}
{table(300)}
<g transform="translate(150 268)"><ellipse rx="60" ry="18" fill="#fffefd" class="o"/>
  <ellipse rx="40" ry="10" fill="none" stroke="{MUTED}" stroke-width="2.5"/></g>
<g transform="translate(150 210)"><path d="M-24 0v-46h48v46z" fill="#fffefd" class="o"/>
  <path d="M24-36q22 0 22 14t-22 14" fill="none" class="o"/></g>
{ring(150, 236, 116)}
<g transform="translate(450 250)"><path d="M-64 40q0-72 64-72t64 72z" class="coralp o"/>
  <path d="M-64 40h128v14h-128z" class="coral o"/>
  <circle cx="0" cy="-44" r="10" class="coral o"/></g>
{''.join(spark(x, y, 1) for x, y in [(360,140),(540,150)])}
{ring(450, 218, 118, True)}''')

add('murky', '澄んだ水と、濁って底が見えない水の対比', f'''
{split()}
<g transform="translate(150 220)"><path d="M-70-100h140v200h-140z" fill="#eaf4fb" class="o"/>
  <path d="M-58-60h116v152h-116z" fill="{BLUP}"/>
  <path d="M-38 60q34-30 76-6-40 20-76 6z" class="teal o"/>
  <path d="M-70-100h140v200h-140z" fill="none" class="o"/></g>
{ring(150, 220, 128, True)}
<g transform="translate(450 220)"><path d="M-70-100h140v200h-140z" fill="#eaf4fb" class="o"/>
  <path d="M-58-60h116v152h-116z" fill="#9aa38a"/>
  <path d="M-38 60q34-30 76-6-40 20-76 6z" fill="#8a9280"/>
  <path d="M-70-100h140v200h-140z" fill="none" class="o"/></g>
{ring(450, 220, 128)}''')

add('mustard', 'ソーセージにしぼり出す黄色いからし', f'''
{table(320)}
<g transform="translate(180 250) rotate(28)"><path d="M-26 0v-92q0-18 14-26v-16h24v16q14 8 14 26V0z" class="goldp o"/>
  <path d="M-12-134h24v-16h-24z" class="goldd o"/></g>
<path d="M250 210q46 10 66 44" fill="none" stroke="{GLD}" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(410 280)"><ellipse rx="106" ry="18" fill="#fffefd" class="o"/>
  <path d="M-80-14q80-26 160 0-80 22-160 0z" fill="#d08a5a" class="o"/>
  <path d="M-56-20q56-16 112 0" fill="none" stroke="{GLD}" stroke-width="9" stroke-linecap="round"/></g>''')

add('mute', 'つまみを押すと、出ていた音が止まる', f'''
{split()}
<g transform="translate(150 200)"><path d="M-40-40h34l56-46v172l-56-46h-34z" class="teal o"/>
  {''.join(f'<path d="M64 {-24-i*20}q{24+i*20} {24+i*20} 0 {(24+i*20)*2}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(2))}</g>
<g transform="translate(450 200)"><path d="M-40-40h34l56-46v172l-56-46h-34z" class="teal o"/>
  {''.join(f'<path d="M64 {-24-i*20}q{24+i*20} {24+i*20} 0 {(24+i*20)*2}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>' for i in range(2))}</g>
<g transform="translate(450 330)"><rect x="-40" y="-24" width="80" height="48" rx="12" class="corald o"/>
  <circle r="12" fill="#fffefd" class="o"/></g>
{hand(516, 336, -1)}''')

# --- 人がら ------------------------------------------------------------------

add('naive', 'うますぎる話をそのまま信じてしまう', f'''
{person(160, 306, 1.15, 1, 'teal', 'blue', 'reach', 'bob', 'smile')}
<g transform="translate(400 170)"><rect x="-120" y="-70" width="240" height="140" rx="22" class="paper"/>
  <path d="M-104 56l-38 44 6-44z" class="paper"/>
  {coin(-40, 0, 26)}{coin(20, 0, 26)}{coin(80, 0, 26)}
  {spark(-70, -40, 0.8)}{spark(90, -44, 0.8)}</g>
<path d="M262 190l40-16" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('nosy', 'へいの向こうをのぞきこんで、人のことを知りたがる', f'''
<path d="M60 230h340v14H60z" class="goldd o"/>
{''.join(f'<path d="M{80+i*52} 244v92" stroke="{GLDD}" stroke-width="26" fill="none"/>' for i in range(6))}
{head(300, 200, 30, 'coral', 'short')}
<g transform="translate(348 230)">{hand(0, 0, 1)}</g>
{person(500, 306, 1.05, -1, 'teal', 'blue', 'hold', 'bob', 'neutral')}
<path d="M340 190l110 20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('obnoxious', 'そばで大声を出しつづけ、みんなが顔をしかめる', f'''
{person(200, 306, 1.2, 1, 'coral', 'blue', 'up', 'short', 'neutral')}
{''.join(f'<path d="M256 {170-i*22}q{28+i*20} {28+i*20} 0 {(28+i*20)*2}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for i in range(3))}
{head(430, 260, 28, 'teal', 'bob')}
{head(520, 300, 26, 'violet', 'short')}
<path d="M406 208q16-16 0-34M498 250q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M462 300q20 14 40 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>''')

add('obsessive', '同じことを何度も確かめずにいられない', f'''
<g transform="translate(300 220)"><path d="M-58-96h116v192h-116z" fill="#fffefd" class="o"/>
  <g transform="translate(34 10)"><rect x="-20" y="-14" width="40" height="34" rx="6" class="gold o"/>
    <path d="M-11-14v-12a11 11 0 0 1 22 0v12" fill="none" class="a"/></g></g>
{hand(230, 240, 1)}
<g transform="translate(300 100)"><path d="M-70 0a70 44 0 1 1 24 34" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/></g>
{head(490, 260, 28, 'coral', 'short')}
{''.join(f'<circle cx="{452+i*30}" cy="180" r="6" class="ink"/>' for i in range(3))}''', arrow=True)

add('obstinate', '引っぱられても、足をふんばって動かない', f'''
{person(400, 306, 1.25, -1, 'coral', 'blue', 'stand', 'short', 'neutral')}
<path d="M348 236h-70" fill="none" stroke="{GLDD}" stroke-width="10" stroke-linecap="round"/>
{person(200, 306, 1.15, -1, 'teal', 'green', 'reach', 'bob', 'sad', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M448 250h34M452 286h34"/></g>
<path d="M370 340h60" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>''')

# --- ない・存在しない --------------------------------------------------------

add('nameless', '札のついた品が並ぶなか、一つだけ名札が白いまま', f'''
{table(320)}
{''.join(box(110 + i*130, 260, 84, 62, 20, 'teal') for i in range(4))}
{''.join(f'<rect x="{68+i*130}" y="292" width="84" height="26" rx="5" class="paper"/>' for i in range(4))}
{''.join(word(110 + i*130, 305, 3, 18, MUTED) for i in range(3))}
{ring(500, 305, 56)}''')

add('nonexistent', '形だけ描かれていて、手がそのまま通りぬける', f'''
{table(330)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10">
  <path d="M230 300v-96h140v96z"/><path d="M230 204l30-30h140l-30 30M370 204l30-30v96l-30 30"/></g>
{hand(300, 250, 1)}
<path d="M420 250h80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{head(120, 250, 28, 'coral', 'bob')}
<path d="M160 240l60 6" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('needless', '晴れた空の下で、いらない傘をさしている', f'''
{sun(480, 90, 46)}
{person(240, 306, 1.2, 1, 'teal', 'blue', 'hold', 'short', 'neutral')}
<path d="M262 232v-96" fill="none" stroke="{GLDD}" stroke-width="7"/>
<path d="M160 140q102-96 204 0z" class="coral o"/>
<path d="M160 140q26-22 51 0t51 0 51 0" fill="none" class="o"/>
{ring(262, 168, 118, True)}''')

add('odourless', 'においの立つ入れものと、まったく無臭の入れものの対比', f'''
{split()}
{bottle(150, 300, 1.0, 'green')}
<g fill="none" stroke="{GRN}" stroke-width="5" stroke-linecap="round">
  <path d="M126 150q-16-26 0-52 16-26 0-50M174 156q-16-26 0-52 16-26 0-50"/></g>
{bottle(450, 300, 1.0, 'teal')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" stroke-linecap="round">
  <path d="M426 150q-16-26 0-52M474 156q-16-26 0-52"/></g>''')

add('painless', '注射をしても、痛みを感じないまま笑っている', f'''
{person(180, 306, 1.2, 1, 'teal', 'blue', 'reach', 'bob', 'smile')}
<g transform="translate(340 210) rotate(30)"><path d="M-14-60h28v96h-28z" fill="#fffefd" class="o"/>
  <path d="M-8 36h16v22h-16z" class="blue o"/><path d="M0 58v40" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-14-60h28v-16h-28z" class="blued o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7">
  <path d="M420 150l30-30M460 200h40M420 250l30 30"/></g>''')

# --- 身のまわりの名詞 ----------------------------------------------------------

add('nationality', '国旗のついた旅券', f'''
{table(330)}
<g transform="translate(300 296) rotate(-6)"><rect x="-96" y="-132" width="192" height="264" rx="12" class="blued o"/>
  <rect x="-60" y="-96" width="120" height="74" rx="6" class="paper"/>
  <path d="M-56-92h56v34h-56z" class="blue o"/>
  <path d="M0-92h56M0-76h56M0-58h56" fill="none" stroke="{CRL}" stroke-width="8"/>
  {''.join(f'<rect x="-60" y="{4+i*26}" width="{120-(i%2)*40}" height="10" rx="5" fill="#dfe6ea"/>' for i in range(4))}</g>''')

add('newborn', '布にくるまれた、生まれたばかりの赤ん坊', f'''
{hand(160, 260, 1)}
<g transform="translate(320 230) rotate(-8)">
  <path d="M-120 40q0-70 120-70t120 70q-120 40-240 0z" class="tealp o"/>
  <circle cx="90" cy="-24" r="52" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M60-56q30-24 60 0" fill="none" stroke="{HAIR}" stroke-width="6" stroke-linecap="round"/>
  <path d="M72-24q6 8 12 0M100-24q6 8 12 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M80 4q10 10 22 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
{''.join(spark(x, y, 0.8) for x, y in [(470,120),(120,140)])}''')

add('nonfiction', '本から現れるのは、作り話でなく実際にあったもの', f'''
{table(330)}
<g transform="translate(260 312)">
  <path d="M-116 0q56-26 112-8v-72q-56-18-112 8z" fill="#fffefd" class="o"/>
  <path d="M116 0q-56-26-112-8v-72q56-18 112 8z" fill="#fffefd" class="o"/>
  <path d="M-4-80v72" fill="none" stroke="{MUTED}" stroke-width="3"/></g>
<g transform="translate(320 170)">
  <path d="M-140 66l86-116 60 62 46-52 78 106z" fill="#c3cbd1" class="o"/>
  {sun(96, -54, 30)}</g>
{''.join(spark(x, y, 0.8) for x, y in [(120,120),(506,110)])}''')

add('nutritional', '料理と、その栄養の内わけを示す表', f'''
{table(320)}
<g transform="translate(160 268)"><ellipse rx="86" ry="24" fill="#fffefd" class="o"/>
  <circle cx="-30" cy="-12" r="20" class="greenp o"/><circle cx="14" cy="-16" r="16" class="coral o"/>
  <path d="M40-14q22-14 34 6-22 12-34-6z" class="gold o"/></g>
<path d="M270 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 190)"><rect x="-110" y="-110" width="220" height="220" rx="12" class="paper"/>
  {''.join(f'<rect x="-86" y="{-80+i*46}" width="{40+i*38}" height="26" rx="6" class="{c}"/>' for i, c in enumerate(['teal','coral','gold','green']))}
  {''.join(f'<path d="M-86 {-88+i*46}h172" fill="none" stroke="#e6ebee" stroke-width="2"/>' for i in range(4))}</g>''', arrow=True)

add('nylon', '目のつまった化学繊維の生地と、そこから編んだ網', f'''
<g transform="translate(160 200)"><rect x="-100" y="-100" width="200" height="200" rx="10" class="bluep o"/>
  {''.join(f'<path d="M-100 {-84+i*24}h200" fill="none" stroke="{BLU}" stroke-width="3"/>' for i in range(8))}
  {''.join(f'<path d="M{-84+i*24} -100v200" fill="none" stroke="{BLU}" stroke-width="3"/>' for i in range(8))}</g>
<g transform="translate(440 200)" fill="none" stroke="{TEA}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M{-110+i*40} -110L{-30+i*40} 110"/>' for i in range(6))}
  {''.join(f'<path d="M{110-i*40} -110L{30-i*40} 110"/>' for i in range(6))}</g>''')

add('oat', '穂に実ったえん麦と、煮て作ったかゆ', f'''
{table(320)}
<g transform="translate(160 300)"><path d="M0 0v-190" fill="none" stroke="{GRND}" stroke-width="6"/>
  {''.join(f'<g transform="translate(0 {-60-i*30})"><ellipse cx="-24" cy="0" rx="10" ry="18" class="goldp o" transform="rotate(-28 -24 0)"/>'
           f'<ellipse cx="24" cy="-8" rx="10" ry="18" class="goldp o" transform="rotate(28 24 -8)"/></g>' for i in range(4))}
  <ellipse cx="0" cy="-192" rx="10" ry="18" class="goldp o"/></g>
<g transform="translate(420 264)"><path d="M-84 0q0 40 84 40t84-40z" fill="#fffefd" class="o"/>
  <ellipse cy="0" rx="84" ry="20" class="goldp o"/>
  {''.join(f'<ellipse cx="{-46+i*30}" cy="{-4+(i%2)*8}" rx="9" ry="6" class="gold o"/>' for i in range(4))}</g>''')

add('painkiller', '薬をのむと、ずきずきする痛みがおさまる', f'''
{split()}
{head(150, 250, 44, 'coral', 'short')}
<g class="corals" stroke-width="5">{''.join(f'<path d="M150 168v-26" transform="rotate({d} 150 214)"/>' for d in [-40, -20, 0, 20, 40])}</g>
<g transform="translate(450 190)"><rect x="-52" y="-26" width="104" height="52" rx="26" fill="#fffefd" class="o"/>
  <path d="M0-26v52" fill="none" class="o"/><path d="M-52 0a52 26 0 0 1 52-26v52a52 26 0 0 1-52-26z" class="coral o"/></g>
{head(450, 300, 40, 'teal', 'short')}''')

add('paperback', '厚い表紙の本と、やわらかい紙表紙の本', f'''
{table(330)}
<g transform="translate(160 306)"><path d="M-80 0v-190h160V0z" class="teald o"/>
  <path d="M-64 0v-176h136V0z" fill="#fffefd" class="o"/>
  <path d="M-80-190h160v14h-160z" class="teal o"/></g>
<g transform="translate(430 306) rotate(-4)"><path d="M-76 0q-8-160 0-176 70-14 152 0 8 16 0 176z" class="coralp o"/>
  <path d="M-58-150h116M-58-118h90" fill="none" stroke="{CRL}" stroke-width="7"/>
  <path d="M-76 0q76-16 152 0" fill="none" class="o"/></g>''')

# --- 見え方・状態 --------------------------------------------------------------

add('nominal', '立派な品なのに、値札はごくわずかな額', f'''
{table(320)}
{box(230, 240, 200, 130, 40, 'violet')}
{''.join(spark(x, y, 0.9) for x, y in [(120,120),(370,110)])}
<g transform="translate(450 250) rotate(-10)"><path d="M-60-40h96l24 40-24 40h-96z" class="paper"/>
  <circle cx="30" cy="0" r="7" class="ink"/>{coin(-20, 0, 14)}</g>''')

add('normative', 'あるべき基準の線に、みんなを合わせる', f'''
<path d="M60 190h480" fill="none" stroke="{CRL}" stroke-width="6"/>
{''.join(f'<rect x="{86+i*74}" y="190" width="50" height="{110}" rx="6" class="tealp o"/>' for i in range(6))}
<path d="M300 130v40" class="a" marker-end="url(#ar)"/>
{''.join(f'<path d="M{60+i*40} 190v-14" fill="none" stroke="{CRL}" stroke-width="4"/>' for i in range(13))}''', arrow=True)

add('nostalgic', '古い写真を見て、昔をなつかしむ', f'''
{sit(180, 306, 1.15, 1, 'teal', 'blue', 'bun', 'smile', 'lap')}
{chair(194, 306, 1.05, 'gold', -1)}
<g transform="translate(250 226) rotate(-10)"><rect x="-40" y="-50" width="80" height="100" rx="4" fill="#f3ead6" class="o"/>
  <rect x="-32" y="-42" width="64" height="62" class="goldp o"/>
  {head(0, -12, 16, 'coral', 'bob')}</g>
<circle cx="320" cy="176" r="9" fill="#fffefd" class="o"/>
<circle cx="344" cy="148" r="13" fill="#fffefd" class="o"/>
<g transform="translate(460 140)"><ellipse rx="116" ry="82" fill="#fffefd" class="o"/>
  {tree(60, 46, 0.6)}{sun(-64, -30, 24)}
  {person(-16, 48, 0.4, 1, 'coral', 'blue', 'up', 'bob', 'smile')}</g>''')

add('nauseous', '胃のあたりを押さえ、気分が悪くて顔が青い', f'''
{person(300, 306, 1.3, 1, 'green', 'blue', 'hold', 'short', 'sad')}
<circle cx="300" cy="166" r="34" fill="{TONES['green'][1]}" opacity="0.75"/>
<g fill="none" stroke="{GRN}" stroke-width="5" stroke-linecap="round">
  <path d="M370 150q18-24 0-46M410 176q18-24 0-46"/></g>
<path d="M232 230q16-18 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>
{drop(348 , 130, 1.1, 'blue')}''')

add('noxious', 'たるから立ちのぼる有毒な煙で、草が枯れる', f'''
<g transform="translate(180 280)"><path d="M-56 26q-14-72 0-144h112q14 72 0 144z" class="greend o"/>
  <path d="M-58-60h116" fill="none" stroke="{INK}" stroke-width="4"/></g>
<g fill="none" stroke="{GRN}" stroke-width="6" stroke-linecap="round" opacity="0.85">
  <path d="M150 130q-20-30 0-56 20-26 0-52M210 136q-20-30 0-56 20-26 0-52"/></g>
{warn(330, 140, 1.1)}
<g transform="translate(470 306)"><path d="M0 0v-70" fill="none" stroke="{GRND}" stroke-width="7"/>
  <path d="M0-44q-40-6-46-46 38 4 46 34z" fill="#a8a878" class="o" transform="rotate(30 0 -44)"/>
  <path d="M0-60q34-16 38-52-36 8-44 44z" fill="#a8a878" class="o" transform="rotate(40 0 -60)"/></g>''')

add('numb', '冷えきって、つついても感覚がない手', f'''
{hand(280, 210, 1)}
<g fill="none" stroke="{BLU}" stroke-width="4" stroke-dasharray="9 8">
  <circle cx="280" cy="214" r="86"/><circle cx="280" cy="214" r="118"/></g>
<g transform="translate(430 300) rotate(-40)"><path d="M-6-90h12v120h-12z" class="goldd o"/>
  <path d="M0-90l-12-24h24z" class="ink"/></g>
{''.join(f'<path d="M{170+i*44} 96l6 14 14 6-14 6-6 14-6-14-14-6 14-6z" fill="{BLU}"/>' for i in range(3))}''')

add('obscure', '霧に半分かくれて、はっきり見えない山', f'''
<path d="M40 340L280 90l180 250z" fill="#c3cbd1" class="o"/>
<path d="M340 340l160-160 100 160z" fill="#d5dbde" class="o"/>
<g opacity="0.9">{cloud(240, 250, 2.0, 'blue')}{cloud(440, 270, 1.8, 'blue')}</g>
<g opacity="0.6">{cloud(340, 210, 1.6, 'blue')}</g>
{head(90, 300, 26, 'coral', 'short')}''')

add('obsolete', 'ほこりをかぶった古い電話と、今つかう電話', f'''
{table(330)}
<g transform="translate(160 300)"><path d="M-70 0v-56h140V0z" fill="#c3cbd1" class="o"/>
  <path d="M-66-56q0-36 66-36t66 36z" fill="#d5dbde" class="o"/>
  <path d="M-52-70h104v20h-104z" class="ink"/>
  <path d="M-30-92v-30h60v30" fill="none" stroke="{INK}" stroke-width="6"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3">
  <path d="M96 240q34-16 66 0t66-6"/><path d="M100 258q40-10 60 6"/></g>
<path d="M290 220h56" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 300)"><rect x="-52" y="-116" width="104" height="116" rx="12" class="teal o"/>
  <rect x="-40" y="-104" width="80" height="86" rx="4" fill="#fffefd"/>
  <path d="M-14-10h28" fill="none" stroke="#fffefd" stroke-width="4"/></g>''', arrow=True)

add('ominous', '黒い雲が垂れこめ、いやな予感がする', f'''
<g opacity="0.95">{cloud(180, 100, 1.8, 'violet')}{cloud(400, 90, 2.1, 'violet')}</g>
<path d="M310 150l-30 66h40l-34 70 90-96h-42l30-40z" class="gold o"/>
<g transform="translate(160 306)"><path d="M-46 0v-56h92V0z" fill="#fffefd" class="o"/>
  <path d="M-58-56L0-100l58 44z" class="corald o"/></g>
<g transform="translate(500 190)"><path d="M-34 0q-14-26 8-34 20-8 30 10 22-4 26 12-4 16-30 18-26 2-34-6z" fill="{INK}"/>
  <path d="M-34-4l-18-6 18-10z" fill="{INK}"/><circle cx="10" cy="-16" r="3" fill="#fffdf6"/></g>''')

add('on the other hand', '一方の手にこちら、もう一方の手にあちら', f'''
{split()}
{hand(150, 250, 1)}
{box(150, 140, 110, 78, 24, 'teal')}
{hand(450, 250, -1)}
{box(450, 140, 110, 78, 24, 'coral')}''')

add('opaque', '向こうが透けて見える板と、まったく透けない板の対比', f'''
{split()}
<g transform="translate(150 200)"><rect x="-96" y="-110" width="192" height="220" rx="8" fill="#e8f4fa" opacity="0.7" class="o"/>
  <circle cx="0" cy="0" r="52" class="coral o" opacity="0.55"/></g>
{ring(150, 200, 128, True)}
<g transform="translate(450 200)"><rect x="-96" y="-110" width="192" height="220" rx="8" fill="#9aa6ae" class="o"/></g>
<g opacity="0.25"><circle cx="450" cy="200" r="52" class="coral"/></g>
{ring(450, 200, 128)}''')

add('optimal', 'いちばん高くなる、ちょうどよい点', f'''
<path d="M60 330h480M90 350V110" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M90 320q140-230 210-190 76 44 210 190" fill="none" stroke="{TEA}" stroke-width="7"/>
<circle cx="300" cy="132" r="14" class="coral o"/>
{ring(300, 132, 46)}
<path d="M300 178v140" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('ornamental', '使うための器と、飾るための器の対比', f'''
{split()}
{table(320)}
<g transform="translate(150 296)"><path d="M-46 0q-14-70 0-96h92q14 26 0 96z" fill="#fffefd" class="o"/></g>
{ring(150, 250, 108, True)}
<g transform="translate(450 296)"><path d="M-52 0q-20-60 0-84-24-30 0-46h104q24 16 0 46 20 24 0 84z" class="violetp o"/>
  <path d="M-40-70q40-16 80 0" fill="none" stroke="{VIO}" stroke-width="5"/>
  <circle cx="0" cy="-40" r="14" class="violet o"/>
  <path d="M-30-20q30-14 60 0" fill="none" stroke="{VIO}" stroke-width="5"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(370,150),(536,160)])}
{ring(450, 240, 118)}''')

add('overcrowded', '定員をこえて、人がぎゅうぎゅうに詰まっている', f'''
<g transform="translate(300 220)"><rect x="-200" y="-96" width="400" height="192" rx="14" fill="#fffefd" class="o"/></g>
{''.join(head(120 + (i % 6) * 72, 180 + (i // 6) * 62, 26, c, h)
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('violet','short'),('green','bun'),('gold','cap'),('blue','short'),
                                     ('coral','short'),('teal','bob'),('gold','short'),('violet','bun'),('blue','cap'),('green','short')]))}
{head(520, 300, 26, 'coral', 'short')}
<path d="M508 178q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('overdue', '返す日の線をこえて、まだ返していない', f'''
<path d="M40 250h520" fill="none" stroke="{MUTED}" stroke-width="6"/>
<path d="M330 130v170" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="12 10"/>
{''.join(f'<circle cx="{110+i*74}" cy="250" r="12" class="tealp o"/>' for i in range(3))}
<circle cx="470" cy="250" r="18" class="coral o"/>
<path d="M350 320h110" class="a" stroke="{CRL}" marker-end="url(#ar)"/>
<g transform="translate(470 160)"><path d="M-44 0v-70h88V0z" class="teald o"/>
  <path d="M-34 0v-60h68V0z" fill="#fffefd" class="o"/></g>''', arrow=True)

add('overt', 'こそこそ隠れてやるのと、みんなの前で堂々とやるのの対比', f'''
{split()}
<g transform="translate(150 306)"><path d="M-90 0v-150h60V0z" class="goldd o"/></g>
{head(96, 220, 26, 'teal', 'short')}
{box(150, 250, 80, 56, 18, 'coral')}
{ring(150, 210, 118, True)}
{person(430, 306, 1.1, 1, 'teal', 'blue', 'give', 'short', 'neutral')}
{box(520, 220, 70, 50, 16, 'coral')}
{head(360, 290, 22, 'violet', 'bob')}
{ring(450, 210, 126)}''')

add('painstaking', '時間をかけて、細かいところを一つずつ埋めていく', f'''
{table(330)}
<g transform="translate(250 200)"><rect x="-130" y="-110" width="260" height="220" rx="8" class="paper"/>
  {''.join(f'<circle cx="{-104+ (i%8)*30}" cy="{-84+(i//8)*30}" r="9" class="{"teal" if i < 30 else "tealp"} o"/>' for i in range(48))}</g>
<g transform="translate(400 150) rotate(24)"><path d="M-7-90h14v120l-7 20-7-20z" class="coral o"/></g>
{clock(500, 120, 0.9, 4, 30)}
{drop(160, 90, 1.1)}
{head(520, 280, 26, 'gold', 'short')}''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
