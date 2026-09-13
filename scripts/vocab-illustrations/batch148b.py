# -*- coding: utf-8 -*-
"""第148回の描き直し。人のポーズが読めなかった6枚。"""
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

def arms_folded(x, y, s=1):
    """胸の前で腕を組む。resentful と同じ描き方。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-32 0l64-14M32-2l-64 16" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/></g>')

# 1 深く後悔している：割ってしまったものを思い返してうなだれる
add('remorseful', '割ってしまった皿を思い返し、うなだれてあやまる', f'''
{person(190, 306, 1.25, 1, 'coral', 'blue', 'stand', 'short', 'sad')}
<path d="M162 200q28 22 56 0" fill="none" stroke="{MUTED}" stroke-width="4"/>
<circle cx="270" cy="180" r="9" fill="#fffefd" class="o"/>
<circle cx="294" cy="150" r="13" fill="#fffefd" class="o"/>
<g transform="translate(410 116)"><ellipse rx="112" ry="72" fill="#fffefd" class="o"/>
  <path d="M-60 20q10-46 56-46t56 46z" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <path d="M-60 20l38-8 20 12 24-14 22 10 16-8" fill="none" stroke="{CRL}" stroke-width="5"/>
  <path d="M-24 40l-16 22M20 40l14 24" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
{drop(150, 206, 1.0)}
{person(520, 306, 1.1, -1, 'teal', 'blue', 'stand', 'bob', 'neutral')}''')

# 2 容赦がない：手を合わせて頼まれても、腕を組んで受けつけない
add('remorseless', 'すがる相手に、腕を組んだまま取り合わない', f'''
{person(140, 306, 1.15, 1, 'teal', 'blue', 'reach', 'bob', 'sad')}
<g transform="translate(230 200)"><rect x="-56" y="-34" width="112" height="60" rx="16" class="paper"/>
  <path d="M-40 22l-20 26 4-26z" class="paper"/>
  <path d="M-22-8h44M-30 8h60" fill="none" stroke="{MUTED}" stroke-width="6"/></g>
<path d="M320 100v240" fill="none" stroke="{MUTED}" stroke-width="8"/>
<path d="M292 200h-24" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<g transform="translate(450 306)">
  <path d="M-14-8l-8 34M14-8l8 34" fill="none" stroke="{BLUD}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-28-84q28-14 56 0l-9 76h-38z" fill="{VIO}" class="o"/>
  <circle cx="0" cy="-116" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 -8)" fill="{HAIR}"/>
  <path d="M-16-124l14 6M16-124l-14 6" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-10-100h20" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
{arms_folded(450, 246, 1.05)}''')

# 3 罰が重すぎる：小さな過ちに、つり合わない重い罰
add('punitive', '小さな過ちに対して、つり合わないほど重い罰', f'''
<g transform="translate(300 90)"><path d="M-210 0h420" fill="none" stroke="{INK}" stroke-width="7" transform="rotate(-13)"/>
  <path d="M0 0v-56" fill="none" stroke="{INK}" stroke-width="7"/><circle cy="-62" r="9" class="ink"/></g>
<path d="M96 42v54" fill="none" stroke="{INK}" stroke-width="4"/>
{box(96, 130, 60, 42, 14, 'gold')}
<path d="M504 138v46" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(504 262)"><path d="M-84 66l24-92h120l24 92z" fill="#5b6b78" class="o"/>
  <path d="M-30-26v-16a30 30 0 0 1 60 0v16" fill="none" stroke="{INK}" stroke-width="8"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M400 300h-30M420 340h-30"/></g>''')

# 4 くり返しの多い：同じ動きを何度も
add('repetitive', '同じ腕の動きを、何度もくり返す', f'''
{table(340)}
<g opacity="0.28">{person(280, 306, 1.25, 1, 'teal', 'blue', 'up', 'short', 'neutral')}</g>
<g opacity="0.5">{person(280, 306, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'neutral')}</g>
{person(280, 306, 1.25, 1, 'teal', 'blue', 'hold', 'short', 'neutral')}
<g transform="translate(392 176) rotate(30)"><path d="M-8 0h16v80h-16z" class="goldd o"/>
  <path d="M-30-30h60v26h-60z" class="ink"/></g>
<g transform="translate(430 260)"><path d="M-58 0a58 58 0 1 1 20 44" fill="none" class="a" stroke-width="6" marker-end="url(#ar)"/></g>
<path d="M150 190q16-18 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>''', arrow=True)

# 5 落ち着かない：いすから何度も立ったり座ったり
add('restless', 'いすに座ってもすぐ立ち上がり、落ち着かない', f'''
{chair(400, 340, 1.25, 'gold', -1)}
<g opacity="0.3">{sit(400, 340, 1.25, 1, 'coral', 'blue', 'short', 'neutral', 'lap')}</g>
{person(230, 340, 1.25, 1, 'coral', 'blue', 'up', 'short', 'neutral', 'walk')}
<g transform="translate(320 250)"><path d="M-60 40a70 70 0 0 1 120-40" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/>
  <path d="M60 60a70 70 0 0 1-120 30" fill="none" class="a" stroke-width="5" marker-end="url(#ar)"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M120 180q16-20 0-40M540 190q-16-20 0-40"/></g>''', arrow=True)

# 6 和解させる：切れていたつながりが結び直される
add('reconcile', '切れていたつながりが、握手で結び直される', f'''
{person(130, 306, 1.2, 1, 'coral', 'blue', 'give', 'short', 'smile')}
{person(470, 306, 1.2, -1, 'teal', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(300 216)">{hand(-20, 0, 1)}{hand(20, 0, -1)}</g>
<g opacity="0.35"><path d="M180 120l40 40-40 20 40 30M420 120l-40 40 40 20-40 30" fill="none" stroke="{CRL}" stroke-width="6"/></g>
<path d="M190 96q110-56 220 0" fill="none" stroke="{GRN}" stroke-width="7"/>
{''.join(spark(x, y, 0.9) for x, y in [(240,150),(360,148)])}''')

print(sheet(W, '/tmp/vocab-sheet2.html', 3))
