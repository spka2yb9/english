# -*- coding: utf-8 -*-
"""第144回の描き直し。読み取れなかった10枚。"""
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

def spark(x, y, s=1, cls='gold'):
    return (f'<path d="M{x} {y-16*s}l{5*s} {11*s} {11*s} {5*s}-{11*s} {5*s}-{5*s} {11*s}'
            f'-{5*s}-{11*s}-{11*s}-{5*s} {11*s}-{5*s}z" class="{cls} o"/>')

def beaker(x, y, level, mark=0.7):
    """必要量の破線に対して level まで入った容器。suffice と deficient で同じ絵を使う。"""
    h, w = 160, 112
    fh = h * level
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M{-w/2+5} {-fh}h{w-10}v{fh-6}q0 6-8 6h{-w+26}q-8 0-8-6z" class="blue"/>'
            f'<path d="M{-w/2} {-h}v{h-8}q0 8 10 8h{w-20}q10 0 10-8v{-h+8}" fill="none" class="o"/>'
            f'<path d="M{-w/2-26} {-h*mark}h{w+52}" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="11 9"/>'
            f'<path d="M{-w/2-14} {-h*mark}v0" fill="none"/></g>')

# 1 危険をそらす
add('avert', '転がってきた岩の進路をそらして家をまもる', f'''
<g transform="translate(110 246)"><circle r="46" fill="#b9c1c6" class="o"/>
  <path d="M-18-16l16 10-8 18M14-22l10 16" fill="none" stroke="{INK}" stroke-width="3"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M42 214h-30M36 246h-38M42 278h-30"/></g>
<path d="M166 246h180" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M240 246q70 4 84-90" class="a" stroke-width="6" marker-end="url(#ar)"/>
<g transform="translate(470 250)">{building(0, 56, 0.72, 'teal')}</g>
{person(310, 306, 1.0, -1, 'coral', 'blue', 'reach', 'short', 'neutral')}''', arrow=True)

# 2 耳が聞こえなくなる
add('deafen', '大音量が押し寄せ、両手で耳をふさぐ', f'''
<g transform="translate(96 200)"><path d="M-40-40h34l56-46v172l-56-46h-34z" class="teal o"/></g>
{''.join(f'<path d="M160 {200-46-i*30}q{46+i*30} {46+i*30} 0 {(46+i*30)*2}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for i in range(4))}
<g transform="translate(440 306)">
  <path d="M-14-8l-8 34M14-8l8 34" fill="none" stroke="{BLUD}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-78q26-13 52 0l-8 72h-36z" fill="{CRL}" class="o"/>
  <path d="M-22-72L-46-104M22-72L46-104" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-112" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 -4)" fill="{HAIR}"/>
  <path d="M-14-116l12 8M14-116l-12 8" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-9-96q9-8 18 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="-46" cy="-108" r="13" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cx="46" cy="-108" r="13" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<path d="M508 154q18-16 6-38" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>''')

# 3 続けてきたものを打ち切る
add('discontinue', '並んで出てきた品が、赤い止め板から先はもう作られない', f'''
<path d="M40 300h520v16H40z" class="teald o"/>
{''.join(box(96 + i*92, 292, 68, 52, 16, 'gold') for i in range(3))}
<path d="M336 130v170" stroke="{CRL}" stroke-width="16" stroke-linecap="round" fill="none"/>
<path d="M336 150h180" stroke="{CRL}" stroke-width="16" stroke-linecap="round" fill="none"/>
{''.join(f'<path d="M{382 + i*92 - 34} 240h68v52h-68z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/>' for i in range(2))}
<path d="M96 200h150" class="a" marker-end="url(#ar)"/>''', arrow=True)

# 4 先手を打って防ぐ
add('forestall', '倒れかけた積み木に、倒れる前につっかい棒をあてる', f'''
<g opacity="0.3">{''.join(f'<rect x="{300+i*60}" y="272" width="54" height="30" rx="5" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>' for i in range(3))}</g>
<g transform="translate(180 306) rotate(16)">
  {''.join(f'<rect x="-46" y="{-56-i*54}" width="92" height="50" rx="8" class="teal o"/>' for i in range(4))}
</g>
<path d="M296 300l-56-118" stroke="{GLDD}" stroke-width="18" stroke-linecap="round" fill="none"/>
{person(420, 306, 1.15, -1, 'coral', 'blue', 'reach', 'short', 'neutral')}''')

# 5 もう一度火をつける
add('reignite', '消えたろうそくに、もう一度火をともす', f'''
{split()}
{table(300)}
<g transform="translate(160 300)"><path d="M-24-104h48v104h-48z" fill="#fffefd" class="o"/>
  <path d="M0-104v-14" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-2-124q-16-16 4-30M8-142q18-14 2-30" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
<path d="M232 200h132" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 300)"><path d="M-24-104h48v104h-48z" fill="#fffefd" class="o"/>
  <path d="M0-104v-12" fill="none" stroke="{INK}" stroke-width="4"/></g>
<g transform="translate(431 188) scale(0.46)">{flame(0, 0, 1)}</g>''', arrow=True)

# 6 / 7 足りる・足りない（同じ絵で線に届くかどうかだけ変える）
add('suffice', '必要量の破線にちょうど届くまで入っている', f'''
{beaker(280, 320, 0.70)}
{head(500, 268, 28, 'green', 'short')}
<path d="M448 200l-96 0" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('deficient', '必要量の破線にとどかず、足りない分が空いている', f'''
{beaker(280, 320, 0.34)}
<path d="M280 240v-56" fill="none" stroke="{CRL}" stroke-width="5" marker-end="url(#ar)"/>
{head(500, 268, 28, 'coral', 'short')}
<path d="M448 200l-96 0" class="a" marker-end="url(#ar)"/>''', arrow=True)

# 8 抜け目がない
add('astute', 'うまい話の下に隠れた釣り針を、虫めがねで見つける', f'''
{box(190, 160, 130, 96, 28, 'gold')}
{spark(110, 74, 0.9)}{spark(272, 66, 0.8)}
<path d="M190 210v46q0 34 34 34t34-28" fill="none" stroke="{CRL}" stroke-width="11" stroke-linecap="round"/>
<path d="M258 262l-14 12 20 6z" class="coral o"/>
<g transform="translate(226 268) rotate(24)"><circle r="78" fill="#ffffff" opacity="0.16" stroke="{INK}" stroke-width="7"/>
  <path d="M0 78v46" stroke="{INK}" stroke-width="17" stroke-linecap="round"/></g>
{head(470, 250, 34, 'teal', 'short')}
<path d="M486 224l16-10" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>''')

# 10 実在しない
add('fictional', '開いた本の上に、破線で描かれた実在しない城が浮かぶ', f'''
{table(330)}
<g transform="translate(260 312)">
  <path d="M-116 0q56-26 112-8v-72q-56-18-112 8z" fill="#fffefd" class="o"/>
  <path d="M116 0q-56-26-112-8v-72q56-18 112 8z" fill="#fffefd" class="o"/>
  <path d="M-4-80v72" fill="none" stroke="{MUTED}" stroke-width="3"/>
  {''.join(f'<path d="M{-96+0} {-62+i*18}q40-14 78-6" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for i in range(3))}
  {''.join(f'<path d="M96 {-62+i*18}q-40-14-78-6" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for i in range(3))}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="12 9" stroke-linejoin="round" stroke-linecap="round">
  <path d="M170 236v-96h44v-30l22-26 22 26v30h44v96z"/>
  <path d="M302 236v-124h40v-26l20-24 20 24v26h40v124z"/>
  <path d="M214 236v-46h40v46"/>
  <path d="M346 236v-40h32v40"/>
  <path d="M362 62v-34l40 12-40 12"/>
  <path d="M258 84v-26l36 10-36 10"/>
</g>
{spark(140, 120, 0.9)}{spark(468, 96, 0.8)}''')

print(sheet(W, '/tmp/vocab-sheet2.html', 4))
