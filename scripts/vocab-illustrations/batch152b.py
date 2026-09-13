# -*- coding: utf-8 -*-
"""第152回の描き直し。2枚。"""
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

GLDD = TONES['gold'][2]
CRL = TONES['coral'][0]
VIO, VIOP, VIOD = TONES['violet']

add('untenable', '足もとの岩が割れて崩れ、その場に立っていられない', f'''
<path d="M0 306h240v94H0z" class="ground"/>
<path d="M240 306l30 94h-30z" fill="#5b6b78"/>
<path d="M240 306v94" fill="none" stroke="{INK}" stroke-width="3"/>
<path d="M0 306h240v40H0z" fill="#c3cbd1" class="o"/>
<g transform="translate(300 330) rotate(24)"><path d="M-40-16h80v34h-80z" fill="#c3cbd1" class="o"/></g>
<g transform="translate(360 380) rotate(-38)"><path d="M-30-14h60v28h-60z" fill="#c3cbd1" class="o"/></g>
<path d="M196 306v40M170 306l10 40" fill="none" stroke="{INK}" stroke-width="3"/>
{person(150, 306, 1.2, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M60 180q16-20 0-40M250 170q-16-20 0-40"/></g>''')

add('wind up', '会が終わり、いすを重ねてコードを巻き取る', f'''
<g transform="translate(140 306)">
  {''.join(f'<g transform="translate(0 {-i*40})"><path d="M-70-20h140v20h-140z" class="violet o"/>'
           f'<path d="M-70-20v-70h20v70z" class="violetd o"/></g>' for i in range(3))}
  <path d="M-56 0v40M56 0v40" fill="none" stroke="{VIOD}" stroke-width="10" stroke-linecap="round"/></g>
{person(470, 306, 1.25, -1, 'teal', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(390 210)"><circle r="56" fill="none" stroke="{INK}" stroke-width="12"/>
  <circle r="30" fill="none" stroke="{INK}" stroke-width="12"/>
  <path d="M-56 0q-60 30-90-4" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0-56a56 56 0 0 1 40 20" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/></g>''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet2.html', 2))
