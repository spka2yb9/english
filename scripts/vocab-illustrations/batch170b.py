# -*- coding: utf-8 -*-
"""第170回の描き直し。digestion / digestive / fend for / face up to。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('digestion', '飲みこんだりんごが胃の中へ進み、そこで細かい粒に分かれていく',
    '消化＝digestion。', f'''
<g transform="translate(300 200)">
  <path d="M-150-170h300v340h-300z" fill="#eef4f7" class="o"/></g>
<g transform="translate(300 60)"><circle r="30" class="green o"/>
  <path d="M0-30v-18" stroke="{GRND}" stroke-width="6" fill="none"/></g>
<path d="M300 96v64" fill="none" stroke="{CRLD}" stroke-width="26" stroke-linecap="round"/>
<g transform="translate(300 250)">
  <path d="M-30-90q-62 26-56 92 8 62 70 64 58 2 66-62 8-56-44-94z" class="coralp o"/>
  <path d="M50 60q12 42-22 58-38 18-62-10" fill="none" stroke="{CRLD}" stroke-width="22" stroke-linecap="round"/>
  {''.join(f'<circle cx="{x}" cy="{y}" r="{r}" class="green o"/>' for x, y, r in [(-20, -20, 13), (18, 4, 10), (-6, 30, 9), (28, -34, 8), (-34, 22, 7)])}</g>
{line(300, 128, 300, 152, MUTED, True, 0, False)}''')

add('digestive', '口から胃、そして腸へとつながる消化の通り道を取り出した図',
    '消化の＝digestive。', f'''
<g transform="translate(300 200)">
  <path d="M-160-170h320v340h-320z" fill="#eef4f7" class="o"/></g>
<g transform="translate(300 70)"><ellipse rx="42" ry="24" class="coralp o"/>
  <path d="M-42 0q42 22 84 0" fill="none" stroke="{CRLD}" stroke-width="4"/></g>
<path d="M300 96v52" fill="none" stroke="{CRLD}" stroke-width="24" stroke-linecap="round"/>
<g transform="translate(288 200)">
  <path d="M-22-56q-50 20-44 70 6 48 54 50 46 2 52-48 6-44-34-72z" class="coralp o"/></g>
<g transform="translate(300 306)">
  <path d="M-90-30h180v70h-180z" fill="none" stroke="{CRLD}" stroke-width="20" stroke-linejoin="round"/>
  <path d="M-52-6h104v32h-104z" fill="none" stroke="{CRL}" stroke-width="15" stroke-linejoin="round"/></g>
{ring(296, 206, 150, True)}''')

add('fend for', 'だれの手も借りず、自分で火をおこして自分の鍋を煮る',
    '(fend for oneself で)自分でなんとかする＝fend for。', f'''
{flame(410, 330, 1.0)}
<g transform="translate(410 214)">
  <path d="M-110 0h220" stroke="{MUTED}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M-104 0l-20 120M104 0l20 120" stroke="{MUTED}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M-64 4h128l-14 70h-100z" fill="{STONE}" class="o"/>
  <path d="M-74 4h148" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
{''.join(f'<path d="M{368+i*42} 196q14-22 0-40" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}
{person(150, 340, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'flat')}
<g opacity="0.24">{person(60, 340, 0.95, 1, 'coral', 'green', 'give', 'bob', 'flat')}</g>
{cross(60, 140, 0.6)}''')

add('face up to', '目をそらさず、壁に貼られた右下がりの悪い数字の紙に正面から向き合う',
    '(いやな事実を)直視する、受け入れる＝face up to。', f'''
<g transform="translate(410 180)">
  <path d="M-120-120h240v240h-240z" class="paper"/>
  <path d="M-86 86h172M-86 86v-150" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-70-40L-10 10 40 0 84 64" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M84 64H36M84 64V24" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/></g>
{person(150, 340, 1.3, 1, 'teal', 'blue', 'stand', 'short', 'flat')}
{line(212, 190, 272, 190, MUTED, True, 4)}''', arrow=True)

finish(__file__)
