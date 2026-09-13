# -*- coding: utf-8 -*-
"""第184回。plus32 の50語。cheetah の描き直しも含む。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('cheetah', '細身のチーターが四肢を伸ばして草原を走り、体には黒い点が散る',
    'チーター＝cheetah。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<g transform="translate(300 250)">
  <path d="M-120 20q-24-54 24-70 80-26 150-6 46 14 44 44-4 30-50 34-92 8-168-2z" fill="#e0b862" class="o"/>
  <path d="M98-46q26-30 58-18 28 12 14 42-12 24-44 22z" fill="#e0b862" class="o"/>
  <path d="M148-24l36 6-34 16z" fill="#c89a44" class="o"/>
  <path d="M112-62l-4-30 26 18zM144-66l14-28 8 26z" fill="#e0b862" class="o"/>
  <circle cx="140" cy="-32" r="5" class="ink"/>
  <path d="M136-12l-10 22" stroke="{INK}" stroke-width="3" fill="none"/>
  <path d="M-120 24q-52-10-72-44 42-2 70 26z" fill="#e0b862" class="o"/>
  <path d="M-96 34q-14 56-50 70M-30 40q-16 52-4 72M40 40q18 48 46 62M92 30q28 40 66 44" fill="none" stroke="#e0b862" stroke-width="17" stroke-linecap="round"/>
  {''.join(f'<circle cx="{-90+(i%8)*32}" cy="{-24+(i//8)*26}" r="5" fill="#5b4030"/>' for i in range(16))}</g>
{''.join(f'<path d="M40 {200+i*36}h70" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}''')

add('cork', 'びんの口から抜かれた円柱形のコルク栓',
    'コルク、コルク栓＝cork。', f'''
{table(352)}
<g transform="translate(220 270)">
  <path d="M-28-100h56v40l26 30q10 14 10 30v60a16 16 0 0 1-16 16h-96a16 16 0 0 1-16-16v-60q0-16 10-30l26-30z" fill="#3a6b3a" class="o"/>
  <path d="M-40 10h80v50h-80z" fill="#fffefd" class="o"/></g>
<g transform="translate(420 230) rotate(16)">
  <path d="M-30-56h60v112h-60z" fill="#c8a05f" class="o"/>
  <ellipse cy="-56" rx="30" ry="10" fill="#e0c48c" class="o"/>
  {''.join(f'<circle cx="{-14+(i%3)*14}" cy="{-24+(i//3)*30}" r="4" fill="#a87f42"/>' for i in range(6))}</g>
{arc(320, 200, 380, 190, 40, MUTED, True, 4)}''', arrow=True)

add('corkscrew', 'らせん状の金具のついた栓抜きが、コルクにねじこまれる',
    'コルク抜き、栓抜き＝corkscrew。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-70-130h140v26h-140z" fill="{BRN}" class="o"/>
  <path d="M-10-104h20v40h-20z" fill="#9aa7b1" class="o"/>
  <path d="M0-64q-26 12 0 24t0 24-26 24 0 24t0 24" fill="none" stroke="#9aa7b1" stroke-width="9" stroke-linecap="round"/>
  <path d="M-70-118q-40 30-30 70M70-118q40 30 30 70" fill="none" stroke="#9aa7b1" stroke-width="10" stroke-linecap="round"/></g>
<g transform="translate(300 330)">
  <path d="M-30-24h60v48h-60z" fill="#c8a05f" class="o"/></g>''')

add('courtyard', '建物に四方を囲まれた中庭に、木と長いすが置かれている',
    '中庭＝courtyard。', f'''
<g transform="translate(300 200)">
  <path d="M-280-180h560v360h-560z" fill="#e4dccb" class="o"/>
  <path d="M-170-100h340v280h-340z" class="greenp o"/>
  {''.join(f'<rect x="{-250+ (i%2)*440}" y="{-140+(i//2)*80}" width="50" height="50" class="tealp o"/>' for i in range(6))}
  {''.join(f'<rect x="{-140+i*90}" y="-160" width="50" height="50" class="tealp o"/>' for i in range(4))}</g>
{tree(300, 300, 1.0)}
<g transform="translate(160 320)">
  <path d="M-50-12h100v14h-100z" fill="#c9a464" class="o"/>
  <path d="M-40 2v20M40 2v20" stroke="{BRN}" stroke-width="7" fill="none"/></g>''')

add('cradle', '木のゆりかごが、弓形の脚の上で静かに揺れる',
    'ゆりかご＝cradle。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-130-50h260v70q0 40-40 40h-180q-40 0-40-40z" fill="#c9a464" class="o"/>
  <path d="M-130-50h260" fill="none" stroke="{BRN}" stroke-width="5"/>
  {''.join(f'<path d="M{-100+i*40} -50v-50" stroke="{BRN}" stroke-width="8" fill="none" stroke-linecap="round"/>' for i in range(6))}
  <path d="M-104-100h208" stroke="{BRN}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M-150 60q150 60 300 0" fill="none" stroke="{BRN}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-70 0q70-20 140 0v20h-140z" fill="#fffefd" class="o"/></g>
<g transform="translate(300 100)"><path d="M-70 0q70-30 140 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/></g>''', arrow=True)

add('crane', '高い鉄のクレーンが、鉤で鉄骨をつり上げている',
    'クレーン、起重機＝crane。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(200 340)">
  <path d="M-30 0v-260h60V0z" fill="{GLDP}" class="o"/>
  {''.join(f'<path d="M-30 {-30-i*46}l60-46" stroke="{GLDD}" stroke-width="4" fill="none"/>' for i in range(5))}
  <path d="M-70-280h330v30h-330z" class="gold o"/>
  {''.join(f'<path d="M{-50+i*50} -280l50 30" stroke="{GLDD}" stroke-width="4" fill="none"/>' for i in range(6))}
  <path d="M220-250v90" stroke="{INK}" stroke-width="5" fill="none"/>
  <path d="M204-160h32v20h-32z" fill="{MUTED}" class="o"/></g>
<g transform="translate(420 220)">
  <path d="M-90-10h180v20h-180z" fill="#8a97a3" class="o"/>
  <path d="M-8 10v20" stroke="{INK}" stroke-width="0"/></g>''')

add('crate', '板の隙間のある木箱に、果物が詰められている',
    '木箱、輸送用の箱＝crate。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-140-60h280v110h-280z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M-140 {-40+i*36}h280" stroke="#fffaf1" stroke-width="10" fill="none"/>' for i in range(3))}
  <path d="M-140-60h280v110h-280z" fill="none" class="o"/>
  <path d="M-140-60v-10h280v10" fill="none" stroke="{BRN}" stroke-width="6"/></g>
{''.join(f'<circle cx="{{}}" cy="196" r="24" class="{{}} o"/>'.format(230 + i * 48, c) for i, c in enumerate(['coral', 'gold', 'coral']))}''')

add('crater', '火山の頂上にすり鉢状の穴があき、煙が立ちのぼる',
    '噴火口、クレーター＝crater。', f'''
<path d="M0 360h600v40H0z" class="ground"/>
<path d="M40 360L230 130h140l190 230z" fill="#8a7a6a" class="o"/>
<path d="M230 130h140l-30 40h-80z" fill="#5b4636" class="o"/>
<path d="M244 132q56 24 112 0" fill="none" stroke="#4a3a2a" stroke-width="5"/>
{''.join(f'<path d="M{{}} {{}}q20-26 0-50" fill="none" stroke="{MUTED}" stroke-width="5"/>'.format(270 + i * 34, 110 - i * 20) for i in range(3))}
{''.join(f'<path d="M{{}} 220l-40 60" fill="none" stroke="#8a7a6a" stroke-width="4"/>'.format(220 + i * 160) for i in range(2))}''')

add('crayon', '紙の上に色の棒で線を描き、箱にほかの色が並ぶ',
    'クレヨン＝crayon。', f'''
{table(352)}
<g transform="translate(260 270)">
  <path d="M-150-70h300v130h-300z" class="paper"/>
  <path d="M-110 30q40-90 90-40t100-20" fill="none" stroke="{CRL}" stroke-width="12" stroke-linecap="round"/></g>
<g transform="translate(180 140) rotate(40)">
  <path d="M-16-70h32v110h-32z" class="coral o"/>
  <path d="M-16 40h32l-16 30z" class="corald o"/>
  <path d="M-16-40h32v14h-32z" fill="#fffefd"/></g>
<g transform="translate(480 280)">
  <path d="M-60-40h120v80h-120z" fill="#f0e6d2" class="o"/>
  {''.join(f'<rect x="{-46+i*22}" y="-56" width="14" height="60" rx="3" fill="{c}" stroke="{INK}" stroke-width="2"/>' for i, c in enumerate(['#e86452', '#d99a2b', '#4e986a', '#4e86c6', '#816eb2']))}</g>''')

add('crease', 'ズボンの前に一本だけ、はっきりした縦の折り目が入る',
    '折り目、しわ＝crease。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-100-120h200v240h-200z" class="bluep o"/>
  <path d="M-100-120h200v24h-200z" class="blue o"/>
  <path d="M0-96v216" fill="none" stroke="{BLUD}" stroke-width="6"/>
  <path d="M-4-96v216" fill="none" stroke="#ffffff" stroke-width="3"/></g>
{ring(300, 250, 0, True)}
<g transform="translate(470 180)"><path d="M-30 0h60" fill="none" stroke="{CRL}" stroke-width="0"/></g>
{''.join(f'<path d="M{{}} 200h-60" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(470) for _ in range(1))}''', arrow=True)

add('crockery', '皿とカップとボウルが、棚にきちんと積まれている',
    '食器類＝crockery。', f'''
{table(352)}
<g transform="translate(180 290)">
  {''.join(f'<ellipse cy="{-i*16}" rx="{80-i*6}" ry="{20-i}" fill="#fffefd" class="o"/>' for i in range(5))}</g>
<g transform="translate(370 280)">
  <path d="M-46-30h92v40a30 30 0 0 1-30 30h-32a30 30 0 0 1-30-30z" fill="#fffefd" class="o"/>
  <path d="M46-18q30 0 30 22t-30 22" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-38-22h76v28a24 24 0 0 1-24 24h-28a24 24 0 0 1-24-24z" class="tealp"/></g>
<g transform="translate(490 290)">
  <path d="M-56-20q0 54 56 54t56-54z" fill="#fffefd" class="o"/>
  <ellipse cy="-20" rx="56" ry="16" fill="#fffefd" class="o"/></g>''')

add('crossing', '道路の上に白い横線が並び、歩行者用の信号が立つ',
    '横断歩道、踏切＝crossing。', f'''
<path d="M0 200h600v200H0z" fill="#9aa7b1"/>
{''.join(f'<rect x="{{}}" y="210" width="46" height="180" fill="#fffefd"/>'.format(160 + i * 70) for i in range(4))}
<path d="M0 190h600v14H0z" fill="#fffefd"/>
<g transform="translate(90 320)">
  <path d="M-8 0v-180h16V0z" fill="{MUTED}"/>
  <path d="M-30-260h60v80h-60z" fill="#2f3a4d" class="o"/>
  <circle cy="-220" r="18" class="green"/></g>
{person(330, 380, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'smile')}''')

add('crowbar', '先の割れた鉄の棒を、ふたの隙間に差しこんでこじ開ける',
    'バール、かなてこ＝crowbar。', f'''
{table(352)}
<g transform="translate(300 290)">
  <path d="M-140-40h280v70h-280z" fill="#c9a464" class="o"/>
  <path d="M-140-40h280v-14h-280z" fill="#a0764a" class="o" transform="rotate(-8 -140 -40)"/></g>
<g transform="translate(240 190) rotate(38)">
  <path d="M-12-120h24v230h-24z" fill="#6b7680" class="o"/>
  <path d="M-12 110q-14 24 0 34 10-10 24-6l-8-28z" fill="#6b7680" class="o"/>
  <path d="M-4 128h14v12h-14z" fill="#fffaf1"/></g>
{arc(200, 130, 150, 200, 50, MUTED, True, 4)}''', arrow=True)

add('cube', '六つの面がすべて正方形の、立方体のかたまり',
    '立方体、さいの目＝cube。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-80-40h160v160h-160z" class="teal o"/>
  <path d="M-80-40l50-50h160l-50 50z" class="tealp o"/>
  <path d="M80-40l50-50v160l-50 50z" class="teald o"/></g>
{''.join(f'<path d="M{{}} {{}}h{{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"/>'.format(a, b, c) for a, b, c in [(220, 350, 160)])}
<path d="M220 356h160" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

add('cutlery', 'ナイフとフォークとスプーンが、そろって並べられている',
    '食卓用の刃物類＝cutlery。', f'''
{table(352)}
<g transform="translate(170 250)">
  <path d="M-10-100h20v200h-20z" fill="#c3cbd1" class="o"/>
  <path d="M-10-100q-20 60 0 80h20q20-20 0-80z" fill="#dfe6ea" class="o"/></g>
<g transform="translate(300 250)">
  <path d="M-8-100h16v200h-16z" fill="#c3cbd1" class="o"/>
  {''.join(f'<path d="M{-16+i*16} -100v46" stroke="#c3cbd1" stroke-width="7" fill="none" stroke-linecap="round"/>' for i in range(3))}
  <path d="M-18-56h36v22h-36z" fill="#c3cbd1" class="o"/></g>
<g transform="translate(430 250)">
  <path d="M-8-100h16v200h-16z" fill="#c3cbd1" class="o"/>
  <ellipse cy="-74" rx="26" ry="36" fill="#dfe6ea" class="o"/></g>''')

add('cycling', 'ヘルメットをかぶった人が、自転車で坂道を走る',
    'サイクリング＝cycling。', f'''
<path d="M0 340q140-40 300-20t300 20v60H0z" class="greenp o"/>
<g transform="translate(300 290)">
  <circle cx="-90" cy="46" r="50" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="90" cy="46" r="50" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-90 46L-10-20 40 46 -10-20 66-28 90 46" fill="none" stroke="{TEA}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M66-28l-10-26M30-56h40" stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round"/>
  <circle cx="0" cy="46" r="12" fill="none" stroke="{INK}" stroke-width="6"/></g>
{person(290, 290, 0.95, 1, 'coral', 'blue', 'reach', 'cap', 'smile')}
{''.join(f'<path d="M{{}} {{}}h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>'.format(50, 170 + i * 34) for i in range(2))}''')

add('daybreak', '地平線から日が顔を出し、空が明るくなり始める',
    '夜明け＝daybreak。', f'''
<path d="M0 0h600v260H0z" fill="#4a5570"/>
<path d="M0 140h600v120H0z" fill="#8a7d8f"/>
<path d="M0 200h600v60H0z" fill="#e8a86a"/>
<path d="M0 260h600v140H0z" fill="#3f4a5c"/>
<g transform="translate(300 260)"><path d="M-80 0a80 80 0 0 1 160 0z" class="goldp o"/>
  {''.join(f'<path d="M0-92v-24" transform="rotate({a})" stroke="{GLD}" stroke-width="6" stroke-linecap="round" fill="none"/>' for a in (-50, -25, 0, 25, 50))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="2.5" fill="#fff6d8"/>'.format(50 + (i * 83) % 500, 30 + (i * 41) % 80) for i in range(7))}
<g opacity="0.9"><path d="M60 260q40-60 80 0zM470 260q50-70 100 0z" fill="#2f3a4d"/></g>''')

add('deckchair', '縞の布を張った折りたたみいすが、浜辺に広げてある',
    'デッキチェア＝deckchair。', f'''
<path d="M0 300h600v100H0z" fill="#f0e0b8"/>
{sun(500, 90, 40)}
<g transform="translate(280 300)">
  <path d="M-130 0L-30-130" stroke="{BRN}" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M110 0L-30-130" stroke="{BRN}" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M-70 0L60-60" stroke="{BRN}" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M-30-130L60-60l-110 50-70-40z" class="coral o"/>
  {''.join(f'<path d="M{-24+i*24} -124l60 54" stroke="#fffefd" stroke-width="9" fill="none"/>' for i in range(4))}</g>''')

add('detergent', '洗剤のボトルからキャップ一杯分を、洗濯機に入れる',
    '洗剤＝detergent。', f'''
{table(352)}
<g transform="translate(400 270)">
  <path d="M-110-90h220v170h-220z" fill="#dfe6ea" class="o"/>
  <circle cy="0" r="60" fill="#fffefd" class="o"/>
  <circle cy="0" r="42" class="bluep o"/>
  {''.join(f'<circle cx="{-70+i*46}" cy="-72" r="9" fill="#9aa7b1"/>' for i in range(2))}</g>
<g transform="translate(180 250) rotate(24)">
  <path d="M-44-70h88v130a22 22 0 0 1-22 22h-44a22 22 0 0 1-22-22z" class="tealp o"/>
  <path d="M-22-92h44v22h-44z" class="teal o"/>
  <path d="M-36-30h72v50h-72z" fill="#fffefd" class="o"/></g>
{''.join(drop(270 + i * 14, 210 + i * 24, 1.0, 'teal') for i in range(2))}''')

add('diaper', '赤ちゃんが布のおむつをつけ、横に替えの一枚が畳んである',
    'おむつ＝diaper。', f'''
{table(352)}
<g transform="translate(240 250)">
  <circle cy="-50" r="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40-14q40-20 80 0 16 40 0 60h-80q-16-20 0-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-44 22h88q10 44-14 56h-60q-24-12-14-56z" fill="#fffefd" class="o"/>
  <path d="M-44 22h88" fill="none" stroke="{BLU}" stroke-width="4"/>
  <circle cx="-14" cy="-56" r="4" class="ink"/><circle cx="14" cy="-56" r="4" class="ink"/>
  <path d="M-10-38q10 8 20 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-44 40q-30 8-34 30M44 40q30 8 34 30" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/></g>
<g transform="translate(460 300)">
  <path d="M-60-30h120v60h-120z" fill="#fffefd" class="o"/>
  <path d="M-60 0h120" fill="none" stroke="{BLU}" stroke-width="4"/></g>''')

add('dictation', '聞こえた文を、そのままノートに書き取っていく',
    '書き取り、ディクテーション＝dictation。', f'''
{table(352)}
<g transform="translate(150 200)">
  <path d="M-70-50h140v90h-40l-18 26-12-26h-70z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="-48" y="{-28+i*24}" width="{96-(i%2)*30}" height="10" rx="5" fill="{MUTED}"/>' for i in range(2))}</g>
{arc(240, 190, 330, 220, 50, MUTED, True, 4)}
<g transform="translate(400 270)">
  <path d="M-110-70h220v140h-220z" class="paper"/>
  {''.join(f'<rect x="-86" y="{-44+i*26}" width="{172-(i%3)*44}" height="10" rx="5" fill="{INK}"/>' for i in range(4))}</g>
<g transform="translate(520 150) rotate(34)">
  <path d="M-9-80h18v110l-9 22-9-22z" class="teal o"/></g>''', arrow=True)

add('dinner', '夜の食卓に主菜と付け合わせが並び、ろうそくがともる',
    '夕食、その日の主な食事＝dinner。', f'''
{table(300)}
<g transform="translate(280 288)">
  <ellipse rx="110" ry="30" fill="#fffefd" class="o"/>
  <path d="M-50-24q50-22 100 0 6 30-50 30t-50-30z" fill="#b5744a" class="o"/>
  {''.join(f'<ellipse cx="{-70+i*24}" cy="-6" rx="16" ry="9" class="green o"/>' for i in range(2))}</g>
<g transform="translate(470 280)">
  <path d="M-16 0q-4-50 0-60h32q4 10 0 60z" fill="#f0e6d2" class="o"/>
  {flame(0, -66, 0.22)}</g>
<g transform="translate(120 290)">
  <path d="M-8-60h16v80h-16z" fill="#c3cbd1" class="o"/></g>
<g transform="translate(150 290)">
  <path d="M-6-60h12v80h-12z" fill="#c3cbd1" class="o"/>
  {''.join(f'<path d="M{-10+i*10} -60v26" stroke="#c3cbd1" stroke-width="5" fill="none"/>' for i in range(3))}</g>''')

add('dish', '大きな皿に一品の料理が盛りつけられている',
    '大皿、料理の一品＝dish。', f'''
{table(352)}
<g transform="translate(300 280)">
  <ellipse rx="160" ry="46" fill="#fffefd" class="o"/>
  <ellipse rx="120" ry="32" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-60-16q60-30 120 0 8 34-60 34t-60-34z" fill="#b5744a" class="o"/>
  {''.join(f'<ellipse cx="{-80+i*30}" cy="4" rx="15" ry="9" class="green o"/>' for i in range(2))}
  <circle cx="76" cy="2" r="12" class="coral o"/></g>''')

add('ditch', '道路のわきに掘られた細長い溝に、水が流れている',
    '溝、どぶ＝ditch。', f'''
<path d="M0 200h600v200H0z" class="greenp"/>
<path d="M0 190h600v40H0z" fill="#9aa7b1"/>
<g transform="translate(300 300)">
  <path d="M-300-40q40 60 0 100h600q-40-40 0-100z" fill="#5b4636" class="o"/>
  <path d="M-300 40q160 20 300 0t300 0v20h-600z" class="bluep"/></g>
{''.join(f'<path d="M{{}} 344q22-10 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 96) for i in range(6))}
{''.join(flower(80 + i * 180, 250, 0.45, 'gold') for i in range(3))}''')

add('doctor', '白衣を着た医師が、聴診器を首から下げて立つ',
    '医師＝doctor。', f'''
<g transform="translate(300 330)">
  <path d="M-80 0v-160q80-34 160 0V0z" fill="#fffefd" class="o"/>
  <path d="M-26-160q26 28 52 0l-14 70h-24z" class="tealp o"/>
  <path d="M-80-160l-30 80M80-160l34 76" fill="none" stroke="#fffefd" stroke-width="24" stroke-linecap="round"/>
  <circle cx="0" cy="-206" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-38-214q4-40 38-40 32 0 38 38-20-18-38-8-20-10-38 10z" fill="{HAIR}"/>
  <circle cx="-12" cy="-206" r="3.4" class="ink"/><circle cx="12" cy="-206" r="3.4" class="ink"/>
  <path d="M-11-188q11 9 22 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-40-160q-24 70 20 96M40-160q24 70-20 96" fill="none" stroke="{MUTED}" stroke-width="7"/>
  <circle cx="0" cy="-56" r="18" fill="none" stroke="{MUTED}" stroke-width="7"/>
  <path d="M-58-92h30v24h-30z" class="coralp o"/></g>''')

add('doorbell', '玄関のわきの押しボタンを指で押すと、音が鳴る',
    '呼び鈴、ドアベル＝doorbell。', f'''
<g transform="translate(250 380)">
  <path d="M-120-320h240v320h-240z" fill="#e8ddc9" class="o"/>
  <path d="M-96-296h192v276h-192z" class="teal o"/>
  <circle cx="66" cy="-160" r="10" class="goldp o"/></g>
<g transform="translate(420 200)">
  <path d="M-30-40h60v80h-60z" fill="#e8ddc9" class="o"/>
  <circle r="20" class="coral o"/>
  <circle r="10" class="corald"/></g>
{hand(500, 240, -1)}
{''.join(f'<path d="M{{}} {{}}q16-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(390 + i * -20, 160 + i * 0) for i in range(2))}''')

add('doormat', '玄関の前に敷かれた厚い毛の敷物で、靴の底をぬぐう',
    '玄関マット＝doormat。', f'''
<g transform="translate(300 380)">
  <path d="M-120-320h240v300h-240z" fill="#e8ddc9" class="o"/>
  <path d="M-96-296h192v276h-192z" class="teal o"/>
  <circle cx="66" cy="-160" r="10" class="goldp o"/></g>
<g transform="translate(300 350) rotate(-2)">
  <path d="M-130-32h260v64h-260z" fill="#9a7a4a" class="o"/>
  <path d="M-110-18h220v36h-220z" fill="none" stroke="#7a5c34" stroke-width="4"/>
  {''.join(f'<path d="M{-120+i*24} -32v64" stroke="#7a5c34" stroke-width="2" fill="none"/>' for i in range(11))}</g>
<g transform="translate(300 300)"><path d="M-40 20q0-40 34-40h18l30 24v16z" fill="{INK}"/></g>''')

add('dragonfly', '透明な四枚の羽と細長い体をもつトンボが、水面の上を飛ぶ',
    'トンボ＝dragonfly。', f'''
<path d="M0 300h600v100H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 320q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 190)">
  <path d="M-20-8h180v16h-180z" fill="{TEA}" class="o"/>
  {''.join(f'<path d="M{30+i*30} -8v16" stroke="{TEAD}" stroke-width="3" fill="none"/>' for i in range(5))}
  <circle cx="-40" cy="0" r="34" class="teald o"/>
  <circle cx="-56" cy="-12" r="9" fill="#fffefd" class="o"/><circle cx="-56" cy="12" r="9" fill="#fffefd" class="o"/>
  <path d="M-6-10q60-70 120-40-50 10-100 44zM-6 10q60 70 120 40-50-10-100-44z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="2.5"/>
  <path d="M6-10q46-60 96-36-44 8-80 40zM6 10q46 60 96 36-44-8-80-40z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="2.5"/></g>
{''.join(flower(80 + i * 440, 320, 0.5, 'gold') for i in range(2))}''')

add('drainpipe', '屋根の雨どいから壁を伝って、縦の管が地面へ下りる',
    '排水管、雨どいの縦管＝drainpipe。', f'''
<g transform="translate(300 200)">
  <path d="M-240-160h480v360h-480z" fill="#e4dccb" class="o"/>
  <path d="M-260-160h520l-30-40h-460z" class="corald o"/></g>
<g transform="translate(430 200)">
  <path d="M-140-136h280v30h-280z" fill="#9aa7b1" class="o"/>
  <path d="M100-106h40v290h-40z" fill="#9aa7b1" class="o"/>
  <path d="M100 184h40l30 30h-40z" fill="#9aa7b1" class="o"/></g>
{''.join(drop(610 - 30 + i * 0, 360 + i * 0, 1.0, 'blue') for i in range(1))}
{''.join(f'<path d="M{{}} {{}}l-8 20" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>'.format(100 + i * 44, 60 + (i % 3) * 30) for i in range(5))}''')

add('dressing', 'サラダの上から、とろりとしたドレッシングがかけられる',
    'ドレッシング／(傷の)包帯＝dressing。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-110-30q0 60 110 60t110-60z" fill="#fffefd" class="o"/>
  <ellipse cy="-30" rx="110" ry="30" fill="#fffefd" class="o"/>
  {''.join(f'<ellipse cx="{-60+i*40}" cy="{-34+(i%2)*10}" rx="30" ry="14" class="green o"/>' for i in range(4))}
  <circle cx="40" cy="-30" r="14" class="coral o"/></g>
<g transform="translate(190 130) rotate(40)">
  <path d="M-30-50h60v90a22 22 0 0 1-22 22h-16a22 22 0 0 1-22-22z" class="goldp o"/>
  <path d="M-14-70h28v20h-28z" class="gold o"/></g>
<path d="M258 200q10 40 0 60" fill="none" stroke="{GLD}" stroke-width="12" stroke-linecap="round"/>''')

add('duckling', '毛のふさふさした小さなアヒルの子が、水の上に浮かぶ',
    'アヒルの子、カモの子＝duckling。', f'''
<path d="M0 290h600v110H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 310q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 280)">
  <ellipse rx="80" ry="52" class="gold o"/>
  <circle cx="60" cy="-52" r="38" class="gold o"/>
  <path d="M92-56l34 10-34 12z" class="corald o"/>
  <circle cx="72" cy="-62" r="5" class="ink"/>
  <path d="M-70-10q-26 10-26 34 24-4 38-22z" class="goldd o"/>
  {''.join(f'<path d="M{-40+i*40} -34q14-20 28 0" fill="none" stroke="{GLDD}" stroke-width="3"/>' for i in range(3))}</g>
{''.join(f'<ellipse cx="{{}}" cy="330" rx="34" ry="9" fill="none" stroke="{BLU}" stroke-width="3"/>'.format(300 + i * 0) for i in range(1))}''')

add('duster', '布のはたきで棚の上をふき、ほこりが舞い上がる',
    'ぞうきん、はたき＝duster。', f'''
{table(300)}
<g transform="translate(300 290)">
  <path d="M-200-10h400v20h-400z" fill="#c9a464" class="o"/></g>
<g transform="translate(280 250) rotate(-14)">
  <path d="M-60-30h120q14 30 0 60h-120q-14-30 0-60z" class="goldp o"/>
  <path d="M-40-30v60M0-30v60M40-30v60" fill="none" stroke="{GLDD}" stroke-width="3"/></g>
{hand(200, 200, 1)}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="{MUTED}" opacity="0.6"/>'.format(390 + (i * 37) % 120, 200 + (i * 23) % 60, 4 + i % 3) for i in range(8))}
{''.join(f'<path d="M{{}} {{}}h60" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(340, 200 + i * 30) for i in range(2))}''', arrow=True)

add('earthworm', '土の中を、節のある細長いミミズが進んでいる',
    'ミミズ＝earthworm。', f'''
<path d="M0 180h600v220H0z" fill="#5b4636"/>
<path d="M0 180h600v20H0z" class="greenp"/>
<g transform="translate(300 290)">
  <path d="M-200 40q40-70 80-20t80-40 80 20 80-40" fill="none" stroke="#c47a7a" stroke-width="34" stroke-linecap="round"/>
  {''.join(f'<path d="M{-170+i*46} {14-((i%3)-1)*20}l10 26" stroke="#a85c5c" stroke-width="3" fill="none"/>' for i in range(9))}
  <circle cx="196" cy="-38" r="4" class="ink"/></g>
{''.join(f'<path d="M{{}} 220q20 14 40 0" fill="none" stroke="#3f3126" stroke-width="4"/>'.format(60 + i * 140) for i in range(4))}''')

add('eggshell', '割れた卵の殻が二つに分かれ、中身が下の器へ落ちる',
    '卵の殻＝eggshell。', f'''
{table(352)}
<g transform="translate(300 180)">
  <path d="M-70-20q-20-50 20-66 34-14 56 10-30 24-76 56z" fill="#fffefd" class="o"/>
  <path d="M-70-20q40 26 90-4-24-30-50-44z" fill="#fffefd" class="o"/></g>
<g transform="translate(300 300)">
  <path d="M-100-30q0 60 100 60t100-60z" fill="#fffefd" class="o"/>
  <ellipse cy="-30" rx="100" ry="28" fill="#fffefd" class="o"/>
  <ellipse cy="-30" rx="60" ry="18" fill="#fdf3c8"/>
  <circle cy="-32" r="20" class="gold o"/></g>
{''.join(f'<path d="M300 {{}}v14" stroke="#fdf3c8" stroke-width="14" fill="none"/>'.format(210 + i * 20) for i in range(3))}''')

add('embroidery', '布の上に、糸で細かい花の模様が縫い出されている',
    '刺しゅう＝embroidery。', f'''
{table(352)}
<g transform="translate(300 250)">
  <circle r="130" fill="none" stroke="{BRN}" stroke-width="16"/>
  <circle r="118" fill="#fffefd" class="o"/>
  {''.join(flower(-50 + (i % 3) * 50, -40 + (i // 3) * 60, 0.5, c) for i, c in enumerate(['coral', 'gold', 'violet', 'green', 'coral', 'gold']))}
  <path d="M-90 70q90-40 180 0" fill="none" stroke="{GRN}" stroke-width="5" stroke-dasharray="10 8"/></g>
<g transform="translate(470 140) rotate(30)">
  <path d="M-3-70h6v120h-6z" fill="#c3cbd1" class="o"/>
  <path d="M-3-70q10 60 0 90" fill="none" stroke="{CRL}" stroke-width="4"/></g>''')

add('emerald', '深い緑色の宝石が、指輪の台にはめこまれている',
    'エメラルド＝emerald。', f'''
{table(352)}
<g transform="translate(300 270)">
  <ellipse cy="40" rx="90" ry="26" fill="none" stroke="{GLD}" stroke-width="14"/>
  <path d="M-56-40h112l-20-40h-72z" class="green o"/>
  <path d="M-56-40h112l-30 60h-52z" class="greend o"/>
  <path d="M-36-40l14-40M36-40l-14-40M-22 20l10-60M22 20l-10-60" fill="none" stroke="#e6f3e8" stroke-width="3"/></g>
{''.join(spark(160 + i * 280, 140, 0.8, 'gold') for i in range(2))}''')

add('eraser', '四角い消しゴムで鉛筆の線を消し、消しかすが出る',
    '消しゴム＝eraser。', f'''
{table(352)}
<g transform="translate(280 280)">
  <path d="M-170-60h340v90h-340z" class="paper"/>
  <path d="M-140 0h120" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <g opacity="0.25"><path d="M-10 0h110" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g></g>
<g transform="translate(320 250) rotate(-12)">
  <path d="M-44-30h88v60h-88z" class="coralp o"/>
  <path d="M-44 0h88" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="{CRLP}" stroke="{CRL}" stroke-width="2"/>'.format(400 + (i * 29) % 90, 296 + (i * 17) % 20, 5 + i % 3) for i in range(6))}''')

add('escalator', '斜めに上がっていく階段の上で、人が手すりにつかまって立つ',
    'エスカレーター＝escalator。', f'''
<g transform="translate(300 250)">
  {''.join(f'<path d="M{-220+i*44} {110-i*34}h60v34h-60z" fill="#c3cbd1" stroke="{INK}" stroke-width="2.5"/>' for i in range(9))}
  <path d="M-240 130L200-80" fill="none" stroke="{MUTED}" stroke-width="14" stroke-linecap="round"/>
  <path d="M-240 170L200-40" fill="none" stroke="#9aa7b1" stroke-width="10" stroke-linecap="round"/></g>
{person(360, 240, 0.95, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(210, 330, 0.95, 1, 'coral', 'green', 'stand', 'bob', 'smile')}
{arc(420, 200, 470, 130, 40, MUTED, True, 5)}''', arrow=True)

add('fairground', '夜の広場に観覧車と屋台が並び、電球が光る',
    '移動遊園地の会場＝fairground。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#2f3a4d"/></g>
<g transform="translate(180 230)">
  <circle r="110" fill="none" stroke="{GLD}" stroke-width="7"/>
  {''.join(f'<g transform="rotate({i*45})"><path d="M0 0v-110" stroke="{GLD}" stroke-width="4" fill="none"/><rect x="-13" y="-124" width="26" height="20" rx="4" class="coral o"/></g>' for i in range(8))}
  <circle r="12" class="goldp o"/>
  <path d="M-50 110h100l-50-100z" fill="none" stroke="{GLD}" stroke-width="6"/></g>
<g transform="translate(450 330)">
  <path d="M-90 0v-80h180V0z" fill="#f6efe1" class="o"/>
  <path d="M-104-80h208l-16-36h-176z" class="coral o"/>
  {''.join(f'<circle cx="{-80+i*32}" cy="-124" r="8" class="goldp"/>' for i in range(6))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="4" fill="#fff6d8"/>'.format(60 + (i * 71) % 500, 40 + (i * 37) % 80) for i in range(8))}''')

add('falcon', '翼をすぼめたハヤブサが、空から急降下する',
    'ハヤブサ＝falcon。', f'''
{''.join(cloud(120 + i * 300, 80, 1.0, 'blue') for i in range(2))}
<g transform="translate(310 220) rotate(40)">
  <ellipse rx="30" ry="70" fill="#7a6a54" class="o"/>
  <circle cx="0" cy="-84" r="26" fill="#8a7a64" class="o"/>
  <path d="M18-96q22 4 20 16-14 10-22 0z" class="gold o"/>
  <circle cx="8" cy="-92" r="4" class="ink"/>
  <path d="M-26-40q-50 30-46 90 34-20 50-60zM26-40q50 30 46 90-34-20-50-60z" fill="#6b5b48" class="o"/>
  <path d="M0 70l-10 40M0 70l12 40" stroke="{GLDD}" stroke-width="7" fill="none" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}l40 46" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>'.format(170 + i * 26, 70 + i * 20) for i in range(3))}''')

add('fender', '車の前輪の上をおおう泥よけの部分に、へこみがある',
    '(車の)フェンダー、泥よけ＝fender。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(300 300)">
  <path d="M-170 0v-60l50-70h240l50 70V0z" class="teal o"/>
  <path d="M-100-124h180l34 54h-248z" fill="#dfeaf2" class="o"/>
  <circle cx="-100" cy="6" r="40" class="ink"/>
  <circle cx="110" cy="6" r="40" class="ink"/>
  <path d="M-160-20q10-60 60-60t60 60" fill="none" stroke="{TEAD}" stroke-width="12"/></g>
{ring(230, 270, 74, True)}
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(190 + i * 18, 200 - i * 14) for i in range(2))}''')

add('fiddle', '民俗楽団で、あごに挟んだバイオリンを弓で弾く',
    'バイオリン(くだけた言い方)＝fiddle。', f'''
{person(300, 350, 1.3, 1, 'coral', 'blue', 'reach', 'short', 'smile')}
<g transform="translate(370 210) rotate(-28)">
  <path d="M-40-40q-30 24-16 54 12 26 40 26t40-26q14-30-16-54-10-24-24-24t-24 24z" fill="#a2603a" class="o"/>
  <path d="M-10-100h20v70h-20z" fill="#7a3f22" class="o"/>
  <path d="M-16-112h32v16h-32z" fill="#7a3f22" class="o"/>
  <path d="M-4-92v90M4-92v90" stroke="#f0e6d2" stroke-width="2" fill="none"/></g>
<g transform="translate(410 260) rotate(28)">
  <path d="M-100-4h200v8h-200z" fill="{BRN}" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q14-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(190 + i * 20, 180 - i * 14) for i in range(2))}''')

add('firewood', '割った薪が積み上げられ、斧が切り株に刺さっている',
    'まき、たきぎ＝firewood。', f'''
<path d="M0 320h600v80H0z" class="ground"/>
<g transform="translate(400 320)">
  {''.join(f'<g transform="translate({-90+ (i%5)*46} {-26-(i//5)*46})"><ellipse rx="22" ry="22" fill="#c9a464" stroke="{INK}" stroke-width="2.5"/><path d="M-22 0h44" stroke="#a0764a" stroke-width="3" fill="none"/><path d="M0-22v44" stroke="#a0764a" stroke-width="3" fill="none"/></g>' for i in range(15))}</g>
<g transform="translate(150 320)">
  <path d="M-50 0v-50h100V0z" fill="#a0764a" class="o"/>
  <ellipse cy="-50" rx="50" ry="16" fill="#c9a464" class="o"/></g>
<g transform="translate(150 240) rotate(-30)">
  <path d="M-9-90h18v100h-18z" fill="{BRN}" class="o"/>
  <path d="M-9-96q40-20 44 22-24 10-44-2z" fill="#9aa7b1" class="o"/></g>''')

add('flannel', '起毛したやわらかい格子模様の布が、たたまれている',
    'フランネル＝flannel。', f'''
{table(352)}
<g transform="translate(300 260) rotate(-3)">
  <path d="M-160-80h320v160h-160z" fill="none"/>
  <path d="M-160-80h320v160h-320z" fill="#c96a5a" class="o"/>
  {''.join(f'<path d="M{-130+i*50} -80v160" stroke="#a8493c" stroke-width="14" fill="none"/>' for i in range(6))}
  {''.join(f'<path d="M-160 {-56+i*46}h320" stroke="#a8493c" stroke-width="14" fill="none"/>' for i in range(4))}
  <path d="M-160-80h320v160h-320z" fill="none" class="o"/>
  <path d="M-160 0h320" fill="none" stroke="#7f352c" stroke-width="4"/></g>
{hand(470, 170, -1)}''')

add('flask', '細い口と丸い胴のフラスコに、色のついた液が入っている',
    'フラスコ／水筒＝flask。', f'''
{table(352)}
<g transform="translate(230 260)">
  <path d="M-16-100h32v50l54 96a20 20 0 0 1-18 30h-88a20 20 0 0 1-18-30l54-96z" fill="#fffefd" class="o"/>
  <path d="M-64 40l24-42h80l24 42a20 20 0 0 1-18 36h-92a20 20 0 0 1-18-36z" class="tealp"/>
  <path d="M-18-104h36v10h-36z" class="teal o"/></g>
<g transform="translate(440 260)">
  <path d="M-44-90h88v160a20 20 0 0 1-20 20h-48a20 20 0 0 1-20-20z" fill="#c3cbd1" class="o"/>
  <path d="M-30-112h60v22h-60z" class="coral o"/>
  <path d="M-44-20h88v60h-88z" fill="#9aa7b1"/></g>''')

add('flatmate', '同じアパートに住む二人が、台所で並んで家事をする',
    '同居人、ルームシェアの相手＝flatmate。', f'''
<g transform="translate(300 200)"><path d="M-260-160h520v320h-520z" fill="#f6efe1" class="o"/></g>
{table(300)}
<g transform="translate(300 250)">
  <path d="M-200-40h400v40h-400z" fill="#c9a464" class="o"/></g>
{person(190, 250, 1.05, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
{person(400, 250, 1.05, -1, 'coral', 'green', 'reach', 'bob', 'smile')}
<g transform="translate(300 224)"><ellipse rx="40" ry="12" fill="#fffefd" class="o"/></g>
<g transform="translate(500 130)"><path d="M-50-40h100v80h-100z" fill="#dfeaf2" class="o"/>
  <path d="M0-40v80M-50 0h100" fill="none" stroke="{INK}" stroke-width="4"/></g>''')

add('flea', '犬の毛の間を、跳ねる力の強い小さな虫が移動する',
    'ノミ＝flea。', f'''
<g transform="translate(220 300)">
  <path d="M-140 40q-20-50 20-64 90-30 170-8 46 12 44 40-4 28-48 32-100 8-186 0z" fill="#c8a05f" class="o"/>
  <path d="M96-24q24-26 52-12 24 12 10 36-12 20-40 18z" fill="#c8a05f" class="o"/>
  <circle cx="128" cy="-16" r="4" class="ink"/>
  <path d="M-100 44l-14 40M-30 48l-8 38M40 46l8 40M96 40l18 40" stroke="#c8a05f" stroke-width="15" fill="none" stroke-linecap="round"/></g>
<g transform="translate(400 170) scale(2.8)">
  <ellipse rx="20" ry="14" fill="#6a3f22" class="o"/>
  <circle cx="-18" cy="-4" r="8" fill="#5b3218" class="o"/>
  <path d="M-24-10l-10-8" stroke="{INK}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M8 12l16 18M-2 14l0 18M16 8l20 14" stroke="{INK}" stroke-width="2.5" fill="none" stroke-linecap="round"/></g>
{ring(400, 170, 80, True)}
{arc(400, 240, 300, 270, 50, CRL, True, 4)}''', arrow=True)

add('fleece', '刈り取った羊の毛が、ひとかたまりになって置かれている',
    '羊毛、フリースの上着＝fleece。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-130 50q-40-40-20-80 0-40 44-46 26-40 76-30 50-10 70 34 44 10 40 52 8 40-30 70z" fill="#f4f1ea" class="o"/>
  {''.join(f'<circle cx="{-80+(i%5)*40}" cy="{-20+(i//5)*36}" r="16" fill="none" stroke="#d8d2c4" stroke-width="4"/>' for i in range(10))}</g>
<g transform="translate(120 200)">
  <ellipse rx="46" ry="34" fill="#f4f1ea" class="o"/>
  <circle cx="36" cy="-20" r="20" fill="#4a4238" class="o"/>
  <circle cx="44" cy="-24" r="3" fill="#fffefd"/>
  <path d="M-26 30v18M10 32v18" stroke="#4a4238" stroke-width="7" fill="none"/></g>''')

add('florist', '花屋の店先にバケツの花が並び、店主が束を作っている',
    '花屋＝florist。', f'''
<g transform="translate(330 330)">
  <path d="M-160 0v-140h320V0z" fill="#fffefd" class="o"/>
  <path d="M-176-140h352l-20-44h-312z" class="green o"/></g>
{''.join(f'<g transform="translate({{}} 330)"><path d="M-30-40h60l-8 40h-44z" class="bluep o"/>{{}}</g>'.format(180 + i * 90, ''.join(flower(-12 + j * 14, -60 - j * 8, 0.36, c) for j, c in enumerate(['coral', 'gold', 'violet']))) for i in range(3))}
{person(490, 330, 1.0, -1, 'coral', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(448 250)">
  <path d="M-30-20l30 44 30-44q-30 14-60 0z" fill="#f6efe1" class="o"/>
  {''.join(flower(-14 + i * 14, -34, 0.36, c) for i, c in enumerate(['coral', 'gold']))}</g>''')

add('flowerbed', '庭の土を区切った一角に、花がまとめて植えられている',
    '花壇＝flowerbed。', f'''
<path d="M0 250h600v150H0z" class="greenp"/>
<g transform="translate(300 320)">
  <path d="M-200-50h400v90h-400z" fill="#5b4636" class="o"/>
  <path d="M-210-50h420v-14h-420z" fill="#a0764a" class="o"/></g>
{''.join(flower(150 + (i % 5) * 76, 300 + (i // 5) * 36, 0.6, c) for i, c in enumerate(['coral', 'gold', 'violet', 'coral', 'teal', 'gold', 'violet', 'coral', 'teal', 'gold']))}
{person(70, 300, 0.85, 1, 'teal', 'blue', 'hold', 'cap', 'smile')}''')

add('foal', '長い脚の子馬が、母馬のそばに寄り添って立つ',
    '子馬＝foal。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<g transform="translate(220 280)">
  <ellipse rx="110" ry="60" fill="#8a6a46" class="o"/>
  <path d="M96-36q30-50 60-30 24 16 4 50-14 22-40 22z" fill="#8a6a46" class="o"/>
  <path d="M150-70l-4-30 24 18zM176-74l16-26 6 26z" fill="#8a6a46" class="o"/>
  <circle cx="152" cy="-26" r="5" class="ink"/>
  <path d="M-96 50l-16 60M-30 56l-10 56M40 56l12 56M96 46l22 60" stroke="#8a6a46" stroke-width="17" fill="none" stroke-linecap="round"/>
  <path d="M-110-10q-46 20-56 70 34-10 60-44z" fill="#6a4a2a" class="o"/></g>
<g transform="translate(430 320)">
  <ellipse cy="-60" rx="60" ry="34" fill="#c8a05f" class="o"/>
  <path d="M50-86q20-34 42-20 16 12 2 34-10 16-28 14z" fill="#c8a05f" class="o"/>
  <path d="M84-108l-4-22 18 14zM102-112l12-18 4 18z" fill="#c8a05f" class="o"/>
  <circle cx="84" cy="-84" r="4" class="ink"/>
  <path d="M-46-32l-8 62M-10-28l-4 58M22-28l6 58M50-34l14 60" stroke="#c8a05f" stroke-width="11" fill="none" stroke-linecap="round"/></g>''')

finish(__file__)
