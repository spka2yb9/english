# -*- coding: utf-8 -*-
"""第148回。re- の形容詞と動詞、pr-/r- の名詞。"""
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

def star(x, y, s=1):
    pts = []
    for i in range(10):
        r = 26*s if i % 2 == 0 else 11*s
        a = math.radians(-90 + i*36)
        pts.append(f'{x + r*math.cos(a):.0f} {y + r*math.sin(a):.0f}')
    return f'<path d="M{"L".join(pts)}z" class="gold o"/>'

def gauge(x, y, level, w=160):
    return (f'<g transform="translate({x} {y})"><rect x="{-w/2}" y="-18" width="{w}" height="36" rx="18" fill="#fffefd" class="o"/>'
            f'<rect x="{-w/2+4}" y="-14" width="{(w-8)*level:.0f}" height="28" rx="14" class="green"/></g>')

def lion(x, y, s=1):
    mane = ''.join(f'<circle cx="{74*math.cos(math.radians(a)):.0f}" cy="{74*math.sin(math.radians(a)):.0f}" r="26" fill="#c98f3c" stroke="{INK}" stroke-width="2.5"/>' for a in range(0, 360, 30))
    return (f'<g transform="translate({x} {y}) scale({s})">{mane}'
            f'<circle r="70" fill="#e0a94e" class="o"/>'
            f'<circle cx="-26" cy="-22" r="6" class="ink"/><circle cx="26" cy="-22" r="6" class="ink"/>'
            f'<path d="M-40 14q40-24 80 0 0 44-40 44t-40-44z" fill="#7a2f28" class="o"/>'
            f'<path d="M-22 18q22-8 44 0-8 14-22 14t-22-14z" fill="#f2c29d"/>'
            f'<path d="M-10-6h20l-10 12z" class="ink"/></g>')

# --- ことば・音 --------------------------------------------------------------

add('pronunciation', '口の形をまねて、同じ音を出してみる', f'''
<g transform="translate(170 200)"><ellipse rx="110" ry="80" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-56 6q56-46 112 0-56 60-112 0z" fill="#7a2f28" class="o"/>
  <path d="M-40 6q40-14 80 0" fill="none" stroke="#fffefd" stroke-width="9"/>
  <path d="M-30 26q30 18 60 0" fill="none" stroke="{CRL}" stroke-width="9"/></g>
{''.join(f'<path d="M296 {200-22-i*22}q{22+i*22} {22+i*22} 0 {(22+i*22)*2}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(3))}
{head(490, 240, 40, 'teal', 'bob')}
<path d="M470 262q20 16 40 0" fill="none" stroke="{INK}" stroke-width="4"/>
{''.join(f'<path d="M{542+i*0} {206-i*16}q14 14 0 28" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(1))}''')

add('roar', '口を大きく開けて、地ひびきのような声をとどろかせる', f'''
{lion(200, 200, 1.0)}
{''.join(f'<path d="M300 {200-24-i*26}q{24+i*26} {24+i*26} 0 {(24+i*26)*2}" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round"/>' for i in range(4))}
{head(540, 260, 26, 'teal', 'short')}
<path d="M566 216q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('rhythmic', '一定の間かくで、規則正しく打ちつづける', f'''
<g transform="translate(140 250)"><path d="M-70 60V-20q70-26 140 0V60z" class="coral o"/>
  <ellipse cy="-20" rx="70" ry="24" fill="#f3e9d6" class="o"/>
  <path d="M-70-20q70 26 140 0" fill="none" stroke="{CRLD}" stroke-width="3"/></g>
<g transform="translate(126 130) rotate(-24)"><path d="M-6 0h12v90h-12z" class="goldd o"/><circle cy="-6" r="14" class="gold o"/></g>
<path d="M260 240h300" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<rect x="{278+i*54}" y="{190 if i%2==0 else 210}" width="24" height="{50 if i%2==0 else 30}" rx="5" class="teal o"/>' for i in range(6))}
{''.join(f'<circle cx="{290+i*54}" cy="270" r="8" class="coral o"/>' for i in range(6))}''')

add('repetition', '同じ印を、判で押したように並べる', f'''
<g transform="translate(150 160) rotate(-14)"><path d="M-30 40h60v20h-60z" class="teald o"/>
  <path d="M-16-40h32v80h-32z" class="teal o"/><path d="M-30-56h60v18h-60z" class="teald o"/></g>
{table(320)}
{''.join(f'<circle cx="{250+i*74}" cy="272" r="26" class="coralp o"/>' for i in range(5))}
{''.join(f'<circle cx="{250+i*74}" cy="272" r="12" class="coral o"/>' for i in range(5))}
<path d="M226 200l30 40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('repetitive', '同じ動きを、何度も何度もくり返す', f'''
{person(280, 306, 1.3, 1, 'teal', 'blue', 'hold', 'short', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9">
  <path d="M300 236q60-40 96 4M300 236q60 10 90 56"/></g>
<g transform="translate(430 200)"><path d="M-56 0a56 56 0 1 1 20 42" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/></g>
<path d="M186 190q16-18 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<path d="M{140-i*0} {250+i*24}h30" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''', arrow=True)

add('rewrite', '書きなぐった下書きを捨て、新しく書き直す', f'''
{table(330)}
<g transform="translate(160 200) rotate(-8)">{doc(0, 0, 170, 220, 5)}
  <path d="M-70-80l140 160M70-80l-140 160" fill="none" stroke="{MUTED}" stroke-width="6"/></g>
<path d="M280 200h60" class="a" marker-end="url(#ar)"/>
{doc(440, 200, 170, 220, 5)}
<g transform="translate(530 130) rotate(30)"><path d="M-7-90h14v120l-7 20-7-20z" class="coral o"/></g>''', arrow=True)

# --- 気持ち ------------------------------------------------------------------

add('regretful', '乗りそこねた列車を見送り、残念に思う', f'''
<path d="M0 330h600v14H0z" class="goldd o"/>
<g transform="translate(430 250) "><path d="M-140 60V-40q0-30 30-30h220V60z" class="teal o"/>
  {''.join(f'<rect x="{-120+i*60}" y="-24" width="44" height="40" rx="5" class="tealp o"/>' for i in range(4))}
  <circle cx="-100" cy="66" r="18" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="60" cy="66" r="18" fill="none" stroke="{INK}" stroke-width="7"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M256 240h-40M266 280h-50"/></g>
{person(120, 330, 1.2, 1, 'coral', 'blue', 'reach', 'short', 'sad')}''')

add('remorseful', '傷つけた相手に、深く頭を下げてあやまる', f'''
{person(430, 306, 1.2, -1, 'teal', 'blue', 'stand', 'bob', 'neutral')}
<g transform="translate(200 306)">
  <path d="M-14-8l-8 34M14-8l8 34" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-78q26-13 52 0l-8 72h-36z" fill="{CRL}" class="o"/>
  <path d="M-22-72q-16 30-10 56M22-72q16 30 10 56" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <g transform="translate(30 -66) rotate(66)"><circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="{HAIRS['short']}" transform="translate(0 108) scale(1.08)" fill="{HAIR}"/>
    <circle cx="-9" cy="-4" r="2.6" class="ink"/><circle cx="9" cy="-4" r="2.6" class="ink"/>
    <path d="M-8 12q8-8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
</g>
{drop(258, 200, 1.0)}
<path d="M300 160q40-30 80 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('remorseless', 'あやまる相手を見おろし、まるで容赦しない', f'''
{person(400, 306, 1.3, -1, 'violet', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(180 306)">
  <path d="M-40 0h80v-16h-80z" fill="none"/>
  <path d="M-16-40h60v40h-70z" class="coral o"/>
  <path d="M-40-40q-16 0-16 20t16 20" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <path d="M20-40l30-30" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="60" cy="-84" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bob']}" transform="translate(60 24) scale(1)" fill="{HAIR}"/>
  <circle cx="52" cy="-80" r="2.4" class="ink"/><circle cx="70" cy="-80" r="2.4" class="ink"/>
  <path d="M52-66q8-8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
<g transform="translate(280 160)"><rect x="-56" y="-34" width="112" height="68" rx="16" class="paper"/>
  <path d="M-40 30l-20 26 4-26z" class="paper"/>
  <path d="M-20 0h40" fill="none" stroke="{MUTED}" stroke-width="6"/></g>
<path d="M340 250h-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('resentful', '横目でにらみ、腹に据えかねている', f'''
<g transform="translate(180 306)">
  <path d="M-6-34h40v34" fill="none" stroke="{TONES['blue'][2]}" stroke-width="17" stroke-linecap="round"/>
  <path d="M-28-34q28-12 56 0l-8-52h-40z" fill="{VIO}" class="o"/>
  <path d="M-30-64l58 14M30-66l-58 16" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/>
  <circle cx="0" cy="-114" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 -6)" fill="{HAIR}"/>
  <circle cx="10" cy="-116" r="3" class="ink"/><circle cx="-6" cy="-116" r="3" class="ink"/>
  <path d="M-16-126l14 6M16-126l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-9-98q9 8 18 0" fill="none" stroke="{INK}" stroke-width="3"/></g>
<g opacity="0.7">{cloud(180, 130, 1.2, 'violet')}</g>
{person(450, 306, 1.15, -1, 'teal', 'blue', 'stand', 'bun', 'smile')}
<path d="M240 190l150 20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('restless', 'いすの上で、じっとしていられない', f'''
{chair(300, 330, 1.2, 'gold', -1)}
<g opacity="0.3">{sit(266, 330, 1.15, 1, 'coral', 'blue', 'short', 'neutral', 'up')}</g>
<g opacity="0.3">{sit(330, 330, 1.15, -1, 'coral', 'blue', 'short', 'neutral', 'down')}</g>
{sit(300, 330, 1.2, 1, 'coral', 'blue', 'short', 'neutral', 'lap')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M170 180q16-20 0-40M430 180q-16-20 0-40M160 250h-30M440 250h30"/></g>''')

add('rebellious', 'みんなが同じ向きに進むなか、ひとりだけ逆を向く', f'''
{''.join(f'<g transform="translate({100+i*100} 306)">{person(0, 0, 0.95, 1, "teal", "blue", "walk", "short", "neutral")}</g>' for i in range(4))}
{person(520, 306, 1.0, -1, 'coral', 'green', 'walk', 'bob', 'neutral')}
<path d="M100 120h300" class="a" marker-end="url(#ar)"/>
<path d="M560 120h-70" class="a" stroke="{CRL}" marker-end="url(#ar)"/>''', arrow=True)

add('receptive', '扉を開け、両手を広げて受け入れる', f'''
<g transform="translate(300 306)"><path d="M-120 0v-200h240V0z" fill="none" stroke="{GLDD}" stroke-width="8"/></g>
<g transform="translate(180 210) rotate(-30)"><path d="M0-96h108v192H0z" class="goldp o"/><circle cx="90" cy="10" r="7" class="ink"/></g>
{person(360, 306, 1.15, -1, 'teal', 'blue', 'up', 'bun', 'smile')}
{box(520, 200, 80, 58, 18, 'coral')}
<path d="M470 210h-40" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('reckless', '警告を無視して、猛スピードで突っこむ', f'''
{warn(500, 150, 1.2) if False else ''}
<g transform="translate(500 160)"><path d="M0-44l44 76h-88z" class="gold o"/>
  <path d="M0-16v22" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="18" r="4" class="ink"/></g>
<g transform="translate(250 280)">
  <path d="M-120 0v-40l34-46h150l36 46V0z" class="coral o"/>
  <path d="M-70-46l20-30h100l24 30z" class="bluep o"/>
  <circle cx="-70" cy="6" r="26" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle cx="80" cy="6" r="26" fill="none" stroke="{INK}" stroke-width="8"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M60 200h-50M40 250h-40M70 300h-50"/></g>
{head(232, 234, 20, 'teal', 'short')}
<path d="M222 230l8 6M242 230l-8 6" fill="none" stroke="{INK}" stroke-width="3"/>''')

add('reconcile', 'あいだに立つ人が、対立していた二人を握手させる', f'''
{person(140, 306, 1.1, 1, 'coral', 'blue', 'give', 'short', 'neutral')}
{person(460, 306, 1.1, -1, 'teal', 'blue', 'give', 'bob', 'neutral')}
<g transform="translate(300 218)">{hand(-18, 0, 1)}{hand(18, 0, -1)}</g>
{person(300, 400, 1.0, 1, 'violet', 'green', 'up', 'bun', 'smile')}
<path d="M226 130q74-40 148 0" fill="none" stroke="{GRN}" stroke-width="5" stroke-dasharray="0"/>
{''.join(spark(x, y, 0.8) for x, y in [(220,100),(380,96)])}''')

# --- 続く・押さえる ----------------------------------------------------------

add('relentless', 'やむことなく打ちつけつづける雨', f'''
{cloud(170, 90, 1.6, 'blue')}{cloud(400, 80, 1.8, 'blue')}
{''.join(f'<path d="M{50+i*36} {150+(i%3)*20}v56" fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round"/>' for i in range(15))}
{''.join(f'<path d="M{68+i*36} {240+(i%3)*18}v46" fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round"/>' for i in range(14))}
{person(300, 380, 1.0, 1, 'coral', 'blue', 'hold', 'short', 'sad')}''')

add('repressive', '大きな手が上から押さえつけて、動けなくする', f'''
<g transform="translate(300 120) scale(2.4 1.6)">{hand(0, 0, 1)}</g>
{''.join(f'<g transform="translate({140+i*110} 350)">{person(0, 0, 0.8, 1, c, "blue", "up", h, "sad")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('violet','bob'),('green','short'),('gold','bun')]))}
<g fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round">
  <path d="M120 214v22M300 220v22M480 214v22"/></g>''')

add('restrictive', '小さな枠に押しこめられ、身動きがとりにくい', f'''
<g transform="translate(300 210)"><rect x="-100" y="-96" width="200" height="192" rx="10" fill="none" stroke="{INK}" stroke-width="9"/></g>
{person(300, 300, 0.86, 1, 'coral', 'blue', 'hold', 'short', 'sad')}
<g fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round">
  <path d="M170 150h-40M430 150h40M170 270h-40M430 270h40"/></g>''')

add('rigid', 'しなる棒と、まったく曲がらない棒の対比', f'''
{split()}
<path d="M90 120q90 80 0 160" fill="none" stroke="{TEA}" stroke-width="18" stroke-linecap="round"/>
{hand(80, 100, 1)}{hand(80, 300, 1)}
{ring(150, 200, 122, True)}
<path d="M450 110v180" fill="none" stroke="{TEAD}" stroke-width="20" stroke-linecap="round"/>
<g fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round">
  <path d="M382 170h-32M382 230h-32M518 170h32M518 230h32"/></g>
{ring(450, 200, 122)}''')

add('punitive', '重い罰を、上からどんと科す', f'''
<g transform="translate(300 150)"><path d="M-90 60V-30q0-30 90-30t90 30V60z" fill="#5b6b78" class="o"/>
  <path d="M-56-30q0-40 56-40t56 40" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-30 20h60v22h-60z" class="ink"/></g>
<path d="M300 216v40" class="a" stroke-width="6" marker-end="url(#ar)"/>
{person(300, 400, 1.0, 1, 'coral', 'blue', 'hold', 'short', 'sad')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M160 250h-40M480 250h40"/></g>''', arrow=True)

add('rampant', '手入れをやめたとたん、雑草が庭じゅうにはびこる', f'''
<g transform="translate(430 306)"><path d="M-80 0v-110h160V0z" fill="#fffefd" class="o"/>
  <path d="M-96-110L0-176l96 66z" class="corald o"/>
  <path d="M-24 0v-56h48V0z" class="teal o"/></g>
{''.join(f'<g transform="translate({40+i*46} {306+(i%3)*8})"><path d="M0 0v-{70+(i%4)*26}" fill="none" stroke="{GRND}" stroke-width="6"/>'
         f'<path d="M0-{40+(i%4)*20}q-34-6-40-40 32 2 40 30zM0-{56+(i%4)*20}q34-8 40-42-34 4-40 32z" class="greenp o"/></g>' for i in range(12))}''')

# --- 立ち直る・もどす --------------------------------------------------------

add('resilient', '押しつぶされても、すぐ元の形にもどる', f'''
<g transform="translate(150 250)"><ellipse rx="76" ry="34" class="teal o"/></g>
{hand(150, 160, 1)}
<path d="M256 250h60" class="a" marker-end="url(#ar)"/>
<circle cx="430" cy="200" r="76" class="teal o"/>
<g fill="none" stroke="{GRN}" stroke-width="6" stroke-linecap="round">
  <path d="M430 96v-26M356 130l-18-18M504 130l18-18"/></g>''', arrow=True)

add('restorative', '休むと、へっていた力がもとまで満ちる', f'''
{split()}
{sit(150, 306, 1.15, 1, 'coral', 'blue', 'short', 'sad', 'down')}
{chair(164, 306, 1.05, 'gold', -1)}
{gauge(150, 110, 0.22, 170)}
{sit(450, 306, 1.15, 1, 'teal', 'blue', 'short', 'smile', 'lap')}
{chair(464, 306, 1.05, 'gold', -1)}
{gauge(450, 110, 1.0, 170)}
<g transform="translate(400 250)"><path d="M-24 0v-42h48V0z" fill="#fffefd" class="o"/>
  <path d="M24-32q22 0 22 14t-22 14" fill="none" class="o"/>
  <path d="M-10-52q-12-16 0-30M10-56q-12-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/></g>''')

add('regenerative', '切られたところから、また新しい芽が伸びる', f'''
{table(340)}
<g transform="translate(180 306)"><path d="M0 0v-80" fill="none" stroke="{GRND}" stroke-width="9"/>
  <path d="M-30-80h60" fill="none" stroke="{CRL}" stroke-width="6" stroke-dasharray="9 7"/></g>
<path d="M260 220h70" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 306)"><path d="M0 0v-80" fill="none" stroke="{GRND}" stroke-width="9"/>
  <path d="M0-80q-6-50 26-70" fill="none" stroke="{GRN}" stroke-width="7"/>
  <path d="M0-80q6-46-26-64" fill="none" stroke="{GRN}" stroke-width="7"/>
  <path d="M26-150q30-6 34-36-30 2-38 30z" class="greenp o"/>
  <path d="M-26-144q-30-8-32-38 30 4 36 32z" class="greenp o"/></g>''', arrow=True)

add('reuse', 'あきびんを捨てず、もう一度使う', f'''
{table(330)}
<g transform="translate(150 306)"><path d="M-34 0v-84q0-18 14-26v-26h40v26q14 8 14 26V0z" class="greenp o"/></g>
<g transform="translate(450 306)"><path d="M-34 0v-84q0-18 14-26v-26h40v26q14 8 14 26V0z" class="greenp o"/>
  <path d="M-28-70h56v64h-56z" class="green"/>
  <path d="M-14-140q14-30 34-8" fill="none" stroke="{GRND}" stroke-width="6"/>
  <path d="M6-160q30-6 34-34-30 4-36 32z" class="greenp o"/></g>
<g transform="translate(300 170)"><path d="M-70 0a70 70 0 1 1 24 52" fill="none" class="a" stroke-width="7" marker-end="url(#ar)"/></g>''', arrow=True)

add('revolve', '中心のまわりを、ぐるりと回る', f'''
<circle cx="300" cy="200" r="60" class="gold o"/>
<ellipse cx="300" cy="200" rx="200" ry="120" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
<circle cx="500" cy="200" r="28" class="teal o"/>
<path d="M470 300q60-40 66-90" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>
<circle cx="160" cy="140" r="18" class="tealp o"/>''', arrow=True)

# --- 評価・程度 --------------------------------------------------------------

add('prophetic', '言い当てたことが、そのとおりに起こる', f'''
{head(140, 250, 40, 'violet', 'bun')}
<g transform="translate(320 150)"><ellipse rx="110" ry="76" fill="#fffefd" class="o"/>
  {cloud(-30, -14, 0.9, 'violet')}
  <path d="M10 10l-20 40h26l-22 44 60-62h-28l20-26z" class="gold o"/></g>
<circle cx="212" cy="212" r="9" fill="#fffefd" class="o"/>
<path d="M440 190h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(530 250)">{cloud(0, -60, 1.0, 'violet')}
  <path d="M8 -20l-18 36h24l-20 40 54-56h-26l18-24z" class="gold o"/></g>''', arrow=True)

add('prosperous', '店に人があふれ、町がにぎわっている', f'''
{''.join(f'<g transform="translate({110+i*160} 306)"><path d="M-70 0v-96h140V0z" fill="#fffefd" class="o"/>'
         f'<path d="M-82-96h164l-22-34h-120z" class="{c} o"/>'
         f'<path d="M-24 0v-56h48V0z" class="{c}d o"/></g>' for i, c in enumerate(['teal','coral','violet']))}
{''.join(head(70 + i*70, 350, 22, c, h) for i, (c, h) in enumerate([('gold','short'),('green','bob'),('blue','short'),('coral','bun'),('teal','cap'),('violet','short'),('gold','bob'),('green','short')]))}
{''.join(coin(x, y, 18) for x, y in [(90,110),(300,80),(520,120)])}
{''.join(spark(x, y, 0.8) for x, y in [(200,90),(420,90)])}''')

add('provisional', '本ものができるまでの、間に合わせの橋', f'''
<path d="M0 306h150v94H0zM450 306h150v94H450z" class="ground"/>
<path d="M150 306l24 94h-24zM450 306l-24 94h24z" fill="#5b6b78"/>
<path d="M150 296h300v18H150z" class="goldd o"/>
{''.join(f'<path d="M{190+i*70} 314v-40" fill="none" stroke="{GLDD}" stroke-width="6"/>' for i in range(4))}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="13 10">
  <path d="M150 240q150-90 300 0"/><path d="M150 240v56M450 240v56"/>
  {''.join(f'<path d="M{190+i*70} {224+int(30*math.sin(math.pi*(i+1)/5))}v{56-int(30*math.sin(math.pi*(i+1)/5))}"/>' for i in range(4))}</g>''')

add('prudent', '渡る前に棒で深さを確かめる', f'''
<path d="M240 306h360v94H240z" fill="{BLUP}"/>
<path d="M240 306h360" fill="none" stroke="{BLU}" stroke-width="5"/>
{person(160, 306, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'neutral')}
<path d="M226 196l150 190" fill="none" stroke="{GLDD}" stroke-width="8" stroke-linecap="round"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M330 330h130"/></g>''')

add('reputable', '評判がよく、いつも人が並ぶ店', f'''
<g transform="translate(400 306)"><path d="M-110 0v-120h220V0z" fill="#fffefd" class="o"/>
  <path d="M-124-120h248l-30-40h-188z" class="teal o"/>
  <path d="M-30 0v-70h60V0z" class="teald o"/></g>
{''.join(star(300 + i*54, 96, 0.9) for i in range(5))}
{''.join(head(70 + i*60, 300, 24, c, h) for i, (c, h) in enumerate([('coral','short'),('violet','bob'),('green','short'),('gold','bun')]))}
<path d="M100 240h180" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('redundant', '四つで足りるところに、五つ目がある', f'''
{''.join(f'<g transform="translate({120+i*100} 220)"><rect x="-40" y="-40" width="80" height="80" rx="10" class="teal o"/></g>' for i in range(4))}
<g transform="translate(520 220)"><rect x="-40" y="-40" width="80" height="80" rx="10" class="tealp o"/></g>
{ring(520, 220, 74, True)}
<path d="M60 320h360" fill="none" stroke="{GRN}" stroke-width="6"/>
<path d="M460 320h120" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/>''')

add('reddish', '真っ赤ではないが、赤みを帯びている', f'''
{''.join(f'<rect x="{80+i*160}" y="130" width="140" height="140" rx="12" fill="{c}" class="o"/>' for i, c in enumerate(['#e2e6e8', '#e6a596', CRL]))}
{ring(310, 200, 96)}''')

add('reflective', '水面が、上のものをそのまま映し返す', f'''
<g transform="translate(300 160)"><path d="M-110 60l70-96 50 52 42-58 68 102z" fill="#c3cbd1" class="o"/>
  {sun(-96, -34, 26)}</g>
<path d="M0 232h600v168H0z" fill="{BLUP}"/>
<path d="M0 232h600" fill="none" stroke="{BLU}" stroke-width="5"/>
<g transform="translate(300 304) scale(1 -1)" opacity="0.45"><path d="M-110 60l70-96 50 52 42-58 68 102z" fill="#c3cbd1"/>
  <circle cx="-96" cy="-34" r="26" class="goldp"/></g>
{''.join(f'<path d="M{80+i*90} {300+(i%3)*30}h60" fill="none" stroke="#ffffff" stroke-width="4" opacity="0.7"/>' for i in range(6))}''')

add('rigorous', 'すべての項目を、ものさしできっちり測って調べる', f'''
{doc(220, 200, 210, 260, 0)}
{''.join(f'<g><rect x="130" y="{110+i*54}" width="18" height="18" rx="4" fill="none" stroke="{INK}" stroke-width="3"/>'
         f'<path d="M131 {120+i*54}l6 7 12-14" fill="none" stroke="{GRN}" stroke-width="4" stroke-linecap="round"/>'
         f'<rect x="162" y="{112+i*54}" width="{130-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/></g>' for i in range(4))}
<g transform="translate(430 200) rotate(12)"><rect x="-30" y="-130" width="60" height="260" rx="6" class="goldp o"/>
  {''.join(f'<path d="M-30 {-110+i*30}h{28 if i%2 else 18}" fill="none" stroke="{GLDD}" stroke-width="3"/>' for i in range(8))}</g>
{head(540, 300, 26, 'teal', 'bun')}''')

add('rudimentary', 'こまかい絵と、線だけのごく簡単な絵の対比', f'''
{split()}
<g transform="translate(150 200)">
  <circle cy="-70" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-36 8q36-24 72 0l-10 92h-52z" class="teal o"/>
  <path d="M-36 8L-70 76M36 8l34 68" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-18 100l-10 60M18 100l10 60" fill="none" stroke="{BLUD}" stroke-width="13" stroke-linecap="round"/>
  <circle cx="-12" cy="-74" r="3.4" class="ink"/><circle cx="12" cy="-74" r="3.4" class="ink"/></g>
{ring(150, 200, 130, True)}
<g transform="translate(450 200)" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round">
  <circle cy="-70" r="30"/><path d="M0-40v80M0-16l-50-14M0-16l50-14M0 40l-40 60M0 40l40 60"/></g>
{ring(450, 200, 130)}''')

# --- 名詞 --------------------------------------------------------------------

add('publisher', '刷り上がった本を次々に世に出す', f'''
<g transform="translate(190 220)"><rect x="-120" y="-70" width="240" height="140" rx="12" class="teal o"/>
  <rect x="-96" y="-46" width="192" height="60" rx="6" fill="#fffefd" class="o"/>
  <circle cx="-60" cy="40" r="16" class="teald o"/><circle cx="60" cy="40" r="16" class="teald o"/></g>
<path d="M320 250h50" class="a" marker-end="url(#ar)"/>
{table(330)}
{''.join(f'<g transform="translate({450+i*8} {300-i*36}) rotate({-4+i*3})"><rect x="-56" y="-16" width="112" height="32" rx="3" class="{c} o"/>'
         f'<rect x="-56" y="-16" width="14" height="32" class="{c}d o"/></g>' for i, c in enumerate(['coral','gold','violet','teal']))}''', arrow=True)

add('receptionist', '受付のカウンターで、来客を迎える', f'''
{table(250)}
<g transform="translate(300 250)"><path d="M-190 0h380v70h-380z" class="teald o"/></g>
{person(200, 250, 1.15, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
<g transform="translate(370 232)"><path d="M-30 18q0-30 30-30t30 30z" class="goldp o"/>
  <circle cy="-16" r="6" class="gold o"/><path d="M-36 18h72v8h-72z" class="goldd o"/></g>
{person(480, 320, 1.15, -1, 'coral', 'green', 'carry', 'short', 'smile')}''')

add('retailer', '大きな倉庫から仕入れ、客に一つずつ売る', f'''
<g transform="translate(120 306)"><path d="M-100 0v-120h200V0z" fill="#d5dbde" class="o"/>
  <path d="M-110-120h220l-30-40h-160z" fill="#9aa6ae" class="o"/>
  <path d="M-40 0v-70h80V0z" class="ink" opacity="0.4"/></g>
<path d="M250 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(400 306)"><path d="M-80 0v-96h160V0z" fill="#fffefd" class="o"/>
  <path d="M-92-96h184l-22-32h-140z" class="coral o"/></g>
{box(400, 250, 60, 42, 14, 'gold')}
{head(540, 300, 26, 'teal', 'short')}
<path d="M470 250h40" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('rehearsal', '客のいない客席の前で、本番前のけいこをする', f'''
<path d="M0 306h600v94H0z" class="ground"/>
{person(220, 306, 1.15, 1, 'coral', 'blue', 'up', 'bun', 'neutral')}
{person(360, 306, 1.1, -1, 'teal', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(300 110)"><rect x="-140" y="-30" width="280" height="24" class="teald o"/>
  <path d="M-110-6v20M0-6v20M110-6v20" fill="none" stroke="{INK}" stroke-width="5"/></g>
{''.join(f'<g transform="translate({70+i*90} 380)">{chair(0, 0, 0.5, "violet", 1)}</g>' for i in range(6))}
{doc(520, 190, 90, 120, 4)}''')

add('ruins', '柱が折れ、草に埋もれた古い遺跡', f'''
<g transform="translate(300 306)">
  {''.join(f'<g transform="translate({-190+i*90} 0)"><path d="M-22 0v-{h}h44V0z" fill="#d5dbde" class="o"/>'
           f'<path d="M-28-{h}h56v14h-56z" fill="#c3cbd1" class="o"/></g>' for i, h in enumerate([150, 90, 170, 60, 130]))}
  <path d="M-230-10h460v10h-460z" fill="#c3cbd1" class="o"/></g>
{''.join(f'<path d="M{60+i*54} 306q-6-30 8-46 6 20 0 46z" class="greenp o"/>' for i in range(10))}
<path d="M150 100h90v20h-90z" fill="#d5dbde" class="o" transform="rotate(-14 195 110)"/>''')

add('reproductive', '花が実になり、種から次の草が育つ', f'''
<g transform="translate(110 306)"><path d="M0 0v-100" fill="none" stroke="{GRND}" stroke-width="7"/>
  {''.join(f'<ellipse cx="0" cy="-124" rx="12" ry="24" class="coral o" transform="rotate({d} 0 -100)"/>' for d in range(0, 360, 60))}
  <circle cy="-100" r="14" class="goldp o"/></g>
<path d="M186 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(300 306)"><path d="M0 0v-70" fill="none" stroke="{GRND}" stroke-width="7"/>
  <circle cy="-100" r="40" class="coral o"/><path d="M0-140v-16" fill="none" stroke="{GRND}" stroke-width="5"/></g>
<path d="M376 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(490 306)"><ellipse cx="0" cy="-14" rx="16" ry="22" class="goldd o"/>
  <path d="M0-36v-40" fill="none" stroke="{GRN}" stroke-width="6"/>
  <path d="M0-58q26-8 30-34-28 4-34 30z" class="greenp o"/></g>''', arrow=True)

add('robotic', 'かくかくした関節で、機械のように動く', f'''
<g transform="translate(300 306)">
  <rect x="-26" y="-60" width="22" height="60" rx="3" class="teald o"/>
  <rect x="4" y="-60" width="22" height="60" rx="3" class="teald o"/>
  <rect x="-60" y="-160" width="120" height="100" rx="8" class="teal o"/>
  <rect x="-110" y="-150" width="46" height="20" rx="4" class="teald o"/>
  <rect x="-124" y="-150" width="20" height="70" rx="4" class="teald o"/>
  <rect x="64" y="-150" width="46" height="20" rx="4" class="teald o"/>
  <rect x="104" y="-172" width="20" height="46" rx="4" class="teald o"/>
  <rect x="-14" y="-180" width="28" height="22" class="teald o"/>
  <rect x="-52" y="-250" width="104" height="70" rx="10" class="tealp o"/>
  <circle cx="-22" cy="-218" r="10" class="ink"/><circle cx="22" cy="-218" r="10" class="ink"/>
  <path d="M-20-196h40" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M0-250v-26" fill="none" stroke="{INK}" stroke-width="5"/><circle cy="-284" r="9" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M110 150h30M110 200h30M460 150h30M460 200h30"/></g>''')

add('rudeness', 'あいさつも順番も無視して、人を押しのける', f'''
{person(300, 306, 1.25, 1, 'coral', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(430 306) rotate(22)">{person(0, 0, 1.05, -1, 'teal', 'green', 'reach', 'bob', 'surprised')}</g>
{head(140, 300, 26, 'violet', 'bun')}
<path d="M104 244q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M392 190h30M400 230h30"/></g>''')

add('quarter', '四つに分けたうちの、ひとつ分', f'''
<circle cx="230" cy="200" r="130" class="goldp o"/>
<path d="M230 200v-130a130 130 0 0 1 130 130z" class="gold o"/>
<path d="M230 200h-130M230 200v130" fill="none" stroke="{GLDD}" stroke-width="4"/>
<g transform="translate(470 200)"><path d="M0-110A110 110 0 0 1 110 0H0z" class="gold o"/></g>
<path d="M380 130h40" class="a" marker-end="url(#ar)"/>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
