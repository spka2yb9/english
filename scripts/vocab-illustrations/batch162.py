# -*- coding: utf-8 -*-
"""第162回。j-/k-/l-/ma- の名詞と慣用表現。"""
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

def house(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-80 0v-100h160V0z" fill="#fffefd" class="o"/>'
            f'<path d="M-94-100L0-166l94 66z" class="{cls}d o"/>'
            f'<path d="M-24 0v-56h48V0z" class="{cls} o"/>'
            f'<rect x="-62" y="-82" width="34" height="30" class="{cls}p o"/></g>')

def magnifier(x, y, r=60, rot=24):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><circle r="{r}" fill="#ffffff" opacity="0.16" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M0 {r}v{r*0.7:.0f}" stroke="{INK}" stroke-width="15" stroke-linecap="round"/></g>')

# --- 旅・場所 ----------------------------------------------------------------

add('itinerary', '日ごとの行き先と時刻を並べた、旅の予定表', f'''
{doc(300, 200, 380, 320, 0)}
<path d="M130 110h340" fill="none" stroke="{INK}" stroke-width="4"/>
{word(230, 90, 3, 32, INK)}
{''.join(f'<g transform="translate(140 {150+i*46})">'
         f'<rect x="0" y="-8" width="54" height="16" rx="8" class="teal"/>'
         f'<circle cx="86" cy="0" r="10" class="coralp o"/>'
         f'<rect x="112" y="-8" width="{220-(i%2)*60}" height="16" rx="8" fill="{MUTED}"/></g>' for i in range(4))}''')

add('layover', '次の便まで、空港でしばらく待つ', f'''
<g transform="translate(300 130)"><rect x="-250" y="-90" width="500" height="180" rx="12" fill="#eaf4fb" class="o"/>
  {''.join(f'<path d="M{-190+i*130} -90v180" fill="none" stroke="#c6dcea" stroke-width="4"/>' for i in range(4))}</g>
{plane(120, 90, 0.32, -14, 'teal')}
{plane(480, 90, 0.32, -14, 'coral')}
{sit(300, 340, 1.2, 1, 'violet', 'blue', 'bun', 'neutral', 'lap')}
{chair(314, 340, 1.1, 'gold', -1)}
<g transform="translate(430 300)"><path d="M-40-26h80v52h-80z" class="gold o"/>
  <path d="M-16-26v-14h32v14" fill="none" class="a"/></g>
<g transform="translate(140 280)"><circle r="46" fill="#fffefd" class="o"/>
  <path d="M0 0v-30M0 0l22 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></g>''')

add('locality', '地図のうえで、その一帯だけを指す', f'''
<g transform="translate(300 200)"><rect x="-260" y="-160" width="520" height="320" rx="10" fill="#f2f5f6" class="o"/>
  <path d="M-260-40h520M-60-160v320M140-160v320" fill="none" stroke="#ffffff" stroke-width="14"/>
  <path d="M-260-40h520M-60-160v320M140-160v320" fill="none" stroke="{MUTED}" stroke-width="2"/></g>
{''.join(f'<g transform="translate({x} {y}) scale(0.3)">' + house(0, 0, 1, c) + '</g>'
         for x, y, c in [(30,120,'teal'),(110,150,'coral'),(-10,230,'violet'),(90,250,'green')])}
<g transform="translate(60 190)"><rect x="-30" y="-24" width="60" height="48" rx="5" fill="#fffefd" class="o"/>
  <path d="M-34-24h68l-14-20h-40z" class="coral o"/></g>
{ring(60, 190, 130)}''')

add('marsh', '足もとがぬかるみ、あしの生える水辺', f'''
<path d="M0 240q140-20 300-10t300 10v160H0z" fill="#8fa07a" class="o"/>
{''.join(f'<ellipse cx="{80+i*110}" cy="{300+(i%3)*30}" rx="{50-(i%2)*14}" ry="{18-(i%2)*5}" fill="{BLUP}" stroke="{BLU}" stroke-width="2.5"/>' for i in range(5))}
{''.join(f'<g transform="translate({60+i*54} {290+(i%3)*20})"><path d="M0 0v-{90+(i%4)*26}" fill="none" stroke="{GRND}" stroke-width="5"/>'
         f'<ellipse cx="0" cy="-{96+(i%4)*26}" rx="7" ry="18" fill="#8c6b42" stroke="{INK}" stroke-width="2"/></g>' for i in range(10))}
{cloud(140, 90, 1.2, 'blue')}''')

add('landfill', 'ごみを谷に埋めて、上から土をかぶせる', f'''
<path d="M0 200q120 40 300 40t300-40v200H0z" fill="#d9c9a4" class="o"/>
<path d="M60 300q120-70 240-50t180 40v110H60z" fill="#8f9a72" class="o"/>
{''.join(f'<rect x="-14" y="-10" width="28" height="20" rx="3" fill="#b0b6a0" stroke="{INK}" stroke-width="2" transform="translate({120+ (i%5)*80} {310+(i//5)*30}) rotate({-30+i*20})"/>' for i in range(10))}
<g transform="translate(140 200)">
  <path d="M-70 40v-40h90v40z" class="gold o"/>
  <path d="M20 0h40v-30h-40z" class="goldd o"/>
  <circle cx="-40" cy="48" r="22" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="30" cy="48" r="22" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M60-20l70-40 40 30-40 40z" fill="#8d949a" class="o"/></g>''')

add('mansion', '部屋がいくつもある、とても大きな屋敷', f'''
<g transform="translate(300 306)">
  <path d="M-230 0v-160h460V0z" fill="#fffefd" class="o"/>
  <path d="M-246-160h492l-46-60h-400z" class="corald o"/>
  <path d="M-90 0v-110h180V0z" fill="#f4f7f8" class="o"/>
  <path d="M-40 0v-80q0-30 40-30t40 30V0z" class="coral o"/>
  {''.join(f'<rect x="{-206+i*54}" y="-130" width="34" height="44" class="coralp o"/>' for i in range(4))}
  {''.join(f'<rect x="{104+i*54}" y="-130" width="34" height="44" class="coralp o"/>' for i in range(3))}
  {''.join(f'<rect x="{-206+i*54}" y="-60" width="34" height="44" class="coralp o"/>' for i in range(3))}
  {''.join(f'<rect x="{104+i*54}" y="-60" width="34" height="44" class="coralp o"/>' for i in range(3))}
  <path d="M-120-220v-40h30v40zM90-220v-40h30v40z" class="corald o"/></g>
{tree(60, 350, 0.5)}{tree(550, 350, 0.5)}''')

add('lodger', '人の家の一部屋を借りて住む人', f'''
<g transform="translate(300 306)"><path d="M-180 0v-190h360V0z" fill="#fffefd" class="o"/>
  <path d="M-196-190L0-290l196 100z" class="corald o"/>
  <path d="M0-190V0" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-120 0v-70h60V0z" class="coral o"/></g>
<g transform="translate(390 240)"><rect x="-70" y="-70" width="140" height="140" fill="#f4f7f8" class="o"/></g>
{head(390, 250, 26, 'teal', 'bob')}
{ring(390, 250, 62)}
{head(150, 250, 26, 'violet', 'bun')}
<g transform="translate(470 130)">{coin(0, 0, 22)}</g>
<path d="M420 170l30-26" class="a" marker-end="url(#ar)"/>''', arrow=True)

# --- しくみ・お金 -------------------------------------------------------------

add('ledger', '取引を一行ずつ書きこんでいく、分厚い帳簿', f'''
{table(340)}
<g transform="translate(300 210)"><path d="M-230 130q110-40 226-16v-250q-116-26-226 14z" fill="#fffefd" class="o"/>
  <path d="M230 130q-110-40-226-16v-250q116-26 226 14z" fill="#fffefd" class="o"/>
  <path d="M-4-122v246" fill="none" stroke="{MUTED}" stroke-width="3"/>
  {''.join(f'<path d="M-200 {-80+i*42}q90-18 190-6" fill="none" stroke="#dde4e8" stroke-width="3"/>' for i in range(5))}
  {''.join(f'<path d="M200 {-80+i*42}q-90-18-190-6" fill="none" stroke="#dde4e8" stroke-width="3"/>' for i in range(5))}
  {''.join(f'<rect x="-180" y="{-90+i*42}" width="90" height="12" rx="6" fill="{MUTED}"/><rect x="-70" y="{-90+i*42}" width="50" height="12" rx="6" class="teal"/>' for i in range(4))}
  {''.join(f'<rect x="30" y="{-90+i*42}" width="90" height="12" rx="6" fill="{MUTED}"/><rect x="132" y="{-90+i*42}" width="46" height="12" rx="6" class="coral"/>' for i in range(4))}
  <path d="M-230 130q110-40 226-16M230 130q-110-40-226-16" fill="none" class="o"/></g>''')

add('markup', '仕入れ値に利幅を足して、売り値になる', f'''
<path d="M60 340h480" fill="none" stroke="{MUTED}" stroke-width="4"/>
<rect x="110" y="180" width="120" height="160" rx="6" class="tealp o"/>
<rect x="330" y="180" width="120" height="160" rx="6" class="tealp o"/>
<rect x="330" y="90" width="120" height="90" rx="6" class="coral o"/>
<path d="M250 260h60" class="a" marker-end="url(#ar)"/>
<path d="M480 90v90" class="a" stroke="{CRL}" marker-end="url(#ar)" marker-start="url(#ar)"/>
{coin(170, 130, 26)}{coin(390, 50, 24)}''', arrow=True)

add('liquidation', '会社をたたみ、あるものをすべて売り払う', f'''
<g transform="translate(200 306)"><path d="M-120 0v-150h240V0z" fill="#fffefd" class="o"/>
  <path d="M-134-150h268l-30-40h-208z" class="teal o"/>
  {''.join(f'<path d="M-90 {-120+i*30}h180" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(5))}
  <path d="M-40 0v-60h80V0z" fill="#c3cbd1" class="o"/></g>
<path d="M340 200h50" class="a" marker-end="url(#ar)"/>
{''.join(f'<g transform="translate({450+ (i%2)*80} {180+(i//2)*90})">{box(0, 0, 66, 48, 14, c)}</g>' for i, c in enumerate(['gold','coral','violet','green']))}
{''.join(coin(430 + i*40, 340, 20) for i in range(3))}''', arrow=True)

add('livelihood', '手わざで働き、日々の糧を得る', f'''
{table(330)}
{person(180, 306, 1.2, 1, 'teal', 'blue', 'carry', 'cap', 'neutral')}
<g transform="translate(250 200) rotate(24)"><path d="M-8 0h16v70h-16z" class="goldd o"/>
  <path d="M-30-30h60v26h-60z" class="ink"/></g>
<path d="M330 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 290)"><path d="M-70 0q-14-64 0-78 70-16 140 0 14 14 0 78z" fill="#c98f52" class="o"/>
  <path d="M-50-64q50-12 100 0" fill="none" stroke="#a8703a" stroke-width="4"/></g>
{house(490, 180, 0.34, 'coral')}''', arrow=True)

add('logistics', '倉庫から車を出し、道すじを組んで届ける', f'''
<g transform="translate(300 200)"><rect x="-260" y="-160" width="520" height="320" rx="10" fill="#f2f5f6" class="o"/>
  <path d="M-200 130q80-160 200-140t180 -60" fill="none" stroke="{CRL}" stroke-width="6" stroke-dasharray="14 10"/></g>
<g transform="translate(110 306)"><path d="M-70 0v-90h140V0z" fill="#dfe6ea" class="o"/>
  <path d="M-80-90h160l-24-30h-112z" fill="#9aa6ae" class="o"/></g>
<g transform="translate(320 250)"><path d="M-70 0v-46h86v46z" class="teal o"/>
  <path d="M16-34h40l22 34h-62z" class="tealp o"/>
  <circle cx="-40" cy="8" r="15" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="46" cy="8" r="15" fill="none" stroke="{INK}" stroke-width="6"/></g>
{''.join(f'<g transform="translate({500} {120+i*70})"><path d="M-40 0v-40h80V0z" fill="#fffefd" class="o"/>'
         f'<path d="M-46-40h92l-14-20h-64z" class="{c} o"/></g>' for i, c in enumerate(['coral','violet']))}''')

add('licensing', '使ってよいという許諾を、判つきで与える', f'''
{table(280)}
{person(130, 380, 1.15, 1, 'violet', 'blue', 'give', 'bun', 'neutral')}
<g transform="translate(280 200) rotate(-6)"><rect x="-90" y="-60" width="180" height="120" rx="8" class="paper"/>
  {''.join(f'<rect x="-70" y="{-38+i*28}" width="{136-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="52" cy="34" r="24" fill="none" stroke="{CRL}" stroke-width="5"/></g>
<path d="M390 170h50" class="a" marker-end="url(#ar)"/>
{person(510, 380, 1.15, -1, 'teal', 'blue', 'reach', 'short', 'smile')}
{box(500, 250, 66, 46, 14, 'gold')}''', arrow=True)

add('libel', '刷って出した記事で名誉を傷つけ、法廷で問われる', f'''
<g transform="translate(170 200) rotate(-6)"><rect x="-110" y="-130" width="220" height="260" rx="4" class="paper"/>
  <rect x="-86" y="-100" width="172" height="16" rx="8" class="coral"/>
  {''.join(f'<rect x="-86" y="{-60+i*30}" width="{150-(i%2)*40}" height="10" rx="5" fill="{MUTED}"/>' for i in range(4))}
  <ellipse cx="30" cy="80" rx="46" ry="32" fill="{INK}" opacity="0.55"/></g>
<path d="M310 200h50" class="a" stroke="{CRL}" marker-end="url(#ar)"/>
<g transform="translate(450 180) rotate(20)"><path d="M-12 0h24v70h-24z" class="goldd o"/>
  <path d="M-40-36h80v38h-80z" class="goldd o"/></g>
<g transform="translate(450 300)"><rect x="-70" y="-14" width="140" height="28" rx="6" class="goldd o"/></g>''', arrow=True)

# --- からだ ------------------------------------------------------------------

add('ligament', '骨と骨をつなぎとめる、じょうぶな帯', f'''
<g transform="translate(300 200)">
  <path d="M-46-170q0-30 30-30t26 30v90h-56z" fill="#efe9db" class="o"/>
  <path d="M-46 170q0 30 30 30t26-30v-90h-56z" fill="#efe9db" class="o"/>
  <path d="M-56-80q56-20 112 0v40q-56 20-112 0z" class="tealp o"/>
  <path d="M-56 80q56 20 112 0v-40q-56-20-112 0z" class="tealp o"/>
  <path d="M-70-70q-20 70 0 140M70-70q20 70 0 140" fill="none" stroke="{CRL}" stroke-width="16" stroke-linecap="round"/></g>
{ring(300, 200, 140)}''')

add('marrow', '切った骨の中にある、やわらかい部分', f'''
{table(340)}
<g transform="translate(300 260)"><path d="M-150-60q-30 0-30 30t30 30v-60zM-150-60h230v60h-230z" fill="#efe9db" class="o"/>
  <path d="M80-70q40 0 40 40t-40 40q40 0 40 20t-40 20-40-20 20-20q-20 0-20-40t20-40q-20 0-20-20t40-20 40 20-20 20z" fill="#efe9db" class="o"/>
  <ellipse cx="-160" cy="0" rx="26" ry="42" fill="#e0a2a2" class="o"/></g>
{ring(140, 260, 66)}
<g transform="translate(300 130) rotate(90)"><path d="M-100-14h240l40 14-40 14h-240z" fill="#dfe6ea" class="o"/></g>''')

add('mane', 'たてがみが首すじをおおう', f'''
<g transform="translate(320 250)">
  <path d="M-140 60q-16-70 30-100 70-46 150-16 50 20 42 76z" fill="#b98d55" class="o"/>
  <path d="M96-56q34-40 74-20 36 20 16 58-16 28-52 26z" fill="#b98d55" class="o"/>
  <path d="M150-38l40 4-38 20z" fill="#b98d55" class="o"/>
  <path d="M104-78l-6-32 28 22z" fill="#b98d55" class="o"/>
  <circle cx="142" cy="-30" r="5" class="ink"/>
  <g fill="#6d4a26" stroke="{INK}" stroke-width="2">
    {''.join(f'<path d="M{20+i*24}-{54+i*4}q{18+i*3}-{40+i*6} {6+i*2}-{62+i*8}q{22} {26} {14} {62}z" transform="rotate({-6+i*3} {20+i*24} -54)"/>' for i in range(5))}</g></g>
{ring(400, 150, 96)}''')

# --- 情報・まちがい -----------------------------------------------------------

add('misinformation', '写すうちに中身がずれて、まちがった知らせが伝わる', f'''
{''.join(f'<g transform="translate({100+i*120} {200})"><rect x="-50" y="-64" width="100" height="128" rx="6" class="paper"/>'
         f'<rect x="-34" y="{-44}" width="68" height="10" rx="5" fill="{MUTED}"/>'
         f'<rect x="-34" y="-20" width="{58-i*10}" height="10" rx="5" fill="{CRL if i >= 2 else MUTED}"/>'
         f'<rect x="-34" y="4" width="{50-i*6}" height="10" rx="5" fill="{MUTED}"/></g>' for i in range(4))}
{''.join(f'<path d="M{158+i*120} 200h44" class="a" marker-end="url(#ar)"/>' for i in range(3))}
<g transform="translate(460 90)"><path d="M0-30l30 52h-60z" class="gold o"/>
  <path d="M0-10v10" fill="none" stroke="{INK}" stroke-width="4"/><circle cy="12" r="3" class="ink"/></g>''', arrow=True)

add('misconception', '頭のなかの思いこみが、じっさいとちがう', f'''
{head(150, 260, 40, 'teal', 'short')}
<circle cx="220" cy="190" r="9" fill="#fffefd" class="o"/>
<g transform="translate(300 120)"><ellipse rx="106" ry="72" fill="#fffefd" class="o"/>
  <path d="M-40 30l40-60 40 60z" class="coral o"/></g>
<g transform="translate(470 260)"><circle r="70" class="teal o"/></g>
<path d="M380 170l50 40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{cross(470, 120, 1.0)}''')

add('malware', 'こっそり入りこんで悪さをする、しくまれたもの', f'''
<g transform="translate(300 200)"><rect x="-190" y="-140" width="380" height="240" rx="12" class="teald o"/>
  <rect x="-166" y="-116" width="332" height="192" rx="6" fill="#dfe6ea"/>
  <path d="M-90 100h180v30h-180z" class="teald o"/></g>
<g transform="translate(300 190)"><ellipse rx="46" ry="34" fill="{VIO}" class="o"/>
  <circle cx="-16" cy="-10" r="6" fill="#fffefd"/><circle cx="16" cy="-10" r="6" fill="#fffefd"/>
  <path d="M-46-16l-30-24M46-16l30-24M-46 16l-34 20M46 16l34 20" fill="none" stroke="{VIOD}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-20-34l-8-24M20-34l8-24" fill="none" stroke="{VIOD}" stroke-width="5" stroke-linecap="round"/></g>
<g transform="translate(470 110)"><path d="M0-34l34 58h-68z" class="gold o"/>
  <path d="M0-12v12" fill="none" stroke="{INK}" stroke-width="4"/><circle cy="14" r="3" class="ink"/></g>''')

add('manifesto', 'かかげた公約を、ずらりと並べて示す', f'''
<g transform="translate(300 200)"><rect x="-200" y="-150" width="400" height="300" rx="10" class="paper"/>
  <rect x="-200" y="-150" width="400" height="60" rx="0" class="coral o"/>
  {''.join(f'<g><circle cx="-160" cy="{-50+i*54}" r="12" class="teal o"/>'
           f'<rect x="-136" y="{-60+i*54}" width="{290-(i%2)*80}" height="20" rx="10" fill="{MUTED}"/></g>' for i in range(4))}</g>
{head(90, 340, 24, 'violet', 'bun')}
{head(510, 340, 24, 'teal', 'short')}''')

add('manifestation', '目には見えない原因が、目に見える形で現れる', f'''
<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="12 10">
  <circle cx="150" cy="200" r="80"/>
  {''.join(f'<path d="M{150+56*math.cos(math.radians(a)):.0f} {200+56*math.sin(math.radians(a)):.0f}l{20*math.cos(math.radians(a)):.0f} {20*math.sin(math.radians(a)):.0f}"/>' for a in range(0, 360, 60))}</g>
<path d="M270 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 200)"><circle r="80" class="coral o"/>
  {''.join(f'<circle cx="{50*math.cos(math.radians(a)):.0f}" cy="{50*math.sin(math.radians(a)):.0f}" r="14" class="coralp o"/>' for a in range(0, 360, 60))}</g>
{''.join(spark(x, y, 0.8) for x, y in [(370,90),(540,300)])}''', arrow=True)

# --- 見る・追う ---------------------------------------------------------------

add('look back on', 'アルバムをめくって、過ぎた日々を思い返す', f'''
{sit(180, 340, 1.2, 1, 'violet', 'blue', 'bun', 'smile', 'lap')}
{chair(194, 340, 1.1, 'gold', -1)}
<g transform="translate(400 250)"><path d="M-140 90q70-30 140-10v-160q-70-20-140 10z" fill="#c9a06c" class="o"/>
  <path d="M140 90q-70-30-140-10v-160q70-20 140 10z" fill="#c9a06c" class="o"/>
  {''.join(f'<rect x="{-116+ (i%2)*74}" y="{-96+(i//2)*70}" width="60" height="52" rx="4" fill="#f3ead6" stroke="{INK}" stroke-width="2"/>' for i in range(4))}
  {''.join(f'<rect x="{24+ (i%2)*74}" y="{-96+(i//2)*70}" width="60" height="52" rx="4" fill="#f3ead6" stroke="{INK}" stroke-width="2"/>' for i in range(4))}</g>
<path d="M290 130h-60" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('look out for', '目をこらして、それらしいものをさがす', f'''
{person(170, 306, 1.25, 1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
<path d="M150 194h50" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9">
  <path d="M230 200L520 130M230 210L540 240M234 230L500 330"/></g>
{box(520, 130, 60, 44, 12, 'coral')}
{ring(520, 128, 66)}
<g opacity="0.35">{box(520, 250, 56, 40, 12, 'gold')}{box(490, 340, 56, 40, 12, 'green')}</g>''')

add('lose sight of', '追っていたものが、霧のむこうに見えなくなる', f'''
{person(120, 306, 1.2, 1, 'coral', 'blue', 'reach', 'short', 'sad')}
<g opacity="0.9">{cloud(340, 220, 2.2, 'blue')}{cloud(460, 260, 2.0, 'blue')}</g>
<g opacity="0.28">{box(490, 220, 90, 66, 20, 'gold')}</g>
<path d="M190 220h80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
<path d="M290 220h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="4 12" opacity="0.5"/>''')

add('keep track of', '記録をつけつづけて、どうなっているかを押さえる', f'''
{doc(230, 200, 220, 260, 0)}
{''.join(f'<g><rect x="140" y="{110+i*50}" width="18" height="18" rx="4" fill="none" stroke="{INK}" stroke-width="3"/>'
         f'{"<path d=@M141 " + str(120+i*50) + "l6 7 12-14@ fill=@none@ stroke=@" + GRN + "@ stroke-width=@4@ stroke-linecap=@round@/>" if i < 3 else ""}'
         f'<rect x="172" y="{112+i*50}" width="{130-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/></g>'.replace('@', chr(34)) for i in range(4))}
{person(460, 306, 1.2, -1, 'teal', 'blue', 'reach', 'bun', 'neutral')}
<g transform="translate(400 200) rotate(24)"><path d="M-8-70h16v90l-8 16-8-16z" class="coral o"/></g>
<g transform="translate(520 130)"><circle r="42" fill="#fffefd" class="o"/>
  <path d="M0 0v-26M0 0l20 12" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/></g>''')

add('jump to conclusions', 'ひとつ見ただけで、途中を飛ばして決めつける', f'''
<g transform="translate(120 240)"><rect x="-56" y="-46" width="112" height="92" rx="8" class="tealp o"/>
  <circle r="20" class="teal o"/></g>
<g opacity="0.35" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9">
  <rect x="230" y="200" width="120" height="80" rx="8"/><rect x="230" y="100" width="120" height="80" rx="8"/></g>
<path d="M180 200q140-120 260-40" fill="none" stroke="{CRL}" stroke-width="7" marker-end="url(#ar)"/>
<g transform="translate(490 200)"><rect x="-70" y="-56" width="140" height="112" rx="10" class="paper"/>
  {cross(0, 0, 1.1)}</g>
{head(120, 350, 24, 'coral', 'short')}''', arrow=True)

# --- 危なさ・重み -------------------------------------------------------------

add('jeopardy', '大事なものが、落ちるすれすれのところにある', f'''
{table(340)}
<g transform="translate(520 300)"><path d="M-46-30h92l-46 70z" class="violet o"/>
  <path d="M-46-30l22-24h48l22 24z" class="violetp o"/></g>
<path d="M556 340v60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{''.join(f'<path d="M{420+i*26} {160+i*16}q14-16 28 0" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(2))}
{person(180, 340, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'surprised')}
<g transform="translate(340 150)"><path d="M0-40l40 70h-80z" class="gold o"/>
  <path d="M0-14v14" fill="none" stroke="{INK}" stroke-width="5"/><circle cy="16" r="4" class="ink"/></g>''')

add('juncture', '道が分かれる、その大事な一点', f'''
<path d="M60 200h200" fill="none" stroke="{GLDD}" stroke-width="12"/>
<path d="M260 200q80 0 110-70t170-70" fill="none" stroke="{GLDD}" stroke-width="10" marker-end="url(#ar)"/>
<path d="M260 200q80 0 110 70t170 70" fill="none" stroke="{GLDD}" stroke-width="10" marker-end="url(#ar)"/>
<circle cx="262" cy="200" r="20" class="coral o"/>
{ring(262, 200, 56)}
{person(140, 250, 0.8, 1, 'teal', 'blue', 'walk', 'short', 'neutral', 'walk')}''', arrow=True)

add('massacre', '多くの命が一度に失われたあと、花をたむける', f'''
<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="11 9">
  {''.join(f'<g><circle cx="{100+ (i%5)*80}" cy="{200+(i//5)*90}" r="22"/>'
           f'<path d="M{78+ (i%5)*80} 236q22-12 44 0l-8 60h-30z"/></g>' for i in range(10))}</g>
<g opacity="0.7">{cloud(300, 80, 2.0, 'violet')}</g>
<g transform="translate(520 340)"><path d="M0 40v-40" fill="none" stroke="{GRND}" stroke-width="5"/>
  {''.join(f'<ellipse cx="0" cy="-24" rx="9" ry="18" class="coralp o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 72))}</g>
{head(520, 250, 24, 'blue', 'short')}''')

# --- 人・仲介 ----------------------------------------------------------------

add('mediator', 'あいだに立って、話し合いをまとめる人', f'''
{table(260)}
{person(130, 380, 1.15, 1, 'coral', 'blue', 'give', 'short', 'neutral')}
{person(470, 380, 1.15, -1, 'teal', 'blue', 'give', 'bob', 'neutral')}
{person(300, 380, 1.25, 1, 'violet', 'green', 'up', 'bun', 'smile')}
<path d="M210 220h60M390 220h-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
{ring(300, 280, 130)}''')

add('mediation', '仲立ちのおかげで、両者が握手にいたる', f'''
{table(260)}
{person(120, 380, 1.15, 1, 'coral', 'blue', 'give', 'short', 'smile')}
{person(480, 380, 1.15, -1, 'teal', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(300 300)">{hand(-20, 0, 1)}{hand(20, 0, -1)}</g>
{head(300, 150, 26, 'violet', 'bun')}
<path d="M300 190v40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
{''.join(spark(x, y, 0.8) for x, y in [(220,200),(380,196)])}''')

add('midwife', 'お産に立ち会い、赤ん坊を取り上げる人', f'''
{table(340)}
<g transform="translate(360 340)"><path d="M-140 0v-40h280V0z" class="goldd o"/>
  <path d="M-120-40v-30h240v30z" class="tealp o"/>
  <path d="M-114-70q-6-26 30-26h50v26z" fill="#fffefd" class="o"/></g>
{head(226, 262, 24, 'violet', 'bob')}
{person(120, 340, 1.2, 1, 'teal', 'blue', 'carry', 'bun', 'smile')}
<g transform="translate(140 240) rotate(-14)"><path d="M-46 20q0-40 46-40t46 40q-46 16-92 0z" class="coralp o"/>
  <circle cx="20" cy="-6" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/></g>
{''.join(spark(x, y, 0.7) for x, y in [(80,150),(240,130)])}''')

# --- しくみ・性質 -------------------------------------------------------------

add('magnetism', '磁石が、鉄の粉を強く引き寄せる', f'''
<g transform="translate(200 200)"><path d="M-70 80v-90a70 70 0 0 1 140 0v90h-46v-90a24 24 0 0 0-48 0v90z" fill="#8d949a" class="o"/>
  <path d="M-70 80h46v20h-46zM24 80h46v20h-46z" class="coral o"/></g>
{''.join(f'<path d="M{300+i*10} {130+i*24}q60-10 120 0" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 6"/>' for i in range(5))}
{''.join(f'<rect x="-8" y="-4" width="16" height="8" rx="2" fill="#5b6b78" transform="translate({380+ (i%4)*50} {150+(i//4)*50}) rotate({-20+i*14})"/>' for i in range(12))}
{''.join(f'<path d="M{330+i*40} 250h-40" class="a" marker-end="url(#ar)"/>' for i in range(3))}''', arrow=True)

add('lubrication', '油をさすと、きしみが消えてなめらかに回る', f'''
{split()}
<g transform="translate(150 210)"><circle r="66" class="teal o"/>
  {''.join(f'<rect x="-9" y="-84" width="18" height="20" rx="3" class="teal o" transform="rotate({d})"/>' for d in range(0, 360, 45))}
  <circle r="22" fill="#fffdf6" class="o"/></g>
{''.join(f'<path d="M{70-i*10} {130+i*30}q-18 16 0 32" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(2))}
{ring(150, 210, 126, True)}
<g transform="translate(450 230)"><circle r="66" class="teal o"/>
  {''.join(f'<rect x="-9" y="-84" width="18" height="20" rx="3" class="teal o" transform="rotate({d})"/>' for d in range(0, 360, 45))}
  <circle r="22" fill="#fffdf6" class="o"/></g>
<g transform="translate(430 100) rotate(150)"><path d="M-24 0v-40h48V0z" class="goldd o"/>
  <path d="M24-30l40-16v34z" class="goldd o"/></g>
{''.join(drop(455 + i*12, 140 + i*14, 0.8, 'gold') for i in range(2))}''')

add('longevity', '何十年も生き、たくさんのろうそくを吹き消す', f'''
{table(330)}
<g transform="translate(320 300)"><path d="M-120 0q0-70 120-70t120 70z" class="coralp o"/>
  <path d="M-120 0h240v14h-240z" class="coral o"/>
  {''.join(f'<g transform="translate({-96+i*32} -74)"><path d="M-5 0v-30h10V0z" fill="#fffefd" stroke="{INK}" stroke-width="2"/>'
           f'<path d="M0-34q-8-10 0-18 8 8 0 18z" class="gold o"/></g>' for i in range(7))}</g>
{head(120, 250, 30, 'violet', 'bun')}
<path d="M100 220l14 6M140 220l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
{''.join(spark(x, y, 0.8) for x, y in [(200,110),(500,120)])}''')

add('make the most of', '少ない材料を、あますところなく使いきる', f'''
{table(340)}
<g transform="translate(150 300)"><rect x="-60" y="-40" width="120" height="40" rx="6" class="goldp o"/></g>
<path d="M250 200h60" class="a" marker-end="url(#ar)"/>
{''.join(f'<g transform="translate({380+ (i%3)*70} {200+(i//3)*80})">'
         + (f'<circle r="26" class="gold o"/>' if i % 3 == 0 else
            f'<rect x="-24" y="-24" width="48" height="48" rx="6" class="gold o"/>' if i % 3 == 1 else
            f'<path d="M-26 22l26-46 26 46z" class="gold o"/>') + '</g>' for i in range(6))}
{''.join(spark(x, y, 0.7) for x, y in [(320,110),(560,300)])}''', arrow=True)

add('knack', '同じ道具でも、こつを知っていると軽々できる', f'''
{split()}
{person(150, 320, 1.15, 1, 'coral', 'blue', 'carry', 'short', 'sad')}
<g transform="translate(164 220)"><path d="M-40-26h80v52h-80z" class="gold o"/></g>
{drop(110, 190, 0.9)}
{ring(150, 220, 126, True)}
{person(450, 320, 1.15, 1, 'teal', 'blue', 'hold', 'bob', 'smile')}
<g transform="translate(478 214) rotate(-16)"><path d="M-40-26h80v52h-80z" class="gold o"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(390,130),(540,150)])}
{ring(450, 220, 126)}''')

add('mentality', 'その人の色めがねを通して、世の中が見える', f'''
{head(150, 260, 40, 'teal', 'short')}
<g transform="translate(300 200)"><ellipse rx="60" ry="90" fill="{VIOP}" opacity="0.8" class="o"/></g>
<g transform="translate(470 200)"><rect x="-110" y="-110" width="220" height="220" rx="10" fill="#f4f7f8" class="o"/>
  <path d="M-90 90l60-80 44 44 40-56 66 92z" fill="{VIOP}"/>
  {sun(60, -56, 24)}
  <rect x="-110" y="-110" width="220" height="220" rx="10" fill="{VIO}" opacity="0.25"/></g>
<path d="M196 240l60-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('mindset', '心の向きを、あらかじめこちらに合わせておく', f'''
{head(180, 250, 46, 'teal', 'short')}
<g transform="translate(180 130)"><circle r="56" fill="#fffefd" class="o"/>
  <path d="M-46 30a56 56 0 0 1 92 0" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <path d="M0 30L34-24" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round"/>
  <circle cy="30" r="6" class="ink"/></g>
<path d="M260 230h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 240)"><path d="M-90 60v-90l90-60 90 60v90z" class="tealp o"/>
  <path d="M-30 60V10h60v50" class="teal o"/></g>''', arrow=True)

# --- 慣用表現 ----------------------------------------------------------------

add('let alone', '小さなほうでもできないのに、まして大きいほうは無理', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(200 340)"><path d="M-40 0v-40h80v40" fill="none" stroke="{GLDD}" stroke-width="9"/>
  <path d="M-50-40h100" fill="none" stroke="{CRL}" stroke-width="9"/></g>
<g transform="translate(450 340)"><path d="M-70 0v-200h140v200" fill="none" stroke="{GLDD}" stroke-width="10"/>
  <path d="M-80-200h160" fill="none" stroke="{CRL}" stroke-width="10"/></g>
{person(110, 340, 1.1, 1, 'coral', 'blue', 'reach', 'short', 'sad')}
{cross(200, 250, 0.9)}
{cross(450, 160, 1.2)}''')

add('let the cat out of the bag', '袋からねこが飛び出し、秘密がばれる', f'''
{table(340)}
<g transform="translate(230 300)"><path d="M-70 0q-16-70 0-90 70-24 140 0 16 20 0 90z" class="goldp o"/>
  <path d="M-70-90q70 26 140 0" fill="none" stroke="{GLDD}" stroke-width="5"/></g>
<g transform="translate(380 190) rotate(-14)"><ellipse rx="60" ry="36" fill="#c9a06c" class="o"/>
  <circle cx="46" cy="-24" r="26" fill="#c9a06c" class="o"/>
  <path d="M28-42l-6-24 22 14zM62-48l14-22 8 22z" fill="#c9a06c" class="o"/>
  <circle cx="38" cy="-26" r="4" class="ink"/><circle cx="56" cy="-26" r="4" class="ink"/>
  <path d="M-58 6q-40-16-40-50" fill="none" stroke="#c9a06c" stroke-width="12" stroke-linecap="round"/></g>
{head(530, 280, 26, 'teal', 'short')}
<path d="M556 240q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('learn the ropes', '先輩に綱の扱いを教わって、仕事を覚える', f'''
<path d="M0 300h600v100H0z" fill="{BLUP}"/>
<g transform="translate(300 300)"><path d="M-240 0h480l-40 60h-400z" class="coral o"/>
  <path d="M-100 0v-190" fill="none" stroke="{GLDD}" stroke-width="10"/>
  <path d="M-100-190q100 40 160 190M-100-160q80 40 120 160" fill="none" stroke="{GLDD}" stroke-width="6"/></g>
{person(180, 300, 1.15, 1, 'violet', 'blue', 'point', 'cap', 'smile')}
{person(330, 300, 1.05, -1, 'teal', 'blue', 'reach', 'short', 'neutral')}
<path d="M250 190h40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('lead to', '最初のひと押しが、次々に次を起こす', f'''
{''.join(f'<g transform="translate({110+i*80} 280) rotate({-40+ (0 if i else -40)})">'
         f'<rect x="-16" y="-90" width="32" height="90" rx="4" class="tealp o"/></g>' for i in range(1))}
{''.join(f'<rect x="-16" y="-90" width="32" height="90" rx="4" class="tealp o" transform="translate({190+i*70} 280) rotate({-14})"/>' for i in range(5))}
<path d="M60 200h50" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(540 280)"><rect x="-16" y="-90" width="32" height="90" rx="4" class="coral o"/></g>
<path d="M150 130h340" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9" marker-end="url(#ar)"/>''', arrow=True)

add('keynote', '会のはじめに、主題となる話をする', f'''
<g transform="translate(430 190)"><rect x="-150" y="-110" width="300" height="220" rx="10" class="teald o"/>
  <rect x="-134" y="-94" width="268" height="188" rx="4" fill="#f4f7f8"/>
  {word(0, -30, 4, 44, TEA)}
  {''.join(f'<rect x="-100" y="{20+i*30}" width="{200-(i%2)*60}" height="14" rx="7" fill="{MUTED}"/>' for i in range(2))}</g>
{person(140, 340, 1.25, 1, 'violet', 'blue', 'point', 'bun', 'smile')}
<g transform="translate(168 236) rotate(-18)"><rect x="-11" y="-30" width="22" height="66" rx="10" class="ink"/>
  <circle cy="-34" r="16" fill="#8f9aa2" class="o"/></g>
{''.join(f'<g transform="translate({70+i*70} 390)">{head(0, 0, 22, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','cap')]))}''')

# --- もの ---------------------------------------------------------------------

add('ivy', '壁をつたって、上へのぼる緑のつる', f'''
<g transform="translate(300 210)"><rect x="-230" y="-160" width="460" height="320" rx="6" fill="#e8dfcd" class="o"/>
  {''.join(f'<path d="M-230 {-110+i*54}h460" fill="none" stroke="#d5c9ae" stroke-width="3"/>' for i in range(5))}</g>
{''.join(f'<path d="M{130+i*110} 360q-20-90 10-150t-6-140" fill="none" stroke="{GRND}" stroke-width="6"/>' for i in range(4))}
{''.join(f'<path d="M{124+ (i%4)*110+ (12 if i//4 % 2 else -12)} {330-(i//4)*60}q-24-6-28-30 22 2 28 22q6-24 30-28-4 24-30 36z" class="greenp o"/>' for i in range(16))}''')

add('lotus', '池に浮かぶ、大きな葉と八重の花', f'''
<path d="M0 240h600v160H0z" fill="{BLUP}"/>
{''.join(f'<g transform="translate({x} {y})"><path d="M-60 0a60 30 0 1 0 120 0 60 30 0 1 0-120 0z" class="greenp o"/>'
         f'<path d="M0-8v16M-40 0h80" fill="none" stroke="{GRND}" stroke-width="3"/></g>' for x, y in [(130,320),(470,300)])}
<g transform="translate(300 250)">
  {''.join(f'<ellipse cx="0" cy="-40" rx="18" ry="46" class="coralp o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 45))}
  {''.join(f'<ellipse cx="0" cy="-26" rx="14" ry="32" class="coral o" transform="rotate({d+22} 0 0)"/>' for d in range(0, 360, 45))}
  <circle r="16" class="goldp o"/>
  <path d="M0 46v50" fill="none" stroke="{GRND}" stroke-width="6"/></g>''')

add('linen', 'あさの糸で織った、目の見える布', f'''
{table(340)}
<g transform="translate(280 240)"><rect x="-160" y="-110" width="320" height="220" rx="6" fill="#efe6d2" class="o"/>
  {''.join(f'<path d="M-160 {-92+i*24}h320" fill="none" stroke="#d8ccb0" stroke-width="5"/>' for i in range(9))}
  {''.join(f'<path d="M{-140+i*24} -110v220" fill="none" stroke="#d8ccb0" stroke-width="5"/>' for i in range(12))}</g>
<g transform="translate(500 300)"><path d="M0 0v-120" fill="none" stroke="{GRND}" stroke-width="6"/>
  {''.join(f'<ellipse cx="0" cy="-140" rx="10" ry="18" class="bluep o" transform="rotate({d} 0 -122)"/>' for d in range(0, 360, 72))}</g>''')

add('margarine', 'パンにぬる、植物からつくったやわらかい脂', f'''
{table(340)}
<g transform="translate(230 300)"><path d="M-80 0v-80h160V0z" class="goldp o"/>
  <path d="M-86-80h172v-16h-172z" class="goldd o"/>
  <path d="M-60-50h50v30h-50z" fill="#fffefd" opacity="0.6"/></g>
<g transform="translate(430 280)"><path d="M-70 20q-14-56 0-66 70-16 140 0 14 10 0 66z" fill="#c98f52" class="o"/>
  <path d="M-56-40q56-12 112 0" fill="none" stroke="#a8703a" stroke-width="4"/>
  <path d="M-50-46q50-14 100 0" fill="none" stroke="{GLD}" stroke-width="8"/></g>
<g transform="translate(340 190) rotate(24)"><path d="M-8 0h16v70h-16z" class="goldd o"/>
  <path d="M-6-70h12v70h-12z" fill="#dfe6ea" class="o"/></g>''')

add('marmalade', '皮ごと煮た、だいだい色のジャム', f'''
{table(340)}
<g transform="translate(280 300)"><path d="M-70 0v-110h140V0z" fill="#eaf4fb" class="o"/>
  <path d="M-62-96h124v92h-124z" fill="#e08a3c"/>
  {''.join(f'<rect x="-8" y="-4" width="24" height="8" rx="3" fill="#c96a26" transform="translate({-40+ (i%4)*28} {-70+(i//4)*26}) rotate({-30+i*20})"/>' for i in range(8))}
  <path d="M-76-110h152v-18h-152z" class="goldd o"/>
  <path d="M-70 0v-110h140V0z" fill="none" class="o"/></g>
<g transform="translate(470 290)"><circle r="50" fill="#e8983a" class="o"/>
  <path d="M0-50v-16" fill="none" stroke="{GRND}" stroke-width="5"/>
  <path d="M4-60q26-8 30-30-26 4-32 26z" class="greenp o"/></g>''')

add('mash', 'ゆでたいもを、押しつぶしてなめらかにする', f'''
{table(340)}
<g transform="translate(280 300)"><path d="M-90 0q0 20 90 20t90-20v-50h-180z" class="teal o"/>
  <ellipse cy="-50" rx="90" ry="24" class="tealp o"/>
  <ellipse cy="-50" rx="70" ry="18" fill="#f3e2b6"/></g>
<g transform="translate(280 150) rotate(6)"><path d="M-10-90h20v90h-20z" class="goldd o"/>
  <path d="M-46 0h92v22h-92z" fill="#8d949a" class="o"/>
  {''.join(f'<path d="M{-34+i*17} 0v22" fill="none" stroke="{INK}" stroke-width="3"/>' for i in range(5))}</g>
<path d="M280 60v30" class="a" stroke-width="6" marker-end="url(#ar)"/>
{''.join(f'<ellipse cx="{460+ (i%2)*40}" cy="{280+(i//2)*30}" rx="24" ry="18" fill="#e0c98f" stroke="{INK}" stroke-width="2.5"/>' for i in range(4))}''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
