# -*- coding: utf-8 -*-
"""第150回の描き直し。4枚。"""
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
GRN, GRND = TONES['green'][0], TONES['green'][2]
TEA = TONES['teal'][0]
VIO = TONES['violet'][0]

def ring(x, y, r=64, dash=False, cls='coral'):
    d = ' stroke-dasharray="11 10"' if dash else ''
    c = MUTED if dash else TONES[cls][0]
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="4"{d}/>'

add('synonym', 'ちがう二つの語が、同じりんごを指す', f'''
{word(150, 110, 4, 34, TEA)}
{word(450, 110, 6, 26, VIO)}
<path d="M270 104h60M270 130h60" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
<path d="M150 160l120 90M450 160l-120 90" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(300 300)">
  <path d="M0-56q-46-40-76 0-26 36 6 82 24 34 70 34t70-34q32-46 6-82-30-40-76 0z" class="coral o"/>
  <path d="M0-56v-34" fill="none" stroke="{GRND}" stroke-width="7"/>
  <path d="M4-80q34-10 40-42-34 6-42 34z" class="greenp o"/>
  <path d="M-40-14q-10 34 14 56" fill="none" stroke="#fffefd" stroke-width="7" opacity="0.6"/></g>''')

add('trumpet', '朝顔のように開いた口をもつ金管楽器', f'''
<g transform="translate(290 220) rotate(-10)">
  <path d="M-230-12h250v24h-250z" class="gold o"/>
  <path d="M-230-12q-26 0-26 12t26 12z" class="goldd o"/>
  <path d="M-260-8h30v16h-30z" class="goldd o"/>
  <path d="M20-56q80 22 80 56t-80 56z" class="goldp o"/>
  <path d="M20-56v112" fill="none" stroke="{INK}" stroke-width="3"/>
  {''.join(f'<g><rect x="{-140+i*50}" y="-52" width="26" height="42" rx="7" class="goldd o"/>'
           f'<rect x="{-146+i*50}" y="-64" width="38" height="16" rx="7" class="gold o"/></g>' for i in range(3))}
  <path d="M-40 12q0 46 40 46t40-46" fill="none" stroke="{GLDD}" stroke-width="10"/>
</g>
{''.join(f'<path d="M{440+i*26} {130-i*22}q18 18 0 36" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}''')

add('stepfather', '母の再婚で、あとから父になった人', f'''
{person(150, 306, 1.15, 1, 'violet', 'blue', 'give', 'bob', 'smile')}
{person(450, 306, 1.2, -1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(300, 306, 0.72, 1, 'coral', 'green', 'up', 'bob', 'smile')}
<path d="M210 170h150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M300 190v-30" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M170 130q60-40 120 0" fill="none" stroke="{GRN}" stroke-width="5"/>
{ring(450, 210, 108)}''')

add('stepmother', '父の再婚で、あとから母になった人', f'''
{person(150, 306, 1.2, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(450, 306, 1.15, -1, 'violet', 'blue', 'give', 'bob', 'smile')}
{person(300, 306, 0.72, 1, 'coral', 'green', 'up', 'bob', 'smile')}
<path d="M210 170h150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M300 190v-30" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M170 130q60-40 120 0" fill="none" stroke="{GRN}" stroke-width="5"/>
{ring(450, 210, 108)}''')

print(sheet(W, '/tmp/vocab-sheet2.html', 2))
