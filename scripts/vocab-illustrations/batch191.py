# -*- coding: utf-8 -*-
"""第191回(最終)。plus39 の50語。stork の描き直しも含む。これで8,000語すべてに絵がそろう。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('stork', '長い足と赤いくちばしのコウノトリが、煙突の巣に立つ',
    'コウノトリ＝stork。', f'''
<g transform="translate(300 330)">
  <path d="M-200 70L-40-60h80L200 70z" class="corald o"/>
  <path d="M40-60h56v-110H40z" fill="{STONE}" class="o"/>
  <path d="M34-176h68v16H34z" fill="#9aa7b1" class="o"/></g>
<g transform="translate(340 140)">
  <ellipse rx="46" ry="20" fill="#8a6a46" class="o"/>
  {''.join(f'<path d="M{-34+i*17} -12l16-10" stroke="#6a4a2a" stroke-width="3" fill="none"/>' for i in range(5))}</g>
<g transform="translate(320 90)">
  <ellipse rx="56" ry="34" fill="#fffefd" class="o"/>
  <path d="M-38-8q-40 10-50 34" fill="none" stroke="#2f3542" stroke-width="10" stroke-linecap="round"/>
  <path d="M26-20q36-14 42-52" fill="none" stroke="#fffefd" stroke-width="20" stroke-linecap="round"/>
  <circle cx="70" cy="-74" r="18" fill="#fffefd" class="o"/>
  <path d="M86-78l52 10-50 16z" class="coral o"/>
  <circle cx="76" cy="-80" r="3.4" class="ink"/>
  <path d="M-14 32v22M12 32v22" stroke="{CRL}" stroke-width="6" fill="none" stroke-linecap="round"/></g>''')

# --- plus39 ------------------------------------------------------------------

add('trampoline', 'ばねで枠に張った布の上で、子どもが跳ね上がる',
    'トランポリン＝trampoline。', f'''
<path d="M0 340h600v60H0z" class="greenp"/>
<g transform="translate(300 300)">
  <ellipse rx="180" ry="44" fill="#4e5a66" class="o"/>
  <ellipse rx="150" ry="34" fill="#2f3a4d"/>
  {''.join(f'<path d="M{int(166*math.cos(math.radians(a)))} {int(40*math.sin(math.radians(a)))}l{int(-16*math.cos(math.radians(a)))} {int(-6*math.sin(math.radians(a)))}" stroke="#8a97a3" stroke-width="4" fill="none"/>' for a in range(0, 360, 20))}
  <path d="M-150 30v40M150 30v40" stroke="{MUTED}" stroke-width="9" fill="none"/></g>
{person(300, 200, 1.1, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{arc(300, 130, 300, 250, 0, MUTED, True, 5)}''', arrow=True)

add('translator', '原文の本を見ながら、別の言語の文に置き換えていく',
    '翻訳者＝translator。', f'''
{table(300)}
{person(160, 340, 1.1, 1, 'violet', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(320 250)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  {''.join(f'<rect x="-66" y="{-46+i*26}" width="{132-(i%3)*40}" height="10" rx="5" fill="{INK}"/>' for i in range(4))}</g>
{arc(420, 200, 470, 200, 40, MUTED, True, 4)}
<g transform="translate(500 250)">
  <path d="M-70-70h140v140h-140z" class="paper"/>
  {''.join(f'<rect x="{-50+ (i%2)*6}" y="{-46+i*26}" width="{100-(i%3)*30}" height="10" rx="5" fill="{CRL}"/>' for i in range(4))}</g>''', arrow=True)

add('tray', '縁のある平たい盆にカップをのせて運ぶ',
    '盆、トレー＝tray。', f'''
{table(352)}
<g transform="translate(300 260) rotate(-4)">
  <path d="M-160-40h320v50h-320z" fill="#c9a464" class="o"/>
  <path d="M-176-44h32v40h-32zM144-44h32v40h-32z" fill="#a0764a" class="o"/>
  <path d="M-160-40h320v10h-320z" fill="#a0764a"/></g>
{''.join(f'<g transform="translate({{}} 236)"><path d="M-30-30h60v30a20 20 0 0 1-20 20h-20a20 20 0 0 1-20-20z" fill="#fffefd" class="o"/><path d="M30-20q24 0 24 18t-24 18" fill="none" stroke="{INK}" stroke-width="6"/></g>'.format(220 + i * 90) for i in range(3))}
{hand(160, 320, 1)}''')

add('treadmill', 'ベルトの上を走り、手すりのついた運動器具',
    'ランニングマシン＝treadmill。', f'''
<g transform="translate(300 320)">
  <path d="M-180 0h300v20h-300z" fill="#2f3a4d" class="o"/>
  {''.join(f'<circle cx="{-160+i*40}" cy="10" r="8" fill="#8a97a3"/>' for i in range(8))}
  <path d="M120 0v-140h20v140z" fill="#6b7680" class="o"/>
  <path d="M60-140h80v20H60z" fill="#6b7680" class="o"/>
  <path d="M70-140h60v-40H70z" fill="#dfe6ea" class="o"/>
  {''.join(f'<rect x="{80+i*16}" y="-172" width="10" height="20" fill="{INK}"/>' for i in range(3))}</g>
{person(200, 320, 1.2, 1, 'coral', 'blue', 'walk', 'cap', 'smile')}
{''.join(f'<path d="M{{}} {{}}h-50" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(150, 300 + i * 20) for i in range(2))}''', arrow=True)

add('trellis', '斜め格子の枠に、つる植物が絡んで伸びる',
    '格子の垣、つる植物用の棚＝trellis。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#e4dccb" class="o"/></g>
<g transform="translate(300 220)">
  {''.join(f'<path d="M{-200+i*50} -160L{-100+i*50} 160" stroke="#c9a464" stroke-width="8" fill="none"/>' for i in range(9))}
  {''.join(f'<path d="M{-100+i*50} -160L{-200+i*50} 160" stroke="#c9a464" stroke-width="8" fill="none"/>' for i in range(9))}</g>
<g transform="translate(300 230)">
  <path d="M-140 150q40-140 0-220t60-70" fill="none" stroke="#3f8f6a" stroke-width="9"/>
  {''.join(f'<ellipse cx="{-150+ (i%2)*40}" cy="{100-i*40}" rx="20" ry="12" class="green o" transform="rotate({-30+i*20} {-150+(i%2)*40} {100-i*40})"/>' for i in range(6))}
  {''.join(flower(-110 + i * 20, -120 + i * 24, 0.42, 'coral') for i in range(3))}</g>''')

add('tricycle', '前に一輪、後ろに二輪のついた子ども用の乗り物',
    '三輪車＝tricycle。', f'''
<path d="M0 350h600v50H0z" class="ground"/>
<g transform="translate(300 320)">
  <circle cx="-90" cy="20" r="46" class="ink"/>
  <circle cx="-90" cy="20" r="20" fill="#9aa7b1"/>
  <circle cx="80" cy="30" r="28" class="ink"/>
  <circle cx="130" cy="30" r="28" class="ink"/>
  <path d="M-90 20L20 0h90v30" fill="none" stroke="{CRL}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-90 20v-80" stroke="{CRLD}" stroke-width="10" fill="none" stroke-linecap="round"/>
  <path d="M-130-60h80" stroke="{INK}" stroke-width="10" fill="none" stroke-linecap="round"/>
  <path d="M0-20h60l-10 20H0z" class="coral o"/>
  <path d="M-90 30l-30 20" stroke="{MUTED}" stroke-width="8" fill="none" stroke-linecap="round"/></g>''')

add('trimmer', '電動の刈り込み機で、生け垣の上をそろえて刈る',
    '刈り込み機、トリマー＝trimmer。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(300 330)">
  <path d="M-220 0v-110h440V0z" class="green o"/>
  <path d="M-220-110h440" fill="none" stroke="#2a6b4c" stroke-width="6"/></g>
<g transform="translate(300 190) rotate(-8)">
  <path d="M-40-30h100v50h-100z" fill="#e86452" class="o"/>
  <path d="M-160-14h120v22h-120z" fill="#c3cbd1" class="o"/>
  {''.join(f'<path d="M{-150+i*20} 8l10 12 10-12z" fill="#8a97a3"/>' for i in range(6))}
  <path d="M40 20v40h40V20" fill="none" stroke="#c8453a" stroke-width="12"/></g>
{''.join(f'<ellipse cx="{{}}" cy="{{}}" rx="14" ry="8" class="green o" transform="rotate({{}} {{}} {{}})"/>'.format(150 + i * 70, 250 + (i % 2) * 26, -20 + i * 18, 150 + i * 70, 250 + (i % 2) * 26) for i in range(4))}''')

add('tripod', '三本脚の台にカメラを据えて、高さを合わせる',
    '三脚＝tripod。', f'''
<path d="M0 360h600v40H0z" class="ground"/>
<g transform="translate(300 360)">
  <path d="M0-180L-110 0M0-180L110 0M0-180v180" stroke="{MUTED}" stroke-width="11" fill="none" stroke-linecap="round"/>
  <path d="M-60-100h120" stroke="#8a97a3" stroke-width="7" fill="none"/>
  <path d="M-16-200h32v24h-32z" fill="#6b7680" class="o"/></g>
<g transform="translate(300 140)">
  <path d="M-70-30h140v60h-140z" fill="#2f3542" class="o"/>
  <circle cx="10" cy="0" r="24" fill="#4e5a66" class="o"/>
  <circle cx="10" cy="0" r="12" fill="#8a97a3"/>
  <path d="M-50-46h40v16h-40z" fill="#2f3542" class="o"/></g>''')

add('trowel', '片手の小さなこてで、土に穴を掘る',
    '移植ごて、こて＝trowel。', f'''
<path d="M0 280h600v120H0z" fill="#5b4636"/>
<g transform="translate(300 290) rotate(20)">
  <path d="M-14-140h28v90h-28z" fill="{BRN}" class="o"/>
  <path d="M-30-160h60v24h-60z" fill="#8a6a46" class="o"/>
  <path d="M-40-50h80l-14 110q-26 16-52 0z" fill="#c3cbd1" class="o"/>
  <path d="M0-46v104" stroke="#9aa7b1" stroke-width="4" fill="none"/></g>
<g transform="translate(210 320)"><path d="M-50-16q50-24 100 0-20 30-50 30t-50-30z" fill="#3f3126"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="#3f3126"/>'.format(160 + (i * 29) % 80, 300 + (i * 19) % 40, 5 + i % 3) for i in range(6))}''')

add('tub', 'ふたつきの円い容器に、アイスクリームが入っている',
    'おけ、たらい／容器＝tub。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-90-50h180l-16 110h-148z" fill="#fffefd" class="o"/>
  <ellipse cy="-50" rx="90" ry="24" fill="#dfeaf2" class="o"/>
  <path d="M-70-20h140l-10 60h-120z" class="coralp o"/>
  <circle cx="-20" cy="-2" r="16" class="coral o"/></g>
<g transform="translate(300 180) rotate(-14)">
  <ellipse rx="96" ry="26" fill="#dfeaf2" class="o"/>
  <path d="M-96 0q96 22 192 0v12q-96 22-192 0z" fill="#b9c9d4" class="o"/></g>''')

add('tumbler', '取っ手のない平底のコップに、水が注がれている',
    'タンブラー＝tumbler。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-60-90h120l-10 180h-100z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="4"/>
  <path d="M-52-10h104l-6 100h-92z" class="bluep"/>
  <path d="M-60-90h120l-10 180h-100z" fill="none" class="o"/>
  <path d="M-44-70q0 40 8 70" fill="none" stroke="#ffffff" stroke-width="7" opacity="0.8"/></g>
{''.join(drop(300, 120 + i * 26, 1.0, 'blue') for i in range(2))}''')

add('turnip', '白く丸い根菜に、上から緑の葉が出ている',
    'カブ＝turnip。', f'''
{table(352)}
<g transform="translate(280 280)">
  <path d="M-70 10q0-80 70-80t70 80q0 60-70 60t-70-60z" fill="#fffefd" class="o"/>
  <path d="M-40 20q40 26 80 0" fill="none" stroke="#e0dcd0" stroke-width="4"/>
  <path d="M0 70v40" stroke="#e0dcd0" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path d="M-20-74q-10-50 6-64 12 30 14 64M10-74q4-56 24-70-10 40-6 70" fill="none" stroke="#3f8f6a" stroke-width="6"/>
  <ellipse cx="-30" cy="-128" rx="26" ry="14" class="green o" transform="rotate(-24 -30 -128)"/>
  <ellipse cx="36" cy="-140" rx="26" ry="14" class="green o" transform="rotate(20 36 -140)"/></g>''')

add('turret', '城の角に立つ、円い小さな塔',
    '小塔、やぐら＝turret。', f'''
<path d="M0 350h600v50H0z" class="greenp"/>
<g transform="translate(300 350)">
  <path d="M-180 0v-150h360V0z" fill="#e8ddc9" class="o"/>
  <path d="M-180-150v-26h34v-16h34v16h40v-16h34v16h40v-16h34v16h34v26z" fill="#e8ddc9" class="o"/>
  <path d="M-30 0v-70h60V0z" class="corald o"/></g>
<g transform="translate(150 350)">
  <path d="M-50 0v-220h100V0z" fill="#d8cdb6" class="o"/>
  <path d="M-60-220h120l-60-90z" class="corald o"/>
  <path d="M-20-170h40v50h-40z" fill="#2f3542" class="o"/>
  <path d="M-50-220v-14h100v14z" fill="#c8b898"/></g>
{ring(150, 240, 0, True)}''')

add('typewriter', '活字のキーと紙をはさむローラーのついた機械',
    'タイプライター＝typewriter。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-140-30h280v80h-280z" fill="#4e5a66" class="o"/>
  {''.join(f'<circle cx="{-110+ (i%9)*26}" cy="{-8+(i//9)*24}" r="9" fill="#dfe6ea" stroke="{INK}" stroke-width="2"/>' for i in range(27))}
  <path d="M-110-60h220v30h-220z" fill="#6b7680" class="o"/>
  <path d="M-120-70h240v14h-240z" fill="#8a97a3" class="o"/>
  <circle cx="-124" cy="-64" r="12" fill="#6b7680" class="o"/>
  <circle cx="124" cy="-64" r="12" fill="#6b7680" class="o"/>
  <path d="M-70-140h140v70h-140z" class="paper"/>
  {''.join(f'<rect x="-50" y="{-120+i*22}" width="{100-(i%2)*30}" height="8" rx="4" fill="{MUTED}"/>' for i in range(2))}</g>''')

add('underpass', '道路の下をくぐる地下道を通って、向こう側へ渡る',
    '地下道、アンダーパス＝underpass。', f'''
<path d="M0 0h600v160H0z" class="ground"/>
<path d="M0 140h600v30H0z" fill="#9aa7b1"/>
{''.join(f'<rect x="{{}}" y="148" width="50" height="10" fill="#fffefd"/>'.format(40 + i * 110) for i in range(5))}
<g transform="translate(300 280)">
  <path d="M-300-110h600v230h-600z" fill="#5b5346"/>
  <path d="M-160 120v-90q0-70 160-70t160 70v90z" fill="#eef4f7" class="o"/>
  <path d="M-130 120v-84q0-56 130-56t130 56v84z" fill="#dfe6ea"/></g>
{person(300, 380, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{''.join(f'<circle cx="{{}}" cy="230" r="10" class="goldp o"/>'.format(220 + i * 160) for i in range(2))}''')

add('urn', '口の広い大きなつぼが、台の上に置かれている',
    'つぼ、骨つぼ＝urn。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-60-70q-40 50-30 100 10 50 90 50t90-50q10-50-30-100z" fill="#a2825e" class="o"/>
  <path d="M-70-70h140v-20h-140z" fill="#8a6a46" class="o"/>
  <path d="M-60-90q60-24 120 0" fill="none" stroke="#8a6a46" stroke-width="6"/>
  <path d="M-60-40q-36 0-36 30t36 30M60-40q36 0 36 30t-36 30" fill="none" stroke="#8a6a46" stroke-width="12"/>
  <path d="M-40 80h80v20h-80z" fill="#8a6a46" class="o"/>
  <path d="M-40-10q40 20 80 0" fill="none" stroke="#8a6a46" stroke-width="4"/></g>''')

add('utensil', '引き出しの中に、台所で使う道具がそろっている',
    '(台所の)道具、器具＝utensil。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-190-60h380v120h-380z" fill="#c9a464" class="o"/>
  <path d="M-190-60h380v14h-380z" fill="#a0764a"/>
  <path d="M-30-84h60v20h-60z" class="goldd o"/></g>
{''.join(f'<g transform="translate({{}} 280) rotate({{}})"><path d="M-6-56h12v104h-12z" fill="#c3cbd1" class="o"/>{{}}</g>'.format(160 + i * 70, -10 + i * 7, o) for i, o in enumerate([
  f'<ellipse cy="-66" rx="18" ry="24" fill="#dfe6ea" class="o"/>',
  f'<path d="M-16-60h32v22h-32z" fill="#c3cbd1" class="o"/>',
  f'<path d="M-20-70q20 26 40 0v34h-40z" fill="#c3cbd1" class="o"/>',
  f'<path d="M-22-72h44v40h-44z" fill="#c3cbd1" class="o"/>',
  f'<circle cy="-62" r="22" fill="none" stroke="#c3cbd1" stroke-width="7"/>']))}''')

add('valve', 'パイプの途中のハンドルを回して、流れを止める',
    '弁、バルブ＝valve。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-240-24h180v48h-180zM60-24h180v48H60z" fill="#8a97a3" class="o"/>
  <path d="M-70-40h140v80h-140z" fill="#6b7680" class="o"/>
  <path d="M-10-100h20v60h-20z" fill="#6b7680" class="o"/>
  <circle cy="-110" r="44" fill="none" stroke="{CRL}" stroke-width="13"/>
  <path d="M-44-110h88M0-154v88" stroke="{CRL}" stroke-width="10" fill="none"/></g>
<g transform="translate(300 130)"><path d="M-60 0a60 60 0 0 1 40-56" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="9 8" marker-end="url(#ar)"/></g>''', arrow=True)

add('vase', '背の高いガラスの花びんに、花が生けてある',
    '花びん＝vase。', f'''
{table(352)}
{''.join(flower(270 + i * 40, 150 - (i % 2) * 30, 0.6, c) for i, c in enumerate(['coral', 'gold', 'violet']))}
<g transform="translate(300 290)">
  {''.join(f'<path d="M{-20+i*20} -80v-60" stroke="{GRND}" stroke-width="5" fill="none"/>' for i in range(3))}
  <path d="M-40-90q-30 40-24 90 6 50 64 50t64-50q6-50-24-90z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-56-10q56 24 112 0 4 40-56 40t-56-40z" class="bluep"/></g>''')

add('venison', '皿に盛られたシカ肉の切り身に、ソースが添えられる',
    'シカ肉＝venison。', f'''
{table(352)}
<g transform="translate(300 290)">
  <ellipse rx="150" ry="40" fill="#fffefd" class="o"/>
  <path d="M-70-24q70-30 140 0 10 34-70 34t-70-34z" fill="#8a4232" class="o"/>
  <path d="M-50-14q50-16 100 0" fill="none" stroke="#6a2c20" stroke-width="4"/>
  {''.join(f'<ellipse cx="{-100+i*28}" cy="8" rx="16" ry="9" class="green o"/>' for i in range(2))}
  <path d="M70 6q30-10 50 6-24 14-50 2z" fill="#b5744a" class="o"/></g>
<g transform="translate(120 160)">
  <path d="M-20 40q-30-20-24-48 22 4 30 20 4-20 18-24-4 18 6 28z" fill="#c8a05f" class="o"/></g>''')

add('veranda', '屋根のついた細長い縁側に、いすが並ぶ',
    'ベランダ、屋根つきの縁側＝veranda。', f'''
<path d="M0 340h600v60H0z" class="greenp"/>
<g transform="translate(300 340)">
  <path d="M-260 0v-70h520V0z" fill="#c9a464" class="o"/>
  <path d="M-260-70h520v-14h-520z" fill="#a0764a"/>
  {''.join(f'<path d="M{-220+i*110} -84v-120" stroke="#c9a464" stroke-width="14" fill="none"/>' for i in range(5))}
  <path d="M-280-204h560v26h-560z" fill="#a0764a" class="o"/>
  <path d="M-300-204h600l-40-50h-520z" class="corald o"/>
  {''.join(f'<path d="M{-220+i*110} -120h110" stroke="#c9a464" stroke-width="9" fill="none"/>' for i in range(4))}</g>
{chair(200, 340, 0.9, 'gold', 1)}
{chair(400, 340, 0.9, 'gold', -1)}''')

add('vet', '白衣の獣医が、診察台の上の犬を診る',
    '獣医＝vet。', f'''
{table(300)}
{person(160, 330, 1.2, 1, 'violet', 'blue', 'reach', 'bun', 'smile')}
<g transform="translate(420 280)">
  <ellipse rx="80" ry="40" fill="#c8a05f" class="o"/>
  <circle cx="66" cy="-30" r="30" fill="#c8a05f" class="o"/>
  <path d="M40-48q-20-18-10-38 22 8 28 26zM92-50q20-18 10-38-22 8-28 26z" fill="#a8814a" class="o"/>
  <circle cx="56" cy="-34" r="4" class="ink"/><circle cx="78" cy="-34" r="4" class="ink"/>
  <ellipse cx="68" cy="-16" rx="9" ry="6" fill="#5b4030"/>
  <path d="M-50 34v18M-8 38v14M34 38v14" stroke="#c8a05f" stroke-width="12" fill="none" stroke-linecap="round"/></g>
<g transform="translate(180 240)">
  <path d="M-30-40q-24 70 20 96" fill="none" stroke="{MUTED}" stroke-width="6"/>
  <circle cx="-10" cy="60" r="14" fill="none" stroke="{MUTED}" stroke-width="6"/></g>''')

add('viaduct', '谷をまたぐアーチの並んだ高架橋を、列車が渡る',
    '高架橋＝viaduct。', f'''
<path d="M0 340h600v60H0z" class="greenp"/>
<path d="M0 340q140-100 300-100t300 100z" fill="#c8d8c0" class="o"/>
<g transform="translate(300 340)">
  <path d="M-280-160h560v40h-560z" fill="#b5a894" class="o"/>
  {''.join(f'<g transform="translate({-224+i*112} 0)"><path d="M-46 0v-90q0-36 46-36t46 36V0z" fill="#b5a894" stroke="{INK}" stroke-width="2.5"/><path d="M-24 0v-84q0-20 24-20t24 20V0z" fill="#c8d8c0"/></g>' for i in range(5))}</g>
<g transform="translate(280 160)">
  <path d="M-120-40h240v40h-240z" class="teal o"/>
  {''.join(f'<rect x="{-100+i*46}" y="-30" width="30" height="20" class="tealp o"/>' for i in range(5))}</g>''')

add('village', '小さな家が数軒と教会の集まった村',
    '村＝village。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<path d="M0 300q140-70 300-40t300 40" fill="#c8d8c0" class="o"/>
{''.join(house(100 + i * 130, 320, 0.55, c) for i, c in enumerate(['coral', 'teal', 'gold']))}
<g transform="translate(470 320)">
  <path d="M-50 0v-90h100V0z" fill="#e8ddc9" class="o"/>
  <path d="M-20 0v-180h40V0z" fill="#e8ddc9" class="o"/>
  <path d="M-26-180L0-240l26 60z" fill="#8a97a3" class="o"/>
  <path d="M-14 0v-46h28V0z" class="corald o"/></g>
<path d="M40 380q140-50 280-30t240 30" fill="none" stroke="#d8cdb6" stroke-width="20" stroke-linecap="round"/>''')

add('vineyard', '丘の斜面に、ぶどうの木の列が整然と並ぶ',
    'ぶどう園＝vineyard。', f'''
<path d="M0 260q160-60 300-30t300 30v140H0z" class="greenp o"/>
{''.join(f'<g transform="translate({{}} {{}})"><path d="M0 0v-60" stroke="{BRN}" stroke-width="7" fill="none"/><path d="M-40-60h80" stroke="{BRN}" stroke-width="5" fill="none"/>{{}}</g>'.format(70 + (i % 5) * 120, 320 + (i // 5) * 50, ''.join(f'<circle cx="{-24+j*16}" cy="{-70-(j%2)*12}" r="8" fill="#6a3f8a" stroke="{INK}" stroke-width="1.5"/>' for j in range(4))) for i in range(10))}
{sun(510, 80, 36)}''')

add('vocabulary', '辞書と単語カードが積まれ、覚えた語が増えていく',
    '語彙、単語力＝vocabulary。', f'''
{table(352)}
{book(200, 250, 1.15, 'teal')}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M-50-32h100v64h-100z" class="paper"/><rect x="-34" y="-14" width="{{}}" height="10" rx="5" fill="{INK}"/></g>'.format(430 + (i % 2) * 20, 310 - i * 30, -8 + i * 6, 68 - (i % 2) * 20) for i in range(4))}
{''.join(spark(350 + i * 30, 130 + (i % 2) * 30, 0.6, 'gold') for i in range(2))}
{arc(300, 190, 380, 190, 44, MUTED, True, 4)}''', arrow=True)

add('waiter', '盆を持った給仕が、客のテーブルへ料理を運ぶ',
    '給仕、ウェイター＝waiter。', f'''
{table(300)}
{sit(460, 300, 1.0, 1, 'coral', 'blue', 'bob', 'smile', 'lap')}
{chair(466, 300, 0.9, 'gold', 1)}
{person(180, 340, 1.25, 1, 'blue', 'green', 'up', 'short', 'smile')}
<g transform="translate(238 190) rotate(-4)">
  <ellipse rx="80" ry="20" fill="#c9a464" class="o"/>
  <ellipse cx="-20" cy="-14" rx="40" ry="12" fill="#fffefd" class="o"/>
  <path d="M22-26h36v20H22z" class="coralp o"/></g>
{arc(300, 160, 400, 200, 50, MUTED, True, 4)}''', arrow=True)

add('wallpaper', '柄のついた紙を壁に貼り、しわを伸ばす',
    '壁紙＝wallpaper。', f'''
<g transform="translate(300 200)">
  <path d="M-280-180h560v360h-560z" fill="#e4dccb" class="o"/>
  <path d="M-260-160h240v340h-240z" class="violetp o"/>
  {''.join(f'<circle cx="{-230+ (i%4)*60}" cy="{-130+(i//4)*60}" r="12" fill="{VIO}" opacity="0.6"/>' for i in range(20))}</g>
<g transform="translate(360 200) rotate(6)">
  <path d="M-40-180h120v360h-120z" class="violetp o"/>
  {''.join(f'<circle cx="{-10+ (i%2)*50}" cy="{-150+(i//2)*60}" r="12" fill="{VIO}" opacity="0.6"/>' for i in range(12))}
  <path d="M80-180q30 20 0 40" fill="#c8bade" class="o"/></g>
{hand(460, 150, -1)}''')

add('washbasin', '洗面台の上の蛇口から、水が流れる',
    '洗面台＝washbasin。', f'''
<g transform="translate(300 180)">
  <path d="M-240-160h480v300h-480z" fill="#eef4f7" class="o"/>
  {''.join(f'<path d="M{-240+i*80} -160v300" stroke="#d7e3ea" stroke-width="3" fill="none"/>' for i in range(1, 6))}</g>
<g transform="translate(300 250)">
  <path d="M-110-20q0 70 110 70t110-70z" fill="#fffefd" class="o"/>
  <ellipse cy="-20" rx="110" ry="28" fill="#fffefd" class="o"/>
  <ellipse cy="-18" rx="88" ry="20" fill="#eef4f7"/>
  <path d="M-24 50h48v90h-48z" fill="#fffefd" class="o"/>
  <path d="M0-70v34" stroke="#9aa7b1" stroke-width="10" fill="none"/>
  <path d="M0-70q0-24-24-24" fill="none" stroke="#9aa7b1" stroke-width="10"/></g>
{''.join(drop(300, 200 + i * 22, 0.9, 'blue') for i in range(2))}''')

add('washer', 'ボルトの下に薄い輪の座金をはさんで締める',
    '(ねじの)座金、ワッシャー＝washer。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-160-20h320v40h-320z" fill="#c3cbd1" class="o"/></g>
<g transform="translate(300 280)">
  <ellipse rx="70" ry="20" fill="#8a97a3" class="o"/>
  <ellipse rx="26" ry="8" fill="#fffaf1" class="o"/></g>
<g transform="translate(300 180)">
  <path d="M-22 0h44v80h-44z" fill="#6b7680" class="o"/>
  <path d="M-40-40h80l-14-30h-52z" fill="#6b7680" class="o"/></g>
{line(300, 230, 300, 254, MUTED, True, 4)}
{ring(300, 280, 90, True)}''', arrow=True)

add('wastebin', '紙くずを入れる小さなごみ箱が、机のそばに置かれる',
    'くずかご、ごみ箱＝wastebin。', f'''
{table(300)}
<g transform="translate(400 340)">
  <path d="M-60-90l12 90h96l12-90z" fill="#8a97a3" class="o"/>
  {''.join(f'<path d="M{-48+i*24} -86l8 86" stroke="#6b7680" stroke-width="4" fill="none"/>' for i in range(5))}
  <ellipse cy="-90" rx="60" ry="16" fill="#b5bec4" class="o"/></g>
<g transform="translate(360 200) rotate(24)">
  <path d="M-30-26q30-14 60 0 10 30-6 40h-48q-16-10-6-40z" class="paper"/></g>
{arc(250, 200, 350, 210, 50, MUTED, True, 4)}
{person(150, 340, 1.05, 1, 'teal', 'blue', 'give', 'short', 'smile')}''', arrow=True)

add('watchdog', '見張り役の犬が、門の前で身構えて番をする',
    '監視機関、番犬＝watchdog。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(460 330)">
  <path d="M-110-160h40v160h-40zM70-160h40v160H70z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-60+i*30} -140v140" stroke="{BRN}" stroke-width="9" fill="none"/>' for i in range(5))}
  <path d="M-70-140h140M-70-70h140" stroke="{BRN}" stroke-width="9" fill="none"/></g>
<g transform="translate(220 300)">
  <ellipse rx="80" ry="44" fill="#5b4636" class="o"/>
  <circle cx="66" cy="-34" r="32" fill="#5b4636" class="o"/>
  <path d="M40-56l-4-30 26 18zM92-58l14-28 8 28z" fill="#5b4636" class="o"/>
  <circle cx="54" cy="-38" r="4.5" fill="#fffefd"/><circle cx="78" cy="-38" r="4.5" fill="#fffefd"/>
  <ellipse cx="66" cy="-18" rx="10" ry="7" fill="#2f2620"/>
  <path d="M50-4q16 10 32 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-52 38v26M-10 42v22M32 42v22" stroke="#5b4636" stroke-width="13" fill="none" stroke-linecap="round"/>
  <path d="M-78-10q-30-18-24-48" fill="none" stroke="#5b4636" stroke-width="11" stroke-linecap="round"/></g>''')

add('watering can', '注ぎ口の先が蓮口になったじょうろで、水をやる',
    'じょうろ＝watering can。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<g transform="translate(220 250) rotate(-16)">
  <path d="M-70-50h140v100a24 24 0 0 1-24 24h-92a24 24 0 0 1-24-24z" fill="#4e86c6" class="o"/>
  <path d="M-70-30h140" fill="none" stroke="#315f98" stroke-width="4"/>
  <path d="M-70-50q70-24 140 0" fill="none" stroke="#315f98" stroke-width="7"/>
  <path d="M70-30h60l30-30h20l-40 60H70z" class="blue o"/>
  <ellipse cx="176" cy="-56" rx="22" ry="12" fill="#315f98" class="o" transform="rotate(-40 176 -56)"/>
  <path d="M-30-70q30-30 60 0" fill="none" stroke="#315f98" stroke-width="10"/></g>
{''.join(drop(400 + (i % 3) * 24, 190 + (i // 3) * 30 + (i % 3) * 12, 0.9, 'blue') for i in range(6))}
{''.join(f'<g transform="translate({{}} 330)"><path d="M0 0v-40" stroke="{GRND}" stroke-width="6" fill="none"/><ellipse cx="-16" cy="-44" rx="16" ry="9" class="green o"/><ellipse cx="16" cy="-50" rx="16" ry="9" class="green o"/></g>'.format(400 + i * 60) for i in range(3))}''')

add('wax', 'ろうそくのろうが溶けて、横へ流れ落ちる',
    'ろう、ワックス＝wax。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-40 0q-6-140 0-160h80q6 20 0 160z" fill="#f0e6d2" class="o"/>
  <path d="M-40-160q40-20 80 0-14 30-40 30t-40-30z" fill="#e2d4b4"/>
  <path d="M0-160v-20" stroke="{INK}" stroke-width="4" fill="none"/>
  {flame(0, -186, 0.3)}
  <path d="M-40-130q-20 40-10 80 14-30 10-80zM40-124q22 34 12 76-16-28-12-76z" fill="#f6efe1" class="o"/>
  <ellipse cy="4" rx="70" ry="16" fill="#f0e6d2" class="o"/></g>''')

add('weathervane', '屋根の上でニワトリ形の風見が、風の向きを示す',
    '風見、風向計＝weathervane。', f'''
<path d="M0 350h600v50H0z" class="greenp"/>
<g transform="translate(300 350)">
  <path d="M-160 0v-90h320V0z" fill="#e8ddc9" class="o"/>
  <path d="M-180-90L0-200l180 110z" class="corald o"/></g>
<g transform="translate(300 150)">
  <path d="M-6 0h12v-110h-12z" fill="{MUTED}"/>
  <path d="M-70-70h140M-70-70v0M0-140v140" stroke="{MUTED}" stroke-width="6" fill="none"/>
  <path d="M-70-70l-14-10v20zM70-70l14-10v20z" fill="{MUTED}"/>
  <g transform="translate(20 -136)">
    <ellipse rx="34" ry="22" fill="#6b7680" class="o"/>
    <circle cx="28" cy="-18" r="15" fill="#6b7680" class="o"/>
    <path d="M40-24l22 6-22 8z" class="gold o"/>
    <path d="M22-32l-4-16 16 8z" class="coral o"/>
    <path d="M-30 6q-26 10-30 34 24-4 36-22z" fill="#6b7680" class="o"/></g></g>
{''.join(f'<path d="M40 {{}}q80-16 160 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>'.format(80 + i * 40) for i in range(2))}''')

add('wetsuit', '体にぴったりした黒いスーツを着て、海へ入る',
    'ウェットスーツ＝wetsuit。', f'''
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(300 250)">
  <path d="M-60-100q60-26 120 0 20 130 0 190h-120q-20-60 0-190z" fill="#2f3542" class="o"/>
  <path d="M-60-96l-46 24 30 90 26-14M60-96l46 24-30 90-26-14" fill="#2f3542" class="o"/>
  <path d="M-50 90l-10 110h44l16-80M50 90l10 110H16l-16-80" fill="#2f3542" class="o"/>
  <circle cx="0" cy="-136" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-38-144q4-40 38-40 32 0 38 38-20-18-38-8-20-10-38 10z" fill="#2f3542"/>
  <circle cx="-12" cy="-136" r="3.4" class="ink"/><circle cx="12" cy="-136" r="3.4" class="ink"/>
  <path d="M-10-118q10 9 20 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M0-100v190" stroke="{CRL}" stroke-width="5" fill="none"/></g>''')

add('wheelbarrow', '前に一輪、後ろに取っ手のついた手押し車で土を運ぶ',
    '手押し車、一輪車＝wheelbarrow。', f'''
<path d="M0 340h600v60H0z" class="greenp"/>
<g transform="translate(300 300)">
  <path d="M-110-50h180l-24 60h-140z" class="coral o"/>
  <path d="M-110-50q90-20 180 0" fill="none" stroke="{CRLD}" stroke-width="4"/>
  <circle cx="80" cy="34" r="34" class="ink"/>
  <circle cx="80" cy="34" r="15" fill="#9aa7b1"/>
  <path d="M-110-30l-80 50M-110 10l-80 30" stroke="{BRN}" stroke-width="10" fill="none" stroke-linecap="round"/>
  <path d="M-60 10l-20 40" stroke="{MUTED}" stroke-width="8" fill="none"/></g>
<g transform="translate(280 234)">
  <path d="M-70 16q-16-40 20-50 50-14 90 4 30 16 10 46z" fill="#5b4636" class="o"/></g>''')

add('whistle', '審判が口にくわえた笛を吹き、音が鳴り響く',
    '笛、口笛＝whistle。', f'''
{person(210, 350, 1.3, 1, 'violet', 'blue', 'reach', 'cap', 'flat')}
<g transform="translate(300 230) rotate(-10)">
  <path d="M-50-22h70l26 22-26 22h-70z" fill="#c3cbd1" class="o"/>
  <circle cx="20" cy="0" r="12" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <path d="M-50-14h-30v28h30z" fill="#8a97a3" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}a{{}} {{}} 0 0 1 0 {{}}" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>'.format(370, 230 - 24 - i * 22, 24 + i * 22, 24 + i * 22, 48 + i * 44) for i in range(3))}''')

add('whiteboard', '白い板に色のペンで書き、消して使う',
    'ホワイトボード＝whiteboard。', f'''
<g transform="translate(300 200)">
  <path d="M-240-150h480v300h-480z" fill="#c3cbd1" class="o"/>
  <path d="M-220-130h440v260h-440z" fill="#fffefd" class="o"/>
  <path d="M-180-80h200v10h-200z" fill="{TEA}"/>
  <path d="M-180-40h140v10h-140z" fill="{CRL}"/>
  <path d="M-180 0h180v10h-180z" fill="{BLU}"/>
  <path d="M60-80q40 40 0 80" fill="none" stroke="{GLD}" stroke-width="8"/>
  <path d="M-240 130h480v20h-480z" fill="#9aa7b1" class="o"/>
  {''.join(f'<rect x="{-180+i*46}" y="126" width="34" height="12" rx="4" fill="{c}"/>' for i, c in enumerate(['#e86452', '#238b83', '#4e86c6']))}</g>
{hand(390, 130, 1)}''')

add('wick', 'ろうそくの中心を通る糸の芯に、火がともる',
    '(ろうそくやランプの)芯＝wick。', f'''
{table(352)}
<g transform="translate(300 290)">
  <path d="M-50 0q-6-150 0-170h100q6 20 0 170z" fill="#f0e6d2" class="o"/>
  <ellipse cy="-170" rx="50" ry="14" fill="#e2d4b4" class="o"/>
  <path d="M0-170v-30" stroke="{INK}" stroke-width="5" fill="none"/>
  <g opacity="0.35"><path d="M0-170v150" stroke="{INK}" stroke-width="4" stroke-dasharray="9 8" fill="none"/></g>
  {flame(0, -206, 0.32)}</g>
{ring(300, 100, 54, True)}''')

add('windmill', '四枚の羽根をもつ風車が、丘の上で回る',
    '風車＝windmill。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<path d="M0 330q140-70 300-40t300 40" fill="#c8d8c0" class="o"/>
<g transform="translate(300 320)">
  <path d="M-70 0l20-180h100l20 180z" fill="#e8ddc9" class="o"/>
  <path d="M-54-180h108l-14-40h-80z" class="corald o"/>
  <path d="M-24-60h48v60h-48z" fill="#8a6a46" class="o"/>
  <g transform="translate(0 -210)">
    {''.join(f'<g transform="rotate({i*90+20})"><path d="M-9 0h18v-120h-18z" fill="#c9a464" stroke="{INK}" stroke-width="2.5"/><path d="M9-20h34v-90H9z" fill="#f0e6d2" stroke="{INK}" stroke-width="2"/></g>' for i in range(4))}
    <circle r="12" fill="#8a6a46" class="o"/></g></g>
<g transform="translate(300 60)"><path d="M-50 0a50 50 0 0 1 30-46" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="9 8" marker-end="url(#ar)"/></g>''', arrow=True)

add('windowpane', '窓わくにはまったガラスを、雨が流れ落ちる',
    '窓ガラス＝windowpane。', f'''
<g transform="translate(300 200)">
  <path d="M-200-160h400v320h-400z" fill="#e8ddc9" class="o"/>
  <path d="M-170-130h150v110h-150zM20-130h150v110H20zM-170 20h150v110h-150zM20 20h150v110H20z" fill="#cfe4f0" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q10 30 0 60" fill="none" stroke="#9fc8dd" stroke-width="6" stroke-linecap="round"/>'.format(150 + (i * 47) % 300, 100 + (i * 37) % 200) for i in range(9))}
{''.join(drop(160 + (i * 61) % 290, 120 + (i * 41) % 180, 0.8, 'blue') for i in range(6))}''')

add('wineglass', '脚のついた薄いグラスに、赤い液が注がれている',
    'ワイングラス＝wineglass。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-60-80q0 90 60 90t60-90z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-50-30q0 50 50 50t50-50z" fill="#8a2c3a"/>
  <path d="M-60-80q0 90 60 90t60-90z" fill="none" class="o"/>
  <path d="M-6 10h12v90h-12z" fill="#e6f2f6" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="102" rx="56" ry="14" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/></g>''')

add('wok', '底の丸い深い中華なべで、野菜を強火で炒める',
    '中華なべ＝wok。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-140-30q0 100 140 100t140-100z" fill="#4e5a66" class="o"/>
  <ellipse cy="-30" rx="140" ry="36" fill="#2f3542"/>
  <path d="M-140-30h-50v18h50M140-30h50v18h-50" fill="#8a97a3" class="o"/>
  {''.join(f'<ellipse cx="{-60+i*40}" cy="-30" rx="22" ry="11" class="green o"/>' for i in range(3))}
  <circle cx="60" cy="-24" r="12" class="coral o"/></g>
{''.join(f'<path d="M{{}} {{}}q16-22 0-40" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(220 + i * 60, 180 - i * 12) for i in range(3))}
{flame(300, 380, 0.5)}''')

add('woodpecker', '木の幹にとまったキツツキが、くちばしで幹をたたく',
    'キツツキ＝woodpecker。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(200 200)">
  <path d="M-50-200h100v330h-100z" fill="#a0764a" class="o"/>
  {''.join(f'<path d="M{-36+i*24} -200v330" stroke="#8a6437" stroke-width="3" fill="none"/>' for i in range(3))}
  {''.join(f'<circle cx="{40}" cy="{-100+i*40}" r="7" fill="#5b4030"/>' for i in range(3))}</g>
<g transform="translate(300 150) rotate(-16)">
  <ellipse rx="46" ry="30" fill="#2f3542" class="o"/>
  <path d="M-10-14q40-14 60 6-30 16-60 4z" fill="#fffefd" class="o"/>
  <circle cx="-40" cy="-18" r="22" fill="#2f3542" class="o"/>
  <path d="M-40-38q-14-16-4-24 14 6 14 22z" class="coral o"/>
  <path d="M-58-24l-46-8 44 20z" class="gold o"/>
  <circle cx="-46" cy="-22" r="3.4" fill="#fffefd"/>
  <path d="M40 14q30 14 40 40" fill="none" stroke="#2f3542" stroke-width="10" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}l16-14" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(300 + i * 20, 110 - i * 14) for i in range(2))}''')

add('workbench', '万力のついた頑丈な作業台に、工具が並ぶ',
    '作業台＝workbench。', f'''
<path d="M0 360h600v40H0z" class="ground"/>
<g transform="translate(300 360)">
  <path d="M-240-120h480v30h-480z" fill="#c9a464" class="o"/>
  <path d="M-210-90v90h26v-90zM184-90v90h26v-90z" fill="#a0764a" class="o"/>
  <path d="M-210-40h420v16h-420z" fill="#a0764a"/></g>
<g transform="translate(140 250)">
  <path d="M-40-20h40v40h-40z" fill="{MUTED}" class="o"/>
  <path d="M0-14h30v28H0z" fill="{MUTED}" class="o"/>
  <circle cx="52" cy="0" r="18" fill="none" stroke="{MUTED}" stroke-width="8"/></g>
<g transform="translate(330 220)">
  <path d="M-10 0h20v40h-20z" fill="{BRN}" class="o"/>
  <path d="M-34-30h68v30h-68z" fill="#8a97a3" class="o"/></g>
<g transform="translate(440 232) rotate(-14)">
  <path d="M-70-8h140l16 8-16 8h-140z" fill="#c3cbd1" class="o"/>
  <path d="M-100-12h30v24h-30z" fill="{BRN}" class="o"/></g>''')

add('wrapper', 'お菓子を包んでいた紙が、破られて残る',
    '包み紙、包装＝wrapper。', f'''
{table(352)}
<g transform="translate(240 280) rotate(-10)">
  <path d="M-70-40h140v80h-140z" class="coralp o"/>
  <path d="M-70-10q70 20 140 0" fill="none" stroke="{CRL}" stroke-width="4"/>
  <path d="M-70-30l-40-16v60l40-8zM70-30l40-16v60l-40-8z" class="coral o"/></g>
<g transform="translate(420 300) rotate(20)">
  <path d="M-50-30h100l-10 60h-80z" class="coralp o"/>
  <path d="M-50-30l-30-12v40l30-6z" class="coral o"/></g>
<g transform="translate(380 240)"><rect x="-30" y="-20" width="60" height="40" rx="6" fill="#7a4a28" stroke="{INK}" stroke-width="2.5"/></g>''')

add('wrestling', '二人が組み合い、マットの上で力を競う',
    'レスリング、格闘＝wrestling。', f'''
<g transform="translate(300 340)">
  <path d="M-260-30h520v60h-520z" fill="#4e86c6" class="o"/>
  <ellipse cy="-30" rx="200" ry="40" fill="#6a9fd4" class="o"/>
  <ellipse cy="-30" rx="130" ry="26" fill="none" stroke="#fffefd" stroke-width="5"/></g>
<g transform="translate(250 300)">
  <path d="M-40-80q40-20 80 0 16 60 0 80h-80q-16-20 0-80z" class="coral o"/>
  <circle cx="0" cy="-116" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-34-124q4-34 34-34 28 0 34 32-18-14-34-6-16-8-34 8z" fill="{HAIR}"/>
  <path d="M40-70q40 0 60 24" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
  <path d="M-26 0l-14 40M26 0l16 40" stroke="{CRLD}" stroke-width="16" fill="none" stroke-linecap="round"/></g>
<g transform="translate(370 300)">
  <path d="M-40-80q40-20 80 0 16 60 0 80h-80q-16-20 0-80z" class="teal o"/>
  <circle cx="0" cy="-116" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-34-124q4-34 34-34 28 0 34 32-18-14-34-6-16-8-34 8z" fill="{HAIR}"/>
  <path d="M-40-70q-40 0-60 24" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
  <path d="M-26 0l-16 40M26 0l14 40" stroke="{TEAD}" stroke-width="16" fill="none" stroke-linecap="round"/></g>''')

add('yarn', '毛糸の玉から糸が伸び、編みかけの布につながる',
    '毛糸、編み糸＝yarn。', f'''
{table(352)}
<g transform="translate(200 280)">
  <circle r="70" class="coral o"/>
  <path d="M-60-24q60 50 120 0M-56 24q56-50 112 0M-40-50q40 80 80 0" fill="none" stroke="{CRLD}" stroke-width="4"/></g>
<path d="M266 250q80-30 120 10" fill="none" stroke="{CRL}" stroke-width="5"/>
<g transform="translate(440 270)">
  <path d="M-70-50h140v110h-140z" class="coralp o"/>
  {''.join(f'<path d="M{-58+ (i%5)*26} {-34+(i//5)*30}q12-14 24 0" fill="none" stroke="{CRL}" stroke-width="4"/>' for i in range(15))}</g>''')

add('zinc', '亜鉛のめっきをした波形の板が、さびを防ぐ',
    '亜鉛＝zinc。', f'''
{table(352)}
<g transform="translate(300 250)">
  {''.join(f'<path d="M{-200+i*50} -80q25 40 0 80t0 80" fill="none" stroke="#b8bcc0" stroke-width="26" stroke-linecap="round"/>' for i in range(9))}
  <path d="M-215-96h430v14h-430z" fill="#9ba1a6" class="o"/></g>
{''.join(spark(150 + i * 300, 140, 0.6, 'gold') for i in range(2))}
{''.join(f'<path d="M{{}} 340q10-14 0-26" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}''')

finish(__file__)
