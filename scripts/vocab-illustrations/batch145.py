# -*- coding: utf-8 -*-
"""第145回。-tion/-ance の抽象名詞と、in-/with- の連語、mi-/mo- の形容詞。"""
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

def bulb(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="30" class="goldp o"/>'
            f'<path d="M-12 30h24v10h-24z" class="goldd o"/>'
            f'<g class="golds"><path d="M0-46v-18"/><path d="M34-34l14-14"/><path d="M-34-34l-14-14"/>'
            f'<path d="M46 0h18"/><path d="M-46 0h-18"/></g></g>')

def flag(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0v-96" fill="none" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M0-96h58l-14 22 14 22H0z" class="{cls} o"/></g>')

def warn(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0-44l44 76h-88z" class="gold o"/>'
            f'<path d="M0-16v22" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cy="18" r="4" class="ink"/></g>')

# --- 言い方・まとめ方 --------------------------------------------------------

add('as a matter of fact', '思っていたものの陰から、本当のことが現れる', f'''
<g transform="translate(180 190)"><rect x="-96" y="-96" width="192" height="192" rx="14" class="paper"/>
  <circle cy="-10" r="46" class="bluep o"/><path d="M-56 66h112" fill="none" stroke="{MUTED}" stroke-width="5"/></g>
<g transform="translate(430 190)"><rect x="-96" y="-96" width="192" height="192" rx="14" class="paper"/>
  <path d="M-46 54l46-100 46 100z" class="coral o"/></g>
<path d="M334 96q-16 90 0 188" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="12 10"/>
<path d="M300 60h120" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('as such', 'それだけを取り出した姿と、飾りをつけた姿の対比', f'''
{split()}
{box(160, 200, 130, 100, 30, 'teal')}
{ring(160, 186, 116)}
{box(450, 210, 130, 100, 30, 'teal')}
<g opacity="0.9">{spark(360, 120, 1.1)}{spark(548, 132, 1)}{flag(392, 130, 0.5, 'gold')}</g>
<path d="M370 288h164" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/>
{ring(450, 196, 130, True)}''')

add('at large', '空になったおりから足あとが外へ続いている', f'''
<g transform="translate(180 200)"><path d="M-96-96h192v192h-192z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{-70+i*36} -96v192" fill="none" stroke="{INK}" stroke-width="6"/>' for i in range(5))}
  <path d="M26-96v192" fill="none" stroke="{CRL}" stroke-width="8" transform="rotate(24 26 0)"/></g>
{''.join(f'<ellipse cx="{300+i*56}" cy="{318+(i%2)*26}" rx="17" ry="9" class="ink"/>' for i in range(5))}
{head(520, 190, 26, 'blue', 'cap')}
<g transform="translate(520 250)"><circle r="30" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M22 22l24 24" stroke="{INK}" stroke-width="9" stroke-linecap="round"/></g>''')

add('in other words', '同じ中身を、別の言い方に置きかえる', f'''
{''.join(word(160, 130 + i*54, 5, 30) for i in range(3))}
<path d="M276 190h48M276 218h48" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
{''.join(word(440, 130 + i*54, 4 + i, 30, TEA) for i in range(3))}''')

add('in short', '長い文章を、ひとことに絞り込む', f'''
{doc(160, 170, 190, 250, 7)}
<path d="M276 130h60l-34 60h48" fill="none" class="a" marker-end="url(#ar)"/>
<path d="M270 96l86 74-86 74z" class="tealp o"/>
{word(470, 170, 3, 34, TEA)}''', arrow=True)

add('make sense of', 'ばらばらの断片を組み合わせて、絵の意味が通る', f'''
<g opacity="0.95">{''.join(f'<rect x="-30" y="-30" width="60" height="60" rx="8" class="tealp o" transform="translate({100+(i%2)*72} {150+(i//2)*84}) rotate({-30+i*25})"/>' for i in range(4))}</g>
<path d="M250 220h70" class="a" marker-end="url(#ar)"/>
<g transform="translate(430 216)">
  {''.join(f'<rect x="{-60+(i%2)*60}" y="{-60+(i//2)*60}" width="60" height="60" class="teal o"/>' for i in range(4))}
  <circle cx="0" cy="0" r="34" class="goldp o"/></g>
{bulb(430, 90, 0.9)}''', arrow=True)

add('in detail', '全体の一部を拡大して、細かいところまで見る', f'''
<g transform="translate(150 200)"><path d="M-96-96h192v192h-192z" fill="#fffefd" class="o"/>
  <path d="M-96 60l60-70 44 44 40-56 52 82v40h-196z" class="greenp o"/>
  {sun(46, -50, 22)}
  <rect x="-56" y="-30" width="52" height="52" fill="none" stroke="{CRL}" stroke-width="4"/></g>
<path d="M110 190l180-70M110 244l180 92" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"/>
<g transform="translate(420 214)"><circle r="126" fill="#fffefd" stroke="{INK}" stroke-width="5"/>
  <path d="M-110 66l70-92 56 60 46-52 58 84z" class="greenp o"/>
  {''.join(f'<path d="M{-80+i*34} 60q10-26 22 0" fill="none" stroke="{GRND}" stroke-width="3"/>' for i in range(5))}</g>''')

# --- できごとの名詞 ----------------------------------------------------------

add('entirety', '切り分けた一切れではなく、まるごと全部', f'''
{split()}
<g transform="translate(150 190)"><circle r="96" class="goldp o"/>
  {''.join(f'<path d="M0 0l{96*math.cos(math.radians(a)):.0f} {96*math.sin(math.radians(a)):.0f}" fill="none" stroke="{GLDD}" stroke-width="3"/>' for a in range(0, 360, 45))}</g>
{ring(150, 190, 118)}
<g transform="translate(450 210)"><path d="M0 0l68-68a96 96 0 0 1 28 68z" class="goldp o"/></g>
{ring(474, 190, 100, True)}''')

add('experimentation', 'いくつも組み合わせを変えて試してみる', f'''
{table(310)}
{''.join(f'<g transform="translate({110+i*116} 300)"><path d="M-14-96h28v54l30 42h-88l30-42z" fill="#fffefd" class="o"/>'
         f'<path d="M-46 0h92l-24-34h-44z" class="{c}"/></g>' for i, c in enumerate(['teal','coral','green','violet']))}
{''.join(f'<path d="M{110+i*116} 168q10-16 20 0" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(4))}
{head(534, 190, 26, 'blue', 'bob')}''')

add('facilitation', '通り道の石をどけて、進みやすくしてやる', f'''
<path d="M40 330q120-40 250-40t270 34" fill="none" stroke="{GLDD}" stroke-width="10" stroke-dasharray="18 14"/>
<g opacity="0.35"><circle cx="330" cy="286" r="34" fill="#b9c1c6" class="o"/></g>
<circle cx="180" cy="180" r="34" fill="#b9c1c6" class="o"/>
<path d="M300 250q-50-58-104-64" class="a" marker-end="url(#ar)"/>
{person(370, 306, 1.0, -1, 'teal', 'blue', 'reach', 'short', 'smile')}
{person(520, 306, 1.05, -1, 'coral', 'green', 'walk', 'bob', 'smile')}''', arrow=True)

add('fidelity', 'もとの形をそのまま写しとった、そっくりの複製', f'''
<g transform="translate(150 190)"><rect x="-96" y="-80" width="192" height="160" rx="12" class="paper"/>
  <path d="M-70 46q40-84 74-14 20 40 66-30" fill="none" stroke="{TEA}" stroke-width="6"/></g>
<path d="M276 174h48M276 206h48" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
<g transform="translate(450 190)"><rect x="-96" y="-80" width="192" height="160" rx="12" class="paper"/>
  <path d="M-70 46q40-84 74-14 20 40 66-30" fill="none" stroke="{TEA}" stroke-width="6"/></g>''')

add('for the purpose of', 'ねらった的に向けて手を打つ', f'''
{''.join(f'<circle cx="450" cy="190" r="{96-i*30}" class="{c} o"/>' for i, c in enumerate(['coralp','coral','coralp','coral']))}
{person(140, 306, 1.15, 1, 'teal', 'blue', 'point', 'short', 'neutral')}
<path d="M226 208h130" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('with a view to', '遠くの旗を見すえて歩いていく', f'''
{flag(510, 300, 1.1, 'coral')}
<path d="M40 336q140-30 300-30t222 26" fill="none" stroke="{GLDD}" stroke-width="8" stroke-dasharray="16 12"/>
{person(170, 300, 1.15, 1, 'teal', 'blue', 'hold', 'cap', 'neutral', 'walk')}
<g transform="translate(214 188)"><rect x="-12" y="-16" width="52" height="32" rx="10" class="ink"/>
  <circle cx="42" cy="0" r="9" class="bluep o"/></g>
<path d="M262 186l186-42" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>''')

add('formality', '中身より、判をつく手続きのほうが大事にされる', f'''
{table(300)}
{doc(220, 210, 180, 210, 5)}
<circle cx="270" cy="252" r="34" fill="none" stroke="{CRL}" stroke-width="6"/>
<g transform="translate(400 176)"><path d="M-30 40h60v20h-60z" class="teald o"/>
  <path d="M-16-40h32v80h-32z" class="teal o"/><path d="M-30-56h60v18h-60z" class="teald o"/></g>
{head(520, 250, 26, 'violet', 'bun')}''')

add('fulfilment', '長い坂を登りきって、頂上に旗を立てる', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<path d="M40 340L360 90l180 250z" fill="#c3cbd1" class="o"/>
<path d="M360 90l60 84h-120z" fill="#fffefd" class="o"/>
{flag(392, 122, 0.7, 'coral')}
{person(340, 128, 0.62, 1, 'teal', 'blue', 'up', 'cap', 'smile')}
<path d="M120 300q90-70 210-150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>''')

add('gratification', 'ほしかったものがすぐに手に入る心地よさ', f'''
{table(300)}
<g transform="translate(300 268)"><ellipse rx="76" ry="20" fill="#fffefd" class="o"/>
  <path d="M-54-8q0-56 54-56t54 56z" class="coralp o"/>
  <path d="M-54-8h108v8h-108z" class="coral o"/>
  <circle cx="0" cy="-72" r="10" class="coral o"/></g>
{head(140, 230, 30, 'teal', 'short')}
{''.join(spark(x, y, 1) for x, y in [(210,140),(300,110),(400,140)])}
<path d="M180 226l70 8" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('grievance', '苦情を書いた紙を窓口に差し出す', f'''
{table(280)}
{person(140, 306, 1.15, 1, 'coral', 'blue', 'give', 'short', 'sad')}
<g transform="translate(280 208) rotate(-6)"><rect x="-54" y="-70" width="108" height="140" rx="6" class="paper"/>
  {''.join(f'<rect x="-38" y="{-48+i*26}" width="{76-(i%2)*22}" height="8" rx="4" fill="{MUTED}"/>' for i in range(4))}
  <path d="M-24 46h32" stroke="{CRL}" stroke-width="6" fill="none"/></g>
<path d="M348 170h56" class="a" marker-end="url(#ar)"/>
{head(490, 240, 28, 'teal', 'bun')}''', arrow=True)

add('immersion', '水の中にすっかり沈めて、全体を浸す', f'''
<path d="M0 170h600v230H0z" fill="{BLUP}"/>
<path d="M0 170h600" fill="none" stroke="{BLU}" stroke-width="6"/>
{box(300, 260, 150, 116, 34, 'gold')}
{''.join(f'<circle cx="{200+i*54}" cy="{212-(i%3)*30}" r="{7+(i%3)*3}" fill="none" stroke="{BLU}" stroke-width="3"/>' for i in range(6))}
<path d="M300 110v40" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('inception', 'ずらりと続く歩みの、いちばん最初の一点', f'''
<path d="M60 200h480" fill="none" stroke="{MUTED}" stroke-width="6"/>
{''.join(f'<circle cx="{100+i*84}" cy="200" r="16" class="{"coral" if i==0 else "tealp"} o"/>' for i in range(6))}
{ring(100, 200, 50)}
<g transform="translate(100 300)"><path d="M0-40v40" fill="none" stroke="{GRND}" stroke-width="7"/>
  <path d="M0-24q-30-4-34-34 28 2 34 26z" class="greenp o"/></g>''')

add('indulgence', 'ほしがるままに、山ほど与えてしまう', f'''
{table(300)}
<g transform="translate(300 268)"><ellipse rx="86" ry="22" fill="#fffefd" class="o"/>
  <path d="M-64-14q0-64 64-64t64 64z" class="coralp o"/>
  <path d="M-40-52q0-42 40-42t40 42z" class="goldp o"/>
  <circle cx="0" cy="-104" r="11" class="coral o"/></g>
{head(120, 250, 28, 'teal', 'bob')}
{head(490, 250, 28, 'violet', 'short')}
<path d="M420 200l-58 24" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('insanity', 'すじの通った頭の中と、こんがらがった頭の中の対比', f'''
{split()}
<g transform="translate(150 190)"><ellipse rx="94" ry="106" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  {''.join(f'<path d="M-56 {-50+i*34}h112" fill="none" stroke="{TEA}" stroke-width="6" stroke-linecap="round"/>' for i in range(4))}</g>
{ring(150, 190, 126, True)}
<g transform="translate(450 190)"><ellipse rx="94" ry="106" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-58-40q60-40 96 10-70 20-80 56 60 30 96-20" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-40 60q50 26 96-16" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/></g>
{ring(450, 190, 126)}''')

add('madness', '割れ目を三輪車で跳び越そうとする、正気とは思えない企て', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<path d="M230 306h140v94H230z" fill="#fffaf1"/>
<path d="M230 306v94M370 306v94" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(150 296)"><circle cx="-30" cy="-14" r="26" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="34" cy="-4" r="14" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-30-40l30-30h34v66" fill="none" stroke="{CRLD}" stroke-width="7"/></g>
{person(140, 240, 0.86, 1, 'coral', 'blue', 'up', 'cap', 'surprised')}
{head(500, 250, 28, 'teal', 'bob')}
{drop(534, 210, 1.1, 'blue')}
{warn(470, 160, 0.9)}''')

add('realisation', 'つながりに気づいて、はっと分かる', f'''
{head(200, 280, 42, 'teal', 'short')}
{bulb(200, 130, 1.5)}
<g transform="translate(450 210)"><rect x="-100" y="-90" width="200" height="180" rx="16" class="paper"/>
  <circle cx="-46" cy="-34" r="24" class="tealp o"/><circle cx="46" cy="34" r="24" class="coralp o"/>
  <path d="M-30-18l58 40" class="a" marker-end="url(#ar)"/></g>
<path d="M262 170l86 10" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''', arrow=True)

add('recourse', '道がふさがれ、残された一つの手にたよる', f'''
{''.join(f'<g transform="translate({120+i*180} 220)"><path d="M-56-96h112v192h-112z" fill="#fffefd" class="o"/>'
         f'<circle cx="34" cy="10" r="7" class="ink"/></g>' for i in range(3))}
{''.join(f'<path d="M{64+i*180} 150l112 130M{176+i*180} 150l-112 130" fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round"/>' for i in range(2))}
<path d="M424 220h112" fill="none" stroke="{GRN}" stroke-width="0"/>
<g transform="translate(480 220)"><path d="M-56-96h112v192h-112z" class="greenp o"/></g>
{person(300, 380, 0.7, 1, 'teal', 'blue', 'walk', 'short', 'neutral')}
<path d="M340 340h96" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('seclusion', '町から遠く離れた丘に、ぽつんと建つ小屋', f'''
<g opacity="0.4">{tower(80, 306, 0.5, 'teal', 4)}{tower(150, 306, 0.42, 'blue', 3)}{tower(214, 306, 0.46, 'violet', 4)}</g>
<path d="M280 340q80-70 190-64" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"/>
<path d="M300 400q120-140 300-120v120z" class="greenp o"/>
<g transform="translate(470 268)"><path d="M-52 0v-56h104V0z" fill="#fffefd" class="o"/>
  <path d="M-64-56L0-104l64 48z" class="corald o"/>
  <path d="M-14 0v-32h28V0z" class="teal o"/></g>
{tree(556, 280, 0.6)}''')

add('severance', 'つながりを断ち切り、手当を渡して送り出す', f'''
<path d="M60 190h180M360 190h180" fill="none" stroke="{GLDD}" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(300 190) rotate(-20)">
  <path d="M-6 6l-64 56M-6-6l-64-56" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="-74" cy="66" r="16" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="-74" cy="-66" r="16" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M0 0l70 8" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g>
<g transform="translate(180 306)"><path d="M-70-46h140v70h-140z" class="goldp o"/>
  <path d="M-70-46L0 4l70-50" fill="none" class="o"/>{coin(0, -10, 16)}</g>
{person(470, 306, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'neutral')}''')

add('staffing', '組織の枠のあいた席に、人を割りあてる', f'''
{''.join(f'<g transform="translate({150+i*150} 130)"><rect x="-62" y="-46" width="124" height="92" rx="10" class="paper"/></g>' for i in range(3))}
{''.join(f'<g transform="translate({150+i*150} 280)"><rect x="-62" y="-46" width="124" height="92" rx="10" class="paper"/></g>' for i in range(3))}
<path d="M150 176v58M300 176v58M450 176v58" fill="none" stroke="{MUTED}" stroke-width="3"/>
{head(150, 126, 26, 'teal', 'short')}{head(300, 126, 26, 'coral', 'bob')}
{head(450, 126, 26, 'violet', 'short')}{head(150, 276, 26, 'green', 'bun')}
{head(450, 276, 26, 'blue', 'cap')}
<path d="M300 240v22" class="a" marker-end="url(#ar)"/>
{head(300, 210, 22, 'gold', 'short')}''', arrow=True)

add('tenderness', '両手でそっと小鳥を包む', f'''
{hand(220, 250, 1)}
{hand(390, 250, -1)}
<g transform="translate(304 206)"><ellipse rx="46" ry="36" class="goldp o"/>
  <circle cx="-30" cy="-24" r="22" class="goldp o"/>
  <path d="M-48-28l-18 6 18 8z" class="coral o"/>
  <circle cx="-24" cy="-28" r="4" class="ink"/>
  <path d="M10-6q28-14 40 12-26 12-40-12z" class="gold o"/></g>
<g class="corals">{''.join(f'<path d="M{160+i*150} {120+i*14}q14-20 28 0" />' for i in range(3))}</g>''')

add('utterance', '口から出たひとことが、そのまま形になる', f'''
{head(160, 260, 46, 'teal', 'short')}
<path d="M140 276q20 16 40 0" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(400 180)"><rect x="-130" y="-70" width="260" height="140" rx="24" class="paper"/>
  <path d="M-114 56l-42 46 4-46z" class="paper"/>
  {word(0, 0, 4, 44, TEA)}</g>
<path d="M212 246l40-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

# --- 連語・状態 --------------------------------------------------------------

add('governmental', '旗の立った、ドームのある役所の建物', f'''
<g transform="translate(300 306)">
  <path d="M-190 0v-120h380V0z" fill="#fffefd" class="o"/>
  <path d="M-200-120h400l-40-40h-320z" class="teald o"/>
  {''.join(f'<path d="M{-160+i*54} 0v-100h34V0z" class="tealp o"/>' for i in range(7))}
  <path d="M-96-160q96-96 192 0z" class="teal o"/>
  <path d="M-26-160h52v-30h-52z" class="teald o"/></g>
{flag(300, 116, 0.7, 'coral')}''')

add('in danger of', 'がけのふちに立っていて、落ちる恐れがある', f'''
<path d="M0 306h340v94H0z" class="ground"/>
<path d="M340 306v94" fill="none" stroke="{INK}" stroke-width="4"/>
{person(296, 306, 1.2, 1, 'coral', 'blue', 'stand', 'short', 'surprised')}
<path d="M356 330q10 40 0 60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{warn(450, 190, 1.3)}''')

add('in need of', 'パンクした自転車が、空気入れを必要としている', f'''
{table(340)}
<g transform="translate(210 300)">
  <circle cx="-70" cy="-30" r="46" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M60-30a46 20 0 1 1-92 0 46 20 0 1 1 92 0z" fill="none" stroke="{CRL}" stroke-width="7"/>
  <path d="M-70-76l40-46h44l26 92" fill="none" stroke="{TEA}" stroke-width="7"/></g>
<path d="M330 210h64" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 300)"><path d="M-22-96h44v96h-44z" class="blue o"/>
  <path d="M0-96v-30h-24" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M22-30h50" fill="none" stroke="{INK}" stroke-width="6"/></g>''', arrow=True)

add('in public', '大勢の前に立って話す', f'''
<g transform="translate(180 300)"><path d="M-70 0v-80h140V0z" class="goldd o"/></g>
{person(180, 220, 1.15, 1, 'teal', 'blue', 'point', 'short', 'neutral')}
{''.join(head(340 + (i % 3) * 84, 250 + (i // 3) * 66, 26, c, h)
         for i, (c, h) in enumerate([('coral','short'),('violet','bob'),('green','short'),('blue','bun'),('gold','cap'),('teal','short')]))}''')

add('insolvent', '払える金より、払うべき額のほうが重い', f'''
<g transform="translate(300 110)"><path d="M-200 0h400" fill="none" stroke="{INK}" stroke-width="7" transform="rotate(12)"/>
  <path d="M0 0v-60" fill="none" stroke="{INK}" stroke-width="7"/><circle cy="-66" r="9" class="ink"/></g>
<path d="M104 154v70" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(104 250)"><path d="M-56-26h112v52h-112z" class="goldp o"/>{coin(0, 0, 16)}</g>
<path d="M496 70v130" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(496 240)">{''.join(f'<rect x="-52" y="{-20-i*36}" width="104" height="32" rx="5" class="paper"/>' for i in range(3))}
  {''.join(f'<rect x="-38" y="{-10-i*36}" width="58" height="8" rx="4" fill="{CRL}"/>' for i in range(3))}</g>''')

add('interpretive', '分かりにくい形が何を指すのかを解いて示す', f'''
<g transform="translate(150 200)"><rect x="-96" y="-96" width="192" height="192" rx="14" class="paper"/>
  <path d="M-56 46q30-100 62-30 20 44 50-40" fill="none" stroke="{VIO}" stroke-width="8"/>
  <circle cx="30" cy="-52" r="14" class="violetp o"/></g>
{head(300, 300, 26, 'teal', 'bun')}
<path d="M262 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 190)"><rect x="-110" y="-80" width="220" height="160" rx="20" class="paper"/>
  <path d="M-92 66l-30 40 8-40z" class="paper"/>
  {tree(-40, 40, 0.5)}{sun(46, -26, 22)}</g>''', arrow=True)

add('intoxicated', '酒びんのそばで足もとがふらつく', f'''
{table(320)}
<g transform="translate(150 300)"><path d="M-24-70h48v70h-48z" class="green o"/>
  <path d="M-10-70v-34h20v34z" class="greend o"/></g>
{person(360, 306, 1.2, 1, 'coral', 'blue', 'reach', 'short', 'neutral', 'walk')}
<g transform="translate(360 150)"><path d="M0 0a26 26 0 1 1 22-14 18 18 0 1 0 14 24" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/></g>
<path d="M250 260q14-18 0-36M480 260q-14-18 0-36" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>''')

add('keen on', 'これが好きで仕方ない、と目を輝かせる', f'''
{person(180, 306, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
<g transform="translate(430 240)"><circle r="70" fill="#fffefd" class="o"/>
  <path d="M0-70a70 70 0 0 1 0 140 44 70 0 0 0 0-140z" class="ink"/>
  <path d="M-70 0h140" fill="none" stroke="{INK}" stroke-width="3"/></g>
{''.join(f'<path d="M{280+i*40} {150-i*14}q-16-22 0-34 16 12 0 34z" class="coral o"/>' for i in range(3))}''')

add('meticulous', 'ピンセットで小さな部品を一つずつ正確に置く', f'''
{table(320)}
<g transform="translate(300 290)"><rect x="-110" y="-46" width="220" height="46" rx="6" class="tealp o"/>
  {''.join(f'<rect x="{-92+i*36}" y="-36" width="24" height="26" rx="4" class="teal o"/>' for i in range(5))}</g>
<g transform="translate(320 170) rotate(20)"><path d="M-10-70l6 70M10-70l-6 70" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <rect x="-14" y="-84" width="28" height="18" rx="6" class="ink"/></g>
<rect x="330" y="222" width="16" height="16" rx="3" class="coral o"/>
<g transform="translate(160 150)"><circle r="52" fill="#ffffff" opacity="0.2" stroke="{INK}" stroke-width="6"/>
  <path d="M36 36l30 30" stroke="{INK}" stroke-width="13" stroke-linecap="round"/></g>
{head(500, 200, 28, 'coral', 'short')}''')

add('microscopic', '目には点にしか見えないものを、大きく拡大して見る', f'''
{table(320)}
{coin(140, 280, 40)}
<circle cx="230" cy="292" r="4" class="ink"/>
<path d="M256 270l86-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<path d="M256 300l86 40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(430 190)"><circle r="120" fill="#fffefd" stroke="{INK}" stroke-width="6"/>
  <circle r="52" class="tealp o"/>
  {''.join(f'<circle cx="{40*math.cos(math.radians(a)):.0f}" cy="{40*math.sin(math.radians(a)):.0f}" r="10" class="teal o"/>' for a in range(0, 360, 60))}</g>''')

add('mindless', '何も考えずに、同じ動きをくり返す', f'''
{person(230, 306, 1.2, 1, 'blue', 'blue', 'carry', 'short', 'neutral')}
<g transform="translate(244 216)"><rect x="-40" y="-28" width="80" height="56" rx="6" class="gold o"/></g>
<circle cx="330" cy="180" r="9" fill="#fffefd" class="o"/>
<circle cx="356" cy="150" r="13" fill="#fffefd" class="o"/>
<g transform="translate(450 116)"><ellipse rx="110" ry="72" fill="#fffefd" class="o"/></g>
{''.join(f'<path d="M{120+i*30} 340q16-16 30 0" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('miraculous', 'こわれた車から、かすり傷ひとつなく歩いて出てくる', f'''
<g transform="translate(180 290) rotate(-8)">
  <path d="M-120 0v-46l30-44h150l30 44V0z" class="corald o"/>
  <path d="M-40-90l-16-40 44 30 24-34 12 44z" class="coral o"/>
  <circle cx="-70" cy="6" r="26" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle cx="70" cy="6" r="26" fill="none" stroke="{INK}" stroke-width="8"/></g>
{person(430, 306, 1.2, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{''.join(spark(x, y, 1.1) for x, y in [(360,120),(500,110),(560,190)])}''')

add('mischievous', 'こっそりかばんにカエルを入れて、にやりと笑う', f'''
{table(300)}
<g transform="translate(410 268)"><path d="M-56 30v-58h112v58z" class="violet o"/>
  <path d="M-24-28v-16h48v16" fill="none" class="a"/></g>
<g transform="translate(408 208)"><ellipse rx="30" ry="22" class="green o"/>
  <circle cx="-14" cy="-18" r="9" class="greenp o"/><circle cx="14" cy="-18" r="9" class="greenp o"/>
  <circle cx="-14" cy="-19" r="4" class="ink"/><circle cx="14" cy="-19" r="4" class="ink"/>
  <path d="M-30 24l-16 14M30 24l16 14" fill="none" stroke="{GRND}" stroke-width="7" stroke-linecap="round"/></g>
{person(180, 306, 1.1, 1, 'coral', 'blue', 'point', 'short', 'neutral')}
<path d="M168 200q12 12 24 0" fill="none" stroke="{INK}" stroke-width="3"/>
{''.join(spark(x, y, 0.7) for x, y in [(120,160),(250,150)])}''')

add('misguided', '案内どおりに進んだが、目あては反対側だった', f'''
<g transform="translate(300 306)"><path d="M-6-160v160" fill="none" stroke="{GLDD}" stroke-width="12"/>
  <path d="M-6-150h-130l-26 26 26 26h130z" class="gold o"/></g>
{person(140, 306, 1.0, -1, 'coral', 'blue', 'walk', 'short', 'neutral')}
{cross(70, 170, 1.1)}
{flag(500, 300, 1.0, 'green')}
{tick(506, 170, 1.1)}
<path d="M240 250h-90" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('molecule', '玉と棒でつないだ、いくつかの原子のかたまり', f'''
<g stroke="{INK}" stroke-width="12" stroke-linecap="round" fill="none">
  <path d="M300 190l-110 68M300 190l110 68M300 190v-96"/></g>
<circle cx="300" cy="190" r="60" class="teal o"/>
<circle cx="190" cy="258" r="42" class="coral o"/>
<circle cx="410" cy="258" r="42" class="coral o"/>
<circle cx="300" cy="94" r="42" class="gold o"/>''')

add('momentary', 'ひらめいた光が、次の瞬間にはもう消えている', f'''
{split()}
{''.join(spark(150, 190, 2.4)  for _ in [0])}
{''.join(f'<path d="M150 {90-0}v-0"/>' for _ in [])}
<g transform="translate(450 190)"><g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9">
  <path d="M-40-40l80 80M40-40l-80 80"/></g></g>
<path d="M60 330h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
<path d="M132 330h36" fill="none" stroke="{CRL}" stroke-width="14" stroke-linecap="round"/>
<path d="M240 330h30" class="a" marker-end="url(#ar)"/>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
