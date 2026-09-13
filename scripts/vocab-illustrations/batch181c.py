# -*- coding: utf-8 -*-
"""第181回の描き直し2。左端の見切れを直し、suicide の電話を受話器の形にする。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

HANDSET = ('M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 '
           '1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 '
           '0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z')

def receiver(x, y, s=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s}) translate(-12 -12)">'
            f'<path d="{HANDSET}" fill="{TONES[cls][0]}" stroke="{INK}" stroke-width="0.5" '
            f'stroke-linejoin="round"/></g>')

add('rape', '一人を囲む境界の線を、顔のない影の手が越えようとして、法の記号に止められている',
    '強姦、性暴力＝rape。同意のない性的行為を指し、法で禁じられた重大な犯罪です。', f'''
<g transform="translate(290 200)">
  <circle r="114" class="tealp" opacity="0.6"/>
  <circle r="114" fill="none" stroke="{TEA}" stroke-width="9"/></g>
{person(290, 288, 1.05, 1, 'teal', 'blue', 'stand', 'short', 'flat')}
<g opacity="0.38">
  <path d="M46 200h50" fill="none" stroke="#6b7680" stroke-width="30" stroke-linecap="round"/>
  <path d="M84 172q40-6 46 28-10 30-46 26z" fill="#6b7680"/></g>
{ban(166, 200, 50)}
<g transform="translate(500 252)">
  <path d="M-58-76h116v152h-116z" fill="#fffefd" class="o"/>
  <path d="M-64-76h13v152h-13z" class="violetd o"/>
  {''.join(f'<rect x="-34" y="{-48+i*28}" width="{82-(i%2)*24}" height="9" rx="4.5" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="10" cy="46" r="21" class="coralp o"/>
  <circle cx="10" cy="46" r="12" fill="none" stroke="{CRL}" stroke-width="3.5"/></g>
<path d="M436 200h-32" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('suicide', '暗がりでうつむく人に、相談窓口の受話器の明かりがつながって手がさしのべられる',
    '自殺＝suicide。suicide prevention（自殺予防）や helpline（相談窓口）の形でよく使われます。', f'''
<path d="M0 0h250v400H0z" fill="#3b4557"/>
<path d="M250 0h44v400h-44z" fill="#4a5570" opacity="0.5"/>
<g transform="translate(132 338)">
  <path d="M-64 0v-74q64-28 128 0V0z" fill="#4e6070" class="o"/>
  <path d="M-64-74q-20 48 42 56" fill="none" stroke="#8a93a5" stroke-width="19" stroke-linecap="round"/>
  <circle cx="10" cy="-118" r="30" fill="#8a93a5"/>
  <path d="M-22-126q4-34 32-34 26 0 32 32-17-15-32-6-15-9-32 8z" fill="#2f3a4d"/>
  <path d="M-2-112h22" fill="none" stroke="#3b4557" stroke-width="3.5"/></g>
<g transform="translate(442 206)">
  <circle r="130" class="goldp" opacity="0.65"/>
  <circle r="130" fill="none" stroke="{GLD}" stroke-width="4" stroke-dasharray="13 11"/></g>
{receiver(442, 222, 7.4, 'teal')}
<g transform="translate(442 86)">
  <path d="M0 30q-38-28-38-52 0-20 20-20 11 0 18 13 7-13 18-13 20 0 20 20 0 24-38 52z" class="coral o"/></g>
{''.join(f'<path d="M{330+i*20} {150+i*16}q16-16 0-32" fill="none" stroke="{GLD}" stroke-width="4"/>' for i in range(2))}
<path d="M208 282q88 46 152 0" fill="none" stroke="{GLD}" stroke-width="6" stroke-linecap="round" stroke-dasharray="14 11"/>
{hand(304, 312, -1)}''')

finish(__file__)
