# -*- coding: utf-8 -*-
"""第183回。plus31 の50語。台所・教室・工具まわり。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def bread_loaf(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-80 34q-12-72 26-82 8-26 54-26t54 26q38 10 26 82z" fill="#d9a45e" class="o"/>'
            f'<path d="M-80 34h160v20h-160z" fill="#b9813f" class="o"/></g>')

def cup_saucer(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse cy="46" rx="80" ry="18" fill="#fffefd" class="o"/>'
            f'<path d="M-52-34h104v46a30 30 0 0 1-30 30h-44a30 30 0 0 1-30-30z" fill="#fffefd" class="o"/>'
            f'<path d="M52-20q34 0 34 26t-34 26" fill="none" stroke="{INK}" stroke-width="8"/>'
            f'<path d="M-44-24h88v34a22 22 0 0 1-22 22h-44a22 22 0 0 1-22-22z" class="{cls}p"/></g>')

add('breadcrumb', '切ったパンから細かいくずが落ち、皿の上に散らばる',
    'パン粉、パンくず＝breadcrumb。', f'''
{table(352)}
{bread_loaf(180, 250, 0.9)}
<g transform="translate(420 280)"><ellipse rx="110" ry="30" fill="#fffefd" class="o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="#d9a45e" stroke="{INK}" stroke-width="1.8"/>'.format(350 + (i * 41) % 150, 262 + (i * 23) % 24, 4 + i % 3) for i in range(14))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="4" fill="#d9a45e"/>'.format(290 + i * 16, 250 + (i % 2) * 14) for i in range(3))}''')

add('breakfast', '朝の食卓にトーストと卵と紅茶が並び、窓の外に朝日が見える',
    '朝食＝breakfast。', f'''
{table(300)}
<g transform="translate(500 130)"><path d="M-70-60h140v120h-140z" fill="#dfeaf2" class="o"/>{sun(0, 0, 30)}</g>
<g transform="translate(180 286)"><ellipse rx="80" ry="22" fill="#fffefd" class="o"/>
  <path d="M-50-34h100v34h-100z" fill="#e0b872" class="o"/>
  <ellipse cx="20" cy="-10" rx="30" ry="18" fill="#fffefd" class="o"/>
  <circle cx="20" cy="-10" r="11" class="gold"/></g>
{cup_saucer(370, 250, 0.8)}
{''.join(f'<path d="M{{}} {{}}q12-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(350 + i * 20, 200 - i * 12) for i in range(2))}''')

add('breezy', 'そよ風に洗濯物と木の葉が軽く揺れ、日差しも明るい',
    'そよ風の吹く＝breezy。', f'''
{sun(500, 90, 40)}
<path d="M0 320h600v80H0z" class="greenp"/>
<path d="M60 160q240-40 480 0" fill="none" stroke="{BRN}" stroke-width="5"/>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M-26-10h52v70h-52z" fill="{{}}" stroke="{INK}" stroke-width="2.5"/></g>'.format(150 + i * 110, 176 + i * 2, 10 + i * 3, c) for i, c in enumerate(['#dff4ef', '#fde9e3', '#e1edfb', '#fff0c5']))}
{''.join(f'<path d="M40 {{}}q80-16 160 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>'.format(240 + i * 34) for i in range(2))}
{tree(520, 330, 0.8)}''')

add('brewery', '大きな金属の醸造タンクが並び、管でつながっている',
    '醸造所、ビール工場＝brewery。', f'''
{table(352)}
{''.join(f'<g transform="translate({{}} 250)"><path d="M-60-110h120v190a30 30 0 0 1-30 30h-60a30 30 0 0 1-30-30z" fill="#c3cbd1" class="o"/><ellipse cy="-110" rx="60" ry="20" fill="#dfe6ea" class="o"/><path d="M-30 40h60v20h-60z" fill="#9aa7b1" class="o"/></g>'.format(150 + i * 160) for i in range(2))}
<path d="M210 160h180" fill="none" stroke="{MUTED}" stroke-width="14"/>
<g transform="translate(470 280)">
  <path d="M-44-70h88v110a24 24 0 0 1-24 24h-40a24 24 0 0 1-24-24z" fill="#fffefd" class="o"/>
  <path d="M-36-30h72v70a18 18 0 0 1-18 18h-36a18 18 0 0 1-18-18z" class="gold"/>
  <path d="M-36-40h72v18h-72z" fill="#fffefd"/>
  <path d="M44-40q30 0 30 26t-30 26" fill="none" stroke="{INK}" stroke-width="8"/></g>''')

add('briefcase', '角ばった革のかばんに取っ手と留め金がついている',
    '書類かばん、ブリーフケース＝briefcase。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-150-70h300v140h-300z" fill="{BRN}" class="o"/>
  <path d="M-150 0h300" fill="none" stroke="#6a5040" stroke-width="5"/>
  <path d="M-50-70q50-46 100 0" fill="none" stroke="#6a5040" stroke-width="12"/>
  <path d="M-30-14h60v28h-60z" class="goldd o"/>
  <path d="M-110-40h40v20h-40zM70-40h40v20h-40z" fill="#6a5040"/></g>''')

add('brochure', '表紙に写真の載った薄い冊子が、半分開いて立っている',
    'パンフレット、小冊子＝brochure。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M0-100L-130-70v160L0 110z" fill="#fffefd" class="o"/>
  <path d="M0-100l130-30v160L0 110z" fill="#f6efe1" class="o"/>
  <path d="M-110-54h84v54h-84z" class="tealp o"/>
  {''.join(f'<rect x="-110" y="{14+i*20}" width="{84-(i%2)*26}" height="9" rx="4.5" fill="{MUTED}"/>' for i in range(3))}
  {''.join(f'<rect x="26" y="{-40+i*24}" width="{86-(i%3)*26}" height="9" rx="4.5" fill="{MUTED}"/>' for i in range(5))}</g>''')

add('bronze', '銅色に鈍く光るメダルが、リボンで下げられている',
    '青銅、銅メダル＝bronze。', f'''
<g transform="translate(300 250)">
  <path d="M-50-150l40 90h-80zM50-150l-40 90h80z" class="coral o"/>
  <circle r="80" fill="#b08048" class="o"/>
  <circle r="54" fill="none" stroke="#8a6034" stroke-width="6"/>
  <path d="M-24 0l16 22 34-42" fill="none" stroke="#8a6034" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></g>
{''.join(spark(150 + i * 300, 130, 0.7, 'gold') for i in range(2))}''')

add('buckle', 'ベルトの先が留め金に通され、ピンで穴に留まっている',
    '(ベルトの)留め金＝buckle。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-240-26h200v52h-200z" fill="{BRN}" class="o"/>
  <path d="M60-26h240v52H60z" fill="{BRN}" class="o"/>
  {''.join(f'<circle cx="{120+i*44}" cy="0" r="7" fill="#6a5040"/>' for i in range(4))}
  <path d="M-44-46h104v92h-104z" fill="none" stroke="{GLDD}" stroke-width="14"/>
  <path d="M-10-46v92" stroke="{GLDD}" stroke-width="10" fill="none"/>
  <path d="M-10 0h56" stroke="{GLDD}" stroke-width="8" fill="none" stroke-linecap="round"/></g>''')

add('bumper', '車の前についた横長の部品が、ぶつかった衝撃でへこんでいる',
    '(車の)バンパー＝bumper。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(300 300)">
  <path d="M-170 0v-50l50-80h240l50 80V0z" class="teal o"/>
  <path d="M-100-124h200l34 60h-268z" fill="#dfeaf2" class="o"/>
  <circle cx="-110" cy="6" r="34" class="ink"/><circle cx="110" cy="6" r="34" class="ink"/>
  <path d="M-180-28h360v34h-360z" fill="#9aa7b1" class="o"/>
  <path d="M-60-28q30 34 60 0" fill="#6b7680" stroke="{INK}" stroke-width="2.5"/></g>
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(300 + i * 20, 230 - i * 16) for i in range(2))}''')

add('bunk', '上下に重なった二段の寝台に、はしごがかかっている',
    '作りつけの寝台、二段ベッド＝bunk。', f'''
<g transform="translate(300 250)">
  <path d="M-160-120v240M160-120v240" stroke="{BRN}" stroke-width="14" fill="none" stroke-linecap="round"/>
  <path d="M-160-40h320v40h-320z" fill="#fffefd" class="o"/>
  <path d="M-160 80h320v40h-320z" fill="#fffefd" class="o"/>
  <path d="M-150-52h80v12h-80zM-150 68h80v12h-80z" class="bluep o"/>
  <path d="M-70-46q110-20 220 0v-6H-70zM-70 74q110-20 220 0v-6H-70z" class="blue o"/>
  <path d="M100-40v120M150-40v120" stroke="{BRN}" stroke-width="8" fill="none"/>
  {''.join(f'<path d="M100 {-10+i*36}h50" stroke="{BRN}" stroke-width="7" fill="none"/>' for i in range(3))}</g>''')

add('buoy', '海に浮かぶ赤いブイが、波の上で位置を知らせる',
    '浮標、ブイ＝buoy。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 262q22-14 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 250)">
  <path d="M-60 0q0-60 60-60t60 60z" class="coral o"/>
  <path d="M-60 0q0 40 60 40t60-40z" class="corald o"/>
  <path d="M0-60v-60" stroke="{MUTED}" stroke-width="8" fill="none"/>
  <circle cy="-130" r="16" class="goldp o"/>
  <path d="M0 40v50" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9" fill="none"/></g>
{''.join(f'<path d="M{{}} {{}}q10-12 0-22" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(400 + i * 20, 180 - i * 12) for i in range(2))}''')

add('cafeteria', '盆を持った人が、並んだ料理から自分で選んで取る',
    'カフェテリア、セルフ式の食堂＝cafeteria。', f'''
{table(300)}
<g transform="translate(380 250)">
  <path d="M-180-60h360v60h-360z" fill="#dfe6ea" class="o"/>
  {''.join(f'<g transform="translate({-130+i*90} -30)"><path d="M-36-14h72v28h-72z" fill="#c3cbd1" class="o"/><ellipse cy="-14" rx="30" ry="9" class="{c}p o"/></g>' for i, c in enumerate(['coral', 'green', 'gold', 'violet']))}</g>
{person(140, 340, 1.2, 1, 'teal', 'blue', 'carry', 'bun', 'smile')}
<g transform="translate(196 262) rotate(-6)">
  <path d="M-50-14h100v28h-100z" fill="#c9a464" class="o"/>
  <ellipse cx="-12" cy="-20" rx="26" ry="9" fill="#fffefd" class="o"/></g>''')

add('calcium', '牛乳とチーズの上に、骨の形が重ねて示される',
    'カルシウム＝calcium。', f'''
{table(346)}
<g transform="translate(170 270)">
  <path d="M-50-80h100v130a20 20 0 0 1-20 20h-60a20 20 0 0 1-20-20z" fill="#fffefd" class="o"/>
  <path d="M-50-20h100v70a20 20 0 0 1-20 20h-60a20 20 0 0 1-20-20z" fill="#f2f6f8"/>
  <path d="M-30-100h60v20h-60z" class="bluep o"/></g>
<g transform="translate(330 300)">
  <path d="M-60-40h120l-16 40h-88z" class="goldp o"/>
  {''.join(f'<circle cx="{-30+i*30}" cy="-20" r="7" fill="{GLDD}"/>' for i in range(3))}</g>
<g transform="translate(470 200)">
  <path d="M-14-70h28v140h-28z" fill="#fffefd" class="o"/>
  <circle cx="-22" cy="-78" r="22" fill="#fffefd" class="o"/><circle cx="22" cy="-78" r="22" fill="#fffefd" class="o"/>
  <circle cx="-22" cy="78" r="22" fill="#fffefd" class="o"/><circle cx="22" cy="78" r="22" fill="#fffefd" class="o"/></g>
{''.join(f'<path d="M{{}} 180L440 160" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(x) for x in (220, 350))}''')

add('calculator', '数字のキーが並んだ電卓の画面に、計算の結果が出ている',
    '電卓、計算機＝calculator。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M-110-140h220v280h-220z" class="tealp o"/>
  <path d="M-86-116h172v56h-172z" fill="#e6f0e8" class="o"/>
  {''.join(f'<rect x="{-20+i*22}" y="-100" width="14" height="24" rx="2" fill="{INK}"/>' for i in range(4))}
  {''.join(f'<rect x="{-86+(i%4)*46}" y="{-38+(i//4)*44}" width="34" height="32" rx="5" fill="#fffefd" stroke="{INK}" stroke-width="2.5"/>' for i in range(16))}</g>''')

add('calligraphy', '筆で紙の上に、なめらかな一筆の線が引かれる',
    '書道、美しい字を書く技術＝calligraphy。', f'''
{table(352)}
<g transform="translate(280 270)">
  <path d="M-170-90h340v180h-340z" class="paper"/>
  <path d="M-110 40q40-120 110-90t100 60" fill="none" stroke="{INK}" stroke-width="18" stroke-linecap="round"/>
  <path d="M-60-30q50 40 110 10" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/></g>
<g transform="translate(440 130) rotate(34)">
  <path d="M-10-110h20v140h-20z" fill="{BRN}" class="o"/>
  <path d="M-10 30q10 60 0 80-10-20 0-80z" class="ink"/></g>
<g transform="translate(120 260)"><ellipse rx="46" ry="20" fill="#2f3a4d" class="o"/></g>''')

add('canoe', '細長い舟にひとりが座り、両端に羽のあるパドルでこぐ',
    'カヌー＝canoe。', f'''
<path d="M0 260h600v140H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 272q22-14 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 270)">
  <path d="M-180 0q0 40 180 40t180-40q-60-24-180-24T-180 0z" class="coral o"/>
  <path d="M-150-4q150-18 300 0" fill="none" stroke="{CRLD}" stroke-width="4"/></g>
<g transform="translate(300 230)">{sit(0, 0, 0.9, 1, 'teal', 'blue', 'cap', 'smile', 'lap')}</g>
<g transform="translate(360 250) rotate(-34)">
  <path d="M-8-110h16v220h-16z" fill="{BRN}" class="o"/>
  <path d="M-26-140q26-20 52 0-6 34-26 40-20-6-26-40z" fill="#c9a464" class="o"/>
  <path d="M-26 140q26 20 52 0-6-34-26-40-20 6-26 40z" fill="#c9a464" class="o"/></g>''')

add('canteen', '職場の食堂で、カウンター越しに温かい食事が出される',
    '社員食堂、学校の食堂＝canteen。', f'''
{table(290)}
<g transform="translate(300 250)">
  <path d="M-220-40h440v40h-440z" fill="#c9a464" class="o"/></g>
{''.join(f'<g transform="translate({{}} 200)"><path d="M-40-16h80v32h-80z" fill="#c3cbd1" class="o"/><ellipse cy="-16" rx="34" ry="10" class="{{}}p o"/></g>'.format(180 + i * 100, c) for i, c in enumerate(['coral', 'green', 'gold']))}
{person(480, 250, 0.95, -1, 'violet', 'blue', 'give', 'bun', 'smile')}
{person(110, 340, 1.05, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
<g transform="translate(160 258)"><ellipse rx="40" ry="12" fill="#fffefd" class="o"/></g>''')

add('carousel', '木馬の並んだ回転木馬が、屋根の下でぐるりと回る',
    '回転木馬＝carousel。', f'''
<g transform="translate(300 260)">
  <path d="M-190 60h380v20h-380z" class="goldd o"/>
  <path d="M-200-60h400l-40-70h-320z" class="coral o"/>
  {''.join(f'<path d="M{-160+i*80} -60l-32 70h64z" fill="#fffefd" class="o"/>' for i in range(5))}
  <path d="M0-130v-30" stroke="{MUTED}" stroke-width="8" fill="none"/>
  {''.join(f'<path d="M{-150+i*100} -60v120" stroke="{GLDD}" stroke-width="9" fill="none"/>' for i in range(4))}
  {''.join(f'<g transform="translate({-150+i*100} 20)"><ellipse rx="34" ry="20" fill="#f0e6d2" class="o"/><circle cx="28" cy="-16" r="16" fill="#f0e6d2" class="o"/><path d="M-30 18l-6 24M30 18l6 24" stroke="#f0e6d2" stroke-width="9" fill="none"/></g>' for i in range(4))}</g>
<g transform="translate(300 60)"><path d="M-90 0a90 40 0 1 0 40-34" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9" marker-end="url(#ar)"/></g>''', arrow=True)

add('carrot', 'オレンジ色の細長い根に、緑の葉がついたニンジン',
    'ニンジン＝carrot。', f'''
{table(352)}
<g transform="translate(300 270) rotate(14)">
  <path d="M-46-100h92l-46 200z" fill="#e07a2a" class="o"/>
  {''.join(f'<path d="M{-34+i*22} {-70+i*14}l{20-i*4} 6" stroke="#b95f18" stroke-width="4" fill="none"/>' for i in range(4))}
  <path d="M-30-100q-20-60 0-80 14 34 14 80M0-100q0-70 14-86-4 44 4 86M30-100q20-56 40-70-20 28-24 70z" class="green o"/></g>''')

add('cart', '木の荷車に荷を積み、取っ手を持って引いていく',
    '荷車、手押し車＝cart。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(320 300)">
  <path d="M-140-60h280v60h-280z" fill="#c9a464" class="o"/>
  <path d="M-140-60v-20h280v20" fill="none" stroke="{BRN}" stroke-width="6"/>
  <circle cx="-80" cy="20" r="36" fill="none" stroke="{BRN}" stroke-width="10"/>
  <circle cx="80" cy="20" r="36" fill="none" stroke="{BRN}" stroke-width="10"/>
  <path d="M-140-40l-80-30" stroke="{BRN}" stroke-width="10" fill="none" stroke-linecap="round"/></g>
{''.join(f'<g transform="translate({{}} 210)"><path d="M-34-24h68v48h-68z" class="{{}} o"/></g>'.format(250 + i * 80, c) for i, c in enumerate(['gold', 'coral']))}
{person(110, 350, 1.0, 1, 'teal', 'blue', 'reach', 'cap', 'smile')}''')

add('carton', '屋根形の口がついた紙パックから、牛乳が注がれる',
    '紙パック、紙箱＝carton。', f'''
{table(352)}
<g transform="translate(230 250) rotate(-16)">
  <path d="M-60-70h120v150h-120z" fill="#fffefd" class="o"/>
  <path d="M-60-70l60-40 60 40z" fill="#dfeaf2" class="o"/>
  <path d="M-40-30h80v60h-80z" class="bluep o"/>
  <path d="M0-110v-14" stroke="{MUTED}" stroke-width="0"/></g>
{''.join(drop(330 + i * 8, 210 + i * 26, 1.1, 'blue') for i in range(2))}
<g transform="translate(400 300)">
  <path d="M-46-56l8 100h76l8-100z" fill="#fffefd" class="o"/>
  <path d="M-38 0h76l6 44h-88z" class="bluep"/>
  <path d="M-46-56l8 100h76l8-100z" fill="none" class="o"/></g>''')

add('cartridge', 'プリンターの差込口へ、インクのカートリッジを入れる',
    '(インクなどの)カートリッジ＝cartridge。', f'''
{table(352)}
<g transform="translate(300 290)">
  <path d="M-160-60h320v100h-320z" class="tealp o"/>
  <path d="M-120-60h240v-30h-240z" fill="#c3cbd1" class="o"/>
  <path d="M-60-90h120v20h-120z" fill="#fffefd" class="o"/></g>
<g transform="translate(300 150)">
  <path d="M-50-50h100v90h-100z" class="coral o"/>
  <path d="M-30 40h60v20h-60z" class="corald o"/>
  <path d="M-34-34h68v22h-68z" fill="#fffefd"/></g>
{line(300, 200, 300, 224, MUTED, True, 5)}''', arrow=True)

add('casserole', 'ふたつきの厚手の鍋で、肉と野菜がぐつぐつ煮えている',
    '煮込み料理、煮込み鍋＝casserole。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-130-40h260v70a30 30 0 0 1-30 30h-200a30 30 0 0 1-30-30z" class="coral o"/>
  <path d="M-160-40h320v-14h-320z" class="corald o"/>
  <path d="M-140-54q140-40 280 0" fill="#f2b0a4" class="o"/>
  <path d="M-24-94h48v40h-48z" class="corald o"/>
  <path d="M-160-20h-30v20h30M160-20h30v20h-30" fill="none" stroke="{CRLD}" stroke-width="12" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}q16-20 0-38" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(230 + i * 60, 180 - i * 12) for i in range(3))}''')

add('cellar', '家の下の地下室に、ワインの棚が並んでいる',
    '地下室、貯蔵室＝cellar。', f'''
<path d="M0 0h600v150H0z" class="ground"/>
<g transform="translate(300 150)">
  <path d="M-260 0h520v250h-520z" fill="#5f5346"/>
  <path d="M-230 20h460v210h-460z" fill="#3f3830"/></g>
<g transform="translate(300 250)">
  {''.join(f'<path d="M-180 {i*54}h360v10h-360z" fill="#8b6437"/>' for i in range(3))}
  {''.join(f'<g transform="translate({-150+ (i%6)*60} {(i//6)*54-14})"><path d="M-12-30h24v30h-24z" fill="#3a6b3a" stroke="{INK}" stroke-width="2"/><path d="M-5-44h10v14h-10z" fill="#3a6b3a" stroke="{INK}" stroke-width="2"/></g>' for i in range(12))}</g>
{''.join(f'<path d="M{{}} 120v30" stroke="{BRN}" stroke-width="8" fill="none"/>'.format(80 + i * 440) for i in range(2))}''')

add('cement', 'ミキサーから出したセメントを、こてで平らにならす',
    'セメント＝cement。', f'''
{table(352)}
<g transform="translate(320 290)">
  <path d="M-180-30h360v60h-360z" fill="#9aa7b1" class="o"/>
  <path d="M-180-30q90-16 180 0t180 0" fill="#b5bec4"/></g>
<g transform="translate(150 200)">
  <path d="M-50-60h100v80l-50 40-50-40z" fill="#c3cbd1" class="o"/>
  <path d="M-34-74h68v14h-68z" fill="#9aa7b1" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}l-8 22" fill="none" stroke="#9aa7b1" stroke-width="8" stroke-linecap="round"/>'.format(160 + i * 14, 240) for i in range(2))}
<g transform="translate(430 230) rotate(-16)">
  <path d="M-70-10h140v20h-140z" fill="#c3cbd1" class="o"/>
  <path d="M-10-34h20v24h-20z" fill="{BRN}" class="o"/>
  <path d="M-30-44h60v14h-60z" fill="{BRN}" class="o"/></g>''')

add('centipede', 'たくさんの足をもつ細長い虫が、床を走り抜ける',
    'ムカデ＝centipede。', f'''
{table(352)}
<g transform="translate(300 260)">
  {''.join(f'<ellipse cx="{-220+i*44}" cy="{math.sin(i*0.7)*22:.0f}" rx="26" ry="18" fill="#a2603a" stroke="{INK}" stroke-width="2.5"/>' for i in range(11))}
  {''.join(f'<path d="M{-220+i*44} {math.sin(i*0.7)*22-18:.0f}l-10-24M{-220+i*44} {math.sin(i*0.7)*22+18:.0f}l-10 24" stroke="#7a3f22" stroke-width="4" fill="none" stroke-linecap="round"/>' for i in range(11))}
  <circle cx="240" cy="{math.sin(10*0.7)*22:.0f}" r="20" fill="#8a4c2c" class="o"/>
  <path d="M256 -8l20-14M256 2l20 8" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/></g>''')

add('chandelier', '腕を広げた飾りの照明が、天井から吊り下がっている',
    'シャンデリア＝chandelier。', f'''
<path d="M0 0h600v40H0z" fill="#e4dccb"/>
<g transform="translate(300 40)">
  <path d="M0 0v70" stroke="{GLDD}" stroke-width="8" fill="none"/>
  <circle cy="80" r="20" class="gold o"/>
  {''.join(f'<path d="M0 92q{dx} 40 {dx*2} 56" fill="none" stroke="{GLDD}" stroke-width="7"/>' for dx in (-70, -34, 34, 70))}
  {''.join(f'<g transform="translate({dx*2} 148)"><path d="M-16 0h32l-6-40h-20z" class="goldp o"/><path d="M-6-40h12v-26h-12z" fill="#fffefd" class="o"/>{flame(0, -70, 0.2)}</g>' for dx in (-70, -34, 34, 70))}
  {''.join(f'<path d="M{-60+i*40} 110v40" stroke="{GLD}" stroke-width="3" fill="none"/><circle cx="{-60+i*40}" cy="158" r="8" class="goldp o"/>' for i in range(4))}</g>''')

add('cheese', '穴のあいた大きなチーズのかたまりが、切り分けられている',
    'チーズ＝cheese。', f'''
{table(352)}
<g transform="translate(260 270)">
  <path d="M-130 40l0-60 130-50v60z" fill="#e8c86a" class="o"/>
  <path d="M0-10l130 30v40L0 40z" fill="#d9b455" class="o"/>
  <path d="M-130-20l130-50 130 50-130 50z" fill="#f2dc8e" class="o"/>
  {''.join(f'<ellipse cx="{-70+i*54}" cy="{-16+(i%2)*22}" rx="14" ry="9" fill="#d9b455"/>' for i in range(4))}</g>
<g transform="translate(470 290) rotate(16)">
  <path d="M-50 30L0-40l50 70z" fill="#f2dc8e" class="o"/>
  <ellipse cx="0" cy="6" rx="12" ry="8" fill="#d9b455"/></g>''')

add('cheetah', '黒い点の模様をもつチーターが、草原を全速力で走る',
    'チーター＝cheetah。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<g transform="translate(300 260)">
  <path d="M-130 30q-30-60 20-80 90-34 180-10 60 16 58 50-2 34-56 38-100 12-202 2z" fill="#e0b862" class="o"/>
  <path d="M140-30q30-26 60-10 26 16 6 40-16 20-44 14z" fill="#e0b862" class="o"/>
  <path d="M190-16l34 6-32 14z" fill="#c89a44" class="o"/>
  <path d="M152-44l-6-28 26 18zM182-48l12-26 10 24z" fill="#e0b862" class="o"/>
  <circle cx="182" cy="-22" r="4" class="ink"/>
  <path d="M176-4l-14 20" stroke="{INK}" stroke-width="3" fill="none"/>
  {''.join(f'<circle cx="{-100+ (i%7)*40}" cy="{-20+(i//7)*30}" r="5" fill="#5b4030"/>' for i in range(14))}
  <path d="M-130 34l-20 56M-70 40l-14 52M30 44l-10 50M100 40l4 52" stroke="#e0b862" stroke-width="16" fill="none" stroke-linecap="round"/>
  <path d="M-130 10q-60-14-76-54 46 4 74 40z" fill="#e0b862" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}h50" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>'.format(40, 200 + i * 34) for i in range(3))}''')

add('chess', '白と黒のマスの盤の上に、駒が向かい合って並ぶ',
    'チェス＝chess。', f'''
{table(352)}
<g transform="translate(300 290)">
  <path d="M-180-70h360v90h-360z" fill="#c9a464" class="o"/>
  {''.join(f'<rect x="{-170+ (i%8)*42}" y="{-60+(i//8)*34}" width="42" height="34" fill="{"#f6efe1" if (i//8+i%8)%2 else "#5b4636"}"/>' for i in range(16))}
  <path d="M-180-70h360v90h-360z" fill="none" class="o"/></g>
{''.join(f'<g transform="translate({{}} 234)"><path d="M-16 20h32l-6-34h-20z" fill="{{}}" stroke="{INK}" stroke-width="2.5"/><circle cy="-22" r="12" fill="{{}}" stroke="{INK}" stroke-width="2.5"/></g>'.format(180 + i * 44, c, c) for i, c in enumerate(['#fffefd', '#fffefd', '#2f3542', '#2f3542']))}
<g transform="translate(420 214)">
  <path d="M-20 40h40l-8-50h-24z" fill="#2f3542" class="o"/>
  <path d="M-22-10h44l-6-30-10 10-6-16-6 16-10-10z" fill="#2f3542" class="o"/></g>''')

add('chestnut', 'いがの割れ目から、つやのある茶色の栗の実がのぞく',
    'クリ、クリの木＝chestnut。', f'''
{table(352)}
<g transform="translate(220 260)">
  <circle r="80" class="greenp o"/>
  {''.join(f'<path d="M0 0l{int(96*math.cos(math.radians(a)))} {int(96*math.sin(math.radians(a)))}" stroke="{GRND}" stroke-width="4" fill="none" stroke-linecap="round"/>' for a in range(0, 360, 20))}
  <path d="M-50 10q50 50 100 0-50-30-100 0z" fill="#8a5c2b" class="o"/></g>
<g transform="translate(430 290)">
  <path d="M-60 40q-20-70 20-92 20-12 40 0 40 22 20 92z" fill="#8a5c2b" class="o"/>
  <path d="M-40 40q40 16 80 0" fill="#c8a05f"/>
  <path d="M-60 40q-20-70 20-92 20-12 40 0 40 22 20 92z" fill="none" class="o"/>
  <path d="M-6-56h12v-18h-12z" fill="#5b4030"/></g>''')

add('chew', '口を動かして食べ物を何度もかみ、飲みこむ前にすりつぶす',
    'かむ、かみ砕く＝chew。', f'''
<g transform="translate(300 200)">
  <circle r="120" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-118-44q10-84 118-84t118 84q-50-38-118-26-66-12-118 26z" fill="{HAIR}"/>
  <path d="M-48-20l24 12M48-20l-24 12" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <ellipse cy="52" rx="46" ry="30" class="corald o"/>
  <path d="M-46 52q46-26 92 0" fill="none" stroke="{CRL}" stroke-width="4"/>
  {''.join(f'<circle cx="{-24+i*24}" cy="46" r="8" class="greenp o"/>' for i in range(3))}</g>
{''.join(f'<path d="M{440+i*22} {200+i*0}q16-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
<g transform="translate(300 60)"><path d="M-50 0q50-30 100 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/></g>''', arrow=True)

add('chick', '黄色い羽毛のひよこが、割れた卵のそばで口を開ける',
    'ひな、ひよこ＝chick。', f'''
{table(352)}
<g transform="translate(330 280)">
  <ellipse rx="70" ry="60" class="gold o"/>
  <circle cx="0" cy="-68" r="44" class="gold o"/>
  <path d="M36-72l30 10-30 12z" class="corald o"/>
  <circle cx="16" cy="-82" r="5" class="ink"/>
  <path d="M-20 50v20M20 50v20" stroke="{GLDD}" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M-60 10q-30 10-30 34 26-4 40-20z" class="goldd o"/></g>
<g transform="translate(160 300)">
  <path d="M-50 30q-16-60 20-70 30-8 44 14-40 10-64 56z" fill="#fffefd" class="o"/>
  <path d="M-50 30q40 22 84-6-20-30-44-40z" fill="#fffefd" class="o"/></g>''')

add('chilly', '肌寒い朝、上着の前を合わせて白い息を吐く',
    '肌寒い＝chilly。', f'''
<path d="M0 300h600v100H0z" fill="#eef4f7"/>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#ffffff" stroke="{MUTED}" stroke-width="1.2"/>'.format(60 + (i * 79) % 480, 60 + (i * 47) % 200) for i in range(10))}
{person(260, 340, 1.4, 1, 'coral', 'blue', 'hold', 'cap', 'flat')}
<g transform="translate(330 210)">
  <path d="M0 0q40-18 60 4 22 24-6 32-40 8-54-36z" fill="#fffefd" opacity="0.85" stroke="{MUTED}" stroke-width="2.5"/></g>
{''.join(f'<path d="M{{}} {{}}q14-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(480 + i * 22, 200 - i * 14) for i in range(2))}
{bare_tree_placeholder if False else ''}''')

add('chisel', 'のみの刃を木に当て、木づちでたたいて削る',
    'のみ、たがね＝chisel。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-200-30h400v40h-400z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-160+i*80} -26q40 12 0 26" fill="none" stroke="#a0764a" stroke-width="3"/>' for i in range(5))}</g>
<g transform="translate(300 210) rotate(10)">
  <path d="M-16-90h32v90h-32z" fill="{BRN}" class="o"/>
  <path d="M-12 0h24v60l-12 20-12-20z" fill="#c3cbd1" class="o"/></g>
<g transform="translate(200 120) rotate(-24)">
  <path d="M-12 0h24v100h-24z" fill="{BRN}" class="o"/>
  <path d="M-44-40h88v40h-88z" fill="#a0764a" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{GLD}" stroke-width="5"/>'.format(370 + i * 18, 190 - i * 14) for i in range(2))}''')

add('chopsticks', '二本のはしが手の中で組まれ、食べ物をつまむ',
    'はし＝chopsticks。', f'''
{table(352)}
<g transform="translate(300 250) rotate(-20)">
  <path d="M-160-14h320l-8 10h-312z" fill="#c9a464" class="o"/>
  <path d="M-160 14h320l-8-10h-312z" fill="#c9a464" class="o"/></g>
<g transform="translate(430 214)"><circle r="18" class="coral o"/></g>
{hand(180, 300, 1)}
<g transform="translate(300 320)">
  <ellipse rx="90" ry="24" fill="#fffefd" class="o"/>
  {''.join(f'<ellipse cx="{-40+i*40}" cy="-8" rx="20" ry="10" fill="#f2f6f8" stroke="{INK}" stroke-width="2"/>' for i in range(3))}</g>''')

add('clamp', '万力が二枚の板を上下から挟み、ねじで締めつけている',
    '締め具、万力＝clamp。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-140-30h280v30h-280z" fill="#c9a464" class="o"/>
  <path d="M-140 0h280v30h-280z" fill="#a0764a" class="o"/></g>
<g transform="translate(300 260)">
  <path d="M-70-90h20v190h-20z" fill="{MUTED}" class="o"/>
  <path d="M-70-90h150v22h-150z" fill="{MUTED}" class="o"/>
  <path d="M-70 78h150v22h-150z" fill="{MUTED}" class="o"/>
  <path d="M66-68h24v36H66z" fill="{MUTED}" class="o"/>
  <path d="M78-32v22" stroke="{MUTED}" stroke-width="12" fill="none"/>
  <circle cx="78" cy="-86" r="22" fill="none" stroke="{MUTED}" stroke-width="10"/></g>
{''.join(f'<path d="M{{}} 236v-24" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(200 + i * 80) for i in range(2))}''', arrow=True)

add('clasp', 'ネックレスの両端についた留め金が、かちりとかみ合う',
    '留め金＝clasp。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-200 0q60 80 200 80t200-80" fill="none" stroke="{GLD}" stroke-width="8"/>
  {''.join(f'<circle cx="{-170+i*44}" cy="{22+abs(i-4)*-4+20}" r="9" class="goldp o"/>' for i in range(9))}</g>
<g transform="translate(300 180)">
  <path d="M-60-16h50v32h-50z" class="goldd o"/>
  <path d="M10-16h50v32H10z" class="goldd o"/>
  <path d="M-10-8h20v16h-20z" class="gold o"/></g>
{ring(300, 180, 60, True)}''')

add('classmate', '同じ教室の机に並んで座る、同い年の友だち',
    '同級生、クラスメート＝classmate。', f'''
<g transform="translate(300 200)"><path d="M-260-160h520v320h-520z" fill="#f6efe1" class="o"/></g>
{''.join(f'<g transform="translate({{}} 320)"><path d="M-60-40h120v16h-120z" fill="#c9a464" class="o"/><path d="M-50-24v40M50-24v40" stroke="{BRN}" stroke-width="8" fill="none"/></g>'.format(180 + i * 240) for i in range(2))}
{sit(180, 290, 1.0, 1, 'teal', 'blue', 'short', 'smile', 'lap')}
{sit(420, 290, 1.0, 1, 'coral', 'green', 'bob', 'smile', 'lap')}
{''.join(chair(174 + i * 240, 290, 0.9, 'gold', 1) for i in range(2))}
<path d="M240 180h120" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('classroom', '黒板と机の並んだ教室で、先生が前に立つ',
    '教室＝classroom。', f'''
<g transform="translate(300 200)"><path d="M-260-160h520v320h-520z" fill="#f6efe1" class="o"/></g>
<g transform="translate(300 120)">
  <path d="M-180-70h360v140h-360z" fill="#2f5a45" class="o"/>
  {''.join(f'<rect x="-150" y="{-40+i*30}" width="{240-(i%2)*70}" height="9" rx="4.5" fill="#e6f0e8"/>' for i in range(3))}</g>
{''.join(f'<g transform="translate({{}} 330)"><path d="M-54-36h108v14h-108z" fill="#c9a464" class="o"/><path d="M-44-22v36M44-22v36" stroke="{BRN}" stroke-width="7" fill="none"/></g>'.format(150 + i * 150) for i in range(3))}
{''.join(head(150 + i * 150, 274, 24, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('coral', 'bob'), ('green', 'bun')]))}
{person(530, 330, 0.95, -1, 'violet', 'blue', 'point', 'bun', 'smile')}''')

add('clay', '手で押した粘土のかたまりに、指の跡が残っている',
    '粘土＝clay。', f'''
{table(352)}
<g transform="translate(300 290)">
  <path d="M-130 40q-30-70 20-100 60-36 130-10 60 22 44 84-10 30-64 30z" fill="#a2825e" class="o"/>
  {''.join(f'<ellipse cx="{-50+i*44}" cy="{-6+(i%2)*16}" rx="16" ry="20" fill="#8a6a46"/>' for i in range(3))}</g>
{hand(300, 150, 1)}
{line(300, 200, 300, 224, MUTED, True, 4)}
<g transform="translate(490 250)">
  <path d="M-40 40q-14-50 10-60 20-8 34 4 20 14 6 56z" fill="#a2825e" class="o"/></g>''', arrow=True)

add('cloakroom', '番号のついた札を渡し、上着を預けて棚に掛けてもらう',
    'クローク、携帯品預かり所＝cloakroom。', f'''
{table(290)}
<g transform="translate(400 200)">
  <path d="M-160-100h320v10h-320z" fill="{MUTED}" class="o"/>
  {''.join(f'<g transform="translate({-120+i*70} -90)"><path d="M0 0v16" stroke="{MUTED}" stroke-width="4" fill="none"/><path d="M-30 16h60l-6 20h-48z" fill="{c}" stroke="{INK}" stroke-width="2.5"/><path d="M-34 36h68l10 70h-88z" fill="{c}" stroke="{INK}" stroke-width="2.5"/></g>' for i, c in enumerate(['#238b83', '#e86452', '#4e86c6', '#816eb2']))}</g>
{person(130, 340, 1.1, 1, 'coral', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(210 240) rotate(-8)">
  <path d="M-26-18h52v36h-52z" class="goldp o"/>
  <circle cx="0" cy="0" r="8" fill="{GLDD}"/></g>''')

add('cobweb', '部屋の隅に張られた古いクモの巣に、ほこりが積もる',
    'クモの巣＝cobweb。', f'''
<g transform="translate(300 200)"><path d="M-260-160h520v320h-520z" fill="#e4dccb" class="o"/></g>
<path d="M60 60L60 60" fill="none"/>
<g transform="translate(70 70)">
  {''.join(f'<path d="M0 0L{int(240*math.cos(math.radians(a)))} {int(240*math.sin(math.radians(a)))}" stroke="{MUTED}" stroke-width="2.5" fill="none"/>' for a in (0, 18, 36, 54, 72, 90))}
  {''.join(f'<path d="M{int(r*math.cos(0))} 0Q{int(r*0.78)} {int(r*0.78)} 0 {r}" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for r in (60, 110, 165, 225))}</g>
<g transform="translate(230 220)">
  <ellipse rx="20" ry="15" fill="#4a4238" class="o"/><circle cx="-18" cy="-4" r="10" fill="#4a4238" class="o"/>
  {''.join(f'<path d="M{-6+i*6} -12q{-20+i*10}-24 {-34+i*16}-30" stroke="#4a4238" stroke-width="3" fill="none"/>' for i in range(3))}
  {''.join(f'<path d="M{-6+i*6} 12q{-20+i*10} 24 {-34+i*16} 30" stroke="#4a4238" stroke-width="3" fill="none"/>' for i in range(3))}</g>''')

add('cockpit', '前が窓になった操縦室に、計器と操縦かんが並ぶ',
    '操縦室、コックピット＝cockpit。', f'''
<g transform="translate(300 200)">
  <path d="M-260-160h520v320h-520z" fill="#dfe6ea" class="o"/>
  <path d="M-220-130h440v120h-440z" fill="#cfe4f0" class="o"/>
  <path d="M-60-130v120M60-130v120" stroke="{INK}" stroke-width="5" fill="none"/>
  <path d="M-220 20h440v70h-440z" fill="#6b7680" class="o"/>
  {''.join(f'<circle cx="{-170+i*70}" cy="55" r="22" fill="#2f3a4d" stroke="{INK}" stroke-width="2.5"/><path d="M{-170+i*70} 55l12-14" stroke="#9aa7b1" stroke-width="3" fill="none"/>' for i in range(6))}
  <path d="M-110 90v50M110 90v50" stroke="{INK}" stroke-width="10" fill="none"/>
  <path d="M-140 140h60M80 140h60" stroke="{INK}" stroke-width="10" fill="none" stroke-linecap="round"/></g>''')

add('colander', '穴のあいた器にパスタを上げ、湯が下へ落ちる',
    '水切りボウル、ざる＝colander。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M-120-30q0 110 120 110t120-110z" fill="#c3cbd1" class="o"/>
  <ellipse cy="-30" rx="120" ry="30" fill="#dfe6ea" class="o"/>
  {''.join(f'<circle cx="{-70+ (i%5)*36}" cy="{10+(i//5)*30}" r="7" fill="#fffaf1"/>' for i in range(12))}
  <path d="M-120-30h-30v14h30M120-30h30v14h-30" fill="none" stroke="#9aa7b1" stroke-width="10"/>
  {''.join(f'<path d="M{-70+i*26} -34q26-14 40 0" fill="none" stroke="#e8d2a8" stroke-width="8" stroke-linecap="round"/>' for i in range(4))}</g>
{''.join(drop(250 + i * 50, 340, 0.9, 'blue') for i in range(3))}''')

add('compass', '円い文字盤の中で、赤い針が北を指している',
    '方位磁石、コンパス＝compass。', f'''
{table(352)}
<g transform="translate(300 230)">
  <circle r="130" fill="#c9a464" class="o"/>
  <circle r="112" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M0-100v-14" transform="rotate({a})" stroke="{MUTED}" stroke-width="4" fill="none"/>' for a in range(0, 360, 30))}
  {''.join(f'<path d="M0-96v-22" transform="rotate({a})" stroke="{INK}" stroke-width="6" fill="none"/>' for a in (0, 90, 180, 270))}
  <path d="M0-84L22 0 0 22-22 0z" class="coral o"/>
  <path d="M0 84L22 0h-44z" fill="#fffefd" class="o"/>
  <circle r="10" class="ink"/></g>''')

add('compost', '庭の隅の堆肥の山に、野菜くずと落ち葉が積まれている',
    '堆肥＝compost。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<g transform="translate(320 300)">
  <path d="M-150 0q-10-90 60-110 90-26 150 20 50 38 20 90z" fill="#5b4636" class="o"/>
  {''.join(f'<ellipse cx="{-90+ (i%5)*46}" cy="{-40-(i//5)*30}" rx="18" ry="10" fill="{c}" stroke="{INK}" stroke-width="2" transform="rotate({-20+i*14} {-90+(i%5)*46} {-40-(i//5)*30})"/>' for i, c in enumerate(['#4e986a', '#d99a2b', '#e86452', '#4e986a', '#a66b15', '#4e986a', '#d99a2b', '#8b6437']))}</g>
<g transform="translate(120 330)">
  <path d="M-40-60h80v60h-80z" fill="{GRNP}" class="o"/></g>
{''.join(f'<path d="M{{}} 210q10-14 0-26" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(480 + i * 20) for i in range(2))}''')

add('cone', 'とがった先を上にした円すいの形が、影とともに置かれる',
    '円すい、コーン＝cone。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<g transform="translate(220 320)">
  <path d="M-90 0L0-200 90 0z" class="coral o"/>
  <ellipse cy="0" rx="90" ry="24" class="corald o"/>
  <path d="M-56-124h112v26h-112z" fill="#fffefd"/></g>
<g transform="translate(450 300)">
  <path d="M-50 0L0-110 50 0z" class="goldp o"/>
  <ellipse cy="0" rx="50" ry="14" class="gold o"/>
  <circle cy="-124" r="34" fill="#fffefd" class="o"/></g>''')

add('confetti', '色とりどりの小さな紙片が、上から舞い落ちる',
    '紙吹雪＝confetti。', f'''
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-11" y="-7" width="22" height="14" rx="2" fill="{{}}"/></g>'.format(50 + (i * 67) % 520, 40 + (i * 43) % 280, (i * 37) % 180, c) for i, c in enumerate(['#e86452','#d99a2b','#4e86c6','#4e986a','#816eb2','#238b83']*5))}
{person(240, 350, 1.15, 1, 'teal', 'blue', 'up', 'bob', 'smile')}
{person(380, 350, 1.15, -1, 'coral', 'green', 'up', 'short', 'smile')}''')

add('cookbook', '開いた料理本に、写真つきの手順が載っている',
    '料理の本＝cookbook。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-170-90h160v180h-160zM10-90h160v180H10z" class="paper"/>
  <path d="M-14-96h28v192h-28z" class="corald o"/>
  <path d="M-150-66h116v66h-116z" class="goldp o"/>
  <circle cx="-92" cy="-34" r="22" class="coral o"/>
  {''.join(f'<rect x="-150" y="{12+i*22}" width="{116-(i%2)*34}" height="9" rx="4.5" fill="{MUTED}"/>' for i in range(3))}
  {''.join(f'<g><circle cx="34" cy="{-56+i*32}" r="9" class="teal"/><rect x="54" y="{-64+i*32}" width="{96-(i%3)*24}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(5))}</g>''')

finish(__file__)
