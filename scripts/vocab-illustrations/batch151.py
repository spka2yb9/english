# -*- coding: utf-8 -*-
"""第151回。t- の形容詞と un- の否定形容詞。un- は「あるはずのものを破線で消す」で描く。"""
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

def scale(x, y, tilt=0, s=1):
    """てんびん。tilt が正だと右が下がる。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-70" fill="none" stroke="{INK}" stroke-width="7"/><circle cy="-76" r="9" class="ink"/>'
            f'<path d="M-190 0h380" fill="none" stroke="{INK}" stroke-width="7" transform="translate(0 -76) rotate({tilt})"/>'
            f'<path d="M-40 0h80v14h-80z" class="ink" transform="translate(0 0)"/></g>')

def clock(x, y, s=1, h=2, m=0):
    ah = math.radians(h*30 + m*0.5 - 90); am = math.radians(m*6 - 90)
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="54" fill="#fffefd" class="o"/>'
            f'<path d="M0 0l{42*math.cos(am):.0f} {42*math.sin(am):.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M0 0l{28*math.cos(ah):.0f} {28*math.sin(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle r="4" class="ink"/></g>')

def sign(x, y, dirs, s=1):
    """道しるべ。dirs は (向き, 色) の並び。向き 1 で右、-1 で左。"""
    arms = ''
    for i, (d, c) in enumerate(dirs):
        yy = -160 + i*56
        arms += (f'<path d="M0 {yy}h{110*d}l{26*d} 26-{26*d} 26H0z" class="{c} o"/>' if d > 0
                 else f'<path d="M0 {yy}h{110*d}l{26*d} 26-{26*d} 26H0z" class="{c} o"/>')
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M-8 0v-190h16V0z" class="goldd o"/>{arms}</g>'

# --- t- ----------------------------------------------------------------------

add('tireless', 'まわりが休んでも、手を止めずに働きつづける', f'''
{table(330)}
{person(200, 306, 1.2, 1, 'teal', 'blue', 'carry', 'cap', 'smile')}
<g transform="translate(214 216)"><path d="M-40-26h80v52h-80z" class="gold o"/></g>
<g opacity="0.4">{sit(430, 340, 1.0, 1, 'coral', 'blue', 'bob', 'sad', 'down')}{chair(444, 340, 0.92, 'gold', -1)}</g>
{clock(110, 100, 0.7, 2, 0)}
{clock(300, 100, 0.7, 8, 0)}
<path d="M162 100h74" fill="none" class="a" marker-end="url(#ar)"/>
{''.join(spark(x, y, 0.8) for x, y in [(400,110),(520,150)])}''', arrow=True)

add('tolerant', 'かたちのちがうものも、そのまま輪に入れる', f'''
<circle cx="290" cy="210" r="150" fill="none" stroke="{TEA}" stroke-width="6"/>
{''.join(f'<circle cx="{x}" cy="{y}" r="30" class="teal o"/>' for x, y in [(220,150),(300,140),(360,210),(240,270)])}
<path d="M330 270l-34 56h68z" class="coral o"/>
<rect x="316" y="176" width="56" height="56" rx="8" class="gold o"/>
{person(520, 306, 1.1, -1, 'violet', 'blue', 'give', 'bun', 'smile')}
<path d="M470 210h-40" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('toothless', '歯がそろった口と、一本もない口の対比', f'''
{split()}
<g transform="translate(150 200)"><ellipse rx="110" ry="80" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60 0q60-50 120 0-60 60-120 0z" fill="#7a2f28" class="o"/>
  {''.join(f'<rect x="{-52+i*20}" y="-14" width="16" height="22" rx="3" fill="#fffefd" stroke="{INK}" stroke-width="2"/>' for i in range(6))}</g>
{ring(150, 200, 132, True)}
<g transform="translate(450 200)"><ellipse rx="110" ry="80" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60 0q60-50 120 0-60 60-120 0z" fill="#7a2f28" class="o"/>
  {''.join(f'<rect x="{-52+i*20}" y="-14" width="16" height="22" rx="3" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="5 5"/>' for i in range(6))}</g>
{ring(450, 200, 132)}''')

add('topical', '今日の新聞に出たばかりの話題で、みなが盛り上がる', f'''
{doc(180, 190, 220, 270, 0)}
<path d="M80 110h200" fill="none" stroke="{INK}" stroke-width="4"/>
{word(180, 140, 4, 40, CRL)}
{''.join(f'<rect x="{86+ (i%2)*104}" y="{200+(i//2)*36}" width="88" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}
<g transform="translate(226 96)"><rect x="-40" y="-22" width="80" height="34" rx="8" class="coral o"/></g>
{head(400, 240, 28, 'teal', 'short')}{head(500, 280, 28, 'violet', 'bob')}
<g transform="translate(470 130)"><rect x="-70" y="-40" width="140" height="80" rx="18" class="paper"/>
  <path d="M-50 36l-24 30 4-30z" class="paper"/>{word(0, 0, 3, 26, TEA)}</g>''')

add('tranquil', '風のない林の道に、やわらかい光が差す', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<path d="M240 400q30-120 60-140 30 20 60 140z" fill="#e0d3b8" class="o"/>
{''.join(tree(x, 320, s) for x, s in [(80,1.1),(170,0.9),(470,1.15),(550,0.85)])}
{''.join(f'<path d="M{160+i*70} 40l60 240" fill="#fff6d8" opacity="0.55" stroke="none"/>' for i in range(4))}
{''.join(f'<path d="M{60+i*90} {350+(i%2)*20}h50" fill="none" stroke="{GRND}" stroke-width="3"/>' for i in range(6))}''')

add('transatlantic', '大西洋をまたいで、両側の大陸を結ぶ', f'''
<path d="M0 0h600v400H0z" fill="{BLUP}"/>
<path d="M-20 60q80 40 60 120t20 180h-60z" class="greenp o"/>
<path d="M120 90q60 20 40 90t-60 60-40-70 60-80z" class="greenp o"/>
<path d="M620 40q-90 60-60 160t40 200h20z" class="greenp o"/>
<path d="M470 120q80-30 100 40t-70 90-80-40 50-90z" class="greenp o"/>
<path d="M120 250q180-160 360-70" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="14 12"/>
<g transform="translate(300 130)">{plane(0, 0, 0.55, 14, 'coral')}</g>''')

add('transient', 'ふっと現れて、すぐ消えてしまう', f'''
{''.join(f'<circle cx="{130+i*170}" cy="200" r="{70}" fill="none" stroke="{BLU}" stroke-width="{7-i*2}" opacity="{1-i*0.3:.1f}" '
         f'{"" if i == 0 else chr(115)+chr(116)+chr(114)+chr(111)+chr(107)+chr(101)+"-dasharray="+chr(34)+str(14-i*3)+" "+str(10+i*4)+chr(34)}/>' for i in range(3))}
<circle cx="130" cy="176" r="18" fill="#ffffff" opacity="0.7"/>
{''.join(f'<path d="M{222+i*170} 200h40" class="a" marker-end="url(#ar)"/>' for i in range(2))}
{''.join(spark(x, y, 0.7) for x, y in [(470,140),(510,240)])}
{table(330)}''', arrow=True)

add('transitional', '前のかたちから次のかたちへ、途中の段階をはさむ', f'''
<rect x="60" y="150" width="120" height="120" rx="8" class="teal o"/>
<path d="M300 150h120v120h-120z" class="teal o" transform="rotate(0 360 210)"/>
<path d="M300 210a60 60 0 0 1 120 0 60 60 0 0 1-120 0z" fill="none"/>
<path d="M420 210a60 60 0 0 0-120 0z" fill="none"/>
<g><path d="M300 178q60-40 120 0v64q-60 40-120 0z" class="tealp o"/></g>
<circle cx="520" cy="210" r="60" class="teal o"/>
<path d="M200 210h80M440 210h20" class="a" marker-end="url(#ar)"/>
{ring(360, 210, 92, True)}''', arrow=True)

add('traumatic', '受けた傷が、あとあとまで心に残る', f'''
{head(180, 250, 46, 'teal', 'short')}
<path d="M158 262q22 12 44 0" fill="none" stroke="{INK}" stroke-width="3"/>
<circle cx="250" cy="180" r="9" fill="#fffefd" class="o"/>
<circle cx="276" cy="148" r="13" fill="#fffefd" class="o"/>
<g transform="translate(420 140)"><ellipse rx="130" ry="90" fill="#fffefd" class="o"/>
  <g opacity="0.85">{cloud(-40, -20, 1.1, 'violet')}</g>
  <path d="M20 20l-24 44h30l-26 50 66-70h-32l22-30z" class="gold o"/>
  {person(-20, 60, 0.45, 1, 'coral', 'blue', 'up', 'short', 'sad')}</g>
<g transform="translate(180 320)"><path d="M0 22q-40-30-40-56 0-20 20-20 12 0 20 12 8-12 20-12 20 0 20 20 0 26-40 56z" class="coralp o"/>
  <path d="M0-40l-14 30 20 8-14 26" fill="none" stroke="{CRLD}" stroke-width="4"/></g>''')

add('turbulent', '荒れた海に、小さな船がもまれる', f'''
<path d="M0 200q60-60 120 0t120 0 120 0 120 0 120 0v200H0z" fill="{BLU}" class="o"/>
<path d="M0 250q60-60 120 0t120 0 120 0 120 0 120 0" fill="none" stroke="#fffefd" stroke-width="6" opacity="0.5"/>
<g transform="translate(300 210) rotate(-18)"><path d="M-70 0h140l-24 40h-92z" class="coral o"/>
  <path d="M0 0v-80" fill="none" stroke="{GLDD}" stroke-width="7"/>
  <path d="M0-80l44 30-44 20z" fill="#fffefd" class="o"/></g>
{cloud(140, 80, 1.5, 'violet')}{cloud(430, 70, 1.7, 'violet')}
{''.join(f'<path d="M{100+i*70} {150+(i%3)*16}v26" fill="none" stroke="{BLUD}" stroke-width="5"/>' for i in range(7))}''')

add('typical of', 'その仲間らしい特徴を、そのまま全部そなえている', f'''
{''.join(f'<g transform="translate({110+ (i%3)*90} {130+(i//3)*100})"><circle r="38" class="tealp o"/>'
         f'<path d="M-16-8h32M-10 12h20" fill="none" stroke="{TEAD}" stroke-width="5"/></g>' for i in range(6))}
<g transform="translate(470 200)"><circle r="70" class="teal o"/>
  <path d="M-30-16h60M-20 22h40" fill="none" stroke="#fffefd" stroke-width="8"/></g>
{ring(470, 200, 96)}
<path d="M340 200h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('ubiquitous', '町のどの角にも、同じ店がある', f'''
<g transform="translate(300 200)"><rect x="-260" y="-160" width="520" height="320" rx="12" fill="#f2f5f6" class="o"/>
  <path d="M-260-40h520M-260 60h520M-100-160v320M100-160v320" fill="none" stroke="#ffffff" stroke-width="16"/>
  <path d="M-260-40h520M-260 60h520M-100-160v320M100-160v320" fill="none" stroke="{MUTED}" stroke-width="2"/></g>
{''.join(f'<g transform="translate({x} {y})"><rect x="-30" y="-26" width="60" height="52" rx="5" fill="#fffefd" class="o"/>'
         f'<path d="M-34-26h68l-12-20h-44z" class="coral o"/></g>' for x, y in
         [(120,110),(320,110),(500,110),(120,210),(320,210),(500,210),(120,310),(320,310),(500,310)])}''')

# --- un- --------------------------------------------------------------------

add('unambiguous', '二方向に読める案内と、一方向だけの案内の対比', f'''
{split()}
{sign(150, 330, [(1, 'gold'), (-1, 'gold')], 0.8)}
{ring(150, 210, 130, True)}
{sign(450, 330, [(1, 'coral')], 0.8)}
{ring(450, 210, 130)}''')

add('unequivocal', 'ぼかした返事と、はっきりした返事の対比', f'''
{split()}
<g transform="translate(150 190)"><rect x="-100" y="-60" width="200" height="120" rx="24" class="paper"/>
  <path d="M-80 50l-24 30 6-30z" class="paper"/>
  <path d="M-60 0q20-24 40 0t40 0" fill="none" stroke="{MUTED}" stroke-width="7"/></g>
{ring(150, 200, 128, True)}
<g transform="translate(450 190)"><rect x="-100" y="-60" width="200" height="120" rx="24" class="paper"/>
  <path d="M-80 50l-24 30 6-30z" class="paper"/>
  <path d="M-56 0h112" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round"/></g>
{ring(450, 200, 128)}''')

add('unanimous', 'その場の全員が、同じほうに手を上げる', f'''
{''.join(f'<g transform="translate({100+ (i%4)*120} {230+(i//4)*130})">{person(0, 0, 0.86, 1, c, "blue", "up", h, "smile")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun'),
                                     ('violet','short'),('blue','cap'),('teal','bob'),('coral','short')]))}''')

add('unassuming', '飾りたてる人たちのなかで、ひとりだけ控えめ', f'''
{split()}
{person(150, 306, 1.15, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{ring(150, 210, 122)}
{person(400, 306, 1.15, 1, 'violet', 'gold', 'up', 'bun', 'smile')}
{person(510, 306, 1.1, 1, 'coral', 'gold', 'up', 'cap', 'smile')}
{''.join(spark(x, y, 0.9) for x, y in [(360,130),(470,110),(560,150)])}''')

add('unattended', '荷物だけが置かれ、持ち主がいない', f'''
<g transform="translate(300 306)"><path d="M-190-24h380v24h-380z" class="goldd o"/>
  <path d="M-160 0v70M160 0v70M-190-24v-70h380v70" fill="none" stroke="{GLDD}" stroke-width="10"/></g>
<g transform="translate(240 274)"><path d="M-46 24v-70h92v70z" class="violet o"/>
  <path d="M-20-46v-16h40v16" fill="none" class="a"/></g>
<g opacity="0.5">{person(420, 306, 1.0, 1, 'coral', 'blue', 'stand', 'bob', 'neutral')}</g>
<rect x="352" y="140" width="136" height="180" rx="12" fill="#fffaf1" opacity="0.85"/>
<rect x="352" y="140" width="136" height="180" rx="12" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>''')

add('unauthorised', '通行証を持たないまま、柵の中に入りこむ', f'''
<path d="M300 90v250" fill="none" stroke="{GLDD}" stroke-width="12"/>
{''.join(f'<path d="M{330+i*66} 150v190" fill="none" stroke="{GLDD}" stroke-width="10"/>' for i in range(4))}
<path d="M300 150h250" fill="none" stroke="{GLDD}" stroke-width="10"/>
{person(370, 340, 1.05, 1, 'coral', 'blue', 'walk', 'short', 'neutral')}
<g transform="translate(140 200)"><rect x="-56" y="-40" width="112" height="80" rx="8" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/>
  <circle cx="-22" cy="-10" r="14" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6"/>
  <path d="M4-14h40M-40 20h80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="7 6"/></g>
<path d="M210 240l80 60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('unavoidable', '両側が壁で、その道しか通れない', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<path d="M60 306v-230h60v230zM480 306v-230h60v230z" fill="#c3cbd1" class="o"/>
<path d="M120 340h360" fill="none" stroke="{GLDD}" stroke-width="10" stroke-dasharray="22 16"/>
{person(200 , 380, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'neutral')}
<path d="M300 240h140" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8">
  <path d="M240 160v-70M360 160v-70"/></g>''', arrow=True)

add('unaware', 'すぐうしろで起きていることに、まったく気づかない', f'''
{person(200, 306, 1.25, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
<g transform="translate(440 250)"><path d="M-70 56V-40q0-24 24-24h92q24 0 24 24v96z" class="corald o"/>
  <path d="M-46-24h92v50h-92z" class="coralp o"/></g>
{''.join(f'<path d="M{380-i*20} {160-i*20}l16 16" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(3))}
<path d="M270 200h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<path d="M338 200l-10-10 10-10" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('unbeaten', '並んだ結果が、ぜんぶ勝ち', f'''
{''.join(f'<g transform="translate({100+ (i%5)*100} {160+(i//5)*120})"><circle r="42" class="greenp o"/>'
         f'<path d="M-20 2l14 16 28-32" fill="none" stroke="{GRN}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>' for i in range(10))}''')

add('unbiased', 'どちらにもかたよらず、水平に釣り合う', f'''
{scale(300, 250, 0, 1)}
<path d="M110 174v40" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M490 174v40" fill="none" stroke="{INK}" stroke-width="4"/>
{box(110, 250, 90, 60, 18, 'teal')}
{box(490, 250, 90, 60, 18, 'coral')}
<path d="M60 174h480" fill="none" stroke="{GRN}" stroke-width="0"/>
<path d="M180 120h240" fill="none" stroke="{GRN}" stroke-width="4" stroke-dasharray="10 8"/>''')

add('unjust', '同じだけ働いたのに、返ってくるものがまるでちがう', f'''
{person(130, 306, 1.05, 1, 'teal', 'blue', 'carry', 'short', 'neutral')}
{person(400, 306, 1.05, 1, 'coral', 'blue', 'carry', 'bob', 'sad')}
{box(144, 216, 80, 52, 16, 'gold')}
{box(414, 216, 80, 52, 16, 'gold')}
<path d="M200 130h40M470 130h40" class="a" marker-end="url(#ar)"/>
{''.join(coin(268 + i*36, 120, 20) for i in range(3))}
{coin(546, 120, 20)}
{scale(300, 380, 0, 0)}''', arrow=True)

add('uncanny', '見分けがつかないほどそっくりで、少し不気味', f'''
{person(190, 306, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
{person(410, 306, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
<g fill="none" stroke="{VIO}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M300 90v240"/></g>
{''.join(f'<path d="M{120-i*0} {150+i*40}q-20 20 0 40" fill="none" stroke="{VIO}" stroke-width="4"/>' for i in range(3))}
{''.join(f'<path d="M480 {150+i*40}q20 20 0 40" fill="none" stroke="{VIO}" stroke-width="4"/>' for i in range(3))}''')

add('uncommon', 'ほとんど見かけず、めったに出てこない', f'''
<path d="M60 330h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
{''.join(f'<rect x="{90+i*100}" y="{330-h}" width="60" height="{h}" rx="6" class="tealp o"/>' for i, h in enumerate([180, 150, 200, 170]))}
<rect x="490" y="308" width="60" height="22" rx="6" class="coral o"/>
{ring(520, 300, 62)}''')

add('unconvincing', 'すじの通らない話に、聞き手が納得しない', f'''
{person(140, 306, 1.15, 1, 'violet', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(320 200)">
  <rect x="-90" y="30" width="180" height="34" rx="6" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9">
    <rect x="-70" y="-20" width="140" height="34" rx="6"/><rect x="-50" y="-70" width="100" height="34" rx="6"/></g>
  <path d="M-70 14h-30M70 14h30" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{person(500, 306, 1.15, -1, 'teal', 'blue', 'hold', 'bob', 'sad')}
<path d="M540 190q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('undecided', '二つの道の前で、どちらとも決められない', f'''
{sign(300, 306, [(1, 'teal'), (-1, 'coral')], 0.9)}
{person(300, 400, 1.0, 1, 'gold', 'blue', 'think', 'short', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8">
  <path d="M250 250l-100 40"/><path d="M350 250l100 40"/></g>
<g transform="translate(160 130)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''')

add('undeniable', '目の前の証拠が大きすぎて、否定のしようがない', f'''
{table(340)}
<g transform="translate(230 250)"><ellipse rx="150" ry="86" fill="#e8e2d4" class="o"/>
  <ellipse cx="-30" cy="-16" rx="60" ry="44" fill="#b8ae98"/>
  {''.join(f'<ellipse cx="{40+ (i%3)*34}" cy="{-40+(i//3)*40}" rx="18" ry="14" fill="#b8ae98"/>' for i in range(5))}</g>
{person(490, 306, 1.15, -1, 'coral', 'blue', 'reach', 'short', 'surprised')}
<path d="M420 200h-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('underpaid', '仕事の山に対して、返ってくるのはコイン一枚', f'''
{table(330)}
{''.join(f'<g transform="translate({190+ (i%2)*10} {300-i*40}) rotate({-4+i*3})"><rect x="-90" y="-18" width="180" height="36" rx="4" class="paper"/>'
         f'<rect x="-70" y="-8" width="120" height="10" rx="5" fill="{MUTED}"/></g>' for i in range(6))}
{scale(0, 0, 0, 0)}
{coin(470, 280, 26)}
<path d="M330 180h80" class="a" marker-end="url(#ar)"/>
{head(520, 190, 26, 'coral', 'short')}
<path d="M550 152q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>''', arrow=True)

add('underrated', 'ほんとうの値打ちより、ずっと低い点しかつかない', f'''
<g transform="translate(200 220)"><path d="M-90 130V-100l90-60 90 60v230z" class="violetp o"/>
  {''.join(spark(x, y, 0.9) for x, y in [(-40,-60),(40,-30),(0,40)])}</g>
<path d="M330 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(480 210)"><rect x="-80" y="-70" width="160" height="140" rx="10" class="paper"/>
  {''.join(f'<path d="M{-60+i*30} 20l6 14 14 6-14 6-6 14-6-14-14-6 14-6z" fill="{"#d9dfe3" if i else GLD}"/>' for i in range(5))}
  <rect x="-56" y="-44" width="112" height="14" rx="7" fill="{MUTED}"/></g>
<path d="M480 300v40" fill="none" stroke="{CRL}" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('underway', '始まってはいるが、まだ途中', f'''
<g transform="translate(300 200)"><rect x="-230" y="-34" width="460" height="68" rx="34" fill="#fffefd" class="o"/>
  <path d="M-226 0a30 30 0 0 1 30-30h190v60h-190a30 30 0 0 1-30-30z" class="teal"/>
  <path d="M-6-30h20v60h-20z" class="tealp"/></g>
<path d="M20 200h-1" fill="none"/>
<g transform="translate(300 320)"><path d="M-120 0h240" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-120-10v20M120-10v20" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
{''.join(f'<path d="M{60+i*36} 110v-24" fill="none" stroke="{TEA}" stroke-width="4"/>' for i in range(6))}
<path d="M60 110h480" fill="none" stroke="{MUTED}" stroke-width="0"/>
<g transform="translate(430 100)"><path d="M-30 0h60" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/></g>''', arrow=True)

add('undesirable', '出されたものを、こちらへ来るなと押し返す', f'''
{table(300)}
<g transform="translate(400 268)"><ellipse rx="76" ry="20" fill="#fffefd" class="o"/>
  <ellipse cy="-12" rx="42" ry="20" fill="#8f9a72" class="o"/>
  {''.join(f'<path d="M{372+i*24} 220q-14-20 0-40" fill="none" stroke="{GRN}" stroke-width="4" transform="translate(-400 -268)"/>' for i in range(2))}</g>
{person(180, 306, 1.2, 1, 'teal', 'blue', 'reach', 'bob', 'sad')}
{hand(280, 230, 1)}
<path d="M330 230h50" fill="none" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('undue', '小さなくぎに、大きすぎるハンマーを振り下ろす', f'''
{table(340)}
<g transform="translate(320 306)"><path d="M-6-40h12v40h-12z" class="ink"/><path d="M-16-40h32v10h-32z" class="ink"/></g>
<g transform="translate(280 150) rotate(-24)"><path d="M-14 0h28v190h-28z" class="goldd o"/>
  <path d="M-90-70h180v76h-180z" fill="#5b6b78" class="o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M480 200h40M470 260h40"/></g>
{head(520, 330, 24, 'teal', 'short')}''')

add('uneasy', 'はっきりしないまま、そわそわして落ち着かない', f'''
{sit(280, 330, 1.25, 1, 'teal', 'blue', 'short', 'sad', 'lap')}
{chair(294, 330, 1.15, 'gold', -1)}
<g transform="translate(280 200)"><path d="M-30 0a30 30 0 1 1 24 48" fill="none" stroke="{VIO}" stroke-width="5" stroke-dasharray="8 7"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M150 190q16-20 0-40M420 200q-16-20 0-40M130 260h-30M450 260h30"/></g>
<g transform="translate(520 140)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''')

add('uneven', 'たいらな面と、でこぼこした面の対比', f'''
{split()}
<path d="M40 240h220v70H40z" class="goldp o"/>
<path d="M40 240h220" fill="none" stroke="{INK}" stroke-width="4"/>
{ring(150, 240, 122, True)}
<path d="M340 310v-40l30-26 34 34 40-50 30 40 46-30v72z" class="goldp o"/>
<path d="M340 270l30-26 34 34 40-50 30 40 46-30" fill="none" stroke="{INK}" stroke-width="4"/>
{ring(450, 240, 122)}''')

add('unforeseen', '思い描いた道すじに、想定外のことが割りこむ', f'''
<path d="M60 240h480" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 10"/>
{''.join(f'<circle cx="{110+i*100}" cy="240" r="14" class="tealp o"/>' for i in range(3))}
<g transform="translate(400 240)">
  <g class="corals" stroke-width="7">{''.join(f'<path d="M0 -50v-30" transform="rotate({d})"/>' for d in range(0, 360, 45))}</g>
  <path d="M0-46l14 30 32 4-24 24 6 32-28-16-28 16 6-32-24-24 32-4z" class="coral o"/></g>
{head(150, 330, 24, 'teal', 'short')}
<path d="M186 316l180-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('ungrateful', '助けてもらったのに、礼も言わず立ち去る', f'''
{person(160, 306, 1.15, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
{box(280, 230, 76, 54, 16, 'gold')}
{person(450, 306, 1.15, 1, 'coral', 'blue', 'walk', 'short', 'neutral')}
<path d="M340 190h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(400 120)"><rect x="-60" y="-36" width="120" height="72" rx="16" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/>
  <path d="M-40 30l-20 26 4-26z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/></g>''', arrow=True)

add('unilateral', '相手に相談せず、片方だけで決めて署名する', f'''
{table(280)}
{doc(200, 200, 170, 210, 4)}
<g transform="translate(270 150) rotate(30)"><path d="M-7-80h14v110l-7 18-7-18z" class="coral o"/></g>
{person(120, 306, 1.15, 1, 'violet', 'blue', 'reach', 'short', 'neutral')}
<g opacity="0.4">{person(470, 306, 1.15, -1, 'teal', 'blue', 'stand', 'bob', 'neutral')}</g>
<path d="M330 200h80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<path d="M420 200l-12-10M420 200l-12 10" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M300 110h-140" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('uninterested', '話をされても、よそを向いてあくびをする', f'''
{person(160, 306, 1.2, 1, 'violet', 'blue', 'point', 'bun', 'neutral')}
<g transform="translate(300 160)"><rect x="-70" y="-40" width="140" height="80" rx="16" class="paper"/>
  <path d="M-50 36l-24 30 4-30z" class="paper"/>{word(0, 0, 4, 26, MUTED)}</g>
{person(470, 306, 1.2, -1, 'teal', 'blue', 'hold', 'short', 'neutral')}
<ellipse cx="470" cy="212" rx="11" ry="15" fill="{INK}"/>
<path d="M446 186l12 6M494 186l-12 6" fill="none" stroke="{INK}" stroke-width="3"/>
<path d="M520 170q16-16 6-34" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('unofficial', '判のある正式な文書と、手書きのただのメモの対比', f'''
{split()}
{doc(150, 200, 180, 230, 4)}
<circle cx="200" cy="270" r="34" fill="none" stroke="{CRL}" stroke-width="6"/>
{ring(150, 200, 132, True)}
<g transform="translate(450 200) rotate(-6)"><rect x="-90" y="-110" width="180" height="220" rx="4" fill="#fdf6d8" class="o"/>
  {''.join(f'<path d="M-64 {-70+i*44}q40-14 70 4t56-6" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(4))}</g>
{ring(450, 200, 132)}''')

add('unpaid', '請求書の支払い欄が、期限を過ぎても空のまま', f'''
{doc(280, 200, 260, 290, 0)}
{''.join(f'<rect x="180" y="{110+i*44}" width="{180-(i%2)*60}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}
<path d="M170 250h220" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(340 290)"><rect x="-60" y="-26" width="120" height="52" rx="6" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/></g>
<g transform="translate(180 292)">{coin(0, 0, 22)}</g>
<path d="M212 292h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<g transform="translate(500 130)"><path d="M-40 0v-70h80V0z" class="teald o"/>
  <path d="M-30 0v-60h60V0z" fill="#fffefd" class="o"/>
  <path d="M-30-30h60" fill="none" stroke="{CRL}" stroke-width="6"/></g>''')

add('unparalleled', '後続がはるか後ろで、並ぶものがない', f'''
<path d="M0 340h600v14H0z" class="goldd o"/>
{person(470, 340, 1.25, 1, 'coral', 'blue', 'walk', 'cap', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M370 200h-60M356 260h-70"/></g>
<g opacity="0.5">{person(110, 340, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'neutral', 'walk')}
{person(180, 340, 0.95, 1, 'violet', 'blue', 'walk', 'bob', 'neutral', 'walk')}</g>
<path d="M220 386h220" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('unpredictable', '線を引こうにも、次にどこへ行くか読めない', f'''
<path d="M60 340h480M90 360V70" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M90 250l50-90 40 130 50-150 44 120 46-90" fill="none" stroke="{TEA}" stroke-width="7"/>
{''.join(f'<path d="M320 170l{70+i*10} {-40+i*70}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9" marker-end="url(#ar)"/>' for i in range(3))}
<g transform="translate(500 90)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''', arrow=True)

add('unrelenting', '波が休みなく、同じ岩を打ちつづける', f'''
<path d="M0 260h600v140H0z" fill="{BLUP}"/>
<g transform="translate(430 280)"><path d="M-90 40q10-100 90-130 80 30 90 130z" fill="#8d949a" class="o"/></g>
{''.join(f'<path d="M{40+i*80} 300q40-70 80 0" fill="none" stroke="{BLU}" stroke-width="8" stroke-linecap="round"/>' for i in range(4))}
{''.join(f'<path d="M{60+i*80} 350q40-50 80 0" fill="none" stroke="{BLU}" stroke-width="7" stroke-linecap="round"/>' for i in range(4))}
{''.join(f'<path d="M{240+i*40} {200-i*30}h60" class="a" marker-end="url(#ar)"/>' for i in range(3))}''', arrow=True)

add('unreliable', 'すわったとたんに、こわれてしまういす', f'''
<g transform="translate(300 306) rotate(14)">
  <path d="M-46-24v24M46-24v24" fill="none" stroke="{GLDD}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-54-42h108v20h-108z" class="gold o"/>
  <path d="M-54-42v-92h20v92z" class="gold o" transform="rotate(-36 -44 -88)"/></g>
{person(300, 400, 1.0, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
{''.join(f'<path d="M{170+i*30} {200-i*20}l-20-20" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(2))}
{''.join(f'<path d="M{420+i*30} {200-i*20}l20-20" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(2))}''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
