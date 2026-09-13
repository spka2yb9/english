# -*- coding: utf-8 -*-
"""第132回の描き直し。reshape・relegate・equate。"""
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


# 粘土のかたまりと壺が小さすぎて読めなかった。両方を大きくし、手を添える。
add('reshape', '粘土のかたまりをこねて壺の形に作りかえる', f'''
{split()}
{table(350)}
<g transform="translate(150 250)">
  <path d="M-80-60h160v110h-160z" fill="#b08c6c" class="o"/>
  <path d="M-80-60l20-24h160l-20 24z" fill="#c09c7c" class="o"/>
  <path d="M80-60l20-24v110l-20 24z" fill="#96765a" class="o"/>
</g>
{hand(150, 130, 1)}
<g transform="translate(450 250)">
  <path d="M-56-20q0-40 56-40t56 40q14 70-14 90-42 16-84 0-28-20-14-90z" fill="#b08c6c" class="o"/>
  <path d="M-40-26h80v-14q0-12-40-12t-40 12z" fill="#96765a" class="o"/>
  <path d="M56 0q40 0 40 24t-40 24" fill="none" stroke="#b08c6c" stroke-width="16"/>
  <g fill="none" stroke="#96765a" stroke-width="4"><path d="M-52 20q52 16 104 0"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

# 上段の枠に入れたはずの顔が枠外に出ていた。座標を絶対値で置き直す。
add('relegate', '上の組の枠から外され、下の組へ落とされる', f'''
{table(380)}
<g transform="translate(300 130)">
  <path d="M-230-70h460v130h-460z" class="goldp o"/>
</g>
{head(200, 130, 24, 'gold', 'short')}
{head(300, 130, 24, 'coral', 'bob')}
{head(400, 130, 24, 'teal', 'cap')}
<g transform="translate(300 320)">
  <path d="M-230-46h460v100h-460z" fill="#dde3e8" class="o"/>
</g>
{head(220, 320, 24, 'blue', 'short')}
{head(380, 320, 24, 'violet', 'bun')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M540 170v100"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 225h520"/></g>''', ground=False)

# てんびんの傾きだけでは「同じとみなす」が出ない。等号を大きく描いて重ねる。
add('equate', '重さの違う二つを、同じものとして扱ってしまう', f'''
{table(380)}
<g transform="translate(300 170)">
  <path d="M-10 0h20v170h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-70 170h140v20h-140z" fill="#8f9aa6" class="o"/>
  <path d="M-200-8h400v16h-400z" fill="#b8bfc8" class="o"/>
  <circle r="16" fill="#8f9aa6" class="o"/>
  <path d="M-190 8v40M190 8v40" stroke="{INK}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(110 218)">
  <path d="M-56 0q0 30 56 30t56-30z" class="tealp o"/>
  <ellipse ry="10" rx="56" class="tealp o"/>
  <circle cy="-24" r="30" class="teal o"/>
</g>
<g transform="translate(490 218)">
  <path d="M-56 0q0 30 56 30t56-30z" class="coralp o"/>
  <ellipse ry="10" rx="56" class="coralp o"/>
  <circle cy="-10" r="12" class="coral o"/>
</g>
<g fill="{TONES['coral'][0]}">
  <rect x="256" y="296" width="88" height="18" rx="9"/>
  <rect x="256" y="330" width="88" height="18" rx="9"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="322" r="70"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
