# -*- coding: utf-8 -*-
"""第147回。p- の形容詞と、職業をあらわす名詞。"""
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

def crown(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-46 22l-10-56 28 20 18-34 18 34 28-20-10 56z" class="gold o"/>'
            f'<path d="M-46 22h92v14h-92z" class="goldd o"/></g>')

def gem(x, y, s=1, cls='violet'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-46-26h92l-46 70z" class="{cls} o"/>'
            f'<path d="M-46-26l22-24h48l22 24z" class="{cls}p o"/>'
            f'<path d="M-24-26L0 44l24-70z" fill="none" stroke="{INK}" stroke-width="2"/></g>')

def warn(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0-44l44 76h-88z" class="gold o"/>'
            f'<path d="M0-16v22" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cy="18" r="4" class="ink"/></g>')

def pill(x, y, s=1, r=0):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({r})"><rect x="-44" y="-22" width="88" height="44" rx="22" fill="#fffefd" class="o"/>'
            f'<path d="M-44 0a44 22 0 0 1 44-22v44a44 22 0 0 1-44-22z" class="coral o"/></g>')

# --- 気持ち・ようす ----------------------------------------------------------

add('panicky', '書類をまき散らして、あわてふためく', f'''
{person(300, 306, 1.3, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
{''.join(f'<rect x="-30" y="-38" width="60" height="76" rx="4" class="paper" transform="translate({x} {y}) rotate({r})"/>' for x, y, r in [(130,140,-28),(180,250,18),(440,130,26),(470,240,-14),(240,90,10)])}
{drop(240, 150, 1.1)}{drop(370, 158, 1.0)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M170 320q16-16 34 0M400 322q16-16 34 0"/></g>''')

add('paramount', 'いくつも並ぶなかで、いちばん高くて重い一つ', f'''
{''.join(f'<rect x="{80+i*74}" y="{306-60-i*10}" width="52" height="{60+i*10}" rx="6" class="tealp o"/>' for i in range(5))}
<rect x="450" y="120" width="76" height="186" rx="8" class="teal o"/>
{crown(488, 90, 1.0)}
{ring(488, 210, 116)}''')

add('pathetic', '力をこめたのに、できあがりが情けない', f'''
{table(330)}
<g transform="translate(200 300)"><ellipse cx="0" cy="-14" rx="66" ry="26" fill="#fffefd" class="o"/>
  <ellipse cx="6" cy="-46" rx="40" ry="20" fill="#fffefd" class="o" transform="rotate(-10 6 -46)"/>
  <ellipse cx="-16" cy="-70" rx="22" ry="14" fill="#fffefd" class="o" transform="rotate(14 -16 -70)"/>
  <circle cx="-30" cy="-74" r="3" class="ink"/><circle cx="-6" cy="-76" r="3" class="ink"/>
  <path d="M-26-62q10 6 18-2" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
{person(430, 306, 1.15, -1, 'teal', 'blue', 'stand', 'short', 'sad')}
<path d="M330 190q14-18 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('peckish', '腹いっぱいではないが、少し何かつまみたい', f'''
{table(300)}
<g transform="translate(430 270)"><ellipse rx="46" ry="14" fill="#fffefd" class="o"/>
  <circle cx="-14" cy="-10" r="13" class="goldp o"/><circle cx="14" cy="-8" r="11" class="goldp o"/></g>
{person(190, 306, 1.2, 1, 'teal', 'blue', 'hold', 'bob', 'neutral')}
<circle cx="196" cy="230" r="26" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>
<path d="M236 210l70-6" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<path d="M250 260q12-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('petrified', '恐ろしさに、石になったように動けない', f'''
<g transform="translate(430 200)" opacity="0.55">
  <path d="M-90 106q-30-90 20-140 56-56 130-10 60 38 30 116-24 62-100 58-64-4-80-24z" fill="{INK}"/>
  <circle cx="-20" cy="10" r="12" fill="#fffdf6"/><circle cx="40" cy="4" r="12" fill="#fffdf6"/></g>
<g transform="translate(180 306)">
  <path d="M-14-8l-8 34M14-8l8 34" fill="none" stroke="#a8b0b6" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-78q26-13 52 0l-8 72h-36z" fill="#c3cbd1" class="o"/>
  <path d="M-22-72L-46-40M22-72L46-40" fill="none" stroke="#c3cbd1" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-108" r="26" fill="#d5dbde" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="-9" cy="-112" r="5" class="ink"/><circle cx="9" cy="-112" r="5" class="ink"/>
  <ellipse cx="0" cy="-92" rx="8" ry="10" class="ink"/></g>
{''.join(f'<path d="M{110+i*24} {150-i*10}v-22" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''')

add('powerless', '目の前の大波に、なすすべもなく立ちつくす', f'''
<path d="M300 400q0-260 300-300v300z" fill="{BLUP}" class="o"/>
<path d="M420 130q60-40 120-30-50 30-60 76-40-30-60-46z" fill="{BLU}" class="o"/>
{person(150, 306, 1.15, 1, 'coral', 'blue', 'stand', 'short', 'sad')}
<path d="M228 250h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('preoccupied', '考えごとに気を取られて、柱にぶつかる', f'''
<path d="M420 306v-260h30v260z" class="goldd o"/>
{person(360, 306, 1.2, 1, 'teal', 'blue', 'walk', 'short', 'neutral')}
<g fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round">
  <path d="M410 186l24-14M414 210l26 4M406 162l16-24"/></g>
<circle cx="270" cy="190" r="9" fill="#fffefd" class="o"/>
<circle cx="246" cy="160" r="13" fill="#fffefd" class="o"/>
<g transform="translate(150 110)"><ellipse rx="104" ry="70" fill="#fffefd" class="o"/>
  {doc(0, 0, 80, 96, 3)}</g>''')

add('prone', '何度やっても、同じところでつまずいてしまう', f'''
<path d="M60 330h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
{''.join(f'<path d="M{110+i*140} 330v-26h34v26z" class="goldd o"/>' for i in range(3))}
{''.join(f'<g opacity="{0.35 if i < 2 else 1}" transform="translate({150+i*140} 330) rotate(38)">{person(0, 0, 0.72, 1, "coral", "blue", "reach", "short", "sad")}</g>' for i in range(3))}
{''.join(f'<path d="M{190+i*140} 190q40-40 80 0" fill="none" class="a" marker-end="url(#ar)"/>' for i in range(2))}''', arrow=True)

add('pompous', '台の上でふんぞり返って、もったいぶって話す', f'''
<g transform="translate(300 306)"><path d="M-96 0v-56h192V0z" class="goldd o"/>
  <path d="M-110-56h220v-16h-220z" class="gold o"/></g>
{person(300, 234, 1.25, 1, 'violet', 'blue', 'point', 'short', 'neutral')}
{crown(300, 96, 0.7)}
<g transform="translate(470 160)"><rect x="-70" y="-46" width="140" height="92" rx="18" class="paper"/>
  <path d="M-54 40l-30 32 6-32z" class="paper"/>
  {word(0, 0, 3, 30, VIO)}</g>
{head(120, 320, 22, 'teal', 'bob')}
<path d="M158 288q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('pretentious', '中身はただの一品を、うんと大げさに飾りつける', f'''
{split()}
{table(320)}
<g transform="translate(150 286)"><ellipse rx="60" ry="18" fill="#fffefd" class="o"/>
  <circle cx="0" cy="-10" r="18" class="goldp o"/></g>
{ring(150, 250, 106, True)}
<g transform="translate(450 286)"><ellipse rx="88" ry="24" fill="#fffefd" class="o"/>
  <circle cx="0" cy="-12" r="18" class="goldp o"/>
  <path d="M-56-20q22-40 44-6M56-20q-22-40-44-6" fill="none" stroke="{GRN}" stroke-width="5"/>
  <path d="M-70-6q-16-30 6-44M70-6q16-30-6-44" fill="none" stroke="{GRN}" stroke-width="5"/>
  <path d="M0-40v-40" fill="none" stroke="{GLDD}" stroke-width="5"/>
  <path d="M0-80l30 14-30 14z" class="coral o"/></g>
{''.join(spark(x, y, 0.9) for x, y in [(360,150),(546,140)])}
{ring(450, 236, 128)}''')

add('perceptive', 'みんなが見のがす小さな印に、ひとりだけ気づく', f'''
<g transform="translate(300 200)"><rect x="-190" y="-120" width="380" height="240" rx="12" class="paper"/>
  {''.join(f'<rect x="{-160+ (i%6)*56}" y="{-86+(i//6)*58}" width="40" height="40" rx="8" fill="#e8edf0"/>' for i in range(12))}
  <rect x="48" y="30" width="40" height="40" rx="8" class="coralp o"/>
  <circle cx="68" cy="50" r="9" class="coral o"/></g>
{head(90, 330, 24, 'teal', 'bob')}
<path d="M126 316l232-56" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{head(510, 336, 22, 'violet', 'short')}''')

# --- 危なさ・確かさ ----------------------------------------------------------

add('perilous', '深い谷にかかる細い吊り橋を渡る', f'''
<path d="M0 306h140v94H0zM460 306h140v94H460z" class="ground"/>
<path d="M140 306l30 94h-30zM460 306l-30 94h30z" fill="#5b6b78"/>
<path d="M140 306h320" fill="none" stroke="#5b6b78" stroke-width="0"/>
<path d="M140 290q160 76 320 0" fill="none" stroke="{GLDD}" stroke-width="7"/>
<path d="M140 240q160 76 320 0" fill="none" stroke="{GLDD}" stroke-width="5"/>
{''.join(f'<path d="M{170+i*44} {286+int(38*math.sin(math.pi*i/7))}v{-46-int(30*math.sin(math.pi*i/7))}" fill="none" stroke="{GLDD}" stroke-width="4"/>' for i in range(8))}
{person(300, 322, 0.9, 1, 'coral', 'blue', 'reach', 'cap', 'surprised')}
{warn(520, 160, 1.0)}''')

add('precarious', '小さな土台の上に高く積んで、いまにも崩れそう', f'''
{table(330)}
<g transform="translate(280 306)">
  <rect x="-30" y="-34" width="60" height="34" rx="4" class="teal o"/>
  <rect x="-52" y="-72" width="104" height="36" rx="5" class="teal o" transform="rotate(4)"/>
  <rect x="-40" y="-112" width="80" height="38" rx="5" class="teal o" transform="rotate(-6)"/>
  <rect x="-62" y="-156" width="124" height="42" rx="6" class="teal o" transform="rotate(9)"/>
  <rect x="-34" y="-196" width="68" height="38" rx="5" class="teal o" transform="rotate(-12)"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M180 120q16-20 0-40M420 130q-16-20 0-40"/></g>
{head(500, 300, 26, 'coral', 'bob')}''')

add('plausible', 'その説明が、空いた形にぴたりとはまる', f'''
<g transform="translate(230 200)"><rect x="-150" y="-110" width="300" height="220" rx="12" class="tealp o"/>
  <path d="M20-50h80v100h-80a34 34 0 0 0 0-100z" fill="#fffaf1" stroke="{INK}" stroke-width="3"/></g>
<g transform="translate(470 200)"><path d="M-40-50h80v100h-80a34 34 0 0 0 0-100z" class="coral o"/></g>
<path d="M400 200h-70" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('pertinent', 'いくつもあるなかで、話の中心につながる一つ', f'''
<circle cx="300" cy="200" r="66" class="tealp o"/>
{''.join(f'<circle cx="{300+170*math.cos(math.radians(a)):.0f}" cy="{200+130*math.sin(math.radians(a)):.0f}" r="36" class="{"coral" if a==0 else "goldp"} o"/>' for a in [0, 72, 144, 216, 288])}
<path d="M366 200h68" fill="none" stroke="{CRL}" stroke-width="7"/>
{''.join(f'<path d="M{300+66*math.cos(math.radians(a)):.0f} {200+58*math.sin(math.radians(a)):.0f}L{300+134*math.cos(math.radians(a)):.0f} {200+104*math.sin(math.radians(a)):.0f}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>' for a in [72, 144, 216, 288])}
{ring(470, 200, 58)}''')

add('pervasive', '一滴のしみが、布のすみずみまで広がる', f'''
<g transform="translate(300 200)"><rect x="-210" y="-130" width="420" height="260" rx="14" fill="#fffefd" class="o"/>
  <path d="M-200-124q100 40 40 120t60 120" fill="none" stroke="#eef2f4" stroke-width="0"/>
  <g opacity="0.5"><circle r="180" class="violetp"/></g>
  <g opacity="0.7"><circle r="120" class="violetp"/></g>
  <circle r="60" class="violet o"/>
  <rect x="-210" y="-130" width="420" height="260" rx="14" fill="none" class="o"/></g>
{''.join(f'<path d="M{300+150*math.cos(math.radians(a)):.0f} {200+96*math.sin(math.radians(a)):.0f}m-6 0a6 6 0 1 0 12 0 6 6 0 1 0-12 0" class="violet"/>' for a in range(0, 360, 45))}''')

add('predictive', 'これまでの線から、この先を点線でのばす', f'''
<path d="M60 330h480M90 350V90" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M90 300l70-36 70 20 70-56 60-30" fill="none" stroke="{TEA}" stroke-width="7"/>
<path d="M360 198l180-84" fill="none" stroke="{CRL}" stroke-width="7" stroke-dasharray="14 11" marker-end="url(#ar)"/>
{''.join(f'<circle cx="{90+i*70}" cy="{y}" r="9" class="teal o"/>' for i, y in enumerate([300, 264, 284, 228]))}
<circle cx="360" cy="198" r="9" class="teal o"/>''', arrow=True)

add('preventive', '起きる前に手を打って、災いを防ぐ', f'''
<g transform="translate(430 250)"><path d="M0-120q60 24 84 34 0 90-84 128-84-38-84-128 24-10 84-34z" class="tealp o"/>
  <path d="M-40 8l30 32 60-72" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>
{''.join(f'<path d="M{110+i*40} {110+i*30}l40 34" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round" marker-end="url(#ar)"/>' for i in range(3))}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M330 200h-40"/></g>''', arrow=True)

add('periodic', '同じ間かくで、くり返しやってくる', f'''
<path d="M60 250h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
{''.join(f'<path d="M{90+i*90} 250q45-90 90 0" fill="none" stroke="{TEA}" stroke-width="6"/>' for i in range(5))}
{''.join(f'<circle cx="{90+i*90}" cy="250" r="11" class="coral o"/>' for i in range(6))}
{''.join(f'<path d="M{90+i*90} 288v22M{180+i*90} 288v22" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(1))}
{''.join(f'<path d="M{96+i*90} 300h78" fill="none" stroke="{MUTED}" stroke-width="3" marker-end="url(#ar)"/>' for i in range(5))}''', arrow=True)

add('perpetual', '止まることなく、ぐるぐる回りつづける', f'''
<g transform="translate(300 200)">
  <path d="M-118 0a118 118 0 1 1 40 88" fill="none" stroke="{TEA}" stroke-width="16" stroke-linecap="round" marker-end="url(#ar)"/>
  <path d="M118 0a118 118 0 1 1-40-88" fill="none" stroke="{TEA}" stroke-width="16" stroke-linecap="round" marker-end="url(#ar)"/>
</g>
{''.join(spark(300 + 172*math.cos(math.radians(a)), 200 + 172*math.sin(math.radians(a)), 0.7) for a in [30, 150, 270])}''', arrow=True)

add('permissive', '門が開けはなたれ、好きなようにさせている', f'''
<path d="M60 306v-190h30v190M470 306v-190h30v190" class="goldd o"/>
<g transform="translate(150 210) rotate(-32)"><path d="M0-96h100v192H0z" fill="none" stroke="{GLDD}" stroke-width="7"/>
  {''.join(f'<path d="M{16+i*24} -96v192" fill="none" stroke="{GLDD}" stroke-width="5"/>' for i in range(4))}</g>
<g transform="translate(440 210) rotate(32)"><path d="M-100-96H0v192h-100z" fill="none" stroke="{GLDD}" stroke-width="7"/>
  {''.join(f'<path d="M{-16-i*24} -96v192" fill="none" stroke="{GLDD}" stroke-width="5"/>' for i in range(4))}</g>
{person(260, 306, 0.8, 1, 'coral', 'blue', 'up', 'short', 'smile', 'walk')}
{person(350, 306, 0.76, 1, 'violet', 'green', 'walk', 'bob', 'smile')}
{sit(560, 306, 0.9, -1, 'teal', 'blue', 'bun', 'smile', 'lap')}''')

add('prescriptive', '決まりの札を指さして、こうしろと押しつける', f'''
<g transform="translate(450 190)"><rect x="-110" y="-120" width="220" height="240" rx="10" class="paper"/>
  {''.join(f'<g><circle cx="-80" cy="{-84+i*54}" r="9" class="coral o"/><rect x="-58" y="{-92+i*54}" width="{132-(i%2)*40}" height="16" rx="8" fill="{MUTED}"/></g>' for i in range(4))}</g>
{person(150, 306, 1.2, 1, 'coral', 'blue', 'point', 'bun', 'neutral')}
{head(300, 316, 24, 'teal', 'short')}
<path d="M300 270q14-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('prevalent', 'ほとんどの人が、同じものを身につけている', f'''
{''.join(f'<g transform="translate({100+(i%4)*120} {180+(i//4)*130})">{person(0, 0, 0.78, 1, "teal" if i != 5 else "coral", "blue", "stand", "cap" if i != 5 else "bob", "smile")}</g>' for i in range(8))}''')

add('priceless', '値段のつけようがないほど貴重なもの', f'''
{table(330)}
<g transform="translate(300 306)"><path d="M-80 0v-30h160V0z" class="goldd o"/>
  <path d="M-56-30v-24h112v24z" class="gold o"/></g>
{gem(300, 200, 1.4)}
{''.join(spark(x, y, 1) for x, y in [(180,130),(420,120),(200,240)])}
<g transform="translate(480 130) rotate(-10)"><path d="M-56-30h84l28 30-28 30h-84z" class="paper"/>
  <circle cx="34" cy="0" r="7" class="ink"/>
  <path d="M-40 0h40" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="9 8"/></g>''')

# --- 職業・場所 --------------------------------------------------------------

add('pharmacy', '緑の十字をかかげ、薬の並んだ店', f'''
<g transform="translate(300 306)"><path d="M-190 0v-150h380V0z" fill="#fffefd" class="o"/>
  <path d="M-200-150h400l-24-40h-352z" class="teal o"/>
  {''.join(f'<g><path d="M{-150+i*100} -20v-100h80v100z" class="tealp o"/>'
           f'{"".join(f2 for f2 in [f"<rect x=chr(34){-142+i*100}chr(34) y=chr(34){-104+j*30}chr(34) width=chr(34)64chr(34) height=chr(34)20chr(34) rx=chr(34)5chr(34) class=chr(34)goldpchr(34)/>".replace("chr(34)", chr(34)) for j in range(3)])}</g>' for i in range(4))}
</g>
<g transform="translate(300 116)"><path d="M-16-46h32v30h30v32h-30v30h-32v-30h-30v-32h30z" class="green o"/></g>''')

add('pharmacist', '白衣の人が、窓口で薬を手わたす', f'''
{table(280)}
{person(430, 306, 1.2, -1, 'teal', 'blue', 'give', 'bun', 'smile')}
<path d="M398 228h-58" fill="none" stroke="{SKIN}" stroke-width="0"/>
{pill(300, 216, 0.9, -14)}
<path d="M258 216h-52" class="a" marker-end="url(#ar)"/>
{head(150, 250, 28, 'coral', 'short')}
<g transform="translate(430 130)"><path d="M-16-40h32v26h26v32h-26v26h-32v-26h-26v-32h26z" class="green o"/></g>''', arrow=True)

add('plumber', '工具を手に、水もれしている配管を直す', f'''
<path d="M60 130h180v40H60zM240 130h40v180h-40z" class="tealp o"/>
<path d="M228 118h28v64h-28z" class="teald o"/>
{''.join(drop(262, 200 + i*40, 1.2) for i in range(3))}
{person(400, 306, 1.2, -1, 'coral', 'blue', 'reach', 'cap', 'neutral')}
<g transform="translate(320 210) rotate(-30)"><path d="M-8 0h16v70h-16z" class="ink"/>
  <path d="M-22-30h44v22h-16v12h-12v-12h-16z" class="ink"/></g>''')

add('performer', '照明を浴びて、舞台の上で演じる', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<g opacity="0.55"><path d="M300 190L160 306h280z" class="goldp"/></g>
<g transform="translate(300 110)"><path d="M-30-20h60v40h-60z" class="teald o"/></g>
{person(300, 306, 1.25, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
{''.join(head(70 + i*100, 386, 26, c, h) for i, (c, h) in enumerate([('teal','short'),('violet','bob'),('green','short'),('gold','bun'),('blue','cap'),('coral','short')]))}''')

add('presenter', 'マイクを持って、番組の進行をつとめる', f'''
{person(190, 306, 1.25, 1, 'violet', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(214 200) rotate(-18)"><rect x="-11" y="-30" width="22" height="70" rx="10" class="ink"/>
  <circle cy="-34" r="17" fill="#8f9aa2" class="o"/></g>
<g transform="translate(440 200)"><rect x="-130" y="-100" width="260" height="200" rx="12" class="teald o"/>
  <rect x="-114" y="-84" width="228" height="168" rx="6" fill="#fffefd"/>
  {''.join(f'<rect x="-90" y="{-56+i*44}" width="{180-(i%2)*60}" height="16" rx="8" fill="{MUTED}"/>' for i in range(3))}</g>''')

add('pedestrian', '横断歩道を歩いて渡る人', f'''
<path d="M0 306h600v94H0z" fill="#c3cbd1"/>
{''.join(f'<rect x="{60+i*90}" y="316" width="56" height="76" rx="3" fill="#fffefd"/>' for i in range(6))}
{person(300, 380, 1.2, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
<g transform="translate(500 190)"><rect x="-34" y="-90" width="68" height="180" rx="10" class="teald o"/>
  {head(0, 0, 22, 'green', 'short')}</g>''')

add('penniless', '財布をさかさに振っても、一枚も出てこない', f'''
{person(240, 306, 1.2, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<g transform="translate(300 130) rotate(180)"><path d="M-56-34h112v68h-112z" class="goldp o"/>
  <path d="M-56-34L0 16l56-50" fill="none" class="o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8">
  <circle cx="330" cy="216" r="18"/><circle cx="376" cy="262" r="15"/></g>
{table(330)}''')

add('preschool', '小さい子どもたちが積み木で遊ぶ、就学前の教室', f'''
{table(330)}
{''.join(f'<rect x="{190+(i%3)*54}" y="{306-40-(i//3)*40}" width="46" height="36" rx="5" class="{c} o"/>' for i, c in enumerate(['teal','coral','gold','green','violet','blue']))}
{person(110, 306, 0.72, 1, 'coral', 'blue', 'reach', 'bob', 'smile')}
{person(410, 306, 0.7, -1, 'green', 'blue', 'reach', 'short', 'smile')}
{person(520, 306, 1.05, -1, 'violet', 'green', 'stand', 'bun', 'smile')}
{''.join(spark(x, y, 0.7) for x, y in [(160,120),(480,110)])}''')

add('postwar', 'こわれた建物のとなりに、新しい家を建て直す', f'''
<g transform="translate(150 306)"><path d="M-90 0v-130h60v50h60V0z" fill="#c3cbd1" class="o"/>
  <path d="M-90-130l30-30 24 28M30-80l30-24" fill="none" stroke="{MUTED}" stroke-width="5"/>
  {''.join(f'<rect x="{-70+i*40}" y="{-100+ (i%2)*40}" width="26" height="26" fill="#e2e7e9"/>' for i in range(3))}</g>
<g transform="translate(430 306)"><path d="M-80 0v-110h160V0z" fill="#fffefd" class="o"/>
  <path d="M-96-110L0-180l96 70z" class="corald o"/>
  <path d="M-24 0v-56h48V0z" class="teal o"/></g>
<path d="M300 306v-230h14v230z" class="goldd o"/>
<path d="M306 90h130v14H306z" class="goldd o"/>
<path d="M420 104v40" fill="none" stroke="{INK}" stroke-width="4"/>
{box(420, 176, 60, 44, 14, 'gold')}''')

# --- 見た目・ことば ----------------------------------------------------------

add('paternal', '父親が子どもの手を引いて歩く', f'''
{person(240, 306, 1.3, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(400, 306, 0.72, 1, 'coral', 'green', 'reach', 'bob', 'smile')}
<path d="M312 216l40 12" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
{sun(500, 90, 36)}''')

add('patriotic', '国の旗をかかげ、胸に手をあてる', f'''
{person(230, 306, 1.3, 1, 'coral', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(360 306)"><path d="M0 0v-230" fill="none" stroke="{GLDD}" stroke-width="8"/>
  <path d="M0-230h130l-30 44 30 44H0z" class="blue o"/>
  <circle cx="52" cy="-186" r="20" class="coral o"/></g>
<path d="M230 216h34" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
<path d="M254 200q14-16 28 0q-4 22-14 26-10-4-14-26z" class="coral o"/>''')

add('phonetic', '口から出た音を、記号で書きあらわす', f'''
{head(130, 220, 44, 'teal', 'short')}
<path d="M112 240q18 16 36 0" fill="none" stroke="{INK}" stroke-width="4"/>
{''.join(f'<path d="M186 {220-20-i*20}q{20+i*20} {20+i*20} 0 {(20+i*20)*2}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(3))}
<g transform="translate(430 220)"><path d="M-116-70q-24 70 0 140M116-70q24 70 0 140" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cx="-52" cy="0" r="16" class="teal o"/>
  <path d="M-8-24v48M-8 0h32" fill="none" stroke="{TEA}" stroke-width="7" stroke-linecap="round"/>
  <path d="M56-22q22 22 0 44" fill="none" stroke="{TEA}" stroke-width="7" stroke-linecap="round"/></g>''')

add('photographic', '見たままがそのまま写る一枚', f'''
<g transform="translate(170 200)"><path d="M-100 66l64-90 44 46 40-52 60 96z" class="greenp o"/>
  {sun(60, -50, 24)}</g>
<g transform="translate(300 130)"><rect x="-56" y="-34" width="112" height="76" rx="10" class="teald o"/>
  <circle cy="4" r="26" fill="#9fb3c0" class="o"/><circle cy="4" r="13" class="ink"/>
  <rect x="-46" y="-46" width="34" height="14" rx="4" class="teal o"/></g>
<path d="M300 190v40" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 300) rotate(6)"><rect x="-96" y="-116" width="192" height="232" rx="4" fill="#f7f3e8" class="o"/>
  <rect x="-80" y="-100" width="160" height="160" class="greenp o"/>
  <path d="M-80 60l52-70 34 36 32-40 42 74z" class="green o"/></g>''', arrow=True)

add('picturesque', '額に入れたような、絵になる眺め', f'''
<g transform="translate(300 190)"><rect x="-230" y="-140" width="460" height="280" rx="8" class="goldd o"/>
  <rect x="-206" y="-116" width="412" height="232" fill="#eaf4fb" class="o"/>
  <path d="M-206 116l120-150 80 84 70-92 142 158z" fill="#c3cbd1" class="o"/>
  <path d="M-206 116q120-40 206 0t206 0v0h-412z" class="greenp o"/>
  {sun(-120, -66, 30)}
  <g transform="translate(60 70)"><path d="M-40 0v-40h80V0z" fill="#fffefd" class="o"/>
    <path d="M-50-40L0-74l50 34z" class="corald o"/></g>
</g>
{''.join(spark(x, y, 0.8) for x, y in [(80,50),(530,60)])}''')

add('piercing', '突き刺さるような、鋭い音', f'''
<g transform="translate(120 200)"><path d="M-40-40h34l56-46v172l-56-46h-34z" class="teal o"/></g>
<g stroke="{CRL}" stroke-width="7" fill="none" stroke-linecap="round">
  {''.join(f'<path d="M180 200L440 {96+i*52}"/>' for i in range(5))}</g>
{head(500, 250, 32, 'blue', 'short')}
<path d="M470 214l16-12M530 214l-16-12" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
<g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M552 190q16-16 0-34"/></g>''')

add('pitiful', '皿にたった一粒しかない、情けないほど少ない量', f'''
{table(300)}
<g transform="translate(300 270)"><ellipse rx="120" ry="32" fill="#fffefd" class="o"/>
  <ellipse rx="88" ry="20" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
  <circle cx="0" cy="-6" r="9" class="goldp o"/></g>
{head(120, 200, 28, 'coral', 'short')}
<path d="M156 210l90 40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<path d="M120 150q16-18 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('pivotal', 'そこを軸にして、全体が動く一点', f'''
<path d="M300 260L110 200M300 260l190-60" fill="none" stroke="{TEAD}" stroke-width="0"/>
<g transform="translate(300 250)"><path d="M-30 60L0 0l30 60z" class="teald o"/></g>
<g transform="translate(300 250) rotate(-14)"><rect x="-220" y="-16" width="440" height="26" rx="8" class="teal o"/></g>
<circle cx="300" cy="250" r="16" class="coral o"/>
{ring(300, 250, 52)}
<g fill="none" class="a" marker-end="url(#ar)"><path d="M110 150q40-50 100-58"/><path d="M490 320q-40 50-100 58"/></g>''', arrow=True)

add('plentiful', 'かごからあふれるほど、たっぷりある', f'''
{table(330)}
<g transform="translate(300 306)"><path d="M-140 0q-16-96 0-110h280q16 14 0 110z" class="goldp o"/>
  {''.join(f'<path d="M{-140+i*32} -110v110" fill="none" stroke="{GLDD}" stroke-width="3"/>' for i in range(10))}</g>
{''.join(f'<circle cx="{x}" cy="{y}" r="{r}" class="{c} o"/>' for x, y, r, c in
  [(200,180,32,'coral'),(266,158,34,'green'),(336,164,32,'gold'),(400,182,30,'coral'),
   (232,208,28,'green'),(300,200,30,'coral'),(370,208,28,'green'),(160,214,26,'gold'),(440,216,26,'gold')])}''')

add('poetic', '短い行を並べ、月をながめて詩をつづる', f'''
{doc(200, 200, 230, 280, 0)}
{''.join(word(200, 110 + i*44, n, 26, TEA) for i, n in enumerate([3, 5, 2, 4]))}
<g transform="translate(370 150) rotate(28)"><path d="M-8-100q30 40 8 100l-8 20-8-20q-22-60 8-100z" fill="#fffefd" class="o"/>
  <path d="M0 20v24" fill="none" stroke="{INK}" stroke-width="4"/></g>
<path d="M500 110a44 44 0 1 1-34-42 34 34 0 0 0 34 42z" class="goldp o"/>
{''.join(spark(x, y, 0.7) for x, y in [(430,60),(548,180)])}''')

add('primitive', '石を打ち欠いた道具と、たき火と草ぶきの小屋', f'''
<g transform="translate(430 306)"><path d="M-90 0q0-96 90-130 90 34 90 130z" fill="#c8a878" class="o"/>
  {''.join(f'<path d="M{-70+i*24} 0q6-70 {40-i*8}-100" fill="none" stroke="#a8865a" stroke-width="4"/>' for i in range(7))}
  <path d="M-26 0v-50h52V0z" class="ink" opacity="0.5"/></g>
<g transform="translate(180 280) rotate(-20)"><path d="M-8 0h16v90h-16z" class="goldd o"/>
  <path d="M-34-46l30-24 40 20-24 40z" fill="#9aa3a8" class="o"/></g>
<g transform="translate(300 320) scale(0.55)">{flame(0, 0, 1)}</g>''')

add('prolific', 'つぎつぎ描き上げて、作品が山と積まれる', f'''
{person(150, 306, 1.15, 1, 'teal', 'blue', 'point', 'bun', 'smile')}
<g transform="translate(280 210) rotate(-6)"><rect x="-70" y="-90" width="140" height="180" rx="4" class="paper"/>
  <path d="M-56 60l40-56 30 30 26-40 42 66z" class="greenp o"/></g>
{''.join(f'<g transform="translate({450+ (i%2)*10} {300-i*44}) rotate({-6+i*4})"><rect x="-66" y="-30" width="132" height="60" rx="4" class="paper"/>'
         f'<rect x="-52" y="-18" width="104" height="36" class="tealp o"/></g>' for i in range(5))}''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
