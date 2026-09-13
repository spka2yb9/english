# -*- coding: utf-8 -*-
"""第156回。con-/cou-/cr-/cu-/d- の名詞と句動詞。"""
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

def magnifier(x, y, r=60, rot=24):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><circle r="{r}" fill="#ffffff" opacity="0.16" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M0 {r}v{r*0.7:.0f}" stroke="{INK}" stroke-width="15" stroke-linecap="round"/></g>')

def clock(x, y, s=1, h=9, m=0):
    ah = math.radians(h*30 + m*0.5 - 90); am = math.radians(m*6 - 90)
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="54" fill="#fffefd" class="o"/>'
            f'<path d="M0 0l{42*math.cos(am):.0f} {42*math.sin(am):.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M0 0l{28*math.cos(ah):.0f} {28*math.sin(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle r="4" class="ink"/></g>')

def bars(x, y, n=6, h=200, gap=34):
    return ''.join(f'<path d="M{x+i*gap} {y}v{-h}" fill="none" stroke="{INK}" stroke-width="8"/>' for i in range(n))

def car(x, y, s=1, cls='coral', f=1):
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M-90 0v-30l26-36h116l28 36V0z" class="{cls} o"/>'
            f'<path d="M-54-66l16-22h72l18 22z" class="bluep o"/>'
            f'<circle cx="-52" cy="4" r="20" fill="none" stroke="{INK}" stroke-width="7"/>'
            f'<circle cx="56" cy="4" r="20" fill="none" stroke="{INK}" stroke-width="7"/></g>')

# --- 非難・批判 --------------------------------------------------------------

add('condemnation', 'おおぜいが指をさして、強く非難する', f'''
{person(430, 306, 1.25, -1, 'violet', 'blue', 'hold', 'short', 'sad')}
{''.join(f'<g transform="translate({80+i*90} 306)">{person(0, 0, 1.05, 1, c, "blue", "point", h, "neutral")}</g>'
         for i, (c, h) in enumerate([('coral','short'),('teal','bob'),('gold','bun')]))}
{''.join(f'<path d="M{160+i*90} 230h60" fill="none" stroke="{CRL}" stroke-width="5" marker-end="url(#ar)"/>' for i in range(3))}
{''.join(f'<path d="M{60+i*90} 170q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''', arrow=True)

add('critical of', '計画のあらを一つずつ指摘する', f'''
<g transform="translate(400 190)"><rect x="-160" y="-130" width="320" height="260" rx="10" class="paper"/>
  {''.join(f'<rect x="-130" y="{-100+i*54}" width="{230-(i%2)*70}" height="16" rx="8" fill="{MUTED}"/>' for i in range(4))}
  {''.join(f'<g transform="translate(120 {-92+i*54})"><path d="M-14-14l28 28M14-14l-28 28" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/></g>' for i in [0, 2])}
  <path d="M-130 30q80-16 130 10" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{person(130, 306, 1.2, 1, 'teal', 'blue', 'point', 'bun', 'neutral')}''')

add('defamation', '刷った紙で嘘を広め、その人の名を傷つける', f'''
{''.join(f'<g transform="translate({120+ (i%3)*80} {230+(i//3)*60}) rotate({-10+i*8})">'
         f'<rect x="-46" y="-58" width="92" height="116" rx="4" class="paper"/>'
         f'<rect x="-32" y="-42" width="64" height="10" rx="5" class="coral"/>'
         f'<ellipse cx="0" cy="0" rx="24" ry="18" fill="{INK}" opacity="0.6"/></g>' for i in range(4))}
<g transform="translate(470 220)"><rect x="-70" y="-90" width="140" height="180" rx="8" fill="#fffefd" class="o"/>
  {head(470, 190, 30, 'teal', 'bob')}
  <path d="M-54 60h108" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-60-60l120 140" fill="none" stroke="{CRL}" stroke-width="7"/></g>
<path d="M330 200h60" class="a" stroke="{CRL}" marker-end="url(#ar)"/>''', arrow=True)

add('defiance', '命じられた紙を、目の前で破って従わない', f'''
{person(450, 306, 1.3, -1, 'violet', 'blue', 'point', 'short', 'neutral')}
{person(180, 306, 1.25, 1, 'coral', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(250 180) rotate(-14)"><path d="M-60-70h56l-10 140h-46z" class="paper"/></g>
<g transform="translate(320 190) rotate(16)"><path d="M4-70h56l-10 140h-46z" class="paper"/></g>
{''.join(f'<path d="M{270+i*24} {130-i*14}l14-20" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}
<path d="M390 250h-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

# --- 閉じこめ・封じこめ --------------------------------------------------------

add('confinement', 'せまい部屋に閉じこめられ、外に出られない', f'''
<g transform="translate(300 220)"><rect x="-130" y="-140" width="260" height="280" rx="6" fill="#eef1f2" class="o"/>
  <rect x="-130" y="-140" width="260" height="280" rx="6" fill="none" stroke="{INK}" stroke-width="8"/>
  <rect x="40" y="-100" width="70" height="70" rx="4" fill="#dfe6ea" class="o"/>
  {bars(50, -30, 3, 70, 26)}</g>
{person(250, 350, 1.05, 1, 'coral', 'blue', 'hold', 'short', 'sad')}
<g transform="translate(180 300)"><rect x="-20" y="-16" width="40" height="34" rx="6" class="gold o"/>
  <path d="M-11-16v-12a11 11 0 0 1 22 0v12" fill="none" class="a"/></g>''')

add('containment', 'こぼれたものを、輪で囲ってそれ以上広げない', f'''
<g transform="translate(300 240)"><ellipse rx="110" ry="70" class="violetp o"/>
  <ellipse rx="70" ry="44" class="violet o"/></g>
<g transform="translate(300 240)"><ellipse rx="170" ry="118" fill="none" stroke="{TEAD}" stroke-width="16"/></g>
{''.join(f'<path d="M{300+206*math.cos(math.radians(a)):.0f} {240+150*math.sin(math.radians(a)):.0f}l{-24*math.cos(math.radians(a)):.0f} {-20*math.sin(math.radians(a)):.0f}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="7 7"/>' for a in range(0, 360, 45))}
{person(80, 340, 0.8, 1, 'teal', 'blue', 'reach', 'cap', 'neutral')}''')

add('contamination', '工場の排水が流れこみ、川がよごれる', f'''
<g transform="translate(120 200)"><path d="M-80 100v-120h160v120z" fill="#dfe6ea" class="o"/>
  <path d="M-50-20v-50h30v50zM10-20v-70h30v70z" class="teald o"/></g>
<path d="M200 260h60v24h-60z" class="teald o"/>
<path d="M0 300h600v100H0z" fill="{BLUP}"/>
<path d="M260 284q60 20 90 30" fill="none" stroke="#8f9a72" stroke-width="14" stroke-linecap="round"/>
<g opacity="0.75"><path d="M300 320q120-30 300 10v70H300z" fill="#8f9a72"/></g>
<g transform="translate(470 350) rotate(180)"><path d="M-40 0q26-24 60-8 16 8 0 16-34 16-60-8z" class="teal o"/>
  <path d="M20 4l24-14v28z" class="teal o"/></g>
{''.join(f'<path d="M{330+i*70} 250q-14-24 0-44" fill="none" stroke="#8f9a72" stroke-width="4"/>' for i in range(2))}''')

# --- 同調・つながり ----------------------------------------------------------

add('conformity', '角ばったものを型に押しこんで、まわりと同じ形にする', f'''
{''.join(f'<circle cx="{90+i*90}" cy="300" r="34" class="teal o"/>' for i in range(4))}
<rect x="256" y="70" width="88" height="88" rx="6" class="coral o"/>
<g transform="translate(300 210)"><path d="M-70-40h140v80h-140z" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle r="34" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="9 8"/></g>
<path d="M300 170v20" class="a" stroke-width="6" marker-end="url(#ar)"/>
<circle cx="450" cy="300" r="34" class="coral o"/>''', arrow=True)

add('conjunction', '二つの文をつなぐ、あいだの短いことば', f'''
{''.join(word(150, 140 + i*44, 4, 26, INK) for i in range(2))}
{''.join(word(450, 140 + i*44, 3, 30, INK) for i in range(2))}
<g transform="translate(300 162)"><rect x="-56" y="-24" width="112" height="48" rx="12" class="coral o"/></g>
<path d="M244 162h-30M356 162h30" fill="none" stroke="{MUTED}" stroke-width="5"/>
{ring(300, 162, 84)}''')

add('consist of', '全体をばらすと、こういう部品でできている', f'''
<g transform="translate(150 200)"><path d="M-90 0v-90h180v180h-180z" fill="none"/>
  <rect x="-90" y="-90" width="180" height="180" rx="10" class="teal o"/>
  <circle cx="0" cy="0" r="44" class="goldp o"/></g>
<path d="M270 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(460 200)">
  <rect x="-110" y="-110" width="100" height="100" rx="8" class="teal o"/>
  <rect x="10" y="-110" width="100" height="100" rx="8" class="teal o"/>
  <circle cx="-60" cy="60" r="44" class="goldp o"/>
  <rect x="10" y="16" width="100" height="88" rx="8" class="teal o"/></g>''', arrow=True)

add('conscious of', 'うしろで起きていることに、ちゃんと気づいている', f'''
{person(200, 306, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(450 250)"><path d="M-70 56V-40q0-24 24-24h92q24 0 24 24v96z" class="corald o"/>
  <path d="M-46-24h92v50h-92z" class="coralp o"/></g>
<g transform="translate(200 130)"><path d="M-34 0q34-24 68 0-34 24-68 0z" fill="#fffefd" class="o"/><circle r="10" class="ink"/></g>
<path d="M240 150l180 70" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>''')

add('consolation', 'しずんでいる人の肩に、そっと手を置く', f'''
{sit(340, 340, 1.25, 1, 'blue', 'blue', 'short', 'sad', 'down')}
{chair(354, 340, 1.15, 'gold', -1)}
{person(180, 340, 1.25, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<path d="M232 238l72-14" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
{drop(300, 230, 0.9)}
{''.join(spark(x, y, 0.8) for x, y in [(130,150),(440,150)])}''')

add('dependent on', '根が水源につながっていて、それなしでは育たない', f'''
<g transform="translate(430 290)"><path d="M-60 40q-16-80 0-96h120q16 16 0 96z" class="bluep o"/>
  <path d="M-64-56h128v-16h-128z" class="blue o"/></g>
<g transform="translate(180 306)"><path d="M0 0v-140" fill="none" stroke="{GRND}" stroke-width="8"/>
  <path d="M0-90q-40-8-48-48 38 4 48 34zM0-114q40-10 48-50-38 6-48 36z" class="greenp o"/></g>
<path d="M200 306q90 26 170-4" fill="none" stroke="{BLU}" stroke-width="10" stroke-dasharray="0"/>
<path d="M370 260h-60" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

# --- 状態 --------------------------------------------------------------------

add('congestion', '道が車でうまり、まったく進まない', f'''
<path d="M0 200h600v200H0z" fill="#c3cbd1"/>
<path d="M0 290h600" fill="none" stroke="#ffffff" stroke-width="6" stroke-dasharray="30 24"/>
{''.join(car(110 + (i%3)*180, 250 + (i//3)*90, 0.62, c, 1) for i, c in enumerate(['coral','teal','violet','gold','green','blue']))}
{''.join(f'<path d="M{100+ (i%3)*180} {190+(i//3)*90}q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(6))}''')

add('contemplation', '静かに腰かけて、ひとつのことを深く考える', f'''
{sit(240, 330, 1.35, 1, 'violet', 'blue', 'bun', 'neutral', 'lap')}
{chair(254, 330, 1.2, 'gold', -1)}
<path d="M214 220l24-40" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<circle cx="330" cy="180" r="9" fill="#fffefd" class="o"/>
<circle cx="356" cy="150" r="13" fill="#fffefd" class="o"/>
<g transform="translate(460 120)"><ellipse rx="110" ry="76" fill="#fffefd" class="o"/>
  <circle r="40" class="tealp o"/></g>
{''.join(f'<path d="M{110+i*24} {200+i*30}h26" fill="none" stroke="{MUTED}" stroke-width="0"/>' for i in range(0))}''')

add('continuation', 'いったん切れたように見えて、その先へ続いていく', f'''
<path d="M60 200h180" fill="none" stroke="{TEA}" stroke-width="12"/>
<path d="M250 130v140M280 130v140" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
<path d="M290 200h200" fill="none" stroke="{TEA}" stroke-width="12" marker-end="url(#ar)"/>
{''.join(f'<circle cx="{90+i*50}" cy="200" r="10" class="teald o"/>' for i in range(4))}
{''.join(f'<circle cx="{320+i*50}" cy="200" r="10" class="teald o"/>' for i in range(4))}''', arrow=True)

add('contour', '高さの同じところをつないだ、丘の線', f'''
<g transform="translate(300 210)">
  {''.join(f'<ellipse rx="{200-i*40}" ry="{130-i*26}" fill="none" stroke="{GRND}" stroke-width="5"/>' for i in range(5))}
  <ellipse rx="20" ry="14" class="greenp o"/></g>
<path d="M40 340q120-40 260-40t260 40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
<path d="M100 360l200-140 200 140" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('damp', '乾いた壁と、しみの残る湿った壁の対比', f'''
{split()}
<g transform="translate(150 200)"><rect x="-100" y="-120" width="200" height="240" rx="6" fill="#f4f1e8" class="o"/>
  {''.join(f'<path d="M-100 {-60+i*60}h200" fill="none" stroke="#e2ddce" stroke-width="4"/>' for i in range(3))}</g>
{ring(150, 200, 132, True)}
<g transform="translate(450 200)"><rect x="-100" y="-120" width="200" height="240" rx="6" fill="#f4f1e8" class="o"/>
  {''.join(f'<path d="M-100 {-60+i*60}h200" fill="none" stroke="#e2ddce" stroke-width="4"/>' for i in range(3))}
  <path d="M-80-120q30 70 -10 120t60 60 20-80 40 40-30 100" fill="#b8bda6" opacity="0.6"/>
  <ellipse cx="40" cy="60" rx="40" ry="30" fill="#b8bda6" opacity="0.55"/></g>
{''.join(drop(400 + i*44, 300 + (i%2)*20, 0.9) for i in range(3))}
{ring(450, 200, 132)}''')

add('deadlock', '両側から引き合ったまま、印がまん中から動かない', f'''
{person(120, 306, 1.2, -1, 'teal', 'blue', 'reach', 'short', 'neutral')}
{person(480, 306, 1.2, 1, 'coral', 'blue', 'reach', 'bob', 'neutral')}
<path d="M170 220h260" fill="none" stroke="{GLDD}" stroke-width="12"/>
<path d="M300 180v80" fill="none" stroke="{CRL}" stroke-width="7"/>
<path d="M300 130v-30M240 140h-40M360 140h40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>
<g fill="none" class="a" stroke-width="6"><path d="M240 320h-70" marker-end="url(#ar)"/><path d="M360 320h70" marker-end="url(#ar)"/></g>''', arrow=True)

add('delusion', '本人には立派な城が見えているが、そこにあるのは小屋', f'''
{split()}
<g transform="translate(150 306)"><path d="M-60 0v-70h120V0z" fill="#fffefd" class="o"/>
  <path d="M-70-70L0-114l70 44z" class="corald o"/></g>
{head(150, 130, 30, 'teal', 'short')}
<g transform="translate(450 210)" fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="12 9" stroke-linejoin="round">
  <path d="M-110 100v-96h44v-30l22-26 22 26v30h44v96z"/>
  <path d="M22 100v-124h40v-26l20-24 20 24v26h40v124z"/>
  <path d="M-66 100v-46h40v46"/></g>
<circle cx="220" cy="150" r="9" fill="#fffefd" class="o"/>
<circle cx="256" cy="126" r="13" fill="#fffefd" class="o"/>''')

# --- 数・お金 -----------------------------------------------------------------

add('deflation', 'ものの値段が、そろって下がっていく', f'''
<path d="M60 340h480M90 360V70" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M110 110l90 60 90 30 90 60 90 40" fill="none" stroke="{CRL}" stroke-width="7" marker-end="url(#ar)"/>
{''.join(f'<circle cx="{110+i*90}" cy="{110+ [0,60,90,150,190][i]}" r="9" class="coral o"/>' for i in range(5))}
<g transform="translate(500 120)"><path d="M0 40q-40-16-40-56 0-30 40-30t40 30q0 40-40 56z" class="coralp o"/>
  <path d="M-24 44q24 8 48 0" fill="none" stroke="{CRLD}" stroke-width="5"/></g>
<path d="M500 200v40" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('debtor', '借りた側として、返す義務を負っている人', f'''
{person(150, 306, 1.2, 1, 'coral', 'blue', 'hold', 'short', 'sad')}
<g transform="translate(300 200) rotate(-6)"><rect x="-70" y="-50" width="140" height="100" rx="6" class="paper"/>
  {''.join(f'<rect x="-50" y="{-30+i*24}" width="{100-(i%2)*36}" height="10" rx="5" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="44" cy="30" r="14" fill="none" stroke="{CRL}" stroke-width="4"/></g>
<path d="M370 250h60" class="a" marker-end="url(#ar)"/>
{''.join(coin(400 + i*40, 320, 20) for i in range(2))}
{person(500, 306, 1.2, -1, 'violet', 'blue', 'reach', 'bun', 'neutral')}
{ring(150, 210, 118)}''', arrow=True)

add('demotion', '上の段から、下の段へ移される', f'''
{''.join(f'<rect x="{100+i*130}" y="{330-i*70}" width="120" height="{70+i*70}" rx="6" class="tealp o"/>' for i in range(3))}
<g opacity="0.35">{person(420, 190, 1.0, 1, 'violet', 'blue', 'stand', 'short', 'neutral')}</g>
{person(160, 330, 1.0, 1, 'violet', 'blue', 'stand', 'short', 'sad')}
<path d="M400 160q-120-40-200 60" fill="none" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(300 300)"><path d="M0-16l16 10v18L0 30l-16-8v-18z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="7 6"/></g>''', arrow=True)

add('counterbalance', '軽いほうにおもりを足して、水平にもどす', f'''
<g transform="translate(300 130)"><path d="M-200 0h400" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M0 0v-56" fill="none" stroke="{INK}" stroke-width="7"/><circle cy="-62" r="9" class="ink"/></g>
<path d="M110 134v50M490 134v50" fill="none" stroke="{INK}" stroke-width="4"/>
{box(110, 250, 120, 84, 26, 'gold')}
{box(490, 250, 70, 50, 16, 'teal')}
<g transform="translate(490 190)">{box(0, 0, 70, 44, 14, 'coral')}</g>
<path d="M490 100v50" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('cut down on', '大盛りをやめて、量をぐっと減らす', f'''
{split()}
{table(320)}
<g transform="translate(150 280)"><ellipse rx="90" ry="24" fill="#fffefd" class="o"/>
  <path d="M-64-10q0-60 64-60t64 60z" class="goldp o"/>
  <circle cx="-20" cy="-56" r="16" class="coral o"/><circle cx="24" cy="-62" r="14" class="green o"/></g>
{ring(150, 240, 122, True)}
<g transform="translate(450 280)"><ellipse rx="90" ry="24" fill="#fffefd" class="o"/>
  <circle cx="0" cy="-14" r="20" class="goldp o"/></g>
<path d="M300 130v40" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
{ring(450, 250, 122)}''', arrow=True)

add('counterfeit', '本物にそっくりだが、よく見るとちがう偽札', f'''
{split()}
<g transform="translate(150 200)"><rect x="-120" y="-70" width="240" height="140" rx="8" class="goldp o"/>
  <circle cx="-60" cy="0" r="34" class="gold o"/>
  <rect x="-10" y="-30" width="110" height="12" rx="6" fill="{GLDD}"/>
  <rect x="-10" y="10" width="80" height="12" rx="6" fill="{GLDD}"/></g>
{ring(150, 200, 138, True)}
<g transform="translate(450 200)"><rect x="-120" y="-70" width="240" height="140" rx="8" class="goldp o"/>
  <circle cx="-60" cy="0" r="34" class="goldp o"/>
  <rect x="-10" y="-30" width="110" height="12" rx="6" fill="#cbb98f"/>
  <rect x="-10" y="10" width="60" height="12" rx="6" fill="#cbb98f"/></g>
{magnifier(470, 230, 76, 24)}
{ring(450, 200, 148)}''')

# --- 学び・つくる ------------------------------------------------------------

add('coursework', '試験ではなく、学期のあいだに出す提出物の積み重ね', f'''
{table(330)}
{''.join(f'<g transform="translate({230+ (i%2)*8} {300-i*40}) rotate({-4+i*3})">'
         f'<rect x="-90" y="-18" width="180" height="36" rx="4" class="paper"/>'
         f'<rect x="-70" y="-8" width="90" height="10" rx="5" fill="{MUTED}"/>'
         f'<circle cx="60" cy="0" r="9" fill="none" stroke="{CRL}" stroke-width="3"/></g>' for i in range(6))}
<path d="M60 130h130" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<circle cx="{70+i*40}" cy="130" r="9" class="teal o"/>' for i in range(4))}
{person(500, 306, 1.15, -1, 'teal', 'blue', 'give', 'bob', 'smile')}''')

add('craftsmanship', '手をかけて仕上げた、細やかな出来ばえ', f'''
{table(330)}
<g transform="translate(300 290)"><path d="M-70 0q-24-90 0-110 70-24 140 0 24 20 0 110z" class="corald o"/>
  <path d="M-76-110h152v-16h-152z" class="coral o"/>
  {''.join(f'<path d="M{-60+i*30} -100q10 50 0 96" fill="none" stroke="{GLD}" stroke-width="4"/>' for i in range(5))}
  <path d="M-64-60q64 20 128 0" fill="none" stroke="{GLD}" stroke-width="5"/></g>
{hand(150, 200, 1)}
{magnifier(450, 190, 64, 24)}
{''.join(spark(x, y, 0.8) for x, y in [(210,110),(400,100)])}''')

add('cultivation', 'うねを作って、苗を一列に育てる', f'''
<path d="M0 240q140-20 300-16t300 16v160H0z" fill="#d9c9a4" class="o"/>
{''.join(f'<path d="M40 {280+i*40}q140-16 260-12t260 12" fill="none" stroke="#c0ab7f" stroke-width="7"/>' for i in range(3))}
{''.join(f'<g transform="translate({80+ (i%5)*110} {268+(i//5)*40})"><path d="M0 0v-30" fill="none" stroke="{GRND}" stroke-width="5"/>'
         f'<path d="M0-20q-24-4-28-28 22 2 28 20zM0-28q24-6 28-30-22 4-28 22z" class="greenp o"/></g>' for i in range(10))}
{person(500, 240, 1.0, -1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
<g transform="translate(440 200) rotate(34)"><path d="M-7 0h14v100h-14z" class="goldd o"/>
  <path d="M-30-24h60v24h-60z" class="ink"/></g>''')

add('dataset', '同じ形の記録が、たくさん集まったもの', f'''
{''.join(f'<g transform="translate(300 {250-i*60})"><rect x="-220" y="-40" width="440" height="80" rx="8" class="paper"/>'
         f'{"".join(f2 for f2 in ["<rect x=@" + str(-190+j*110) + "@ y=@-12@ width=@" + str(80-(j%2)*20) + "@ height=@14@ rx=@7@ fill=@" + (TEA if j == 0 else MUTED) + "@/>" for j in range(4)])}</g>'.replace('@', chr(34)) for i in range(4))}
<g transform="translate(300 330)"><rect x="-220" y="-14" width="440" height="28" rx="8" fill="#dfe6ea" class="o"/></g>
{ring(300, 190, 0) if False else ''}''')

# --- 音・動き ----------------------------------------------------------------

add('creak', '古い扉が、ぎいっと鳴る', f'''
<g transform="translate(340 306)"><path d="M-110 0v-230h220V0z" fill="#fffefd" class="o"/></g>
<g transform="translate(250 210) rotate(-20)"><path d="M0-96h150v192H0z" class="goldp o"/>
  {''.join(f'<path d="M20 {-70+i*46}h110" fill="none" stroke="{GLDD}" stroke-width="4"/>' for i in range(4))}
  <circle cx="126" cy="10" r="8" class="ink"/></g>
{''.join(f'<path d="M{120-i*10} {150+i*30}q-20 16 0 32" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}
<path d="M240 100a90 90 0 0 1 40 26" fill="none" class="a" stroke-width="4" marker-end="url(#ar)"/>''', arrow=True)

add('croak', 'カエルが、のどをふくらませて低く鳴く', f'''
<path d="M0 300h600v100H0z" fill="{BLUP}"/>
<g transform="translate(230 280)"><ellipse rx="90" ry="60" class="green o"/>
  <circle cx="-40" cy="-54" r="26" class="green o"/><circle cx="34" cy="-56" r="26" class="green o"/>
  <circle cx="-40" cy="-58" r="11" fill="#fffefd" class="o"/><circle cx="34" cy="-60" r="11" fill="#fffefd" class="o"/>
  <circle cx="-40" cy="-58" r="5" class="ink"/><circle cx="34" cy="-60" r="5" class="ink"/>
  <ellipse cy="34" rx="52" ry="34" class="greenp o"/>
  <path d="M-36 10q36 22 72 0" fill="none" stroke="{GRND}" stroke-width="4"/>
  <path d="M-84 46l-44 28 44 8M76 50l46 26-42 10" fill="none" stroke="{GRN}" stroke-width="11" stroke-linecap="round"/></g>
{''.join(f'<path d="M350 {250-30-i*30}q{30+i*30} {30+i*30} 0 {(30+i*30)*2}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for i in range(3))}''')

add('crossroads', '四方に道が伸びる十字路で、どちらへ行くか決める', f'''
<path d="M0 0h600v400H0z" class="greenp"/>
<path d="M0 160h600v100H0z" fill="#c3cbd1"/>
<path d="M240 0h120v400H240z" fill="#c3cbd1"/>
<path d="M0 210h240M360 210h240" fill="none" stroke="#ffffff" stroke-width="5" stroke-dasharray="26 20"/>
<path d="M300 0v160M300 260v140" fill="none" stroke="#ffffff" stroke-width="5" stroke-dasharray="26 20"/>
{person(300, 250, 1.0, 1, 'coral', 'blue', 'think', 'short', 'neutral')}
<g fill="none" class="a" stroke-width="5">
  <path d="M170 130h-80" marker-end="url(#ar)"/><path d="M430 130h80" marker-end="url(#ar)"/>
  <path d="M300 340v50" marker-end="url(#ar)"/></g>''', arrow=True)

add('crumb', 'パンから落ちた、小さなかけら', f'''
{table(330)}
<g transform="translate(230 260)"><path d="M-80 40q-16-80 0-96 80-18 160 0 16 16 0 96z" fill="#c98f52" class="o"/>
  <path d="M-60-40q60-14 120 0" fill="none" stroke="#a8703a" stroke-width="4"/>
  <path d="M40 40l40-30 30 30z" fill="#e6cfa4" class="o"/></g>
{''.join(f'<ellipse cx="{380+ (i%4)*36}" cy="{300+(i//4)*20}" rx="{5+(i%3)*2}" ry="{4+(i%2)*2}" fill="#c98f52" stroke="{INK}" stroke-width="2"/>' for i in range(8))}
{ring(430, 306, 84)}''')

# --- ずるさ・きまり ----------------------------------------------------------

add('cunning', 'うまい餌をしかけて、相手がかかるのを待つ', f'''
{box(400, 220, 110, 80, 24, 'gold')}
<path d="M400 262v50q0 34 34 34t34-28" fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round"/>
<g transform="translate(150 300)"><circle cx="0" cy="-30" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 106) scale(1.4)" fill="{HAIR}"/>
  <path d="M-22-38l18 8M22-38l-18 8" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-14-16q14 12 28-4" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-36 6q36-14 72 0l-10 60h-52z" fill="{VIO}" class="o"/></g>
<path d="M210 220q60-60 130-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{''.join(spark(x, y, 0.8) for x, y in [(330,120),(500,120)])}''')

add('curfew', 'この時刻までに帰らないと、門が閉まる', f'''
{clock(140, 150, 0.9, 9, 0)}
<g transform="translate(420 306)"><path d="M-120 0v-16h240v16z" class="goldd o"/>
  <path d="M-100-16v-190h20v190zM80-16v-190h20v190z" class="goldd o"/>
  <path d="M-80-200h160" fill="none" stroke="{GLDD}" stroke-width="10"/>
  <path d="M-80-30v-140h70v140zM10-30v-140h70v140z" class="goldp o"/></g>
{person(230, 340, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'neutral', 'walk')}
<path d="M270 250h70" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('corrective', '曲がったものを、器具で正しい形に直す', f'''
{split()}
<path d="M90 120q90 80 0 160" fill="none" stroke="{TEA}" stroke-width="18" stroke-linecap="round"/>
{ring(150, 200, 122, True)}
<path d="M450 110v180" fill="none" stroke="{TEA}" stroke-width="18" stroke-linecap="round"/>
<g fill="none" stroke="{CRLD}" stroke-width="9">
  <path d="M400 150h100M400 250h100"/></g>
<path d="M360 200h50M540 200h-50" class="a" marker-end="url(#ar)"/>
{ring(450, 200, 132)}''', arrow=True)

add('cut corners', '角をきちんと回らず、手前で近道してしまう', f'''
<path d="M100 90v180h340" fill="none" stroke="{GLDD}" stroke-width="14"/>
<path d="M100 90v180h340" fill="none" stroke="#ffffff" stroke-width="4" stroke-dasharray="20 18"/>
<path d="M100 150L400 270" fill="none" stroke="{CRL}" stroke-width="7" stroke-dasharray="14 10" marker-end="url(#ar)"/>
{person(230, 240, 0.95, 1, 'coral', 'blue', 'walk', 'short', 'neutral', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M120 320h300"/></g>''', arrow=True)

add('cope with', 'いくつも降ってくるが、なんとかさばききる', f'''
{person(300, 340, 1.25, 1, 'teal', 'blue', 'up', 'short', 'neutral')}
{''.join(f'<g transform="translate({x} {y}) rotate({r})">{box(0, 0, 64, 46, 14, c)}</g>'
         for x, y, r, c in [(160,120,-16,'coral'),(300,80,8,'gold'),(440,130,20,'violet'),(220,220,-10,'green')])}
{''.join(f'<path d="M{x} {y}v40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>' for x, y in [(160,160),(300,120),(440,170)])}
{drop(240, 190, 0.9)}''')

add('concentrate on', 'まわりを閉じて、一点だけに気持ちを向ける', f'''
<g opacity="0.28">{''.join(f'<g transform="translate({x} {y})">{box(0, 0, 60, 44, 12, c)}</g>' for x, y, c in [(100,120,'coral'),(510,120,'gold'),(110,320,'violet'),(510,320,'green')])}</g>
{person(180, 306, 1.2, 1, 'teal', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(410 210)"><circle r="90" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
  <circle r="56" fill="none" stroke="{CRL}" stroke-width="5"/>
  <circle r="20" class="coral o"/></g>
<path d="M250 210h70" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('cool down', '湯気の立つ飲みものが、さめて落ち着く', f'''
{split()}
{table(320)}
<g transform="translate(150 290)"><path d="M-44 0v-80h88V0z" fill="#fffefd" class="o"/>
  <path d="M-38-66h76v62h-76z" class="coralp"/>
  <path d="M44-64q26 0 26 20t-26 20" fill="none" class="o"/></g>
{''.join(f'<path d="M{126+i*28} 190q-16-26 0-46 16-24 0-44" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{ring(150, 240, 122, True)}
<g transform="translate(450 290)"><path d="M-44 0v-80h88V0z" fill="#fffefd" class="o"/>
  <path d="M-38-66h76v62h-76z" class="bluep"/>
  <path d="M44-64q26 0 26 20t-26 20" fill="none" class="o"/></g>
<path d="M300 150v40" class="a" stroke="{BLU}" stroke-width="6" marker-end="url(#ar)"/>
{ring(450, 250, 122)}''', arrow=True)

# --- 人・もの ----------------------------------------------------------------

add('condolence', 'お悔やみのことばを、そっと伝える', f'''
{person(430, 306, 1.2, -1, 'blue', 'blue', 'hold', 'short', 'sad')}
{person(180, 306, 1.2, 1, 'teal', 'blue', 'give', 'bun', 'neutral')}
<g transform="translate(300 210)"><rect x="-70" y="-46" width="140" height="92" rx="8" class="paper"/>
  <path d="M-70-46L0 10l70-56" fill="none" class="o"/>
  <path d="M-46 30h92" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
<g transform="translate(520 300)"><path d="M0 40v-40" fill="none" stroke="{GRND}" stroke-width="5"/>
  {''.join(f'<ellipse cx="0" cy="-24" rx="9" ry="18" class="violetp o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 72))}</g>
{drop(400 , 200, 0.9)}''')

add('defendant', '法廷で、訴えられた側として立つ人', f'''
<g transform="translate(300 130)"><path d="M-110 60v-40h220v40z" class="goldd o"/>
  <path d="M-90 20v-40h180v40z" fill="#fffefd" class="o"/></g>
{head(300, 96, 26, 'violet', 'bun')}
<g transform="translate(430 150) rotate(24)"><path d="M-10 0h20v60h-20z" class="goldd o"/>
  <path d="M-34-32h68v34h-68z" class="goldd o"/></g>
<g transform="translate(180 306)"><path d="M-70 0v-70h140V0z" class="goldd o"/></g>
{person(180, 306, 1.1, 1, 'coral', 'blue', 'stand', 'short', 'neutral')}
{ring(180, 210, 118)}
{''.join(f'<g transform="translate({470+i*60} 350)">{head(0, 0, 22, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('green','bob')]))}''')

add('courtship', '花をさし出して、思いを伝える', f'''
{person(180, 306, 1.2, 1, 'teal', 'blue', 'give', 'short', 'smile')}
<g transform="translate(290 240)"><path d="M0 60V0" fill="none" stroke="{GRND}" stroke-width="6"/>
  {''.join(f'<ellipse cx="0" cy="-22" rx="12" ry="22" class="coral o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 60))}
  <circle r="12" class="goldp o"/></g>
{person(440, 306, 1.2, -1, 'violet', 'blue', 'reach', 'bob', 'smile')}
{''.join(f'<path d="M{330+i*36} {150+i*16}q14-20 28 0q-4 22-14 26-10-4-14-26z" class="coral o"/>' for i in range(2))}''')

add('daffodil', '中心がラッパの形にとび出した、黄色い花', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<g transform="translate(300 250)">
  <path d="M0 120V0" fill="none" stroke="{GRND}" stroke-width="9"/>
  {''.join(f'<ellipse cx="0" cy="-52" rx="26" ry="46" class="goldp o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 60))}
  <path d="M-34-14q34-24 68 0 6 44-34 50t-34-50z" class="gold o"/>
  <path d="M-34-14q34 16 68 0" fill="none" stroke="{GLDD}" stroke-width="4"/></g>
{''.join(f'<path d="M{240+i*70} 330q-10-90 {10+i*4}-130" fill="none" stroke="{GRND}" stroke-width="8"/>' for i in range(3))}''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
