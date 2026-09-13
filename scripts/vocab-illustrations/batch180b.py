# -*- coding: utf-8 -*-
"""第180回の描き直し。wig / wobble / zoom in。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('wig', '髪の形に作られたかぶり物が、頭の形をした台にかぶせてある',
    'かつら＝wig。', f'''
{table(352)}
<g transform="translate(300 300)">
  <ellipse rx="86" ry="18" fill="#e8ddc9" class="o"/>
  <path d="M-30 0v-40h60v40z" fill="#e8ddc9" class="o"/></g>
<g transform="translate(300 200)">
  <circle cy="0" r="70" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-90 50q-20-140 90-140t90 140q-40-46-90-38-52-8-90 38z" fill="{HAIR}"/>
  <path d="M-90 50q-14 36 0 58 20-16 22-44M90 50q14 36 0 58-20-16-22-44" fill="{HAIR}"/></g>
{''.join(f'<path d="M{460+i*22} {180-i*14}q12-14 0-26" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(2))}''')

add('wobble', '積み上げた箱が左右にぐらつき、いまにも倒れそうになる',
    'ぐらぐらする、ぐらつき＝wobble。', f'''
{table(352)}
<g transform="translate(300 300) rotate(10)">
  {''.join(f'<rect x="-52" y="{-52-i*54}" width="104" height="50" rx="6" class="teal o"/>' for i in range(4))}</g>
<g opacity="0.26" transform="translate(300 300) rotate(-10)">
  {''.join(f'<rect x="-52" y="{-52-i*54}" width="104" height="50" rx="6" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>' for i in range(4))}</g>
<g transform="translate(300 60)"><path d="M-70 0q70-30 140 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/></g>''', arrow=True)

add('zoom in', '小さく写っていた窓のあたりだけが、画面いっぱいに引き寄せられる',
    '拡大する、寄る＝zoom in。', f'''
<g transform="translate(150 200)">
  <path d="M-110-90h220v180h-220z" fill="#fffefd" class="o"/>
  {house(0, 50, 0.4, 'coral')}
  <path d="M-40 0h44v34h-44z" fill="none" stroke="{CRL}" stroke-width="4"/></g>
<g transform="translate(450 200)">
  <path d="M-110-90h220v180h-220z" fill="#fffefd" class="o"/>
  <path d="M-110-90h220v180h-220z" fill="{CRLP}"/>
  <path d="M-60-40h120v100h-120z" fill="#fffefd" class="o"/>
  <path d="M0-40v100M-60 10h120" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-110-90h220v180h-220z" fill="none" class="o"/></g>
<path d="M110 200L340 110M194 234L340 290" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>
{arc(270, 100, 330, 100, 36, MUTED, True, 5)}''', arrow=True)

finish(__file__)
