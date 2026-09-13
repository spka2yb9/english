# -*- coding: utf-8 -*-
"""第181回。第114回で保留した rape / suicide の2語。

第114回の方針（加害の場面を描かず、物・跡・制度の側から示す）を引き継ぐ。
rape は「本人の境界線と、それを越えさせない法」、suicide は「予防の相談窓口」で示す。
どちらも被害・自傷の場面そのものは描かない。
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('rape', '一人の周りに引かれた境界の線を、顔のない影の手が越えようとして、法の記号に止められている',
    '強姦、性暴力＝rape。同意のない性的行為を指し、法で禁じられた重大な犯罪です。', f'''
<g transform="translate(250 210)">
  <circle r="120" fill="none" stroke="{TEA}" stroke-width="8"/>
  <circle r="120" class="tealp" opacity="0.5"/></g>
{person(250, 300, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'flat')}
<g opacity="0.42">
  <path d="M20 210h70" fill="none" stroke="#6b7680" stroke-width="26" stroke-linecap="round"/>
  <path d="M78 186q34-4 40 24-8 26-40 22z" fill="#6b7680"/></g>
{ban(140, 210, 52)}
<g transform="translate(470 250)">
  <path d="M-70-90h140v180h-140z" fill="#fffefd" class="o"/>
  <path d="M-76-90h14v180h-14z" class="violetd o"/>
  {''.join(f'<rect x="-44" y="{-56+i*34}" width="{100-(i%2)*30}" height="10" rx="5" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="14" cy="56" r="24" class="coralp o"/>
  <circle cx="14" cy="56" r="14" fill="none" stroke="{CRL}" stroke-width="3.5"/></g>
<path d="M400 210h-96" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('suicide', '暗い側でうつむく人に、相談窓口の明かりと受話器がつながって手がさしのべられる',
    '自殺＝suicide。suicide prevention（自殺予防）や helpline（相談窓口）の形でよく使われます。', f'''
<g transform="translate(150 200)"><path d="M-150-180h300v380h-300z" fill="#3b4557"/></g>
<g transform="translate(160 330)">
  <path d="M-60 0v-70q60-26 120 0V0z" fill="#4e6070" class="o"/>
  <path d="M-60-70q-18 44 40 52" fill="none" stroke="#8a93a5" stroke-width="18" stroke-linecap="round"/>
  <circle cx="8" cy="-112" r="28" fill="#8a93a5"/>
  <path d="M-22-120q4-32 30-32 24 0 30 30-16-14-30-6-14-8-30 8z" fill="#2f3a4d"/>
  <path d="M-4-108h20" fill="none" stroke="#3b4557" stroke-width="3"/></g>
<g transform="translate(430 200)">
  <circle r="96" class="goldp" opacity="0.55"/>
  <circle r="96" fill="none" stroke="{GLD}" stroke-width="4" stroke-dasharray="12 10"/>
  <path d="M-70-10a70 70 0 0 1 140 0" fill="none" stroke="{TEA}" stroke-width="20" stroke-linecap="round"/>
  <path d="M-70-10v34a20 20 0 0 0 40 0v-34zM70-10v34a20 20 0 0 1-40 0v-34z" class="teal o"/>
  <path d="M0 36q-26-20-26-38 0-14 14-14 8 0 12 10 4-10 12-10 14 0 14 14 0 18-26 38z" class="coral o"/></g>
<path d="M234 250q70 40 128 10" fill="none" stroke="{GLD}" stroke-width="6" stroke-linecap="round" stroke-dasharray="14 11"/>
{hand(330, 300, -1)}
{''.join(spark(330 + i * 60, 100 + (i % 2) * 30, 0.7, 'gold') for i in range(2))}''')

finish(__file__)
