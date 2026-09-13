# -*- coding: utf-8 -*-
"""第161回。in- の抽象名詞と慣用表現。"""
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

def torso(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0-190a44 44 0 1 1 0 88 44 44 0 1 1 0-88z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-90-96q90-30 180 0 20 130 0 226h-180q-20-96 0-226z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>')

def scalebar(x, y, tilt=0, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-70" fill="none" stroke="{INK}" stroke-width="7"/><circle cy="-76" r="9" class="ink"/>'
            f'<path d="M-180 0h360" fill="none" stroke="{INK}" stroke-width="7" transform="translate(0 -76) rotate({tilt})"/>'
            f'<path d="M-40 0h80v14h-80z" class="ink"/></g>')

def house(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-80 0v-100h160V0z" fill="#fffefd" class="o"/>'
            f'<path d="M-94-100L0-166l94 66z" class="{cls}d o"/>'
            f'<path d="M-24 0v-56h48V0z" class="{cls} o"/>'
            f'<rect x="-62" y="-82" width="34" height="30" class="{cls}p o"/></g>')

# --- からだ ------------------------------------------------------------------

add('inflammation', 'ぶつけた関節が赤くはれ、熱をもつ', f'''
<g transform="translate(300 200)">
  <path d="M-40-160h80v120h-80z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-44 40h88v130h-88z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse cy="-4" rx="76" ry="60" class="coralp o"/>
  <ellipse cy="-4" rx="46" ry="36" class="coral o"/></g>
<g class="corals" stroke-width="5">{''.join(f'<path d="M300 100v-24" transform="rotate({d} 300 196)"/>' for d in range(0, 360, 45))}</g>''')

add('irritation', 'こすれた肌が赤くなって、かゆくなる', f'''
<g transform="translate(280 220)">
  <path d="M-70-120q70-24 140 0l-16 200q-54 20-108 0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  {''.join(f'<circle cx="{-40+ (i%4)*28}" cy="{-40+(i//4)*30}" r="{7+(i%2)*3}" class="coral" opacity="0.8"/>' for i in range(8))}</g>
{hand(430, 200, -1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M390 160h-30M400 250h-30"/></g>''')

add('inhalation', '鼻から空気を吸いこんで、肺に入れる', f'''
{torso(300, 300, 1.0)}
<g transform="translate(300 210)"><path d="M-14-70h28v50h-28z" class="tealp o"/>
  <path d="M-14-20q-60 0-60 60t34 60 26-50zM14-20q60 0 60 60t-34 60-26-50z" class="tealp o"/></g>
{''.join(f'<path d="M{240+i*60} 60v70" class="a" stroke="{BLU}" stroke-width="6" marker-end="url(#ar)"/>' for i in range(3))}
<path d="M300 130v20" fill="none" stroke="{BLU}" stroke-width="6"/>''', arrow=True)

add('infusion', '管を通して、体に液をゆっくり注ぎ入れる', f'''
<path d="M150 40v40" fill="none" stroke="{INK}" stroke-width="7"/>
<path d="M110 40h80" fill="none" stroke="{INK}" stroke-width="7"/>
<g transform="translate(150 180)"><path d="M-50-100h100v140q0 30-50 30t-50-30z" fill="#eaf4fb" class="o"/>
  <path d="M-44-60h88v98q0 24-44 24t-44-24z" class="bluep"/></g>
<path d="M150 250q0 90 120 90h60" fill="none" stroke="{MUTED}" stroke-width="6"/>
{''.join(drop(150, 254 + i*22, 0.8) for i in range(2))}
<g transform="translate(410 330)"><path d="M-70-30q70-24 140 0l-6 40h-128z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <rect x="-16" y="-34" width="32" height="16" rx="4" class="tealp o"/></g>''')

# --- 入りこむ・流れこむ --------------------------------------------------------

add('infiltration', '見分けがつかない姿で、内側に入りこむ', f'''
<path d="M300 60v300" fill="none" stroke="{INK}" stroke-width="8"/>
{''.join(f'<g transform="translate({390+ (i%2)*100} {200+(i//2)*110})">{head(0, 0, 28, "teal", "short")}</g>' for i in range(4))}
<g transform="translate(490 200)">{head(0, 0, 28, 'teal', 'short')}</g>
{ring(490, 200, 52)}
<path d="M120 200q90-40 150 0t180 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"/>
{head(90, 240, 28, 'violet', 'short')}''', arrow=True)

add('intrusion', '呼ばれてもいないのに、扉を押し開けて入ってくる', f'''
<g transform="translate(300 306)"><path d="M-140 0v-230h280V0z" fill="#fffefd" class="o"/></g>
<g transform="translate(200 210) rotate(-30)"><path d="M0-96h130v192H0z" class="goldp o"/><circle cx="110" cy="10" r="7" class="ink"/></g>
{person(260, 306, 1.2, 1, 'violet', 'blue', 'up', 'short', 'neutral', 'walk')}
{person(470, 306, 1.15, -1, 'teal', 'blue', 'hold', 'bob', 'surprised')}
<g class="corals" stroke-width="6">{''.join(f'<path d="M160 180v-26" transform="rotate({d} 160 220)"/>' for d in [-30, 0, 30])}</g>''')

add('influx', 'あちこちから、いちどにどっと入ってくる', f'''
<g transform="translate(400 210)"><circle r="110" class="tealp o"/>
  {''.join(f'<g transform="translate({50*math.cos(math.radians(a)):.0f} {50*math.sin(math.radians(a)):.0f})">{head(0, 0, 22, c, h)}</g>'
           for a, (c, h) in zip([0, 120, 240], [('teal','short'),('coral','bob'),('gold','bun')]))}</g>
{''.join(f'<path d="M{40+ (i%2)*40} {80+i*70}L{270+ (i%2)*10} {180+i*10}" class="a" stroke-width="6" marker-end="url(#ar)"/>' for i in range(4))}''', arrow=True)

add('irrigation', '水路を引いて、畑のすみずみまで水をまわす', f'''
<path d="M0 200q140-20 300-16t300 16v200H0z" fill="#d9c9a4" class="o"/>
<path d="M0 240h600" fill="none" stroke="{BLU}" stroke-width="20"/>
{''.join(f'<path d="M{100+i*120} 240v130" fill="none" stroke="{BLU}" stroke-width="12"/>' for i in range(4))}
{''.join(f'<g transform="translate({60+ (i%8)*70} {300+(i//8)*60})"><path d="M0 0v-34" fill="none" stroke="{GRND}" stroke-width="5"/>'
         f'<path d="M0-22q-26-4-30-30 24 2 30 22zM0-30q26-6 30-32-24 4-30 24z" class="greenp o"/></g>' for i in range(16))}''')

# --- 妨げ・止める -------------------------------------------------------------

add('inhibition', 'やりたい動きを、内側から引きとめる', f'''
{table(300)}
<g transform="translate(440 268)"><ellipse rx="70" ry="20" fill="#fffefd" class="o"/>
  <path d="M-50-10q0-50 50-50t50 50z" class="coralp o"/></g>
{person(180, 306, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'neutral')}
<path d="M248 214h90" fill="none" stroke="{SKIN}" stroke-width="0"/>
<path d="M120 214q-40 20-40 60" fill="none" stroke="{VIO}" stroke-width="8"/>
<path d="M250 214h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<path d="M320 214l-14-12M320 214l-14 12" fill="none" stroke="{CRL}" stroke-width="5"/>
<g transform="translate(130 130)"><path d="M-40 0h80" stroke="{VIO}" stroke-width="10" stroke-linecap="round" fill="none"/></g>''')

add('injunction', '裁判所の命令で、その動きが止められる', f'''
<g transform="translate(430 250)"><rect x="-110" y="-90" width="220" height="180" rx="12" class="teald o"/>
  <circle cx="0" cy="0" r="46" fill="none" stroke="{TEAP}" stroke-width="12"/>
  {''.join(f'<rect x="-8" y="{-84}" width="16" height="24" rx="4" class="teal o" transform="rotate({d})"/>' for d in range(0, 360, 45))}</g>
<g transform="translate(180 220) rotate(-6)"><rect x="-90" y="-110" width="180" height="220" rx="8" class="paper"/>
  {''.join(f'<rect x="-66" y="{-76+i*46}" width="{130-(i%2)*40}" height="14" rx="7" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="44" cy="66" r="30" fill="none" stroke="{CRL}" stroke-width="6"/></g>
<path d="M290 200h50" fill="none" stroke="{CRL}" stroke-width="10" marker-end="url(#ar)"/>
<path d="M360 160v90" fill="none" stroke="{CRL}" stroke-width="12"/>''', arrow=True)

add('insulation', '壁の断熱材が、内の熱を外へ逃がさない', f'''
<g transform="translate(300 210)">
  <rect x="-40" y="-150" width="80" height="300" fill="#e8dfcd" class="o"/>
  {''.join(f'<path d="M-36 {-140+i*30}q36 14 72 0" fill="none" stroke="#c9b78e" stroke-width="6"/>' for i in range(10))}
  <rect x="-56" y="-150" width="16" height="300" fill="#c3ccd2" class="o"/>
  <rect x="40" y="-150" width="16" height="300" fill="#c3ccd2" class="o"/></g>
{''.join(f'<path d="M120 {120+i*50}h110" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>' for i in range(4))}
{''.join(f'<path d="M{240} {120+i*50}h1" fill="none"/>' for i in range(0))}
{''.join(f'<path d="M400 {130+i*60}h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>' for i in range(3))}''', arrow=True)

add('in vain', '穴のあいた桶に、いくら水を入れてもたまらない', f'''
{table(340)}
<g transform="translate(300 300)"><path d="M-80 0q-16-100 0-110h160q16 10 0 110z" fill="#c9a06c" class="o"/>
  <path d="M-74-70h148" fill="none" stroke="#a8804f" stroke-width="6"/>
  <path d="M-70-20l30 16-26 14 26 12" fill="none" stroke="{CRL}" stroke-width="5"/></g>
<g transform="translate(180 130) rotate(50)"><path d="M-30 0v-70h60V0z" class="blue o"/>
  <path d="M30-54l40-16v40z" class="blue o"/></g>
{''.join(drop(250, 190 + i*30, 1.0) for i in range(3))}
{''.join(drop(200 - i*20, 300 + i*26, 1.0) for i in range(3))}
{head(500, 260, 26, 'teal', 'short')}
<path d="M534 220q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

# --- 伝える・受け取る ---------------------------------------------------------

add('interception', '送られた知らせが、途中でつかまえられる', f'''
{head(80, 250, 28, 'teal', 'short')}
{head(520, 250, 28, 'coral', 'bob')}
<path d="M120 250h150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M330 250h150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<g transform="translate(300 250)"><rect x="-56" y="-36" width="112" height="72" rx="6" class="paper"/>
  <path d="M-56-36L0 12l56-48" fill="none" class="o"/></g>
{hand(300, 140, 1)}
<path d="M300 180v30" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
{ring(300, 250, 84)}''', arrow=True)

add('informant', 'こっそり紙を渡して、内側の話を伝える人', f'''
{person(160, 306, 1.2, 1, 'violet', 'blue', 'give', 'short', 'neutral')}
<g transform="translate(280 230) rotate(-10)"><rect x="-46" y="-30" width="92" height="60" rx="5" class="paper"/>
  {''.join(f'<rect x="-32" y="{-14+i*16}" width="{62-(i%2)*20}" height="7" rx="3.5" fill="{MUTED}"/>' for i in range(2))}</g>
{person(430, 306, 1.2, -1, 'blue', 'blue', 'reach', 'cap', 'neutral')}
<g opacity="0.4"><path d="M540 60v300" fill="none" stroke="{INK}" stroke-width="8"/></g>
{ring(160, 210, 118)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M120 130q40-40 80-10"/></g>''')

add('intermediary', 'あいだに立って、両方のやりとりを取り次ぐ', f'''
{person(110, 306, 1.15, 1, 'teal', 'blue', 'give', 'short', 'neutral')}
{person(490, 306, 1.15, -1, 'coral', 'blue', 'give', 'bob', 'neutral')}
{person(300, 306, 1.2, 1, 'violet', 'green', 'give', 'bun', 'smile')}
{box(210, 200, 66, 48, 14, 'gold')}
{box(400, 200, 66, 48, 14, 'gold')}
<g fill="none" class="a" stroke-width="5">
  <path d="M170 130h70" marker-end="url(#ar)"/><path d="M360 130h70" marker-end="url(#ar)"/></g>''', arrow=True)

add('interrogation', '灯りの下で、こまかく問いただされる', f'''
<g transform="translate(300 70)"><path d="M-46 40h92l-26-40h-40z" class="teald o"/>
  <path d="M0 0v-30" fill="none" stroke="{INK}" stroke-width="4"/>
  <g opacity="0.35"><path d="M-46 40L-120 260h240L46 40z" fill="#ffe9a8"/></g></g>
{table(250)}
{sit(230, 380, 1.2, 1, 'coral', 'blue', 'short', 'sad', 'lap')}
{chair(244, 380, 1.1, 'gold', -1)}
{person(450, 380, 1.25, -1, 'violet', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(360 190)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''')

add('interviewee', '質問される側にすわっている人', f'''
{table(260)}
{person(180, 380, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(440, 380, 1.25, -1, 'violet', 'blue', 'point', 'bun', 'neutral')}
<g transform="translate(310 180)"><rect x="-70" y="-44" width="140" height="88" rx="18" class="paper"/>
  <path d="M50 40l26 30-44-30z" class="paper"/>
  <path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="34" r="5" fill="{MUTED}"/></g>
{ring(180, 280, 122)}''')

add('insistence', '同じ点をくり返し、ゆずらずに言い張る', f'''
{person(160, 306, 1.25, 1, 'coral', 'blue', 'point', 'short', 'neutral')}
{''.join(f'<g transform="translate({350} {130+i*80})"><rect x="-110" y="-32" width="220" height="64" rx="16" class="paper"/>'
         f'<path d="M-90 30l-22 26 4-26z" class="paper"/>{word(0, 0, 3, 30, CRL)}</g>' for i in range(3))}
{''.join(f'<path d="M240 {160+i*80}h20" fill="none" stroke="{MUTED}" stroke-width="0"/>' for i in range(0))}
{head(540, 330, 24, 'teal', 'bob')}''')

# --- 権利・お金 ---------------------------------------------------------------

add('infringement', 'よその区画の線を越えて、勝手に入りこむ', f'''
<path d="M300 60v300" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="14 12"/>
{house(150, 306, 0.6, 'teal')}
{house(460, 306, 0.6, 'coral')}
<g transform="translate(360 250)"><rect x="-80" y="-40" width="160" height="80" rx="8" class="teal o"/></g>
<path d="M240 160h120" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
{head(520, 200, 24, 'coral', 'bob')}
<path d="M544 164q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>''', arrow=True)

add('inheritance', '遺言とともに、家や品が受けつがれる', f'''
{table(320)}
{doc(160, 200, 170, 210, 4)}
<circle cx="200" cy="270" r="26" fill="none" stroke="{CRL}" stroke-width="5"/>
<path d="M270 200h50" class="a" marker-end="url(#ar)"/>
{house(430, 290, 0.5, 'coral')}
{''.join(coin(390 + i*44, 320, 20) for i in range(2))}
<g transform="translate(520 250)"><path d="M-44 40q-14-70 0-80 44-14 88 0 14 10 0 80z" class="goldp o"/>
  <path d="M-48-40h96v-14h-96z" class="goldd o"/></g>''', arrow=True)

add('instalment', '総額を分けて、毎月おなじ額ずつ払う', f'''
<g transform="translate(150 130)">{box(0, 0, 180, 120, 34, 'violet')}</g>
<path d="M280 130h50" class="a" marker-end="url(#ar)"/>
{''.join(f'<g transform="translate({410+ (i%3)*70} {110+(i//3)*90})">{coin(0, 0, 28)}</g>' for i in range(6))}
<g transform="translate(300 320)"><rect x="-250" y="-40" width="500" height="80" rx="8" class="paper"/>
  {''.join(f'<rect x="{-226+i*80}" y="-22" width="60" height="44" rx="5" fill="{"#f7e2c8" if i < 6 else "#eef2f4"}" stroke="{INK}" stroke-width="2"/>' for i in range(6))}</g>''', arrow=True)

add('invest in', 'お金を注ぎこんで、育つのを待つ', f'''
{table(340)}
<g transform="translate(180 306)"><path d="M-56 0l8-70h96l8 70z" class="corald o"/>
  <path d="M-60-70h120v-16h-120z" class="coral o"/>
  <path d="M0-86v-40" fill="none" stroke="{GRND}" stroke-width="6"/>
  <path d="M0-110q-26-4-30-30 24 2 30 22z" class="greenp o"/></g>
{''.join(coin(150 + i*30, 150 - i*20, 20) for i in range(3))}
<path d="M240 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 306)"><path d="M-56 0l8-70h96l8 70z" class="corald o"/>
  <path d="M-60-70h120v-16h-120z" class="coral o"/>
  <path d="M0-86v-150" fill="none" stroke="{GRND}" stroke-width="8"/>
  <path d="M0-180q-46-8-54-52 44 4 54 38zM0-210q46-10 54-54-44 6-54 40z" class="greenp o"/></g>''', arrow=True)

add('interest', '預けたお金に、時とともに利息がつく', f'''
<g transform="translate(150 250)">{''.join(coin(0, -i*26, 34) for i in range(3))}</g>
<path d="M240 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(430 250)">{''.join(coin(0, -i*26, 34) for i in range(6))}</g>
<path d="M300 340h180" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9" marker-end="url(#ar)"/>
{''.join(spark(x, y, 0.8) for x, y in [(380,80),(520,110)])}''', arrow=True)

# --- 気持ち・かかわり ---------------------------------------------------------

add('indignation', '不公平なあつかいに、腹の底から怒る', f'''
{scalebar(430, 250, 16, 0.9)}
{box(310, 190, 70, 50, 16, 'teal')}
{box(560, 290, 70, 50, 16, 'coral')}
{person(140, 306, 1.3, 1, 'coral', 'blue', 'point', 'short', 'neutral')}
<path d="M112 190l16 6M168 190l-16 6" fill="none" stroke="{INK}" stroke-width="4"/>
<g class="corals" stroke-width="6">{''.join(f'<path d="M140 130v-26" transform="rotate({d} 140 178)"/>' for d in [-30, 0, 30])}</g>''')

add('intimidation', '大きな影で見下ろし、言うことを聞かせる', f'''
<g transform="translate(430 306)" opacity="0.9">
  <path d="M-14-8l-8 34M14-8l8 34" fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-40-110q40-18 80 0l-12 102h-56z" fill="{INK}"/>
  <path d="M-36-100l-44 46M36-100l44 46" fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round"/>
  <circle cx="0" cy="-146" r="34" fill="{INK}"/></g>
{person(180, 306, 0.95, 1, 'teal', 'blue', 'hold', 'short', 'sad')}
<path d="M330 220h-70" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
{drop(150, 200, 0.9)}''', arrow=True)

add('intimacy', 'ふたりだけの静かな時間を、近くで分け合う', f'''
{table(300)}
{sit(240, 380, 1.15, 1, 'teal', 'blue', 'bob', 'smile', 'lap')}
{sit(370, 380, 1.15, -1, 'coral', 'blue', 'short', 'smile', 'lap')}
{''.join(f'<g transform="translate({x} 268)"><path d="M-24 0v-44h48V0z" fill="#fffefd" class="o"/>'
         f'<path d="M24-34q22 0 22 12t-22 12" fill="none" class="o"/></g>' for x in [270, 340])}
<g transform="translate(305 130)"><path d="M0 26q-40-30-40-56 0-20 20-20 12 0 20 12 8-12 20-12 20 0 20 20 0 26-40 56z" class="coralp o"/></g>
{''.join(f'<path d="M{250+i*22} {200-i*14}q-14-20 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('intrigue', '半分だけ開いた箱に、つい引きこまれる', f'''
{table(330)}
<g transform="translate(400 280)"><path d="M-80 26v-70h160v70z" class="violet o"/>
  <path d="M-80-44l-16-30h192l-16 30z" class="violetd o" transform="rotate(-24 -80 -44)"/>
  {''.join(spark(-20 + i*30, -70, 0.7) for i in range(3))}</g>
{person(150, 306, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'surprised')}
<path d="M220 210h100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(250 110)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''')

add('interplay', '二つがたがいに影響し合って、動きをつくる', f'''
<circle cx="180" cy="200" r="80" class="teal o"/>
<circle cx="420" cy="200" r="80" class="coral o"/>
<g fill="none" class="a" stroke-width="6">
  <path d="M240 150q60-40 120 0" marker-end="url(#ar)"/>
  <path d="M360 250q-60 40-120 0" marker-end="url(#ar)"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(300,90),(300,320)])}''', arrow=True)

add('intuition', '手順をふまずに、答えがすっと浮かぶ', f'''
{head(150, 220, 40, 'teal', 'short')}
<g opacity="0.4" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9">
  {''.join(f'<rect x="240" y="{100+i*70}" width="130" height="50" rx="8"/>' for i in range(3))}</g>
<path d="M200 200q120-70 250 0" fill="none" stroke="{VIO}" stroke-width="7" marker-end="url(#ar)"/>
<g transform="translate(480 210)"><circle r="52" class="goldp o"/>
  <path d="M-22 4l16 18 32-38" fill="none" stroke="{GRN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></g>''', arrow=True)

add('initiation', '輪に迎え入れられ、しるしを受け取る', f'''
{''.join(f'<g transform="translate({230+130*math.cos(math.radians(a)):.0f} {210+100*math.sin(math.radians(a)):.0f})">{head(0, 0, 26, c, h)}</g>'
         for a, (c, h) in zip([180, 240, 300, 0, 60, 120], [('teal','short'),('coral','bob'),('gold','bun'),('green','short'),('blue','cap'),('violet','bob')]))}
<circle cx="230" cy="210" r="160" fill="none" stroke="{TEA}" stroke-width="5" stroke-dasharray="0"/>
{person(500, 306, 1.15, -1, 'coral', 'green', 'reach', 'short', 'smile')}
<path d="M470 210h-60" class="a" marker-end="url(#ar)"/>
<g transform="translate(500 200)"><path d="M0-18l16 10v18L0 30l-16-8v-18z" class="gold o"/></g>''', arrow=True)

add('insurgency', '旗を立てて、支配する側に立ち向かう', f'''
<g transform="translate(470 306)"><path d="M-110 0v-190h220V0z" fill="#c3cbd1" class="o"/>
  <path d="M-124-190h248l-30-40h-188z" fill="#9aa6ae" class="o"/>
  {''.join(f'<rect x="{-86+i*60}" y="-150" width="40" height="40" fill="#8b9196"/>' for i in range(3))}</g>
{''.join(f'<g transform="translate({70+i*80} 340)">{person(0, 0, 1.0, 1, c, "blue", "up", h, "neutral")}</g>'
         for i, (c, h) in enumerate([('coral','short'),('violet','bob'),('gold','cap')]))}
{''.join(f'<g transform="translate({110+i*80} 340)"><path d="M0 0v-160" fill="none" stroke="{GLDD}" stroke-width="7"/>'
         f'<path d="M0-160h70l-16 24 16 24H0z" class="coral o"/></g>' for i in range(2))}
<path d="M300 180h60" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('induction', '入ったばかりの人に、初日の手ほどきをする', f'''
{table(300)}
{person(200, 380, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
<g transform="translate(220 250)"><rect x="-34" y="-16" width="68" height="32" rx="6" class="coralp o"/></g>
{doc(330, 240, 130, 160, 4)}
{person(470, 380, 1.2, -1, 'violet', 'blue', 'point', 'bun', 'smile')}
<path d="M410 200h-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
{''.join(spark(x, y, 0.7) for x, y in [(130,150),(550,160)])}''')

# --- 性質・形 ----------------------------------------------------------------

add('inherent in', '塗ったのではなく、材そのものに通っている木目', f'''
{split()}
<g transform="translate(150 200)"><rect x="-100" y="-120" width="200" height="240" rx="8" fill="#c9a06c" class="o"/>
  <rect x="-100" y="-120" width="200" height="40" fill="{TEA}"/>
  <path d="M-100-80h200" fill="none" stroke="{INK}" stroke-width="3"/></g>
{ring(150, 200, 132, True)}
<g transform="translate(450 200)"><rect x="-100" y="-120" width="200" height="240" rx="8" fill="#c9a06c" class="o"/>
  {''.join(f'<path d="M-100 {-96+i*34}q50 20 100 0t100 0" fill="none" stroke="#a8804f" stroke-width="5"/>' for i in range(7))}</g>
{ring(450, 200, 132)}''')

add('inversion', '上下がそっくり入れかわる', f'''
{split()}
<g transform="translate(150 210)"><path d="M-70 60l70-120 70 120z" class="teal o"/>
  <circle cx="0" cy="-90" r="20" class="gold o"/></g>
{ring(150, 200, 132, True)}
<g transform="translate(450 210) scale(1 -1)"><path d="M-70 60l70-120 70 120z" class="teal o"/>
  <circle cx="0" cy="-90" r="20" class="gold o"/></g>
<path d="M300 350h1" fill="none"/>
<path d="M380 350a70 70 0 0 1 140 0" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>
{ring(450, 200, 132)}''', arrow=True)

add('irregularity', 'そろって並ぶなかに、一つだけ間かくがずれる', f'''
{''.join(f'<rect x="{70+i*70}" y="150" width="44" height="110" rx="6" class="tealp o"/>' for i in range(4))}
<rect x="392" y="150" width="44" height="110" rx="6" class="coral o"/>
{''.join(f'<rect x="{480+i*70}" y="150" width="44" height="110" rx="6" class="tealp o"/>' for i in range(1))}
{''.join(f'<path d="M{114+i*70} 300h26" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>' for i in range(3))}
<path d="M324 300h68" class="a" stroke="{CRL}" marker-end="url(#ar)" marker-start="url(#ar)"/>
{ring(414, 205, 78)}''', arrow=True)

add('iteration', '試すたびに手を入れて、少しずつ良くしていく', f'''
{''.join(f'<g transform="translate({110+i*130} 200)"><rect x="-56" y="-70" width="112" height="140" rx="8" class="paper"/>' + s + '</g>'
         for i, s in enumerate([
  f'<path d="M-30 40q30-70 60 0z" fill="none" stroke="{MUTED}" stroke-width="4"/>',
  f'<path d="M-34 40q34-80 68 0z" class="tealp o"/>',
  f'<path d="M-34 40q34-80 68 0z" class="teal o"/><circle cx="16" cy="-30" r="12" class="goldp o"/>',
  f'<path d="M-34 40q34-80 68 0z" class="teal o"/><circle cx="16" cy="-30" r="12" class="gold o"/>'
  f'<path d="M-40 40h80" fill="none" stroke="{GRND}" stroke-width="5"/>']))}
{''.join(f'<path d="M{180+i*130} 200h40" class="a" marker-end="url(#ar)"/>' for i in range(3))}''', arrow=True)

add('inscription', '石に彫りこまれた、消えない文字', f'''
<g transform="translate(280 220)"><rect x="-170" y="-130" width="340" height="260" rx="8" fill="#c3ccd2" class="o"/>
  {''.join(f'<g transform="translate({-120+ (i%4)*80} {-70+(i//4)*70})">'
           f'<path d="M-24 0h48M0-20v40" fill="none" stroke="#8b9196" stroke-width="10" stroke-linecap="round"/>'
           f'<path d="M-24 0h48M0-20v40" fill="none" stroke="#e8eef1" stroke-width="4" stroke-linecap="round" transform="translate(-2 -2)"/></g>' for i in range(8))}</g>
<g transform="translate(470 130) rotate(40)"><path d="M-12 0h24v90h-24z" class="goldd o"/>
  <path d="M-12 90h24l-12 24z" fill="#8d949a" class="o"/></g>''')

# --- 慣用表現 ----------------------------------------------------------------

add('in search of', '灯りを手に、さがしものを求めて進む', f'''
<rect width="600" height="400" fill="#2a3340"/>
<g opacity="0.5"><path d="M330 130L200 400h260z" fill="#ffe9a8"/></g>
<g transform="translate(330 120)"><path d="M-26 0h52v40h-52z" class="goldp o"/>
  <path d="M-16-14h32v14h-32z" class="goldd o"/>
  <path d="M0-14v-26" fill="none" stroke="#dfe6ea" stroke-width="4"/></g>
{person(250, 340, 1.15, 1, 'teal', 'blue', 'reach', 'cap', 'neutral', 'walk')}
<g fill="none" stroke="#8d949a" stroke-width="4" stroke-dasharray="11 9">
  <rect x="440" y="290" width="90" height="70" rx="8"/></g>''')

add('in so far as', 'この範囲のなかでだけ、その言い分は通る', f'''
<path d="M60 340h480M90 360V80" fill="none" stroke="{MUTED}" stroke-width="4"/>
<rect x="90" y="100" width="220" height="240" fill="{TONES['teal'][1]}"/>
<path d="M310 80v280" fill="none" stroke="{CRL}" stroke-width="6" stroke-dasharray="12 10"/>
<path d="M110 300l180-160" fill="none" stroke="{TEA}" stroke-width="7"/>
<path d="M310 140q60 100 210 60" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/>
<g transform="translate(200 130)"><path d="M-30 0l24 26 48-56" fill="none" stroke="{GRN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></g>''')

add('in the absence of', 'いつもの人がいないので、代わりの人が入る', f'''
<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="12 10">
  <circle cx="180" cy="200" r="28"/>
  <path d="M152 244q28-14 56 0l-8 72h-40z"/>
  <path d="M152 248l-24 46M208 248l24 46"/>
  <path d="M164 316l-8 34M196 316l8 34"/></g>
<path d="M280 250h60" class="a" marker-end="url(#ar)"/>
{person(450, 350, 1.15, 1, 'coral', 'blue', 'stand', 'bob', 'neutral')}
{ring(450, 250, 122)}''', arrow=True)

add('in the event of', '火が出たときは、このガラスを割って使う', f'''
<g transform="translate(300 210)"><rect x="-130" y="-140" width="260" height="280" rx="10" class="coral o"/>
  <rect x="-104" y="-114" width="208" height="228" rx="6" fill="#eaf4fb" class="o"/>
  <g transform="translate(0 20) scale(0.6)">{flame(0, 0, 1)}</g>
  <path d="M-104-114l208 228M104-114L-104 114" fill="none" stroke="#b6cdd8" stroke-width="4"/></g>
<g transform="translate(470 320) rotate(-30)"><path d="M-10 0h20v80h-20z" class="goldd o"/>
  <path d="M-34-30h68v34h-68z" fill="#5b6b78" class="o"/></g>
<g transform="translate(120 120) scale(0.5)">{flame(0, 0, 1)}</g>
<path d="M170 150h60" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('in the light of', 'あかりを当てて分かったことから、判断を決める', f'''
<g transform="translate(180 130)"><path d="M-40 0h80v50h-80z" class="goldp o"/>
  <path d="M-24-16h48v16h-48z" class="goldd o"/>
  <g opacity="0.4"><path d="M-40 50L-110 260h220L40 50z" fill="#ffe9a8"/></g></g>
<g transform="translate(180 300)"><rect x="-90" y="-40" width="180" height="80" rx="6" class="paper"/>
  <path d="M-60 10q40-30 70 0t40-10" fill="none" stroke="{CRL}" stroke-width="5"/></g>
<path d="M300 260h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 260)"><rect x="-90" y="-70" width="180" height="140" rx="8" class="paper"/>
  <path d="M-40 10l26 28 52-60" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>''', arrow=True)

add('in the wake of', '通ったあとに、波紋が広がっていく', f'''
<path d="M0 200h600v200H0z" fill="{BLUP}"/>
<g transform="translate(430 250) rotate(-8)"><path d="M-100 0h200l-30 40h-140z" class="coral o"/>
  <path d="M-40 0v-56h80v56z" fill="#fffefd" class="o"/></g>
{''.join(f'<path d="M{300-i*70} {300+i*10}q-60-40-120 0" fill="none" stroke="{BLU}" stroke-width="{7-i}" opacity="{1-i*0.2:.1f}"/>' for i in range(4))}
{''.join(f'<path d="M{320-i*70} {250+i*8}q-50-30-100 0" fill="none" stroke="{BLU}" stroke-width="{6-i}" opacity="{0.9-i*0.2:.1f}"/>' for i in range(4))}
<path d="M300 130h-200" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('in turn', 'ひとりずつ、順に番が回ってくる', f'''
{''.join(f'<g transform="translate({100+i*110} 300)">{head(0, 0, 30, c, h)}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun'),('green','short'),('violet','cap')]))}
{''.join(f'<path d="M{100+i*110} 190v50" class="a" marker-end="url(#ar)"/>' for i in range(1))}
{box(100, 150, 66, 46, 14, 'gold')}
{''.join(f'<path d="M{146+i*110} 150h64" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>' for i in range(4))}''', arrow=True)

add('intoxication', '検査の数値が高く出る、酔いの状態', f'''
{person(180, 306, 1.2, 1, 'coral', 'blue', 'reach', 'short', 'neutral', 'walk')}
<g transform="translate(180 130)"><path d="M0 0a26 26 0 1 1 22-14 18 18 0 1 0 14 24" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/></g>
<g transform="translate(430 240)"><rect x="-80" y="-100" width="160" height="200" rx="14" class="teald o"/>
  <rect x="-62" y="-80" width="124" height="70" rx="6" fill="#dfe6ea"/>
  {''.join(f'<rect x="{-46+i*32}" y="-56" width="20" height="30" rx="4" class="coral"/>' for i in range(3))}
  <path d="M-40 30h80M-40 60h50" fill="none" stroke="{TEAP}" stroke-width="8"/>
  <path d="M62-100v-30h-24" fill="none" stroke="{INK}" stroke-width="6"/></g>''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
