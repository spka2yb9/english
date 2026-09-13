# -*- coding: utf-8 -*-
"""第182回。8,000語化で足した plus30 の50語。月・曜日と、家まわりの具体物。

月は「12マスの年の帯 + 季節の景色」、曜日は「7マスの週の帯 + 語源の印」で描き分ける。
どちらも文字を使わずに位置で何番目かを示す。
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def year_strip(n, y=330, cls='coral'):
    """12マスの帯。n番目(1始まり)を塗る。"""
    g = []
    for i in range(12):
        x = 40 + i * 44
        c = TONES[cls][0] if i == n - 1 else '#fffefd'
        g.append(f'<rect x="{x}" y="{y}" width="38" height="38" rx="5" fill="{c}" stroke="{INK}" stroke-width="2.5"/>')
    return ''.join(g)

def week_strip(n, y=330, cls='coral'):
    """7マスの帯。n番目(1始まり)を塗る。"""
    g = []
    for i in range(7):
        x = 90 + i * 60
        c = TONES[cls][0] if i == n - 1 else '#fffefd'
        g.append(f'<rect x="{x}" y="{y}" width="52" height="44" rx="6" fill="{c}" stroke="{INK}" stroke-width="2.5"/>')
    return ''.join(g)

def snow(n=12, y0=60, h=200):
    return ''.join(f'<circle cx="{40 + (i * 97) % 520}" cy="{y0 + (i * 61) % h}" r="{4 + i % 3}" fill="#ffffff" stroke="{MUTED}" stroke-width="1.5"/>' for i in range(n))

def bare_tree(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-8 0v-70h16V0z" class="goldd"/>'
            f'<path d="M0-60l-40-40M0-60l40-44M0-80l-24-40M0-80l26-38" fill="none" stroke="{BRN}" stroke-width="7" stroke-linecap="round"/></g>')

def blossom_tree(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-9 0v-60h18V0z" class="goldd"/>'
            f'<circle cx="-26" cy="-76" r="30" class="coralp o"/><circle cx="24" cy="-84" r="34" class="coralp o"/>'
            f'<circle cx="0" cy="-108" r="28" class="coralp o"/></g>')

# --- 月 ----------------------------------------------------------------------

add('january', '12マスの年の帯の1つ目が塗られ、雪の積もった景色が広がる',
    '1月＝January。', f'''
<path d="M0 230q140-40 300 0t300 0v90H0z" fill="#eef4f7" class="o"/>
{snow(14)}
{bare_tree(150, 250, 0.9)}{bare_tree(440, 244, 0.8)}
{year_strip(1)}''')

add('february', '12マスの年の帯の2つ目が塗られ、まだ雪の残る寒い景色が続く',
    '2月＝February。', f'''
<path d="M0 240q140-30 300 0t300 0v80H0z" fill="#eef4f7" class="o"/>
{snow(9)}
{bare_tree(180, 258, 0.85)}
<g transform="translate(430 250)"><path d="M0 0v-40" stroke="{GRND}" stroke-width="6" fill="none"/>
  <path d="M0-30q-30-4-32-30 28-4 32 30z" class="green o"/></g>
{year_strip(2)}''')

add('april', '12マスの年の帯の4つ目が塗られ、花の咲いた木と小雨の景色になる',
    '4月＝April。', f'''
<path d="M0 250h600v70H0z" class="greenp"/>
{blossom_tree(180, 250, 1.0)}
{''.join(f'<path d="M{{}} {{}}l-10 22" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>'.format(330 + i * 40, 70 + (i % 3) * 34) for i in range(7))}
{sun(500, 90, 34)}
{year_strip(4)}''')

add('june', '12マスの年の帯の6つ目が塗られ、緑の濃い庭に花が咲きそろう',
    '6月＝June。', f'''
<path d="M0 240h600v80H0z" class="greenp"/>
{tree(140, 245, 1.0)}
{''.join(flower(260 + i * 70, 262, 0.6, c) for i, c in enumerate(['coral', 'violet', 'gold']))}
{''.join(f'<path d="M{{}} {{}}l-10 20" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>'.format(440 + i * 34, 80 + (i % 2) * 30) for i in range(4))}
{year_strip(6)}''')

add('july', '12マスの年の帯の7つ目が塗られ、真上の強い日差しが照りつける',
    '7月＝July。', f'''
{sun(300, 110, 62)}
<path d="M0 250h600v70H0z" class="greenp"/>
{tree(120, 255, 0.9)}{tree(480, 255, 0.85)}
{''.join(f'<path d="M{{}} 220q16-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(220 + i * 60) for i in range(3))}
{year_strip(7)}''')

add('august', '12マスの年の帯の8つ目が塗られ、浜辺にパラソルの立つ暑い景色になる',
    '8月＝August。', f'''
{sun(120, 90, 44)}
<path d="M0 230h600v90H0z" fill="#f0e0b8"/>
<path d="M0 230h600" fill="none" stroke="{GLDD}" stroke-width="0"/>
<path d="M380 230h220v90H380z" class="bluep"/>
<g transform="translate(240 250) rotate(-12)">
  <path d="M-80 0a80 80 0 0 1 160 0z" class="coral o"/>
  <path d="M0 0v70" stroke="{BRN}" stroke-width="7" fill="none"/></g>
{year_strip(8)}''')

add('september', '12マスの年の帯の9つ目が塗られ、かばんを持った子が学校へ向かう',
    '9月＝September。', f'''
<path d="M0 250h600v70H0z" class="greenp"/>
{building(450, 250, 0.7, 'teal')}
{person(180, 268, 0.9, 1, 'coral', 'blue', 'walk', 'cap', 'smile')}
<g transform="translate(212 200)"><path d="M-26-20h52v44h-52z" fill="{BRN}" class="o"/></g>
{arc(240, 190, 350, 190, 44, MUTED, True, 4)}
{year_strip(9)}''', arrow=True)

add('october', '12マスの年の帯の10個目が塗られ、赤や黄の葉が落ちる',
    '10月＝October。', f'''
<path d="M0 250h600v70H0z" class="greenp"/>
<g transform="translate(180 250)"><path d="M-9 0v-70h18V0z" class="goldd"/>
  <circle cx="-20" cy="-88" r="28" class="gold o"/><circle cx="22" cy="-96" r="30" class="coral o"/>
  <circle cx="0" cy="-118" r="26" class="gold o"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><ellipse rx="14" ry="8" class="{{}} o"/></g>'.format(300 + i * 60, 170 + (i % 3) * 46, -30 + i * 25, c) for i, c in enumerate(['gold', 'coral', 'goldd', 'coral', 'gold']))}
{year_strip(10)}''')

add('november', '12マスの年の帯の11個目が塗られ、葉を落とした木と厚い雲が並ぶ',
    '11月＝November。', f'''
{cloud(160, 100, 1.4, 'violet')}{cloud(420, 90, 1.2, 'violet')}
<path d="M0 250h600v70H0z" fill="#d9d3c2"/>
{bare_tree(170, 250, 1.0)}{bare_tree(430, 254, 0.9)}
{''.join(f'<path d="M{{}} {{}}l-10 20" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>'.format(240 + i * 44, 170 + (i % 2) * 26) for i in range(5))}
{year_strip(11)}''')

add('december', '12マスの年の帯の12個目が塗られ、雪の積もった家に明かりがともる',
    '12月＝December。', f'''
<path d="M0 230q140-40 300 0t300 0v90H0z" fill="#eef4f7" class="o"/>
{snow(14)}
<g transform="translate(300 250)">
  <path d="M-80 0v-90h160V0z" fill="#fffefd" class="o"/>
  <path d="M-96-90L0-150l96 60z" class="corald o"/>
  <path d="M-94-92q46-18 94 0t94 0" fill="#eef4f7" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-40-56h36v36h-36z" class="goldp o"/></g>
{bare_tree(110, 250, 0.7)}
{year_strip(12)}''')

# --- 曜日 --------------------------------------------------------------------

add('monday', '7マスの週の帯の1つ目が塗られ、上に月が浮かぶ',
    '月曜日＝Monday。Moon(月)の日が語源です。', f'''
<g transform="translate(300 170)">
  <circle r="90" class="goldp o"/>
  <circle cx="-24" cy="-24" r="14" fill="#eddfb4"/><circle cx="26" cy="10" r="18" fill="#eddfb4"/>
  <circle cx="-8" cy="44" r="10" fill="#eddfb4"/></g>
{week_strip(1)}''')

add('tuesday', '7マスの週の帯の2つ目が塗られ、上に軍神の剣が置かれる',
    '火曜日＝Tuesday。軍神ティール(Tiw)の日が語源です。', f'''
<g transform="translate(300 170)">
  <path d="M-14-120h28v170h-28z" fill="#c3cbd1" class="o"/>
  <path d="M-14 50h28l-14 30z" fill="#c3cbd1" class="o"/>
  <path d="M-60-6h120v20h-120z" class="goldd o"/>
  <path d="M-12 14h24v40h-24z" fill="{BRN}" class="o"/></g>
{week_strip(2)}''')

add('wednesday', '7マスの週の帯の3つ目が塗られ、上に主神の使いのワタリガラスが止まる',
    '水曜日＝Wednesday。主神オーディン(Woden)の日が語源です。', f'''
<g transform="translate(300 200)">
  <path d="M-120 60h240" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
  <ellipse cx="0" cy="0" rx="60" ry="40" fill="#2f3542" class="o"/>
  <circle cx="48" cy="-28" r="26" fill="#2f3542" class="o"/>
  <path d="M70-34l34 8-34 12z" class="goldd o"/>
  <circle cx="54" cy="-34" r="4" fill="#fffefd"/>
  <path d="M-60 4l-46-16 40 34z" fill="#2f3542" class="o"/>
  <path d="M-8 40v20M14 40v20" stroke="{GLDD}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
{week_strip(3)}''')

add('thursday', '7マスの週の帯の4つ目が塗られ、上に雷神の大づちと稲妻が並ぶ',
    '木曜日＝Thursday。雷神トール(Thor)の日が語源です。', f'''
<g transform="translate(260 180) rotate(-18)">
  <path d="M-14 0h28v130h-28z" fill="{BRN}" class="o"/>
  <path d="M-56-70h112v70h-112z" fill="#b5bec4" class="o"/>
  <path d="M-56-70h112v18h-112z" fill="#9aa7b1"/></g>
{bolt(430, 150, 1.6)}
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{GLD}" stroke-width="5"/>'.format(470 + i * 18, 240 - i * 14) for i in range(2))}
{week_strip(4)}''')

add('friday', '7マスの週の帯の5つ目が塗られ、上に愛の女神を表すハートが浮かぶ',
    '金曜日＝Friday。女神フリッグ(Frigg)の日が語源です。', f'''
<g transform="translate(300 170)">
  <path d="M0 84q-104-76-104-136 0-50 52-50 28 0 52 36 24-36 52-36 52 0 52 50 0 60-104 136z" class="coral o"/></g>
{''.join(spark(160 + i * 280, 110, 0.8, 'gold') for i in range(2))}
{week_strip(5)}''')

add('saturday', '7マスの週の帯の6つ目が塗られ、上に環をもつ土星が浮かぶ',
    '土曜日＝Saturday。農耕神サトゥルヌス(Saturn)の日が語源です。', f'''
<g transform="translate(300 170)">
  <circle r="68" class="goldp o"/>
  <path d="M-60 24q60 30 120 0" fill="none" stroke="{GLDD}" stroke-width="4"/>
  <ellipse rx="130" ry="34" fill="none" stroke="{GLD}" stroke-width="12" transform="rotate(-16)"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="{MUTED}"/>'.format(70 + (i * 83) % 460, 60 + (i * 37) % 60) for i in range(6))}
{week_strip(6)}''')

add('sunday', '7マスの週の帯の7つ目が塗られ、上に太陽が輝く',
    '日曜日＝Sunday。Sun(太陽)の日が語源です。', f'''
{sun(300, 170, 80)}
{week_strip(7)}''')

# --- もの --------------------------------------------------------------------

add('air', '開けた窓から新しい空気が流れこみ、カーテンがふくらむ',
    '空気、大気＝air。', f'''
<g transform="translate(300 190)">
  <path d="M-200-150h400v300h-400z" fill="#e4dccb" class="o"/>
  <path d="M-150-110h300v220h-300z" fill="#dfeaf2" class="o"/>
  <path d="M0-110v220" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-150-110q60 60 0 120 60 60 0 100" fill="#fffefd" opacity="0.75" stroke="{INK}" stroke-width="2.5"/></g>
{''.join(f'<path d="M{{}} {{}}q40-24 80 0t80 0" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>'.format(180, 130 + i * 60) for i in range(3))}
{''.join(f'<path d="M{{}} {{}}h60" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(420, 130 + i * 60) for i in range(3))}''', arrow=True)

add('allotment', '区切られた小さな畑の一区画で、野菜を育てている',
    '市民農園、貸し菜園＝allotment。', f'''
<path d="M0 230h600v170H0z" fill="#5b4636"/>
{''.join(f'<path d="M{{}} 230v170" fill="none" stroke="{BRN}" stroke-width="6" stroke-dasharray="12 10"/>'.format(200 + i * 200) for i in range(2))}
{''.join(f'<g transform="translate({{}} {{}})"><path d="M0 0v-40" stroke="{GRND}" stroke-width="6" fill="none"/><ellipse cx="-16" cy="-46" rx="16" ry="9" class="green o"/><ellipse cx="16" cy="-52" rx="16" ry="9" class="green o"/></g>'.format(240 + (i % 3) * 60, 300 + (i // 3) * 60) for i in range(6))}
{person(100, 330, 1.0, 1, 'teal', 'blue', 'hold', 'cap', 'smile')}
<g transform="translate(146 262) rotate(16)"><path d="M-7-50h14v80h-14z" fill="{BRN}" class="o"/>
  <path d="M-22 30h44l-6 40h-32z" fill="{MUTED}" class="o"/></g>
<g transform="translate(500 250)"><path d="M-60 0v-60h120V0z" fill="#fffefd" class="o"/>
  <path d="M-70-60L0-100l70 40z" class="corald o"/></g>''')

add('amber', '木の樹脂が固まった琥珀の中に、小さな虫が閉じこめられている',
    '琥珀＝amber。信号の黄色も amber と言います。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M-110 60q-30-90 20-130 50-40 110-20 60 20 60 90 0 60-80 70z" class="gold o"/>
  <path d="M-70 20q-14-50 30-70" fill="none" stroke="{GLDP}" stroke-width="10" stroke-linecap="round"/>
  <g transform="translate(20 10)">
    <ellipse rx="22" ry="12" fill="#6a5040"/><circle cx="-24" cy="-2" r="9" fill="#6a5040"/>
    <path d="M-10 12l-8 16M6 14l0 16M20 10l10 16M-10-12l-8-16M6-14l0-16M20-10l10-16" stroke="#6a5040" stroke-width="3" fill="none"/></g></g>
{''.join(spark(150 + i * 300, 130, 0.7, 'gold') for i in range(2))}''')

add('apricot', '枝についた小ぶりのオレンジ色の実が、半分に割られて種が見える',
    'アンズ、アプリコット＝apricot。', f'''
{table(352)}
<g transform="translate(200 250)">
  <circle r="70" class="gold o"/>
  <path d="M0-70q-6-30 14-44" fill="none" stroke="{GRND}" stroke-width="6"/>
  <ellipse cx="26" cy="-104" rx="24" ry="12" class="green o" transform="rotate(-20 26 -104)"/>
  <path d="M0-68v136" fill="none" stroke="{GLDD}" stroke-width="3"/></g>
<g transform="translate(430 260)">
  <path d="M0-60a60 60 0 0 1 0 120z" class="gold o"/>
  <path d="M0-60a60 60 0 0 0 0 120z" class="goldp o"/>
  <ellipse cx="-14" cy="0" rx="20" ry="26" fill="#8a5c2b" class="o"/></g>''')

add('ashtray', '浅い皿のふちに切れこみがあり、中に灰がたまっている',
    '灰皿＝ashtray。', f'''
{table(340)}
<g transform="translate(300 280)">
  <ellipse rx="130" ry="46" fill="#c3cbd1" class="o"/>
  <ellipse cy="-10" rx="100" ry="32" fill="#9aa7b1" class="o"/>
  <path d="M-40-40h80v14h-80z" fill="#c3cbd1" class="o"/>
  {''.join(f'<circle cx="{-40+i*34}" cy="-6" r="{7+i%2}" fill="#7d8790"/>' for i in range(3))}</g>
<g transform="translate(240 242) rotate(-16)">
  <path d="M-40-8h80v16h-80z" fill="#fffefd" class="o"/>
  <path d="M28-8h12v16H28z" fill="{GLDD}"/></g>
{''.join(f'<path d="M{{}} {{}}q12-14 0-26" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(200 + i * 16, 200 - i * 12) for i in range(2))}''')

add('awning', '店先の窓の上に、縞の布が斜めに張り出して日陰を作る',
    '日よけ、雨よけの張り出し＝awning。', f'''
<g transform="translate(300 300)">
  <path d="M-200-180h400v280h-400z" fill="#e4dccb" class="o"/>
  <path d="M-130-60h260v160h-260z" fill="#dfeaf2" class="o"/></g>
<g transform="translate(300 200)">
  <path d="M-180-40h360l40 70h-440z" class="coral o"/>
  {''.join(f'<path d="M{-150+i*60} -40l-22 70" stroke="#fffefd" stroke-width="16" fill="none"/>' for i in range(6))}
  <path d="M-220 30h440" fill="none" stroke="{CRLD}" stroke-width="8" stroke-linecap="round"/></g>
{sun(90, 80, 34)}
<g opacity="0.2"><path d="M100 240h400v120H100z" fill="{INK}"/></g>''')

add('backpacker', '大きなリュックを背負った人が、地図を手に旅を続ける',
    'バックパッカー、リュック旅行者＝backpacker。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
{person(280, 350, 1.4, 1, 'teal', 'blue', 'walk', 'cap', 'smile')}
<g transform="translate(238 250)">
  <path d="M-44-60h88v120h-88z" fill="{BRN}" class="o"/>
  <path d="M-44-60q44-24 88 0" fill="none" stroke="#6a5040" stroke-width="5"/>
  <path d="M-30 20h60v18h-60z" fill="#6a5040"/></g>
<g transform="translate(400 250) rotate(10)">
  <path d="M-50-34h100v68h-100z" class="paper"/>
  <path d="M-34 20L-6-14l20 16 26-30" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{tree(90, 336, 0.8)}{tree(540, 336, 0.7)}''')

add('backyard', '家の裏手にある、柵で囲まれた芝生の庭',
    '裏庭＝backyard。', f'''
<path d="M0 250h600v150H0z" class="greenp"/>
<g transform="translate(120 250)">
  <path d="M-110 0v-130h220V0z" fill="#fffefd" class="o"/>
  <path d="M-40 0v-70h80V0z" class="corald o"/></g>
{''.join(f'<path d="M{{}} 300v-70" stroke="{BRN}" stroke-width="11" fill="none" stroke-linecap="round"/>'.format(300 + i * 50) for i in range(6))}
<path d="M290 250h270M290 278h270" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
{tree(420, 250, 0.7)}
{''.join(flower(200 + i * 50, 340, 0.5, c) for i, c in enumerate(['coral', 'gold']))}''')

add('badger', '白と黒の縞のある顔をしたアナグマが、巣穴のそばに出てくる',
    'アナグマ＝badger。', f'''
<path d="M0 300h600v100H0z" fill="#5b4636"/>
<path d="M60 300q60-50 120 0z" fill="#3f3126"/>
<g transform="translate(340 290)">
  <ellipse rx="130" ry="62" fill="#6b6b6b" class="o"/>
  <path d="M-130-20q130-50 260 0" fill="#8a8a8a"/>
  <ellipse rx="130" ry="62" fill="none" class="o"/>
  <circle cx="-120" cy="-30" r="46" fill="#fffefd" class="o"/>
  <path d="M-150-64q-14 70 10 84M-98-66q16 66-8 82" stroke="#2f3542" stroke-width="14" fill="none"/>
  <circle cx="-160" cy="-72" r="14" fill="#6b6b6b" class="o"/><circle cx="-86" cy="-76" r="14" fill="#6b6b6b" class="o"/>
  <ellipse cx="-160" cy="-12" rx="10" ry="7" fill="#2f3542"/>
  <circle cx="-142" cy="-40" r="4" class="ink"/><circle cx="-104" cy="-42" r="4" class="ink"/>
  {''.join(f'<path d="M{-60+i*60} 58v28" stroke="#6b6b6b" stroke-width="18" fill="none" stroke-linecap="round"/>' for i in range(3))}</g>''')

add('bakery', '窓にパンを並べた店先から、焼きたての湯気が上がる',
    'パン屋、製パン所＝bakery。', f'''
<g transform="translate(300 330)">
  <path d="M-160 0v-160h320V0z" fill="#fffefd" class="o"/>
  <path d="M-178-160h356l-24-50h-308z" class="coral o"/>
  <path d="M-120-120h140v90h-140z" class="goldp o"/>
  <path d="M60-100h70v100H60z" class="corald o"/>
  {''.join(f'<g transform="translate({-90+i*46} {-90})"><path d="M-18 16q-4-26 8-30 4-10 12-10t12 10q12 4 8 30z" fill="#d9a45e" class="o"/></g>' for i in range(3))}
  {''.join(f'<ellipse cx="{-90+i*46}" cy="-52" rx="18" ry="8" fill="#c88f4e" class="o"/>' for i in range(3))}</g>
{''.join(f'<path d="M{{}} {{}}q14-18 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(180 + i * 40, 140 - i * 16) for i in range(3))}''')

add('banister', '階段に沿って斜めに走る手すりを、手がつかんでいる',
    '階段の手すり＝banister。', f'''
{''.join(f'<path d="M{{}} 360v-{{}}h90v{{}}z" fill="{STONE}" class="o"/>'.format(60 + i * 90, 50 + i * 62, 50 + i * 62) for i in range(5))}
<path d="M70 300L510 30" fill="none" stroke="{BRN}" stroke-width="18" stroke-linecap="round"/>
{''.join(f'<path d="M{{}} {{}}v{{}}" stroke="{BRN}" stroke-width="9" fill="none"/>'.format(120 + i * 90, 268 - i * 55, 56) for i in range(5))}
{hand(290, 168, 1)}''')

add('barbecue', '炭火の網の上で肉と野菜が焼かれ、煙が立ちのぼる',
    'バーベキュー＝barbecue。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(300 300)">
  <path d="M-120 0h240v-40h-240z" fill="#6b7680" class="o"/>
  <path d="M-100-40h200l-10-60h-180z" fill="#4e5a66" class="o"/>
  {''.join(f'<path d="M{-90+i*24} -100v-10" stroke="{MUTED}" stroke-width="0"/>' for i in range(1))}
  <path d="M-100-100h200" fill="none" stroke="{INK}" stroke-width="4"/>
  {''.join(f'<path d="M{-92+i*26} -104v8" stroke="{INK}" stroke-width="4" fill="none"/>' for i in range(8))}
  <path d="M-100 0l-24 60M100 0l24 60" stroke="#4e5a66" stroke-width="12" fill="none" stroke-linecap="round"/></g>
{''.join(f'<ellipse cx="{{}}" cy="192" rx="26" ry="12" fill="#b5744a" class="o"/>'.format(250 + i * 60) for i in range(2))}
{''.join(f'<circle cx="{{}}" cy="192" r="13" class="coral o"/>'.format(360 + i * 0) for i in range(1))}
{''.join(f'<path d="M{{}} {{}}q16-20 0-38" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(220 + i * 60, 150 - i * 16) for i in range(3))}''')

add('barn', '屋根の高い納屋の大きな扉が開き、中に干し草が積んである',
    '納屋、家畜小屋＝barn。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<g transform="translate(300 320)">
  <path d="M-160 0v-140h320V0z" class="coral o"/>
  <path d="M-180-140L0-240l180 100z" class="corald o"/>
  <path d="M-70 0v-120h140V0z" fill="#c9a464" class="o"/>
  <path d="M0-120v120M-70-60h140M-70-120l140 120M70-120L-70 0" fill="none" stroke="{BRN}" stroke-width="5"/>
  <path d="M-30-190h60v40h-60z" class="coralp o"/></g>
{''.join(f'<g transform="translate({{}} 350)"><ellipse rx="40" ry="20" fill="#e0c48c" class="o"/><path d="M-30-10q30-14 60 0" fill="none" stroke="{GLDD}" stroke-width="3"/></g>'.format(90 + i * 420) for i in range(2))}''')

add('basin', '浅く広い器に湯が張られ、そばに石けんが置かれている',
    '洗面器、たらい／(地形の)盆地＝basin。', f'''
{table(346)}
<g transform="translate(300 260)">
  <path d="M-140-40q0 100 140 100t140-100z" fill="#fffefd" class="o"/>
  <ellipse cy="-40" rx="140" ry="34" fill="#fffefd" class="o"/>
  <ellipse cy="-34" rx="120" ry="26" class="bluep"/></g>
<g transform="translate(460 200) rotate(12)">
  <rect x="-34" y="-22" width="68" height="44" rx="12" class="goldp o"/></g>
{''.join(f'<path d="M{{}} {{}}q12-14 0-26" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(180 + i * 20, 180 - i * 12) for i in range(2))}''')

add('bathroom', '浴槽と洗面台と鏡のある、タイル張りの部屋',
    '浴室、洗面所＝bathroom。', f'''
<g transform="translate(300 200)">
  <path d="M-260-160h520v320h-520z" fill="#eef4f7" class="o"/>
  {''.join(f'<path d="M{-260+i*65} -160v320" fill="none" stroke="#d7e3ea" stroke-width="3"/>' for i in range(1, 8))}
  {''.join(f'<path d="M-260 {-100+i*80}h520" fill="none" stroke="#d7e3ea" stroke-width="3"/>' for i in range(4))}</g>
<g transform="translate(180 300)">
  <path d="M-110-50q0 70 110 70t110-70z" fill="#fffefd" class="o"/>
  <path d="M-110-50h220" fill="none" class="o"/>
  <path d="M-92-30q0 46 92 46t92-46z" class="bluep"/></g>
<g transform="translate(450 250)">
  <path d="M-60-10q0 50 60 50t60-50z" fill="#fffefd" class="o"/>
  <path d="M-60-10h120" fill="none" class="o"/>
  <path d="M0 40v50" stroke="#fffefd" stroke-width="16" fill="none"/>
  <path d="M0-40v20" stroke="{MUTED}" stroke-width="8" fill="none"/>
  <path d="M-44-130h88v70h-88z" fill="#dfeaf2" class="o"/></g>''')

add('bathtub', '脚のついた白い浴槽に湯が張られ、泡が浮かんでいる',
    '浴槽、バスタブ＝bathtub。', f'''
<g transform="translate(300 250)">
  <path d="M-180-60q-14 120 30 130h300q44-10 30-130z" fill="#fffefd" class="o"/>
  <ellipse cy="-60" rx="180" ry="40" fill="#fffefd" class="o"/>
  <ellipse cy="-56" rx="158" ry="32" class="bluep"/>
  <path d="M-140 70l-20 60M140 70l20 60" stroke="#e8e3d8" stroke-width="16" fill="none" stroke-linecap="round"/>
  <path d="M-180-60q-14 120 30 130h300q44-10 30-130" fill="none" class="o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="#ffffff" stroke="{BLU}" stroke-width="2"/>'.format(200 + (i * 53) % 200, 180 + (i * 31) % 24, 8 + i % 4) for i in range(7))}
<g transform="translate(470 150)"><path d="M0 40V0q0-30-30-30" fill="none" stroke="{MUTED}" stroke-width="12"/></g>
{''.join(drop(470, 200 + i * 22, 1.0, 'blue') for i in range(2))}''')

add('beard', '男性のあごの下いっぱいに、濃いひげが生えている',
    'あごひげ＝beard。', f'''
<g transform="translate(300 200)">
  <circle r="110" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-108-40q10-76 108-76t108 76q-46-34-108-24-60-10-108 24z" fill="{HAIR}"/>
  <circle cx="-40" cy="-16" r="6" class="ink"/><circle cx="40" cy="-16" r="6" class="ink"/>
  <path d="M-96 20q22 110 96 110t96-110q-14 66-96 66T-96 20z" fill="{HAIR}"/>
  <path d="M-30 36q30 20 60 0" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-28 10h20M8 10h20" fill="none" stroke="{HAIR}" stroke-width="8" stroke-linecap="round"/></g>
{ring(300, 268, 100, True)}''')

add('beaver', '平たい尾をもつビーバーが、かじった枝で川をせき止めている',
    'ビーバー＝beaver。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M-50-8h100v16h-100z" fill="{BRN}" class="o"/></g>'.format(400 + (i % 3) * 40, 250 + (i // 3) * 26, -20 + i * 18) for i in range(6))}
<g transform="translate(210 280)">
  <ellipse rx="90" ry="54" fill="#7a5a3a" class="o"/>
  <circle cx="-78" cy="-34" r="40" fill="#8a6a46" class="o"/>
  <circle cx="-104" cy="-62" r="14" fill="#6a4a2a" class="o"/><circle cx="-58" cy="-68" r="14" fill="#6a4a2a" class="o"/>
  <circle cx="-96" cy="-38" r="5" class="ink"/>
  <ellipse cx="-116" cy="-24" rx="10" ry="7" fill="#4a3420"/>
  <path d="M-110-8h14v22h-14zM-94-8h14v22h-14z" fill="#fffefd" stroke="{INK}" stroke-width="2"/>
  <path d="M84 24q60 6 74-24-20-30-74-16z" fill="#5b4030" class="o"/></g>''')

add('bedbug', 'ベッドのシーツの上を、平たく小さな虫が這っている',
    'トコジラミ、南京虫＝bedbug。', f'''
<g transform="translate(300 290)">
  <path d="M-220 0v-60h440V0z" fill="#fffefd" class="o"/>
  <path d="M-220-60h110v-50h-110z" class="bluep o"/>
  <path d="M-110-48q110-30 330 0v-12h-330z" class="blue o"/></g>
<g transform="translate(320 230) scale(2.6)">
  <ellipse rx="26" ry="18" fill="#a2603a" class="o"/>
  <circle cx="-24" cy="-4" r="10" fill="#8a4c2c" class="o"/>
  <path d="M-32-10l-12-8M-32-2l-12 6" stroke="{INK}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M-10 16l-6 12M4 18l0 12M16 14l8 12M-10-16l-6-12M4-18l0-12M16-14l8-12" stroke="{INK}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  {''.join(f'<path d="M{-14+i*14} -14v28" stroke="#7a3f22" stroke-width="2" fill="none"/>' for i in range(3))}</g>
{ring(320, 230, 90, True)}''')

add('bedding', 'たたんだシーツと毛布とまくらが、重ねて積まれている',
    '寝具一式＝bedding。', f'''
{table(352)}
<g transform="translate(300 300)">
  {''.join(f'<g transform="translate(0 {-i*44})"><path d="M-130-22h260v44h-260z" fill="{c}" stroke="{INK}" stroke-width="2.5"/><path d="M-130 0h260" fill="none" stroke="{MUTED}" stroke-width="2"/></g>' for i, c in enumerate(['#fffefd', '#dff4ef', '#e1edfb']))}</g>
<g transform="translate(300 130)">
  <path d="M-110-40q110-30 220 0 16 40 0 70-110 26-220 0-16-30 0-70z" fill="#fffefd" class="o"/></g>
{''.join(spark(140 + i * 320, 250, 0.6, 'gold') for i in range(2))}''')

add('bedroom', 'ベッドと小さな棚と窓のある、眠るための部屋',
    '寝室＝bedroom。', f'''
<g transform="translate(300 200)">
  <path d="M-260-160h520v320h-520z" fill="#f6efe1" class="o"/></g>
<g transform="translate(250 310)">
  <path d="M-150 0v-70h300V0z" fill="#fffefd" class="o"/>
  <path d="M-150-70h70v-56h-70z" class="bluep o"/>
  <path d="M-80-56q80-28 230 0v-14H-80z" class="blue o"/>
  <path d="M-150 0v30M150 0v30" stroke="{BRN}" stroke-width="10" fill="none"/>
  <path d="M-140-92q34-22 62 0 8 22 0 34-30 12-62 0-8-14 0-34z" fill="#fffefd" class="o"/></g>
<g transform="translate(500 300)">
  <path d="M-46 0v-90h92V0z" fill="#c9a464" class="o"/>
  <path d="M-30-70h60v24h-60zM-30-38h60v24h-60z" fill="#a0764a"/></g>
<g transform="translate(470 130)"><path d="M-70-60h140v120h-140z" fill="#dfeaf2" class="o"/>
  <path d="M0-60v120M-70 0h140" fill="none" stroke="{INK}" stroke-width="4"/></g>''')

add('bicycle', '二つの車輪とペダル、ハンドルのついた自転車',
    '自転車＝bicycle。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(300 280)">
  <circle cx="-140" cy="60" r="80" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle cx="140" cy="60" r="80" fill="none" stroke="{INK}" stroke-width="9"/>
  {''.join(f'<g transform="translate(-140 60) rotate({i*45})"><path d="M0 0v-74" stroke="{MUTED}" stroke-width="3" fill="none"/></g>' for i in range(8))}
  {''.join(f'<g transform="translate(140 60) rotate({i*45})"><path d="M0 0v-74" stroke="{MUTED}" stroke-width="3" fill="none"/></g>' for i in range(8))}
  <path d="M-140 60L-20-30 60 60 -20-30 100-40 140 60M-20-30L-40-60" fill="none" stroke="{TEA}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M100-40l-16-40" stroke="{TEA}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M60-90h60" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M-60-70h50l-10 18h-40z" class="coral o"/>
  <circle cx="0" cy="60" r="18" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M0 60l26 18" stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round"/></g>''')

add('billboard', '道路のわきに立つ大きな広告板が、脚に支えられている',
    '(屋外の)大型広告板＝billboard。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<g transform="translate(300 330)">
  <path d="M-40 0v-90h20v90zM20 0v-90h20v90z" fill="{MUTED}"/>
  <path d="M-200-260h400v170h-400z" fill="#fffefd" class="o"/>
  <path d="M-200-260h400v36h-400z" class="teal o"/>
  <circle cx="-120" cy="-160" r="42" class="coralp o"/>
  <path d="M-60-186h230v26h-230zM-60-146h170v20h-170z" fill="{MUTED}"/>
  {''.join(f'<path d="M{-140+i*140} -260v-20" stroke="{MUTED}" stroke-width="6" fill="none"/><circle cx="{-140+i*140}" cy="-288" r="12" class="goldp o"/>' for i in range(3))}</g>''')

add('binoculars', '二つの筒が並んだ双眼鏡を、両手でのぞきこむ',
    '双眼鏡＝binoculars。', f'''
<g transform="translate(300 210)">
  {''.join(f'<g transform="translate({x} 0)"><path d="M-50-90h100v150a50 50 0 0 1-100 0z" class="teal o"/><ellipse cy="-90" rx="50" ry="18" class="teald o"/><ellipse cy="-90" rx="32" ry="11" fill="#2f3a4d"/><path d="M-50 0h100" stroke="{TEAD}" stroke-width="8" fill="none"/></g>' for x in (-70, 70))}
  <path d="M-24-40h48v70h-48z" class="teald o"/></g>
{hand(160, 300, 1)}
{hand(440, 300, -1)}
{''.join(f'<path d="M{{}} {{}}q16-16 0-32" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(470 + i * 20, 110 - i * 14) for i in range(2))}''')

add('bleach', '漂白剤のボトルから注いだ液で、しみのついた布が白くなる',
    '漂白剤、漂白する＝bleach。', f'''
{table(352)}
{split()}
<g transform="translate(150 290)">
  <path d="M-80-40h160v80h-160z" fill="#fffefd" class="o"/>
  <path d="M-40-20q-20 30 10 40 34 10 44-16 6-22-24-30z" fill="#b5744a"/></g>
<g transform="translate(450 290)">
  <path d="M-80-40h160v80h-160z" fill="#fffefd" class="o"/></g>
{tick(450, 180, 0.7)}
<g transform="translate(300 130) rotate(30)">
  <path d="M-34-70h68v110a24 24 0 0 1-24 24h-20a24 24 0 0 1-24-24z" class="tealp o"/>
  <path d="M-16-92h32v22h-32z" class="teal o"/></g>
{''.join(drop(360 + i * 12, 200 + i * 24, 1.0, 'teal') for i in range(2))}''')

add('blizzard', '横なぐりの雪で前が見えず、人が身をかがめて進む',
    '猛吹雪＝blizzard。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#dfe4e6"/></g>
{''.join(f'<path d="M{{}} {{}}l-46 20" fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="round"/>'.format(120 + (i * 97) % 500, 40 + (i * 53) % 300) for i in range(16))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="#ffffff"/>'.format(60 + (i * 71) % 500, 60 + (i * 41) % 280, 4 + i % 4) for i in range(14))}
<g transform="translate(320 350) rotate(-20)">{person(0, 0, 1.3, 1, 'coral', 'blue', 'walk', 'cap', 'flat')}</g>
<path d="M0 350h600v50H0z" fill="#ffffff"/>''')

add('bookcase', '床から天井まである棚に、本がぎっしり並んでいる',
    '本棚、書棚＝bookcase。', f'''
<g transform="translate(300 200)">
  <path d="M-180-180h360v360h-360z" fill="#c9a464" class="o"/>
  <path d="M-160-160h320v320h-320z" fill="#f6efe1" class="o"/>
  {''.join(f'<path d="M-160 {-80+i*80}h320v14h-320z" fill="#a0764a"/>' for i in range(3))}
  {''.join(f'<rect x="{-150+ (i%9)*35}" y="{-152+(i//9)*80}" width="{22+(i%3)*6}" height="{66-(i%2)*8}" rx="3" fill="{c}" stroke="{INK}" stroke-width="2"/>' for i, c in enumerate(['#238b83','#e86452','#d99a2b','#4e86c6','#816eb2','#4e986a','#238b83','#e86452','#d99a2b']*4))}</g>''')

add('bookmark', '本のページの間から、細長いしおりの端がのぞく',
    'しおり＝bookmark。', f'''
{table(352)}
{book(300, 240, 1.5, 'teal')}
<g transform="translate(350 190) rotate(6)">
  <path d="M-24-120h48v200l-24-30-24 30z" class="coral o"/>
  <path d="M-14-90h28v10h-28zM-14-64h28v10h-28z" fill="#fffefd"/></g>''')

add('bottle', '首の細いびんに、栓とラベルがついている',
    'びん、ボトル＝bottle。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-24-140h48v40l34 40q14 18 14 40v80a20 20 0 0 1-20 20h-104a20 20 0 0 1-20-20v-80q0-22 14-40l34-40z" fill="#dff1f8" class="o"/>
  <path d="M-26-150h52v18h-52z" class="coral o"/>
  <path d="M-58-10h116v70h-116z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="-40" y="{6+i*20}" width="{80-(i%2)*24}" height="8" rx="4" fill="{MUTED}"/>' for i in range(2))}
  <path d="M-58 30q0 48 58 48t58-48" fill="none" stroke="{BLU}" stroke-width="0"/></g>''')

add('boulder', '人の背より大きな丸い岩が、山道をふさいでいる',
    '大きな丸い岩＝boulder。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<path d="M40 340q120-60 250-30t270 20" fill="none" stroke="{STONE}" stroke-width="0"/>
<g transform="translate(340 250)">
  <path d="M-150 90q-40-100 20-150 60-50 140-20 80 30 70 120-6 50-70 50z" fill="{STONE}" class="o"/>
  <path d="M-100 40q40-50 100-40" fill="none" stroke="#a9b3ba" stroke-width="6"/>
  <path d="M40 60q40-20 50-60" fill="none" stroke="#a9b3ba" stroke-width="5"/></g>
{person(110, 350, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'flat')}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="{STONE}" class="o"/>'.format(150 + i * 30, 350 + (i % 2) * 10, 10 + i % 3) for i in range(3))}''')

add('bouquet', '色とりどりの花を束ね、紙で包んでリボンを結んだ花束',
    '花束＝bouquet。', f'''
{''.join(flower(250 + (i % 3) * 56, 140 + (i // 3) * 44, 0.8, c) for i, c in enumerate(['coral', 'gold', 'violet', 'coral', 'green', 'gold']))}
<g transform="translate(300 290)">
  <path d="M-110-70l110 150 110-150q-110 40-220 0z" fill="#f6efe1" class="o"/>
  <path d="M-40 40h80v20h-80z" class="coral o"/>
  <path d="M-40 50q-40-14-56 10M40 50q40-14 56 10" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>
  {''.join(f'<path d="M{-40+i*26} -70v-40" stroke="{GRND}" stroke-width="5" fill="none"/>' for i in range(4))}</g>''')

add('boxing', 'グローブをはめた二人が、ロープに囲まれたリングで構える',
    'ボクシング＝boxing。', f'''
<g transform="translate(300 300)">
  <path d="M-260 60h520" fill="none" stroke="{STONE}" stroke-width="0"/>
  <path d="M-240 60h480v20h-480z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M-250 {-60+i*44}h500" stroke="{CRL}" stroke-width="9" fill="none" stroke-linecap="round"/>' for i in range(3))}
  <path d="M-250-70v140M250-70v140" stroke="{MUTED}" stroke-width="14" fill="none" stroke-linecap="round"/></g>
{person(200, 340, 1.15, 1, 'coral', 'blue', 'up', 'short', 'flat')}
{person(400, 340, 1.15, -1, 'teal', 'green', 'up', 'cap', 'flat')}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="24" class="{{}} o"/>'.format(x, y, c) for x, y, c in [(248, 208, 'coral'), (352, 208, 'teal')])}''')

add('braid', '長い髪が三つの束に分けられ、交差させて編まれている',
    '編んだ髪、三つ編み＝braid。', f'''
<g transform="translate(300 190)">
  <circle cy="-60" r="72" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-72-96q8-72 72-72t72 72q-34-30-72-22-40-8-72 22z" fill="{HAIR}"/>
  <circle cx="-26" cy="-58" r="4.5" class="ink"/><circle cx="26" cy="-58" r="4.5" class="ink"/>
  <path d="M-18-30q18 14 36 0" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-72-70q-20 60 0 90 20-30 0-90M72-70q20 60 0 90-20-30 0-90" fill="{HAIR}"/></g>
<g transform="translate(370 220)">
  {''.join(f'<path d="M-24 {i*36}q24 18 48 0M24 {i*36}q-24 18-48 0" fill="none" stroke="{HAIR}" stroke-width="18" stroke-linecap="round"/>' for i in range(4))}
  <path d="M-10 150h20v18h-20z" class="coral o"/></g>''')

finish(__file__)
