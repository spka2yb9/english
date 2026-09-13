# -*- coding: utf-8 -*-
"""第127回の描き直し。cloak が紫のおばけに見えた。人の形を残してマントを羽織らせる。"""
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

add('cloak', '肩から羽織った長いマントで体を覆い隠している', f'''
{split()}
{table(380)}
{person(150, 380, 1.15, 1, 'coral', 'blue', 'stand', 'bob', 'smile')}
<g transform="translate(450 380)">
  <path d="M-14-10l-8 10M14-10l8 10" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-30-90q30-16 60 0l-9 82h-42z" class="coral o"/>
  <circle cy="-124" r="27" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bob']}" transform="translate(0 -14) scale(1.1)" fill="{HAIR}"/>
  <circle cx="-9" cy="-120" r="2.4" fill="{INK}"/><circle cx="9" cy="-120" r="2.4" fill="{INK}"/>
  <path d="M-9-108q9 8 18 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M-52-96q52-24 104 0l32 96H-84z" class="violetd o"/>
  <path d="M-84 0h168l-6 0H-84z" fill="none"/>
  <path d="M-52-96q0-24 52-24t52 24q-52 22-104 0z" class="violetd o"/>
  <path d="M-16-116q16 8 32 0" fill="none" stroke="{TONES['violet'][0]}" stroke-width="3"/>
  <circle cx="-40" cy="-104" r="9" class="gold o"/><circle cx="40" cy="-104" r="9" class="gold o"/>
  <g fill="none" stroke="{TONES['violet'][0]}" stroke-width="3"><path d="M-60-40q60 22 120 0M-74-8q74 26 148 0"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
