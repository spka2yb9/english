# -*- coding: utf-8 -*-
"""第158回。e-/f- の抽象名詞と慣用表現。"""
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
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-40 18l-8-48 24 16 16-30 16 30 24-16-8 48z" class="gold o"/>'
            f'<path d="M-40 18h80v12h-80z" class="goldd o"/></g>')

def magnifier(x, y, r=60, rot=24):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><circle r="{r}" fill="#ffffff" opacity="0.16" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M0 {r}v{r*0.7:.0f}" stroke="{INK}" stroke-width="15" stroke-linecap="round"/></g>')

def gauge(x, y, level, w=170):
    return (f'<g transform="translate({x} {y})"><rect x="{-w/2}" y="-18" width="{w}" height="36" rx="18" fill="#fffefd" class="o"/>'
            f'<rect x="{-w/2+4}" y="-14" width="{(w-8)*level:.0f}" height="28" rx="14" class="green"/></g>')

def house(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-80 0v-100h160V0z" fill="#fffefd" class="o"/>'
            f'<path d="M-94-100L0-166l94 66z" class="{cls}d o"/>'
            f'<path d="M-24 0v-56h48V0z" class="{cls} o"/>'
            f'<rect x="-62" y="-82" width="34" height="30" class="{cls}p o"/></g>')

def flag(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0v-110" fill="none" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M0-110h70l-16 26 16 26H0z" class="{cls} o"/></g>')

# --- 気持ち・勢い -------------------------------------------------------------

add('eagerly', '待ちきれず、勢いよく駆け寄る', f'''
{person(380, 330, 1.3, 1, 'coral', 'blue', 'up', 'short', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M240 180h-90M220 240h-110M250 300h-90"/></g>
{box(520, 300, 90, 64, 20, 'gold')}
{''.join(spark(x, y, 0.9) for x, y in [(480,130),(560,190)])}''')

add('eagerness', '身を乗り出して、しきりにやりたがる', f'''
{table(280)}
{person(200, 380, 1.25, 1, 'teal', 'blue', 'up', 'bob', 'smile')}
<path d="M262 260q60-30 120-6" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{person(460, 380, 1.15, -1, 'violet', 'blue', 'give', 'bun', 'smile')}
{''.join(spark(x, y, 0.9) for x, y in [(130,150),(300,120)])}
{''.join(f'<path d="M{140+i*22} {200-i*16}q14-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('fervour', 'たいまつをかかげ、熱く声をそろえる', f'''
{''.join(f'<g transform="translate({110+i*110} 340)">{person(0, 0, 1.05, 1, c, "blue", "up", h, "neutral")}</g>'
         for i, (c, h) in enumerate([('coral','short'),('violet','bob'),('gold','short'),('teal','cap')]))}
{''.join(f'<g transform="translate({86+i*110} 150) scale(0.34)">{flame(0, 0, 1)}</g>' for i in range(4))}
{''.join(f'<path d="M{86+i*110} 160v90" fill="none" stroke="{GLDD}" stroke-width="8"/>' for i in range(4))}''')

add('euphoria', '足が地につかないほど、気持ちが高ぶる', f'''
<g transform="translate(300 240)">{person(0, 0, 1.3, 1, 'coral', 'blue', 'up', 'short', 'smile')}</g>
{''.join(spark(x, y, 1.2) for x, y in [(120,120),(480,110),(150,280),(470,290),(300,60)])}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M180 330h240"/></g>
{''.join(f'<rect x="-10" y="-6" width="20" height="12" rx="3" class="{c}" transform="translate({x} {y}) rotate({r})"/>' for x, y, r, c in
  [(200,90,20,'teal'),(400,80,-30,'gold'),(240,180,40,'violet'),(380,190,-20,'green')])}''')

add('exhaustion', '力を使い果たし、地面に伸びてしまう', f'''
{table(340)}
<g transform="translate(300 340)">
  <path d="M-140-10q140-30 280 0v20h-280z" fill="none"/>
  <path d="M-120-14q10-26 40-22l90 8q30 4 30 26h-160z" fill="{CRL}" class="o"/>
  <circle cx="-150" cy="-30" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(-150 78) scale(1.16)" fill="{HAIR}"/>
  <path d="M-164-36l14 6M-136-36l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-158-18h16" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M60-12l70 8M60-6l66 16" fill="none" stroke="{BLUD}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-110-30l-40-30" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/></g>
{gauge(300, 120, 0.04, 200)}
{''.join(f'<path d="M{160+i*24} {230-i*22}q16 16 0 32" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('fatigue', '曲げつづけた金属に、ひびが入る', f'''
<g transform="translate(300 210)"><rect x="-220" y="-30" width="440" height="60" rx="8" fill="#c3ccd2" class="o"/>
  <path d="M-20-30l14 22-16 14 18 24" fill="none" stroke="{CRL}" stroke-width="7"/></g>
<g fill="none" class="a" stroke-width="5">
  <path d="M120 120q-40 40 0 80" marker-end="url(#ar)"/>
  <path d="M480 120q40 40 0 80" marker-end="url(#ar)"/></g>
{''.join(f'<path d="M{200+i*100} 300h60" fill="none" stroke="{MUTED}" stroke-width="0"/>' for i in range(0))}
{''.join(f'<path d="M{240+i*40} 300q20-20 40 0" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''', arrow=True)

add('faint', '目の前が暗くなって、その場に倒れる', f'''
<g transform="translate(320 320) rotate(96)">{person(0, 0, 1.2, 1, 'teal', 'blue', 'up', 'bob', 'neutral')}</g>
{''.join(f'<g transform="translate({160+i*70} {120-i*10})"><path d="M0-18l5 11 11 5-11 5-5 11-5-11-11-5 11-5z" class="gold o"/></g>' for i in range(3))}
<path d="M120 200a70 70 0 0 1 60-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>
{head(520, 300, 26, 'coral', 'short')}
<path d="M480 280l-60 10" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('fascination', '目を離せないほど、強く引きこまれる', f'''
{person(160, 306, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'surprised')}
<g transform="translate(430 200)"><circle r="80" class="violetp o"/>
  <circle r="46" class="violet o"/>
  {''.join(f'<path d="M0 -104v-26" transform="rotate({d})" fill="none" stroke="{VIO}" stroke-width="5"/>' for d in range(0, 360, 45))}</g>
<path d="M230 200h100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{''.join(spark(x, y, 0.9) for x, y in [(330,110),(540,300)])}''')

add('ferocity', '牙をむき出して、荒々しくうなる', f'''
<g transform="translate(300 250)">
  {''.join(f'<circle cx="{86*math.cos(math.radians(a)):.0f}" cy="{86*math.sin(math.radians(a)):.0f}" r="28" fill="#b06a3a" stroke="{INK}" stroke-width="2.5"/>' for a in range(0, 360, 30))}
  <circle r="80" fill="#d08a4e" class="o"/>
  <path d="M-40-30l24 10M40-30l-24 10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cx="-26" cy="-8" r="6" class="ink"/><circle cx="26" cy="-8" r="6" class="ink"/>
  <path d="M-46 22q46-16 92 0 0 46-46 46t-46-46z" fill="#6d2620" class="o"/>
  <path d="M-30 22l10 22 10-22M10 22l10 22 10-22" fill="#fffefd" stroke="{INK}" stroke-width="2"/></g>
{''.join(f'<path d="M{430+i*30} {170+i*30}q20 16 0 32" fill="none" stroke="{CRL}" stroke-width="6"/>' for i in range(3))}''')

# --- 移動・追い出し -----------------------------------------------------------

add('evacuation', '危険を知らせる音で、建物から外へ逃げる', f'''
<g transform="translate(180 306)"><path d="M-130 0v-230h260V0z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="{-100+ (i%3)*70}" y="{-200+(i//3)*66}" width="46" height="46" class="tealp o"/>' for i in range(6))}
  <path d="M64 0v-90h60V0z" class="teald o"/></g>
<g transform="translate(180 40)"><circle r="26" class="coral o"/>
  {''.join(f'<path d="M0 -40v-18" transform="rotate({d})" fill="none" stroke="{CRL}" stroke-width="5"/>' for d in [-40, 0, 40])}</g>
{person(360, 340, 1.05, 1, 'coral', 'blue', 'walk', 'short', 'surprised', 'walk')}
{person(470, 340, 1.0, 1, 'violet', 'blue', 'walk', 'bob', 'surprised', 'walk')}
<path d="M330 200h200" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('eviction', '家財を外に出され、住まいを明け渡す', f'''
{house(150, 306, 0.72, 'coral')}
{''.join(f'<g transform="translate({300+i*70} {306}) rotate({-10+i*8})">{box(0, -24, 64, 46, 14, c)}</g>' for i, c in enumerate(['gold','violet','teal']))}
{person(500, 306, 1.15, 1, 'blue', 'blue', 'hold', 'short', 'sad')}
{person(230, 306, 1.15, -1, 'violet', 'blue', 'point', 'bun', 'neutral')}
<path d="M270 190h80" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('emigration', '荷物を持って、自分の国から出ていく', f'''
<path d="M300 60v300" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="16 12"/>
{flag(150, 140, 0.8, 'teal')}
{flag(450, 140, 0.8, 'coral')}
{house(120, 340, 0.42, 'teal')}
{person(360, 340, 1.15, 1, 'violet', 'blue', 'carry', 'short', 'neutral', 'walk')}
<g transform="translate(376 254)"><path d="M-40-26h80v52h-80z" class="gold o"/>
  <path d="M-16-26v-14h32v14" fill="none" class="a"/></g>
<path d="M230 250h180" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('extinction', '最後の一頭がいなくなり、群れが絶える', f'''
<path d="M0 306h600v94H0z" class="ground"/>
{''.join(f'<g transform="translate({90+i*100} 300) scale(0.28)" opacity="{0.5-i*0.14:.2f}">{beast(0, 0, 1, "#8a6a48", 1)}</g>' for i in range(3))}
<g transform="translate(400 300) scale(0.28)">{beast(0, 0, 1, '#8a6a48', 1)}</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10">
  <path d="M480 260q30 30 60 0" transform="translate(0 20)"/>
  <ellipse cx="530" cy="290" rx="46" ry="30"/></g>
<path d="M60 130h480" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>''', arrow=True)

add('famine', 'ひび割れた土地に作物がなく、うつわが空のまま', f'''
<path d="M0 260h600v140H0z" fill="#d9c48f"/>
{''.join(f'<path d="M{40+i*70} 400l{20-i*4} -{80+(i%3)*30}l-14-30" fill="none" stroke="#b09a62" stroke-width="4"/>' for i in range(8))}
{''.join(f'<g transform="translate({140+i*90} 250)"><path d="M0 0v-50" fill="none" stroke="#a89a72" stroke-width="5"/>'
         f'<path d="M0-34q-20 12-30 0 12-16 30-6z" fill="#a89a72" stroke="{INK}" stroke-width="2"/></g>' for i in range(3))}
<g transform="translate(430 300)"><path d="M-56 0q0 34 56 34t56-34z" fill="#fffefd" class="o"/>
  <ellipse cy="0" rx="56" ry="16" fill="#eef2f4" class="o"/></g>
{head(200, 330, 26, 'coral', 'short')}
<path d="M164 300q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

# --- 大きさ・数 ---------------------------------------------------------------

add('enlargement', '小さな絵を、大きく引きのばす', f'''
<g transform="translate(140 200)"><rect x="-60" y="-46" width="120" height="92" rx="6" fill="#f7f3e8" class="o"/>
  <path d="M-46 34l34-46 24 24 22-30 34 52z" class="greenp o"/>
  {sun(30, -22, 12)}</g>
<path d="M230 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(430 200)"><rect x="-140" y="-110" width="280" height="220" rx="8" fill="#f7f3e8" class="o"/>
  <path d="M-110 80l80-110 56 56 52-72 80 126z" class="greenp o"/>
  {sun(70, -52, 28)}</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 7">
  <path d="M200 154L290 90M200 246L290 310"/></g>''', arrow=True)

add('elevation', 'ふもとから頂上までの、高さ', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<path d="M60 340L300 90l240 250z" fill="#c3cbd1" class="o"/>
<path d="M300 90l50 60h-100z" fill="#fffefd" class="o"/>
<path d="M560 340v-250" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 7"/>
<path d="M300 90h260M300 340h260" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 7"/>
<path d="M560 100v230" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
{ring(300, 120, 62)}''', arrow=True)

add('expensive', 'ねだんが高く、たくさん払わないと買えない', f'''
{table(330)}
{box(200, 280, 130, 96, 28, 'violet')}
<g transform="translate(430 190) rotate(-10)"><path d="M-56-34h96l24 34-24 34h-96z" class="paper"/>
  <circle cx="46" cy="0" r="7" class="ink"/>
  {''.join(coin(-30 + i*26, 0, 13) for i in range(3))}</g>
{''.join(coin(360 + i*40, 300, 22) for i in range(4))}
{''.join(spark(x, y, 0.8) for x, y in [(130,140),(280,120)])}''')

add('electron', '原子のまわりを回る、小さな粒', f'''
<circle cx="300" cy="200" r="56" class="coral o"/>
{''.join(f'<ellipse cx="300" cy="200" rx="180" ry="70" fill="none" stroke="{MUTED}" stroke-width="4" transform="rotate({a} 300 200)"/>' for a in [0, 60, 120])}
{''.join(f'<circle cx="{300+180*math.cos(math.radians(a))*math.cos(math.radians(r))-70*math.sin(math.radians(a))*math.sin(math.radians(r)):.0f}" cy="{200+180*math.cos(math.radians(a))*math.sin(math.radians(r))+70*math.sin(math.radians(a))*math.cos(math.radians(r)):.0f}" r="16" class="teal o"/>' for a, r in [(20, 0), (200, 60), (110, 120)])}
{ring(480, 200, 40)}''')

add('equilibrium', 'くぼみの底で、玉がそれ以上動かず落ち着く', f'''
<path d="M60 120q240 260 480 0" fill="none" stroke="{TEAD}" stroke-width="12"/>
<circle cx="300" cy="266" r="34" class="coral o"/>
<g fill="none" class="a" stroke-width="5">
  <path d="M180 200l50 40" marker-end="url(#ar)"/><path d="M420 200l-50 40" marker-end="url(#ar)"/></g>
<g opacity="0.35"><circle cx="160" cy="196" r="28" class="coralp o"/><circle cx="440" cy="196" r="28" class="coralp o"/></g>''', arrow=True)

add('estimation', 'ざっと見て、だいたいの数を見積もる', f'''
{table(330)}
{''.join(f'<circle cx="{110+ (i%5)*44}" cy="{280-(i//5)*40}" r="18" class="goldp o"/>' for i in range(15))}
{head(430, 200, 30, 'teal', 'bun')}
<path d="M390 220l-70 30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(500 300)"><rect x="-60" y="-46" width="120" height="92" rx="6" class="paper"/>
  <path d="M-30-10q20-24 40 0t0 0" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-30 20q20-24 40 0" fill="none" stroke="{INK}" stroke-width="7"/></g>''')

add('elimination', '勝ち残る側から、負けた側が消されていく', f'''
{''.join(f'<g transform="translate(80 {70+i*80})">{head(0, 0, 24, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun')]))}
<g fill="none" stroke="{MUTED}" stroke-width="5">
  <path d="M116 70h60v80h-60M116 230h60v80h-60"/><path d="M176 110h60M176 270h60"/></g>
<g fill="none" stroke="{CRL}" stroke-width="6"><path d="M236 110h60v160h-60"/><path d="M296 190h60"/></g>
{head(400, 190, 28, 'teal', 'short')}
{''.join(f'<g transform="translate(80 {150+i*160})"><path d="M-20-20l40 40M20-20l-40 40" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/></g>' for i in range(2))}
{''.join(f'<g opacity="0.35"><g transform="translate(80 {150+i*160})">{head(0, 0, 24, "violet", "bob")}</g></g>' for i in range(0))}''')

add('exemption', 'みんなが払うなか、この人だけ免じられて通される', f'''
<g transform="translate(300 200)"><rect x="-30" y="-150" width="60" height="300" rx="8" class="teald o"/></g>
{''.join(f'<g transform="translate({80+i*80} 330)">{head(0, 0, 24, c, h)}{coin(0, -50, 16)}</g>' for i, (c, h) in enumerate([('coral','short'),('gold','bob')]))}
<g transform="translate(430 330)">{head(0, 0, 26, 'teal', 'short')}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"><circle cx="430" cy="280" r="18"/></g>
<path d="M340 200h100" class="a" stroke-width="6" marker-end="url(#ar)"/>
{ring(430, 306, 84)}''', arrow=True)

# --- 掘る・取り出す -----------------------------------------------------------

add('excavation', '重機で土を掘り下げ、大きな穴をあける', f'''
<path d="M0 260h600v140H0z" fill="#d9c9a4"/>
<path d="M240 260q10 100 90 100h140q40 0 50-100z" fill="#fffaf1" class="o"/>
<g transform="translate(160 250)">
  <path d="M-90 40v-50h110v50z" class="gold o"/>
  <path d="M20-10h50v-40h-50z" class="goldd o"/>
  <circle cx="-50" cy="48" r="24" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle cx="40" cy="48" r="24" fill="none" stroke="{INK}" stroke-width="8"/>
  <path d="M60-40l90-60" fill="none" stroke="{GLDD}" stroke-width="12"/>
  <path d="M150-100l60 40" fill="none" stroke="{GLDD}" stroke-width="12"/>
  <path d="M200-64q30 20 20 54l-56-14z" fill="#8d949a" class="o"/></g>''')

add('extraction', 'やっとこで、悪い歯を抜き取る', f'''
<g transform="translate(240 250)">
  {''.join(f'<path d="M{-140+i*70} 40q-16-70 0-84 34-14 68 0 16 14 0 84z" fill="#fffefd" class="o"/>' for i in range(4))}
  <path d="M-140-44h278" fill="none" stroke="#e3e8eb" stroke-width="0"/></g>
<g transform="translate(310 200)"><path d="M-40 40q-16-70 0-84 34-14 68 0 16 14 0 84z" fill="#e8cf9a" class="o"/></g>
<g transform="translate(340 100) rotate(14)">
  <path d="M-30 0l-16-70M30 0l16-70" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-30 0q30 40 60 0" fill="none" stroke="{INK}" stroke-width="9"/></g>
<path d="M340 60v-40" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('embargo', '港で船が止められ、荷を通せない', f'''
<path d="M0 300h600v100H0z" fill="{BLUP}"/>
<g transform="translate(180 290)"><path d="M-120 0h240l-40 50h-160z" class="coral o"/>
  <path d="M-70 0v-60h120v60z" fill="#fffefd" class="o"/>
  <path d="M-40-60v-30h30v30z" class="corald o"/></g>
<path d="M330 100v260" fill="none" stroke="{CRL}" stroke-width="16"/>
<path d="M330 160h180" fill="none" stroke="{CRL}" stroke-width="16"/>
<g transform="translate(470 300)"><path d="M-90 0v-40h180V0z" class="goldd o"/></g>
{''.join(box(430 + i*70, 300, 60, 44, 14, 'gold') for i in range(2))}
<path d="M300 240h-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

# --- 見せかけ・確かめ ---------------------------------------------------------

add('exaggeration', '小さな魚を、これほど大きかったと語る', f'''
{person(180, 306, 1.25, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<path d="M110 190h150" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<path d="M110 150v80M260 150v80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>
<g transform="translate(430 260)"><path d="M-40 0q26-24 60-8 16 8 0 16-34 16-60-8z" class="teal o"/>
  <path d="M20 4l24-14v28z" class="teal o"/>
  <circle cx="-24" cy="-2" r="4" class="ink"/></g>
<g transform="translate(430 160)"><ellipse rx="80" ry="52" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/>
  <path d="M-56 0q40-40 92-12 24 12 0 24-52 26-92-12z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g>
<path d="M300 190h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('fabrication', 'もとになる事実もないのに、話をこしらえる', f'''
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9">
  <rect x="60" y="150" width="140" height="110" rx="8"/></g>
<path d="M220 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(370 200)"><rect x="-80" y="-100" width="160" height="200" rx="10" class="teald o"/>
  <rect x="-60" y="-80" width="120" height="60" rx="4" fill="#dfe6ea"/></g>
<path d="M460 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(540 210) rotate(-6)"><rect x="-50" y="-64" width="100" height="128" rx="4" class="paper"/>
  <rect x="-36" y="-46" width="72" height="10" rx="5" class="coral"/>
  {''.join(f'<rect x="-36" y="{-20+i*20}" width="{62-(i%2)*20}" height="8" rx="4" fill="{MUTED}"/>' for i in range(3))}</g>''', arrow=True)

add('fact-check', '書かれた主張を、もとの資料と突き合わせる', f'''
<g transform="translate(150 200)"><rect x="-90" y="-110" width="180" height="220" rx="8" class="paper"/>
  {''.join(f'<rect x="-66" y="{-76+i*46}" width="{130-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}</g>
<g transform="translate(450 200)"><path d="M-90-110h180v220h-180z" class="teal o"/>
  <path d="M-90-110h20v220h-20z" class="teald o"/>
  <rect x="-40" y="-60" width="100" height="12" rx="6" fill="#fffefd"/></g>
<path d="M256 200h130" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
<g transform="translate(300 320)"><path d="M-30 0l24 26 48-56" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>''', arrow=True)

add('examiner', '試験の場を見まわり、答案を採点する', f'''
{table(300)}
{''.join(f'<g transform="translate({120+i*110} 380)">{head(0, 0, 24, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short')]))}
{''.join(f'<g transform="translate({120+i*110} 286)"><rect x="-40" y="-24" width="80" height="48" rx="4" class="paper"/></g>' for i in range(3))}
{person(490, 380, 1.25, -1, 'violet', 'blue', 'point', 'bun', 'neutral')}
<g transform="translate(470 250) rotate(20)"><path d="M-8-70h16v90l-8 16-8-16z" class="coral o"/></g>
<path d="M420 200h-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('feasibility', 'できるかどうかを、手もとの材料と照らして確かめる', f'''
<g transform="translate(160 190)"><rect x="-110" y="-120" width="220" height="240" rx="8" fill="#2f5f8e" class="o"/>
  <g fill="none" stroke="#dce9f5" stroke-width="4">
    <path d="M-80 90v-80l80-60 80 60v80z"/><path d="M-30 90v-50h60v50"/></g></g>
<path d="M290 200h50" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
{''.join(f'<g transform="translate({430+ (i%2)*80} {140+(i//2)*90})">{box(0, 0, 66, 48, 16, c)}</g>' for i, c in enumerate(['gold','teal','coral','violet']))}
<g transform="translate(300 330)"><path d="M-30 0l24 26 48-56" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>''', arrow=True)

# --- 学び・組織 ---------------------------------------------------------------

add('enrolment', '名簿に名前を書き入れて、講座に加わる', f'''
{table(300)}
{doc(230, 200, 200, 240, 0)}
{''.join(f'<g><circle cx="150" cy="{120+i*46}" r="9" class="tealp o"/>'
         f'<rect x="172" y="{112+i*46}" width="{130-(i%2)*40}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(4))}
<rect x="172" y="296" width="110" height="14" rx="7" class="coral"/>
<g transform="translate(340 250) rotate(30)"><path d="M-8-80h16v100l-8 18-8-18z" class="coral o"/></g>
{person(480, 380, 1.2, -1, 'teal', 'blue', 'reach', 'short', 'smile')}''')

add('fellowship', '同じ卓を囲み、語り合って過ごす', f'''
<g transform="translate(300 240)"><ellipse rx="180" ry="70" fill="#c9a464" class="o"/>
  <ellipse rx="150" ry="52" fill="#d9b57a"/></g>
{''.join(f'<g transform="translate({x} {y})">{head(0, 0, 26, c, h)}</g>'
         for x, y, (c, h) in zip([120, 300, 480, 200, 400], [240, 150, 240, 330, 330],
             [('teal','short'),('coral','bob'),('violet','short'),('gold','bun'),('green','cap')]))}
{''.join(f'<g transform="translate({x} 240)"><ellipse rx="30" ry="9" fill="#fffefd" class="o"/></g>' for x in [230, 370])}
{''.join(spark(x, y, 0.7) for x, y in [(90,120),(510,120)])}''')

add('empowerment', '道具とかぎを渡され、自分でできるようになる', f'''
{person(140, 306, 1.2, 1, 'violet', 'blue', 'give', 'bun', 'smile')}
<g transform="translate(250 220)"><rect x="-30" y="-14" width="44" height="28" rx="6" class="gold o"/>
  <path d="M14-6h50v12h-14v10h-10v-10h-26z" class="gold o"/></g>
<path d="M320 200h60" class="a" marker-end="url(#ar)"/>
{person(470, 306, 1.3, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{''.join(spark(x, y, 0.9) for x, y in [(400,120),(550,140)])}''', arrow=True)

add('enlightenment', '暗がりが明け、はっと道理が見えてくる', f'''
{split()}
<g transform="translate(150 200)"><rect x="-110" y="-140" width="220" height="280" rx="10" fill="#2a3340"/>
  {head(150, 210, 30, 'teal', 'short')}</g>
{ring(150, 200, 138, True)}
<g transform="translate(450 200)"><rect x="-110" y="-140" width="220" height="280" rx="10" fill="#fff6d8" class="o"/>
  {sun(450, 130, 40)}
  {head(450, 250, 30, 'teal', 'short')}</g>
{''.join(spark(x, y, 0.9) for x, y in [(370,110),(540,290)])}
{ring(450, 200, 138)}''')

add('epoch', '長い時の流れを区切る、大きな節目', f'''
<path d="M40 200h520" fill="none" stroke="{MUTED}" stroke-width="6" marker-end="url(#ar)"/>
<path d="M300 90v220" fill="none" stroke="{CRL}" stroke-width="10"/>
{''.join(f'<circle cx="{90+i*50}" cy="200" r="12" class="tealp o"/>' for i in range(4))}
{''.join(f'<circle cx="{350+i*50}" cy="200" r="12" class="violetp o"/>' for i in range(4))}
<g transform="translate(160 300)"><rect x="-80" y="-24" width="160" height="48" rx="10" class="tealp o"/></g>
<g transform="translate(440 300)"><rect x="-80" y="-24" width="160" height="48" rx="10" class="violetp o"/></g>
{ring(300, 200, 60)}''', arrow=True)

add('dynasty', '同じ一族が、代々かんむりを受けつぐ', f'''
{''.join(f'<g transform="translate({110+i*130} 250)">{head(0, 0, 30, c, h)}{crown(0, -46, 0.6)}</g>'
         for i, (c, h) in enumerate([('violet','bun'),('teal','short'),('coral','bob'),('gold','short')]))}
{''.join(f'<path d="M{160+i*130} 250h50" class="a" marker-end="url(#ar)"/>' for i in range(3))}
<path d="M60 340h480" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>''', arrow=True)

add('encore', '拍手にこたえて、演者がもう一度舞台に出る', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<g opacity="0.5"><path d="M300 190L170 306h260z" class="goldp"/></g>
{person(300, 306, 1.25, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
<path d="M180 130q60-60 130 0" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>
{''.join(f'<g transform="translate({x} 380)">{head(0, 0, 26, c, h)}</g>' for x, (c, h) in zip([70, 160, 440, 530], [('teal','short'),('violet','bob'),('green','short'),('gold','cap')]))}
{''.join(f'<g transform="translate({x} 320)">{hand(-14, 0, 1)}{hand(14, 0, -1)}</g>' for x in [115, 485])}''', arrow=True)

# --- 性質・才 ----------------------------------------------------------------

add('elegance', 'むだのない、流れるような線の美しさ', f'''
<g transform="translate(300 220)">
  <path d="M-180 100q60-200 180-200t180 200" fill="none" stroke="{VIO}" stroke-width="8"/>
  <path d="M-140 110q50-160 140-160t140 160" fill="none" stroke="{VIOP}" stroke-width="6"/></g>
<g transform="translate(300 300)"><path d="M-46 0q-16-70 0-90 46-20 92 0 16 20 0 90z" class="violetp o"/>
  <path d="M-50-90q50 16 100 0" fill="none" stroke="{VIO}" stroke-width="4"/>
  <path d="M0-90v-40" fill="none" stroke="{VIOD}" stroke-width="6"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(120,120),(490,120)])}''')

add('extrovert', '人の輪のまん中で、生き生きと話す', f'''
{person(300, 320, 1.25, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{''.join(f'<g transform="translate({300+180*math.cos(math.radians(a)):.0f} {250+120*math.sin(math.radians(a)):.0f})">{head(0, 0, 26, c, h)}</g>'
         for a, (c, h) in zip([200, 250, 290, 340], [('teal','short'),('violet','bob'),('gold','bun'),('green','cap')]))}
{''.join(f'<path d="M{300+90*math.cos(math.radians(a)):.0f} {250+60*math.sin(math.radians(a)):.0f}L{300+140*math.cos(math.radians(a)):.0f} {250+94*math.sin(math.radians(a)):.0f}" class="a" marker-end="url(#ar)"/>' for a in [200, 250, 290, 340])}
{''.join(spark(x, y, 0.8) for x, y in [(200,110),(410,100)])}''', arrow=True)

add('flair', 'だれもが同じに描くなか、ひとふでで見ちがえる', f'''
{split()}
{''.join(f'<g transform="translate({90+ (i%2)*110} {160+(i//2)*110})"><rect x="-44" y="-40" width="88" height="80" rx="6" class="paper"/>'
         f'<path d="M-28 20l24-36 20 20 20-24 24 40z" fill="#d8dfe2"/></g>' for i in range(4))}
{ring(150, 210, 132, True)}
<g transform="translate(450 210)"><rect x="-110" y="-100" width="220" height="200" rx="8" class="paper"/>
  <path d="M-80 60l60-96 44 44 40-56 62 108z" class="greenp o"/>
  {sun(56, -48, 24)}
  <path d="M-80-60q60 40 130-10" fill="none" stroke="{CRL}" stroke-width="6"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(370,110),(540,120)])}
{ring(450, 210, 138)}''')

add('familiarity', 'よく知った道具は、見なくても手が動く', f'''
{table(330)}
{person(230, 306, 1.25, 1, 'teal', 'blue', 'carry', 'short', 'smile')}
<path d="M206 200l14 6M254 200l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(300 250) rotate(20)"><path d="M-8 0h16v70h-16z" class="goldd o"/>
  <path d="M-30-30h60v26h-60z" class="ink"/></g>
<g transform="translate(450 280)"><path d="M-60 26q-14-60 0-70 60-16 120 0 14 10 0 70z" class="corald o"/></g>
{''.join(f'<path d="M{330+i*30} {160+i*14}q14-16 28 0" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('fit in', '同じ形の仲間のなかに、ぴたりとおさまる', f'''
{''.join(f'<g transform="translate({120+i*110} 220)"><path d="M-44-44h88v88h-88z" class="teal o"/></g>' for i in range(3))}
<g transform="translate(450 220)"><path d="M-44-44h88v88h-88z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/></g>
<g transform="translate(450 100)"><path d="M-44-44h88v88h-88z" class="coral o"/></g>
<path d="M450 156v30" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('flicker', 'ともしびが、ついたり消えたりする', f'''
{table(340)}
{''.join(f'<g transform="translate({130+i*110} 306)"><path d="M-24-100h48v100h-48z" fill="#fffefd" class="o"/>'
         f'<path d="M0-100v-12" fill="none" stroke="{INK}" stroke-width="4"/></g>' for i in range(4))}
{''.join(f'<g transform="translate({121+i*220} 194) scale(0.42)">{flame(0, 0, 1)}</g>' for i in range(2))}
{''.join(f'<g transform="translate({231+i*220} 194)"><path d="M0 0c-12-6-14-24-2-36 2 9 7 10 9 5 2-8 9-13 12-19 4 13 12 15 12 26C43-10 20 6 0 0z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/></g>' for i in range(2))}
{''.join(f'<path d="M{175+i*110} 130h30" class="a" marker-end="url(#ar)"/>' for i in range(3))}''', arrow=True)

# --- 慣用 --------------------------------------------------------------------

add('face the music', '逃げずに向き合い、結果を受け止める', f'''
<g transform="translate(430 200)"><rect x="-140" y="-90" width="280" height="60" rx="8" class="goldd o"/>
  {''.join(f'<g transform="translate({-90+i*90} -120)">{head(0, 0, 26, c, h)}</g>' for i, (c, h) in enumerate([('violet','bun'),('teal','short'),('coral','bob')]))}</g>
{person(150, 340, 1.3, 1, 'blue', 'blue', 'stand', 'short', 'neutral')}
<path d="M220 250h100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g opacity="0.3"><path d="M110 340q-60-40-60-120" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="11 9"/>
  <path d="M50 220l-12 18M50 220l12 18" fill="none" stroke="{MUTED}" stroke-width="5"/></g>''')

add('embodiment', '形のない考えが、姿をもって目の前に立つ', f'''
<g transform="translate(150 200)"><path d="M0 40q-50-40-50-72 0-26 26-26 14 0 24 16 10-16 24-16 26 0 26 26 0 32-50 72z" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="11 9"/></g>
<path d="M250 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 306)"><path d="M-80 0v-30h160V0z" class="goldd o"/></g>
{person(450, 276, 1.25, 1, 'violet', 'blue', 'up', 'bun', 'smile')}
{''.join(spark(x, y, 0.9) for x, y in [(370,120),(540,130)])}''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
