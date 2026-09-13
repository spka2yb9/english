# -*- coding: utf-8 -*-
"""第164回。o-/ov-/pa- の名詞と慣用表現。"""
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

def house(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-80 0v-100h160V0z" fill="#fffefd" class="o"/>'
            f'<path d="M-94-100L0-166l94 66z" class="{cls}d o"/>'
            f'<path d="M-24 0v-56h48V0z" class="{cls} o"/>'
            f'<rect x="-62" y="-82" width="34" height="30" class="{cls}p o"/></g>')

def crown(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-46 22l-10-56 28 20 18-34 18 34 28-20-10 56z" class="gold o"/>'
            f'<path d="M-46 22h92v14h-92z" class="goldd o"/></g>')

def clock(x, y, s=1, h=12, m=0):
    ah = math.radians(h*30 + m*0.5 - 90); am = math.radians(m*6 - 90)
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="54" fill="#fffefd" class="o"/>'
            f'<path d="M0 0l{42*math.cos(am):.0f} {42*math.sin(am):.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M0 0l{28*math.cos(ah):.0f} {28*math.sin(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle r="4" class="ink"/></g>')

# --- over- -------------------------------------------------------------------

add('overlap', '二つの輪が、一部だけ重なりあう', f'''
<circle cx="230" cy="200" r="130" class="tealp o" opacity="0.85"/>
<circle cx="370" cy="200" r="130" class="coralp o" opacity="0.85"/>
<path d="M300 82a130 130 0 0 0 0 236 130 130 0 0 0 0-236z" class="violet o" opacity="0.9"/>
{ring(300, 200, 76)}''')

add('overload', '積みすぎて、荷台がたわんでしまう', f'''
{''.join(f'<g transform="translate({250+ (i%2)*10} {230-i*44}) rotate({-6+i*4})">{box(0, 0, 130, 40, 12, "gold")}</g>' for i in range(5))}
<g transform="translate(250 280)"><path d="M-140 0q140 30 280 0v-30h-280z" class="teal o"/>
  <circle cx="-90" cy="20" r="24" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle cx="90" cy="20" r="24" fill="none" stroke="{INK}" stroke-width="8"/></g>
<g fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round">
  <path d="M90 320h-40M470 320h40"/></g>
<g transform="translate(500 130)"><path d="M0-34l34 58h-68z" class="gold o"/>
  <path d="M0-12v12" fill="none" stroke="{INK}" stroke-width="4"/><circle cy="14" r="3" class="ink"/></g>''')

add('overwork', '夜ふけまで、山ほどの仕事に追われる', f'''
{table(340)}
{''.join(f'<g transform="translate({450+ (i%2)*8} {300-i*36}) rotate({-4+i*3})">'
         f'<rect x="-70" y="-16" width="140" height="32" rx="4" class="paper"/></g>' for i in range(6))}
{sit(200, 340, 1.25, 1, 'blue', 'blue', 'short', 'sad', 'lap')}
{chair(214, 340, 1.15, 'gold', -1)}
<path d="M176 236l14 6M224 236l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
{clock(110, 120, 0.7, 12, 0)}
<path d="M520 100a44 44 0 1 1-34-42 34 34 0 0 0 34 42z" class="goldp o"/>''')

add('overthrow', '民衆の手で、玉座がひっくり返される', f'''
<g transform="translate(400 306) rotate(150)"><path d="M-60 60v-60h120v60z" class="goldd o"/>
  <path d="M-46 0v-70q0-30 46-30t46 30V0z" class="gold o"/></g>
{crown(500, 130, 0.7)}
{''.join(f'<g transform="translate({70+i*80} 340)">{person(0, 0, 0.95, 1, c, "blue", "up", h, "neutral")}</g>'
         for i, (c, h) in enumerate([('coral','short'),('violet','bob'),('teal','cap')]))}
<path d="M280 180h80" class="a" stroke="{CRL}" stroke-width="7" marker-end="url(#ar)"/>''', arrow=True)

add('overhead', '売り上げと関係なく、毎月かかる固定の費用', f'''
<g transform="translate(300 130)"><path d="M-160 0v-90h320V0z" fill="#fffefd" class="o"/>
  <path d="M-174-90h348l-30-40h-288z" class="teal o"/></g>
{''.join(f'<g transform="translate({120+i*120} 300)"><rect x="-50" y="-70" width="100" height="70" rx="6" class="coralp o"/>'
         + s + '</g>' for i, s in enumerate([
  f'<g transform="translate(0 -36)">{house(0, 0, 0.2, "coral")}</g>',
  f'<path d="M-14-56l-10 34h20l-14 34 34-46h-22l16-22z" class="gold o"/>',
  f'<path d="M-24-46h48v40h-48z" fill="none" stroke="{BLU}" stroke-width="5"/><path d="M0-46v-14" fill="none" stroke="{BLU}" stroke-width="5"/>',
  f'<circle cy="-34" r="18" class="goldp o"/>']))}
<path d="M60 340h480" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('overdraft', '残高がゼロを割りこんで、マイナスになる', f'''
<path d="M60 200h480" fill="none" stroke="{INK}" stroke-width="5"/>
<path d="M90 360V90" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<rect x="{120+i*70}" y="{200-h}" width="46" height="{h}" rx="5" class="tealp o"/>' for i, h in enumerate([90, 60, 30]))}
{''.join(f'<rect x="{330+i*70}" y="200" width="46" height="{h}" rx="5" class="coral o"/>' for i, h in enumerate([40, 80, 120]))}
<path d="M540 200h20" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(500 120)"><path d="M-56-30h96l24 30-24 30h-96z" class="paper"/>
  <path d="M-40 0h50" stroke="{CRL}" stroke-width="10" stroke-linecap="round" fill="none"/></g>''')

add('offset', 'プラスとマイナスが打ち消しあって、差し引きゼロ', f'''
<path d="M60 210h480" fill="none" stroke="{INK}" stroke-width="5"/>
<rect x="120" y="90" width="90" height="120" rx="6" class="teal o"/>
<rect x="250" y="210" width="90" height="120" rx="6" class="coral o"/>
<g fill="none" class="a" stroke-width="6">
  <path d="M215 150h30" marker-end="url(#ar)"/><path d="M345 270h30" marker-end="url(#ar)"/></g>
<rect x="420" y="200" width="90" height="20" rx="6" fill="#dfe6ea" class="o"/>
<path d="M400 210h130" fill="none" stroke="{GRN}" stroke-width="6"/>''', arrow=True)

# --- 始まり・終わり -----------------------------------------------------------

add('onset', '熱の線が上がりはじめる、その始まり', f'''
<path d="M60 340h480M90 360V80" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M110 300h140l70-160 60 40 80 60" fill="none" stroke="{CRL}" stroke-width="7"/>
<circle cx="250" cy="300" r="14" class="coral o"/>
{ring(250, 300, 48)}
{''.join(f'<circle cx="{110+i*70}" cy="300" r="8" class="tealp o"/>' for i in range(2))}
{thermometer(520, 200, 0.85, 0.6)}''')

add('outset', '出発の線から、走りはじめる', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<path d="M120 100v260" fill="none" stroke="{INK}" stroke-width="8"/>
{''.join(f'<rect x="{120+ (i%2)*24}" y="{110+i*24}" width="24" height="24" fill="{INK if (i%2) else "#fffefd"}" stroke="{INK}" stroke-width="1.5"/>' for i in range(10))}
{person(230, 340, 1.2, 1, 'coral', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<path d="M300 240h200" class="a" stroke-width="6" marker-end="url(#ar)"/>
{ring(120, 230, 0) if False else ''}
<path d="M120 380h1" fill="none"/>''', arrow=True)

add('once and for all', '何度もくり返した争いに、これを最後の裁定を下す', f'''
<g opacity="0.3">{''.join(f'<g transform="translate({120+i*90} 300)"><rect x="-36" y="-36" width="72" height="72" rx="8" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g>' for i in range(3))}</g>
<g transform="translate(400 240) rotate(-24)"><path d="M-14 0h28v90h-28z" class="goldd o"/>
  <path d="M-50-40h100v44h-100z" class="goldd o"/></g>
<g transform="translate(400 340)"><rect x="-90" y="-16" width="180" height="32" rx="8" class="goldd o"/></g>
<g class="golds" stroke-width="6">{''.join(f'<path d="M400 280v-24" transform="rotate({d} 400 320)"/>' for d in [-40, 0, 40])}</g>
<path d="M60 130h480" fill="none" stroke="{CRL}" stroke-width="8"/>''')

add('onslaught', 'いっせいに、四方から激しく押し寄せる', f'''
<g transform="translate(320 210)"><path d="M0-110q66 26 92 38 0 100-92 142-92-42-92-142 26-12 92-38z" class="tealp o"/></g>
{''.join(f'<path d="M{320+250*math.cos(math.radians(a)):.0f} {210+180*math.sin(math.radians(a)):.0f}L{320+130*math.cos(math.radians(a)):.0f} {210+96*math.sin(math.radians(a)):.0f}" class="a" stroke="{CRL}" stroke-width="7" marker-end="url(#ar)"/>' for a in range(0, 360, 40))}''', arrow=True)

# --- 見る人・住む人 -----------------------------------------------------------

add('onlooker', '大道芸のまわりで、ながめている人たち', f'''
{person(300, 306, 1.2, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
{''.join(f'<circle cx="{x}" cy="{y}" r="20" class="{c} o"/>' for x, y, c in [(250,120,'gold'),(300,80,'teal'),(350,120,'violet')])}
{''.join(f'<g transform="translate({x} {y})">{head(0, 0, 24, c, h)}</g>' for x, y, (c, h) in
  zip([80, 150, 460, 530], [300, 340, 300, 340], [('teal','short'),('violet','bob'),('green','short'),('gold','bun')]))}
{''.join(f'<path d="M{120+i*20} {260-i*10}h1" fill="none"/>' for i in range(0))}
{ring(115, 320, 96)}''')

add('occupant', 'いま現にその席を使っている人', f'''
{''.join(f'<g transform="translate({110+i*130} 340)">{chair(0, 0, 1.0, "gold", -1)}</g>' for i in range(4))}
{sit(370, 340, 1.05, 1, 'teal', 'blue', 'short', 'smile', 'lap')}
<g transform="translate(370 150)"><rect x="-56" y="-24" width="112" height="48" rx="8" class="coral o"/></g>
{ring(370, 250, 118)}''')

add('outskirts', '町のはずれ。家がまばらになっていく', f'''
<path d="M0 306h600v94H0z" class="ground"/>
{''.join(f'<g transform="translate({60+i*50} 306) scale(0.5)">{house(0, 0, 1, "teal")}</g>' for i in range(3))}
{''.join(f'<g transform="translate({240+i*80} 306) scale(0.42)">{house(0, 0, 1, "coral")}</g>' for i in range(2))}
<g transform="translate(470 306) scale(0.4)">{house(0, 0, 1, 'violet')}</g>
{tree(560, 320, 0.6)}{tree(390, 330, 0.5)}
<path d="M60 380h480" fill="none" stroke="{GLDD}" stroke-width="8" stroke-dasharray="18 14"/>
{ring(500, 300, 108)}''')

add('organiser', 'かかりを割りふって、会をまとめる人', f'''
{person(150, 306, 1.25, 1, 'violet', 'blue', 'point', 'bun', 'neutral')}
<g transform="translate(150 200) rotate(-8)"><rect x="-46" y="-58" width="92" height="116" rx="6" class="paper"/>
  {''.join(f'<rect x="-32" y="{-40+i*26}" width="64" height="8" rx="4" fill="{MUTED}"/>' for i in range(4))}</g>
{''.join(f'<g transform="translate({330+ (i%2)*130} {230+(i//2)*120})">{head(0, 0, 26, c, h)}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','cap')]))}
{''.join(f'<path d="M230 {200+i*40}L{300+ (i%2)*130} {225+(i//2)*120}" class="a" marker-end="url(#ar)"/>' for i in range(4))}
{ring(150, 210, 122)}''', arrow=True)

# --- 圧力・試練 ---------------------------------------------------------------

add('oppression', '重い支配が、人びとの上にのしかかる', f'''
<g transform="translate(300 150)"><rect x="-220" y="-40" width="440" height="80" rx="8" fill="#5b6b78" class="o"/></g>
{crown(300, 60, 0.9)}
{''.join(f'<g transform="translate({100+i*100} 340)">{person(0, 0, 0.9, 1, c, "blue", "up", h, "sad")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun'),('green','short'),('violet','cap')]))}
{''.join(f'<path d="M{120+i*100} 210v30" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>' for i in range(4))}''', arrow=True)

add('ordeal', '長く険しい道をくぐりぬけ、へとへとで出てくる', f'''
<path d="M0 340h600v60H0z" class="ground"/>
{''.join(f'<path d="M{80+i*90} 340l{30} -{70+(i%3)*30}l{30} {70+(i%3)*30}z" fill="#c3cbd1" class="o"/>' for i in range(4))}
{cloud(150, 90, 1.4, 'violet')}
{''.join(f'<path d="M{100+i*40} {150+(i%3)*20}l-14 34" fill="none" stroke="{BLU}" stroke-width="4"/>' for i in range(8))}
<path d="M40 380q120-40 240 0t280-10" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
{person(500, 340, 1.2, 1, 'coral', 'blue', 'reach', 'cap', 'sad', 'walk')}
{drop(470, 210, 0.9)}''')

add('parole', '条件つきで、期日より早くおりの外へ出される', f'''
<g transform="translate(160 220)"><path d="M-96-96h192v192h-192z" fill="none" stroke="{INK}" stroke-width="6"/>
  {''.join(f'<path d="M{-66+i*34} -96v192" fill="none" stroke="{INK}" stroke-width="6"/>' for i in range(5))}
  <path d="M30-96v192" fill="none" stroke="{GLDD}" stroke-width="8" transform="rotate(24 30 0)"/></g>
{person(420, 306, 1.15, 1, 'teal', 'blue', 'walk', 'short', 'neutral')}
<path d="M280 220h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(520 190) rotate(-6)"><rect x="-56" y="-70" width="112" height="140" rx="6" class="paper"/>
  {''.join(f'<rect x="-40" y="{-46+i*30}" width="{80-(i%2)*24}" height="10" rx="5" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="26" cy="44" r="16" fill="none" stroke="{CRL}" stroke-width="4"/></g>
<g transform="translate(430 356)"><rect x="-26" y="-10" width="52" height="20" rx="10" class="coral o"/></g>''', arrow=True)

# --- 理由・立場 ---------------------------------------------------------------

add('on account of', '雨のせいで、その試合は取りやめになる', f'''
{cloud(160, 90, 1.5, 'violet')}
{''.join(f'<path d="M{80+i*40} {160+(i%3)*20}l-14 36" fill="none" stroke="{BLU}" stroke-width="5"/>' for i in range(7))}
<path d="M300 220h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 220)"><rect x="-110" y="-80" width="220" height="160" rx="10" class="paper"/>
  <circle cx="0" cy="-14" r="36" class="greenp o"/>
  <path d="M-60-70l120 140M60-70L-60 70" fill="none" stroke="{CRL}" stroke-width="8"/></g>''', arrow=True)

add('owing to', 'ストのせいで、列車が遅れている', f'''
{''.join(f'<g transform="translate({80+i*70} 306)">{person(0, 0, 0.9, 1, c, "blue", "up", h, "neutral")}</g>'
         for i, (c, h) in enumerate([('coral','short'),('violet','bob')]))}
{''.join(f'<g transform="translate({80+i*70} 200)"><rect x="-40" y="-30" width="80" height="60" rx="6" class="paper"/>'
         f'<rect x="-26" y="-8" width="52" height="10" rx="5" fill="{MUTED}"/></g>' for i in range(2))}
<path d="M260 220h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 280)"><path d="M-120 60V-40q0-24 24-24h216V60z" class="teal o"/>
  {''.join(f'<rect x="{-96+i*56}" y="-16" width="40" height="36" rx="5" class="tealp o"/>' for i in range(3))}
  <circle cx="-80" cy="66" r="16" fill="none" stroke="{INK}" stroke-width="7"/></g>
{clock(360, 120, 0.6, 3, 30)}''', arrow=True)

add('on the basis of', '積み上げた根拠のうえに、結論が立つ', f'''
{''.join(f'<rect x="{160+ (i%3)*90}" y="{270-(i//3)*54}" width="80" height="46" rx="6" class="tealp o"/>' for i in range(6))}
<g transform="translate(300 130)"><rect x="-110" y="-56" width="220" height="90" rx="10" class="coral o"/></g>
<path d="M300 200v-30" class="a" marker-end="url(#ar)"/>
<path d="M120 340h360" fill="none" stroke="{MUTED}" stroke-width="4"/>''', arrow=True)

add('on the grounds that', 'この理由をあげて、そう決めたと示す', f'''
<g transform="translate(170 200)"><rect x="-110" y="-120" width="220" height="240" rx="8" class="paper"/>
  {''.join(f'<rect x="-86" y="{-84+i*46}" width="{170-(i%2)*50}" height="14" rx="7" fill="{MUTED}"/>' for i in range(4))}
  <rect x="-86" y="16" width="170" height="14" rx="7" class="coral"/></g>
{ring(170, 222, 106)}
<path d="M300 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(460 200) rotate(20)"><path d="M-12 0h24v70h-24z" class="goldd o"/>
  <path d="M-40-36h80v38h-80z" class="goldd o"/></g>
<g transform="translate(460 320)"><rect x="-70" y="-14" width="140" height="28" rx="6" class="goldd o"/></g>''', arrow=True)

add('opposed to', 'その案には賛成できないと、手を下ろす', f'''
<g transform="translate(470 190)"><rect x="-90" y="-110" width="180" height="220" rx="8" class="paper"/>
  {''.join(f'<rect x="-66" y="{-80+i*46}" width="{130-(i%2)*40}" height="14" rx="7" fill="{MUTED}"/>' for i in range(4))}</g>
{''.join(f'<g transform="translate({80+i*90} 340)">{person(0, 0, 0.95, 1, c, "blue", "stand", h, "neutral")}</g>'
         for i, (c, h) in enumerate([('coral','short'),('violet','bob'),('gold','bun')]))}
{''.join(f'<path d="M{80+i*90} 260h1" fill="none"/>' for i in range(0))}
{''.join(f'<g transform="translate({80+i*90} 210)"><circle r="26" fill="none" stroke="{CRL}" stroke-width="7"/>'
         f'<path d="M-16 0h32" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/></g>' for i in range(3))}''')

add('on the contrary', '予想と逆に、まるであべこべの結果になる', f'''
{split()}
<g transform="translate(150 200)" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="11 9">
  <path d="M-90 90l60-120 60 120z"/></g>
<g transform="translate(150 200)"><path d="M-90 90h180" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
{ring(150, 200, 128, True)}
<g transform="translate(450 200) scale(1 -1)"><path d="M-90 90l60-120 60 120z" class="coral o"/></g>
<path d="M360 290h180" fill="none" stroke="{MUTED}" stroke-width="4"/>
{ring(450, 200, 128)}''')

add('on the one hand', '一方の手に、まずこちらの言い分を置く', f'''
{hand(180, 250, 1)}
{box(180, 140, 110, 78, 24, 'teal')}
{ring(180, 200, 130)}
<g opacity="0.3">{hand(430, 250, -1)}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="11 9">
  <rect x="380" y="110" width="110" height="70" rx="8"/></g>''')

add('on the same page', 'ふたりの頭に、まったく同じ絵が浮かんでいる', f'''
{head(140, 320, 34, 'teal', 'short')}
{head(460, 320, 34, 'coral', 'bob')}
{''.join(f'<g transform="translate({x} 150)"><ellipse rx="110" ry="76" fill="#fffefd" class="o"/>'
         f'<path d="M-70 40l50-70 36 36 34-46 56 80z" class="greenp o"/>{sun(50, -34, 22)}</g>' for x in [160, 440])}
<circle cx="230" cy="250" r="9" fill="#fffefd" class="o"/>
<circle cx="370" cy="250" r="9" fill="#fffefd" class="o"/>
<path d="M280 210h40" stroke="{INK}" stroke-width="7" stroke-linecap="round" fill="none"/>
<path d="M280 232h40" stroke="{INK}" stroke-width="7" stroke-linecap="round" fill="none"/>''')

add('other than', 'これ一つを除いた、そのほかぜんぶ', f'''
<g transform="translate(300 200)"><rect x="-260" y="-140" width="520" height="280" rx="14" fill="{TONES['teal'][1]}" class="o"/></g>
{''.join(f'<circle cx="{110+ (i%5)*100}" cy="{140+(i//5)*110}" r="34" class="teal o"/>' for i in range(10) if i != 7)}
<g transform="translate(410 250)"><circle r="34" fill="#fffaf1" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g>
{cross(410, 250, 0.9)}''')

add('out of the question', '検討にすら値せず、その場ではねられる', f'''
<g transform="translate(200 190) rotate(-14)"><rect x="-100" y="-120" width="200" height="240" rx="8" class="paper"/>
  {''.join(f'<rect x="-76" y="{-86+i*50}" width="{150-(i%2)*46}" height="14" rx="7" fill="{MUTED}"/>' for i in range(4))}</g>
{cross(200, 190, 2.4)}
<path d="M330 240h100" class="a" stroke="{CRL}" stroke-width="7" marker-end="url(#ar)"/>
<g transform="translate(500 300)"><path d="M-50 0l8-90h84l8 90z" fill="#c3cbd1" class="o"/>
  <path d="M-58-90h116v-16h-116z" fill="#9aa6ae" class="o"/></g>''', arrow=True)

# --- 記号・分ける -------------------------------------------------------------

add('parenthesis', '丸かっこでくくった、なくても通じる部分', f'''
{word(140, 200, 3, 32, INK)}
<g fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round">
  <path d="M240 150q-24 50 0 100"/><path d="M420 150q24 50 0 100"/></g>
{word(330, 200, 4, 28, MUTED)}
{word(520, 200, 2, 32, INK)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9">
  <rect x="230" y="140" width="200" height="120" rx="12"/></g>''')

add('partition', '一つの部屋を、仕切りで二つに分ける', f'''
<g transform="translate(300 200)"><rect x="-260" y="-150" width="520" height="300" rx="10" fill="#f4f7f8" class="o"/></g>
<g transform="translate(300 200)"><rect x="-16" y="-150" width="32" height="300" fill="#c9a06c" class="o"/>
  {''.join(f'<path d="M-16 {-120+i*60}h32" fill="none" stroke="#a8804f" stroke-width="3"/>' for i in range(5))}</g>
{chair(150, 320, 0.8, 'gold', -1)}
{chair(450, 320, 0.8, 'teal', 1)}
{head(150, 230, 24, 'coral', 'short')}
{head(450, 230, 24, 'violet', 'bob')}''')

add('parity', 'どちらも同じ高さで、まったく対等', f'''
<path d="M60 340h480" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<rect x="{130+i*30}" y="{340-h}" width="24" height="{h}" rx="4" class="teal o"/>' for i, h in enumerate([180, 180, 180]))}
{''.join(f'<rect x="{390+i*30}" y="{340-h}" width="24" height="{h}" rx="4" class="coral o"/>' for i, h in enumerate([180, 180, 180]))}
<path d="M270 180h60M270 210h60" stroke="{INK}" stroke-width="9" stroke-linecap="round" fill="none"/>
<path d="M120 140h340" fill="none" stroke="{GRN}" stroke-width="4" stroke-dasharray="10 9"/>''')

add('omission', '並びのなかから、ひとつ抜け落ちている', f'''
{''.join(f'<g transform="translate(300 {110+i*60})"><rect x="-200" y="-22" width="400" height="44" rx="8" class="tealp o"/></g>' for i in [0, 1, 3, 4])}
<g transform="translate(300 290)"><rect x="-200" y="-22" width="400" height="44" rx="8" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/></g>
{ring(300, 290, 0) if False else ''}
<path d="M540 290h-1" fill="none"/>
<g transform="translate(540 290)"><path d="M-14-12l-14 12 14 12" fill="none" stroke="{CRL}" stroke-width="5"/></g>''')

# --- からだ・自然 -------------------------------------------------------------

add('pancreas', '胃のうしろにある、細長い臓器', f'''
{torso(300, 300, 1.0)}
<g transform="translate(300 230)"><path d="M-90 10q30-40 70-30 40 10 100 30-60 30-100 20-40-10-70-20z" class="violet o"/>
  <ellipse cx="-90" cy="10" rx="26" ry="22" class="violet o"/>
  <path d="M-40-6q40 14 90 14" fill="none" stroke="{VIOD}" stroke-width="4"/></g>
{ring(300, 234, 116)}''')

add('ozone', '地球をつつみ、強い光をさえぎる層', f'''
<rect width="600" height="400" fill="#2a3340"/>
<path d="M0 400q300-200 600 0z" fill="{BLU}" stroke="{INK}" stroke-width="3"/>
<path d="M0 330q300-220 600 0" fill="none" stroke="{TEAP}" stroke-width="26" opacity="0.85"/>
<path d="M0 330q300-220 600 0" fill="none" stroke="{TEA}" stroke-width="4"/>
{''.join(f'<path d="M{80+i*90} 40l{-20+i*8} 130" class="a" stroke="{GLD}" stroke-width="6" marker-end="url(#ar)"/>' for i in range(5))}
{''.join(f'<path d="M{130+i*110} 210l{-14+i*8} -40" fill="none" stroke="{GLD}" stroke-width="6" stroke-dasharray="8 7"/>' for i in range(4))}''', arrow=True)

add('pasture', 'さくで囲われた、家畜が草を食む野', f'''
<path d="M0 240q140-20 300-14t300 14v160H0z" class="greenp o"/>
{''.join(f'<path d="M{40+i*70} 250v90" fill="none" stroke="{GLDD}" stroke-width="8"/>' for i in range(9))}
<path d="M40 270h520M40 310h520" fill="none" stroke="{GLDD}" stroke-width="7"/>
<g transform="translate(200 370) scale(0.5)">{beast(0, 0, 1, '#e8e2d4', 1)}</g>
<g transform="translate(430 380) scale(0.42)">{beast(0, 0, 1, '#c9a06c', -1)}</g>
{''.join(f'<path d="M{70+i*60} 390v-16" fill="none" stroke="{GRND}" stroke-width="4"/>' for i in range(9))}''')

add('orchid', '大きく張り出した唇弁をもつ花', f'''
{table(340)}
<g transform="translate(300 306)"><path d="M-50 0l8-60h84l8 60z" class="teald o"/>
  <path d="M-54-60h108v-14h-108z" class="teal o"/>
  <path d="M0-74v-160" fill="none" stroke="{GRND}" stroke-width="7"/></g>
<g transform="translate(300 150)">
  {''.join(f'<ellipse cx="0" cy="-46" rx="18" ry="44" class="violetp o" transform="rotate({d} 0 0)"/>' for d in [0, 72, 144, 216, 288])}
  <path d="M-40 26q40-40 80 0 6 50-40 60-46-10-40-60z" class="violet o"/>
  <circle r="14" class="goldp o"/></g>''')

add('otter', 'あお向けに水に浮かぶ、カワウソ', f'''
<path d="M0 220h600v180H0z" fill="{BLUP}"/>
<path d="M0 220h600" fill="none" stroke="{BLU}" stroke-width="4"/>
<g transform="translate(300 260)">
  <ellipse rx="140" ry="50" fill="#8a6a48" class="o"/>
  <circle cx="-140" cy="-24" r="42" fill="#8a6a48" class="o"/>
  <circle cx="-166" cy="-52" r="14" fill="#8a6a48" class="o"/><circle cx="-118" cy="-56" r="14" fill="#8a6a48" class="o"/>
  <circle cx="-154" cy="-28" r="5" class="ink"/><circle cx="-126" cy="-28" r="5" class="ink"/>
  <ellipse cx="-140" cy="-10" rx="14" ry="10" fill="#5f4630"/>
  <path d="M-60-40q26-30 50 0M20-44q26-30 50 0" fill="none" stroke="#8a6a48" stroke-width="14" stroke-linecap="round"/>
  <path d="M140 10q60 10 90-30" fill="none" stroke="#8a6a48" stroke-width="22" stroke-linecap="round"/></g>
{''.join(f'<path d="M{80+i*120} {330+(i%2)*20}h60" fill="none" stroke="#ffffff" stroke-width="4" opacity="0.7"/>' for i in range(4))}''')

add('parsley', 'こまかく縮れた、飾りにも使う緑の葉', f'''
{table(340)}
<g transform="translate(300 306)">
  {''.join(f'<path d="M0 0Q{-70+i*35} -60 {-90+i*45} -{110+ (i%3)*30}" fill="none" stroke="{GRND}" stroke-width="6"/>' for i in range(5))}
  {''.join(f'<g transform="translate({-90+i*45} -{110+ (i%3)*30})">'
           + ''.join(f'<circle cx="{-20+ (j%3)*20}" cy="{-14+(j//3)*18}" r="13" class="{"green" if (i+j)%2 else "greenp"} o"/>' for j in range(6))
           + '</g>' for i in range(5))}</g>''')

add('palette', '絵の具を出して混ぜる、画家の板', f'''
{table(340)}
<g transform="translate(280 250) rotate(-10)">
  <path d="M-150 0q0-90 150-90t150 90q0 70-90 70-30 0-30 24t-30 24Q-150 118-150 0z" fill="#c9a06c" class="o"/>
  <circle cx="60" cy="26" r="26" fill="#fffaf1" class="o"/>
  {''.join(f'<circle cx="{-110+ (i%4)*46}" cy="{-40+(i//4)*44}" r="20" class="{c} o"/>' for i, c in enumerate(['coral','gold','green','blue','violet','teal','coralp','goldp']))}</g>
<g transform="translate(470 150) rotate(30)"><path d="M-8-90h16v110l-8 20-8-20z" class="coral o"/></g>''')

# --- 家族・見方 ---------------------------------------------------------------

add('parenthood', '親という立場になること', f'''
{person(220, 306, 1.3, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
{person(380, 306, 0.66, 1, 'coral', 'green', 'reach', 'bob', 'smile')}
<path d="M290 216l50 20" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(220 130)"><path d="M-70-40h140v70l-70 30-70-30z" class="goldp o"/>
  <path d="M-30-10h60M0-30v50" fill="none" stroke="{GLDD}" stroke-width="7"/></g>
{ring(220, 210, 130)}''')

add('parenting', '食べさせ、教え、いっしょに遊ぶ日々', f'''
{''.join(f'<g transform="translate({110+i*190} 200)"><rect x="-86" y="-110" width="172" height="220" rx="10" class="paper"/></g>' for i in range(3))}
<g transform="translate(110 230)">{head(0, -20, 22, 'teal', 'bun')}{head(40, 20, 16, 'coral', 'bob')}
  <path d="M14-6l20 14" fill="none" stroke="{SKIN}" stroke-width="8" stroke-linecap="round"/>
  <ellipse cx="46" cy="46" rx="26" ry="8" fill="#fffefd" class="o"/></g>
<g transform="translate(300 230)">{head(-30, -20, 22, 'teal', 'bun')}{head(30, 10, 16, 'coral', 'bob')}
  <rect x="-20" y="30" width="60" height="40" rx="4" class="paper"/></g>
<g transform="translate(490 230)">{head(-30, -10, 22, 'teal', 'bun')}{head(30, 10, 16, 'coral', 'bob')}
  <circle cx="0" cy="60" r="18" class="coral o"/></g>''')

add('paradigm', 'ばらばらのものを、ひとつの枠組みで並べ直す', f'''
{''.join(f'<circle cx="{-20+ (i%3)*0}" cy="0" r="0"/>' for i in range(0))}
{''.join(f'<circle cx="{80+ (i%4)*40+(i%3)*10}" cy="{120+(i//4)*60+(i%2)*20}" r="18" class="tealp o"/>' for i in range(9))}
<g transform="translate(300 200)"><rect x="-40" y="-140" width="80" height="280" rx="10" fill="none" stroke="{VIO}" stroke-width="8"/></g>
{''.join(f'<g transform="translate({400+ (i%3)*70} {130+(i//3)*70})"><circle r="24" class="teal o"/></g>' for i in range(9))}
<path d="M240 340h130" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('panorama', '高いところから、左右いっぱいに見わたす', f'''
<g transform="translate(300 190)"><rect x="-280" y="-70" width="560" height="140" rx="6" fill="#eaf4fb" class="o"/>
  <path d="M-280 70l90-90 70 60 60-80 80 70 70-60 90 100z" fill="#c3cbd1" class="o"/>
  <path d="M-280 70q140-30 280 0t280 0v0h-560z" class="greenp o"/>
  {sun(-180, -34, 22)}
  {''.join(f'<g transform="translate({-160+i*90} 40) scale(0.16)">{house(0, 0, 1, "coral")}</g>' for i in range(5))}</g>
{person(300, 380, 1.0, 1, 'teal', 'blue', 'up', 'cap', 'smile')}
<path d="M40 300h520" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('omen', '黒い鳥が現れ、そのあと嵐が来る', f'''
<g transform="translate(150 160)"><path d="M-34 0q-14-26 8-34 20-8 30 10 22-4 26 12-4 16-30 18-26 2-34-6z" fill="{INK}"/>
  <path d="M-34-4l-18-6 18-10z" fill="{INK}"/><circle cx="10" cy="-16" r="3" fill="#fffdf6"/>
  <path d="M-6-6q26-24 44-2-22 14-44 2z" fill="{INK}"/></g>
<path d="M240 200h60" class="a" marker-end="url(#ar)"/>
{cloud(440, 130, 1.8, 'violet')}
<path d="M440 190l-26 50h34l-30 60 76-84h-36l26-34z" class="gold o"/>
{''.join(f'<path d="M{370+i*40} {230+(i%2)*20}l-14 40" fill="none" stroke="{BLU}" stroke-width="5"/>' for i in range(5))}''', arrow=True)

add('ounce', 'ごくわずかな重さの単位', f'''
<g transform="translate(300 260)"><path d="M-160 60v-30h320v30z" class="goldd o"/>
  <path d="M-120 30v-40h240v40z" fill="#dfe6ea" class="o"/>
  <path d="M-40-10q0-40 40-40t40 40z" fill="#c3ccd2" class="o"/>
  <ellipse cx="0" cy="-52" rx="80" ry="16" fill="#eef2f4" class="o"/></g>
<g transform="translate(300 180)"><path d="M-24 20q0-34 24-34t24 34z" fill="#8d949a" class="o"/>
  <path d="M-10-14q0-14 10-14t10 14" fill="none" stroke="{INK}" stroke-width="5"/></g>
{ring(300, 190, 66)}
<path d="M120 120h100" class="a" marker-end="url(#ar)"/>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
