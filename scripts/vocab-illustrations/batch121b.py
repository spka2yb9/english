# -*- coding: utf-8 -*-
"""第121回の描き直し。transplant、gloomy、exercise、boarding。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
BRN='#8b6437'
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')

# 苗が しおれて見えた。根鉢を手で持ち上げ、穴から穴へ運ぶ動きにする。
add('transplant', '根のついた苗を掘り上げ、別の穴へ植え替えている', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#a8845c"/>
<path d="M0 238h600v14H0z" fill="#dfe8d8"/>
<path d="M0 238h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g fill="#6b4c28" class="o">
  <path d="M60 250q0 54 60 54t60-54z"/>
  <path d="M420 250q0 54 60 54t60-54z"/>
</g>
<g transform="translate(300 200)">
  <path d="M-40 40q0-34 40-34t40 34q-8 40-40 40t-40-40z" fill="#6b4c28" class="o"/>
  <g stroke="#4e3a22" stroke-width="5" stroke-linecap="round" fill="none">
    <path d="M-18 74q-8 22-20 30M0 78v30M20 74q8 22 22 28"/>
  </g>
  <path d="M-8 8V-60h16V8z" class="greend o"/>
  <path d="M-8-28q-56-22-48-56 46 6 48 56zM8-58q56-22 66 8-44 22-66-8zM-8-56q-46-24-38-52 38 6 38 52z" class="greenp o"/>
</g>
<g>
  <path d="M240 176q-56-14-84 8" fill="none" stroke="{SKINL}" stroke-width="30" stroke-linecap="round"/>
  <path d="M240 176q-56-14-84 8" fill="none" stroke="{SKIN}" stroke-width="25" stroke-linecap="round"/>
  <path d="M360 176q56-14 84 8" fill="none" stroke="{SKINL}" stroke-width="30" stroke-linecap="round"/>
  <path d="M360 176q56-14 84 8" fill="none" stroke="{SKIN}" stroke-width="25" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M130 190q100-120 350 20"/></g>''', arrow=True, ground=False)

# もやを全面にかけたら人が消えた。もやをやめ、暗い室内と雨の窓で陰気さを出す。
add('gloomy', '雨の降る暗い部屋で肩を落として座っている', f'''
<path d="M0 0h600v400H0z" fill="#414c5c"/>
<path d="M0 340h600v60H0z" fill="#2f3846" class="o"/>
<g transform="translate(430 180)">
  <path d="M-100-130h200v260h-200z" fill="#59667c" class="o"/>
  <path d="M-78-108h156v216h-156z" fill="#7d90aa"/>
  <path d="M0-108v216M-78 0h156" stroke="#59667c" stroke-width="7" fill="none"/>
  <g fill="none" stroke="#b6c6da" stroke-width="3.5" stroke-linecap="round">
''' + ''.join(f'<path d="M{-64+i*20} {-92+(i%4)*44}l-12 34"/>' for i in range(8)) + f'''
  </g>
</g>
<g fill="#7d90aa" opacity="0.18"><path d="M330 180L120 330V60z"/></g>
{chair(180, 350, 1.0, 'gold', 1)}
{sit(180, 350, 1.05, 1, 'violet', 'blue', 'bob', 'sad', 'down')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M120 210q-16 12-16 30M240 208q16 12 16 30"/>
</g>
<g fill="{MUTED}"><ellipse cx="180" cy="368" rx="70" ry="10" opacity="0.4"/></g>''', ground=False)

# 腕立ては横向きだと肉のかたまりに見えた。ダンベルを持ち上げる立ち姿にする。
add('exercise', 'ダンベルを両手で持ち上げて運動している', f'''
{table(360)}
<g transform="translate(300 360)">
  <path d="M-190 0h380v-16h-380z" class="tealp o"/>
</g>
{person(300, 360, 1.25, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
<g fill="{INK}">
  <g transform="translate(240 200)"><rect x="-34" y="-9" width="68" height="18" rx="6"/><rect x="-52" y="-26" width="22" height="52" rx="8"/><rect x="30" y="-26" width="22" height="52" rx="8"/></g>
  <g transform="translate(360 200)"><rect x="-34" y="-9" width="68" height="18" rx="6"/><rect x="-52" y="-26" width="22" height="52" rx="8"/><rect x="30" y="-26" width="22" height="52" rx="8"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M170 250v-60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M430 190v60"/></g>
<g fill="{TONES['blue'][0]}"><path d="M330 140q9 10 9 16t-9 7-9-7 9-16z"/></g>''', arrow=True, ground=False)

# ボーディングブリッジが荷物のベルトに見えた。タラップと乗り込む列にする。
add('boarding', 'タラップを列になって飛行機に乗り込んでいる', f'''
<path d="M0 0h600v400H0z" fill="#dceaf4"/>
<path d="M0 320h600v80H0z" fill="#8f9aa6" class="o"/>
<g transform="translate(400 200)">
  <path d="M-180-70h280q60 0 60 70t-60 70h-280q-40 0-40-70t40-70z" fill="#fffdf6" class="o"/>
  <path d="M-180-70q-70 0-100 70 30 70 100 70z" fill="#e8eef2" class="o"/>
  <g class="bluep o">
''' + ''.join(f'<circle cx="{-130+i*46}" cy="-14" r="13"/>' for i in range(7)) + f'''
  </g>
  <path d="M-70 26h56v94h-56z" fill="#5a6270" class="o"/>
  <path d="M100-70q20-90 60-90v90z" class="blue o"/>
  <path d="M50 60q-30 60-90 60h120z" class="bluep o"/>
</g>
<g transform="translate(280 320)">
  <path d="M0 0l120-96h30L30 0z" fill="#b8bfc8" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
''' + ''.join(f'<path d="M{18+i*15} {-12-i*12}h30"/>' for i in range(7)) + f'''
  </g>
  <path d="M6-10L126-106" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
{person(230, 320, 0.85, 1, 'coral', 'blue', 'carry', 'bob', 'smile', 'walk')}
{person(150, 320, 0.85, 1, 'teal', 'violet', 'carry', 'short', 'smile', 'walk')}
{person(70, 320, 0.85, 1, 'gold', 'green', 'carry', 'bun', 'smile', 'walk')}
<g class="a" marker-end="url(#ar)"><path d="M120 170q80-40 180-30"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
