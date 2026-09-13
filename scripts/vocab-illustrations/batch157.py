# -*- coding: utf-8 -*-
"""第157回。de-/di-/do-/dr-/du- の名詞と句動詞。"""
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

def car(x, y, s=1, cls='coral', f=1):
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M-90 0v-30l26-36h116l28 36V0z" class="{cls} o"/>'
            f'<path d="M-54-66l16-22h72l18 22z" class="bluep o"/>'
            f'<circle cx="-52" cy="4" r="20" fill="none" stroke="{INK}" stroke-width="7"/>'
            f'<circle cx="56" cy="4" r="20" fill="none" stroke="{INK}" stroke-width="7"/></g>')

def house(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-80 0v-100h160V0z" fill="#fffefd" class="o"/>'
            f'<path d="M-94-100L0-166l94 66z" class="{cls}d o"/>'
            f'<path d="M-24 0v-56h48V0z" class="{cls} o"/>'
            f'<rect x="-62" y="-82" width="34" height="30" class="{cls}p o"/></g>')

def flag(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0v-110" fill="none" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M0-110h70l-16 26 16 26H0z" class="{cls} o"/></g>')

# --- 広がる・散る -------------------------------------------------------------

add('diffusion', '一滴のインクが、水ぜんたいに広がっていく', f'''
{split()}
<g transform="translate(150 230)"><path d="M-80-110h160v220h-160z" fill="#eaf4fb" class="o"/>
  <path d="M-70-80h140v180h-140z" fill="{BLUP}"/>
  <circle cx="0" cy="-40" r="26" class="violet o"/>
  <path d="M-80-110h160v220h-160z" fill="none" class="o"/></g>
<path d="M240 200h120" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 230)"><path d="M-80-110h160v220h-160z" fill="#eaf4fb" class="o"/>
  <path d="M-70-80h140v180h-140z" fill="{VIOP}"/>
  <path d="M-80-110h160v220h-160z" fill="none" class="o"/></g>''', arrow=True)

add('dispersal', 'かたまっていたものが、四方へ散らばる', f'''
<g opacity="0.4">{''.join(f'<circle cx="{150+ (i%3)*30}" cy="{170+(i//3)*30}" r="16" class="teal o"/>' for i in range(9))}</g>
{''.join(f'<circle cx="{300+150*math.cos(math.radians(a)):.0f}" cy="{200+110*math.sin(math.radians(a)):.0f}" r="18" class="teal o"/>' for a in range(0, 360, 45))}
{''.join(f'<path d="M{300+70*math.cos(math.radians(a)):.0f} {200+52*math.sin(math.radians(a)):.0f}L{300+120*math.cos(math.radians(a)):.0f} {200+88*math.sin(math.radians(a)):.0f}" class="a" marker-end="url(#ar)"/>' for a in range(0, 360, 45))}''', arrow=True)

add('dissolution', '組織の輪がとけて、めいめいが去っていく', f'''
<g transform="translate(230 200)"><path d="M-140 0a140 100 0 1 1 200 92" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 14"/></g>
{''.join(f'<g transform="translate({230+120*math.cos(math.radians(a)):.0f} {286+86*math.sin(math.radians(a)):.0f})">{head(0, 0, 22, c, h)}</g>'
         for a, (c, h) in zip([200, 250, 300], [('teal','short'),('coral','bob'),('gold','bun')]))}
{person(470, 306, 1.05, 1, 'violet', 'blue', 'walk', 'short', 'neutral')}
{person(560, 306, 1.0, 1, 'green', 'blue', 'walk', 'bob', 'neutral')}
<path d="M340 130h160" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('disarray', '整っていた列が崩れて、ばらばらになる', f'''
{split()}
{''.join(f'<rect x="{80+ (i%3)*54}" y="{150+(i//3)*60}" width="40" height="44" rx="6" class="tealp o"/>' for i in range(9))}
{ring(150, 210, 132, True)}
{''.join(f'<rect x="-20" y="-22" width="40" height="44" rx="6" class="tealp o" transform="translate({360+ (i%3)*60+(i%2)*20} {150+(i//3)*66+(i%3)*14}) rotate({-40+i*22})"/>' for i in range(9))}
{ring(450, 210, 132)}''')

# --- ちがい・ずれ -------------------------------------------------------------

add('deviation', '決められた線から、外れて進んでしまう', f'''
<path d="M60 200h480" fill="none" stroke="{TEA}" stroke-width="8" stroke-dasharray="16 12"/>
<path d="M60 200h180q100 0 160 90" fill="none" stroke="{CRL}" stroke-width="7" marker-end="url(#ar)"/>
{''.join(f'<circle cx="{100+i*60}" cy="200" r="9" class="teald o"/>' for i in range(3))}
<path d="M400 200v70" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>
<path d="M410 236h40" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('discrepancy', '二つの記録の数字が、そろっていない', f'''
{''.join(f'<g transform="translate({150+i*300} 200)"><rect x="-110" y="-130" width="220" height="260" rx="8" class="paper"/>'
         f'{"".join(f2 for f2 in ["<rect x=@-86@ y=@" + str(-96+j*52) + "@ width=@110@ height=@14@ rx=@7@ fill=@" + MUTED + "@/><rect x=@36@ y=@" + str(-96+j*52) + "@ width=@" + str(50-(j%2)*16) + "@ height=@14@ rx=@7@ class=@" + ("coral" if (i==1 and j==2) else "teal") + "@/>" for j in range(4)])}</g>'.replace('@', chr(34)) for i in range(2))}
<g fill="none" stroke="{CRL}" stroke-width="5"><path d="M280 108h40M320 108l-14-10M320 108l-14 10"/></g>
{ring(300, 108, 60)}''')

add('disparity', '同じ町なのに、暮らしの差が大きい', f'''
{split()}
{house(150, 306, 0.5, 'coral')}
{ring(150, 250, 122, True)}
<g transform="translate(450 306)"><path d="M-140 0v-180h280V0z" fill="#fffefd" class="o"/>
  <path d="M-156-180h312l-40-50h-232z" class="teald o"/>
  {''.join(f'<rect x="{-110+ (i%4)*60}" y="{-150+(i//4)*60}" width="40" height="40" class="tealp o"/>' for i in range(8))}</g>
{ring(450, 220, 148)}
<path d="M60 380h480" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('distortion', 'まっすぐの升目が、ぐにゃりとゆがむ', f'''
{split()}
<g transform="translate(150 200)">
  {''.join(f'<path d="M-96 {-96+i*48}h192" fill="none" stroke="{TEA}" stroke-width="4"/>' for i in range(5))}
  {''.join(f'<path d="M{-96+i*48} -96v192" fill="none" stroke="{TEA}" stroke-width="4"/>' for i in range(5))}</g>
{ring(150, 200, 132, True)}
<g transform="translate(450 200)">
  {''.join(f'<path d="M-96 {-96+i*48}q48 {-30+i*16} 96 0t96 {10-i*10}" fill="none" stroke="{TEA}" stroke-width="4"/>' for i in range(5))}
  {''.join(f'<path d="M{-96+i*48} -96q{-20+i*12} 48 0 96t{16-i*8} 96" fill="none" stroke="{TEA}" stroke-width="4"/>' for i in range(5))}</g>
{ring(450, 200, 138)}''')

# --- 取り上げ・追い出し --------------------------------------------------------

add('deprivation', '当たり前にあるはずのものが、取り上げられて空になる', f'''
{table(330)}
{''.join(f'<g transform="translate({120+i*110} 280)"><ellipse rx="46" ry="14" fill="#fffefd" class="o"/>'
         f'<circle cx="0" cy="-12" r="{16 if i < 2 else 0}" class="goldp o"/></g>' for i in range(2))}
{''.join(f'<g transform="translate({340+i*110} 280)"><ellipse rx="46" ry="14" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/></g>' for i in range(2))}
{hand(460, 160, -1)}
<path d="M420 200l-40 60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
{head(90, 200, 26, 'coral', 'short')}''')

add('deportation', '旅券に印を押され、国境の外へ送り返される', f'''
<path d="M300 60v300" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="16 12"/>
{flag(200, 130, 0.8, 'teal')}
{flag(400, 130, 0.8, 'coral')}
{person(400, 330, 1.15, 1, 'violet', 'blue', 'walk', 'short', 'sad')}
<path d="M250 250h130" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(140 290) rotate(-8)"><rect x="-46" y="-62" width="92" height="124" rx="6" class="blued o"/>
  <circle cy="-14" r="22" fill="none" stroke="#fffefd" stroke-width="4"/>
  <circle cx="20" cy="30" r="20" fill="none" stroke="{CRL}" stroke-width="5"/></g>''', arrow=True)

add('displacement', '住んでいた家を離れ、荷物を持って移る', f'''
{house(120, 306, 0.7, 'coral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M190 200h60"/></g>
{person(300, 330, 1.1, 1, 'teal', 'blue', 'carry', 'bun', 'sad', 'walk')}
<g transform="translate(316 240)"><path d="M-40-26h80v52h-80z" class="violet o"/>
  <path d="M-16-26v-14h32v14" fill="none" class="a"/></g>
{person(400, 330, 0.72, 1, 'coral', 'green', 'walk', 'bob', 'sad')}
<path d="M260 120h240" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('desertion', '仲間を残して、ひとりだけその場を去る', f'''
{person(180, 306, 1.15, 1, 'coral', 'blue', 'reach', 'short', 'sad')}
{person(280, 306, 1.1, 1, 'gold', 'blue', 'reach', 'bob', 'sad')}
{person(470, 306, 1.15, 1, 'violet', 'blue', 'walk', 'short', 'neutral')}
<path d="M340 220h80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<path d="M400 120h160" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('disregard', '目に入っているのに、札を押しのけて通る', f'''
<g transform="translate(250 200) rotate(-16)"><rect x="-80" y="-56" width="160" height="112" rx="8" class="paper"/>
  <path d="M-56 0h112" fill="none" stroke="{CRL}" stroke-width="10"/></g>
{hand(340, 200, 1)}
<path d="M390 200h60" fill="none" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
{person(160, 340, 1.1, 1, 'teal', 'blue', 'walk', 'short', 'neutral', 'walk')}
<path d="M200 300h180" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''', arrow=True)

# --- 気持ち ------------------------------------------------------------------

add('desperation', '打つ手がなくなり、なりふりかまわず手を伸ばす', f'''
<path d="M0 306h600v94H0z" class="ground"/>
{''.join(f'<rect x="-40" y="-30" width="80" height="60" rx="6" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9" transform="translate({x} {y}) rotate({r})"/>' for x, y, r in [(140,140,-20),(460,130,16),(500,260,-10)])}
{person(280, 306, 1.3, 1, 'coral', 'blue', 'reach', 'short', 'sad')}
{''.join(drop(x, y, 1.0) for x, y in [(220,180),(350,186)])}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M150 230q16-20 0-40M420 240q-16-20 0-40"/></g>''')

add('disbelief', '目の前のことが、どうしても信じられない', f'''
{person(200, 306, 1.25, 1, 'teal', 'blue', 'hold', 'short', 'surprised')}
<g transform="translate(180 190)"><circle r="12" fill="#fffefd" class="o"/><circle r="5" class="ink"/></g>
<g transform="translate(220 190)"><circle r="12" fill="#fffefd" class="o"/><circle r="5" class="ink"/></g>
<g transform="translate(460 210)"><circle r="90" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
  <path d="M-40 40l70-100 40 46 30-40" fill="none" stroke="{CRL}" stroke-width="7"/></g>
<g transform="translate(330 110)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''')

add('discouragement', 'うまくいかず、胸の火が小さくしぼむ', f'''
{split()}
{person(150, 306, 1.2, 1, 'coral', 'blue', 'up', 'short', 'smile')}
<g transform="translate(150 210) scale(0.42)">{flame(0, 40, 1)}</g>
{ring(150, 210, 130, True)}
{person(450, 306, 1.2, 1, 'blue', 'blue', 'hold', 'short', 'sad')}
<g transform="translate(450 214)" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="7 6">
  <path d="M0 0c-12-6-14-22-2-34 2 9 7 10 9 5 2-8 9-12 12-18 4 12 12 14 12 25C31-9 18 5 0 0z"/></g>
{''.join(f'<path d="M{420+i*30} {150-i*16}q-14 14 0 28" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{ring(450, 210, 130)}''')

add('detachment', '感情の渦から一歩引いて、冷静に見る', f'''
<g opacity="0.9">{''.join(f'<g transform="translate({80+i*80} 306)">{person(0, 0, 1.0, 1, c, "blue", "up", h, "sad")}</g>'
         for i, (c, h) in enumerate([('coral','short'),('gold','bob'),('violet','short')]))}</g>
{''.join(f'<path d="M{100+i*80} 160q16-20 0-40" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}
<path d="M370 60v300" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"/>
{person(480, 306, 1.2, -1, 'teal', 'blue', 'stand', 'bun', 'neutral')}
<path d="M420 200h20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('devotion', '毎日欠かさず、心をこめて世話をする', f'''
{table(330)}
<g transform="translate(400 306)"><path d="M-56 0l8-70h96l8 70z" class="corald o"/>
  <path d="M-60-70h120v-16h-120z" class="coral o"/>
  <path d="M0-86v-70" fill="none" stroke="{GRND}" stroke-width="7"/>
  <path d="M0-120q-40-8-46-46 38 4 46 34zM0-140q40-10 46-48-38 6-46 36z" class="greenp o"/></g>
{person(180, 306, 1.2, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
<g transform="translate(280 200) rotate(48)"><path d="M-24 0v-46h48V0z" class="blue o"/>
  <path d="M24-34l30-14v30z" class="blue o"/></g>
{''.join(drop(320 + i*16, 240 + i*14, 0.8) for i in range(3))}
<g transform="translate(150 150)"><path d="M0 22q-40-30-40-56 0-20 20-20 12 0 20 12 8-12 20-12 20 0 20 20 0 26-40 56z" class="coralp o"/></g>''')

# --- 力・支配 ----------------------------------------------------------------

add('deterrent', 'その手前で思いとどまらせる、大きな錠前', f'''
<g transform="translate(360 220)"><rect x="-90" y="-30" width="180" height="150" rx="18" class="gold o"/>
  <path d="M-50-30v-40a50 50 0 0 1 100 0v40" fill="none" stroke="{GLDD}" stroke-width="20"/>
  <circle cy="30" r="20" class="goldd o"/><path d="M0 46v34" stroke="{GLDD}" stroke-width="12"/></g>
{person(120, 306, 1.15, 1, 'coral', 'blue', 'reach', 'short', 'neutral')}
<path d="M190 240h50" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="9 8"/>
<path d="M250 240l-14-12M250 240l-14 12" fill="none" stroke="{CRL}" stroke-width="5"/>''')

add('domination', '大きな一つが、盤面ぜんたいを押さえている', f'''
<g transform="translate(300 210)"><rect x="-250" y="-150" width="500" height="300" rx="8" fill="#f2f5f6" class="o"/>
  {''.join(f'<path d="M{-250+ (i+1)*100} -150v300" fill="none" stroke="{MUTED}" stroke-width="2"/>' for i in range(4))}
  {''.join(f'<path d="M-250 {-150+(i+1)*100}h500" fill="none" stroke="{MUTED}" stroke-width="2"/>' for i in range(2))}</g>
<g opacity="0.35">{''.join(f'<circle cx="{110+i*90}" cy="320" r="20" class="tealp o"/>' for i in range(3))}</g>
<g transform="translate(320 190)"><circle r="110" class="coral o"/>
  <path d="M-46 22l-10-56 28 20 18-34 18 34 28-20-10 56z" class="gold o"/>
  <path d="M-46 22h92v14h-92z" class="goldd o"/></g>''')

add('devastation', '嵐が去ったあと、建物がなぎ倒されている', f'''
{cloud(160, 80, 1.6, 'violet')}{cloud(420, 70, 1.7, 'violet')}
<path d="M0 306h600v94H0z" class="ground"/>
{''.join(f'<g transform="translate({100+i*140} 306) rotate({-24+i*18})">'
         f'<path d="M-60 0v-90h120V0z" fill="#c3cbd1" class="o"/>'
         f'<path d="M-60-90l30-30 26 30" fill="none" stroke="{MUTED}" stroke-width="5"/></g>' for i in range(3))}
{''.join(f'<rect x="{440+ (i%3)*36}" y="{280+(i//3)*20}" width="30" height="18" rx="3" fill="#c3cbd1" stroke="{INK}" stroke-width="2" transform="rotate({-30+i*24} {455+(i%3)*36} {289+(i//3)*20})"/>' for i in range(6))}
{''.join(f'<path d="M{80+i*90} 180l-20 40" fill="none" stroke="{BLU}" stroke-width="5"/>' for i in range(6))}''')

# --- しくみ・お金 -------------------------------------------------------------

add('depreciation', '年がたつほど、車の値打ちが下がっていく', f'''
<path d="M60 340h480M90 360V80" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M110 110l100 70 100 60 100 50 100 30" fill="none" stroke="{CRL}" stroke-width="7"/>
{''.join(f'<circle cx="{110+i*100}" cy="{110+ [0,70,130,180,210][i]}" r="9" class="coral o"/>' for i in range(5))}
{car(200, 130, 0.4, 'teal')}
{car(480, 340, 0.4, 'teal')}
{''.join(f'<path d="M{110+i*100} 350v14" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(5))}''')

add('dividend', '会社のもうけを、持ち主たちに分け与える', f'''
<g transform="translate(300 130)"><circle r="80" class="goldp o"/>
  {''.join(f'<path d="M0 0l{80*math.cos(math.radians(a)):.0f} {80*math.sin(math.radians(a)):.0f}" fill="none" stroke="{GLDD}" stroke-width="3"/>' for a in range(0, 360, 90))}
  <path d="M0 0v-80a80 80 0 0 1 80 80z" class="gold o"/></g>
{''.join(f'<g transform="translate({120+i*120} 330)">{head(0, 0, 26, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('violet','short'),('green','bun')]))}
{''.join(f'<path d="M{280+ (i-1.5)*40:.0f} 220L{120+i*120} 290" class="a" marker-end="url(#ar)"/>' for i in range(4))}''', arrow=True)

add('downturn', '売り上げの線が、右下へ落ちこむ', f'''
<path d="M60 340h480M90 360V70" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M110 240l80-70 80 40 80-30 80 100 80 60" fill="none" stroke="{TEA}" stroke-width="7"/>
{''.join(f'<circle cx="{110+i*80}" cy="{y}" r="9" class="teal o"/>' for i, y in enumerate([240, 170, 210, 180, 280, 340]))}
<path d="M350 200l160 130" fill="none" stroke="{CRL}" stroke-width="0"/>
<g transform="translate(470 130)"><path d="M-80 60v-100h160v100z" fill="#dfe6ea" class="o"/>
  <path d="M-50-40v-40h26v40zM10-40v-56h26v56z" class="teald o"/></g>
<path d="M390 250l100 80" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('downfall', '高い台から、まっさかさまに落ちる', f'''
<g transform="translate(150 306)"><path d="M-70 0v-40h140V0z" class="goldd o"/>
  <path d="M-50-40v-140h100v140z" class="gold o"/></g>
<g opacity="0.3">{person(150, 166, 1.0, 1, 'violet', 'blue', 'up', 'short', 'smile')}</g>
<g transform="translate(430 300) rotate(140)">{person(0, 0, 1.1, 1, 'violet', 'blue', 'up', 'short', 'surprised')}</g>
<path d="M220 130q120-30 190 110" fill="none" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(340 220) rotate(40)"><path d="M-30 14l-8-38 20 14 12-22 12 22 20-14-8 38z" class="gold o"/></g>''', arrow=True)

add('distributor', '工場から品を引き取り、多くの店に配る', f'''
<g transform="translate(90 306)"><path d="M-70 0v-100h140V0z" fill="#dfe6ea" class="o"/>
  <path d="M-44-100v-34h22v34zM10-100v-44h22v44z" class="teald o"/></g>
<g transform="translate(280 290)"><path d="M-90 0v-56h110v56z" class="teal o"/>
  <path d="M20-40h50l26 40h-76z" class="tealp o"/>
  <circle cx="-50" cy="8" r="18" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="60" cy="8" r="18" fill="none" stroke="{INK}" stroke-width="7"/></g>
<path d="M170 200h60" class="a" marker-end="url(#ar)"/>
{''.join(f'<g transform="translate({450+ (i%2)*100} {160+(i//2)*150})"><path d="M-50 0v-56h100V0z" fill="#fffefd" class="o"/>'
         f'<path d="M-58-56h116l-16-24h-84z" class="{c} o"/></g>' for i, c in enumerate(['coral','violet','gold','green']))}
{''.join(f'<path d="M380 {240-i*20}l50 {-60+i*130}" class="a" marker-end="url(#ar)"/>' for i in range(2))}''', arrow=True)

add('dispatch', '荷物を仕分けて、すぐさま送り出す', f'''
{table(330)}
{''.join(box(120 + i*76, 290, 62, 48, 16, c) for i, c in enumerate(['gold','coral','teal']))}
<path d="M330 230h50" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(480 280)"><path d="M-90 0v-60h110v60z" class="coral o"/>
  <path d="M20-44h48l24 44h-72z" class="coralp o"/>
  <circle cx="-50" cy="10" r="20" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="58" cy="10" r="20" fill="none" stroke="{INK}" stroke-width="7"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M390 190h-40M400 150h-60"/></g>''', arrow=True)

# --- 情報・ことば -------------------------------------------------------------

add('disinformation', 'わざと嘘の知らせを流して、広めさせる', f'''
{person(110, 306, 1.15, 1, 'violet', 'blue', 'give', 'short', 'neutral')}
<g transform="translate(240 200)"><rect x="-70" y="-50" width="140" height="100" rx="8" class="paper"/>
  <rect x="-50" y="-30" width="100" height="12" rx="6" class="coral"/>
  <rect x="-50" y="-4" width="70" height="10" rx="5" fill="{MUTED}"/>
  <path d="M20 20l30 30M50 20l-30 30" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{''.join(f'<g transform="translate({400+ (i%2)*110} {150+(i//2)*130})">{head(0, 0, 26, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun'),('green','short')]))}
{''.join(f'<path d="M320 {190+i*20}l{60+i*20} {-30+i*100}" class="a" stroke="{CRL}" marker-end="url(#ar)"/>' for i in range(2))}''', arrow=True)

add('disclaimer', '広告の下に小さく置かれた、責任を負わない断り書き', f'''
<g transform="translate(300 170)"><rect x="-250" y="-120" width="500" height="240" rx="10" class="paper"/>
  {word(0, -50, 4, 60, CRL)}
  {box(-140, 60, 110, 76, 24, 'gold')}
  <rect x="20" y="20" width="200" height="16" rx="8" fill="{MUTED}"/>
  <rect x="20" y="56" width="150" height="16" rx="8" fill="{MUTED}"/></g>
<g transform="translate(300 340)"><rect x="-250" y="-40" width="500" height="80" rx="6" fill="#f2f5f6" class="o"/>
  {''.join(f'<rect x="-230" y="{-26+i*18}" width="{440-(i%2)*90}" height="7" rx="3.5" fill="{MUTED}"/>' for i in range(3))}</g>
{ring(300, 340, 0) if False else ''}
<rect x="46" y="298" width="508" height="84" rx="8" fill="none" stroke="{CRL}" stroke-width="4"/>''')

add('depiction', '目の前のものを、絵に写しとる', f'''
<g transform="translate(120 250)"><path d="M-60 60q0-100 60-100t60 100z" class="tealp o"/>
  <circle cy="-70" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>
<path d="M210 200h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(400 210)"><rect x="-110" y="-130" width="220" height="260" rx="6" fill="#f7f3e8" class="o"/>
  <g transform="translate(0 40) scale(0.8)"><path d="M-60 60q0-100 60-100t60 100z" class="tealp o"/>
    <circle cy="-70" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g></g>
<g transform="translate(520 130) rotate(30)"><path d="M-8-80h16v110l-8 18-8-18z" class="coral o"/></g>''')

add('designation', 'ひとつだけに札をつけて、これと決める', f'''
{''.join(f'<circle cx="{110+i*95}" cy="240" r="40" class="tealp o"/>' for i in range(5))}
<circle cx="300" cy="240" r="40" class="teal o"/>
<g transform="translate(300 120) rotate(-8)"><path d="M-70-30h100l26 30-26 30h-100z" class="coral o"/>
  <circle cx="42" cy="0" r="7" fill="#fffefd"/></g>
<path d="M300 156v40" class="a" marker-end="url(#ar)"/>
{ring(300, 240, 62)}''', arrow=True)

add('diplomacy', '両国の代表が、席についてまとめる', f'''
{table(250)}
{flag(140, 200, 0.7, 'teal')}
{flag(460, 200, 0.7, 'coral')}
{person(180, 380, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(420, 380, 1.15, -1, 'coral', 'blue', 'give', 'bun', 'smile')}
<g transform="translate(300 290)">{hand(-18, 0, 1)}{hand(18, 0, -1)}</g>
{''.join(spark(x, y, 0.8) for x, y in [(250,240),(360,236)])}''')

add('disappearance', 'そこにあったはずのものが、あとかたもなく消える', f'''
{table(330)}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10">
  <rect x="220" y="200" width="160" height="106" rx="8"/>
  <path d="M220 200l30-30h160l-30 30M380 200l30-30v106l-30 30"/></g>
{''.join(f'<ellipse cx="{130-i*0}" cy="{0}" rx="0" ry="0"/>' for i in range(0))}
{''.join(f'<ellipse cx="{100+i*40}" cy="{350+(i%2)*16}" rx="15" ry="8" class="ink" opacity="{0.5-i*0.12:.2f}"/>' for i in range(3))}
{head(500, 250, 28, 'coral', 'short')}
<path d="M460 240l-60 20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<g transform="translate(520 150)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''')

add('disturbance', '静かな部屋に、大きな物音が割りこむ', f'''
<g transform="translate(300 200)"><rect x="-260" y="-160" width="520" height="320" rx="10" fill="#f4f7f8" class="o"/></g>
{sit(200, 330, 1.15, 1, 'teal', 'blue', 'bob', 'surprised', 'lap')}
{chair(214, 330, 1.05, 'gold', -1)}
<g transform="translate(470 300)"><path d="M-60 40q-16-40 6-56 34-24 70-2t30 58z" class="corald o"/>
  {''.join(f'<path d="M{-40+i*30} -30l-16-40" fill="none" stroke="{CRL}" stroke-width="6"/>' for i in range(4))}</g>
<g class="corals" stroke-width="7">{''.join(f'<path d="M470 160v-30" transform="rotate({d} 470 220)"/>' for d in [-40, 0, 40])}</g>
{''.join(f'<path d="M{330-i*24} {200+i*22}q-16 16 0 32" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}''')

add('diversion', '工事で通れず、わきの道へまわされる', f'''
<path d="M0 240h600v90H0z" fill="#c3cbd1"/>
<path d="M300 240v-160h300" fill="none" stroke="#c3cbd1" stroke-width="86"/>
<g transform="translate(430 285)"><path d="M-70 20h140v20h-140z" fill="#e08a3c" class="o"/>
  {''.join(f'<path d="M{-60+i*46} 0l-16 20h30l16-20z" fill="#e08a3c" class="o"/>' for i in range(3))}</g>
<path d="M60 285h180q60 0 60-60V110h180" fill="none" stroke="{CRL}" stroke-width="8" stroke-dasharray="16 12" marker-end="url(#ar)"/>
<g transform="translate(180 170)"><rect x="-70" y="-46" width="140" height="80" rx="8" class="paper"/>
  <path d="M-40 20h50v-40h20l-24-24-24 24h20v22h-42z" class="coral o" transform="rotate(90 0 0)"/></g>''', arrow=True)

add('distraction', 'やることの横から、気を引くものが割りこむ', f'''
{doc(180, 220, 170, 210, 4)}
{person(300, 340, 1.1, 1, 'teal', 'blue', 'reach', 'short', 'neutral')}
<g transform="translate(480 180)"><rect x="-70" y="-50" width="140" height="100" rx="10" class="teald o"/>
  <rect x="-56" y="-36" width="112" height="72" rx="4" fill="#bcd6e6"/>
  {''.join(spark(-30 + i*30, -6, 0.7) for i in range(3))}</g>
<path d="M330 240q60-40 100-40" fill="none" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
<path d="M270 250h-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''', arrow=True)

# --- 人・もの ----------------------------------------------------------------

add('descendant', 'ひとりの先祖から、下へ広がっていく子や孫', f'''
{head(300, 80, 30, 'violet', 'bun')}
<path d="M300 120v40M180 160h240M180 160v30M420 160v30" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<g transform="translate({x} 220)">{head(0, 0, 26, c, h)}</g>' for x, (c, h) in zip([180, 420], [('teal','short'),('coral','bob')]))}
<path d="M180 252v26M100 278h160M100 278v26M180 278v26M260 278v26" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M420 252v26M360 278h120M360 278v26M480 278v26" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<g transform="translate({x} 330)">{head(0, 0, 22, c, h)}</g>' for x, (c, h) in zip([100, 180, 260, 360, 480], [('green','short'),('gold','bob'),('blue','short'),('coral','cap'),('teal','bun')]))}
{ring(290, 330, 260, True)}''')

add('dweller', 'そこに住み、窓から顔を出す人', f'''
<g transform="translate(300 306)"><path d="M-130 0v-180h260V0z" fill="#fffefd" class="o"/>
  <path d="M-146-180L0-270l146 90z" class="corald o"/>
  <path d="M-30 0v-70h60V0z" class="coral o"/>
  <rect x="-104" y="-150" width="70" height="60" class="coralp o"/>
  <rect x="34" y="-150" width="70" height="60" class="coralp o"/></g>
{head(370, 176, 24, 'teal', 'bob')}
{hand(420, 190, -1)}
{tree(80, 340, 0.7)}''')

add('doorstep', '玄関の前の上がり段', f'''
<g transform="translate(300 306)"><path d="M-160 0v-260h320V0z" fill="#fffefd" class="o"/>
  <path d="M-70 0v-190h140V0z" class="goldp o"/>
  <circle cx="46" cy="-90" r="8" class="ink"/></g>
<g transform="translate(300 340)"><path d="M-120 34v-34h240v34z" fill="#c3cbd1" class="o"/>
  <path d="M-96 0v-30h192v30z" fill="#dfe6ea" class="o"/></g>
{box(220, 306, 70, 50, 16, 'coral')}
{ring(300, 336, 152)}''')

add('duvet', '羽根をつめた、ふくらんだかけ布団', f'''
<g transform="translate(300 300)"><path d="M-190 60v-30h380v30z" class="goldd o"/>
  <path d="M-190 30q0-90 26-100 164-30 328 0 26 10 26 100z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{-150+i*70} -66q0 60 0 96" fill="none" stroke="#e3e8eb" stroke-width="5"/>' for i in range(5))}
  <path d="M-164-70q164-30 328 0" fill="none" stroke="#e3e8eb" stroke-width="5"/></g>
{''.join(f'<path d="M{130+i*180} {110-i*10}q30-30 46 0-24 22-46 0z" fill="#fffefd" class="o"/>' for i in range(3))}''')

add('dullness', 'つやのある面と、くすんで冴えない面の対比', f'''
{split()}
<g transform="translate(150 200)"><rect x="-96" y="-96" width="192" height="192" rx="10" fill="#a9a79c" class="o"/></g>
{ring(150, 200, 132)}
<g transform="translate(450 200)"><rect x="-96" y="-96" width="192" height="192" rx="10" class="gold o"/>
  <path d="M-70 90l120-186h34l-120 186z" fill="#ffffff" opacity="0.45"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(390,130),(510,250)])}
{ring(450, 200, 132, True)}
{head(150, 350, 22, 'teal', 'short')}
<ellipse cx="150" cy="360" rx="9" ry="12" fill="{INK}"/>''')

add('diabetes', '血のなかの糖が多すぎる状態', f'''
{torso(300, 300, 1.0) if False else ''}
<g transform="translate(180 220)"><circle r="90" fill="{CRLP}" class="o"/>
  {''.join(f'<rect x="{-52+ (i%3)*40}" y="{-46+(i//3)*40}" width="26" height="26" rx="4" class="goldp o"/>' for i in range(9))}</g>
<g transform="translate(430 240)"><rect x="-90" y="-70" width="180" height="140" rx="12" class="teald o"/>
  <rect x="-72" y="-52" width="144" height="70" rx="6" fill="#dfe6ea"/>
  {''.join(f'<rect x="{-56+i*36}" y="-32" width="24" height="34" rx="4" class="coral"/>' for i in range(3))}
  <path d="M60 40h20" fill="none" stroke="{TEAP}" stroke-width="6"/></g>
{drop(320, 160, 1.2, 'coral')}''')

add('dress up', 'ふだん着から、きちんとした装いにする', f'''
{split()}
{person(150, 306, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
{ring(150, 210, 128, True)}
<g transform="translate(450 306)">
  <path d="M-14-8l-8 34M14-8l8 34" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-30-84q30-14 60 0l-10 76h-40z" fill="{VIOD}" class="o"/>
  <path d="M-10-84l10 30 10-30" fill="#fffefd" class="o"/>
  <path d="M-4-58l10 8-8 14" fill="none" stroke="{CRL}" stroke-width="5"/>
  <path d="M-26-78L-52-40M26-78l26 38" fill="none" stroke="{VIOD}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-116" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 -8) scale(1.06)" fill="{HAIR}"/>
  <circle cx="-9" cy="-112" r="2.6" class="ink"/><circle cx="9" cy="-112" r="2.6" class="ink"/>
  <path d="M-8-100q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(370,130),(540,140)])}
{ring(450, 210, 130)}''')

add('drop in', '約束なしに、ふらりと立ち寄る', f'''
<g transform="translate(430 306)"><path d="M-110 0v-210h220V0z" fill="#fffefd" class="o"/>
  <path d="M-80 0v-190h160V0z" class="goldp o"/><circle cx="52" cy="-96" r="8" class="ink"/></g>
{person(200, 306, 1.2, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<path d="M100 120q100-40 160 40" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"/>
{head(390, 200, 24, 'coral', 'bob')}
<g transform="translate(300 150)"><rect x="-50" y="-30" width="100" height="60" rx="16" class="paper"/>
  {''.join(f'<circle cx="{-20+i*20}" cy="0" r="5" fill="{MUTED}"/>' for i in range(3))}</g>''', arrow=True)

add('destiny', 'はじめから一本の道が引かれていて、行き着く先が決まっている', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<path d="M60 380q140-40 250-120t230-140" fill="none" stroke="{GLDD}" stroke-width="10" stroke-dasharray="20 14"/>
{person(160, 350, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'neutral', 'walk')}
<g transform="translate(520 130)"><circle r="46" class="goldp o"/>
  {''.join(f'<path d="M0 -60v-22" transform="rotate({d})"/>' for d in range(0, 360, 45))}</g>
<g class="golds" stroke-width="4">{''.join(f'<path d="M520 70v-22" transform="rotate({d} 520 130)"/>' for d in range(0, 360, 45))}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M300 200h60"/></g>''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
