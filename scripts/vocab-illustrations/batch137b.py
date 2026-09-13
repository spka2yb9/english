# -*- coding: utf-8 -*-
"""第137回の描き直し。calf と cello。"""
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


# 脚を筒で描いたら肉の塊になった。太もも・ひざ・ふくらはぎ・足首・足を順に置く。
add('calf', 'ふくらはぎの筋肉と、そばにいる子牛', f'''
{table(380)}
<g transform="translate(190 240)">
  <path d="M-26-120h52v70h-52z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse cy="-48" rx="30" ry="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-22-30h44q34 34 22 82t-44 46-44-46 22-82z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-16 98h32v34h-32z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-16 132h72q10 0 10 10t-10 10h-72z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-36 40q36-36 72 0" fill="none" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30 66q30-24 60 0" fill="none" stroke="{SKINL}" stroke-width="3"/>
</g>
<circle cx="190" cy="270" r="64" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
<g transform="translate(440 310) scale(0.68)">
  <ellipse cy="-50" rx="100" ry="56" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><ellipse cx="-30" cy="-56" rx="26" ry="18"/><ellipse cx="40" cy="-34" rx="20" ry="14"/></g>
  <circle cx="86" cy="-96" r="34" fill="#fffdf6" class="o"/>
  <path d="M60-118q-16-20-4-26 12-2 14 20zM106-120q14-20 24-12 4 12-14 20z" fill="#e8c9a0" class="o"/>
  <circle cx="96" cy="-100" r="4" fill="{INK}"/>
  <ellipse cx="112" cy="-84" rx="18" ry="13" fill="#e8c9a0" class="o"/>
  <g stroke="#c9a464" stroke-width="12" stroke-linecap="round" fill="none"><path d="M-40 0v34M30 0v34"/></g>
</g>''', ground=False)

# 円を二つ並べても弦楽器にならない。くびれた輪郭を縦にして、糸巻きと弦を通す。
add('cello', '床に立てて弓で弾く大きな弦楽器', f'''
{table(380)}
<g transform="translate(280 250)">
  <path d="M-70-40q0-70 70-70t70 70q6 30-20 44 26 14 20 44 0 70-70 70t-70-70q-6-30 20-44-26-14-20-44z" fill="#a8552c" class="o"/>
  <path d="M-40 10q-12 14 0 28M-40 38q12 14 24 0" fill="none" stroke="#7c3a1c" stroke-width="4"/>
  <path d="M40 10q12 14 0 28M40 38q-12 14-24 0" fill="none" stroke="#7c3a1c" stroke-width="4"/>
  <path d="M-22-110h44v-90h-44z" fill="#5b4a3c" class="o"/>
  <path d="M-26-200h52v-34h-52z" fill="#a8552c" class="o"/>
  <g fill="#5b4a3c"><circle cx="-18" cy="-216" r="6"/><circle cx="18" cy="-216" r="6"/></g>
  <g fill="none" stroke="#e8dcc0" stroke-width="2.5">
''' + ''.join(f'<path d="M{-12+i*8} 84v-286"/>' for i in range(4)) + f'''
  </g>
  <path d="M-30 74h60v10h-60z" fill="#5b4a3c" class="o"/>
  <path d="M-6 84h12v52h-12z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(410 220) rotate(-72)">
  <path d="M-110-5h220v10h-220z" fill="#c9a464" class="o"/>
  <path d="M-110-2h220v4h-220z" fill="#e8dcc0"/>
</g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
