# -*- coding: utf-8 -*-
"""第145回の描き直し。読み取れなかった6枚。"""
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

def warn(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0-44l44 76h-88z" class="gold o"/>'
            f'<path d="M0-16v22" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cy="18" r="4" class="ink"/></g>')

add('as a matter of fact', '小さく見せていた板をどけると、後ろに大きな本当のものが現れる', f'''
{table(330)}
<g transform="translate(430 300)"><path d="M-90 0l90-166 90 166z" class="coral o"/></g>
<g transform="translate(220 300) rotate(-24)"><rect x="-84" y="-120" width="168" height="120" rx="8" class="paper"/>
  <path d="M-30-30l30-56 30 56z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g>
{hand(150, 170, 1)}
<path d="M258 138h96" class="a" marker-end="url(#ar)"/>
{head(540, 220, 26, 'teal', 'short')}''', arrow=True)

add('facilitation', '通り道の石をどけて、後ろの人が進みやすいようにする', f'''
<path d="M40 330h520" fill="none" stroke="{GLDD}" stroke-width="12" stroke-dasharray="20 14"/>
<circle cx="300" cy="140" r="46" fill="#b9c1c6" class="o"/>
<g opacity="0.4"><circle cx="300" cy="296" r="46" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/></g>
<path d="M300 232v-40" class="a" stroke-width="5" marker-end="url(#ar)"/>
{person(370, 306, 1.05, -1, 'teal', 'blue', 'up', 'short', 'smile')}
{person(120, 306, 1.05, 1, 'coral', 'green', 'walk', 'bob', 'smile')}
<path d="M180 250h70" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('indulgence', 'ほしがるままに、両手にあふれるほど与えてしまう', f'''
{person(160, 306, 1.15, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
{person(470, 306, 0.86, -1, 'coral', 'green', 'up', 'short', 'smile')}
<g transform="translate(320 250)">
  {box(0, 46, 96, 60, 20, 'gold')}
  {box(-16, -14, 76, 50, 16, 'coral')}
  {box(20, -70, 66, 44, 14, 'violet')}
</g>
{''.join(spark(x, y, 0.9) for x, y in [(250,120),(410,110)])}
<path d="M232 190h40" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('madness', '深い割れ目を三輪車で跳び越そうとする、正気とは思えない企て', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<path d="M214 306l26 40-18 54h180l-22-56 28-38z" fill="#5b6b78"/>
<path d="M214 306l26 40-18 54M400 306l-28 38 22 56" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(140 306)">
  <circle cx="-34" cy="-26" r="26" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="34" cy="-14" r="14" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-34-52l24-34h44v58" fill="none" stroke="{CRLD}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-10-86h-28" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
{person(130, 220, 0.8, 1, 'coral', 'blue', 'up', 'cap', 'surprised')}
<path d="M216 140q90-56 168 30" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
{warn(300, 96, 0.9)}
{head(510, 250, 28, 'teal', 'bob')}
{drop(546, 210, 1.1, 'blue')}''')

add('recourse', '板でふさがれた扉が並ぶなか、開いている一つにたよる', f'''
{''.join(f'<g transform="translate({120+i*160} 220)"><path d="M-58-96h116v192h-116z" fill="#fffefd" class="o"/>'
         f'<path d="M-70-50h140v22h-140zM-70 30h140v22h-140z" class="goldd o" transform="rotate({-8+i*16})"/></g>' for i in range(2))}
<g transform="translate(440 220)"><path d="M-58-96h116v192h-116z" class="greenp o"/>
  <path d="M-58-96h44v192h-44z" fill="#fffefd" class="o"/>
  <circle cx="-24" cy="10" r="7" class="ink"/></g>
{person(300, 384, 0.66, 1, 'teal', 'blue', 'walk', 'short', 'neutral')}
<path d="M336 350h64" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('in need of', 'うしろのタイヤがつぶれた自転車に、空気入れが要る', f'''
{table(346)}
<g transform="translate(190 302)">
  <circle cx="-72" cy="-42" r="48" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M72-42m-48 0a48 30 0 1 0 96 0 48 30 0 1 0-96 0" fill="none" stroke="{CRL}" stroke-width="8"/>
  <path d="M-72-42l34-62h56l54 62M-38-104l-20 0M56-104l-14-16h-26" fill="none" stroke="{TEA}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-38-104L72-42" fill="none" stroke="{TEA}" stroke-width="7"/>
</g>
<path d="M336 220h56" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 302)"><path d="M-24-104h48v104h-48z" class="blue o"/>
  <path d="M0-104v-32h-26" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M24-32h54" fill="none" stroke="{INK}" stroke-width="7"/></g>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet2.html', 3))
