# -*- coding: utf-8 -*-
"""第169回の描き直し。clarification / come down to / cut back / corrosive / cosmetic。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def scissors(x, y, r=0, s=1):
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})">'
            f'<path d="M0 0l70-46M0 0l70 46" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
            f'<circle cx="84" cy="-54" r="16" fill="none" stroke="{INK}" stroke-width="7"/>'
            f'<circle cx="84" cy="54" r="16" fill="none" stroke="{INK}" stroke-width="7"/>'
            f'<circle cx="0" cy="0" r="6" class="ink"/></g>')

add('clarification', '曇ったガラスを布で拭いた帯の中だけ、向こうの家がくっきり見える',
    '説明、明確化＝clarification。', f'''
<g transform="translate(300 190)"><path d="M-230-140h460v280h-460z" fill="#fffefd" class="o"/></g>
<clipPath id="band"><path d="M130 50h150v280H130z"/></clipPath>
<g opacity="0.22">{house(300, 290, 1.1, 'coral')}{tree(460, 290, 0.9)}</g>
<g clip-path="url(#band)">{house(300, 290, 1.1, 'coral')}</g>
<g transform="translate(300 190)"><path d="M-230-140h460v280h-460z" fill="none" class="o"/></g>
{''.join(f'<path d="M{x} 70q20 22 0 44" fill="none" stroke="{MUTED}" stroke-width="4"/>' for x in (360, 400, 440))}
<g transform="translate(200 90) rotate(-14)">
  <path d="M-46-34h92v68h-92z" class="goldp o"/>
  <path d="M-46-34q46 20 92 0" fill="none" stroke="{GLDD}" stroke-width="4"/></g>
{line(200, 140, 200, 300, MUTED, True, 4)}''', arrow=True)

add('come down to', 'いくつもの道が最後に一本に合流し、たった一枚の扉の前で終わる',
    '結局〜次第である＝come down to。', f'''
{''.join(f'<path d="M{60+i*120} 50Q{160+i*70} 170 300 250" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>' for i in range(5))}
<path d="M300 250v40" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
<g transform="translate(300 380)">
  <path d="M-80-92h160v92h-160z" fill="#e8ddc9" class="o"/>
  <path d="M-58-76h116v76h-116z" class="teal o"/>
  <circle cx="40" cy="-36" r="8" class="goldp o"/></g>
{ring(300, 250, 34, True)}''')

add('cut back', 'はさみを入れて、支出の棒グラフを点線の高さまで切り下げる',
    '(費用・量を)減らす＝cut back。', f'''
{bar(120, 330, [90, 72, 52], 78, 44, 2.4, ['coralp', 'coralp', 'coral'])}
<path d="M96 200h330" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="12 10"/>
<g opacity="0.25"><path d="M120 126h78v74h-78zM242 158h78v42h-78z" class="coral"/></g>
{scissors(452, 200, 180, 0.9)}
{''.join(f'<path d="M{132+i*122} 348h58" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''')

add('corrosive', 'こぼれた液が金属板を溶かし、ふちのぎざぎざした穴が向こうまで抜ける',
    '腐食性の、むしばむ＝corrosive。', f'''
{table(346)}
<g transform="translate(300 268)">
  <path d="M-190-70h380v116h-380z" fill="{STONE}" class="o"/>
  <path d="M-190-70h380v14h-380z" fill="#d9dfe3"/>
  <path d="M-46-56l18 18-22 16 24 20-16 18 26 16 22-14 20 18 22-22-18-20 20-18-24-16 10-16z"
        fill="#fffaf1" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
  <path d="M92-8l12 12-14 12 18 10 14-16-12-12z" fill="#fffaf1" stroke="{INK}" stroke-width="3"/></g>
<g transform="translate(180 118) rotate(40)">
  <path d="M-26-64h52v92a20 20 0 0 1-20 20h-12a20 20 0 0 1-20-20z" class="greenp o"/>
  <path d="M-12-86h24v22h-24z" class="green o"/></g>
{''.join(drop(238 + i * 14, 172 + i * 20, 1.0, 'green') for i in range(3))}
{''.join(f'<path d="M{356+i*22} {206-i*12}q14-20 0-38" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''')

add('cosmetic', 'ひび割れた壁の上を薄くローラーで塗り、塗った部分だけひびが見えなくなる',
    '化粧の、うわべだけの＝cosmetic。', f'''
<g transform="translate(300 200)">
  <path d="M-230-150h460v300h-460z" fill="#e4dccb" class="o"/></g>
<g opacity="0.9">
  <path d="M150 50l34 92-52 54 44 66M370 50l-38 106 56 48-42 58" fill="none" stroke="{MUTED}" stroke-width="6"/></g>
<path d="M70 50h180v300H70z" class="tealp"/>
<g opacity="0.22"><path d="M150 50l34 92-52 54 44 66" fill="none" stroke="{MUTED}" stroke-width="6"/></g>
<path d="M70 50h180v300H70z" fill="none" stroke="{TEA}" stroke-width="4"/>
<g transform="translate(300 190)">
  <path d="M-52-30h104v60h-104z" class="teal o"/>
  <path d="M0 30v56h70" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>
{''.join(f'<path d="M{262} {160+i*30}h-14" fill="none" stroke="{TEA}" stroke-width="6"/>' for i in range(3))}''')

finish(__file__)
