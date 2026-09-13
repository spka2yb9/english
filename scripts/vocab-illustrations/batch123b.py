# -*- coding: utf-8 -*-
"""第123回の描き直し。claw(こねたパン生地に見えた)、versatile(道具が読めない)、bonnet(部品が車の外に浮いた)。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')

# 肉球を真上から描くとパン生地になる。横から見た足先にして、つめを長く曲げて突き出す。
add('claw', '猫の前足の先から鋭く曲がったつめが突き出している', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-170-70q-30 60 0 100 40 54 130 60 70 4 90-30 16-30-20-56-70-50-140-74z" fill="#c8a070" class="o"/>
  <path d="M-40 26q60-16 110 6-40 34-110-6z" fill="#a8804c"/>
  <g fill="#c8a070" class="o">
''' + ''.join(f'<ellipse cx="{20+i*46}" cy="{58-i*4}" rx="27" ry="21"/>' for i in range(3)) + f'''
  </g>
  <g fill="#fffdf6" class="o">
''' + ''.join(f'<path d="M{40+i*46} 62q40 6 62 40-38 6-62-16z"/>' for i in range(3)) + f'''
    <path d="M-32 46q30 22 34 54-30-6-42-32z"/>
  </g>
  <g fill="none" stroke="#a8804c" stroke-width="3">
    <path d="M-110-40q40 30 90 40M-70-70q50 34 110 46"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 200l-90 90"/></g>''', arrow=True, ground=False)

# 抽象的な「多用途」は道具そのものより、一本で複数の仕事をこなす場面を並べる。
add('versatile', '同じ一本のナイフが、切る・むく・開ける・ねじ回すの四役をこなす', f'''
{table(340)}
<g transform="translate(300 200)">
  <path d="M-24-70h48v150h-48z" class="coral o"/>
  <path d="M-24-70q0-22 24-22t24 22z" class="corald o"/>
  <path d="M0 80v30" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7">
  <path d="M270 170q-90-10-120 60M330 170q90-10 120 60M270 250q-90 20-110 70M330 250q90 20 110 70"/>
</g>
<g transform="translate(120 250)">
  <circle r="40" class="green o"/>
  <path d="M-46-8h92" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(480 250)">
  <ellipse rx="36" ry="44" class="gold o"/>
  <path d="M-40-30q50 40 80-6" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-24 40q40-20 70 6" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
</g>
<g transform="translate(140 340)">
  <path d="M-24-46h48l-6 60q-2 12-18 12t-18-12z" fill="{TONES['green'][1]}" class="o"/>
  <path d="M-26-46h52v-12h-52z" fill="#b8bfc8" class="o"/>
  <path d="M26-56l24-10" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>
<g transform="translate(470 340)">
  <circle r="34" fill="#c8d0d8" class="o"/>
  <path d="M-16-4h32v8h-32z" fill="{INK}"/>
  <path d="M0 34v20" stroke="{INK}" stroke-width="7" fill="none"/>
</g>''', ground=False)

# エンジンを車の外に置いたら別の物に見えた。開いた蓋の下、車の中に収める。
add('bonnet', '車のボンネットを持ち上げて、中のエンジンをのぞいている', f'''
{table(370)}
<g transform="translate(330 320)">
  <path d="M-210 30h420v-56q0-20-20-20h-100l-44-44H-90l-34 44h-66q-20 0-20 20z" fill="{TONES['teal'][0]}" class="o"/>
  <path d="M-84-46h140l40 44H-118z" fill="#dceaf4" class="o"/>
  <circle cx="-120" cy="30" r="26" fill="{INK}"/><circle cx="120" cy="30" r="26" fill="{INK}"/>
  <circle cx="-120" cy="30" r="11" fill="#8f9aa6"/><circle cx="120" cy="30" r="11" fill="#8f9aa6"/>
  <path d="M-210-10h-16v30h16z" class="goldp o"/>
</g>
<g transform="translate(190 300)">
  <path d="M-64-46h128v46h-128z" fill="#3b4450" class="o"/>
  <g fill="#8f9aa6"><rect x="-52" y="-38" width="22" height="32" rx="4"/><rect x="-24" y="-38" width="22" height="32" rx="4"/><rect x="4" y="-38" width="22" height="32" rx="4"/><rect x="32" y="-38" width="22" height="32" rx="4"/></g>
  <circle cx="-70" cy="-20" r="12" class="coral o"/>
  <path d="M-70-32v-30" stroke="{TONES['coral'][0]}" stroke-width="6" fill="none"/>
</g>
<g transform="translate(180 210) rotate(-30)">
  <path d="M-130-9h260v18h-260z" fill="{TONES['teal'][2]}" class="o"/>
  <path d="M-130-9h260v6h-260z" fill="{TONES['teal'][1]}"/>
</g>
<path d="M290 280v-40" stroke="#8f9aa6" stroke-width="7" stroke-linecap="round" fill="none"/>
{person(470, 370, 0.95, -1, 'coral', 'blue', 'reach', 'cap', 'neutral')}
<g class="a" marker-end="url(#ar)"><path d="M120 120l60 60"/></g>''', arrow=True, ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 5))
