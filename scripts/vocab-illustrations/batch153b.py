# -*- coding: utf-8 -*-
"""第153回の描き直し。2枚。"""
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

CRL = TONES['coral'][0]
TEA = TONES['teal'][0]
BRN = '#8c6b42'

def ring(x, y, r=64, dash=False, cls='coral'):
    d = ' stroke-dasharray="11 10"' if dash else ''
    c = MUTED if dash else TONES[cls][0]
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="4"{d}/>'

add('antler', '横向きのシカの頭に生えた、枝分かれした大きな角', f'''
<g transform="translate(300 330)">
  <path d="M-60 40q-30-60 10-96 40-36 90-16l70 44q20 14 4 30l-56 22q-40 22-118 16z" fill="#b58a58" class="o"/>
  <circle cx="34" cy="-22" r="7" class="ink"/>
  <path d="M-40-30q-40-16-46-46 36 4 50 34z" fill="#b58a58" class="o"/>
</g>
<g fill="none" stroke="{BRN}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round">
  <path d="M320 288q10-70-30-116"/>
  <path d="M312 226q-46-8-62-46"/>
  <path d="M300 186q-40-16-46-52"/>
  <path d="M290 172q26-34 66-30"/>
  <path d="M382 292q26-64 76-96"/>
  <path d="M400 240q42 4 66-28"/>
  <path d="M420 208q38-6 52-40"/>
  <path d="M440 190q-16-38 8-64"/>
</g>
{ring(400, 200, 120)}''')

add('at first glance', 'ちらっと見ただけの姿と、よく見たときの姿の対比', f'''
{split()}
<g transform="translate(150 210)"><path d="M-70 60l70-120 70 120z" class="teal o"/></g>
<g transform="translate(150 96)"><path d="M-34 0q34-24 68 0-34 24-68 0z" fill="#fffefd" class="o"/><circle r="10" class="ink"/>
  <path d="M-56-12h-24M-58 8h-30M60-12h24M62 8h30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/></g>
<g transform="translate(450 210)"><path d="M-70 60l70-120 70 120z" class="teal o"/>
  <path d="M-70 60h140" fill="none" stroke="{CRL}" stroke-width="6"/>
  <circle cx="0" cy="24" r="16" class="coral o"/></g>
<g transform="translate(470 240) rotate(24)"><circle r="76" fill="#ffffff" opacity="0.16" stroke="{INK}" stroke-width="6"/>
  <path d="M0 76v44" stroke="{INK}" stroke-width="16" stroke-linecap="round"/></g>''')

print(sheet(W, '/tmp/vocab-sheet2.html', 2))
