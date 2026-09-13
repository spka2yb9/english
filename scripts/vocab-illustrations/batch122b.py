# -*- coding: utf-8 -*-
"""第122回の描き直し。fitted(だぶだぶ側が宙に浮いた)、secluded(家が完全に隠れた)。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')
def split():
    return f'<path d="M300 20v360" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" fill="none"/>'

# 服だけを別に描いたら宙に浮いた。人の上に直接だぶつかせる／体に沿わせる。
add('fitted', 'だぶだぶの服と、体の線に沿ったぴったりの服', f'''
{split()}
{table(370)}
<g transform="translate(150 370)">
  <path d="M-12-8l-7 35M12-8l7 35" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-66-66q66-30 132 0l-16 82H-50z" class="tealp o"/>
  <path d="M-66-66l-44 50 22 18 30-32M66-66l44 50-22 18-30-32" fill="{TONES['teal'][1]}" class="o"/>
  <circle cy="-104" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 4)" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <circle cx="-8" cy="-100" r="2.2" fill="{INK}"/><circle cx="8" cy="-100" r="2.2" fill="{INK}"/>
  <path d="M-8-86q8-8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="3"><path d="M-56-30q56 16 112 0"/></g>
</g>
<g transform="translate(450 370)">
  <path d="M-12-8l-7 35M12-8l7 35" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-27-74q27-14 54 0l-6 42q-4 16-21 16t-21-16z" class="coral o"/>
  <path d="M-27-74l-19 34 14 10 12-24M27-74l19 34-14 10-12-24" class="coral o"/>
  <circle cy="-104" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 4)" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <circle cx="-8" cy="-100" r="2.2" fill="{INK}"/><circle cx="8" cy="-100" r="2.2" fill="{INK}"/>
  <path d="M-8-86q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"><path d="M-22-40q22 8 44 0"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M390 250h50"/></g>
<g class="a" marker-end="url(#ar)"><path d="M510 250h-50"/></g>''', arrow=True, ground=False)

# 木で埋めたら家が消えた。家は手前の空き地に出し、まわりだけを木で囲う。
add('secluded', '林にぐるりと囲まれ、外から見えない場所に小さな家がある', f'''
<path d="M0 0h600v240H0z" fill="#cfe0d4"/>
<path d="M0 240h600v160H0z" fill="#c9d8c0"/>
<path d="M0 240h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
''' + ''.join(tree(30+i*72, 250, 1.15) for i in range(9)) + f'''
<g>
  <path d="M170 300h260v70H170z" fill="#dfe8d8" class="o"/>
</g>
{building(300, 350, 0.85, 'coral')}
''' + ''.join(tree(20+i*90, 396, 1.5) for i in [0, 1, 4, 5, 6]) + f'''
<g fill="{TONES['green'][2]}" opacity="0.1"><path d="M0 0h600v400H0z"/></g>
<g class="a" marker-end="url(#ar)"><path d="M110 70q110 60 170 170"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
