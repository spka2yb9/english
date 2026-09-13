# -*- coding: utf-8 -*-
"""第136回の描き直し。arrogant の組んだ腕が顔にかかった。"""
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


# 組んだ腕を胸の高さと勘違いして顔の位置に置いた。
# person(x,y,s) の顔の中心は y - 108*s。腕は y - 78*s より下に置く。
add('arrogant', 'あごを上げ、腕を組んで人を見下す', f'''
{table(380)}
{person(300, 380, 1.3, 1, 'violet', 'blue', 'hold', 'short', 'neutral')}
<g transform="translate(300 300)">
  <path d="M-62 0q62-26 124 0" stroke="{SKIN}" stroke-width="20" stroke-linecap="round" fill="none"/>
  <path d="M-52 22q56-22 108 0" stroke="{SKIN}" stroke-width="18" stroke-linecap="round" fill="none"/>
  <path d="M-62 0q62-26 124 0M-52 22q56-22 108 0" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(300 240)">
  <path d="M-28-14q14-10 26 0M2-14q14-10 26 0" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round" transform="translate(-2 0)"/>
  <path d="M-14 14h28" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M300 200v-40"/></g>
{head(110, 350, 22, 'coral', 'bob')}
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M240 260l-90 60"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
