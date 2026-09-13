# -*- coding: utf-8 -*-
"""第150回。s-/t- の形容詞と、家族・道具の名詞。"""
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

def spoon(x, y, s=1, r=0):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({r})"><ellipse cy="-56" rx="30" ry="42" class="goldp o"/>'
            f'<path d="M-8-14h16v90h-16z" class="goldd o"/></g>')

def bulb(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="30" class="goldp o"/>'
            f'<path d="M-12 30h24v10h-24z" class="goldd o"/>'
            f'<g class="golds"><path d="M0-46v-18"/><path d="M34-34l14-14"/><path d="M-34-34l-14-14"/>'
            f'<path d="M46 0h18"/><path d="M-46 0h-18"/></g></g>')

# --- からだ・感じ方 ----------------------------------------------------------

add('squeamish', '見ただけで気分が悪くなり、思わず顔をそむける', f'''
{table(320)}
<g transform="translate(430 288)"><ellipse rx="76" ry="20" fill="#fffefd" class="o"/>
  <path d="M-30-10q10-24 34-12 22 12 6 26" fill="none" stroke="#c98a5c" stroke-width="10" stroke-linecap="round"/></g>
{person(180, 306, 1.25, -1, 'green', 'blue', 'hold', 'short', 'sad')}
<circle cx="180" cy="176" r="30" fill="{TONES['green'][1]}" opacity="0.7"/>
<g fill="none" stroke="{GRN}" stroke-width="5" stroke-linecap="round">
  <path d="M120 150q-16-24 0-46M92 180q-16-24 0-46"/></g>
<path d="M250 200l80 40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('startled', '突然の物音に、びくっとして持ち物を落とす', f'''
{person(300, 306, 1.3, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
<g class="corals" stroke-width="6">{''.join(f'<path d="M300 130v-30" transform="rotate({d} 300 190)"/>' for d in [-50, -25, 0, 25, 50])}</g>
<g transform="translate(430 290) rotate(28)"><path d="M-24 0v-42h48V0z" fill="#fffefd" class="o"/></g>
{''.join(f'<path d="M{402+i*20} {230+i*14}q10-14 20 0" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
<g transform="translate(90 180)">{''.join(f'<path d="M0 {-30+i*30}q40 30 0 60" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(2))}</g>''')

add('swollen', 'ふつうの指と、赤くはれ上がった指の対比', f'''
{split()}
<g transform="translate(150 250)"><rect x="-26" y="-120" width="52" height="180" rx="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-26-60h52" fill="none" stroke="{SKINL}" stroke-width="2.5"/></g>
{ring(150, 220, 122, True)}
<g transform="translate(450 250)"><path d="M-26 60v-70q-30-26-8-62 20-32 60-12 34 18 14 60-6 12-8 22v62z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="8" cy="-92" r="34" class="coralp" opacity="0.7"/></g>
<g class="corals" stroke-width="5">{''.join(f'<path d="M450 92v-22" transform="rotate({d} 450 158)"/>' for d in [-40, 0, 40])}</g>
{ring(450, 220, 130)}''')

add('tiredness', '一日の終わり、肩を落として目がとろんとする', f'''
{sit(280, 340, 1.3, 1, 'blue', 'blue', 'short', 'sad', 'down')}
{chair(296, 340, 1.15, 'gold', -1)}
<path d="M236 214l16 6M320 214l-16 6" fill="none" stroke="{INK}" stroke-width="3"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M170 200q16-20 0-40M400 210q-16-20 0-40"/></g>
{''.join(f'<path d="M{430+i*24} {150-i*22}q16 16 0 32" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''')

# --- 態度 --------------------------------------------------------------------

add('stern', '腕を組み、いかめしい顔できまりを指し示す', f'''
<g transform="translate(470 190)"><rect x="-100" y="-110" width="200" height="220" rx="10" class="paper"/>
  {''.join(f'<g><circle cx="-70" cy="{-76+i*50}" r="8" class="coral o"/><rect x="-52" y="{-84+i*50}" width="{118-(i%2)*36}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(4))}</g>
<g transform="translate(200 306)">
  <path d="M-14-8l-8 34M14-8l8 34" fill="none" stroke="{BLUD}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-28-84q28-14 56 0l-9 76h-38z" fill="{VIO}" class="o"/>
  <circle cx="0" cy="-116" r="27" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 -8) scale(1.06)" fill="{HAIR}"/>
  <path d="M-18-124l16 8M18-124l-16 8" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="-10" cy="-112" r="3" class="ink"/><circle cx="10" cy="-112" r="3" class="ink"/>
  <path d="M-10-94h20" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <path d="M-32-40l64-14M32-42l-64 16" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/></g>
<path d="M262 230l90-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('stringent', '条件がきつく、細い口をくぐれるものはごくわずか', f'''
<g transform="translate(300 200)"><path d="M-220-120h440v100l-190 20 190 20v100h-440v-100l190-20-190-20z" fill="#dfe6ea" class="o"/></g>
{''.join(f'<circle cx="{70+i*44}" cy="{130+(i%3)*70}" r="24" class="tealp o"/>' for i in range(6))}
<circle cx="300" cy="200" r="17" class="coral o"/>
<circle cx="470" cy="200" r="24" class="coral o"/>
<path d="M120 200h130" fill="none" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('stingy', 'こわばった手でコインを握りしめ、けっして放さない', f'''
{person(200, 306, 1.25, 1, 'green', 'blue', 'hold', 'short', 'neutral')}
<g transform="translate(238 212)"><ellipse rx="42" ry="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  {''.join(f'<path d="M{-30+i*18} -22q10 22 0 44" fill="none" stroke="{SKINL}" stroke-width="2.5"/>' for i in range(4))}
  {coin(0, -44, 16)}</g>
{person(450, 306, 1.15, -1, 'coral', 'blue', 'reach', 'bob', 'sad')}
<path d="M382 224h-70" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<path d="M300 160v-30" fill="none" stroke="{CRL}" stroke-width="5"/>''')

add('submissive', '言われるまま、うつむいて従う', f'''
{person(430, 306, 1.3, -1, 'violet', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(200 306)">
  <path d="M-12-8l-6 30M10-8l6 30" fill="none" stroke="{BLUD}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-72q26-13 52 0l-8 66h-36z" fill="{TEA}" class="o"/>
  <path d="M-22-66l6 44M22-66l-6 44" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="0" cy="-100" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 4)" fill="{HAIR}"/>
  <path d="M-11-94l10 4M11-94l-10 4" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-7-80h14" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
<path d="M340 220h-90" fill="none" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('timid', 'ふみ出せずに、扉の前でためらう', f'''
<g transform="translate(420 306)"><path d="M-90 0v-210h180V0z" fill="#fffefd" class="o"/>
  <path d="M-70 0v-190h140V0z" class="goldp o"/><circle cx="46" cy="-90" r="8" class="ink"/></g>
{person(180, 306, 1.2, 1, 'teal', 'blue', 'hold', 'bob', 'sad')}
<path d="M240 300l60 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
{''.join(f'<ellipse cx="{270+i*30}" cy="330" rx="14" ry="7" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6"/>' for i in range(2))}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M120 190q16-16 0-32"/></g>
{drop(230, 176, 0.9)}''')

add('tactful', 'とげのない言い方で伝わり、相手も受けとめる', f'''
{person(140, 306, 1.15, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
<g transform="translate(300 180)"><rect x="-90" y="-56" width="180" height="112" rx="52" class="tealp o"/>
  <path d="M-60 50l-24 30 6-30z" class="tealp o"/>
  {word(0, 0, 4, 30, TEAD)}</g>
{person(470, 306, 1.15, -1, 'coral', 'blue', 'stand', 'short', 'smile')}
<path d="M394 190h40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('tactless', 'とげのある言い方が、そのまま相手に刺さる', f'''
{person(140, 306, 1.15, 1, 'violet', 'blue', 'point', 'short', 'neutral')}
<g transform="translate(300 180)">
  <path d="{''.join(f'L{(96 if i%2 else 66)*math.cos(math.radians(i*22.5)):.0f} {(62 if i%2 else 42)*math.sin(math.radians(i*22.5)):.0f}' for i in range(16))[1:]}z" class="coralp o"/>
  {word(0, 0, 4, 26, CRLD)}</g>
{person(480, 306, 1.15, -1, 'teal', 'blue', 'hold', 'bob', 'sad')}
<g class="corals" stroke-width="5">{''.join(f'<path d="M{430+i*10} {150+i*20}h26"/>' for i in range(3))}</g>''')

add('take advantage of', '人が立てかけたはしごを、そのまま使わせてもらう', f'''
<g transform="translate(330 306) rotate(-16)"><path d="M-24 0v-230h48V0z" fill="none" stroke="{GLDD}" stroke-width="9"/>
  {''.join(f'<path d="M-24 {-30-i*38}h48" fill="none" stroke="{GLDD}" stroke-width="8"/>' for i in range(5))}</g>
{person(190, 306, 1.05, -1, 'teal', 'blue', 'reach', 'bun', 'neutral')}
{person(430, 240, 1.0, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{box(510, 110, 70, 50, 16, 'gold')}
<path d="M420 130h50" fill="none" class="a" marker-end="url(#ar)"/>''', arrow=True)

# --- 見え方・質 --------------------------------------------------------------

add('superficial', '表の一枚だけをなでて、奥までは見ない', f'''
<g transform="translate(300 240)"><path d="M-220-80h440v200h-440z" fill="#e8dfcd" class="o"/>
  <path d="M-220-80h440v40h-440z" class="goldp o"/>
  <path d="M-220-40h440" fill="none" stroke="{INK}" stroke-width="3"/>
  {''.join(f'<circle cx="{-160+i*80}" cy="{20+(i%2)*50}" r="18" fill="#cbbfa4"/>' for i in range(6))}</g>
{hand(160, 130, 1)}
<path d="M220 176h180" fill="none" stroke="{CRL}" stroke-width="5" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M470 210v120"/></g>''', arrow=True)

add('superfluous', 'すでに満ちているのに、まだ注ぎ足す', f'''
{table(330)}
<g transform="translate(280 300)"><path d="M-56 0v-104h112V0z" fill="#fffefd" class="o"/>
  <path d="M-50-84h100v82h-100z" class="bluep"/>
  <path d="M-56 0v-104h112V0z" fill="none" class="o"/></g>
<g transform="translate(400 150) rotate(56)"><path d="M-30 0v-70h60V0z" class="teal o"/>
  <path d="M30-54l40-16v40z" class="teal o"/></g>
<path d="M300 176v34" fill="none" stroke="{BLU}" stroke-width="10" stroke-linecap="round"/>
{''.join(drop(228 + i*24, 306 + (i%2)*16, 1.0) for i in range(4))}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M150 200q16-20 0-40"/></g>''')

add('subjective', '同じものを見て、二人が別のものを思い浮かべる', f'''
<g transform="translate(300 300)"><path d="M-46-46h92v92h-92z" class="gold o"/></g>
{head(90, 300, 28, 'teal', 'short')}
{head(510, 300, 28, 'coral', 'bob')}
<g transform="translate(120 130)"><ellipse rx="94" ry="62" fill="#fffefd" class="o"/>
  <circle r="34" class="teal o"/></g>
<g transform="translate(480 130)"><ellipse rx="94" ry="62" fill="#fffefd" class="o"/>
  <path d="M-34 28l34-58 34 58z" class="coral o"/></g>
<path d="M250 280l-90-60M350 280l90-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('succinct', 'だらだら長い言い方と、短く要を得た言い方の対比', f'''
{split()}
{''.join(word(150, 100 + i*46, 5, 26) for i in range(5))}
{ring(150, 200, 130, True)}
{''.join(word(450, 178 + i*46, n, 30, TEA) for i, n in enumerate([4, 3]))}
{ring(450, 200, 130)}''')

add('stagnant', 'よどんで動かない水と、流れている水の対比', f'''
{split()}
<g transform="translate(150 230)"><path d="M-110-60h220v160h-220z" fill="#8f9a72" class="o"/>
  {''.join(f'<ellipse cx="{-70+i*46}" cy="{-20+(i%3)*44}" rx="22" ry="10" fill="#79855e"/>' for i in range(6))}</g>
{ring(150, 230, 132)}
<g transform="translate(450 230)"><path d="M-110-60h220v160h-220z" fill="{BLUP}" class="o"/>
  {''.join(f'<path d="M{-90+ (i%2)*30} {-30+i*30}h140" fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round"/>' for i in range(5))}</g>
<path d="M370 130h160" fill="none" class="a" marker-end="url(#ar)"/>
{ring(450, 230, 132, True)}''', arrow=True)

add('sterile', '袋を切ってはじめて出す、菌のついていない器具', f'''
{table(330)}
<g transform="translate(300 220)"><rect x="-180" y="-70" width="360" height="140" rx="14" fill="#eaf4fb" class="o"/>
  <path d="M-180-46h360M-180 46h360" fill="none" stroke="{BLU}" stroke-width="3" stroke-dasharray="9 8"/>
  <path d="M-110 20v-40h30v40zM-60 20l60-40M20-20h80v10h-80z" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M110-24l50 24-50 24" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 7">
  <circle cx="110" cy="110" r="16"/><circle cx="500" cy="120" r="14"/><circle cx="150" cy="330" r="15"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(200,120),(410,120)])}''')

add('stainless', 'さびたスプーンと、さびない光るスプーンの対比', f'''
{split()}
<g transform="translate(150 220) rotate(-14)"><ellipse cy="-56" rx="34" ry="46" fill="#b08a5a" class="o"/>
  <path d="M-9-14h18v110h-18z" fill="#8c6b42" class="o"/>
  {''.join(f'<circle cx="{-16+i*14}" cy="{-70+(i%3)*24}" r="5" fill="#6f5230"/>' for i in range(5))}</g>
{ring(150, 220, 132, True)}
<g transform="translate(450 220) rotate(-14)"><ellipse cy="-56" rx="34" ry="46" fill="#dfe6ea" class="o"/>
  <path d="M-9-14h18v110h-18z" fill="#c3ccd2" class="o"/>
  <path d="M-16-76q14 26 0 44" fill="none" stroke="#ffffff" stroke-width="7"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(390,120),(520,240)])}
{ring(450, 220, 132)}''')

add('sturdy', 'たわむ台と、重さに耐える頑丈な台の対比', f'''
{split()}
<g transform="translate(150 260)"><path d="M-90-10q90 30 180 0v14q-90 30-180 0z" class="goldp o"/>
  <path d="M-70 26v50M70 26v50" fill="none" stroke="{GLDD}" stroke-width="6"/></g>
{box(150, 190, 110, 66, 20, 'coral')}
{ring(150, 220, 130, True)}
<g transform="translate(450 260)"><path d="M-96-14h192v26h-192z" class="goldd o"/>
  <path d="M-74 12v64M74 12v64" fill="none" stroke="{GLDD}" stroke-width="18" stroke-linecap="round"/></g>
{box(450, 190, 110, 66, 20, 'coral')}
{ring(450, 220, 130)}''')

add('tasteful', '飾りすぎず、すっきり品よくまとめた部屋', f'''
<g transform="translate(300 200)"><rect x="-230" y="-140" width="460" height="280" rx="10" fill="#fdfbf6" class="o"/></g>
<g transform="translate(300 250)"><path d="M-40 0q-14-56 0-70h80q14 14 0 70z" class="tealp o"/>
  <path d="M0-70v-30" fill="none" stroke="{GRND}" stroke-width="5"/>
  <path d="M0-92q26-8 30-34-28 4-34 30z" class="greenp o"/></g>
<g transform="translate(140 140)"><rect x="-56" y="-40" width="112" height="80" rx="4" class="goldd o"/>
  <rect x="-44" y="-28" width="88" height="56" fill="#eef2f4"/></g>
{chair(470, 320, 0.9, 'gold', -1)}''')

add('tasteless', 'あれもこれも飾りたてて、品がなくなった部屋', f'''
<g transform="translate(300 200)"><rect x="-230" y="-140" width="460" height="280" rx="10" fill="#fceff2" class="o"/>
  {''.join(f'<circle cx="{-190+i*44}" cy="{-110+(i%3)*36}" r="14" class="{c}" />' for i, c in enumerate(['coral','gold','violet','green','blue','teal','coral','gold','violet','green']))}</g>
<g transform="translate(300 250)"><path d="M-46 0q-20-60 0-74-24-26 0-40h92q24 14 0 40 20 14 0 74z" class="violet o"/>
  <path d="M-34-58q34-14 68 0M-30-24q30-12 60 0" fill="none" stroke="{GLD}" stroke-width="6"/></g>
<g transform="translate(130 150)"><rect x="-60" y="-46" width="120" height="92" rx="4" class="coral o"/>
  <rect x="-46" y="-32" width="92" height="64" class="goldp o"/>
  {''.join(f'<circle cx="{-52+i*26}" cy="-46" r="7" class="green o"/>' for i in range(5))}</g>
{''.join(spark(x, y, 1.1) for x, y in [(470,120),(520,230),(430,300)])}''')

add('tentative', 'えんぴつで仮に書いた、まだ変わるかもしれない予定', f'''
{doc(280, 200, 300, 280, 0)}
{''.join(f'<g><rect x="150" y="{100+i*54}" width="18" height="18" rx="4" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 5"/>'
         f'<rect x="184" y="{102+i*54}" width="{190-(i%2)*60}" height="12" rx="6" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 7"/></g>' for i in range(4))}
<g transform="translate(470 150) rotate(28)"><path d="M-7-90h14v120l-7 20-7-20z" class="goldp o"/>
  <path d="M-7 30h14l-7 20z" class="ink"/></g>
<g transform="translate(500 300)"><path d="M-30 20h60v-14h-60z" class="coralp o"/></g>''')

# --- ことば ------------------------------------------------------------------

add('suffix', '語のうしろに付いて、意味を変える短い部分', f'''
{word(220, 200, 4, 46, INK)}
<g transform="translate(430 200)">{''.join(f'<rect x="{-46+i*46}" y="-24" width="34" height="48" rx="7" class="coral o"/>' for i in range(2))}</g>
<path d="M350 200h30" fill="none" stroke="{MUTED}" stroke-width="4"/>
{ring(430, 200, 80)}
<path d="M430 300v-30" class="a" marker-end="url(#ar)"/>
{''.join(f'<path d="M{160+i*24} 320h16" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(0))}''', arrow=True)

add('synonym', 'ちがう二つの語が、同じものを指す', f'''
{word(150, 120, 4, 34, TEA)}
{word(450, 120, 6, 26, VIO)}
<path d="M270 120h60" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
<path d="M270 146h60" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
<path d="M150 170l130 80M450 170l-130 80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(300 300)"><circle r="60" class="goldp o"/>
  <path d="M-30 20q30-52 60 0z" class="gold o"/><circle cx="0" cy="-16" r="14" class="gold o"/></g>''')

add('thematic', '同じ話題のものどうしを、まとめて分ける', f'''
{''.join(f'<g transform="translate({150+i*300} 200)"><rect x="-120" y="-130" width="240" height="260" rx="14" fill="none" stroke="{c} " stroke-width="5"/></g>' for i, c in enumerate([TEA, CRL]))}
{''.join(f'<circle cx="{90+(i%3)*60}" cy="{130+(i//3)*74}" r="26" class="teal o"/>' for i in range(6))}
{''.join(f'<path d="M{406+(i%3)*60} {156+(i//3)*74}l-26 44h52z" class="coral o"/>' for i in range(6))}''')

add('think of', 'いくつも案を出して、これはどうかと思いつく', f'''
{person(160, 306, 1.2, 1, 'teal', 'blue', 'think', 'short', 'smile')}
{bulb(212, 120, 1.1)}
{''.join(f'<g transform="translate({350+ (i%2)*140} {130+(i//2)*110})"><rect x="-64" y="-40" width="128" height="80" rx="16" class="paper"/>'
         f'<circle cx="0" cy="0" r="{16+i*4}" class="{c} o"/></g>' for i, c in enumerate(['coral','gold','green','violet']))}
{ring(350, 240, 80)}''')

add('thanks to', '差しかけてもらった傘のおかげで、ぬれずにすむ', f'''
{cloud(160, 90, 1.3, 'blue')}{cloud(400, 80, 1.5, 'blue')}
{''.join(f'<path d="M{70+i*40} {150+(i%3)*20}v40" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>' for i in range(12))}
{person(400, 340, 1.15, -1, 'teal', 'blue', 'reach', 'bun', 'smile')}
<path d="M180 210q120-90 240 0z" class="coral o"/>
<path d="M180 210q30-26 60 0t60 0 60 0" fill="none" class="o"/>
<path d="M300 210v90" fill="none" stroke="{GLDD}" stroke-width="7"/>
{person(250, 340, 1.1, 1, 'coral', 'blue', 'stand', 'short', 'smile')}
<path d="M300 130v-24" fill="none" stroke="{GLDD}" stroke-width="6"/>''')

add('suitable for', 'いくつかのふたのうち、なべにぴたりと合う一つ', f'''
{table(340)}
<g transform="translate(300 300)"><path d="M-90 0q0 6 90 6t90-6v-90h-180z" class="teal o"/>
  <ellipse cy="-90" rx="90" ry="20" class="tealp o"/></g>
<g transform="translate(110 160)"><ellipse rx="58" ry="14" class="goldp o"/><circle cy="-22" r="9" class="gold o"/></g>
<g transform="translate(300 130)"><ellipse rx="92" ry="20" class="coralp o"/><circle cy="-30" r="11" class="coral o"/></g>
<g transform="translate(500 160)"><ellipse rx="120" ry="24" class="goldp o"/><circle cy="-32" r="11" class="gold o"/></g>
<path d="M300 170v30" class="a" marker-end="url(#ar)"/>
{ring(300, 132, 108)}''', arrow=True)

add('temporal', '場所ではなく、時のならびで見る', f'''
<path d="M60 200h480" fill="none" stroke="{MUTED}" stroke-width="6" marker-end="url(#ar)"/>
{''.join(f'<circle cx="{110+i*90}" cy="200" r="14" class="teal o"/>' for i in range(5))}
{''.join(f'<path d="M{110+i*90} 226v22" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(5))}
<g transform="translate(300 320)"><circle r="46" fill="#fffefd" class="o"/>
  <path d="M0 0v-30M0 0l22 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></g>
{''.join(f'<path d="M{110+i*90} 174v-20" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(5))}''', arrow=True)

add('timeless', '時代が変わっても、形が古びない', f'''
{''.join(f'<g transform="translate({130+i*170} 210)"><rect x="-90" y="-110" width="180" height="220" rx="10" class="paper"/>'
         f'<path d="M-46 66q0-96 46-96t46 96z" class="tealp o"/><ellipse cx="0" cy="-30" rx="46" ry="16" class="teal o"/></g>' for i in range(3))}
{''.join(f'<path d="M{130+i*170} 340h60" fill="none" stroke="{MUTED}" stroke-width="0"/>' for i in range(1))}
{''.join(f'<path d="M{230+i*170} 210h40" class="a" marker-end="url(#ar)"/>' for i in range(2))}
{''.join(f'<circle cx="{130+i*170}" cy="352" r="12" class="{c} o"/>' for i, c in enumerate(['goldp','gold','goldd']))}''', arrow=True)

add('thickness', '板の厚さを、はしからはしまで測る', f'''
{table(340)}
<g transform="translate(300 260)"><path d="M-200-20h400v40h-400z" class="goldp o"/>
  <path d="M-200-20l40-30h400l-40 30z" class="gold o"/>
  <path d="M200-20l40-30v40l-40 30z" class="goldd o"/></g>
<path d="M120 240v40" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
<path d="M60 240h50M60 280h50" fill="none" stroke="{MUTED}" stroke-width="3"/>
<g fill="none" stroke="{CRL}" stroke-width="5"><path d="M96 200v-40"/></g>''', arrow=True)

# --- もの・人 ----------------------------------------------------------------

add('steering', 'ハンドルを回して、進む向きを変える', f'''
<path d="M0 306q160-40 300 0t300 40v54H0z" fill="#c3cbd1"/>
<path d="M0 340q160-40 300 0t300 30" fill="none" stroke="#ffffff" stroke-width="6" stroke-dasharray="30 24"/>
<g transform="translate(240 190)"><circle r="110" fill="none" stroke="{INK}" stroke-width="22"/>
  <circle r="30" class="teald o"/>
  <path d="M-96-30l72 18M96-30l-72 18M0 100V30" fill="none" stroke="{INK}" stroke-width="16"/></g>
{hand(140, 130, 1)}{hand(340, 130, -1)}
<path d="M370 90a90 90 0 0 1 30 60" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('stepfather', '母の再婚で、あとから父になった人', f'''
{person(150, 306, 1.15, 1, 'violet', 'blue', 'give', 'bun', 'smile')}
{person(450, 306, 1.2, -1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(300, 306, 0.72, 1, 'coral', 'green', 'up', 'bob', 'smile')}
<path d="M210 170h150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M300 190v-30" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M170 130q60-40 120 0" fill="none" stroke="{GRN}" stroke-width="5"/>
{ring(450, 210, 108)}''')

add('stepmother', '父の再婚で、あとから母になった人', f'''
{person(150, 306, 1.2, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(450, 306, 1.15, -1, 'violet', 'blue', 'give', 'bun', 'smile')}
{person(300, 306, 0.72, 1, 'coral', 'green', 'up', 'bob', 'smile')}
<path d="M210 170h150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M300 190v-30" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M170 130q60-40 120 0" fill="none" stroke="{GRN}" stroke-width="5"/>
{ring(450, 210, 108)}''')

add('technician', '道具を手に、機械のふたを開けて調整する', f'''
<g transform="translate(400 220)"><rect x="-130" y="-140" width="260" height="280" rx="12" class="teald o"/>
  <rect x="-110" y="-120" width="150" height="240" rx="6" fill="#dfe6ea"/>
  {''.join(f'<circle cx="{-80+ (i%3)*46}" cy="{-84+(i//3)*54}" r="14" class="{c} o"/>' for i, c in enumerate(['coral','gold','green','violet','blue','teal']))}
  <path d="M40-120h90v240H40z" fill="#c3ccd2" class="o" transform="rotate(-16 40 0)"/></g>
{person(160, 306, 1.2, 1, 'coral', 'blue', 'reach', 'cap', 'neutral')}
<g transform="translate(250 180) rotate(30)"><path d="M-8 0h16v70h-16z" class="ink"/>
  <path d="M-22-28h44v22h-16v10h-12v-10h-16z" class="ink"/></g>''')

add('trainee', '先輩に見てもらいながら、練習している研修生', f'''
{table(300)}
{person(200, 306, 1.15, 1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
{doc(300, 220, 130, 160, 4)}
{person(440, 306, 1.2, -1, 'violet', 'blue', 'point', 'bun', 'smile')}
<path d="M380 200h-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<g transform="translate(200 130)"><rect x="-30" y="-16" width="60" height="32" rx="8" class="coralp o"/></g>''')

add('toddler', 'よちよちと、はじめの数歩を歩く幼児', f'''
{table(340)}
<g transform="translate(300 306)">
  <path d="M-14-6l-10 32M14-6l10 32" fill="none" stroke="{BLUD}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-30-70q30-14 60 0l-10 64h-40z" fill="{CRL}" class="o"/>
  <path d="M-28-64l-30 20M28-64l30 20" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/>
  <circle cx="0" cy="-108" r="38" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-24-132q24-20 48 0" fill="none" stroke="{HAIR}" stroke-width="7" stroke-linecap="round"/>
  <circle cx="-13" cy="-110" r="4" class="ink"/><circle cx="13" cy="-110" r="4" class="ink"/>
  <path d="M-10-92q10 10 20 0" fill="none" stroke="{INK}" stroke-width="3"/></g>
{''.join(f'<ellipse cx="{140+i*46}" cy="{350+(i%2)*16}" rx="14" ry="7" class="ink"/>' for i in range(3))}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M420 210q16-16 0-32M470 250q16-16 0-32"/></g>''')

add('tights', '足からこしまで、ぴったり覆う衣類', f'''
<g transform="translate(300 200)">
  <path d="M-90-140h180v70q0 30-20 60l-30 150h-40l-10-150-10 150h-40l-30-150q-20-30-20-60z" class="violet o"/>
  <path d="M-90-140h180v24h-180z" class="violetd o"/>
  <path d="M0-70v40" fill="none" stroke="{VIOD}" stroke-width="4"/></g>''')

add('symphony', '大勢の奏者を、指揮者がひとつにまとめる', f'''
{''.join(f'<g transform="translate({100+ (i%4)*116} {250+(i//4)*80})">{head(0, 0, 24, c, h)}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun'),
                                     ('violet','short'),('blue','cap'),('teal','bob'),('coral','short')]))}
{''.join(f'<path d="M{124+ (i%4)*116} {236+(i//4)*80}l30-40" fill="none" stroke="{GLDD}" stroke-width="5"/>' for i in range(8))}
{person(300, 190, 1.0, 1, 'violet', 'blue', 'up', 'bun', 'smile')}
<path d="M348 60l40-30" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>''')

add('trumpet', 'ぱっと開いた朝顔口の金管楽器', f'''
<g transform="translate(300 210) rotate(-12)">
  <path d="M-190-14h240v28h-240z" class="gold o"/>
  <path d="M50-60q60 20 60 74t-60 74z" class="goldp o" transform="rotate(90 50 0)"/>
  <path d="M50 0m0-56q64 24 64 56t-64 56z" class="goldp o"/>
  {''.join(f'<rect x="{-120+i*46}" y="-44" width="22" height="34" rx="6" class="goldd o"/>' for i in range(3))}
  <path d="M-190-14q-40 0-40 14t40 14z" class="goldd o"/></g>
{''.join(f'<path d="M{430+i*22} {150-i*24}q18 18 0 36" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}''')

add('syrup', '重たくとろりと、金色の蜜が落ちる', f'''
{table(330)}
<g transform="translate(300 300)"><ellipse rx="110" ry="24" fill="#fffefd" class="o"/>
  {''.join(f'<ellipse cy="{-16-i*22}" rx="{76-i*6}" ry="20" fill="#e8c68f" class="o"/>' for i in range(3))}</g>
<g transform="translate(180 140) rotate(48)"><path d="M-30 0v-80h60V0z" class="goldp o"/>
  <path d="M30-60l40-14v34z" class="goldp o"/></g>
<path d="M272 152q6 40 0 80" fill="none" stroke="{GLD}" stroke-width="14" stroke-linecap="round"/>
<path d="M272 232q-4 20 0 34" fill="none" stroke="{GLD}" stroke-width="11" stroke-linecap="round"/>''')

add('tablespoon', '小さじと大さじ、大きいほうの計量スプーン', f'''
{table(330)}
{spoon(160, 250, 0.6, -18)}
{spoon(400, 246, 1.15, -12)}
{ring(400, 200, 100)}''')

add('synthetic', '植物からとる繊維と、工場でつくる繊維の対比', f'''
{split()}
<g transform="translate(150 300)"><path d="M0 0v-120" fill="none" stroke="{GRND}" stroke-width="7"/>
  {''.join(f'<circle cx="{-40+i*40}" cy="{-140+(i%2)*30}" r="30" fill="#fffefd" class="o"/>' for i in range(3))}
  <path d="M0-120q-34-6-40-40 32 2 40 30z" class="greenp o"/></g>
{ring(150, 200, 128, True)}
<g transform="translate(450 300)"><path d="M-100 0v-100h200V0z" fill="#dfe6ea" class="o"/>
  <path d="M-70-100v-40h30v40zM10-100v-60h30v60z" class="teald o"/>
  <path d="M-40-60h80v40h-80z" class="teal o"/></g>
{''.join(f'<path d="M{404+i*32} 160q-14-24 0-44" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{ring(450, 220, 132)}''')

add('telescopic', '筒がのびて、遠くを大きく見る', f'''
<g transform="translate(300 230) rotate(-16)">
  <rect x="-190" y="-26" width="130" height="52" rx="10" class="teald o"/>
  <rect x="-70" y="-34" width="130" height="68" rx="10" class="teal o"/>
  <rect x="50" y="-44" width="140" height="88" rx="12" class="tealp o"/>
  <path d="M-60-34v68M50-44v88" fill="none" stroke="{INK}" stroke-width="3"/></g>
<path d="M120 330h360" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
<g transform="translate(500 100)"><circle r="34" class="goldp o"/></g>
<path d="M400 150l60-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''', arrow=True)

add('therapeutic', '湯につかると、こわばりがほどけて楽になる', f'''
<g transform="translate(300 300)"><path d="M-190 60V-40q0-26 26-26h328q26 0 26 26V60z" class="tealp o"/>
  <path d="M-184-26h368" fill="none" stroke="{BLU}" stroke-width="5"/>
  <path d="M-190 0h380v60h-380z" fill="{BLUP}"/></g>
{head(300, 240, 30, 'coral', 'bun')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M170 200q-18-26 0-52 18-26 0-50M430 206q-18-26 0-52 18-26 0-50"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(220,130),(390,120)])}''')

add('thankless', '黙々と片づけても、だれも気づかず通り過ぎる', f'''
{person(180, 306, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'neutral')}
<g transform="translate(260 280) rotate(24)"><path d="M-8 0h16v-120h-16z" class="goldd o"/>
  <path d="M-40-120h80v40h-80z" class="gold o"/></g>
{person(430, 306, 1.0, 1, 'coral', 'green', 'walk', 'bob', 'smile')}
{person(530, 306, 1.0, 1, 'violet', 'blue', 'walk', 'short', 'smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M340 190h140"/></g>
{drop(150, 180, 1.0)}''')

add('swap', 'たがいの持ちものを、そっくり取りかえる', f'''
{person(130, 306, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(470, 306, 1.15, -1, 'coral', 'blue', 'give', 'bob', 'smile')}
{box(220, 200, 80, 58, 18, 'gold')}
{box(380, 200, 80, 58, 18, 'violet')}
<g fill="none" class="a" stroke-width="5">
  <path d="M240 130q60-40 120 0" marker-end="url(#ar)"/>
  <path d="M360 280q-60 40-120 0" marker-end="url(#ar)"/></g>''', arrow=True)

add('to be honest', '取りつくろうのをやめて、本当のところを話す', f'''
{person(160, 306, 1.2, 1, 'teal', 'blue', 'give', 'short', 'neutral')}
<g transform="translate(250 240) rotate(-24)"><ellipse rx="46" ry="56" fill="#fffefd" class="o"/>
  <circle cx="-16" cy="-10" r="6" class="ink"/><circle cx="16" cy="-10" r="6" class="ink"/>
  <path d="M-16 20q16 14 32 0" fill="none" stroke="{INK}" stroke-width="3"/></g>
<g transform="translate(430 170)"><rect x="-110" y="-70" width="220" height="140" rx="22" class="paper"/>
  <path d="M-92 56l-36 44 6-44z" class="paper"/>
  <path d="M-40 10l30 32 62-72" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
