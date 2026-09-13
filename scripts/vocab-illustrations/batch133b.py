# -*- coding: utf-8 -*-
"""第133回の描き直し。saddle が馬に見えなかった。"""
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


# 鞍を馬の上に重ねたら、馬の背中が鞍に食われて別の生き物になった。
# 馬を大きく描き、鞍は背の一点にだけ小さく載せ、あぶみを下げて「鞍だ」と分かるようにする。
add('saddle', '馬の背に鞍を置き、あぶみを下げて締める', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#dfe8d8"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(290 300)">
  <ellipse cx="0" cy="-50" rx="130" ry="62" fill="#a0764a" class="o"/>
  <path d="M90-84q34-46 56-78l40 26q-24 34-50 78z" fill="#a0764a" class="o"/>
  <ellipse cx="196" cy="-160" rx="46" ry="30" fill="#a0764a" class="o" transform="rotate(-24 196 -160)"/>
  <path d="M226-178l30-6-16 30z" fill="#8b6437" class="o"/>
  <path d="M170-192q-10-36 4-40 16 8 10 40zM196-198q10-32 24-26 6 12-10 30z" fill="#a0764a" class="o"/>
  <circle cx="196" cy="-168" r="5" fill="{INK}"/>
  <path d="M150-176q34-28 58-4-30 22-58 4z" fill="#6b4c28" class="o"/>
  <path d="M-130-60q-50-14-64-56 50 4 70 46z" fill="#6b4c28" class="o"/>
  <g stroke="#8b6437" stroke-width="16" stroke-linecap="round" fill="none">
    <path d="M-80 0v52M-30 4v48M50 0v52M96 0v52"/>
  </g>
</g>
<g transform="translate(268 224)">
  <path d="M-44 6q-8-30 14-34 30-6 60 0 22 4 14 34-44 10-88 0z" fill="#5b4a3c" class="o"/>
  <path d="M-44 6q-20 4-20 14 20 6 22-6zM44 6q20 4 20 14-20 6-22-6z" fill="#4a3c30" class="o"/>
  <path d="M-16-28q16-10 32 0" fill="none" stroke="#4a3c30" stroke-width="4"/>
</g>
<g fill="none" stroke="#4a3c30" stroke-width="6">
  <path d="M250 240v54h28v-16h-22"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M268 120v66"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
