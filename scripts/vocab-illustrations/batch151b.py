# -*- coding: utf-8 -*-
"""第151回の描き直し。2枚。"""
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

add('unattended', 'ベンチに荷物だけが残され、持ち主の姿がない', f'''
<g transform="translate(300 306)"><path d="M-200-24h400v24h-400z" class="goldd o"/>
  <path d="M-170 0v70M170 0v70M-200-24v-70h400v70" fill="none" stroke="{GLDD}" stroke-width="10"/></g>
<g transform="translate(200 274)"><path d="M-46 24v-70h92v70z" class="violet o"/>
  <path d="M-20-46v-16h40v16" fill="none" class="a"/>
  <path d="M-46-10h92" fill="none" stroke="{TONES['violet'][2]}" stroke-width="4"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="12 10" stroke-linecap="round">
  <circle cx="420" cy="196" r="26"/>
  <path d="M394 236q26-14 52 0l-8 70h-36z"/>
  <path d="M394 240l-20 44M446 240l20 44"/>
  <path d="M406 306l-8 34M434 306l8 34"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M264 200h96"/></g>''')

add('undeniable', '大きな泥の足あとと、同じ形の泥だらけのくつ', f'''
{table(340)}
<g transform="translate(230 250) rotate(-12)">
  <path d="M-60 60q-16-70 10-104 24-30 56-14 30 16 20 60-8 36-30 58-30 18-56 0z" fill="#8a7a5e" class="o"/>
  {''.join(f'<ellipse cx="{-46+i*26}" cy="{-86-(i%2)*10}" rx="12" ry="10" fill="#8a7a5e" stroke="{INK}" stroke-width="2.5"/>' for i in range(4))}</g>
{person(470, 306, 1.15, -1, 'coral', 'blue', 'reach', 'short', 'surprised')}
<g transform="translate(430 340) rotate(-6)"><path d="M-40 14q-8-24 6-30 20-8 34 4l24 14q10 6 4 12h-68z" fill="#8a7a5e" class="o"/></g>
<path d="M370 210h-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round">
  <path d="M330 300q10-16 26-16"/></g>''')

print(sheet(W, '/tmp/vocab-sheet2.html', 2))
