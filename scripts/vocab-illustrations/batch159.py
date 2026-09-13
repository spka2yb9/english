# -*- coding: utf-8 -*-
"""第159回。f-/g-/h- の名詞と句動詞。"""
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

def torso(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0-190a44 44 0 1 1 0 88 44 44 0 1 1 0-88z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-90-96q90-30 180 0 20 130 0 226h-180q-20-96 0-226z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>')

def fish(x, y, s=1, f=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M-120 0q60-70 150-40 40 14 0 34-90 46-150 6z" class="{cls} o"/>'
            f'<path d="M30 0l60-40v80z" class="{cls} o"/>'
            f'<circle cx="-80" cy="-10" r="7" fill="#fffefd" class="o"/><circle cx="-80" cy="-10" r="3.5" class="ink"/></g>')

# --- 光・音 ------------------------------------------------------------------

add('gleam', 'みがいた刃に、ひとすじ光が走る', f'''
{table(340)}
<g transform="translate(280 250) rotate(-20)">
  <path d="M-160-16h240l40 16-40 16h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-200-14h40v28h-40z" class="goldd o"/>
  <path d="M-140-8h200" fill="none" stroke="#ffffff" stroke-width="8"/></g>
{spark(390, 150, 1.6)}''')

add('glitter', '細かい粒が、あちこちできらきらする', f'''
{table(340)}
<g transform="translate(300 300)"><path d="M-70 0q-16-60 0-70h140q16 10 0 70z" class="violetp o"/>
  <path d="M-74-70h148v-14h-148z" class="violet o"/></g>
{''.join(spark(x, y, 0.5 + (i % 3) * 0.16) for i, (x, y) in enumerate(
  [(150,120),(210,180),(270,110),(330,170),(390,120),(450,180),(180,250),(420,250),(240,60),(360,60),(120,200),(490,140)]))}''')

add('glare', 'まゆをつり上げて、じっとにらみつける', f'''
<g transform="translate(200 220)"><circle r="100" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="{HAIRS['short']}" transform="translate(0 448) scale(4.1)" fill="{HAIR}"/>
  <path d="M-64-28l40 18M64-28l-40 18" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cx="-34" cy="6" r="9" class="ink"/><circle cx="34" cy="6" r="9" class="ink"/>
  <path d="M-24 52h48" fill="none" stroke="{INK}" stroke-width="6"/></g>
<g fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M310 {170+i*22}h120"/>' for i in range(4))}</g>
{head(520, 250, 28, 'teal', 'bob')}''')

add('groan', 'いやな知らせに、思わずうめき声がもれる', f'''
{person(200, 306, 1.3, 1, 'blue', 'blue', 'hold', 'short', 'sad')}
<ellipse cx="200" cy="196" rx="12" ry="16" fill="{INK}"/>
<path d="M176 170l14 6M224 170l-14 6" fill="none" stroke="{INK}" stroke-width="3.5"/>
{''.join(f'<path d="M{270+i*30} {180+i*22}q20 16 0 32" fill="none" stroke="{MUTED}" stroke-width="6"/>' for i in range(3))}
<g transform="translate(470 250)">{doc(0, 0, 140, 170, 4)}
  <path d="M-40-30l80 80M40-30l-80 80" fill="none" stroke="{CRL}" stroke-width="6"/></g>''')

add('growl', '犬が牙を見せて、低くうなる', f'''
<g transform="translate(240 260)">
  <ellipse rx="94" ry="76" fill="#a8763f" class="o"/>
  <path d="M-94-40q-30-50 6-56 26-4 30 30zM94-40q30-50-6-56-26-4-30 30z" fill="#a8763f" class="o"/>
  <path d="M-44-26l24 10M44-26l-24 10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cx="-30" cy="-4" r="7" class="ink"/><circle cx="30" cy="-4" r="7" class="ink"/>
  <ellipse cy="26" rx="34" ry="24" fill="#6d4a26" class="o"/>
  <path d="M-40 44q40 30 80 0 0 30-40 30t-40-30z" fill="#6d2620" class="o"/>
  <path d="M-24 44l8 18 8-18M8 44l8 18 8-18" fill="#fffefd" stroke="{INK}" stroke-width="2"/></g>
{''.join(f'<path d="M{380+i*30} {200+i*26}q18 18 0 36" fill="none" stroke="{CRL}" stroke-width="6"/>' for i in range(3))}''')

add('glitch', '画面が一瞬だけ、帯状に乱れる', f'''
<g transform="translate(300 200)"><rect x="-230" y="-150" width="460" height="300" rx="14" class="teald o"/>
  <rect x="-206" y="-126" width="412" height="252" rx="6" fill="#dfe6ea"/>
  {''.join(f'<rect x="-170" y="{-96+i*44}" width="{300-(i%2)*80}" height="16" rx="8" fill="{MUTED}"/>' for i in range(5))}
  <rect x="-206" y="-20" width="412" height="34" fill="{CRLP}"/>
  <rect x="-140" y="-20" width="412" height="16" fill="{TEAP}"/>
  <rect x="-260" y="4" width="412" height="10" fill="{VIOP}"/></g>
{''.join(f'<path d="M{540+i*0} {120+i*40}h30" fill="none" stroke="{MUTED}" stroke-width="0"/>' for i in range(0))}''')

# --- 動き・自然 ---------------------------------------------------------------

add('gallop', '馬が四本の足を宙に浮かせて疾走する', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(330 260)">
  <path d="M-110-10q-16-60 40-76 80-22 150 6 46 18 40 60-10 44-80 44-104 6-150-34z" fill="#8a6a48" class="o"/>
  <path d="M110-40q26-40 60-24 32 16 14 50-14 26-46 24z" fill="#8a6a48" class="o"/>
  <path d="M164-30l40 6-38 18z" fill="#8a6a48" class="o"/>
  <path d="M122-56l-8-34 30 22zM152-62l14-32 12 30z" fill="#8a6a48" class="o"/>
  <circle cx="150" cy="-26" r="5" fill="#fffdf6"/>
  <path d="M-100 30l-56 40M-40 34l-50 46M50 34l60 40M100 26l70 30" fill="none" stroke="#8a6a48" stroke-width="14" stroke-linecap="round"/>
  <path d="M-110-20q-56-8-70-46 46 0 66 32z" fill="#6d5335" class="o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M150 160h-90M130 220h-100M170 290h-90"/></g>''')

add('germination', '土のなかで種が割れ、芽が地上へ出る', f'''
<path d="M0 220h600v180H0z" fill="#d9c9a4"/>
<path d="M0 220h600" fill="none" stroke="#c0ab7f" stroke-width="4"/>
{''.join(f'<g transform="translate({120+i*160} 300)">' + s + '</g>' for i, s in enumerate([
  f'<ellipse rx="30" ry="40" fill="#a8804f" class="o"/>',
  f'<ellipse rx="30" ry="40" fill="#a8804f" class="o"/><path d="M0-40v-30" fill="none" stroke="{GRND}" stroke-width="6"/><path d="M0 40v30" fill="none" stroke="#c8b48a" stroke-width="5"/>',
  f'<ellipse rx="26" ry="34" fill="#a8804f" class="o"/><path d="M0-34v-120" fill="none" stroke="{GRND}" stroke-width="7"/>'
  f'<path d="M0-120q-34-6-40-40 32 2 40 30zM0-136q34-8 40-42-34 4-40 32z" class="greenp o"/>'
  f'<path d="M0 34v40M0 50l-24 24M0 50l24 24" fill="none" stroke="#c8b48a" stroke-width="5"/>']))}
{''.join(f'<path d="M{200+i*160} 300h50" class="a" marker-end="url(#ar)"/>' for i in range(2))}''', arrow=True)

add('food chain', '草を虫が、虫を鳥が、鳥をきつねが食べる', f'''
<g transform="translate(80 300)"><path d="M0 0v-60" fill="none" stroke="{GRND}" stroke-width="6"/>
  <path d="M0-40q-30-6-34-34 28 2 34 24z" class="greenp o"/></g>
<g transform="translate(220 290)"><ellipse rx="30" ry="18" class="green o"/>
  <circle cx="-26" cy="-10" r="13" class="green o"/>
  <path d="M-34-20l-14-16M-22-24l-4-20" fill="none" stroke="{GRND}" stroke-width="3"/></g>
<g transform="translate(370 280)"><ellipse rx="44" ry="30" class="blue o"/>
  <circle cx="34" cy="-24" r="20" class="blue o"/>
  <path d="M50-26l24 6-22 12z" class="gold o"/>
  <circle cx="38" cy="-28" r="4" class="ink"/>
  <path d="M-44 6l-34 14 34 12" class="bluep o"/></g>
<g transform="translate(520 290) scale(0.32)">{beast(0, 0, 1, '#c06a34', -1)}</g>
{''.join(f'<path d="M{130+i*140} 200h60" class="a" marker-end="url(#ar)"/>' for i in range(3))}''', arrow=True)

add('gill', '魚のえら。水から息を取り入れる', f'''
<path d="M0 100h600v300H0z" fill="{BLUP}"/>
{fish(320, 220, 1.5, 1, 'teal')}
<g transform="translate(220 210)" fill="none" stroke="{TEAD}" stroke-width="7" stroke-linecap="round">
  <path d="M-14-30q18 30 0 60M8-34q20 34 0 68M30-30q18 30 0 60"/></g>
{ring(224, 210, 80)}
{''.join(f'<circle cx="{130-i*30}" cy="{200+i*30}" r="{8-i*2}" fill="none" stroke="{BLU}" stroke-width="3"/>' for i in range(3))}''')

add('fusion', '二つのものが、とけあって一つになる', f'''
<circle cx="130" cy="200" r="70" class="teal o"/>
<circle cx="470" cy="200" r="70" class="coral o"/>
<g fill="none" class="a" stroke-width="6">
  <path d="M212 200h60" marker-end="url(#ar)"/><path d="M388 200h-60" marker-end="url(#ar)"/></g>
<g transform="translate(300 200)"><circle r="86" class="violet o"/>
  <path d="M-86 0a86 86 0 0 1 86-86v172a86 86 0 0 1-86-86z" class="violetp"/></g>
{''.join(spark(x, y, 0.9) for x, y in [(300,80),(300,320)])}''', arrow=True)

# --- 数・変わり方 -------------------------------------------------------------

add('fluctuation', '上がったり下がったり、たえず揺れ動く', f'''
<path d="M60 340h480M90 360V70" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M100 220l50-90 50 130 50-100 50 120 50-80 50 110 50-90 50 70" fill="none" stroke="{TEA}" stroke-width="7"/>
{''.join(f'<circle cx="{100+i*50}" cy="{y}" r="8" class="teal o"/>' for i, y in enumerate([220, 130, 260, 160, 280, 200, 310, 220, 290]))}
<path d="M90 220h460" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>''')

add('fortnight', 'ちょうど二週間ぶんの日にち', f'''
<g transform="translate(300 200)"><rect x="-250" y="-150" width="500" height="300" rx="12" class="paper"/>
  <rect x="-250" y="-150" width="500" height="50" rx="0" class="teal o"/>
  {''.join(f'<rect x="{-226+ (i%7)*66}" y="{-80+(i//7)*70}" width="52" height="54" rx="6" fill="{"#f7e2c8" if i < 14 else "#eef2f4"}" stroke="{INK if i < 14 else "none"}" stroke-width="2"/>' for i in range(21))}
  <rect x="-232" y="-86" width="466" height="146" rx="8" fill="none" stroke="{CRL}" stroke-width="5"/></g>''')

add('for the time being', 'ひとまず今のところは、この形でいく', f'''
<path d="M60 220h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
<rect x="90" y="180" width="240" height="80" rx="10" class="tealp o"/>
<path d="M340 180h200" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M340 260h200" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M90 320h240" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
<g transform="translate(420 120)"><path d="M-14-30a26 26 0 1 1 22 42q-8 8-8 18" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="46" r="6" fill="{MUTED}"/></g>''', arrow=True)

add('for good', 'かぎをかけて、二度と開けないと決める', f'''
<g transform="translate(230 250)"><rect x="-100" y="-110" width="200" height="220" rx="10" fill="#fffefd" class="o"/>
  <rect x="-80" y="-90" width="160" height="180" rx="6" class="goldp o"/>
  <g transform="translate(60 0)"><rect x="-24" y="-16" width="48" height="40" rx="7" class="gold o"/>
    <path d="M-13-16v-14a13 13 0 0 1 26 0v14" fill="none" class="a"/></g></g>
<g transform="translate(470 160) rotate(30)"><path d="M-10 0h20v40h-20z" class="goldd o"/>
  <circle cy="-14" r="18" fill="none" stroke="{GLDD}" stroke-width="9"/>
  <path d="M10 20h14v10h-14zM10 34h14v10h-14z" class="goldd o"/></g>
<path d="M370 200q60-60 90 -30" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M470 240v90"/></g>''', arrow=True)

# --- 話・書きもの -------------------------------------------------------------

add('folklore', '年寄りが火のそばで、昔から伝わる話を語る', f'''
{sit(180, 340, 1.2, 1, 'violet', 'blue', 'bun', 'smile', 'lap')}
{chair(194, 340, 1.1, 'gold', -1)}
<g transform="translate(330 320) scale(0.6)">{flame(0, 0, 1)}</g>
{head(470, 330, 24, 'coral', 'short')}{head(530, 350, 22, 'teal', 'bob')}
<g transform="translate(400 130)"><ellipse rx="150" ry="90" fill="#fffefd" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="11 9" stroke-linejoin="round">
    <path d="M-90 40q-14-46 30-62 50-16 90 14 26 20 6 48"/>
    <path d="M-90 40q40 24 90 10"/><path d="M36 30q30-30 56-6-26 20-50 12"/>
    <path d="M-40 10l30-44 40 34"/></g>
  <circle cx="60" cy="24" r="4" class="ink"/></g>
<circle cx="250" cy="230" r="9" fill="#fffefd" class="o"/>''')

add('footnote', 'ページの下に、線を引いて添える短い注', f'''
{doc(300, 200, 380, 320, 0)}
{''.join(f'<rect x="130" y="{100+i*40}" width="{340-(i%2)*90}" height="14" rx="7" fill="{MUTED}"/>' for i in range(4))}
<g transform="translate(348 100)" stroke="{CRL}" stroke-width="5" stroke-linecap="round" fill="none">
  {''.join(f'<path d="M0 -12v24" transform="rotate({d})"/>' for d in [0, 60, 120])}</g>
<path d="M130 290h150" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(146 316)" stroke="{CRL}" stroke-width="4" stroke-linecap="round" fill="none">
  {''.join(f'<path d="M0 -9v18" transform="rotate({d})"/>' for d in [0, 60, 120])}</g>
<rect x="170" y="310" width="200" height="10" rx="5" fill="{MUTED}"/>
<rect x="170" y="330" width="150" height="10" rx="5" fill="{MUTED}"/>
<rect x="120" y="286" width="360" height="70" rx="8" fill="none" stroke="{CRL}" stroke-width="4"/>''')

add('foreword', '本文の前に、別の人が書き添える文', f'''
<g transform="translate(300 210)"><path d="M-230 130q100-40 220-14v-260q-120-26-220 14z" fill="#fffefd" class="o"/>
  <path d="M230 130q-100-40-220-14v-260q120-26 220 14z" fill="#fffefd" class="o"/>
  <path d="M-10-144v260" fill="none" stroke="{MUTED}" stroke-width="3"/>
  {''.join(f'<path d="M-200 {-94+i*40}q80-22 160-8" fill="none" stroke="{CRL}" stroke-width="6"/>' for i in range(4))}
  {''.join(f'<path d="M200 {-94+i*40}q-80-22-160-8" fill="none" stroke="{MUTED}" stroke-width="5"/>' for i in range(5))}
  <path d="M-190 76q60-16 100 6" fill="none" stroke="{VIO}" stroke-width="5"/></g>
{ring(180, 210, 150)}''')

add('glossary', '本の終わりにつける、ことばと意味の一覧', f'''
{doc(300, 200, 360, 300, 0)}
<path d="M150 110h300" fill="none" stroke="{INK}" stroke-width="4"/>
{word(230, 90, 3, 32, INK)}
{''.join(f'<g transform="translate(150 {150+i*46})">{word(46, 0, 2, 26, TEA)}'
         f'<rect x="106" y="-7" width="{200-(i%2)*60}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(4))}''')

add('gist', '長い書き物から、要点をひとつ取り出す', f'''
{doc(180, 200, 200, 250, 0)}
{''.join(f'<rect x="100" y="{110+i*46}" width="{160-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}
<rect x="100" y="202" width="160" height="12" rx="6" class="coral"/>
{magnifier(200, 208, 66, 24)}
<path d="M310 208h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 208)"><rect x="-100" y="-34" width="200" height="68" rx="12" class="paper"/>
  <rect x="-76" y="-7" width="152" height="14" rx="7" class="coral"/></g>''', arrow=True)

add('framing', '同じ景色でも、切り取り方で印象が変わる', f'''
{split()}
<g transform="translate(150 200)"><rect x="-110" y="-90" width="220" height="180" rx="6" class="goldd o"/>
  <rect x="-94" y="-74" width="188" height="148" fill="#eaf4fb"/>
  <path d="M-94 74l60-70 44 44 40-56 44 82z" fill="#c3cbd1" class="o"/>
  {sun(-40, -40, 20)}</g>
<g transform="translate(450 200)"><rect x="-110" y="-90" width="220" height="180" rx="6" class="goldd o"/>
  <rect x="-94" y="-74" width="188" height="148" fill="#eaf4fb"/>
  <path d="M-94 74l30-40 60 20 40-30 58 50z" fill="#8d949a" class="o"/>
  {cloud(-20, -40, 1.1, 'violet')}</g>''')

# --- 気持ち・性質 -------------------------------------------------------------

add('fondness', '古びても手ばなさない、お気に入り', f'''
{table(340)}
<g transform="translate(300 300)"><ellipse rx="66" ry="50" fill="#c08a5a" class="o"/>
  <circle cx="0" cy="-64" r="42" fill="#c08a5a" class="o"/>
  <circle cx="-34" cy="-92" r="18" fill="#c08a5a" class="o"/><circle cx="34" cy="-92" r="18" fill="#c08a5a" class="o"/>
  <circle cx="-14" cy="-70" r="5" class="ink"/><circle cx="14" cy="-70" r="5" class="ink"/>
  <ellipse cy="-50" rx="12" ry="9" fill="#8c6b42"/>
  <path d="M-62-20l-34 26M62-20l34 26M-30 46l-14 34M30 46l14 34" fill="none" stroke="#c08a5a" stroke-width="20" stroke-linecap="round"/>
  <path d="M-46 4l14 20M40-6l-12 22" fill="none" stroke="#8c6b42" stroke-width="3"/></g>
<g transform="translate(160 150)"><path d="M0 26q-46-34-46-64 0-24 22-24 14 0 24 14 10-14 24-14 22 0 22 24 0 30-46 64z" class="coralp o"/></g>
{head(490, 200, 26, 'teal', 'bob')}''')

add('gentleness', 'ねこの背を、そっとなでる', f'''
{table(340)}
<g transform="translate(340 300)"><ellipse rx="90" ry="46" fill="#c9a06c" class="o"/>
  <circle cx="-70" cy="-40" r="34" fill="#c9a06c" class="o"/>
  <path d="M-94-64l-8-30 26 16zM-52-70l14-28 12 28z" fill="#c9a06c" class="o"/>
  <circle cx="-82" cy="-42" r="4" class="ink"/><circle cx="-58" cy="-42" r="4" class="ink"/>
  <path d="M86-20q40-20 30-60" fill="none" stroke="#c9a06c" stroke-width="14" stroke-linecap="round"/></g>
{hand(300, 190, 1)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-linecap="round">
  <path d="M230 200h-40M240 170h-40M250 230h-40"/></g>
{''.join(spark(x, y, 0.6) for x, y in [(440,180),(500,240)])}''')

add('fragility', 'うすいガラスは、少しの力でひびが入る', f'''
{table(340)}
<g transform="translate(300 300)"><path d="M-50 0v-90q0-24 24-30h52q24 6 24 30V0z" fill="#eaf4fb" class="o"/>
  <path d="M-50 0h100" fill="none" class="o"/>
  <path d="M-20-120l14 40-20 30 22 34" fill="none" stroke="{CRL}" stroke-width="5"/>
  <path d="M30-110l-10 40 18 26" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{hand(160, 200, 1)}
<g transform="translate(470 190)"><path d="M0-44l44 76h-88z" class="gold o"/>
  <path d="M0-16v22" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="18" r="4" class="ink"/></g>''')

add('frenzy', '売り場に人がどっと押し寄せ、収拾がつかない', f'''
<g transform="translate(430 306)"><path d="M-120 0v-140h240V0z" fill="#fffefd" class="o"/>
  <path d="M-134-140h268l-30-40h-208z" class="coral o"/></g>
{''.join(f'<g transform="translate({70+i*80} {320+(i%2)*20}) rotate({-14+i*6})">{person(0, 0, 1.0, 1, c, "blue", "up", h, "surprised", "walk")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('violet','bob'),('gold','short'),('green','bun'),('blue','cap')]))}
{''.join(f'<path d="M{100+i*90} 130q16-20 0-40" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(4))}
{''.join(f'<rect x="-16" y="-10" width="32" height="20" rx="4" class="gold o" transform="translate({x} {y}) rotate({r})"/>' for x, y, r in [(200,150,30),(330,120,-24),(400,190,14)])}''')

add('greatness', 'はるかに大きな存在として、仰ぎ見られる', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<g transform="translate(320 306)">
  <path d="M-120 0v-40h240V0z" fill="#c3cbd1" class="o"/>
  <path d="M-70-40v-200h140v200z" fill="#dfe6ea" class="o"/>
  <circle cy="-282" r="46" fill="#e6ebee" class="o"/>
  <path d="M-70-240q0-56 70-56t70 56" fill="#e6ebee" class="o"/></g>
<g opacity="0.25"><path d="M440 306l120 94H440z" fill="{INK}"/></g>
{''.join(f'<g transform="translate({x} 370)">{head(0, 0, 20, c, h)}</g>' for x, (c, h) in zip([80, 150, 520], [('teal','short'),('coral','bob'),('gold','cap')]))}
{''.join(spark(x, y, 0.9) for x, y in [(180,90),(470,80)])}''')

add('foe', '線をはさんで向かい合う、相手がわ', f'''
<path d="M300 60v300" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="16 12"/>
{person(170, 306, 1.25, 1, 'teal', 'blue', 'point', 'cap', 'neutral')}
{person(430, 306, 1.25, -1, 'coral', 'blue', 'point', 'cap', 'neutral')}
<g transform="translate(120 150)"><path d="M0-40l40 24v32L0 40l-40-24v-32z" class="teal o"/></g>
<g transform="translate(480 150)"><path d="M0-40l40 24v32L0 40l-40-24v-32z" class="coral o"/></g>
<g fill="none" stroke="{CRL}" stroke-width="5"><path d="M250 230h-20M370 230h-20"/></g>''')

# --- しくみ・ふるまい ---------------------------------------------------------

add('focus on', 'レンズが光を集めて、一点に絞る', f'''
{''.join(f'<path d="M40 {120+i*30}h150" fill="none" stroke="{GLD}" stroke-width="6"/>' for i in range(7))}
<g transform="translate(240 210)"><path d="M0-140q60 140 0 280-60-140 0-280z" class="bluep o"/></g>
{''.join(f'<path d="M290 {120+i*30}L430 210" fill="none" stroke="{GLD}" stroke-width="6"/>' for i in range(7))}
<circle cx="436" cy="210" r="16" class="coral o"/>
{ring(436, 210, 48)}''')

add('foresight', '来るものを先に見て、いまのうちに備える', f'''
{cloud(470, 90, 1.6, 'violet')}
{''.join(f'<path d="M{410+i*36} 150v34" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>' for i in range(4))}
{person(160, 330, 1.2, 1, 'teal', 'blue', 'hold', 'cap', 'neutral')}
<g transform="translate(206 216)"><rect x="-12" y="-16" width="52" height="32" rx="10" class="ink"/>
  <circle cx="42" cy="0" r="9" class="bluep o"/></g>
<path d="M256 214l150-70" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
<g transform="translate(260 300)"><path d="M-40 0v-90" fill="none" stroke="{GLDD}" stroke-width="7"/>
  <path d="M-90-90q50-54 100 0z" class="coral o"/></g>''')

add('for the sake of', '自分のためではなく、この人のためにする', f'''
{person(150, 306, 1.25, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{box(290, 240, 90, 64, 20, 'gold')}
<path d="M356 200h70" class="a" stroke-width="6" marker-end="url(#ar)"/>
{person(490, 306, 1.15, -1, 'coral', 'blue', 'reach', 'bob', 'smile')}
<g transform="translate(490 130)"><path d="M0 26q-40-30-40-56 0-20 20-20 12 0 20 12 8-12 20-12 20 0 20 20 0 26-40 56z" class="coralp o"/></g>''', arrow=True)

add('get on with', '肩を並べて、うまくやっていく', f'''
{table(300)}
{person(210, 380, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
{person(390, 380, 1.2, -1, 'coral', 'blue', 'reach', 'bob', 'smile')}
{doc(300, 250, 130, 150, 4)}
<path d="M210 260q90-40 180 0" fill="none" stroke="{SKIN}" stroke-width="0"/>
{''.join(spark(x, y, 0.8) for x, y in [(150,150),(450,150)])}
<g transform="translate(300 120)"><path d="M0 20q-30-24-30-44 0-16 16-16 10 0 14 10 4-10 14-10 16 0 16 16 0 20-30 44z" class="coralp o"/></g>''')

add('get to grips with', 'そでをまくり、大きな問題に正面から取りかかる', f'''
<g transform="translate(400 240)"><path d="M-120 90q-30-100 30-140 80-52 160 6 50 36 20 134z" fill="#8d949a" class="o"/>
  {''.join(f'<path d="M{-80+i*40} 70q10-60 {14-i*6}-110" fill="none" stroke="#6f787d" stroke-width="4"/>' for i in range(4))}</g>
{person(150, 330, 1.3, 1, 'coral', 'blue', 'reach', 'short', 'neutral')}
<path d="M120 226h60" fill="none" stroke="{CRL}" stroke-width="14"/>
{hand(260, 240, 1)}
{drop(110, 200, 0.9)}''')

add('hamper', '足におもりがついていて、思うように進めない', f'''
<path d="M40 340h520" fill="none" stroke="{GLDD}" stroke-width="8" stroke-dasharray="18 14"/>
{person(250, 340, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'sad', 'walk')}
<path d="M230 340q-40 20-60 0" fill="none" stroke="{INK}" stroke-width="6"/>
<g transform="translate(150 348)"><path d="M-46 30l14-52h64l14 52z" fill="#5b6b78" class="o"/>
  <path d="M-16-22v-8a16 16 0 0 1 32 0v8" fill="none" stroke="{INK}" stroke-width="6"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M360 260h50M370 200h50"/></g>
{drop(230, 200, 0.9)}''')

# --- 罪・守り ----------------------------------------------------------------

add('guardian', '子のそばに立って、まもる大人', f'''
{person(230, 306, 1.35, 1, 'violet', 'blue', 'stand', 'bun', 'neutral')}
{person(360, 306, 0.72, 1, 'coral', 'green', 'stand', 'bob', 'smile')}
<path d="M290 190q60 20 70 60" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(300 130)"><path d="M0-70q40 16 56 22 0 60-56 86-56-26-56-86 16-6 56-22z" class="tealp o"/></g>
{ring(230, 210, 128)}''')

add('guardianship', '書面で正式に、後見の役目が定められる', f'''
{table(300)}
{doc(250, 200, 220, 250, 0)}
{''.join(f'<rect x="160" y="{110+i*44}" width="{180-(i%2)*60}" height="14" rx="7" fill="{MUTED}"/>' for i in range(4))}
<circle cx="310" cy="290" r="34" fill="none" stroke="{CRL}" stroke-width="6"/>
{head(120, 330, 26, 'violet', 'bun')}
{head(180, 360, 20, 'coral', 'bob')}
<path d="M150 300q30-30 60 0" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g transform="translate(470 190)"><path d="M-30 40h60v20h-60z" class="teald o"/>
  <path d="M-16-40h32v80h-32z" class="teal o"/><path d="M-30-56h60v18h-60z" class="teald o"/></g>''')

add('guilty of', '残った証拠が本人と結びつき、罪が認められる', f'''
{person(160, 306, 1.2, 1, 'coral', 'blue', 'hold', 'short', 'sad')}
<g transform="translate(330 250) rotate(-12)">
  <path d="M-60 60q-16-70 10-104 24-30 56-14 30 16 20 60-8 36-30 58-30 18-56 0z" fill="#8a7a5e" class="o"/></g>
<path d="M220 250h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(490 180) rotate(24)"><path d="M-10 0h20v60h-20z" class="goldd o"/>
  <path d="M-34-32h68v34h-68z" class="goldd o"/></g>
<g transform="translate(490 280)"><rect x="-60" y="-12" width="120" height="24" rx="6" class="goldd o"/></g>''')

add('genocide', 'ひとつの民のすべてが、消し去られる', f'''
{''.join(f'<g transform="translate({80+i*80} 260)">{head(0, 0, 26, "teal", "short")}</g>' for i in range(2))}
{''.join(f'<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="11 9">'
         f'<circle cx="{240+i*80}" cy="260" r="26"/>'
         f'<path d="M{214+i*80} 300q26-14 52 0l-8 34h-36z"/></g>' for i in range(4))}
<g transform="translate(300 380)"><path d="M-30-40h60v40h-60z" fill="#dfe6ea" class="o"/>
  <path d="M0-40v-16" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M0-56q-14-16 0-30 14 14 0 30z" class="coral o"/></g>
<g opacity="0.7">{cloud(300, 100, 1.8, 'violet')}</g>''')

add('forfeit', '罰として、手にしていたものを取り上げられる', f'''
{person(180, 306, 1.2, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<g opacity="0.35">{box(180, 200, 90, 64, 20, 'gold')}</g>
{box(430, 220, 90, 64, 20, 'gold')}
<path d="M250 180h120" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
{hand(520, 150, -1)}
<g transform="translate(300 330)"><path d="M0-30l30 52h-60z" class="gold o"/>
  <path d="M0-10v10" fill="none" stroke="{INK}" stroke-width="4"/><circle cy="12" r="3" class="ink"/></g>''', arrow=True)

add('gulf', '両側のあいだに、越えられないほどの隔たり', f'''
<path d="M0 306h190v94H0zM410 306h190v94H410z" class="ground"/>
<path d="M190 306l40 94h-40zM410 306l-40 94h40z" fill="#5b6b78"/>
<path d="M190 306v94M410 306v94" fill="none" stroke="{INK}" stroke-width="3"/>
{''.join(f'<g transform="translate({70+i*70} 306)">{person(0, 0, 1.0, 1, c, "blue", "reach", h, "neutral")}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob')]))}
{''.join(f'<g transform="translate({470+i*70} 306)">{person(0, 0, 1.0, -1, c, "blue", "reach", h, "neutral")}</g>' for i, (c, h) in enumerate([('violet','short'),('gold','bun')]))}
<path d="M210 160h180" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('hallmark', '銀器に打たれた、それと分かる刻印', f'''
{table(340)}
<g transform="translate(280 290)"><path d="M-70 0q-24-80 0-100 70-22 140 0 24 20 0 100z" fill="#dfe6ea" class="o"/>
  <path d="M-76-100h152v-16h-152z" fill="#c3ccd2" class="o"/>
  <path d="M-50-80q50 16 100 0" fill="none" stroke="#b0bac0" stroke-width="4"/></g>
<g transform="translate(280 250)"><path d="M-26-16h52v32h-52z" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M0-8l8 8-8 8-8-8z" class="ink"/></g>
{magnifier(400, 250, 62, 24)}
{''.join(spark(x, y, 0.7) for x, y in [(160,150),(470,150)])}''')

# --- からだ・もの -------------------------------------------------------------

add('gland', '体のなかで、必要な液をつくり出す小さな器官', f'''
{torso(300, 300, 1.0)}
<g transform="translate(300 200)"><ellipse rx="46" ry="34" class="violet o"/>
  {''.join(f'<circle cx="{-24+i*24}" cy="{-8+(i%2)*16}" r="10" class="violetp o"/>' for i in range(3))}
  <path d="M0 34v30" fill="none" stroke="{VIOD}" stroke-width="6"/>
  {drop(-6, 66, 1.0, 'blue')}</g>
{ring(300, 200, 76)}''')

add('floorboard', '床に張られた、細長い木の板', f'''
<g transform="translate(300 240)">
  {''.join(f'<rect x="-260" y="{-120+i*46}" width="520" height="42" rx="4" fill="#c9a06c" class="o"/>' for i in range(6))}
  {''.join(f'<path d="M{-180+i*130} {-120+ (i%2)*46}v42" fill="none" stroke="#a8804f" stroke-width="3"/>' for i in range(4))}</g>
<g transform="translate(180 130) rotate(-16)"><rect x="-140" y="-20" width="280" height="42" rx="4" fill="#d9b57a" class="o"/></g>
{ring(180, 140, 152)}''')

add('hardback', 'かたい表紙でしっかり綴じた本', f'''
{table(340)}
<g transform="translate(300 306)"><path d="M-100 0v-240h200V0z" class="teald o"/>
  <path d="M-84 0v-224h172V0z" fill="#fffefd" class="o"/>
  <path d="M-100-240h200v18h-200z" class="teal o"/>
  <path d="M-100 0h200v18h-200z" class="teal o"/>
  <rect x="-50" y="-180" width="110" height="16" rx="8" class="teal"/>
  <rect x="-50" y="-146" width="80" height="12" rx="6" fill="{MUTED}"/></g>
{''.join(f'<path d="M196 {-40+i*0}h1" fill="none"/>' for i in range(0))}
<path d="M180 306v-240" fill="none" stroke="{TEAD}" stroke-width="10"/>''')

add('garnish', '仕上げに、緑の葉をひとつ添える', f'''
{table(320)}
<g transform="translate(300 280)"><ellipse rx="110" ry="30" fill="#fffefd" class="o"/>
  <ellipse cy="-16" rx="66" ry="26" class="goldp o"/>
  <path d="M-30-30q30-20 60 0" fill="none" stroke="{GLDD}" stroke-width="4"/></g>
<g transform="translate(330 220)"><path d="M0 30V0" fill="none" stroke="{GRND}" stroke-width="5"/>
  <path d="M0 0q-30-6-34-34 28 2 34 24zM0-16q30-8 34-36-28 4-34 26z" class="greenp o"/></g>
{hand(400, 130, -1)}
<path d="M370 170l-24 30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('fringe', 'ひたいにかかる、切りそろえた前髪', f'''
<g transform="translate(300 210)"><circle r="120" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-120-20q0-110 120-110t120 110q-20-30-56-24-30-26-64-6-40-22-64 8-30-8-56 22z" fill="{HAIR}"/>
  {''.join(f'<path d="M{-100+i*30} -34v-30" fill="none" stroke="#26374a" stroke-width="3"/>' for i in range(7))}
  <circle cx="-42" cy="18" r="9" class="ink"/><circle cx="42" cy="18" r="9" class="ink"/>
  <path d="M-26 62q26 22 52 0" fill="none" stroke="{INK}" stroke-width="5"/></g>
{ring(300, 130, 152)}''')

add('given that', 'この前提を認めるなら、こうなる', f'''
<g transform="translate(160 190)"><rect x="-110" y="-80" width="220" height="160" rx="10" class="tealp o"/>
  {''.join(f'<rect x="-84" y="{-46+i*40}" width="{170-(i%2)*50}" height="14" rx="7" fill="{TEAD}"/>' for i in range(3))}</g>
{ring(160, 190, 128)}
<path d="M300 190h60" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(470 190)"><rect x="-100" y="-70" width="200" height="140" rx="10" class="paper"/>
  <path d="M-40 10l26 28 52-60" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
