# -*- coding: utf-8 -*-
"""第169回の描き直し2。come down to / cut back。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('come down to', 'いくつもの道が一本に合流し、最後はたった一枚の扉の前で終わる',
    '結局〜次第である＝come down to。', f'''
{''.join(f'<path d="M{40+i*130} 40Q{150+i*74} 150 300 210" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>' for i in range(5))}
<path d="M300 210v30" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<g transform="translate(300 380)">
  <path d="M-96-146h192v146h-192z" fill="#e8ddc9" class="o"/>
  <path d="M-70-128h140v128h-140z" class="teal o"/>
  <path d="M-52-110h104v46h-104zM-52-48h104v48h-104z" fill="none" stroke="{TEAD}" stroke-width="4"/>
  <circle cx="52" cy="-64" r="9" class="goldp o"/></g>
{ring(300, 226, 34, True)}''')

add('cut back', 'はさみを入れて、高すぎた支出の棒を点線の高さまで切り落とす',
    '(費用・量を)減らす＝cut back。', f'''
<path d="M80 344h420" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<path d="M70 190h380" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="12 10"/>
<g opacity="0.28"><path d="M140 70h90v120h-90zM280 110h90v80h-90z" class="coral"/></g>
<path d="M140 70h90v120h-90zM280 110h90v80h-90z" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"/>
<path d="M140 190h90v154h-90z" class="coral o"/>
<path d="M280 190h90v154h-90z" class="coral o"/>
<g transform="translate(500 190) rotate(180)">
  <path d="M0 0l70-46M0 0l70 46" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="84" cy="-54" r="16" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="84" cy="54" r="16" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle r="6" class="ink"/></g>''')

finish(__file__)
