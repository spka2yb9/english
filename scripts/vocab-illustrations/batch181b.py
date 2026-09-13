# -*- coding: utf-8 -*-
"""第181回の描き直し。rape / suicide の構図を取り直す。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def phone(x, y, s=1):
    """受話器つきの電話機。相談窓口の記号として使う。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-80 60q-10-70 80-70t80 70z" class="teal o"/>'
            f'<path d="M-70-30h140v18h-140z" class="teald o"/>'
            f'<g transform="translate(0 -58)">'
            f'<path d="M-72 0q0-26 26-26t26 26h92q0-26 26-26t26 26q0 24-26 24t-26-24h-92q0 24-26 24t-26-24z" '
            f'class="teald o"/></g></g>')

add('rape', '一人を囲む境界の線を、顔のない影の手が越えようとして、法の記号に止められている',
    '強姦、性暴力＝rape。同意のない性的行為を指し、法で禁じられた重大な犯罪です。', f'''
<g transform="translate(250 200)">
  <circle r="118" class="tealp" opacity="0.6"/>
  <circle r="118" fill="none" stroke="{TEA}" stroke-width="9"/></g>
{person(250, 290, 1.05, 1, 'teal', 'blue', 'stand', 'short', 'flat')}
<g opacity="0.38">
  <path d="M-10 200h56" fill="none" stroke="#6b7680" stroke-width="30" stroke-linecap="round"/>
  <path d="M34 172q40-6 46 28-10 30-46 26z" fill="#6b7680"/></g>
{ban(122, 200, 54)}
<g transform="translate(478 250)">
  <path d="M-62-80h124v160h-124z" fill="#fffefd" class="o"/>
  <path d="M-68-80h14v160h-14z" class="violetd o"/>
  {''.join(f'<rect x="-38" y="{-50+i*30}" width="{88-(i%2)*26}" height="9" rx="4.5" fill="{MUTED}"/>' for i in range(3))}
  <circle cx="12" cy="48" r="22" class="coralp o"/>
  <circle cx="12" cy="48" r="13" fill="none" stroke="{CRL}" stroke-width="3.5"/></g>
<path d="M414 200h-38" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('suicide', '暗がりでうつむく人に、相談窓口の電話の明かりがつながって手がさしのべられる',
    '自殺＝suicide。suicide prevention（自殺予防）や helpline（相談窓口）の形でよく使われます。', f'''
<path d="M0 0h250v400H0z" fill="#3b4557"/>
<path d="M250 0h60v400h-60z" fill="#55617a" opacity="0.55"/>
<g transform="translate(130 340)">
  <path d="M-64 0v-74q64-28 128 0V0z" fill="#4e6070" class="o"/>
  <path d="M-64-74q-20 48 42 56" fill="none" stroke="#8a93a5" stroke-width="19" stroke-linecap="round"/>
  <circle cx="10" cy="-118" r="30" fill="#8a93a5"/>
  <path d="M-22-126q4-34 32-34 26 0 32 32-17-15-32-6-15-9-32 8z" fill="#2f3a4d"/>
  <path d="M-2-112h22" fill="none" stroke="#3b4557" stroke-width="3.5"/></g>
<g transform="translate(440 200)">
  <circle r="132" class="goldp" opacity="0.6"/>
  <circle r="132" fill="none" stroke="{GLD}" stroke-width="4" stroke-dasharray="13 11"/></g>
{phone(440, 218, 0.92)}
<g transform="translate(440 84)">
  <path d="M0 30q-38-28-38-52 0-20 20-20 11 0 18 13 7-13 18-13 20 0 20 20 0 24-38 52z" class="coral o"/></g>
{''.join(f'<path d="M{292+i*20} {172+i*14}q16-16 0-32" fill="none" stroke="{GLD}" stroke-width="4"/>' for i in range(2))}
<path d="M206 280q86 48 150 4" fill="none" stroke="{GLD}" stroke-width="6" stroke-linecap="round" stroke-dasharray="14 11"/>
{hand(300, 306, -1)}''')

finish(__file__)
