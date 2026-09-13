# -*- coding: utf-8 -*-
"""第187回。plus35 の50語。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('locker', '番号のついた細長いロッカーが並び、一つだけ扉が開いている',
    'ロッカー＝locker。', f'''
{''.join(f'<g transform="translate({{}} 220)"><path d="M-60-160h120v320h-120z" class="tealp o"/><path d="M-40-130h80v30h-80z" fill="#9aa7b1"/><circle cx="40" cy="0" r="9" class="goldp o"/></g>'.format(110 + i * 130) for i in range(3))}
<g transform="translate(500 220)">
  <path d="M-60-160h120v320h-120z" fill="#d8e6e2" class="o"/>
  <path d="M-60-160l-70 30v260l70 30z" class="teal o"/>
  <path d="M-40-100h80v70h-80z" fill="#fffefd" class="o"/>
  <path d="M-40 20h80v40h-80z" fill="{BRN}" class="o"/></g>''')

add('locket', 'ふたの開いた小さな飾りの中に、写真がおさまっている',
    'ロケット(写真などを入れる小さな飾り)＝locket。', f'''
{table(352)}
<g transform="translate(300 200)">
  <path d="M-160 0q160 100 320 0" fill="none" stroke="{GLD}" stroke-width="6"/>
  {''.join(f'<circle cx="{-140+i*40}" cy="{abs(math.sin(i/7*math.pi))*62:.0f}" r="7" class="gold o"/>' for i in range(8))}</g>
<g transform="translate(250 280)">
  <circle r="54" class="gold o"/>
  <circle r="38" class="goldp o"/>
  {head(0, 4, 22, 'coral', 'bob')}</g>
<g transform="translate(360 272) rotate(20)">
  <circle r="54" class="gold o"/>
  <circle r="38" fill="none" stroke="{GLDD}" stroke-width="4"/></g>''')

add('loft', '屋根裏のはしごを上ると、古い箱がしまわれている',
    '屋根裏、ロフト＝loft。', f'''
<g transform="translate(300 200)">
  <path d="M-260 40L0-160l260 200z" fill="#e8ddc9" class="o"/>
  <path d="M-200 40h400v160h-400z" fill="#f6efe1" class="o"/>
  <path d="M-90 40h180v20h-180z" fill="#2f2620" class="o"/></g>
{''.join(box(200 + i * 80, 210, 70, 46, 16, 'gold') for i in range(2))}
<g transform="translate(300 330)">
  <path d="M-26-70v130M26-70v130" stroke="{BRN}" stroke-width="9" fill="none"/>
  {''.join(f'<path d="M-26 {-50+i*34}h52" stroke="{BRN}" stroke-width="7" fill="none"/>' for i in range(4))}</g>''')

add('lollipop', '棒の先に丸い渦巻き模様のあめがついている',
    '棒つきキャンディー＝lollipop。', f'''
{table(352)}
<g transform="translate(300 220)">
  <circle r="90" fill="#fffefd" class="o"/>
  <path d="M0 0a20 20 0 1 1 18 12 46 46 0 1 1-58-20 76 76 0 1 1 118 42" fill="none" stroke="{CRL}" stroke-width="18" stroke-linecap="round"/>
  <path d="M-8 90h16v110h-16z" fill="#f0e6d2" class="o"/></g>''')

add('loudspeaker', '天井のスピーカーから、案内の音が波になって広がる',
    'スピーカー、拡声器＝loudspeaker。', f'''
<path d="M0 0h600v50H0z" fill="#e4dccb"/>
<g transform="translate(230 160)">
  <path d="M-50-90h100v180h-100z" fill="#6b7680" class="o"/>
  <path d="M50-60l90-50v220l-90-50z" fill="#8a97a3" class="o"/>
  <path d="M0-90v-60" stroke="{MUTED}" stroke-width="7" fill="none"/></g>
{''.join(f'<path d="M400 160a{{}} {{}} 0 0 1 0 0" fill="none"/>'.format(0, 0) for _ in range(0))}
{''.join(f'<path d="M380 {{}}a{{}} {{}} 0 0 1 0 {{}}" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>'.format(160 - 30 - i * 26, 30 + i * 26, 30 + i * 26, 60 + i * 52) for i in range(3))}
{''.join(head(160 + i * 140, 330, 26, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('coral', 'bob'), ('green', 'bun')]))}''')

add('lounge', 'ソファとテーブルのあるくつろぎの部屋で、人が腰かける',
    '居間、ラウンジ＝lounge。', f'''
<g transform="translate(300 200)"><path d="M-280-160h560v320h-560z" fill="#f6efe1" class="o"/></g>
<g transform="translate(260 320)">
  <path d="M-140-50h280v50h-280z" class="violet o"/>
  <path d="M-140-50v-50h280v50" fill="{VIOD}" class="o"/>
  <path d="M-160-60h30v60h-30zM130-60h30v60h-30z" class="violetd o"/>
  <path d="M-130-100v40M130-100v40" stroke="{VIOD}" stroke-width="0" fill="none"/></g>
{sit(260, 300, 1.0, 1, 'coral', 'blue', 'bob', 'smile', 'lap')}
<g transform="translate(480 320)">
  <path d="M-60-40h120v14h-120z" fill="#c9a464" class="o"/>
  <path d="M-46-26v26M46-26v26" stroke="{BRN}" stroke-width="7" fill="none"/>
  <path d="M-20-56h40v16h-40z" class="tealp o"/></g>''')

add('lunch', '昼の食卓に、サンドイッチと果物と飲み物が並ぶ',
    '昼食＝lunch。', f'''
{table(300)}
<g transform="translate(220 286)">
  <ellipse rx="90" ry="24" fill="#fffefd" class="o"/>
  <path d="M-50-40h100l-50 40z" fill="#e0b872" class="o"/>
  <path d="M-40-26h80" stroke="#4e986a" stroke-width="7" fill="none"/></g>
<g transform="translate(400 268)">
  <path d="M-40-60l8 116h64l8-116z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-34-10h68l6 66h-80z" class="bluep"/></g>
<g transform="translate(500 292)"><circle r="26" class="coral o"/><path d="M0-26v-12" stroke="{GRND}" stroke-width="4" fill="none"/></g>
{clock(110, 130, 38, 12, 20)}''')

add('mailbox', '家の前に立つ郵便受けの扉から、手紙がのぞく',
    '郵便受け、郵便ポスト＝mailbox。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(300 330)">
  <path d="M-12 0v-150h24V0z" fill="{BRN}" class="o"/>
  <path d="M-90-260h180v70h-180z" class="bluep o"/>
  <path d="M-90-260q90-50 180 0" fill="#a8c8e0" class="o"/>
  <path d="M-90-190h180v40h-180z" class="blue o"/>
  <path d="M90-240l30-20v40z" class="coral o"/></g>
<g transform="translate(280 194) rotate(-12)">
  <path d="M-40-24h80v48h-80z" class="paper"/>
  <path d="M-40-24l40 26 40-26" fill="none" stroke="{MUTED}" stroke-width="3"/></g>''')

add('mallet', '頭が木でできたつちで、木のくいを打ちこむ',
    '木づち＝mallet。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-200-20h400v40h-400z" fill="#c9a464" class="o"/></g>
<g transform="translate(330 270)">
  <path d="M-14-70h28v70h-28z" fill="#a0764a" class="o"/>
  <path d="M-24 0h48v40h-48z" fill="#8b6437" class="o"/></g>
<g transform="translate(220 180) rotate(-28)">
  <path d="M-12 0h24v130h-24z" fill="{BRN}" class="o"/>
  <path d="M-50-50h100v50h-100z" fill="#c9a464" class="o"/>
  <path d="M-50-50h100v14h-100z" fill="#a0764a"/></g>
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{GLD}" stroke-width="5"/>'.format(390 + i * 18, 230 - i * 14) for i in range(2))}''')

add('mantelpiece', '暖炉の上に渡した棚に、時計と写真立てが並ぶ',
    '暖炉の上の棚、マントルピース＝mantelpiece。', f'''
<g transform="translate(300 300)">
  <path d="M-180-60h360v160h-360z" fill="#b5a894" class="o"/>
  <path d="M-110-20h220v120h-220z" fill="#2f2620" class="o"/>
  {flame(-30, 90, 0.45)}{flame(30, 90, 0.4)}
  <path d="M-210-90h420v34h-420z" fill="#c9a464" class="o"/></g>
{clock(300, 178, 34, 10, 10)}
{''.join(f'<g transform="translate({{}} 184)"><path d="M-30-40h60v72h-60z" class="paper"/>{{}}</g>'.format(180 + i * 240, head(0, -6, 16, c, h)) for i, (c, h) in enumerate([('coral', 'bob'), ('teal', 'short')]))}''')

add('marble', '磨いた石の模様のある床の上に、ガラスのビー玉が転がる',
    '大理石、ビー玉＝marble。', f'''
<g transform="translate(300 250)">
  <path d="M-280-100h560v200h-560z" fill="#f2efe8" class="o"/>
  {''.join(f'<path d="M{-260+i*46} -100q20 60-10 100t10 100" fill="none" stroke="#d8d2c4" stroke-width="5"/>' for i in range(12))}
  {''.join(f'<path d="M-280 {-60+i*70}h560" stroke="#e2ddd2" stroke-width="4" fill="none"/>' for i in range(3))}</g>
{''.join(f'<g transform="translate({{}} {{}})"><circle r="24" fill="#cfe4f0" stroke="{INK}" stroke-width="2.5"/><path d="M-14 4q14-22 28 0" fill="none" stroke="{{}}" stroke-width="9"/></g>'.format(200 + i * 90, 290 + (i % 2) * 20, c) for i, c in enumerate(['#e86452', '#4e986a', '#d99a2b']))}''')

add('mascara', 'ブラシのついた細い容器で、まつげを塗る',
    'マスカラ＝mascara。', f'''
{table(352)}
<g transform="translate(200 260)">
  <path d="M-26-90h52v150a22 22 0 0 1-22 22h-8a22 22 0 0 1-22-22z" fill="#2f3542" class="o"/>
  <path d="M-16-112h32v22h-32z" fill="#4e5a66" class="o"/></g>
<g transform="translate(320 180) rotate(30)">
  <path d="M-6-70h12v70h-12z" fill="#2f3542" class="o"/>
  <path d="M-12 0h24v70h-24z" fill="#1f2a38" class="o"/>
  {''.join(f'<path d="M-12 {8+i*14}h-8M12 {8+i*14}h8" stroke="#1f2a38" stroke-width="4" fill="none"/>' for i in range(4))}</g>
<g transform="translate(470 250)">
  <path d="M-60 0q60-46 120 0-60 40-120 0z" fill="#fffefd" class="o"/>
  <circle r="20" class="teal o"/><circle r="9" class="ink"/>
  {''.join(f'<path d="M{-50+i*25} -14q-4-24 6-34" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>' for i in range(5))}</g>''')

add('mast', '帆船の中央に高い柱が立ち、帆が張られている',
    '(船の)マスト、帆柱＝mast。', f'''
<path d="M0 290h600v110H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 306q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 290)">
  <path d="M-150 0h300l-34 50h-232z" class="coral o"/>
  <path d="M-10-260h20v260h-20z" fill="{BRN}" class="o"/>
  <path d="M-80-200h160v12h-160z" fill="{BRN}" class="o"/>
  <path d="M10-240h120l-30 40 30 40H10z" fill="#f6efe1" class="o"/>
  <path d="M-10-190q-90 40-110 130h110z" fill="#f6efe1" class="o"/></g>
{ring(300, 150, 0, True)}''')

add('matchbox', '引き出した小箱の中にマッチ棒が並び、一本に火がつく',
    'マッチ箱＝matchbox。', f'''
{table(352)}
<g transform="translate(280 290)">
  <path d="M-110-40h220v70h-220z" class="coral o"/>
  <path d="M-110-40h220v14h-220z" class="corald o"/>
  <path d="M-80-24h160v54h-160z" fill="#f0e6d2" class="o"/>
  {''.join(f'<path d="M{-60+i*26} -18h8v44h-8z" fill="#e0c48c" stroke="{INK}" stroke-width="1.5"/><circle cx="{-56+i*26}" cy="-22" r="5" class="corald"/>' for i in range(5))}</g>
<g transform="translate(420 200) rotate(30)">
  <path d="M-5-70h10v110h-5z" fill="#e0c48c" class="o"/>
  <path d="M-5-70h10v110h-10z" fill="#e0c48c" class="o"/>
  {flame(0, -76, 0.26)}</g>''')

add('meal', '一日の食事が三つ並び、それぞれ量と時刻が違う',
    '食事＝meal。', f'''
{table(330)}
{''.join(f'<g transform="translate({{}} 312)"><ellipse rx="{{}}" ry="{{}}" fill="#fffefd" class="o"/><ellipse cy="-8" rx="{{}}" ry="{{}}" class="{{}}p o"/></g>'.format(x, r, r * 0.28, r * 0.6, r * 0.17, c) for x, r, c in [(140, 70, 'gold'), (300, 84, 'coral'), (460, 76, 'green')])}
{''.join(clock(140 + i * 160, 150, 34, h, 0) for i, h in enumerate([7, 12, 7]))}''')

add('mincer', 'ハンドルを回すひき肉器から、細かくなった肉が出る',
    'ひき肉器、ミンサー＝mincer。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-40-100h120v50h-120z" fill="#c3cbd1" class="o"/>
  <path d="M-30-50h100v110h-100z" fill="#c3cbd1" class="o"/>
  <path d="M-30 0h-90v50h90z" fill="#c3cbd1" class="o"/>
  <path d="M-120 10h-30v30h30z" fill="#9aa7b1" class="o"/>
  <path d="M80 10h40v30H80z" fill="#9aa7b1" class="o"/>
  <path d="M120 25h50" stroke="#9aa7b1" stroke-width="10" fill="none"/>
  <circle cx="170" cy="25" r="16" fill="{BRN}" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q-14 20 0 40" fill="none" stroke="#c96a5a" stroke-width="9" stroke-linecap="round"/>'.format(160 - i * 14, 290) for i in range(3))}
<g transform="translate(300 130)"><path d="M-40-16h80v32h-80z" fill="#c96a5a" class="o"/></g>''')

add('mitten', '親指だけが分かれた毛糸の手袋が、二つ並ぶ',
    'ミトン、親指だけ分かれた手袋＝mitten。', f'''
{table(352)}
{''.join(f'<g transform="translate({{}} 250) rotate({{}})"><path d="M-44-60q44-24 88 0 14 90 0 120h-88q-14-30 0-120z" class="coral o"/><path d="M-44-20q-34 0-34 30t34 24" fill="{CRL}" stroke="{INK}" stroke-width="2.5"/><path d="M-46 40h92v20h-92z" class="corald o"/>{{}}</g>'.format(x, r, ''.join(f'<path d="M{-30+j*20} -40q10 20 0 40" fill="none" stroke="{CRLD}" stroke-width="3"/>' for j in range(4))) for x, r in [(200, -8), (400, 8)])}''')

add('mixer', '羽根のついた電動ミキサーで、ボウルの中の卵を泡立てる',
    'ミキサー、泡立て器具＝mixer。', f'''
{table(352)}
<g transform="translate(320 300)">
  <path d="M-90-30q0 60 90 60t90-60z" fill="#dfe6ea" class="o"/>
  <ellipse cy="-30" rx="90" ry="26" fill="#dfe6ea" class="o"/>
  <ellipse cy="-28" rx="70" ry="18" fill="#fdf3c8"/></g>
<g transform="translate(300 180) rotate(-14)">
  <path d="M-70-50h140v70h-140z" class="teal o"/>
  <path d="M70-30h50v30H70z" fill="{TEAD}" class="o"/>
  {''.join(f'<path d="M{-40+i*40} 20q-12 50 0 80" fill="none" stroke="#c3cbd1" stroke-width="7"/>' for i in range(3))}</g>
{''.join(f'<path d="M{{}} {{}}q14-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(450 + i * 20, 200 - i * 14) for i in range(2))}''')

add('moat', '城の周りを一周する水の堀に、はね橋が架かる',
    '堀、外堀＝moat。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<path d="M0 300q140-60 300-60t300 60v40H0z" class="bluep o"/>
<g transform="translate(300 250)">
  <path d="M-120 0v-110h240V0z" fill="#e8ddc9" class="o"/>
  <path d="M-120-110v-30h30v-20h30v20h30v-20h30v20h30v-20h30v20h30v30z" fill="#e8ddc9" class="o"/>
  <path d="M-30 0v-64h60V0z" class="corald o"/></g>
<g transform="translate(300 300)">
  <path d="M-60-6h120v16h-120z" fill="{BRN}" class="o"/></g>
{''.join(f'<path d="M{{}} 330q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(60 + i * 120) for i in range(4))}''')

add('moose', '幅の広い角をもつヘラジカが、森のはずれに立つ',
    'ヘラジカ＝moose。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
{tree(90, 330, 0.9)}{tree(530, 330, 0.8)}
<g transform="translate(300 250)">
  <ellipse rx="120" ry="66" fill="#6b4a30" class="o"/>
  <path d="M100-40q30-60 66-40 26 16 6 56-14 26-44 24z" fill="#6b4a30" class="o"/>
  <path d="M128-84q-40-30-24-60 30 14 40 42zM176-88q40-30 24-60-30 14-40 42z" fill="#c8a05f" class="o"/>
  <circle cx="150" cy="-46" r="5" class="ink"/>
  <ellipse cx="176" cy="-20" rx="16" ry="12" fill="#4a3420"/>
  <path d="M136 20q0 30-14 44" fill="none" stroke="#6b4a30" stroke-width="10" stroke-linecap="round"/>
  <path d="M-80 60v50M-20 64v46M40 64v46M92 58v52" stroke="#6b4a30" stroke-width="17" fill="none" stroke-linecap="round"/></g>''')

add('mosaic', '小さな色タイルを寄せて、一枚の模様を作っている',
    'モザイク＝mosaic。', f'''
<g transform="translate(300 210)">
  <path d="M-230-140h460v280h-460z" fill="#e8ddc9" class="o"/>
  {''.join(f'<rect x="{-216+ (i%22)*20}" y="{-126+(i//22)*20}" width="16" height="16" rx="2" fill="{c}"/>' for i, c in enumerate(['#238b83','#dff4ef','#e86452','#fde9e3','#d99a2b','#fff0c5','#4e86c6','#816eb2','#4e986a','#238b83','#e86452']*30))}
  <g><circle r="70" fill="none" stroke="#fffefd" stroke-width="0"/></g>
  {''.join(f'<rect x="{int(-8+62*math.cos(math.radians(a)))}" y="{int(-8+62*math.sin(math.radians(a)))}" width="16" height="16" rx="2" fill="#fffefd"/>' for a in range(0, 360, 15))}
  <path d="M-230-140h460v280h-460z" fill="none" class="o"/></g>''')

add('motorbike', 'エンジンのついた二輪車が、スタンドを立てて停まる',
    'オートバイ＝motorbike。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(300 290)">
  <circle cx="-130" cy="50" r="56" class="ink"/>
  <circle cx="130" cy="50" r="56" class="ink"/>
  <circle cx="-130" cy="50" r="24" fill="#9aa7b1"/>
  <circle cx="130" cy="50" r="24" fill="#9aa7b1"/>
  <path d="M-130 50L-20-10h100l50 60" fill="none" stroke="{TEAD}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-60-30h110l26 40h-150z" class="teal o"/>
  <path d="M-90-20h50l-10 30h-50z" class="coral o"/>
  <path d="M60-30l30-40h50" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M110-70h50" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M-40 20l-30 80" stroke="{MUTED}" stroke-width="8" fill="none" stroke-linecap="round"/></g>''')

add('moustache', '鼻の下にたくわえた濃い口ひげ',
    '口ひげ＝moustache。', f'''
<g transform="translate(300 210)">
  <circle r="120" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-118-44q10-84 118-84t118 84q-50-38-118-26-66-12-118 26z" fill="{HAIR}"/>
  <circle cx="-42" cy="-16" r="6" class="ink"/><circle cx="42" cy="-16" r="6" class="ink"/>
  <ellipse cy="26" rx="18" ry="12" fill="{SKINL}" opacity="0.35"/>
  <path d="M-4 42q-50-26-80 2 30 28 80 6zM4 42q50-26 80 2-30 28-80 6z" fill="{HAIR}"/>
  <path d="M-30 84q30 18 60 0" fill="none" stroke="{INK}" stroke-width="4"/></g>
{ring(300, 250, 100, True)}''')

add('mug', '取っ手のついた厚手の筒型カップから湯気が立つ',
    'マグカップ＝mug。', f'''
{table(352)}
<g transform="translate(290 270)">
  <path d="M-70-70h140v130a20 20 0 0 1-20 20h-100a20 20 0 0 1-20-20z" class="teal o"/>
  <path d="M70-44q46 0 46 40t-46 40" fill="none" stroke="{TEA}" stroke-width="16"/>
  <path d="M-56-56h112v10h-112z" fill="#7a3f22"/></g>
{''.join(f'<path d="M{{}} {{}}q16-20 0-38" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(250 + i * 40, 170 - i * 10) for i in range(3))}''')

add('muggy', '蒸し暑い夜、風もなく人が扇であおいで汗をぬぐう',
    '蒸し暑い＝muggy。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#cfc0a8"/></g>
{''.join(f'<path d="M{{}} {{}}q16-22 0-40" fill="none" stroke="#a89880" stroke-width="5"/>'.format(80 + (i * 83) % 460, 70 + (i * 47) % 200) for i in range(8))}
{person(280, 350, 1.3, 1, 'coral', 'blue', 'reach', 'short', 'flat')}
<g transform="translate(370 230) rotate(-20)">
  <path d="M-50 0a50 50 0 0 1 100 0z" class="goldp o"/>
  <path d="M0 0v30" stroke="{BRN}" stroke-width="6" fill="none"/></g>
{''.join(drop(240 + i * 16, 230 + i * 16, 0.9, 'blue') for i in range(2))}''')

add('mulberry', 'クワの枝に黒紫の実がつき、葉をカイコが食べる',
    'クワ、クワの実＝mulberry。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(300 330)">
  <path d="M-10 0v-120h20V0z" class="goldd"/>
  <path d="M0-100l-70-40M0-110l70-46" fill="none" stroke="{BRN}" stroke-width="7"/>
  {''.join(f'<ellipse cx="{x}" cy="{y}" rx="30" ry="20" class="green o"/>' for x, y in [(-70, -150), (70, -164), (0, -180), (-30, -120)])}
  {''.join(f'<g transform="translate({x} {y})">{"".join(f"<circle cx=\'{-6+(j%2)*12}\' cy=\'{-6+(j//2)*10}\' r=\'7\' fill=\'#5b2a6a\'/>" for j in range(6))}</g>' for x, y in [(-100, -120), (96, -134), (30, -196)])}</g>
<g transform="translate(140 300) scale(1.2)">
  <path d="M-50 0q10-20 26-16 14-18 30-2 16-12 26 8-10 22-26 16-20 6-26-14-14 4-30-10z" fill="#f4f1ea" class="o"/>
  <circle cx="44" cy="-6" r="3" class="ink"/></g>''')

add('mussel', '黒い殻の二枚貝が、開いて中身を見せる',
    'ムール貝、イガイ＝mussel。', f'''
{table(352)}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M-56-26q56-24 112 0 6 40-56 52-62-12-56-52z" fill="#2f3542" class="o"/><path d="M-40-20q40-16 80 0" fill="none" stroke="#4e5a66" stroke-width="4"/></g>'.format(x, y, r) for x, y, r in [(180, 290, -10), (250, 250, 14)])}
<g transform="translate(400 280)">
  <path d="M-70-30q70-30 140 0 8 50-70 66-78-16-70-66z" fill="#2f3542" class="o"/>
  <path d="M-56-24q56-24 112 0 6 40-56 54-62-14-56-54z" class="gold o"/>
  <path d="M-30-6q30 22 60 0" fill="none" stroke="{GLDD}" stroke-width="4"/></g>''')

add('napkin', 'たたんだ布のナプキンが、皿のわきに置かれている',
    'ナプキン＝napkin。', f'''
{table(330)}
<g transform="translate(360 300)">
  <ellipse rx="110" ry="30" fill="#fffefd" class="o"/>
  <ellipse rx="78" ry="20" fill="none" stroke="{MUTED}" stroke-width="3"/></g>
<g transform="translate(170 290) rotate(-6)">
  <path d="M-70-50h140v100h-140z" class="coralp o"/>
  <path d="M-70 0h140M-70-25h140M-70 25h140" fill="none" stroke="{CRL}" stroke-width="3"/>
  <path d="M-70-50h140v14h-140z" class="coral o"/></g>''')

add('neighbour', '垣根ごしに、隣り合う家の人どうしが挨拶する',
    '隣人、近所の人＝neighbour。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
{house(130, 300, 0.72, 'coral')}
{house(470, 300, 0.72, 'teal')}
{''.join(f'<path d="M300 340v-90" stroke="{BRN}" stroke-width="11" fill="none" stroke-linecap="round"/>' for _ in range(1))}
{''.join(f'<path d="M{{}} 340v-90" stroke="{BRN}" stroke-width="11" fill="none" stroke-linecap="round"/>'.format(270 + i * 30) for i in range(3))}
<path d="M260 264h80M260 296h80" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
{person(230, 340, 1.0, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{person(380, 340, 1.0, -1, 'teal', 'green', 'up', 'bob', 'smile')}''')

add('notepad', 'とじた側から切り取れる小さなメモ帳に、走り書きが残る',
    'メモ帳＝notepad。', f'''
{table(352)}
<g transform="translate(290 260)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <path d="M-100-110h200v24h-200z" fill="#c3cbd1" class="o"/>
  {''.join(f'<circle cx="{-76+i*38}" cy="-98" r="7" fill="{MUTED}"/>' for i in range(5))}
  {''.join(f'<path d="M-76 {-50+i*34}q22-14 44 0t44 0" fill="none" stroke="{MUTED}" stroke-width="5"/>' for i in range(3))}</g>
<g transform="translate(430 160) rotate(34)">
  <path d="M-8-70h16v100l-8 20-8-20z" class="teal o"/></g>''')

add('nozzle', 'ホースの先の筒口から、水が細く勢いよく出る',
    '(ホースなどの)筒先、ノズル＝nozzle。', f'''
<path d="M40 300q120-60 180-40" fill="none" stroke="{GRND}" stroke-width="18" stroke-linecap="round"/>
<g transform="translate(260 250) rotate(-16)">
  <path d="M-50-24h60v48h-60z" fill="#6b7680" class="o"/>
  <path d="M10-16h60l30 16-30 16H10z" fill="#9aa7b1" class="o"/>
  <path d="M-20 24v40h30V24" fill="#6b7680" class="o"/></g>
<path d="M370 214q80-20 170 40" fill="none" stroke="{BLU}" stroke-width="14" stroke-linecap="round"/>
{''.join(drop(420 + i * 50, 200 + (i % 2) * 24, 1.0, 'blue') for i in range(3))}''')

add('nutrient', '食べ物から取り入れられた養分の粒が、体に運ばれる',
    '栄養素＝nutrient。', f'''
<g transform="translate(170 260)">
  <ellipse rx="100" ry="30" fill="#fffefd" class="o"/>
  {''.join(f'<ellipse cx="{-50+i*34}" cy="-16" rx="24" ry="14" class="green o"/>' for i in range(3))}
  <circle cx="56" cy="-14" r="16" class="coral o"/></g>
{arc(280, 200, 380, 200, 50, MUTED, True, 5)}
<g transform="translate(470 240)">
  <circle r="110" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 11"/>
  {''.join(f'<circle cx="{int(60*math.cos(math.radians(a)))}" cy="{int(60*math.sin(math.radians(a)))}" r="16" class="{c} o"/>' for a, c in zip(range(0, 360, 60), ['gold', 'green', 'coral', 'blue', 'violet', 'teal']))}</g>''', arrow=True)

add('oatmeal', 'ひき割りのオーツ麦を煮た粥が、器に盛られている',
    'オートミール＝oatmeal。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-110-30q0 70 110 70t110-70z" fill="#fffefd" class="o"/>
  <ellipse cy="-30" rx="110" ry="30" fill="#fffefd" class="o"/>
  <ellipse cy="-28" rx="90" ry="23" fill="#e8d8b0"/>
  {''.join(f'<ellipse cx="{-50+i*34}" cy="{-34+(i%2)*10}" rx="12" ry="7" fill="#d4bf8e"/>' for i in range(4))}
  <circle cx="30" cy="-30" r="13" class="coral o"/></g>
<g transform="translate(430 190) rotate(30)">
  <path d="M-8-90h16v120h-16z" fill="#c3cbd1" class="o"/>
  <ellipse cy="-96" rx="24" ry="34" fill="#dfe6ea" class="o"/></g>''')

add('octopus', '八本の足を広げたタコが、海の底の岩の間にいる',
    'タコ＝octopus。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#cfe4f0"/></g>
<path d="M0 340h600v60H0z" fill="#d8cdb6"/>
<g transform="translate(300 210)">
  <path d="M-80-20q0-90 80-90t80 90q0 40-80 40t-80-40z" class="coral o"/>
  <circle cx="-30" cy="-40" r="9" class="ink"/><circle cx="30" cy="-40" r="9" class="ink"/>
  {''.join(f'<path d="M{-70+i*20} 16q{-30+i*9} 70 {-60+i*18} 110" fill="none" stroke="{CRL}" stroke-width="13" stroke-linecap="round"/>' for i in range(8))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="none" stroke="#9fc8dd" stroke-width="2.5"/>'.format(80 + (i * 97) % 440, 70 + (i * 53) % 120, 6 + i % 3) for i in range(6))}''')

add('omelette', '折りたたんだ黄色い卵焼きが、皿に盛られている',
    'オムレツ＝omelette。', f'''
{table(352)}
<g transform="translate(300 290)">
  <ellipse rx="150" ry="40" fill="#fffefd" class="o"/>
  <path d="M-100-20q40-56 110-40 60 14 70 50-60 30-180 10z" class="gold o"/>
  <path d="M-70-30q60-30 130-6" fill="none" stroke="{GLDD}" stroke-width="4"/>
  {''.join(f'<path d="M{-40+i*40} -4q20-14 34 0" fill="none" stroke="{GLDD}" stroke-width="3"/>' for i in range(3))}
  <ellipse cx="100" cy="4" rx="24" ry="12" class="green o"/></g>''')

add('onion', '外側の薄い皮をむくと、幾重にも重なった層が見える',
    'タマネギ＝onion。', f'''
{table(352)}
<g transform="translate(200 270)">
  <path d="M-70 20q-10-70 70-90 80 20 70 90-20 50-70 50t-70-50z" fill="#e0c48c" class="o"/>
  <path d="M0-70q-16-30 4-44 10 24 16 44" fill="none" stroke="{GRND}" stroke-width="5"/>
  {''.join(f'<path d="M{-46+i*30} -50q-10 60 0 110" fill="none" stroke="#c8a05f" stroke-width="3"/>' for i in range(4))}</g>
<g transform="translate(430 280)">
  <path d="M-70 0q-10-70 70-80 80 10 70 80z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M-{{}} 0q0-{{}} {{}}-{{}}t{{}} {{}}" fill="none" stroke="#e0d8c0" stroke-width="4"/>'.format(56 - i * 14, 56 - i * 14, 56 - i * 14, 62 - i * 16, 56 - i * 14, 62 - i * 16) for i in range(4))}</g>''')

add('orchard', 'りんごの木が並んだ果樹園で、実を摘む',
    '果樹園＝orchard。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
{''.join(f'<g transform="translate({{}} 310)"><path d="M-9 0v-60h18V0z" class="goldd"/><circle cx="-22" cy="-80" r="34" class="greenp o"/><circle cx="22" cy="-88" r="36" class="greenp o"/><circle cy="-112" r="30" class="greenp o"/>{{}}</g>'.format(110 + i * 130, ''.join(f'<circle cx="{-24+j*24}" cy="{-84-(j%2)*24}" r="10" class="coral o"/>' for j in range(3))) for i in range(4))}
{person(300, 370, 0.8, 1, 'teal', 'blue', 'up', 'cap', 'smile')}
<g transform="translate(330 320)"><path d="M-30-20h60l-6 40h-48z" class="goldp o"/>
  {''.join(f'<circle cx="{-14+i*14}" cy="-6" r="9" class="coral o"/>' for i in range(3))}</g>''')

add('origami', '正方形の紙を折り重ねて、鶴の形に仕上げる',
    '折り紙＝origami。', f'''
{table(352)}
<g transform="translate(160 280) rotate(-8)">
  <path d="M-60-60h120v120h-120z" class="coralp o"/>
  <path d="M-60-60l120 120M60-60L-60 60" fill="none" stroke="{CRL}" stroke-width="3" stroke-dasharray="9 8"/></g>
{arc(250, 230, 320, 230, 46, MUTED, True, 5)}
<g transform="translate(430 270)">
  <path d="M-90 30L0-50l90 80-90 10z" class="coral o"/>
  <path d="M0-50l-30-70 20 60 60-40-40 60z" class="coralp o"/>
  <path d="M-90 30l-30 40 50-10z" class="corald o"/></g>''', arrow=True)

add('ornament', '棚の上に、飾るためだけの小さな置き物が並ぶ',
    '飾り、装飾品＝ornament。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-220-20h440v20h-440z" fill="#c9a464" class="o"/></g>
<g transform="translate(170 250)">
  <path d="M-30 30q-20-40 6-56 24-14 44 2 24 20 6 54z" class="tealp o"/>
  <path d="M-14 30h28v16h-28z" class="teald o"/></g>
<g transform="translate(300 250)">
  <ellipse cy="10" rx="34" ry="34" class="coralp o"/>
  <path d="M-10-30h20v10h-20z" class="corald o"/>
  <path d="M-20 6q20 20 40 0" fill="none" stroke="{CRL}" stroke-width="4"/></g>
<g transform="translate(440 254)">
  <path d="M-26 26L0-34l26 60z" class="violetp o"/>
  <path d="M-30 26h60v14h-60z" class="violetd o"/></g>
{''.join(spark(110 + i * 380, 160, 0.6, 'gold') for i in range(2))}''')

add('overcoat', '丈の長い厚手の外套に、大きなボタンと襟がついている',
    'オーバーコート＝overcoat。', f'''
<g transform="translate(300 210)">
  <path d="M-120-100h240v270h-240z" class="violet o"/>
  <path d="M-120-100l-64 44 36 100 28-16M120-100l64 44-36 100-28-16" class="violet o"/>
  <path d="M-40-100q40 40 80 0l-24 70h-32z" fill="#fffaf1" class="o"/>
  <path d="M-40-100L-70 170M40-100l30 270" fill="none" stroke="{VIOD}" stroke-width="5"/>
  {''.join(f'<circle cx="-6" cy="{-10+i*46}" r="10" class="goldp o"/>' for i in range(4))}
  <path d="M-70 60h56v44h-56zM14 60h56v44H14z" class="violetd o"/>
  <path d="M-120-100h240v270h-240z" fill="none" class="o"/></g>
<path d="M0 90h600v12H0z" fill="{MUTED}"/>''')

add('padlock', '取り外しできる錠が、門の輪に通されて閉じている',
    '南京錠＝padlock。', f'''
<g transform="translate(300 250)">
  <path d="M-200-140h130v300h-130z" fill="#c9a464" class="o"/>
  <path d="M70-140h130v300H70z" fill="#c9a464" class="o"/>
  <circle cx="-50" cy="0" r="26" fill="none" stroke="#8a97a3" stroke-width="10"/>
  <circle cx="50" cy="0" r="26" fill="none" stroke="#8a97a3" stroke-width="10"/></g>
<g transform="translate(300 260)">
  <path d="M-34-30a34 40 0 0 1 68 0v30h-20v-30a14 20 0 0 0-28 0v30h-20z" fill="none" stroke="{GLDD}" stroke-width="12"/>
  <rect x="-50" y="0" width="100" height="74" rx="10" class="gold o"/>
  <circle cy="30" r="10" class="ink"/>
  <path d="M0 34v18" stroke="{INK}" stroke-width="6" fill="none"/></g>''')

add('pallet', 'フォークリフトの爪が入る木の荷台に、箱が積まれている',
    '(荷を載せる)パレット＝pallet。', f'''
{table(352)}
<g transform="translate(300 310)">
  <path d="M-160-16h320v16h-320z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-150+i*100} 0h60v30h-60z" fill="#a0764a" stroke="{INK}" stroke-width="2.5"/>' for i in range(3))}
  <path d="M-160 30h320v14h-320z" fill="#c9a464" class="o"/></g>
{''.join(box(230 + i * 70, 260, 62, 44, 14, 'gold') for i in range(3))}
{''.join(box(265 + i * 70, 210, 62, 44, 14, 'gold') for i in range(2))}
{''.join(f'<path d="M{{}} {{}}h60" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>'.format(80, 322 + i * 30) for i in range(2))}''')

add('pancake', '薄く焼いた生地を重ね、シロップをかける',
    'パンケーキ＝pancake。', f'''
{table(352)}
<g transform="translate(300 300)">
  <ellipse rx="130" ry="34" fill="#fffefd" class="o"/>
  {''.join(f'<ellipse cy="{-14-i*24}" rx="{96-i*4}" ry="24" fill="#e0b872" stroke="{INK}" stroke-width="2.5"/>' for i in range(3))}
  <path d="M-30-90q30 20 60 0" fill="none" stroke="#c08f4e" stroke-width="0"/>
  <rect x="-26" y="-104" width="52" height="18" rx="4" class="gold o"/></g>
<g transform="translate(160 150) rotate(36)">
  <path d="M-30-46h60v80a22 22 0 0 1-22 22h-16a22 22 0 0 1-22-22z" class="goldp o"/></g>
<path d="M230 220q20 30 30 46" fill="none" stroke="{GLD}" stroke-width="10" stroke-linecap="round"/>''')

add('pane', '窓わくにはまったガラスの一枚に、ひびが入っている',
    '窓ガラスの一枚＝pane。', f'''
<g transform="translate(300 200)">
  <path d="M-200-150h400v300h-400z" fill="#e8ddc9" class="o"/>
  <path d="M-170-120h160v110h-160zM10-120h160v110H10zM-170 10h160v110h-160zM10 10h160v110H10z" fill="#dfeaf2" class="o"/></g>
<g transform="translate(390 145)">
  <path d="M-50 20L-10-30 10 0 50-40" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-10-30l-30-24M10 0l34 34" fill="none" stroke="{INK}" stroke-width="3"/></g>
{ring(390, 145, 74, True)}''')

add('pantry', '食品をしまう小さな部屋の棚に、びんと袋が並ぶ',
    '食品庫、パントリー＝pantry。', f'''
<g transform="translate(300 200)">
  <path d="M-220-170h440v340h-440z" fill="#e8ddc9" class="o"/>
  <path d="M-190-140h380v310h-380z" fill="#f6efe1" class="o"/>
  {''.join(f'<path d="M-190 {-70+i*80}h380v12h-380z" fill="#c9a464"/>' for i in range(3))}
  {''.join(f'<g transform="translate({-150+ (i%6)*60} {-92+(i//6)*80})"><path d="M-18-30h36v60h-36z" fill="{c}" stroke="{INK}" stroke-width="2"/><path d="M-10-40h20v10h-20z" fill="{INK}" opacity="0.4"/></g>' for i, c in enumerate(['#dff4ef','#fde9e3','#fff0c5','#e1edfb','#eee8fb','#e1f3e5']*3))}</g>''')

add('paperclip', '曲げた針金のクリップが、紙の束をまとめている',
    'クリップ、紙ばさみ＝paperclip。', f'''
{table(352)}
<g transform="translate(300 260) rotate(-6)">
  <path d="M-120-100h240v200h-240z" class="paper"/>
  {''.join(f'<rect x="-90" y="{-60+i*34}" width="{180-(i%3)*50}" height="10" rx="5" fill="{MUTED}"/>' for i in range(4))}</g>
<g transform="translate(250 180) rotate(-6)">
  <path d="M-20 60V-30a20 20 0 0 1 40 0v70a12 12 0 0 1-24 0V-16" fill="none" stroke="#8a97a3" stroke-width="9" stroke-linecap="round"/></g>
{ring(250, 190, 66, True)}''')

add('parachute', '半円形の傘が開き、その下に人がぶら下がって降りる',
    'パラシュート＝parachute。', f'''
{''.join(cloud(120 + i * 340, 70, 1.0, 'blue') for i in range(2))}
<g transform="translate(300 170)">
  <path d="M-140 0a140 100 0 0 1 280 0z" class="coral o"/>
  <path d="M-140 0q46-100 0 0M-70 0q34-110 0 0M0 0v-100M70 0q-34-110 0 0M140 0q-46-100 0 0" fill="none" stroke="{CRLD}" stroke-width="3"/>
  {''.join(f'<path d="M{-140+i*70} 0L0 110" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(5))}</g>
{person(300, 360, 1.0, 1, 'teal', 'blue', 'up', 'cap', 'smile')}''')

add('parasol', '日差しを遮る大きなパラソルの下に、テーブルがある',
    '日傘、パラソル＝parasol。', f'''
{sun(500, 80, 40)}
<path d="M0 320h600v80H0z" fill="#f0e0b8"/>
<g transform="translate(280 200)">
  <path d="M-150 0a150 110 0 0 1 300 0z" class="teal o"/>
  {''.join(f'<path d="M{-150+i*60} 0q{30-i*10}-80 {30-i*10} -110" fill="none" stroke="#fffefd" stroke-width="10"/>' for i in range(5))}
  <path d="M0 0v150" stroke="{BRN}" stroke-width="9" fill="none"/></g>
<g transform="translate(280 330)">
  <ellipse rx="110" ry="26" fill="#c9a464" class="o"/>
  <path d="M-70 20v40M70 20v40" stroke="{BRN}" stroke-width="9" fill="none"/></g>''')

add('parcel', '茶色の紙で包みひもを掛けた小包に、宛名の札がつく',
    '小包＝parcel。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-130-80h260v160h-260z" fill="#c9a464" class="o"/>
  <path d="M-10-80h20v160h-20z" class="corald"/>
  <path d="M-130-10h260v20h-260z" class="corald"/>
  <path d="M-10-10q-40-40-6-52 20 20 6 52M10-10q40-40 6-52-20 20-6 52" fill="{CRL}" stroke="{INK}" stroke-width="2"/>
  <path d="M52-60h60v40H52z" class="paper"/>
  {''.join(f'<rect x="60" y="{-52+i*12}" width="{44-(i%2)*14}" height="6" rx="3" fill="{MUTED}"/>' for i in range(2))}</g>''')

add('parsnip', '白く太い根菜が、葉をつけたまま置かれている',
    'パースニップ＝parsnip。', f'''
{table(352)}
{''.join(f'<g transform="translate({{}} 260) rotate({{}})"><path d="M-40-90h80l-40 190z" fill="#f0e6cc" class="o"/>{{}}<path d="M-26-90q-16-50 0-70 12 30 12 70M0-90q0-60 12-76-4 38 2 76" fill="none" stroke="{GRND}" stroke-width="5"/></g>'.format(x, r, ''.join(f'<path d="M{-28+j*18} {-60+j*20}l{18-j*4} 6" stroke="#d8c8a8" stroke-width="3" fill="none"/>' for j in range(3))) for x, r in [(210, -8), (390, 10)])}''')

finish(__file__)
