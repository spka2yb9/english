# -*- coding: utf-8 -*-
"""第115回の描き直し。取っ手・厚み・刃の交差がぼやけた7点を描き起こす。"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))

add('saucepan', '長い取っ手が一本ついた片手鍋', f'''
<g>
  <path d="M140 180h200v76q0 40-40 40h-120q-40 0-40-40z" class="teal o"/>
  <ellipse cx="240" cy="180" rx="100" ry="24" class="tealp o"/>
  <ellipse cx="240" cy="180" rx="76" ry="16" fill="#cfe6df"/>
  <path d="M340 190h130q18 0 18 16t-18 16H340z" fill="#5b4a3c" class="o"/>
  <circle cx="452" cy="206" r="7" fill="#3b4450"/>
</g>
<path d="M100 296h380" class="a"/>''', ground=False)

add('mattress', 'ベッド枠の上に厚みのあるマットレスが載っている', f'''
<g>
  <path d="M120 262h360v34H120z" fill="#8b6437" class="o"/>
  <path d="M132 296v40M468 296v40" stroke="#8b6437" stroke-width="16" stroke-linecap="round" fill="none"/>
  <path d="M136 158h328q22 0 22 24v80H114v-80q0-24 22-24z" fill="#fffefd" class="o"/>
  <path d="M114 210h372" stroke="{MUTED}" stroke-width="2.5" fill="none"/>
  <path d="M114 236h372" stroke="{MUTED}" stroke-width="2.5" fill="none"/>
  <g fill="{MUTED}">
    <circle cx="170" cy="184" r="6"/><circle cx="250" cy="184" r="6"/><circle cx="330" cy="184" r="6"/><circle cx="410" cy="184" r="6"/>
    <circle cx="210" cy="224" r="6"/><circle cx="290" cy="224" r="6"/><circle cx="370" cy="224" r="6"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M84 158v104"/></g>
<g class="a" marker-end="url(#ar)"><path d="M84 262v-104"/></g>''', arrow=True, ground=False)

add('pillow', 'ふくらんだまくらが一つ、少し斜めに置かれている', f'''
<g transform="translate(300 200) rotate(-6)">
  <path d="M-160-70q34-26 160-26t160 26q26 40 0 84-34 28-160 28t-160-28q-26-44 0-84z" fill="#fffefd" class="o"/>
  <path d="M-160-70q34 26 160 26t160-26" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
  <path d="M-160 14q34 28 160 28t160-28" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
  <path d="M-134-52q30 40 0 78M134-52q-30 40 0 78" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
</g>
<path d="M110 306h380" class="a"/>''', ground=False)

add('stapler', 'ホチキスが紙の束の角をとじ、金具が刺さっている', f'''
<g class="paper"><path d="M120 224h230v92H120z"/><path d="M130 216h230v92H130z"/></g>
<g fill="{MUTED}" stroke="{INK}" stroke-width="2.5">
  <path d="M156 244h34v7h-34zM156 244v14M190 244v14"/>
</g>
<g transform="translate(340 168)">
  <path d="M-120 30h230q24 0 24 20t-24 20h-230z" class="teald o"/>
  <path d="M-120-14h214q30 0 30 22t-30 22h-214q-18 0-18-22t18-22z" class="teal o"/>
  <path d="M-120-14v44" stroke="{INK}" stroke-width="3.5" fill="none"/>
  <circle cx="104" cy="30" r="9" class="tealp o"/>
  <path d="M-96 8h120" stroke="{TONES['teal'][2]}" stroke-width="4" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M244 90v-44"/></g>''', arrow=True, ground=False)

add('pliers', '先が二枚のあごになったペンチ、柄は赤い', f'''
<g transform="translate(300 214)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-10 4L-120 88q-18 14-8 30t32 6L16 26z" class="coral"/>
    <path d="M10 4L120 88q18 14 8 30t-32 6L-16 26z" class="corald"/>
  </g>
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round" fill="#8f9aa6">
    <path d="M-10-6l-46-96q-6-14 8-20t22 8L4-24z"/>
    <path d="M10-6l46-96q6-14-8-20t-22 8L-4-24z"/>
  </g>
  <g fill="none" stroke="{INK}" stroke-width="2.5">
    <path d="M-30-46h-16M-38-70h-14M22-46h16M30-70h14"/>
  </g>
  <circle r="13" fill="#6f7b88" stroke="{INK}" stroke-width="2.5"/>
</g>''', ground=False)

add('scissors', '二枚の刃と赤い持ち手のはさみが紙を切っている', f'''
<g class="paper"><path d="M50 168h230v140H50z"/></g>
<path d="M164 168v140" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="9 9" fill="none"/>
<g transform="translate(320 224)">
  <g stroke="{INK}" stroke-width="2.5" stroke-linejoin="round">
    <path d="M-6-8L-170-58q-14-4-10-16t20-8L10-26z" fill="#cfd6dd"/>
    <path d="M-6 8L-170 58q-14 4-10 16t20 8L10 26z" fill="#8f9aa6"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="15" stroke-linecap="round">
    <path d="M14-14q64-26 90 4t-22 46"/>
    <path d="M14 14q64 26 90-4t-22-46"/>
  </g>
  <circle r="11" fill="#6f7b88" stroke="{INK}" stroke-width="2.5"/>
</g>''', ground=False)

add('zipper', '上着のファスナーが半分閉まり、歯がかみ合っている', f'''
<g>
  <path d="M150 50h130l-12 300H176z" class="blue o"/>
  <path d="M450 50H320l12 300h96z" class="blue o"/>
</g>
<g fill="{MUTED}" stroke="{INK}" stroke-width="2">
''' + ''.join(f'<rect x="252" y="{62+i*20}" width="22" height="11" rx="3"/><rect x="326" y="{72+i*20}" width="22" height="11" rx="3"/>' for i in range(7)) + f'''
</g>
<g transform="translate(300 224)">
  <path d="M-30-18h60v34h-60z" fill="#8f9aa6" class="o"/>
  <path d="M-10 16h20v42q0 14-10 14t-10-14z" fill="#8f9aa6" class="o"/>
  <path d="M-4 72h8v22h-8z" fill="#8f9aa6" class="o"/>
</g>
<g fill="{MUTED}" stroke="{INK}" stroke-width="2">
''' + ''.join(f'<rect x="{288 if i%2 else 290}" y="{250+i*20}" width="22" height="11" rx="3"/>' for i in range(5)) + f'''
</g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet2.html', 4))
