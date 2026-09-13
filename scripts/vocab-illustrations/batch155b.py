# -*- coding: utf-8 -*-
"""第155回の描き直し。3枚。"""
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
TEA, TEAP, TEAD = TONES['teal']

def spark(x, y, s=1, cls='gold'):
    return (f'<path d="M{x} {y-16*s}l{5*s} {11*s} {11*s} {5*s}-{11*s} {5*s}-{5*s} {11*s}'
            f'-{5*s}-{11*s}-{11*s}-{5*s} {11*s}-{5*s}z" class="{cls} o"/>')

def ring(x, y, r=64, dash=False, cls='coral'):
    d = ' stroke-dasharray="11 10"' if dash else ''
    c = MUTED if dash else TONES[cls][0]
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="4"{d}/>'

add('cartilage', '骨と骨のあいだにはさまる、やわらかい層', f'''
<g transform="translate(300 200)">
  <path d="M-56-170q0-30 30-30t26 30v76q26 10 26 34h-108q0-24 26-34z" fill="#efe9db" class="o"/>
  <path d="M-52 170q0 30 30 30t26-30v-76q26-10 26-34h-108q0 24 26 34z" fill="#efe9db" class="o"/>
  <path d="M-64-30q64-24 128 0 6 34-64 40-70-6-64-40z" class="tealp o"/>
  <path d="M-60 24q60 20 120 0" fill="none" stroke="{TEA}" stroke-width="4"/></g>
{ring(300, 0 + 195, 108)}''')

add('civility', '扉を開けて先に通し、会釈でこたえる', f'''
<g transform="translate(430 306)"><path d="M-100 0v-220h200V0z" fill="#fffefd" class="o"/>
  <path d="M-80 0v-200h160V0z" class="goldp o"/></g>
<g transform="translate(330 210) rotate(-26)"><path d="M0-96h96v192H0z" class="goldp o"/><circle cx="78" cy="10" r="7" class="ink"/></g>
{person(180, 306, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
{person(320, 306, 1.15, 1, 'coral', 'blue', 'walk', 'bob', 'smile')}
<path d="M240 250h50" fill="none" class="a" marker-end="url(#ar)"/>
{''.join(spark(x, y, 0.8) for x, y in [(140,140),(280,120)])}''', arrow=True)

add('coercion', '肩を押さえられ、いやいやペンを走らせる', f'''
{table(300)}
{doc(250, 220, 180, 200, 4)}
<g transform="translate(330 190) rotate(34)"><path d="M-8-84h16v110l-8 18-8-18z" class="coral o"/></g>
{sit(200, 380, 1.25, 1, 'teal', 'blue', 'short', 'sad', 'lap')}
{chair(214, 380, 1.15, 'gold', -1)}
{person(470, 380, 1.35, -1, 'violet', 'blue', 'reach', 'short', 'neutral')}
<path d="M392 250l-140 0" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/>
<path d="M252 250l-14-12M252 250l-14 12" fill="none" stroke="{INK}" stroke-width="0"/>
<path d="M240 200v40" class="a" stroke-width="6" marker-end="url(#ar)"/>
{drop(160, 240, 0.9)}''', arrow=True)

print(sheet(W, '/tmp/vocab-sheet2.html', 3))
