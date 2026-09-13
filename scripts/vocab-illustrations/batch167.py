# -*- coding: utf-8 -*-
"""第167回。re-/ri-/ro-/ru-/sa-/sc-/se- の名詞。"""
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

def flower(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 40V0" fill="none" stroke="{GRND}" stroke-width="5"/>'
            + ''.join(f'<ellipse cx="0" cy="-22" rx="11" ry="22" class="{cls} o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 72))
            + f'<circle r="11" class="ink"/></g>')

# --- 記憶・追悼 ---------------------------------------------------------------

add('remembrance', '胸に花をつけ、頭を下げて静かに思い出す', f'''
{''.join(f'<g transform="translate({120+i*120} 306)">'
         f'<path d="M-12-8l-6 30M10-8l6 30" fill="none" stroke="{TONES["blue"][2]}" stroke-width="12" stroke-linecap="round"/>'
         f'<path d="M-26-72q26-13 52 0l-8 66h-36z" fill="{TONES["blue"][0]}" class="o"/>'
         f'<circle cx="0" cy="-100" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
         f'<path d="{HAIRS[h]}" transform="translate(0 4)" fill="{HAIR}"/>'
         f'<path d="M-11-94l10 4M11-94l-10 4" fill="none" stroke="{INK}" stroke-width="2.5"/></g>'
         for i, h in enumerate(['short', 'bob', 'short', 'bun']))}
{''.join(flower(120 + i*120, 258, 0.5, 'coral') for i in range(4))}
<g transform="translate(300 100)"><rect x="-120" y="-40" width="240" height="60" rx="14" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/></g>''')

add('remnant', 'たっぷりあった布の、最後に残った一枚', f'''
{split()}
{table(340)}
{''.join(f'<g transform="translate(150 {296-i*22})"><rect x="-90" y="-16" width="180" height="24" rx="4" class="{c} o"/></g>'
         for i, c in enumerate(['coral','teal','gold','violet','green']))}
{ring(150, 250, 122, True)}
<g transform="translate(450 290) rotate(-8)"><rect x="-56" y="-16" width="112" height="24" rx="4" class="coral o"/></g>
{ring(450, 284, 84)}''')

add('retention', 'もれずにたまり、そのまま保たれている', f'''
{table(340)}
<g transform="translate(300 300)"><path d="M-80 0v-160h160V0z" fill="#fffefd" class="o"/>
  <path d="M-72-140h144v136h-144z" class="bluep"/>
  <path d="M-80 0v-160h160V0z" fill="none" class="o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M100 300h100M400 300h100"/></g>
<g transform="translate(140 200)"><circle r="34" fill="none" stroke="{GRN}" stroke-width="8"/>
  <path d="M-18 2l14 16 26-30" fill="none" stroke="{GRN}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>
{''.join(drop(300, 100 + i*40, 1.0) for i in range(2))}''')

add('retrospective', 'これまでの作品を、ひととおり並べて見せる', f'''
{''.join(f'<g transform="translate({100+ (i%5)*100} {170+(i//5)*130})"><rect x="-40" y="-46" width="80" height="92" rx="4" class="goldd o"/>'
         f'<rect x="-30" y="-36" width="60" height="72" fill="#f7f3e8"/>'
         + (f'<circle cx="0" cy="0" r="18" class="{c} o"/>' if i % 3 == 0 else
            f'<path d="M-20 20l20-36 20 36z" class="{c} o"/>' if i % 3 == 1 else
            f'<rect x="-18" y="-18" width="36" height="36" class="{c} o"/>') + '</g>'
         for i, c in enumerate(['coral','teal','gold','violet','green','blue','coral','teal','gold','violet']))}
<path d="M60 380h480" class="a" marker-end="url(#ar)"/>''', arrow=True)

# --- 取り消す・やり直す --------------------------------------------------------

add('retraction', '出した記事の主張を、あらためて取り下げる', f'''
<g transform="translate(160 190) rotate(-6)"><rect x="-100" y="-120" width="200" height="240" rx="4" class="paper"/>
  <rect x="-76" y="-90" width="150" height="16" rx="8" class="coral"/>
  {''.join(f'<rect x="-76" y="{-50+i*34}" width="{150-(i%2)*44}" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}</g>
<path d="M290 200h50" class="a" stroke="{CRL}" marker-end="url(#ar)"/>
<g transform="translate(450 190)"><rect x="-100" y="-120" width="200" height="240" rx="4" class="paper"/>
  <rect x="-76" y="-90" width="150" height="16" rx="8" fill="{MUTED}"/>
  <path d="M-76-82h150" stroke="{CRL}" stroke-width="6" fill="none"/>
  <rect x="-76" y="-40" width="150" height="16" rx="8" class="teal"/>
  {''.join(f'<rect x="-76" y="{0+i*34}" width="{150-(i%2)*44}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}</g>''', arrow=True)

add('revocation', '出していた許可が、取り消される', f'''
<g transform="translate(300 200) rotate(-4)"><rect x="-140" y="-100" width="280" height="200" rx="10" class="paper"/>
  <circle cx="-86" cy="-30" r="30" class="tealp o"/>
  {''.join(f'<rect x="-40" y="{-46+i*30}" width="{160-(i%2)*40}" height="14" rx="7" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="84" cy="54" r="28" fill="none" stroke="{MUTED}" stroke-width="5"/></g>
<g transform="translate(300 200)"><path d="M-160 90L160-70" stroke="{CRL}" stroke-width="14" stroke-linecap="round" fill="none"/></g>
<g transform="translate(500 90)"><path d="M-30 40h60v20h-60z" class="corald o"/>
  <path d="M-16-40h32v80h-32z" class="coral o"/><path d="M-30-56h60v18h-60z" class="corald o"/></g>''')

add('rethink', 'いったん止めて、もう一度はじめから考え直す', f'''
<g transform="translate(160 200)"><rect x="-100" y="-100" width="200" height="200" rx="10" class="paper"/>
  {''.join(f'<rect x="-76" y="{-66+i*40}" width="{150-(i%2)*40}" height="14" rx="7" fill="{MUTED}"/>' for i in range(4))}
  <path d="M-90-90l180 180M90-90L-90 90" fill="none" stroke="{CRL}" stroke-width="7"/></g>
<g transform="translate(320 200)"><path d="M-60 0a60 60 0 1 1 20 44" fill="none" class="a" stroke-width="7" marker-end="url(#ar)"/></g>
{head(480, 200, 38, 'teal', 'short')}
<g transform="translate(480 90)"><circle r="9" fill="#fffefd" class="o"/></g>''', arrow=True)

add('reversal', '流れがひっくり返って、逆向きになる', f'''
{split()}
<path d="M60 150h180" class="a" stroke="{TEA}" stroke-width="10" marker-end="url(#ar)"/>
{''.join(f'<rect x="{80+i*60}" y="{300-h}" width="40" height="{h}" rx="5" class="tealp o"/>' for i, h in enumerate([40, 80, 130]))}
{ring(150, 210, 130, True)}
<path d="M540 150h-180" class="a" stroke="{CRL}" stroke-width="10" marker-end="url(#ar)"/>
{''.join(f'<rect x="{360+i*60}" y="{300-h}" width="40" height="{h}" rx="5" class="coral o"/>' for i, h in enumerate([130, 80, 40]))}
{ring(450, 210, 130)}''', arrow=True)

# --- お金・償い ---------------------------------------------------------------

add('reparation', '与えた損害の埋め合わせに、金を払う', f'''
<g transform="translate(150 290)"><path d="M-70 16v-100h140v100z" fill="#fffefd" class="o"/>
  <path d="M-82-84h164l-22-30h-120z" class="corald o"/>
  <path d="M-40-60l20 30-16 20 20 24" fill="none" stroke="{CRL}" stroke-width="5"/>
  <path d="M20-56l-12 30 16 22" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{person(500, 306, 1.15, -1, 'violet', 'blue', 'give', 'short', 'neutral')}
{''.join(coin(300 + i*44, 220, 24) for i in range(3))}
<path d="M400 160h-120" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('repayment', '借りた分を、毎月ずつ返していく', f'''
<g transform="translate(150 200)"><rect x="-90" y="-70" width="180" height="140" rx="8" class="paper"/>
  {''.join(f'<rect x="-66" y="{-44+i*30}" width="{130-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="46" cy="42" r="18" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{''.join(f'<g transform="translate({290+i*70} 200)">{coin(0, 0, 26)}</g>' for i in range(4))}
{''.join(f'<path d="M{320+i*70} 260v30" class="a" marker-end="url(#ar)"/>' for i in range(4))}
<g transform="translate(300 340)"><rect x="-40" y="-16" width="360" height="32" rx="8" fill="#dfe6ea" class="o"/></g>''', arrow=True)

add('renewal', '期限の切れた証を、新しい日付にする', f'''
{split()}
<g transform="translate(150 200) rotate(-6)"><rect x="-100" y="-64" width="200" height="128" rx="10" class="paper"/>
  <circle cx="-60" cy="-16" r="24" fill="#dfe6ea" class="o"/>
  <rect x="-20" y="-30" width="106" height="12" rx="6" fill="{MUTED}"/>
  <rect x="-20" y="4" width="70" height="12" rx="6" class="coral"/>
  <path d="M-20 10h70" stroke="{CRL}" stroke-width="5" fill="none"/></g>
{ring(150, 200, 130, True)}
<g transform="translate(450 200) rotate(-6)"><rect x="-100" y="-64" width="200" height="128" rx="10" class="paper"/>
  <circle cx="-60" cy="-16" r="24" class="tealp o"/>
  <rect x="-20" y="-30" width="106" height="12" rx="6" fill="{MUTED}"/>
  <rect x="-20" y="4" width="70" height="12" rx="6" class="teal"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(370,110),(540,130)])}
{ring(450, 200, 130)}''')

add('renovation', '足場を組んで、古い建物を直して new にする', f'''
{split()}
<g transform="translate(150 306)"><path d="M-90 0v-130h180V0z" fill="#e3ded1" class="o"/>
  <path d="M-104-130L0-196l104 66z" fill="#b8ab92" class="o"/>
  <path d="M-30 0v-64h60V0z" fill="#a89a80" class="o"/>
  <path d="M-70-110h40v34h-40z" fill="#cfc7b4"/></g>
{''.join(f'<path d="M{70+i*80} 306v-180M60 {160+i*60}h180" fill="none" stroke="{GLDD}" stroke-width="6"/>' for i in range(2))}
{ring(150, 220, 138, True)}
{house(450, 306, 0.9, 'coral')}
{''.join(spark(x, y, 0.8) for x, y in [(370,120),(540,130)])}
{ring(450, 220, 138)}''')

# --- 名声・敬い ---------------------------------------------------------------

add('renown', 'その名を、だれもが知っている', f'''
{person(300, 306, 1.3, 1, 'violet', 'blue', 'stand', 'bun', 'smile')}
{''.join(spark(x, y, 1.0) for x, y in [(200,110),(400,100),(160,220),(440,210)])}
{''.join(f'<g transform="translate({x} 350)">{head(0, 0, 24, c, h)}</g>' for x, (c, h) in
  zip([60, 130, 470, 540], [('teal','short'),('coral','bob'),('green','short'),('gold','cap')]))}
{''.join(f'<path d="M{100+i*40} 300l{60-i*20} -40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>' for i in range(2))}
{''.join(f'<path d="M{440-i*40} 300l{-60+i*20} -40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7"/>' for i in range(2))}''')

add('reverence', '深く頭を下げて、うやまう気持ちをあらわす', f'''
<g transform="translate(300 250)"><path d="M-70 56v-70h140v70z" fill="#fffefd" class="o"/>
  <path d="M-84-14L0-90l84 76z" class="corald o"/>
  <path d="M0-92v-30M-18-112h36" fill="none" stroke="{GLDD}" stroke-width="7" stroke-linecap="round"/></g>
{''.join(f'<g transform="translate({130+i*170} 380)">'
         f'<path d="M-12-8l-6 26M10-8l6 26" fill="none" stroke="{TONES["blue"][2]}" stroke-width="11" stroke-linecap="round"/>'
         f'<path d="M-24-64q24-12 48 0l-8 58h-32z" fill="{TONES["teal"][0]}" class="o"/>'
         f'<circle cx="0" cy="-88" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
         f'<path d="{HAIRS["short"]}" transform="translate(0 20) scale(0.92)" fill="{HAIR}"/>'
         f'<path d="M-10-84l9 4M10-84l-9 4" fill="none" stroke="{INK}" stroke-width="2.5"/></g>' for i in range(3))}
{''.join(spark(x, y, 0.8) for x, y in [(120,120),(490,120)])}''')

add('rivalry', 'たがいを意識しながら、競り合って走る', f'''
<path d="M0 340h600v60H0z" class="ground"/>
{''.join(f'<path d="M0 {360+i*20}h600" fill="none" stroke="#ffffff" stroke-width="4" stroke-dasharray="26 22"/>' for i in range(2))}
{person(230, 340, 1.2, 1, 'coral', 'blue', 'walk', 'cap', 'neutral', 'walk')}
{person(360, 340, 1.2, 1, 'teal', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8">
  <path d="M270 210h50"/></g>
{''.join(f'<path d="M{150-i*30} {230+i*40}h-40" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(2))}
{''.join(spark(x, y, 0.7) for x, y in [(300,140)])}''')

# --- からだ ------------------------------------------------------------------

add('respiration', '息を吸って吐く、そのくり返し', f'''
{torso(300, 300, 1.0)}
<g transform="translate(300 210)"><path d="M-14-70h28v50h-28z" class="tealp o"/>
  <path d="M-14-20q-60 0-60 60t34 60 26-50zM14-20q60 0 60 60t-34 60-26-50z" class="tealp o"/></g>
<path d="M230 70v60" class="a" stroke="{BLU}" stroke-width="6" marker-end="url(#ar)"/>
<path d="M370 130v-60" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(500 200)"><path d="M-46 0a46 46 0 1 1 16 34" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/></g>''', arrow=True)

add('secretion', '腺から、液がじわりとしみ出す', f'''
{torso(300, 300, 1.0)}
<g transform="translate(300 200)"><ellipse rx="44" ry="32" class="violet o"/>
  {''.join(f'<circle cx="{-22+i*22}" cy="{-6+(i%2)*14}" r="9" class="violetp o"/>' for i in range(3))}
  <path d="M0 32v34" fill="none" stroke="{VIOD}" stroke-width="6"/></g>
{''.join(drop(292 + i*16, 250 + i*26, 1.0, 'blue') for i in range(3))}
<path d="M300 340h-1" fill="none"/>
{ring(300, 250, 116)}''')

add('sedation', '薬でしずめて、落ち着いた状態にする', f'''
{split()}
{person(150, 306, 1.15, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
{''.join(f'<path d="M{80+i*140} 170q16-20 0-40" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{ring(150, 210, 122, True)}
<g transform="translate(300 340) rotate(-24)"><path d="M-14-50h28v80h-28z" fill="#fffefd" class="o"/>
  <path d="M-8 30h16v20h-16z" class="blue o"/><path d="M0 50v30" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-14-50h28v-14h-28z" class="blued o"/></g>
{sit(450, 340, 1.15, 1, 'teal', 'blue', 'short', 'neutral', 'lap')}
{chair(464, 340, 1.05, 'gold', -1)}
<path d="M430 236l14 6M470 236l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
{ring(450, 240, 122)}''')

# --- しみ込む・たまる ---------------------------------------------------------

add('saturation', 'これ以上は吸えず、あふれ出す', f'''
{table(340)}
<g transform="translate(300 280)"><rect x="-110" y="-60" width="220" height="80" rx="10" fill="{BLUP}" class="o"/>
  {''.join(f'<circle cx="{-84+ (i%6)*34}" cy="{-38+(i//6)*32}" r="10" fill="{BLU}" opacity="0.7"/>' for i in range(12))}</g>
{''.join(drop(300 + (i-1)*24, 150 + (i%2)*20, 1.0) for i in range(3))}
{''.join(drop(160 + i*300, 320 + i*10, 1.0) for i in range(2))}
<g transform="translate(300 350)"><ellipse rx="130" ry="16" fill="{BLUP}" class="o"/></g>''')

add('sediment', 'びんの底に、細かい粒がしずんでたまる', f'''
{table(340)}
<g transform="translate(300 300)"><path d="M-60 0v-140q0-22 14-32v-24h92v24q14 10 14 32V0z" fill="#eaf4fb" class="o"/>
  <path d="M-54-140h108v136h-108z" class="bluep"/>
  <path d="M-54-30q54-16 108 0v26h-108z" fill="#8f9a72"/>
  {''.join(f'<circle cx="{-34+ (i%5)*18}" cy="{-16+(i//5)*12}" r="4" fill="#6f7a54"/>' for i in range(10))}
  <path d="M-60 0v-140q0-22 14-32v-24h92v24q14 10 14 32V0z" fill="none" class="o"/></g>
{ring(300, 290, 84)}''')

add('scarcity', '棚が空になり、長い列だけが残る', f'''
<g transform="translate(400 306)"><path d="M-140 0v-190h280V0z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M-120 {-150+i*50}h240v12h-240z" class="goldd o"/>' for i in range(3))}
  <g opacity="0.4"><rect x="-100" y="-190" width="30" height="40" rx="3" class="tealp o"/></g></g>
{''.join(f'<g transform="translate({40+i*50} 350)">{head(0, 0, 20, c, h)}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun'),('green','short'),('violet','cap')]))}
<g transform="translate(120 130)"><path d="M0-34l34 58h-68z" class="gold o"/>
  <path d="M0-12v12" fill="none" stroke="{INK}" stroke-width="4"/><circle cy="14" r="3" class="ink"/></g>''')

# --- 抑える・救う -------------------------------------------------------------

add('repression', 'わき上がる気持ちを、ふたをして押しこめる', f'''
{torso(300, 300, 1.0)}
<g transform="translate(300 240)"><rect x="-80" y="-40" width="160" height="110" rx="10" class="teald o"/>
  <path d="M-92-40h184v-18h-184z" class="teal o"/>
  {''.join(f'<path d="M{-46+i*46} 0q14-20 0-40" fill="none" stroke="{CRL}" stroke-width="6"/>' for i in range(3))}</g>
<path d="M300 130v40" class="a" stroke="{INK}" stroke-width="8" marker-end="url(#ar)"/>
{''.join(f'<path d="M{200+i*200} 200q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''', arrow=True)

add('salvation', '沈みかけたところを、手が引き上げる', f'''
<path d="M0 240h600v160H0z" fill="{BLU}"/>
{''.join(f'<path d="M{-20+i*90} 260q45-30 90 0" fill="none" stroke="#fffefd" stroke-width="5" opacity="0.6"/>' for i in range(8))}
{head(300, 240, 30, 'coral', 'short')}
{hand(300, 150, 1)}
<path d="M300 190v40" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<path d="M300 110v-50" class="a" stroke-width="6" marker-end="url(#ar)"/>
{''.join(spark(x, y, 0.9) for x, y in [(180,110),(430,100)])}''', arrow=True)

add('sanctuary', 'さくで守られ、生きものが安心して暮らす場所', f'''
<path d="M0 240q140-20 300-14t300 14v160H0z" class="greenp o"/>
{''.join(f'<path d="M{40+i*70} 250v100" fill="none" stroke="{GLDD}" stroke-width="8"/>' for i in range(9))}
<path d="M40 270h520M40 320h520" fill="none" stroke="{GLDD}" stroke-width="7"/>
<g transform="translate(220 360) scale(0.4)">{beast(0, 0, 1, '#8a6a48', 1)}</g>
<g transform="translate(430 350)"><ellipse rx="40" ry="26" class="blue o"/>
  <circle cx="30" cy="-22" r="18" class="blue o"/>
  <path d="M44-24l22 6-20 10z" class="gold o"/><circle cx="34" cy="-26" r="4" class="ink"/></g>
{tree(90, 250, 0.7)}{tree(530, 250, 0.6)}
<g transform="translate(300 130)"><path d="M0-70q40 16 56 22 0 60-56 86-56-26-56-86 16-6 56-22z" class="tealp o"/></g>''')

add('respite', '降りやんだ合間に、ひと息つく', f'''
{cloud(140, 80, 1.4, 'violet')}{cloud(470, 80, 1.4, 'violet')}
{''.join(f'<path d="M{60+i*30} {150+(i%3)*20}l-14 40" fill="none" stroke="{BLU}" stroke-width="5"/>' for i in range(5))}
{''.join(f'<path d="M{440+i*30} {150+(i%3)*20}l-14 40" fill="none" stroke="{BLU}" stroke-width="5"/>' for i in range(5))}
{sun(300, 110, 40)}
{sit(300, 340, 1.15, 1, 'teal', 'blue', 'short', 'smile', 'lap')}
{chair(314, 340, 1.05, 'gold', -1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"><path d="M220 240h160"/></g>''')

# --- 音・光 ------------------------------------------------------------------

add('resonance', '一方をたたくと、もう一方まで鳴りだす', f'''
{''.join(f'<g transform="translate({x} 280)"><path d="M-30-120v90q0 30 30 30t30-30v-90" fill="none" stroke="#9aa6ae" stroke-width="14"/>'
         f'<path d="M0 0v40" stroke="#9aa6ae" stroke-width="14"/><path d="M-24 40h48v14h-48z" class="goldd o"/></g>' for x in [180, 420])}
{''.join(f'<path d="M{230+i*20} {180-i*20}q{20+i*20} {20+i*20} 0 {(20+i*20)*2}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(3))}
{''.join(f'<path d="M{370-i*20} {180-i*20}q-{20+i*20} {20+i*20} 0 {(20+i*20)*2}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" opacity="0.7"/>' for i in range(2))}
{hand(110, 200, 1)}''')

add('rustle', '風に葉がふれあって、かさかさ鳴る', f'''
{tree(300, 340, 1.6)}
{''.join(f'<path d="M{90+i*20} {160+i*24}q-16 16 0 32" fill="none" stroke="{MUTED}" stroke-width="5"/>' for i in range(3))}
{''.join(f'<path d="M{480-i*20} {160+i*24}q16 16 0 32" fill="none" stroke="{MUTED}" stroke-width="5"/>' for i in range(3))}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M60 120h90M50 170h70"/></g>
{''.join(f'<path d="M{380+i*40} {230+i*30}q-20-20-6-40" fill="none" stroke="{GRND}" stroke-width="4"/>' for i in range(2))}''')

add('ring up', '受話器を取って、電話をかける', f'''
{person(180, 306, 1.25, 1, 'teal', 'blue', 'hold', 'bob', 'smile')}
<g transform="translate(226 200) rotate(-20)"><rect x="-14" y="-40" width="28" height="80" rx="12" class="teald o"/>
  <circle cy="-46" r="14" class="teald o"/><circle cy="46" r="14" class="teald o"/></g>
<g transform="translate(430 300)"><path d="M-70 0v-56h140V0z" fill="#dfe6ea" class="o"/>
  <path d="M-66-56q0-36 66-36t66 36z" fill="#c3ccd2" class="o"/>
  <path d="M-52-70h104v20h-104z" class="ink"/>
  {''.join(f'<circle cx="{-40+ (i%3)*40}" cy="{-30+(i//3)*22}" r="8" class="ink"/>' for i in range(6))}</g>
{''.join(f'<path d="M{330+i*22} {150+i*22}q16 16 0 32" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}''')

# --- 硬さ・厳しさ -------------------------------------------------------------

add('rigidity', 'ちょうつがいが固まって、まったく動かない', f'''
{split()}
<g transform="translate(150 210)"><path d="M-90-70h60v140h-60z" class="goldd o"/>
  <g transform="rotate(-40 -30 0)"><path d="M-30-70h120v140h-120z" class="goldp o"/></g>
  <circle cx="-30" cy="0" r="14" class="ink"/></g>
<path d="M110 130a70 70 0 0 1 50 20" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>
{ring(150, 210, 132, True)}
<g transform="translate(450 210)"><path d="M-90-70h60v140h-60z" class="goldd o"/>
  <path d="M-30-70h120v140h-120z" class="goldp o"/>
  <circle cx="-30" cy="0" r="14" class="ink"/></g>
<g transform="translate(450 100)"><circle r="30" fill="none" stroke="{CRL}" stroke-width="8"/>
  <path d="M-18 0h36" stroke="{CRL}" stroke-width="8" stroke-linecap="round" fill="none"/></g>
{ring(450, 210, 132)}''', arrow=True)

add('rigour', 'こまかい目もりまで、きっちり測って確かめる', f'''
{table(340)}
<g transform="translate(240 260)"><rect x="-100" y="-40" width="200" height="46" rx="6" class="tealp o"/>
  <path d="M-70-40v-70h140v70z" fill="#dfe6ea" class="o"/>
  {''.join(f'<rect x="{-50+i*30}" y="-96" width="20" height="20" rx="3" class="teal o"/>' for i in range(4))}</g>
<g transform="translate(430 240) rotate(10)"><rect x="-24" y="-120" width="48" height="240" rx="6" class="goldp o"/>
  {''.join(f'<path d="M-24 {-104+i*24}h{24 if i%2 else 14}" fill="none" stroke="{GLDD}" stroke-width="3"/>' for i in range(10))}</g>
<g transform="translate(120 140)"><circle r="46" fill="#ffffff" opacity="0.2" stroke="{INK}" stroke-width="6"/>
  <path d="M32 32l28 28" stroke="{INK}" stroke-width="12" stroke-linecap="round"/></g>''')

add('richness', '層が重なった、こくのある一皿', f'''
{table(340)}
<g transform="translate(300 290)"><path d="M-110 0q0 30 110 30t110-30z" fill="#fffefd" class="o"/>
  <ellipse cy="0" rx="110" ry="30" fill="#b06a2c" class="o"/>
  <ellipse cy="-6" rx="80" ry="20" fill="#c98040"/>
  <ellipse cy="-10" rx="46" ry="12" fill="#e0a05a"/></g>
{''.join(f'<path d="M{240+i*60} 190q-16-26 0-46 16-24 0-44" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}
{''.join(spark(x, y, 0.7) for x, y in [(130,150),(490,150)])}''')

# --- 人・名簿 ----------------------------------------------------------------

add('respondent', 'アンケートに答えを書きこんでいる人', f'''
{table(300)}
{doc(300, 220, 200, 240, 0)}
{''.join(f'<g><circle cx="220" cy="{120+i*50}" r="10" fill="none" stroke="{INK}" stroke-width="3"/>'
         f'<rect x="244" y="{112+i*50}" width="{130-(i%2)*40}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(4))}
<circle cx="220" cy="170" r="10" class="coral o"/>
{person(120, 380, 1.2, 1, 'teal', 'blue', 'reach', 'bob', 'neutral')}
<g transform="translate(390 180) rotate(28)"><path d="M-8-70h16v90l-8 16-8-16z" class="coral o"/></g>
{ring(120, 280, 122)}''')

add('roster', '登録した顔ぶれを、役ごとに並べた表', f'''
<g transform="translate(300 200)"><rect x="-250" y="-150" width="500" height="300" rx="10" class="paper"/>
  <rect x="-250" y="-150" width="500" height="46" rx="0" class="teal o"/>
  {''.join(f'<path d="M-250 {-104+i*50}h500" fill="none" stroke="#dde4e8" stroke-width="3"/>' for i in range(5))}
  {''.join(f'<g transform="translate(-200 {-80+i*50})">{head(0, 0, 18, c, h)}</g>'
           for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun'),('green','short'),('violet','cap')]))}
  {''.join(f'<rect x="-160" y="{-88+i*50}" width="140" height="14" rx="7" fill="{MUTED}"/>'
           f'<rect x="20" y="{-88+i*50}" width="{100-(i%2)*30}" height="14" rx="7" class="tealp"/>' for i in range(5))}</g>''')

add('rota', '曜日ごとに、当番が順に回ってくる表', f'''
<g transform="translate(300 200)"><rect x="-250" y="-140" width="500" height="280" rx="10" class="paper"/>
  <rect x="-250" y="-140" width="500" height="46" rx="0" class="coral o"/>
  {''.join(f'<path d="M{-180+i*90} -140v280" fill="none" stroke="#dde4e8" stroke-width="3"/>' for i in range(5))}
  {''.join(f'<path d="M-250 {-50+i*62}h500" fill="none" stroke="#dde4e8" stroke-width="3"/>' for i in range(3))}
  {''.join(f'<g transform="translate({-215+ (i%5)*90} {-80+(i//5)*62})">{head(0, 0, 18, c, h)}</g>'
           for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun'),('green','short'),('violet','cap'),
                                        ('coral','bob'),('gold','bun'),('green','short'),('violet','cap'),('teal','short'),
                                        ('gold','bun'),('green','short'),('violet','cap'),('teal','short'),('coral','bob')]))}</g>
<g transform="translate(300 380)"><path d="M-70 0a70 24 0 1 1 24 18" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/></g>''', arrow=True)

add('repatriation', '飛行機で、自分の国へ送り返される', f'''
<path d="M300 60v300" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="16 12"/>
<g transform="translate(150 130)"><path d="M0 0v-90" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M0-90h70l-16 22 16 22H0z" class="teal o"/></g>
<g transform="translate(460 130)"><path d="M0 0v-90" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M0-90h70l-16 22 16 22H0z" class="coral o"/></g>
{plane(300, 230, 0.42, 180, 'gold')}
<path d="M380 300h-160" class="a" stroke-width="6" marker-end="url(#ar)"/>
{person(120, 340, 1.05, 1, 'violet', 'blue', 'up', 'short', 'smile')}
{head(180, 320, 22, 'teal', 'bob')}''', arrow=True)

# --- 図・書きもの -------------------------------------------------------------

add('schematic', '見た目ではなく、つながりだけを描いた図', f'''
{''.join(f'<rect x="{80+ (i%3)*180}" y="{110+(i//3)*140}" width="110" height="70" rx="6" fill="none" stroke="{INK}" stroke-width="4"/>' for i in range(6))}
{''.join(f'<circle cx="{135+ (i%3)*180}" cy="{145+(i//3)*140}" r="{16 if i%2 else 0}" class="teal o"/>' for i in range(6))}
<g fill="none" stroke="{INK}" stroke-width="4">
  <path d="M190 145h70M370 145h70M135 180v70h360v-70"/>
  <path d="M190 285h70M370 285h70"/>
  <path d="M135 320v40h180"/></g>''')

add('scripture', '台にのせて開かれた、古くから伝わる聖典', f'''
{table(360)}
<g transform="translate(300 320)"><path d="M-120 0l30-40h180l30 40z" class="goldd o"/></g>
<g transform="translate(300 250)"><path d="M-160 30q80-30 156-10v-130q-80-20-156 10z" fill="#f3ead6" class="o"/>
  <path d="M160 30q-80-30-156-10v-130q80-20 156 10z" fill="#f3ead6" class="o"/>
  <path d="M-4-110v130" fill="none" stroke="{MUTED}" stroke-width="3"/>
  {''.join(f'<path d="M-136 {-76+i*30}q66-16 124-6" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(4))}
  {''.join(f'<path d="M136 {-76+i*30}q-66-16-124-6" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(4))}</g>
{''.join(spark(x, y, 0.8) for x, y in [(130,120),(480,120)])}''')

add('secrecy', '中身を金庫にしまい、口外しない', f'''
<g transform="translate(400 240)"><rect x="-110" y="-110" width="220" height="220" rx="10" fill="#9aa6ae" class="o"/>
  <rect x="-86" y="-86" width="172" height="172" rx="6" fill="#c3ccd2" class="o"/>
  <circle cx="30" cy="0" r="30" fill="none" stroke="{INK}" stroke-width="8"/>
  {''.join(f'<path d="M30 0l{40*math.cos(math.radians(a)):.0f} {40*math.sin(math.radians(a)):.0f}" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>' for a in range(0, 360, 90))}
  <rect x="-70" y="-40" width="60" height="80" rx="4" class="paper"/></g>
{head(150, 250, 40, 'teal', 'short')}
<path d="M150 280v-6" fill="none"/>
<g transform="translate(150 288)"><path d="M-4-40v70" stroke="{SKIN}" stroke-width="12" stroke-linecap="round" fill="none"/></g>
<path d="M132 272h36" fill="none" stroke="{INK}" stroke-width="4"/>''')

add('seasoning', '仕上げに、塩やこしょうをふる', f'''
{table(330)}
<g transform="translate(380 290)"><ellipse rx="96" ry="26" fill="#fffefd" class="o"/>
  <ellipse cy="-12" rx="60" ry="22" class="goldp o"/></g>
{''.join(f'<g transform="translate({170+i*70} 170) rotate({20-i*40})">'
         f'<path d="M-24 60v-70q0-20 24-30 24 10 24 30v70z" fill="#eaf4fb" class="o"/>'
         f'<path d="M-16-92h32v20h-32z" class="{c} o"/>'
         f'{"".join(f2 for f2 in ["<circle cx=@" + str(-8+j*8) + "@ cy=@-84@ r=@2.5@ fill=@" + INK + "@/>" for j in range(3)])}</g>'.replace('@', chr(34))
         for i, c in enumerate(['goldd', 'teald']))}
{''.join(f'<circle cx="{300+ (i%5)*24}" cy="{220+(i//5)*18}" r="3" fill="{MUTED}"/>' for i in range(10))}''')

add('sabbatical', '長い休みを取って、しばらく職場を離れる', f'''
<g transform="translate(160 190)"><rect x="-120" y="-120" width="240" height="240" rx="10" class="paper"/>
  <rect x="-120" y="-120" width="240" height="44" rx="0" class="teal o"/>
  {''.join(f'<rect x="{-100+ (i%4)*54}" y="{-56+(i//4)*54}" width="42" height="42" rx="5" fill="#f7e2c8" stroke="{INK}" stroke-width="2"/>' for i in range(12))}
  <rect x="-106" y="-62" width="212" height="158" rx="8" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{table(340)}
<g opacity="0.35">{chair(400, 306, 1.0, 'gold', -1)}</g>
{doc(490, 250, 110, 140, 3)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"><path d="M400 200v-60"/></g>''')

add('roundabout', '車がぐるりと回って進む、円い交差点', f'''
<path d="M0 0h600v400H0z" class="greenp"/>
<path d="M240 0h120v400H240zM0 140h600v120H0z" fill="#c3cbd1"/>
<circle cx="300" cy="200" r="120" fill="#c3cbd1"/>
<circle cx="300" cy="200" r="70" class="greenp o"/>
<circle cx="300" cy="200" r="122" fill="none" stroke="#ffffff" stroke-width="5" stroke-dasharray="26 20"/>
<g transform="translate(300 90)"><path d="M-90 0a90 90 0 0 1 60 20" fill="none" class="a" stroke-width="6" marker-end="url(#ar)"/></g>
<g transform="translate(180 320) rotate(-90)"><path d="M-50 0v-24l14-20h72l16 20v24z" class="coral o"/>
  <circle cx="-28" cy="4" r="12" fill="none" stroke="{INK}" stroke-width="5"/>
  <circle cx="30" cy="4" r="12" fill="none" stroke="{INK}" stroke-width="5"/></g>''', arrow=True)

add('rubble', 'くずれた建物の、こわれた石やコンクリート', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<g transform="translate(120 306)"><path d="M-70 0v-110h50v50h40V0z" fill="#c3cbd1" class="o"/>
  <path d="M-70-110l24-24 20 20" fill="none" stroke="{MUTED}" stroke-width="5"/></g>
{''.join(f'<rect x="-24" y="-16" width="48" height="32" rx="3" fill="{c}" stroke="{INK}" stroke-width="2.5" transform="translate({240+ (i%5)*66} {300+(i//5)*36}) rotate({-40+i*22})"/>'
         for i, c in enumerate(['#c3cbd1','#b0b8bd','#d5dbde','#a9b3ba','#c9d0d4','#bcc4c9','#d5dbde','#b0b8bd','#c3cbd1','#a9b3ba']))}
{''.join(f'<path d="M{280+i*60} 250l30 20" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''')

add('rodent', '前歯の目立つ、小さなけもの', f'''
{table(340)}
<g transform="translate(300 290)">
  <ellipse rx="90" ry="56" fill="#a9a29a" class="o"/>
  <circle cx="-80" cy="-30" r="40" fill="#a9a29a" class="o"/>
  <circle cx="-96" cy="-64" r="22" fill="#c4bcb2" class="o"/><circle cx="-56" cy="-70" r="22" fill="#c4bcb2" class="o"/>
  <circle cx="-92" cy="-32" r="5" class="ink"/>
  <path d="M-116-16l-30-8M-116-8l-30 6M-116-24l-26-18" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <ellipse cx="-116" cy="-14" rx="8" ry="6" fill="#7d6f64"/>
  <path d="M-108-4h10v18h-10zM-96-4h10v18h-10z" fill="#fffefd" stroke="{INK}" stroke-width="2"/>
  <path d="M86 20q56 6 60-50" fill="none" stroke="#a9a29a" stroke-width="12" stroke-linecap="round"/></g>
{ring(200, 286, 66)}''')

add('robe', 'ゆったりと体を包む、長い上着', f'''
{table(360)}
<g transform="translate(300 200)">
  <path d="M-120 160V-30l50-60h140l50 60v190z" class="violet o"/>
  <path d="M-70-90q70 60 140 0l-50 70h-40z" fill="#fffaf1" class="o"/>
  <path d="M-120-30l-40 40 40 50 20-30M120-30l40 40-40 50-20-30" fill="{VIO}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-40 40h80v18h-80z" class="goldd o"/>
  <path d="M-40 58q40 20 80 0" fill="none" stroke="{GLDD}" stroke-width="6"/></g>''')

add('repeatedly', '一度きりでなく、何度も何度もたたく', f'''
<g transform="translate(430 306)"><path d="M-110 0v-220h220V0z" fill="#fffefd" class="o"/>
  <path d="M-86 0v-200h172V0z" class="goldp o"/><circle cx="58" cy="-100" r="8" class="ink"/></g>
{person(180, 306, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'neutral')}
{''.join(f'<g transform="translate({{270+i*14}} {{190+i*22}})">{hand(0, 0, 1)}</g>' for i in [0])}
<g opacity="0.35">{hand(250, 160, 1)}{hand(258, 240, 1)}</g>
{''.join(f'<path d="M{{330+i*22}} {{150+i*24}}q16 16 0 32" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}
<g transform="translate(140 130)"><path d="M-40 0a40 40 0 1 1 14 30" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/></g>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
