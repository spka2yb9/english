# -*- coding: utf-8 -*-
"""第160回。h-/i- の名詞と、in- で始まる慣用表現。"""
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

def germ(x, y, s=1, cls='violet'):
    spikes = ''.join(f'<path d="M0 -22v-12" transform="rotate({d})"/>' for d in range(0, 360, 45))
    return (f'<g transform="translate({x} {y}) scale({s})"><g class="{cls}s" stroke-width="4">{spikes}</g>'
            f'<circle r="22" class="{cls} o"/><circle cx="-7" cy="-5" r="4" fill="#fffefd"/></g>')

def bulb(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="30" class="goldp o"/>'
            f'<path d="M-12 30h24v10h-24z" class="goldd o"/>'
            f'<g class="golds"><path d="M0-46v-18"/><path d="M34-34l14-14"/><path d="M-34-34l-14-14"/>'
            f'<path d="M46 0h18"/><path d="M-46 0h-18"/></g></g>')

def hourglass(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-60-90h120v14h-120zM-60 76h120v14h-120z" class="goldd o"/>'
            f'<path d="M-50-76h100l-50 76 50 76h-100l50-76z" fill="#fffefd" class="o"/>'
            f'<path d="M-36-70h72l-36 56z" class="goldp"/>'
            f'<path d="M-30 70h60l-30-44z" class="goldp"/>'
            f'<path d="M0-10v40" fill="none" stroke="{GLD}" stroke-width="4"/></g>')

def scalebar(x, y, tilt=0, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-70" fill="none" stroke="{INK}" stroke-width="7"/><circle cy="-76" r="9" class="ink"/>'
            f'<path d="M-180 0h360" fill="none" stroke="{INK}" stroke-width="7" transform="translate(0 -76) rotate({tilt})"/>'
            f'<path d="M-40 0h80v14h-80z" class="ink"/></g>')

# --- 力・そなえ ---------------------------------------------------------------

add('harness', '風の力をつかまえて、明かりに変える', f'''
{''.join(f'<path d="M40 {110+i*40}h90" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(4))}
<g transform="translate(230 220)"><path d="M-10 130V-10h20V130z" class="teald o"/>
  {''.join(f'<path d="M0-10l{100*math.cos(math.radians(a)):.0f} {100*math.sin(math.radians(a)):.0f}" fill="none" stroke="{TEA}" stroke-width="18" stroke-linecap="round"/>' for a in [270, 30, 150])}
  <circle cy="-10" r="14" class="teald o"/></g>
<path d="M250 320h130" fill="none" stroke="{INK}" stroke-width="5"/>
{bulb(430, 250, 1.3)}
{''.join(spark(x, y, 0.8) for x, y in [(520,160),(530,320)])}''')

add('haven', '嵐の海のなか、静かに休める入り江', f'''
<path d="M0 190h600v210H0z" fill="{BLU}"/>
{''.join(f'<path d="M{-20+i*90} 210q45-50 90 0" fill="none" stroke="#fffefd" stroke-width="6" opacity="0.6"/>' for i in range(8))}
{cloud(120, 80, 1.5, 'violet')}{cloud(400, 70, 1.6, 'violet')}
<path d="M300 400q-40-140 60-180 120-46 240 40v140z" class="greenp o"/>
<path d="M330 330q40-70 130-70t140 60v80H330z" fill="{BLUP}"/>
<g transform="translate(430 320)"><path d="M-70 0h140l-24 34h-92z" class="coral o"/>
  <path d="M0 0v-60" fill="none" stroke="{GLDD}" stroke-width="6"/>
  <path d="M0-60l40 24-40 16z" fill="#fffefd" class="o"/></g>
<g transform="translate(540 250)"><path d="M-40 0v-46h80V0z" fill="#fffefd" class="o"/>
  <path d="M-48-46L0-80l48 34z" class="corald o"/></g>''')

add('harshness', '木も陰もない、冷たく荒れた土地', f'''
<path d="M0 300h600v100H0z" fill="#b3b6ab"/>
<path d="M0 300q120-90 240-60t360-60v120z" fill="#9aa0a4" class="o"/>
{''.join(f'<path d="M{60+i*90} 340l{20+i*4} 60" fill="none" stroke="#8b9196" stroke-width="5"/>' for i in range(6))}
{cloud(180, 90, 1.6, 'violet')}{cloud(430, 80, 1.5, 'violet')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M80 180h130M60 230h110M100 280h120"/></g>
{person(400, 340, 1.05, 1, 'blue', 'blue', 'hold', 'cap', 'sad')}
{''.join(f'<path d="M{300+i*70} {170+ (i%2)*30}l6 14 14 6-14 6-6 14-6-14-14-6 14-6z" fill="#ffffff"/>' for i in range(3))}''')

add('hibernation', '雪のなか、あなぐらで冬を眠って越す', f'''
<path d="M0 0h600v400H0z" fill="#dfe6ea"/>
<path d="M0 240q140-40 300-20t300-30v210H0z" fill="#fffefd" class="o"/>
<g transform="translate(320 340)"><path d="M-160 0q0-120 160-120t160 120z" fill="#6f6357" class="o"/>
  <path d="M-110 0q0-80 110-80t110 80z" fill="#3d372f"/></g>
<g transform="translate(320 320)"><ellipse rx="100" ry="46" fill="#8a6a48" class="o"/>
  <circle cx="-76" cy="-24" r="34" fill="#8a6a48" class="o"/>
  <circle cx="-100" cy="-50" r="14" fill="#8a6a48" class="o"/><circle cx="-56" cy="-56" r="14" fill="#8a6a48" class="o"/>
  <path d="M-90-22h20M-70-16h16" fill="none" stroke="{INK}" stroke-width="3"/></g>
{''.join(f'<path d="M{380+i*30} {230-i*26}q16 16 0 32" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}
{''.join(f'<path d="M{70+i*100} {90+(i%2)*40}l5 12 12 5-12 5-5 12-5-12-12-5 12-5z" fill="#ffffff" stroke="{MUTED}" stroke-width="1.5"/>' for i in range(5))}''')

# --- じゃま・こえる -----------------------------------------------------------

add('hindrance', '出口をふさぐ荷物のせいで、先へ進めない', f'''
<g transform="translate(430 306)"><path d="M-100 0v-210h200V0z" fill="#fffefd" class="o"/>
  <path d="M-80 0v-190h160V0z" class="goldp o"/></g>
{box(400, 306, 130, 94, 28, 'coral')}
{person(160, 306, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'sad')}
<path d="M230 250h80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<path d="M320 250l-14-12M320 250l-14 12" fill="none" stroke="{CRL}" stroke-width="5"/>''')

add('hurdle', 'ひとつずつ跳び越えていく障害', f'''
<path d="M0 340h600v60H0z" class="ground"/>
{''.join(f'<g transform="translate({160+i*170} 340)"><path d="M-50 0v-90h100v90" fill="none" stroke="{GLDD}" stroke-width="10"/>'
         f'<path d="M-60-90h120" fill="none" stroke="{CRL}" stroke-width="10"/></g>' for i in range(3))}
<g transform="translate(240 220) rotate(-12)">{person(0, 0, 1.05, 1, 'coral', 'blue', 'up', 'cap', 'neutral', 'walk')}</g>
<path d="M110 250q120-100 250 60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>''')

add('have no choice but to', 'ほかの案が消えて、残った一つを取るしかない', f'''
{''.join(f'<g transform="translate({130+i*130} 220)"><rect x="-56" y="-76" width="112" height="152" rx="8" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/></g>' for i in range(2))}
<g transform="translate(390 220)"><rect x="-56" y="-76" width="112" height="152" rx="8" class="coral o"/></g>
{ring(390, 220, 92)}
{person(530, 306, 1.1, -1, 'teal', 'blue', 'reach', 'short', 'sad')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"><path d="M120 340h340"/></g>''')

add('hit the nail on the head', '打ちおろした先が、くぎの頭にぴたりと当たる', f'''
{table(340)}
<g transform="translate(300 306)"><path d="M-8-60h16v60h-16z" class="ink"/>
  <path d="M-26-60h52v12h-52z" class="ink"/></g>
<g transform="translate(300 180) rotate(-8)"><path d="M-12 0h24v100h-24z" class="goldd o"/>
  <path d="M-56-40h112v42h-112z" fill="#5b6b78" class="o"/></g>
<g class="golds" stroke-width="6">{''.join(f'<path d="M300 220v-24" transform="rotate({d} 300 258)"/>' for d in [-40, 0, 40])}</g>
{head(500, 250, 26, 'teal', 'short')}
<g transform="translate(120 140)"><rect x="-60" y="-36" width="120" height="72" rx="16" class="paper"/>
  <path d="M-24 6l16 18 32-38" fill="none" stroke="{GRN}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>''')

add('impairment', 'はたらきが、いつもの線より落ちる', f'''
<path d="M60 340h480M90 360V80" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M90 150h450" fill="none" stroke="{GRN}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M110 150l90 4 80 6 90 90 90 40" fill="none" stroke="{CRL}" stroke-width="7"/>
{''.join(f'<circle cx="{110+i*90}" cy="{y}" r="9" class="coral o"/>' for i, y in enumerate([150, 154, 160, 250, 290]))}
<path d="M460 170v100" class="a" stroke="{CRL}" marker-end="url(#ar)"/>
<g transform="translate(510 100)"><path d="M0-30l30 52h-60z" class="gold o"/>
  <path d="M0-10v10" fill="none" stroke="{INK}" stroke-width="4"/><circle cy="12" r="3" class="ink"/></g>''', arrow=True)

# --- からだ・衛生 -------------------------------------------------------------

add('immune to', '盾がはたらいて、菌がはねかえされる', f'''
{person(180, 306, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(300 210)"><path d="M0-110q60 24 84 34 0 90-84 128-84-38-84-128 24-10 84-34z" class="tealp o"/></g>
{''.join(germ(430 + (i%2)*70, 140 + (i//2)*90, 0.9) for i in range(4))}
{''.join(f'<path d="M{410+ (i%2)*70} {150+(i//2)*90}l-40 {20-(i//2)*20}" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="8 7"/>' for i in range(4))}''')

add('immunity', '体の守り手が、入りこんだ菌を取り囲む', f'''
<g transform="translate(300 200)"><circle r="150" fill="{TONES['coral'][1]}" class="o"/>
  {germ(0, 0, 1.1)}
  {''.join(f'<circle cx="{90*math.cos(math.radians(a)):.0f}" cy="{90*math.sin(math.radians(a)):.0f}" r="26" class="tealp o"/>' for a in range(0, 360, 60))}
  {''.join(f'<path d="M{62*math.cos(math.radians(a)):.0f} {62*math.sin(math.radians(a)):.0f}L{40*math.cos(math.radians(a)):.0f} {40*math.sin(math.radians(a)):.0f}" class="a" marker-end="url(#ar)"/>' for a in range(0, 360, 60))}</g>''', arrow=True)

add('hygiene', 'せっけんで手を洗い、清潔をたもつ', f'''
<g transform="translate(200 140)"><path d="M-90-40h40v50h-40z" class="teald o"/>
  <path d="M-50-30h100v22h-30v40h-24v-40h-46z" class="teal o"/></g>
<path d="M224 162v50" fill="none" stroke="{BLU}" stroke-width="10" stroke-linecap="round"/>
{hand(230, 250, 1)}
{hand(310, 260, -1)}
{''.join(f'<circle cx="{200+ (i%4)*40}" cy="{200+(i//4)*40}" r="{10+(i%3)*4}" fill="none" stroke="#ffffff" stroke-width="4"/>' for i in range(8))}
<g transform="translate(460 300)"><rect x="-50" y="-40" width="100" height="80" rx="14" fill="#fffefd" class="o"/>
  <path d="M-30-16q30-20 60 0" fill="none" stroke="{TEAP}" stroke-width="6"/></g>
{''.join(spark(x, y, 0.7) for x, y in [(400,180),(520,200)])}''')

add('hoof', '馬の足の先の、かたいひづめ', f'''
<g transform="translate(300 200)">
  <path d="M-50-160q50-20 100 0l-16 100q-34 14-68 0z" fill="#a8763f" class="o"/>
  <path d="M-34-60q34 14 68 0l16 110q-50 20-100 0z" fill="#a8763f" class="o"/>
  <path d="M-50 50q50 18 100 0l10 50h-120z" fill="#8a6032" class="o"/>
  <path d="M-64 100h128q10 40-64 44-74-4-64-44z" fill="#4a3a2a" class="o"/>
  <path d="M-40 120h80" fill="none" stroke="#2f2620" stroke-width="4"/></g>
{ring(300, 320, 96)}''')

# --- 情報・うそ ---------------------------------------------------------------

add('hoax', 'つくりものを本物のように見せかけた、いたずら', f'''
<g transform="translate(180 190)"><rect x="-110" y="-80" width="220" height="160" rx="8" fill="#f3ead6" class="o"/>
  <rect x="-94" y="-64" width="188" height="112" fill="#c3ccd2"/>
  <path d="M-50 44q-16-40 10-56 30-18 56 4t10 52z" fill="#6f787d"/>
  <circle cx="-16" cy="-4" r="6" fill="#fffefd"/><circle cx="18" cy="-6" r="6" fill="#fffefd"/></g>
<path d="M310 190h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 260)"><path d="M-50 44q-16-40 10-56 30-18 56 4t10 52z" fill="#6f787d" class="o"/>
  <circle cx="-16" cy="-4" r="6" fill="#fffefd" class="o"/><circle cx="18" cy="-6" r="6" fill="#fffefd" class="o"/>
  <path d="M0-56v-90" fill="none" stroke="{MUTED}" stroke-width="3"/></g>
{hand(470, 90, 1)}''', arrow=True)

add('impersonation', 'その人そっくりの面をかぶって、なりすます', f'''
{head(150, 200, 46, 'teal', 'bob')}
<path d="M220 200h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{person(430, 306, 1.3, 1, 'violet', 'blue', 'hold', 'short', 'neutral')}
<g transform="translate(430 168)"><ellipse rx="48" ry="56" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="{HAIRS['bob']}" transform="translate(0 214) scale(1.9)" fill="{HAIR}"/>
  <circle cx="-16" cy="-4" r="5" class="ink"/><circle cx="16" cy="-4" r="5" class="ink"/>
  <path d="M-14 24q14 12 28 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-48 0h-24M48 0h24" fill="none" stroke="{MUTED}" stroke-width="4"/></g>''')

add('imitation', '本物をまねて、そっくりに作ったもの', f'''
{split()}
<g transform="translate(150 290)"><path d="M-56 0q-20-70 0-90 56-20 112 0 20 20 0 90z" class="corald o"/>
  <path d="M-60-90h120v-16h-120z" class="coral o"/>
  <path d="M-40-60q40 16 80 0" fill="none" stroke="{GLD}" stroke-width="5"/></g>
{ring(150, 240, 122, True)}
<g transform="translate(450 290)"><path d="M-56 0q-20-70 0-90 56-20 112 0 20 20 0 90z" fill="#c9b7ad" class="o"/>
  <path d="M-60-90h120v-16h-120z" fill="#b3a196" class="o"/>
  <path d="M-40-60q40 16 80 0" fill="none" stroke="#a09084" stroke-width="5"/></g>
{ring(450, 240, 122)}''')

add('illumination', '暗い部屋に明かりがつき、すみずみまで見える', f'''
{split()}
<g transform="translate(150 200)"><rect x="-110" y="-140" width="220" height="280" rx="10" fill="#2a3340"/>
  <g opacity="0.4">{chair(150, 300, 0.7, 'gold', -1)}</g></g>
{ring(150, 200, 138, True)}
<g transform="translate(450 200)"><rect x="-110" y="-140" width="220" height="280" rx="10" fill="#fff6d8" class="o"/></g>
<g transform="translate(450 110)"><path d="M-56 0h112l-30-40h-52z" class="teald o"/>
  <path d="M0-40v-30" fill="none" stroke="{INK}" stroke-width="4"/>
  <g opacity="0.5"><path d="M-56 0L-96 170h192L56 0z" fill="#ffe9a8"/></g></g>
{chair(450, 300, 0.7, 'gold', -1)}
{ring(450, 200, 138)}''')

# --- 心のうごき ---------------------------------------------------------------

add('humiliation', 'みんなの前で恥をかかされ、うつむく', f'''
<g transform="translate(230 306)">
  <path d="M-12-8l-6 30M10-8l6 30" fill="none" stroke="{BLUD}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-72q26-13 52 0l-8 66h-36z" fill="{CRL}" class="o"/>
  <path d="M-22-66l6 44M22-66l-6 44" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="0" cy="-100" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 4)" fill="{HAIR}"/>
  <path d="M-11-94l10 4M11-94l-10 4" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-7-78h14" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="-26" cy="-86" r="8" class="coralp"/><circle cx="26" cy="-86" r="8" class="coralp"/></g>
{''.join(f'<g transform="translate({420+ (i%2)*90} {250+(i//2)*80})">{head(0, 0, 26, c, h)}'
         f'<path d="M-13 12q13 12 26 0" fill="none" stroke="{INK}" stroke-width="3"/></g>'
         for i, (c, h) in enumerate([('teal','short'),('violet','bob'),('gold','bun'),('green','cap')]))}
{''.join(f'<path d="M{380+ (i%2)*90} {200+(i//2)*80}q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('humility', '腕はたしかなのに、えらぶらず頭を低くする', f'''
{table(330)}
<g transform="translate(430 290)"><path d="M-60 0q-20-80 0-100 60-22 120 0 20 20 0 100z" class="corald o"/>
  <path d="M-64-100h128v-16h-128z" class="coral o"/>
  {''.join(f'<path d="M{-46+i*30} -88q10 46 0 84" fill="none" stroke="{GLD}" stroke-width="4"/>' for i in range(4))}</g>
{''.join(spark(x, y, 0.8) for x, y in [(350,140),(520,140)])}
<g transform="translate(180 306)">
  <path d="M-12-8l-6 30M10-8l6 30" fill="none" stroke="{BLUD}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-72q26-13 52 0l-8 66h-36z" fill="{TEA}" class="o"/>
  <path d="M-22-66l10 40M22-66l-10 40" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="0" cy="-100" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bun']}" transform="translate(0 4)" fill="{HAIR}"/>
  <path d="M-9-96l8 4M9-96l-8 4" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-7-80q7 6 14 0" fill="none" stroke="{INK}" stroke-width="2.5"/></g>''')

add('heroism', '危ないほうへ飛びこんで、人を助ける', f'''
<g transform="translate(430 300)"><path d="M-100 0v-140h200V0z" fill="#fffefd" class="o"/>
  <path d="M-112-140h224l-24-40h-176z" class="corald o"/></g>
<g transform="translate(430 250) scale(0.7)">{flame(0, 40, 1)}</g>
<g transform="translate(230 306) rotate(-10)">{person(0, 0, 1.2, 1, 'coral', 'blue', 'carry', 'cap', 'neutral', 'walk')}</g>
<g transform="translate(250 220)">{head(0, 0, 20, 'teal', 'bob')}</g>
<path d="M330 200h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{''.join(f'<path d="M{120+i*40} 180l-14-24" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('idleness', 'することが積んであるのに、寝ころんでいる', f'''
{table(340)}
{''.join(f'<g transform="translate({470+ (i%2)*6} {300-i*36}) rotate({-4+i*3})">'
         f'<rect x="-60" y="-16" width="120" height="32" rx="4" class="paper"/></g>' for i in range(5))}
<g transform="translate(220 330)">
  <path d="M-120 10q10-30 44-26l100 10q30 4 30 26h-174z" fill="{TEA}" class="o"/>
  <circle cx="-150" cy="-16" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(-150 92) scale(1.16)" fill="{HAIR}"/>
  <path d="M-164-22l14 6M-136-22l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-158-2h16" fill="none" stroke="{INK}" stroke-width="3"/></g>
{''.join(f'<path d="M{110+i*24} {250-i*22}q16 16 0 32" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('hunch', 'たしかな理由はないが、こっちだと感じる', f'''
{''.join(f'<g transform="translate({210+i*130} 260)">{box(0, 0, 100, 74, 22, "gold")}</g>' for i in range(3))}
{head(120, 150, 30, 'teal', 'short')}
<path d="M160 170q80 30 170 40" fill="none" stroke="{VIO}" stroke-width="6" stroke-dasharray="12 10" marker-end="url(#ar)"/>
{ring(340, 250, 84)}
<g transform="translate(120 70)"><path d="M-14-24a24 24 0 1 1 20 38q-6 8-6 16" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="42" r="5" fill="{MUTED}"/></g>''', arrow=True)

add('impulse', '考えるより先に、思わず手が出てしまう', f'''
{table(300)}
<g transform="translate(430 270)"><ellipse rx="80" ry="22" fill="#fffefd" class="o"/>
  <path d="M-56-10q0-56 56-56t56 56z" class="coralp o"/>
  <circle cx="0" cy="-70" r="11" class="coral o"/></g>
{person(170, 306, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'surprised')}
<path d="M240 210q60-30 110-10" fill="none" stroke="{CRL}" stroke-width="7" marker-end="url(#ar)"/>
<g class="corals" stroke-width="5">{''.join(f'<path d="M170 130v-24" transform="rotate({d} 170 178)"/>' for d in [-30, 0, 30])}</g>''', arrow=True)

add('impetus', 'ひと押しが、動き出すきっかけになる', f'''
<path d="M60 180q160 40 240 100t240 100" fill="none" stroke="{GLDD}" stroke-width="10"/>
<circle cx="180" cy="212" r="34" class="teal o"/>
<g opacity="0.35"><circle cx="330" cy="272" r="34" class="teal o"/><circle cx="470" cy="330" r="34" class="teal o"/></g>
{hand(90, 180, 1)}
<path d="M120 200h30" class="a" stroke-width="6" marker-end="url(#ar)"/>
<path d="M230 200q120 40 250 110" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9" marker-end="url(#ar)"/>''', arrow=True)

# --- 人・地位 ----------------------------------------------------------------

add('heir', '一族のあとを継ぎ、かぎを受けとる人', f'''
{head(180, 150, 30, 'violet', 'bun')}
<path d="M180 190v40M180 230h240M420 230v30" fill="none" stroke="{MUTED}" stroke-width="4"/>
{head(420, 290, 30, 'teal', 'short')}
<g transform="translate(300 130)"><rect x="-30" y="-14" width="44" height="28" rx="6" class="gold o"/>
  <path d="M14-6h50v12h-14v10h-10v-10h-26z" class="gold o"/></g>
<path d="M240 150h20" class="a" marker-end="url(#ar)"/>
<path d="M370 150h20" class="a" marker-end="url(#ar)"/>
<g transform="translate(520 250)"><path d="M-56 56v-70h112v70z" fill="#fffefd" class="o"/>
  <path d="M-66-14L0-60l66 46z" class="corald o"/></g>
{ring(420, 290, 62)}''', arrow=True)

add('impeachment', '議会が、その長を正式に訴え出る', f'''
<g transform="translate(300 306)"><path d="M-250 0v-40h500V0z" class="goldd o"/></g>
{''.join(f'<g transform="translate({90+i*90} 320)">{person(0, 0, 0.9, 1, c, "blue", "up", h, "neutral")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun')]))}
{person(500, 320, 1.0, -1, 'violet', 'blue', 'hold', 'short', 'sad')}
<g transform="translate(430 130) rotate(20)"><path d="M-10 0h20v60h-20z" class="goldd o"/>
  <path d="M-34-32h68v34h-68z" class="goldd o"/></g>
<path d="M300 180h100" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('hub', 'あちこちの線が、ここ一点に集まる', f'''
{''.join(f'<path d="M300 200L{300+220*math.cos(math.radians(a)):.0f} {200+150*math.sin(math.radians(a)):.0f}" fill="none" stroke="{MUTED}" stroke-width="5"/>' for a in range(0, 360, 45))}
{''.join(f'<circle cx="{300+220*math.cos(math.radians(a)):.0f}" cy="{200+150*math.sin(math.radians(a)):.0f}" r="20" class="tealp o"/>' for a in range(0, 360, 45))}
<circle cx="300" cy="200" r="52" class="coral o"/>
{ring(300, 200, 82)}''')

add('hive', 'はちが出入りする、六角の巣', f'''
<path d="M60 60h180" fill="none" stroke="{GRND}" stroke-width="10"/>
<g transform="translate(240 200)">
  {''.join(f'<ellipse cy="{-90+i*46}" rx="{60+i*16}" ry="30" class="goldp o"/>' for i in range(5))}
  <path d="M0-120v-30" fill="none" stroke="{GRND}" stroke-width="6"/>
  <ellipse cx="0" cy="86" rx="24" ry="16" class="goldd o"/></g>
{''.join(f'<g transform="translate({x} {y})"><ellipse rx="16" ry="11" fill="{GLD}" stroke="{INK}" stroke-width="2"/>'
         f'<path d="M-12-4h24M-6-8h12" fill="none" stroke="{INK}" stroke-width="2"/>'
         f'<ellipse cx="-2" cy="-12" rx="12" ry="6" fill="#dfe6ea" opacity="0.85"/></g>' for x, y in [(400,150),(460,230),(390,290),(510,170)])}''')

add('head for', 'めざす場所へ向かって進む', f'''
<path d="M40 340q160-20 300-30t220-40" fill="none" stroke="{GLDD}" stroke-width="9" stroke-dasharray="18 14"/>
{person(150, 330, 1.2, 1, 'teal', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g transform="translate(510 270)"><path d="M0 0v-120" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M0-120h-90l22 30-22 30h90z" class="coral o"/></g>
<path d="M230 200h200" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('hear from', '相手から手紙が届いて、たよりを受け取る', f'''
{person(150, 306, 1.2, -1, 'coral', 'blue', 'give', 'bun', 'smile')}
<path d="M470 200h-180" class="a" stroke-width="5" marker-end="url(#ar)"/>
<g transform="translate(330 260)"><rect x="-70" y="-46" width="140" height="92" rx="8" class="paper"/>
  <path d="M-70-46L0 10l70-56" fill="none" class="o"/></g>
{person(500, 306, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'smile')}''', arrow=True)

add('hear of', '人づてに、そういうものがあると知る', f'''
{head(90, 250, 26, 'violet', 'bun')}
{head(230, 250, 26, 'coral', 'bob')}
{head(370, 250, 26, 'green', 'short')}
{head(510, 250, 30, 'teal', 'short')}
{''.join(f'<path d="M{126+i*140} 230h60" class="a" marker-end="url(#ar)"/>' for i in range(3))}
<g transform="translate(300 110)"><rect x="-90" y="-50" width="180" height="100" rx="20" class="paper"/>
  <path d="M-60 44l-20 30 40-30z" class="paper"/>
  {box(0, 0, 70, 48, 14, 'gold')}</g>''', arrow=True)

add('hope for', '手を合わせて、こうなればと願う', f'''
{person(200, 306, 1.25, 1, 'teal', 'blue', 'hold', 'bob', 'smile')}
{hand(230, 220, 1)}
<g transform="translate(440 190)"><ellipse rx="120" ry="86" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
  {sun(-30, -20, 26)}
  <path d="M-60 50q60-40 120 0" fill="none" stroke="{GRN}" stroke-width="6"/></g>
<circle cx="300" cy="230" r="9" fill="#fffefd" class="o"/>
<circle cx="326" cy="200" r="13" fill="#fffefd" class="o"/>''')

# --- 記号・慣用 ---------------------------------------------------------------

add('hyphen', '二つの語をつなぐ、短い横線', f'''
{word(170, 200, 3, 34, INK)}
<path d="M262 200h76" stroke="{CRL}" stroke-width="14" stroke-linecap="round" fill="none"/>
{word(450, 200, 3, 34, INK)}
{ring(300, 200, 62)}''')

add('in a nutshell', '山ほどの話を、ひと言にまとめる', f'''
{''.join(f'<g transform="translate({130+ (i%2)*8} {300-i*30}) rotate({-4+i*3})">'
         f'<rect x="-80" y="-14" width="160" height="28" rx="4" class="paper"/></g>' for i in range(7))}
<path d="M250 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 220)"><ellipse rx="86" ry="96" fill="#b98d55" class="o"/>
  <ellipse rx="70" ry="80" fill="#e6cfa4" class="o"/>
  {word(0, 0, 3, 26, TEA)}</g>''', arrow=True)

add('if anything', 'どちらかといえば、むしろこちら寄り', f'''
{scalebar(300, 250, -6, 1)}
{box(130, 250, 90, 62, 18, 'teal')}
{box(470, 262, 84, 58, 16, 'coral')}
<path d="M130 130v54M470 148v52" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M300 350h-40" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M60 176h480"/></g>''', arrow=True)

add('in accordance with', '手引きに書いてあるとおりに、そのまま行う', f'''
<g transform="translate(160 190)"><rect x="-100" y="-120" width="200" height="240" rx="8" class="paper"/>
  {''.join(f'<g><circle cx="-70" cy="{-84+i*54}" r="9" class="teal o"/>'
           f'<rect x="-50" y="{-92+i*54}" width="{124-(i%2)*36}" height="16" rx="8" fill="{MUTED}"/></g>' for i in range(4))}</g>
<path d="M290 190h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(460 190)">
  {''.join(f'<g><circle cx="-70" cy="{-84+i*54}" r="9" class="teal o"/>'
           f'<rect x="-50" y="{-92+i*54}" width="{124-(i%2)*36}" height="16" rx="8" fill="{MUTED}"/></g>' for i in range(4))}</g>
<g transform="translate(460 330)"><path d="M-30 0l24 26 48-56" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>''', arrow=True)

add('in line with', '引いた線に、きちんとそろえて並べる', f'''
<path d="M60 210h480" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="14 10"/>
{''.join(f'<rect x="{90+i*90}" y="130" width="60" height="80" rx="8" class="teal o"/>' for i in range(5))}
{''.join(f'<path d="M{120+i*90} 240v30" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(5))}
<path d="M90 300h420" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('in contrast to', '一方は高く、もう一方は低い。並べると差がはっきりする', f'''
{split()}
<rect x="100" y="90" width="100" height="220" rx="8" class="teal o"/>
<rect x="400" y="250" width="100" height="60" rx="8" class="coral o"/>
<path d="M230 200h140" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
<path d="M60 340h480" fill="none" stroke="{MUTED}" stroke-width="4"/>''', arrow=True)

add('in place of', 'もとのものに代えて、こちらを入れる', f'''
<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="11 9">
  <rect x="200" y="150" width="200" height="140" rx="10"/></g>
<g transform="translate(300 220)">{box(0, 0, 170, 120, 34, 'coral')}</g>
<path d="M300 90v40" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g opacity="0.35" transform="translate(520 300)">{box(0, 0, 120, 86, 24, 'teal')}</g>
<path d="M400 330h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''', arrow=True)

add('in favour of', 'そちらに賛成だと、手を上げる', f'''
{''.join(f'<g transform="translate({100+i*100} 340)">{person(0, 0, 1.0, 1, c, "blue", "up", h, "smile")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun')]))}
<g transform="translate(500 200)"><rect x="-70" y="-90" width="140" height="180" rx="8" class="paper"/>
  {''.join(f'<rect x="-50" y="{-60+i*40}" width="{100-(i%2)*30}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}</g>
{''.join(f'<path d="M{140+i*100} 150l{300-i*100} 20" fill="none" stroke="{MUTED}" stroke-width="0"/>' for i in range(0))}
<path d="M340 150h80" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('in effect', 'きょうから、その決まりが正式にはたらく', f'''
<g transform="translate(280 200)"><rect x="-160" y="-130" width="320" height="260" rx="10" class="paper"/>
  {''.join(f'<rect x="-130" y="{-96+i*54}" width="{240-(i%2)*70}" height="16" rx="8" fill="{MUTED}"/>' for i in range(4))}
  <circle cx="90" cy="86" r="36" fill="none" stroke="{CRL}" stroke-width="7"/></g>
<g transform="translate(490 130)"><path d="M-46 0v-70h92V0z" class="teald o"/>
  <path d="M-36 0v-60h72V0z" fill="#fffefd" class="o"/>
  <path d="M-36-30h72" fill="none" stroke="{CRL}" stroke-width="6"/></g>
<path d="M490 200v50" class="a" marker-end="url(#ar)"/>
<g transform="translate(490 320)"><path d="M-30 0l24 26 48-56" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>''', arrow=True)

add('in due course', '急がなくても、しかるべき時になれば届く', f'''
{hourglass(160, 200, 1.0)}
<path d="M270 200h70" class="a" marker-end="url(#ar)"/>
<path d="M360 300h200" fill="none" stroke="{MUTED}" stroke-width="5"/>
{''.join(f'<circle cx="{380+i*60}" cy="300" r="10" class="tealp o"/>' for i in range(3))}
<circle cx="540" cy="300" r="16" class="coral o"/>
<g transform="translate(540 190)"><rect x="-50" y="-40" width="100" height="80" rx="8" class="paper"/>
  <path d="M-50-40L0 0l50-40" fill="none" class="o"/></g>
<path d="M540 240v34" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('in principle', '筋のうえでは通るが、細かいところはこれから', f'''
<g transform="translate(200 190)"><rect x="-130" y="-120" width="260" height="240" rx="8" fill="#2f5f8e" class="o"/>
  <g fill="none" stroke="#dce9f5" stroke-width="4">
    <path d="M-100 90v-80l100-70 100 70v80z"/><path d="M-40 90v-56h80v56"/></g></g>
<g transform="translate(200 330)"><path d="M-30 0l24 26 48-56" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="11 9">
  <rect x="390" y="110" width="170" height="70" rx="8"/><rect x="390" y="200" width="170" height="70" rx="8"/></g>
<g transform="translate(475 320)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''')

add('in retrospect', '今になって振り返ると、あの時こうだったと分かる', f'''
{person(430, 306, 1.25, -1, 'teal', 'blue', 'stand', 'short', 'neutral')}
<circle cx="340" cy="190" r="9" fill="#fffefd" class="o"/>
<circle cx="312" cy="158" r="13" fill="#fffefd" class="o"/>
<g transform="translate(180 150)"><ellipse rx="130" ry="92" fill="#fffefd" class="o"/>
  <path d="M-90 50h180" fill="none" stroke="{MUTED}" stroke-width="4"/>
  {person(-30, 44, 0.5, 1, 'coral', 'blue', 'reach', 'short', 'neutral')}
  <path d="M20 10l40 30" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{bulb(500, 150, 0.9)}
<path d="M470 340h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('in light of', '新しく分かったことを踏まえて、判断を改める', f'''
<g transform="translate(150 180)"><rect x="-100" y="-90" width="200" height="180" rx="8" class="paper"/>
  {''.join(f'<rect x="-76" y="{-56+i*44}" width="{150-(i%2)*46}" height="14" rx="7" fill="{MUTED}"/>' for i in range(3))}</g>
{bulb(150, 350, 0.8)}
<path d="M270 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(460 200)"><rect x="-110" y="-110" width="220" height="220" rx="8" class="paper"/>
  {''.join(f'<rect x="-86" y="{-76+i*50}" width="{170-(i%2)*50}" height="14" rx="7" fill="{MUTED}"/>' for i in range(3))}
  <path d="M-86 66h130" fill="none" stroke="{CRL}" stroke-width="8"/></g>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
