# -*- coding: utf-8 -*-
"""第149回の描き直し。3枚。"""
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
MUT = MUTED

def spark(x, y, s=1, cls='gold'):
    return (f'<path d="M{x} {y-16*s}l{5*s} {11*s} {11*s} {5*s}-{11*s} {5*s}-{5*s} {11*s}'
            f'-{5*s}-{11*s}-{11*s}-{5*s} {11*s}-{5*s}z" class="{cls} o"/>')

add('semifinal', '四人が二組に分かれて戦い、勝った二人が決勝へ進む', f'''
{''.join(head(60, 80 + i*80, 26, c, h) for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun')]))}
<g fill="none" stroke="{MUT}" stroke-width="5">
  <path d="M96 80h70v80h-70M96 240h70v80h-70"/>
  <path d="M166 120h60M166 280h60"/>
</g>
<g fill="none" stroke="{CRL}" stroke-width="6">
  <path d="M226 120h60v160h-60"/><path d="M286 200h70"/></g>
{head(390, 200, 30, 'teal', 'short')}
<g transform="translate(510 200)"><path d="M-46 60l12-76h68l12 76z" class="gold o"/>
  <path d="M-34-16q-36 0-36-36h36M34-16q36 0 36-36h-36" fill="none" stroke="{GLDD}" stroke-width="7"/>
  <path d="M-56 60h112v16h-112z" class="goldd o"/></g>
<path d="M226 120h-1" fill="none"/>
<g fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="11 10">
  <rect x="176" y="56" width="120" height="288" rx="16"/></g>''')

add('spontaneous', 'だれの合図もないのに、ひとりが始めた拍手が自然に広がる', f'''
{person(150, 306, 1.2, 1, 'coral', 'blue', 'up', 'short', 'smile')}
<g transform="translate(196 216)">{hand(-14, 0, 1)}{hand(14, 0, -1)}</g>
{person(360, 306, 1.05, 1, 'teal', 'green', 'up', 'bob', 'smile')}
{person(500, 306, 1.05, 1, 'violet', 'blue', 'up', 'short', 'smile')}
<g fill="none" class="a" stroke-width="4">
  <path d="M240 150q50-40 96 0" marker-end="url(#ar)"/>
  <path d="M256 130q120-70 210 0" marker-end="url(#ar)"/></g>
{''.join(spark(x, y, 0.9) for x, y in [(300,96),(430,84)])}
<g transform="translate(96 100)"><rect x="-56" y="-40" width="112" height="80" rx="8" fill="none" stroke="{MUT}" stroke-width="4" stroke-dasharray="11 9"/></g>''', arrow=True)

add('scornful', '相手を見おろして、鼻で笑い、手で払いのける', f'''
{box(430, 300, 90, 60, 20, 'gold')}
<g transform="translate(190 306)">
  <path d="M-14-8l-8 34M14-8l8 34" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-28-84q28-14 56 0l-9 76h-38z" fill="{TONES['violet'][0]}" class="o"/>
  <path d="M-24-76q-18 26-12 52" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <path d="M26-74q40 12 56 44" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-118" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 -10) scale(1.1)" fill="{HAIR}"/>
  <path d="M-18-128l16 8M18-128l-16 8" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="-10" cy="-114" r="3" class="ink"/><circle cx="10" cy="-114" r="3" class="ink"/>
  <path d="M-12-96q10 10 22-4" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M0-110l12 12-12 4z" fill="{SKINL}" opacity="0.55"/>
</g>
{hand(290, 254, 1)}
<g fill="none" stroke="{MUT}" stroke-width="5" stroke-linecap="round">
  <path d="M344 226q26-16 44 6M352 186q26-16 44 6"/></g>
<path d="M226 176l150 78" fill="none" stroke="{MUT}" stroke-width="4" stroke-dasharray="9 8"/>''')

print(sheet(W, '/tmp/vocab-sheet2.html', 3))
