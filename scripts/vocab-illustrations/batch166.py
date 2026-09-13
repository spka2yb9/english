# -*- coding: utf-8 -*-
"""第166回。pr-/q-/ra-/re- の名詞と句動詞。"""
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

def target(x, y, s=1):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="{(96-i*24)*s:.0f}" class="{c} o"/>'
                   for i, c in enumerate(['coralp', 'coral', 'coralp', 'coral']))

def house(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-80 0v-100h160V0z" fill="#fffefd" class="o"/>'
            f'<path d="M-94-100L0-166l94 66z" class="{cls}d o"/>'
            f'<path d="M-24 0v-56h48V0z" class="{cls} o"/>'
            f'<rect x="-62" y="-82" width="34" height="30" class="{cls}p o"/></g>')

# --- 頼る ---------------------------------------------------------------------

add('rely on', '相手に寄りかかって、支えてもらう', f'''
{person(390, 306, 1.3, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(270 306) rotate(-16)">{person(0, 0, 1.15, 1, 'coral', 'blue', 'hold', 'bob', 'smile')}</g>
<path d="M330 220h30" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
{''.join(spark(x, y, 0.7) for x, y in [(150,140),(500,140)])}''')

add('reliant on', 'その一本の線がなければ、動かなくなる', f'''
<g transform="translate(200 220)"><rect x="-110" y="-110" width="220" height="220" rx="14" class="teald o"/>
  <rect x="-90" y="-90" width="180" height="120" rx="6" fill="#dfe6ea"/>
  {''.join(f'<circle cx="{-50+i*50}" cy="60" r="16" class="{c} o"/>' for i, c in enumerate(['coral','gold','green']))}</g>
<path d="M310 240q80 40 140-40" fill="none" stroke="{INK}" stroke-width="8"/>
<g transform="translate(480 170)"><rect x="-40" y="-40" width="80" height="80" rx="10" class="goldp o"/>
  <path d="M-10-16l-8 22h18l-10 26 26-34h-16l12-14z" class="gold o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M380 300h80"/></g>''')

add('reliance', '仕入れの大半を、一つの先に頼っている', f'''
<g transform="translate(300 200)"><circle r="140" class="tealp o"/>
  <path d="M0 0v-140a140 140 0 1 1-100 240z" class="teal o"/>
  {''.join(f'<path d="M0 0l{140*math.cos(math.radians(a)):.0f} {140*math.sin(math.radians(a)):.0f}" fill="none" stroke="{TEAD}" stroke-width="3"/>' for a in [-90, 120, 150])}</g>
<g transform="translate(500 300)"><path d="M-60 0v-70h120V0z" fill="#dfe6ea" class="o"/>
  <path d="M-40-70v-30h20v30z" class="teald o"/></g>
<path d="M420 250h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

# --- 予言・散文 ---------------------------------------------------------------

add('prophecy', '古い巻き物に書かれていた、先を告げることば', f'''
{table(340)}
<g transform="translate(300 260) rotate(-4)">
  <path d="M-190-70h380v140h-380z" fill="#f3ead6" class="o"/>
  <ellipse cx="-190" cy="0" rx="24" ry="70" fill="#e0d3b4" class="o"/>
  <ellipse cx="190" cy="0" rx="24" ry="70" fill="#e0d3b4" class="o"/>
  {''.join(f'<rect x="-150" y="{-44+i*30}" width="{280-(i%2)*80}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}</g>
{''.join(spark(x, y, 0.8) for x, y in [(120,110),(490,110)])}''')

add('prose', '行を区切った詩とちがい、続けて書く文章', f'''
{split()}
{''.join(word(150, 130 + i*44, n, 26, TEA) for i, n in enumerate([3, 5, 2, 4]))}
{ring(150, 200, 132, True)}
{''.join(f'<rect x="340" y="{120+i*36}" width="{220-(i%3)*20}" height="16" rx="8" fill="{MUTED}"/>' for i in range(6))}
{ring(450, 200, 132)}''')

add('provocation', 'わざとつついて、相手を怒らせようとする', f'''
{person(160, 306, 1.2, 1, 'violet', 'blue', 'point', 'short', 'neutral')}
<path d="M230 220h80" fill="none" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
{person(430, 306, 1.25, -1, 'coral', 'blue', 'up', 'short', 'neutral')}
<path d="M406 190l16 6M454 190l-16 6" fill="none" stroke="{INK}" stroke-width="3.5"/>
<g class="corals" stroke-width="6">{''.join(f'<path d="M430 150v-26" transform="rotate({d} 430 190)"/>' for d in [-30, 0, 30])}</g>
<path d="M134 200q14 12 28 0" fill="none" stroke="{INK}" stroke-width="3"/>''', arrow=True)

add('prowess', '遠くの的のまん中を、みごとに射抜く', f'''
{target(470, 200, 1.0)}
<path d="M120 200h300" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
<g transform="translate(440 200)"><path d="M-40 0h80" stroke="{GLDD}" stroke-width="7" fill="none"/>
  <path d="M-40 0l-14-10 4 10-4 10z" fill="{CRLD}"/></g>
{person(120, 306, 1.2, 1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
{''.join(spark(x, y, 0.8) for x, y in [(400,90),(540,90)])}''')

# --- 近さ・広がり -------------------------------------------------------------

add('proximity', '二つが、すぐ隣といえるほど近い', f'''
<circle cx="250" cy="200" r="70" class="teal o"/>
<circle cx="400" cy="200" r="70" class="coral o"/>
<path d="M320 200h10" fill="none" stroke="{MUTED}" stroke-width="0"/>
<path d="M320 130v140M330 130v140" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 7"/>
<path d="M300 320h50" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('radius', '中心から、へりまでの長さ', f'''
<circle cx="300" cy="200" r="150" fill="none" stroke="{TEA}" stroke-width="6"/>
<circle cx="300" cy="200" r="10" class="ink"/>
<path d="M300 200h150" class="a" stroke-width="6" marker-end="url(#ar)"/>
<path d="M300 200l-106 106" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"/>
{ring(300, 200, 172, True)}''', arrow=True)

add('rarity', 'ありふれた品のなかに、ひとつだけの珍しい品', f'''
{''.join(f'<g transform="translate({80+ (i%5)*70} {150+(i//5)*90})"><circle r="28" class="tealp o"/></g>' for i in range(10) if i != 7)}
<g transform="translate(360 240)"><path d="M-34-20h68l-34 54z" class="violet o"/>
  <path d="M-34-20l16-18h36l16 18z" class="violetp o"/></g>
{ring(360, 232, 62)}
<g transform="translate(360 232)"><rect x="-80" y="-90" width="160" height="180" rx="8" fill="none" stroke="{MUTED}" stroke-width="4"/></g>''')

# --- 決まり・手続き -----------------------------------------------------------

add('ratification', '議会が署名と判をそろえ、条約を正式に認める', f'''
{table(280)}
{doc(240, 200, 220, 250, 0)}
{''.join(f'<rect x="150" y="{110+i*44}" width="{180-(i%2)*60}" height="14" rx="7" fill="{MUTED}"/>' for i in range(3))}
<circle cx="310" cy="290" r="34" fill="none" stroke="{CRL}" stroke-width="7"/>
<g transform="translate(190 290) rotate(-14)"><path d="M-60 0q40-24 70-2t50-8" fill="none" stroke="{TEA}" stroke-width="5"/></g>
{''.join(f'<g transform="translate({430+ (i%2)*70} {330+(i//2)*0})">{head(0, 0, 24, c, h)}</g>'
         for i, (c, h) in enumerate([('teal','short'),('violet','bun')]))}
<g transform="translate(490 180)"><path d="M-30 40h60v20h-60z" class="corald o"/>
  <path d="M-16-40h32v80h-32z" class="coral o"/><path d="M-30-56h60v18h-60z" class="corald o"/></g>''')

add('procurement', '必要なものを、外から手配して仕入れる', f'''
<g transform="translate(120 306)"><path d="M-80 0v-110h160V0z" fill="#fffefd" class="o"/>
  <path d="M-92-110h184l-24-34h-136z" class="teal o"/></g>
{''.join(f'<g transform="translate({330+ (i%2)*100} {150+(i//2)*130})">{box(0, 0, 70, 50, 16, c)}</g>' for i, c in enumerate(['gold','violet','coral','green']))}
{''.join(f'<path d="M{290+ (i%2)*100} {170+(i//2)*130}L220 250" class="a" marker-end="url(#ar)"/>' for i in range(4))}
<g transform="translate(220 180) rotate(-8)"><rect x="-50" y="-62" width="100" height="124" rx="6" class="paper"/>
  {''.join(f'<rect x="-34" y="{-42+i*26}" width="68" height="9" rx="4.5" fill="{MUTED}"/>' for i in range(4))}
  <circle cx="20" cy="46" r="14" fill="none" stroke="{CRL}" stroke-width="4"/></g>''', arrow=True)

add('remand', '裁判の日まで、身がらを預かっておく', f'''
<g transform="translate(200 220)"><path d="M-96-96h192v192h-192z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{-66+i*34} -96v192" fill="none" stroke="{INK}" stroke-width="7"/>' for i in range(5))}
  <path d="M-96-96h192v192h-192z" fill="none" class="o"/></g>
{person(200, 316, 1.0, 1, 'coral', 'blue', 'hold', 'short', 'sad')}
<g transform="translate(460 190)"><rect x="-100" y="-90" width="200" height="180" rx="10" class="paper"/>
  <rect x="-100" y="-90" width="200" height="34" rx="0" class="teal o"/>
  {''.join(f'<rect x="{-80+ (i%4)*44}" y="{-38+(i//4)*44}" width="34" height="34" rx="5" fill="#eef2f4"/>' for i in range(8))}
  <rect x="12" y="6" width="34" height="34" rx="5" class="coral o"/></g>
<path d="M320 240h50" class="a" marker-end="url(#ar)"/>''', arrow=True)

# --- やり直す・立て直す --------------------------------------------------------

add('rectification', '記録の誤りに線を引き、正しく書き直す', f'''
{doc(300, 200, 300, 290, 0)}
{''.join(f'<g><rect x="180" y="{110+i*50}" width="120" height="14" rx="7" fill="{MUTED}"/>'
         f'<rect x="316" y="{110+i*50}" width="60" height="14" rx="7" class="teal"/></g>' for i in range(4))}
<path d="M316 160h60" stroke="{CRL}" stroke-width="5" fill="none"/>
<rect x="316" y="176" width="60" height="14" rx="7" class="coral"/>
<g transform="translate(430 130) rotate(30)"><path d="M-8-70h16v90l-8 16-8-16z" class="coral o"/></g>
{ring(346, 176, 62)}''')

add('recurrence', '直したはずの不具合が、しばらくしてまた出る', f'''
<path d="M60 250h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
{''.join(f'<g transform="translate({x} 250)"><path d="M0-40l34 58h-68z" class="gold o"/>'
         f'<path d="M0-18v12" fill="none" stroke="{INK}" stroke-width="4"/><circle cy="10" r="3" class="ink"/></g>' for x in [140, 380])}
{''.join(f'<g transform="translate({x} 300)"><path d="M-22 0l18 20 36-42" fill="none" stroke="{GRN}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>' for x in [250, 490])}
<path d="M180 130q100-70 200 0" fill="none" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('reformation', '古いしくみを組み直して、新しい形にする', f'''
<g transform="translate(150 220)">
  {''.join(f'<rect x="{-90+ (i%3)*62}" y="{-90+(i//3)*62}" width="52" height="52" rx="4" fill="#c3ccd2" stroke="{INK}" stroke-width="2.5" transform="rotate({-14+i*6} {-64+(i%3)*62} {-64+(i//3)*62})"/>' for i in range(9))}</g>
<path d="M280 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(460 220)">
  {''.join(f'<rect x="{-90+ (i%3)*62}" y="{-90+(i//3)*62}" width="52" height="52" rx="4" class="teal o"/>' for i in range(9))}</g>
{''.join(spark(x, y, 0.8) for x, y in [(370,110),(560,120)])}''', arrow=True)

add('refinement', 'ざらついた形を、みがいて上質に仕上げる', f'''
{split()}
<g transform="translate(150 220)"><path d="M-70 70q-30-90 0-120 70-30 140 0 30 30 0 120z" fill="#b0a894" class="o"/>
  {''.join(f'<path d="M{-50+i*30} -30q10 40 0 70" fill="none" stroke="#8f886f" stroke-width="5"/>' for i in range(4))}</g>
{ring(150, 220, 128, True)}
<g transform="translate(450 220)"><path d="M-66 70q-26-90 0-120 66-28 132 0 26 30 0 120z" class="violetp o"/>
  <path d="M-56-40q56-16 112 0" fill="none" stroke="{VIO}" stroke-width="5"/>
  <path d="M-50 20q50 16 100 0" fill="none" stroke="{VIO}" stroke-width="5"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(370,120),(540,130)])}
{ring(450, 220, 128)}''')

add('relaunch', '手を入れて、もう一度売り出す', f'''
{split()}
{box(150, 240, 130, 96, 28, 'teal')}
{ring(150, 210, 128, True)}
{box(450, 240, 130, 96, 28, 'coral')}
<g transform="translate(450 130)"><rect x="-60" y="-26" width="120" height="52" rx="12" class="gold o"/></g>
{''.join(spark(x, y, 0.9) for x, y in [(360,130),(550,150)])}
<path d="M300 350h1" fill="none"/>
{ring(450, 210, 138)}''')

add('reconciliation', '割れていた皿がつなぎ合わされ、もとにもどる', f'''
{table(340)}
{split()}
<g transform="translate(150 280) rotate(-10)"><path d="M-70-16q30-30 60 0-30 24-60 0z" fill="#fffefd" class="o"/></g>
<g transform="translate(160 300) rotate(20)"><path d="M0-14q34-24 66 6-34 22-66-6z" fill="#fffefd" class="o"/></g>
{ring(150, 270, 122, True)}
<g transform="translate(450 280)"><ellipse rx="100" ry="30" fill="#fffefd" class="o"/>
  <path d="M-40-24l14 24-10 22" fill="none" stroke="{GRN}" stroke-width="4"/>
  <path d="M30-22l-8 26 12 20" fill="none" stroke="{GRN}" stroke-width="4"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(370,150),(540,160)])}
{ring(450, 270, 128)}''')

add('redemption', '過ちを悔い、よい行いで償う', f'''
{head(140, 250, 34, 'violet', 'short')}
<g transform="translate(300 130)"><ellipse rx="110" ry="72" fill="#fffefd" class="o"/>
  <g opacity="0.7">{cloud(-20, -10, 1.0, 'violet')}</g>
  <path d="M-40 34l80-60" fill="none" stroke="{CRL}" stroke-width="6"/></g>
<circle cx="212" cy="212" r="9" fill="#fffefd" class="o"/>
<path d="M240 300h50" class="a" marker-end="url(#ar)"/>
{person(420, 306, 1.15, 1, 'violet', 'blue', 'give', 'short', 'neutral')}
{person(540, 306, 0.9, -1, 'coral', 'green', 'reach', 'bob', 'smile')}
{''.join(spark(x, y, 0.8) for x, y in [(400,140),(540,150)])}''', arrow=True)

add('redundancy', '席がいくつも空けられ、人がへらされる', f'''
{''.join(f'<g transform="translate({100+ (i%4)*130} {200+(i//4)*130})">'
         f'<rect x="-56" y="-30" width="112" height="26" rx="4" class="goldd o"/>'
         + (f'{chair(0, 40, 0.7, "gold", -1)}' if i in (1, 3, 5) else f'{chair(0, 40, 0.7, "gold", -1)}') + '</g>' for i in range(8))}
{''.join(f'<g transform="translate({100+ (i%4)*130} {170+(i//4)*130})">{head(0, 0, 22, c, h)}</g>'
         for i, (c, h) in zip([0, 2, 4, 7], [('teal','short'),('coral','bob'),('green','short'),('gold','bun')]))}
{''.join(f'<g transform="translate({100+ (i%4)*130} {170+(i//4)*130})"><circle r="24" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/></g>' for i in [1, 3, 5, 6])}''')

add('relocation', '事務所を、まるごと別の建物へ移す', f'''
<g transform="translate(120 306)">{building(0, 0, 0.7, 'teal')}</g>
<g transform="translate(490 306)">{building(0, 0, 0.7, 'coral')}</g>
<g transform="translate(300 300)"><path d="M-90 0v-50h110v50z" class="gold o"/>
  <path d="M20-36h48l26 36h-74z" class="goldp o"/>
  <circle cx="-50" cy="10" r="16" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="52" cy="10" r="16" fill="none" stroke="{INK}" stroke-width="6"/></g>
<path d="M200 160h200" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

# --- 気持ち・態度 -------------------------------------------------------------

add('reassurance', '心配する人に、だいじょうぶと声をかける', f'''
{person(180, 306, 1.2, 1, 'coral', 'blue', 'hold', 'bob', 'sad')}
{person(450, 306, 1.2, -1, 'teal', 'blue', 'reach', 'short', 'smile')}
<path d="M390 214l-70 10" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(330 120)"><rect x="-90" y="-46" width="180" height="92" rx="22" class="paper"/>
  <path d="M60 42l26 30-44-30z" class="paper"/>
  <path d="M-40 6l24 26 46-54" fill="none" stroke="{GRN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></g>
{drop(140, 200, 0.9)}''')

add('readiness', '荷物をそろえ、いつでも出られるようにしておく', f'''
<g transform="translate(430 306)"><path d="M-100 0v-210h200V0z" fill="#fffefd" class="o"/>
  <path d="M-80 0v-190h160V0z" class="goldp o"/><circle cx="52" cy="-96" r="8" class="ink"/></g>
<g transform="translate(230 290)"><path d="M-56 16v-70h112v70z" class="violet o"/>
  <path d="M-24-54v-16h48v16" fill="none" class="a"/></g>
<g transform="translate(150 300)"><path d="M-30-40h60v40h-60z" class="teald o"/>
  <path d="M-16-40v-16h32v16z" class="teal o"/></g>
{person(120, 200, 0.9, 1, 'teal', 'blue', 'stand', 'cap', 'smile')}
{''.join(spark(x, y, 0.7) for x, y in [(320,130),(540,140)])}''')

add('reluctantly', 'いやそうな顔で、しぶしぶ受け取る', f'''
{person(430, 306, 1.15, -1, 'violet', 'blue', 'give', 'bun', 'neutral')}
{box(300, 230, 80, 58, 18, 'gold')}
{person(150, 306, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'sad')}
<path d="M124 190l16 6M176 190l-16 6" fill="none" stroke="{INK}" stroke-width="3.5"/>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M90 250h-30M100 300h-40"/></g>
<path d="M230 240h-40" class="a" stroke="{MUTED}" marker-end="url(#ar)"/>''', arrow=True)

add('refrain', 'すすめられても、あえて手を出さないでおく', f'''
{person(430, 306, 1.15, -1, 'coral', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(320 230)"><path d="M-24 0v-50h48V0z" class="green o"/>
  <path d="M-12-50v-16h24v16z" class="greend o"/></g>
{person(140, 306, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'neutral')}
{hand(230, 220, 1)}
<g transform="translate(230 220)"><circle r="40" fill="none" stroke="{CRL}" stroke-width="9"/>
  <path d="M-24 0h48" stroke="{CRL}" stroke-width="9" stroke-linecap="round" fill="none"/></g>''')

add('put your foot down', '床を強くふんで、断固として反対する', f'''
{person(220, 306, 1.35, 1, 'coral', 'blue', 'point', 'short', 'neutral')}
<g class="corals" stroke-width="6">{''.join(f'<path d="M220 340v20" transform="rotate({d} 240 340)"/>' for d in [-40, 0, 40])}</g>
<path d="M190 190l16 6M250 190l-16 6" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(440 200)"><rect x="-90" y="-110" width="180" height="220" rx="8" class="paper"/>
  {''.join(f'<rect x="-66" y="{-80+i*46}" width="{130-(i%2)*40}" height="14" rx="7" fill="{MUTED}"/>' for i in range(4))}</g>
<g transform="translate(340 200)"><circle r="34" fill="none" stroke="{CRL}" stroke-width="9"/>
  <path d="M-20 0h40" stroke="{CRL}" stroke-width="9" stroke-linecap="round" fill="none"/></g>''')

add('pull your weight', 'ひとりも手を抜かず、みんなで同じだけ引く', f'''
<path d="M60 230h480" fill="none" stroke="{GLDD}" stroke-width="12"/>
{''.join(f'<g transform="translate({110+i*110} 306)">{person(0, 0, 1.05, 1, c, "blue", "reach", h, "neutral")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun'),('green','cap')]))}
{''.join(f'<path d="M{110+i*110} 130v40" class="a" stroke-width="5" marker-end="url(#ar)"/>' for i in range(4))}
{''.join(f'<path d="M{80+i*110} 100h60" fill="none" stroke="{GRN}" stroke-width="6"/>' for i in range(4))}''', arrow=True)

add('react to', '押されたとたん、すぐさま反応が返る', f'''
{hand(120, 200, 1)}
<path d="M190 200h60" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(320 200)"><rect x="-50" y="-50" width="100" height="100" rx="12" class="teal o"/>
  <circle r="22" fill="#fffefd" class="o"/></g>
<path d="M390 200h60" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(510 200)"><circle r="34" class="coral o"/>
  {''.join(f'<path d="M0 -50v-22" transform="rotate({d})" fill="none" stroke="{CRL}" stroke-width="5"/>' for d in range(0, 360, 45))}</g>''', arrow=True)

# --- 記憶・清算 ---------------------------------------------------------------

add('recollection', 'しまってあった記憶を、ひとつ引き出してくる', f'''
<g transform="translate(200 230)"><rect x="-140" y="-120" width="280" height="240" rx="8" fill="#c9a06c" class="o"/>
  {''.join(f'<g><rect x="-120" y="{-100+i*78}" width="240" height="66" rx="6" fill="#e0c99e" stroke="{INK}" stroke-width="2.5"/>'
           f'<circle cx="0" cy="{-67+i*78}" r="8" class="goldd o"/></g>' for i in range(3))}
  <rect x="-120" y="-22" width="240" height="66" rx="6" fill="#eddcbb" stroke="{INK}" stroke-width="2.5" transform="translate(60 0)"/></g>
<g transform="translate(450 130)"><ellipse rx="110" ry="76" fill="#fffefd" class="o"/>
  {sun(-40, -26, 22)}{tree(46, 40, 0.5)}</g>
<path d="M330 210q60-40 90-20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('reckoning', '帳尻を合わせる日が来て、つけを払う', f'''
{table(300)}
{doc(200, 200, 200, 240, 0)}
{''.join(f'<g><rect x="120" y="{110+i*46}" width="100" height="12" rx="6" fill="{MUTED}"/>'
         f'<rect x="236" y="{110+i*46}" width="48" height="12" rx="6" class="coral"/></g>' for i in range(3))}
<path d="M110 270h180" fill="none" stroke="{INK}" stroke-width="4"/>
<rect x="200" y="286" width="84" height="16" rx="8" class="coral"/>
<path d="M330 250h50" class="a" marker-end="url(#ar)"/>
{''.join(coin(430 + i*44, 250, 24) for i in range(2))}
{head(520, 350, 24, 'teal', 'short')}''', arrow=True)

add('put aside', '使わずに取っておいて、びんにためる', f'''
{table(340)}
<g transform="translate(400 300)"><path d="M-70 0v-140q0-24 16-34v-20h108v20q16 10 16 34V0z" fill="#eaf4fb" class="o"/>
  <path d="M-64-90h128v86h-128z" class="goldp"/>
  {''.join(coin(-30 + (i%3)*30, -30 - (i//3)*26, 16) for i in range(6))}</g>
{coin(200, 150, 26)}
<path d="M240 180l80 40" class="a" marker-end="url(#ar)"/>
{hand(160, 120, 1)}''', arrow=True)

# --- 読み・語り ---------------------------------------------------------------

add('readership', 'その新聞を読んでいる、大勢の人たち', f'''
<g transform="translate(300 130)"><rect x="-120" y="-90" width="240" height="180" rx="4" class="paper"/>
  <rect x="-96" y="-66" width="192" height="18" rx="9" class="coral"/>
  {''.join(f'<rect x="-96" y="{-30+i*30}" width="{170-(i%2)*50}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}</g>
{''.join(f'<g transform="translate({70+ (i%6)*90} {290+(i//6)*70})">{head(0, 0, 26, c, h)}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun'),('green','short'),('violet','cap'),('blue','bob'),
                                     ('coral','short'),('teal','bob'),('gold','short'),('green','bun'),('violet','short'),('blue','cap')]))}
{''.join(f'<path d="M{110+i*90} 250L300 230" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 7"/>' for i in range(5))}''')

add('pundit', 'テレビで、専門の立場から解説する人', f'''
<g transform="translate(400 190)"><rect x="-160" y="-120" width="320" height="240" rx="12" class="teald o"/>
  <rect x="-140" y="-100" width="280" height="200" rx="6" fill="#dfe6ea"/>
  {head(400, 150, 30, 'violet', 'bun')}
  <rect x="-110" y="46" width="220" height="20" rx="10" class="coral"/></g>
<g transform="translate(150 200)"><rect x="-90" y="-60" width="180" height="120" rx="20" class="paper"/>
  <path d="M70 56l30 34-48-34z" class="paper"/>
  {''.join(f'<rect x="-64" y="{-30+i*26}" width="{120-(i%2)*36}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}</g>''')

add('realism', '目に映るとおりを、そのまま写しとる絵', f'''
<g transform="translate(150 200)"><path d="M-100 90l70-110 50 56 44-64 66 118z" fill="#c3cbd1" class="o"/>
  {sun(60, -50, 24)}</g>
<path d="M270 200h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(450 200)"><rect x="-120" y="-120" width="240" height="240" rx="6" class="goldd o"/>
  <rect x="-100" y="-100" width="200" height="200" fill="#f7f3e8"/>
  <path d="M-100 80l60-96 44 48 38-56 58 104z" fill="#c3cbd1" class="o"/>
  {sun(50, -44, 20)}</g>
{''.join(spark(x, y, 0.7) for x, y in [(300,110),(300,300)])}''')

add('qualifier', '本大会の前に行う、勝ち抜きの試合', f'''
{''.join(f'<g transform="translate(80 {80+i*70})">{head(0, 0, 22, c, h)}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun')]))}
<g fill="none" stroke="{MUTED}" stroke-width="5">
  <path d="M116 80h50v70h-50M116 220h50v70h-50"/><path d="M166 115h50M166 255h50"/></g>
<rect x="46" y="46" width="190" height="290" rx="14" fill="none" stroke="{CRL}" stroke-width="5"/>
<g fill="none" stroke="{TEA}" stroke-width="6"><path d="M246 115h60v140h-60"/><path d="M306 185h60"/></g>
{head(410, 185, 28, 'teal', 'short')}
<g transform="translate(520 185)"><path d="M-40 40l10-60h60l10 60z" class="gold o"/>
  <path d="M-30-20q-30 0-30-30h30M30-20q30 0 30-30h-30" fill="none" stroke="{GLDD}" stroke-width="6"/></g>''')

# --- 音・光・純度 -------------------------------------------------------------

add('purr', 'ねこがのどをごろごろ鳴らす', f'''
{table(340)}
<g transform="translate(280 300)"><ellipse rx="96" ry="50" fill="#c9a06c" class="o"/>
  <circle cx="-76" cy="-44" r="36" fill="#c9a06c" class="o"/>
  <path d="M-104-70l-8-32 28 18zM-56-76l14-30 12 30z" fill="#c9a06c" class="o"/>
  <path d="M-90-46l14 6M-62-46l-14 6" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-84-30q8 8 16 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M92-16q44-20 34-64" fill="none" stroke="#c9a06c" stroke-width="16" stroke-linecap="round"/></g>
{''.join(f'<path d="M{400+i*30} {180+i*24}q16 16 0 32" fill="none" stroke="{MUTED}" stroke-width="5"/>' for i in range(3))}''')

add('rattle', 'ゆるんだ部品が、ガタガタ音を立てる', f'''
<g transform="translate(280 220)"><rect x="-140" y="-90" width="280" height="180" rx="12" class="teald o"/>
  <rect x="-116" y="-66" width="180" height="132" rx="6" fill="#dfe6ea"/>
  <g transform="translate(90 20) rotate(-16)"><rect x="-26" y="-26" width="52" height="52" rx="6" class="goldp o"/></g></g>
{''.join(f'<path d="M{430+i*26} {150+i*24}q16 16 0 32" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}
{''.join(f'<path d="M{100-i*20} {150+i*24}q-16 16 0 32" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}''')

add('radiance', 'まわりを照らすほど、明るく輝く', f'''
<g transform="translate(300 200)"><circle r="70" class="goldp o"/>
  <circle r="42" class="gold o"/></g>
{''.join(f'<path d="M300 100v-40" transform="rotate({d} 300 200)" fill="none" stroke="{GLD}" stroke-width="8" stroke-linecap="round"/>' for d in range(0, 360, 30))}
{''.join(f'<circle cx="300" cy="200" r="{130+i*40}" fill="none" stroke="{GLDP}" stroke-width="10" opacity="{0.5-i*0.14:.2f}"/>' for i in range(3))}''')

add('purity', 'まじりけのない水と、粒のまじった水の対比', f'''
{split()}
<g transform="translate(150 230)"><path d="M-60-110h120v220h-120z" fill="#eaf4fb" class="o"/>
  <path d="M-52-70h104v170h-104z" class="bluep"/>
  <path d="M-60-110h120v220h-120z" fill="none" class="o"/></g>
{ring(150, 230, 128)}
<g transform="translate(450 230)"><path d="M-60-110h120v220h-120z" fill="#eaf4fb" class="o"/>
  <path d="M-52-70h104v170h-104z" class="bluep"/>
  {''.join(f'<circle cx="{-34+ (i%4)*24}" cy="{-40+(i//4)*40}" r="{5+(i%3)*2}" fill="#8f9a72"/>' for i in range(12))}
  <path d="M-60-110h120v220h-120z" fill="none" class="o"/></g>
{ring(450, 230, 128, True)}''')

# --- 差別・弾圧 ---------------------------------------------------------------

add('racist', '見た目で人を分け、片方だけを締め出す', f'''
<path d="M300 60v300" fill="none" stroke="{INK}" stroke-width="8"/>
{''.join(f'<g transform="translate({390+ (i%2)*90} {200+(i//2)*100})">{head(0, 0, 28, "teal", "short")}</g>' for i in range(4))}
{''.join(f'<g transform="translate({90+ (i%2)*90} {200+(i//2)*100})">{head(0, 0, 28, "violet", "bob")}</g>' for i in range(2))}
<g transform="translate(300 300)"><circle r="40" fill="none" stroke="{CRL}" stroke-width="11"/>
  <path d="M-24 0h48" stroke="{CRL}" stroke-width="11" stroke-linecap="round" fill="none"/></g>
<path d="M200 200h60" fill="none" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
<path d="M270 200l-14-12M270 200l-14 12" fill="none" stroke="{CRL}" stroke-width="0"/>''', arrow=True)

# --- もの ---------------------------------------------------------------------

add('quilt', 'はぎ合わせた布を重ねてぬった、掛け布団', f'''
{table(360)}
<g transform="translate(300 220)"><rect x="-220" y="-130" width="440" height="260" rx="10" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="{-200+ (i%6)*70}" y="{-110+(i//6)*70}" width="60" height="60" rx="4" class="{c} o"/>'
           for i, c in enumerate(['coralp','tealp','goldp','violetp','greenp','bluep',
                                   'tealp','goldp','coralp','greenp','bluep','violetp',
                                   'goldp','coralp','violetp','bluep','tealp','greenp']))}
  <rect x="-220" y="-130" width="440" height="260" rx="10" fill="none" class="o"/></g>''')

add('radish', '葉つきの、赤くて丸い根', f'''
{table(340)}
<g transform="translate(300 280)">
  <path d="M0-30q-56 0-56 40t56 50 56-50-56-40z" class="coral o"/>
  <path d="M0 60v40" fill="none" stroke="#fffefd" stroke-width="6"/>
  <path d="M-30 0q30 16 60 0" fill="none" stroke="{CRLD}" stroke-width="4"/>
  {''.join(f'<path d="M0-30q-{30+i*10}-30-{20+i*14}-{60+i*20}q{40+i*10} {20} {24+i*14} {60+i*20}z" class="greenp o" transform="rotate({-30+i*30} 0 -30)"/>' for i in range(3))}</g>''')

add('relic', 'ガラスの箱におさめられた、大昔の遺物', f'''
{table(360)}
<g transform="translate(300 250)"><rect x="-150" y="-140" width="300" height="230" rx="6" fill="#eaf4fb" opacity="0.55" class="o"/>
  <rect x="-160" y="90" width="320" height="24" rx="4" class="goldd o"/></g>
<g transform="translate(300 250)"><path d="M-56 76q-24-90 0-110h112q24 20 0 110z" fill="#b58a58" class="o"/>
  <path d="M-60-34h120v-16h-120z" fill="#9a6f42" class="o"/>
  <path d="M-40-10q40 16 80 0" fill="none" stroke="#8a6238" stroke-width="4"/>
  <path d="M20 40l30 36" fill="none" stroke="#8a6238" stroke-width="4"/></g>
{''.join(spark(x, y, 0.7) for x, y in [(180,120),(430,120)])}''')

add('relaxation', 'ハンモックにゆられて、のんびり過ごす', f'''
{tree(90, 340, 1.1)}{tree(520, 340, 1.0)}
<path d="M110 200q190 140 380 0" fill="none" stroke="{GLDD}" stroke-width="10"/>
<path d="M110 200q190 120 380 0" fill="none" stroke="{GLDP}" stroke-width="26" opacity="0.9"/>
<g transform="translate(300 268)">
  <path d="M-120 0q120 40 240 0" fill="none" stroke="{GLDD}" stroke-width="0"/>
  <circle cx="-90" cy="-24" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(-90 84) scale(1.08)" fill="{HAIR}"/>
  <path d="M-104-30l14 6M-76-30l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-98-10q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-60-10q60-16 120 0l-6 20h-108z" fill="{TEA}" class="o"/></g>
{sun(500, 90, 40)}''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
