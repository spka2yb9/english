# -*- coding: utf-8 -*-
"""第170回の描き直し2。digestion / digestive は体の輪郭の中に描く。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def body(x, y, s=1):
    """胴体と頭の輪郭だけ。中に器官を描くための下地。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cy="-192" r="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-84-140q84-30 168 0 24 140 0 280h-168q-24-140 0-280z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'</g>')

add('digestion', '飲みこんだりんごが体の中を下りながら、少しずつ細かい粒に分かれていく',
    '消化＝digestion。', f'''
{body(300, 190, 0.78)}
<g transform="translate(300 90)"><circle r="24" class="green o"/><path d="M0-24v-14" stroke="{GRND}" stroke-width="5" fill="none"/></g>
{''.join(f'<circle cx="{300+dx}" cy="{y}" r="{r}" class="green o"/>' for dx, y, r in [(-16, 170, 15), (18, 186, 13), (-4, 214, 11), (24, 234, 9), (-22, 246, 8), (6, 268, 7), (-14, 288, 6), (20, 296, 5)])}
<path d="M300 122v26" fill="none" stroke="{CRLD}" stroke-width="18" stroke-linecap="round"/>
{line(470, 110, 470, 300, MUTED, True, 5)}
{''.join(f'<circle cx="{470}" cy="{y}" r="{r}" class="greenp o"/>' for y, r in [(140, 20), (200, 14), (260, 9)])}''', arrow=True)

add('digestive', '口から胃、腸へと続く消化の通り道が、体の中で一本につながっている',
    '消化の＝digestive。', f'''
{body(300, 170, 0.62)}
<g transform="translate(300 92)"><ellipse rx="22" ry="11" class="coralp o"/></g>
<path d="M300 102v34" fill="none" stroke="{CRL}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(292 178)">
  <path d="M-14-38q-36 14-30 48 6 34 38 36 32 2 36-34 4-30-24-50z" class="coralp o"/></g>
<path d="M300 254q-32 0-32 20t64 0 0-20" fill="none" stroke="{CRL}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M300 294v28" fill="none" stroke="{CRL}" stroke-width="12" stroke-linecap="round"/>
{ring(300, 206, 138, True)}''')

finish(__file__)
