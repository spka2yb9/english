# -*- coding: utf-8 -*-
"""第186回。plus34 の50語。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('hoop', '大きな輪をくぐり抜けるように、犬が跳ぶ',
    '輪、たが＝hoop。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<g transform="translate(340 220)"><circle r="110" fill="none" stroke="{CRL}" stroke-width="16"/></g>
<g transform="translate(340 230)">
  <ellipse rx="70" ry="34" fill="#c8a05f" class="o"/>
  <circle cx="60" cy="-26" r="26" fill="#c8a05f" class="o"/>
  <path d="M78-44l-4-24 22 14z" fill="#c8a05f" class="o"/>
  <circle cx="72" cy="-32" r="4" class="ink"/>
  <path d="M-56 24l-16 40M-14 30l-8 40M20 30l10 40M56 22l22 40" stroke="#c8a05f" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M-66-6q-34-16-34-44" fill="none" stroke="#c8a05f" stroke-width="11" stroke-linecap="round"/></g>
{arc(140, 300, 250, 250, 60, MUTED, True, 4)}''', arrow=True)

add('hornet', '黄と黒の縞をもつ大きなハチが、羽を広げて飛ぶ',
    'スズメバチ＝hornet。', f'''
<g transform="translate(300 210) scale(1.5)">
  <path d="M-30-30q50-40 90-10 20 16 0 34-40 22-90-24z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="2"/>
  <path d="M-30 10q50 40 90 10 20-16 0-34-40-22-90 24z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="2"/>
  <ellipse rx="56" ry="30" class="gold o"/>
  {''.join(f'<path d="M{-30+i*24} -28v56" stroke="#2f3542" stroke-width="13" fill="none"/>' for i in range(3))}
  <ellipse rx="56" ry="30" fill="none" class="o"/>
  <circle cx="-64" cy="-4" r="22" fill="#2f3542" class="o"/>
  <path d="M-80-20l-16-14M-80 8l-18 8" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M56 0l30 4-30 8z" fill="#2f3542" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q14-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(460 + i * 22, 120 + i * 0) for i in range(2))}''')

add('hospital', '大きな赤い十字の看板のある建物に、救急車が着く',
    '病院＝hospital。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
{tower(220, 330, 1.1, 'teal', 5)}
<g transform="translate(220 130)">
  <path d="M-14-34h28v22h22v28h-22v22h-28v-22h-22v-28h22z" class="coral o"/></g>
<g transform="translate(460 320)">
  <path d="M-110 0v-70h160l40 40V0z" fill="#fffefd" class="o"/>
  <path d="M40-64h34l28 30H40z" fill="#dfeaf2" class="o"/>
  <circle cx="-60" cy="6" r="22" class="ink"/><circle cx="50" cy="6" r="22" class="ink"/>
  <path d="M-70-46h14v10h10v14h-10v10h-14v-10h-10v-14h10z" class="coral o"/></g>''')

add('hourglass', 'くびれたガラスの中で、上から下へ砂が落ちる',
    '砂時計＝hourglass。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M-90-120h180v20h-180zM-90 100h180v20h-180z" fill="{BRN}" class="o"/>
  <path d="M-70-100h140L10 0l60 100h-140L-10 0z" fill="#e6f2f6" opacity="0.85" stroke="{INK}" stroke-width="3"/>
  <path d="M-62-94h124L8-4z" fill="#e0c48c"/>
  <path d="M-46 94h92L8 40z" fill="#e0c48c"/>
  <path d="M0-4v50" stroke="#e0c48c" stroke-width="6" fill="none"/></g>''')

add('humid', '蒸し暑い空気の中で、窓や鏡が曇り、人が汗をぬぐう',
    '湿気の多い、蒸し暑い＝humid。', f'''
<g transform="translate(300 180)">
  <path d="M-150-120h300v240h-300z" fill="#dfeaf2" class="o"/>
  <g opacity="0.6"><path d="M-120-80h240v200h-240z" fill="#eef4f7"/></g>
  {''.join(f'<path d="M{-90+i*60} 0q-16 40 0 60" fill="none" stroke="#b9c9d4" stroke-width="7" stroke-linecap="round"/>' for i in range(4))}</g>
{person(130, 350, 1.2, 1, 'coral', 'blue', 'think', 'short', 'flat')}
{''.join(drop(180 + i * 16, 250 + i * 14, 0.9, 'blue') for i in range(2))}
{''.join(f'<path d="M{{}} {{}}q16-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(490 + i * 22, 180 - i * 14) for i in range(2))}''')

add('hut', '板で組んだ簡素な小屋が、山の草地に一軒だけ立つ',
    '小屋、簡素な家＝hut。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<path d="M0 300L160 180l90 60 120-90 230 150z" fill="#d8cdb6" class="o"/>
<g transform="translate(300 320)">
  <path d="M-90 0v-90h180V0z" fill="#c9a464" class="o"/>
  <path d="M-106-90L0-160l106 70z" fill="#a0764a" class="o"/>
  <path d="M-26 0v-54h52V0z" fill="#8b6437" class="o"/>
  {''.join(f'<path d="M{-80+i*36} -90V0" stroke="#a0764a" stroke-width="3" fill="none"/>' for i in range(5))}</g>
{tree(90, 330, 0.8)}''')

add('icicle', '屋根のふちから、先のとがった氷が何本も垂れ下がる',
    'つらら＝icicle。', f'''
<g transform="translate(300 120)">
  <path d="M-260-80h520l30 60h-580z" class="corald o"/>
  <path d="M-240-20h480v20h-480z" fill="#9aa7b1" class="o"/></g>
{''.join(f'<path d="M{{}} 120q-16 0-16 {{}}l16 {{}} 16-{{}}q0-{{}}-16-{{}}z" fill="#dff1f8" stroke="{INK}" stroke-width="2.5"/>'.format(90 + i * 60, 20 + (i % 3) * 26, 80 + (i % 4) * 40, 80 + (i % 4) * 40, 20 + (i % 3) * 26, 20 + (i % 3) * 26) for i in range(8))}
<path d="M0 340h600v60H0z" fill="#eef4f7"/>''')

add('incense', '香立てに立てた線香の先から、細い煙が立ちのぼる',
    '香、お香＝incense。', f'''
{table(352)}
<g transform="translate(300 300)">
  <ellipse rx="80" ry="20" fill="#8a6a46" class="o"/>
  <path d="M-6-140h12v140h-12z" fill="#6a4a2a" class="o"/>
  <circle cy="-142" r="7" class="coral"/></g>
{''.join(f'<path d="M300 {{}}q{{}} -30 0-60" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>'.format(150 - i * 44, 30 if i % 2 else -30) for i in range(3))}
{''.join(f'<path d="M{{}} {{}}q10-14 0-24" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(400 + i * 20, 200 - i * 14) for i in range(2))}''')

add('ironing', 'アイロン台の上でシャツのしわを伸ばし、湯気が上がる',
    'アイロンがけ＝ironing。', f'''
<g transform="translate(300 300)">
  <path d="M-220-30h440q20 30 0 44h-440q-20-14 0-44z" fill="#e6e0d4" class="o"/>
  <path d="M-120 14l-30 86M120 14l30 86" stroke="{MUTED}" stroke-width="12" fill="none" stroke-linecap="round"/></g>
<g transform="translate(400 270)">
  <path d="M-120-14h240v14h-240z" fill="#fffefd" class="o"/>
  <path d="M-100-34q100-20 200 0v20h-200z" fill="#fffefd" class="o"/></g>
<g transform="translate(220 240)">
  <path d="M-90 30h180l-24-60h-132z" class="teal o"/>
  <path d="M-90 30h180v12h-180z" class="teald o"/>
  <path d="M-66-30h132v-20h-132z" class="teald o"/>
  <path d="M-40-50q40-46 80 0" fill="none" stroke="{INK}" stroke-width="12"/></g>
{''.join(f'<path d="M{{}} {{}}q14-18 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(120 + i * 22, 200 - i * 14) for i in range(2))}''')

add('jacket', 'ファスナーのついた短い上着が、掛けて広げられている',
    '上着、ジャケット＝jacket。', f'''
<g transform="translate(300 210)">
  <path d="M-110-90h220v240h-220z" class="teal o"/>
  <path d="M-110-90l-60 40 34 90 26-14" class="teal o"/>
  <path d="M110-90l60 40-34 90-26-14" class="teal o"/>
  <path d="M-30-90q30 30 60 0l-18 60h-24z" fill="#fffaf1" class="o"/>
  <path d="M-4-30v180" fill="none" stroke="{TEAD}" stroke-width="6"/>
  {''.join(f'<path d="M{-30+i*0} {20+i*44}h52" stroke="{TEAD}" stroke-width="0" fill="none"/>' for i in range(1))}
  <path d="M-56 40h50v40h-50zM10 40h50v40H10z" class="teald o"/>
  <path d="M-110-90h220v240h-220z" fill="none" class="o"/></g>
<path d="M0 90h600v12H0z" fill="{MUTED}"/>
<g transform="translate(300 110)"><path d="M0-20q-16-14 0-22 14-6 16 10" fill="none" stroke="#9aa7b1" stroke-width="6"/></g>''')

add('jade', '深い緑の石を彫った小さな飾りが、台に置かれている',
    'ヒスイ＝jade。', f'''
{table(352)}
<g transform="translate(300 260)">
  <ellipse cy="60" rx="80" ry="18" fill="#8a6a46" class="o"/>
  <path d="M-60 40q-26-70 10-100 34-28 70-6 40 24 16 106z" fill="#3f8f6a" class="o"/>
  <path d="M-30-10q30 30 60 0" fill="none" stroke="#2a6b4c" stroke-width="5"/>
  <path d="M-16-50q20 20 40 0" fill="none" stroke="#2a6b4c" stroke-width="5"/>
  <path d="M-40 20q40 24 80 0" fill="none" stroke="#5aa885" stroke-width="4"/></g>
{''.join(spark(160 + i * 280, 150, 0.7, 'gold') for i in range(2))}''')

add('jasmine', '夜に白い小さな花をつけたジャスミンが、強く香る',
    'ジャスミン＝jasmine。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#3b4557"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="2.5" fill="#fff6d8"/>'.format(50 + (i * 79) % 500, 40 + (i * 41) % 90) for i in range(8))}
<g transform="translate(300 320)">
  <path d="M0 80V-40" stroke="#2a6b4c" stroke-width="9" fill="none"/>
  {''.join(f'<path d="M0 {-10+i*30}q{-60 if i%2 else 60} -20 {-80 if i%2 else 80}-10" fill="none" stroke="#2a6b4c" stroke-width="6"/>' for i in range(3))}
  {''.join(f'<ellipse cx="{-70 if i%2 else 70}" cy="{-24+i*30}" rx="24" ry="13" fill="#2a6b4c" class="o"/>' for i in range(3))}</g>
{''.join(f'<g transform="translate({{}} {{}})">{{}}</g>'.format(x, y, ''.join(f'<ellipse cx="0" cy="-16" rx="8" ry="16" fill="#fffefd" stroke="{MUTED}" stroke-width="2" transform="rotate({a})"/>' for a in range(0, 360, 60)) + '<circle r="7" class="gold"/>') for x, y in [(230, 220), (370, 190), (300, 140), (400, 260)])}
{''.join(f'<path d="M{{}} {{}}q16-18 0-34" fill="none" stroke="#8a93a5" stroke-width="4"/>'.format(460 + i * 24, 160 - i * 16) for i in range(2))}''')

add('jellyfish', 'かさの形をした体から、長い触手が垂れて漂う',
    'クラゲ＝jellyfish。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#cfe4f0"/></g>
<g transform="translate(300 180)">
  <path d="M-110 20q0-110 110-110t110 110q-55 24-110 0t-110 0z" fill="#f0d8f0" opacity="0.9" stroke="{VIO}" stroke-width="3"/>
  {''.join(f'<path d="M{-66+i*33} -30q-10 40 0 60" fill="none" stroke="{VIO}" stroke-width="3" opacity="0.6"/>' for i in range(5))}
  {''.join(f'<path d="M{-80+i*40} 26q{-20 if i%2 else 20} 60 0 120" fill="none" stroke="{VIO}" stroke-width="5" stroke-linecap="round"/>' for i in range(5))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="none" stroke="#9fc8dd" stroke-width="2.5"/>'.format(70 + (i * 97) % 460, 60 + (i * 61) % 280, 6 + i % 4) for i in range(8))}''')

add('jetty', '水面へ突き出した木の桟橋に、小舟がつながれている',
    '桟橋、突堤＝jetty。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h180v150H0z" fill="#d8cdb6" class="o"/>
<g transform="translate(330 250)">
  <path d="M-170-16h340v22h-340z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-150+i*60} 6v70" stroke="{BRN}" stroke-width="12" fill="none"/>' for i in range(6))}</g>
<g transform="translate(470 300) rotate(4)">
  <path d="M-70 0h140l-24 36h-92z" class="coral o"/>
  <path d="M-10 0v-60h60l-52 22" fill="{GLDP}" class="o"/></g>
<path d="M420 258q30 20 40 34" fill="none" stroke="{BRN}" stroke-width="5"/>''')

add('jigsaw', 'ばらばらのパズルの片を組み合わせ、一枚の絵にする',
    'ジグソーパズル＝jigsaw。', f'''
{table(352)}
<g transform="translate(280 250)">
  {''.join(f'<g transform="translate({-105+ (i%3)*70} {-70+(i//3)*70})"><path d="M-35-35h70v70h-70z" fill="{c}" stroke="{INK}" stroke-width="2.5"/><circle cx="35" cy="0" r="11" fill="{c}" stroke="{INK}" stroke-width="2.5"/><circle cx="0" cy="35" r="11" fill="{c}" stroke="{INK}" stroke-width="2.5"/></g>' for i, c in enumerate(['#dff4ef','#fde9e3','#fff0c5','#e1edfb','#eee8fb','#e1f3e5']))}
  <path d="M-140-105h210v140h-210z" fill="none" stroke="{MUTED}" stroke-width="0"/></g>
<g transform="translate(470 300) rotate(20)">
  <path d="M-35-35h70v70h-70z" fill="#dff4ef" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="35" cy="0" r="11" fill="#dff4ef" stroke="{INK}" stroke-width="2.5"/></g>
{arc(450, 250, 380, 250, 50, MUTED, True, 4)}''', arrow=True)

add('jogging', 'ゆっくりした足取りで、公園の道を走り続ける',
    'ジョギング＝jogging。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<path d="M40 360q160-40 260-30t260 20" fill="none" stroke="{STONE}" stroke-width="26" stroke-linecap="round"/>
{person(320, 340, 1.35, 1, 'coral', 'blue', 'walk', 'cap', 'smile')}
{''.join(f'<path d="M{{}} {{}}h44" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>'.format(170 - i * 20, 260 + i * 30) for i in range(3))}
{tree(90, 330, 0.8)}{tree(520, 330, 0.7)}''')

add('kennel', '庭に置かれた小さな犬小屋の入口から、犬が顔を出す',
    '犬小屋＝kennel。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<g transform="translate(310 320)">
  <path d="M-100 0v-100h200V0z" fill="#c9a464" class="o"/>
  <path d="M-116-100L0-180l116 80z" fill="#a0764a" class="o"/>
  <path d="M-40 0v-70q40-24 80 0V0z" fill="#5b4636" class="o"/>
  {''.join(f'<path d="M{-84+i*40} -100V0" stroke="#a0764a" stroke-width="3" fill="none"/>' for i in range(5))}</g>
<g transform="translate(300 300)">
  <circle r="30" fill="#c8a05f" class="o"/>
  <path d="M-26-18l-6-26 22 14zM26-20l8-26-22 14z" fill="#c8a05f" class="o"/>
  <circle cx="-10" cy="-4" r="4" class="ink"/><circle cx="12" cy="-4" r="4" class="ink"/>
  <ellipse cy="14" rx="9" ry="6" fill="#5b4030"/></g>''')

add('keyhole', '扉の金具についた小さな穴の向こうに、光が見える',
    '鍵穴＝keyhole。', f'''
<g transform="translate(300 200)">
  <path d="M-200-180h400v360h-400z" class="teal o"/>
  {''.join(f'<path d="M-160 {-130+i*90}h320v70h-320z" fill="none" stroke="{TEAD}" stroke-width="5"/>' for i in range(3))}</g>
<g transform="translate(300 200)">
  <circle r="80" class="goldd o"/>
  <circle r="60" class="gold o"/>
  <path d="M0-30a22 22 0 1 1 0 44 22 22 0 1 1 0-44zM-12 12h24l8 44h-40z" fill="#2f2620"/></g>
{''.join(spark(180 + i * 240, 120, 0.6, 'gold') for i in range(2))}''')

add('keyring', '金属の輪に何本かの鍵と小さな飾りが通してある',
    'キーホルダー、鍵の輪＝keyring。', f'''
{table(352)}
<g transform="translate(300 230)">
  <circle r="46" fill="none" stroke="#9aa7b1" stroke-width="10"/>
  {''.join(f'<g transform="rotate({-40+i*40})"><path d="M0 46v80" stroke="{GLD}" stroke-width="12" fill="none"/><path d="M-10 110h10v18h-10zM-10 86h8v14h-8z" fill="{GLD}"/></g>' for i in range(3))}
  <g transform="translate(60 -34)"><path d="M0 26q-24-18-24-34 0-14 14-14 6 0 10 8 4-8 10-8 14 0 14 14 0 16-24 34z" class="coral o"/></g></g>''')

add('kindergarten', '小さな子どもたちが、色とりどりの積み木で遊ぶ部屋',
    '幼稚園＝kindergarten。', f'''
<g transform="translate(300 200)"><path d="M-280-160h560v320h-560z" fill="#fdf5e4" class="o"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-26" y="-22" width="52" height="44" rx="5" class="{{}} o"/></g>'.format(x, y, r, c) for x, y, r, c in [(240, 330, 0, 'coral'), (300, 330, 0, 'gold'), (270, 286, -4, 'teal'), (360, 330, 6, 'violet')])}
{person(130, 340, 0.78, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
{person(460, 340, 0.78, -1, 'coral', 'green', 'reach', 'bun', 'smile')}
{''.join(f'<g transform="translate({{}} 110)">{{}}</g>'.format(120 + i * 120, flower(0, 0, 0.5, c)) for i, c in enumerate(['coral', 'gold', 'violet', 'teal']))}''')

add('kitchen', 'コンロと流しと戸棚のそろった、料理をする部屋',
    '台所、キッチン＝kitchen。', f'''
<g transform="translate(300 200)"><path d="M-280-160h560v320h-560z" fill="#f6efe1" class="o"/></g>
<g transform="translate(300 300)">
  <path d="M-240-40h480v100h-480z" fill="#c9a464" class="o"/>
  <path d="M-240-40h480v-14h-480z" fill="#a0764a" class="o"/></g>
<g transform="translate(160 254)">
  <path d="M-70-14h140v28h-140z" fill="#c3cbd1" class="o"/>
  {''.join(f'<circle cx="{-40+i*40}" cy="-24" r="16" fill="#6b7680" class="o"/>' for i in range(2))}</g>
<g transform="translate(420 250)">
  <path d="M-70-20q0 44 70 44t70-44z" fill="#dfe6ea" class="o"/>
  <ellipse cy="-20" rx="70" ry="18" fill="#dfe6ea" class="o"/>
  <path d="M0-50v24" stroke="{MUTED}" stroke-width="8" fill="none"/></g>
<g transform="translate(300 130)">
  <path d="M-200-60h400v70h-400z" fill="#e0c48c" class="o"/>
  {''.join(f'<path d="M{-100+i*100} -60v70" stroke="#a0764a" stroke-width="4" fill="none"/>' for i in range(3))}</g>''')

add('kite', '糸を引く子どもの上で、ひし形の凧が風に上がる',
    'たこ(凧)＝kite。', f'''
<path d="M0 340h600v60H0z" class="greenp"/>
<g transform="translate(390 140) rotate(16)">
  <path d="M0-90L70 0 0 90-70 0z" class="coral o"/>
  <path d="M0-90V90M-70 0h140" fill="none" stroke="{CRLD}" stroke-width="4"/>
  <path d="M0 90q-20 40 10 60t-6 60" fill="none" stroke="{MUTED}" stroke-width="4"/>
  {''.join(f'<path d="M{-12+i*6} {110+i*44}h24" stroke="{GLD}" stroke-width="6" fill="none"/>' for i in range(3))}</g>
<path d="M356 210q-90 60-156 110" fill="none" stroke="{MUTED}" stroke-width="3"/>
{person(180, 350, 1.1, 1, 'teal', 'blue', 'up', 'cap', 'smile')}
{''.join(cloud(120 + i * 340, 80, 0.9, 'blue') for i in range(2))}''')

add('kitten', '小さな子猫が、毛糸玉に前足をかけて遊ぶ',
    '子猫＝kitten。', f'''
{table(352)}
<g transform="translate(260 290)">
  <ellipse rx="64" ry="44" fill="#b5a894" class="o"/>
  <circle cx="46" cy="-40" r="36" fill="#b5a894" class="o"/>
  <path d="M22-64l-6-30 26 18zM66-68l14-28 8 28z" fill="#b5a894" class="o"/>
  <circle cx="36" cy="-44" r="5" class="ink"/><circle cx="60" cy="-46" r="5" class="ink"/>
  <path d="M40-28q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-56 20q-40 6-40 34" fill="none" stroke="#b5a894" stroke-width="12" stroke-linecap="round"/>
  <path d="M-30 40v20M10 44v18" stroke="#b5a894" stroke-width="12" fill="none" stroke-linecap="round"/></g>
<g transform="translate(400 310)">
  <circle r="40" class="coral o"/>
  <path d="M-34-14q34 30 68 0M-30 14q30-30 60 0" fill="none" stroke="{CRLD}" stroke-width="3"/>
  <path d="M36-16l50-26" stroke="{CRL}" stroke-width="4" fill="none"/></g>''')

add('knapsack', '肩ひもの二本ついた布の袋を、背にかつぐ',
    'ナップサック、背負い袋＝knapsack。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-80-70h160v160h-160z" fill="{BRN}" class="o"/>
  <path d="M-80-70q80-40 160 0" fill="none" stroke="#6a4020" stroke-width="6"/>
  <path d="M-60-70q-30-50 0-70 20-14 40 0M60-70q30-50 0-70-20-14-40 0" fill="none" stroke="#6a4020" stroke-width="9"/>
  <path d="M-50 20h100v40h-100z" fill="#6a4020" class="o"/>
  <path d="M-14-30h28v22h-28z" class="goldd o"/></g>''')

add('knitting', '二本の棒針で毛糸を編み、編み地が下に伸びる',
    '編み物＝knitting。', f'''
{table(352)}
<g transform="translate(300 240)">
  <path d="M-90-40h180v140h-180z" class="coralp o"/>
  {''.join(f'<path d="M{-80+ (i%6)*30} {-20+(i//6)*34}q14-16 28 0" fill="none" stroke="{CRL}" stroke-width="4"/>' for i in range(18))}</g>
<g transform="translate(300 190) rotate(-24)">
  <path d="M-140-5h280v10h-280z" fill="#c9a464" class="o"/>
  <circle cx="-146" cy="0" r="9" fill="#a0764a" class="o"/></g>
<g transform="translate(300 200) rotate(24)">
  <path d="M-140-5h280v10h-280z" fill="#c9a464" class="o"/>
  <circle cx="146" cy="0" r="9" fill="#a0764a" class="o"/></g>
<g transform="translate(130 300)">
  <circle r="44" class="coral o"/>
  <path d="M-38-14q38 32 76 0M-34 14q34-32 68 0" fill="none" stroke="{CRLD}" stroke-width="3"/>
  <path d="M40-20l60-30" stroke="{CRL}" stroke-width="4" fill="none"/></g>''')

add('knob', '丸い取っ手を指でつまんで回すと、目盛りが動く',
    '取っ手、つまみ＝knob。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-150-90h300v180h-300z" class="tealp o"/>
  <circle r="60" fill="#e8ddc9" class="o"/>
  <circle r="44" fill="#c9a464" class="o"/>
  <path d="M0 0v-38" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none" transform="rotate(40)"/>
  {''.join(f'<path d="M0-70v-14" transform="rotate({-60+i*30})" stroke="{MUTED}" stroke-width="4" fill="none"/>' for i in range(5))}</g>
{hand(300, 140, 1)}
<g transform="translate(300 200)"><path d="M-50 0a50 50 0 0 1 34-48" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/></g>''', arrow=True)

add('ladle', '深い受け皿と長い柄のお玉で、鍋からスープをすくう',
    'お玉、大さじ＝ladle。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-120-40h240v50a30 30 0 0 1-30 30h-180a30 30 0 0 1-30-30z" fill="#cfd6db" class="o"/>
  <path d="M-110-30h220v40a24 24 0 0 1-24 24h-172a24 24 0 0 1-24-24z" class="goldp"/></g>
<g transform="translate(340 200) rotate(20)">
  <path d="M-8-120h16v140h-16z" fill="#c3cbd1" class="o"/>
  <path d="M-8-120q-22-10-22-26" fill="none" stroke="#c3cbd1" stroke-width="12"/>
  <path d="M-40 20q0 50 40 50t40-50z" fill="#dfe6ea" class="o"/>
  <ellipse cy="20" rx="40" ry="12" fill="#dfe6ea" class="o"/>
  <ellipse cy="22" rx="30" ry="8" class="goldp"/></g>''')

add('ladybird', '赤い羽に黒い点のあるテントウムシが、葉の上を歩く',
    'テントウムシ＝ladybird。', f'''
<g transform="translate(300 280)">
  <path d="M-220 40q80-90 220-90t220 90z" class="green o"/>
  <path d="M-160 20q160-50 320 0" fill="none" stroke="{GRND}" stroke-width="4"/></g>
<g transform="translate(300 210) scale(1.6)">
  <ellipse rx="56" ry="46" class="coral o"/>
  <path d="M0-46v92" stroke="{INK}" stroke-width="4" fill="none"/>
  {''.join(f'<circle cx="{-30+ (i%2)*60}" cy="{-16+(i//2)*28}" r="9" class="ink"/>' for i in range(6))}
  <circle cx="0" cy="-44" r="22" class="ink"/>
  <path d="M-12-60l-12-14M12-60l12-14" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/></g>''')

add('lampshade', '布のかさをかぶせた電灯が、やわらかい光を落とす',
    'ランプのかさ＝lampshade。', f'''
{table(352)}
<g transform="translate(300 280)">
  <ellipse cy="0" rx="70" ry="18" fill="#8a6a46" class="o"/>
  <path d="M-10 0v-90h20V0z" fill="#a0764a" class="o"/>
  <path d="M-100-90h200l-30-90h-140z" class="goldp o"/>
  <path d="M-100-90h200" fill="none" stroke="{GLDD}" stroke-width="4"/></g>
{''.join(f'<path d="M{{}} 200L{{}} 300" fill="none" stroke="{GLD}" stroke-width="4" stroke-dasharray="10 9"/>'.format(220 + i * 40, 180 + i * 60) for i in range(3))}''')

add('landlady', '家主の女性が、玄関で借り手に家賃の受け取りを渡す',
    '女性の家主＝landlady。', f'''
<g transform="translate(180 380)">
  <path d="M-120-300h240v300h-240z" fill="#e8ddc9" class="o"/>
  <path d="M-96-276h192v256h-192z" class="teal o"/>
  <circle cx="66" cy="-150" r="10" class="goldp o"/></g>
{person(330, 350, 1.2, 1, 'violet', 'blue', 'give', 'bun', 'smile')}
{person(490, 350, 1.1, -1, 'coral', 'green', 'reach', 'short', 'smile')}
<g transform="translate(410 250) rotate(-6)">
  <path d="M-40-26h80v52h-80z" class="paper"/>
  {''.join(f'<rect x="-28" y="{-12+i*16}" width="{56-(i%2)*18}" height="7" rx="3.5" fill="{MUTED}"/>' for i in range(2))}</g>''')

add('latch', '門についた掛け金を持ち上げて、外す',
    '掛け金、ラッチ＝latch。', f'''
<g transform="translate(300 220)">
  <path d="M-240-140h200v300h-200z" fill="#c9a464" class="o"/>
  <path d="M40-140h200v300H40z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-230+i*40} -140v300" stroke="#a0764a" stroke-width="3" fill="none"/>' for i in range(5))}
  {''.join(f'<path d="M{50+i*40} -140v300" stroke="#a0764a" stroke-width="3" fill="none"/>' for i in range(5))}</g>
<g transform="translate(300 200)">
  <path d="M-60-14h120v26h-120z" fill="#8a97a3" class="o"/>
  <path d="M40-14h30v40H40z" fill="#8a97a3" class="o"/>
  <circle cx="-60" cy="0" r="12" fill="#6b7680" class="o"/></g>
{hand(300, 100, 1)}
{line(300, 150, 300, 174, MUTED, True, 4)}''', arrow=True)

add('laundry', '洗濯かごに入った衣類と、まわっている洗濯機',
    '洗濯物、洗濯＝laundry。', f'''
{table(352)}
<g transform="translate(410 260)">
  <path d="M-110-100h220v190h-220z" fill="#dfe6ea" class="o"/>
  <circle cy="10" r="66" fill="#fffefd" class="o"/>
  <circle cy="10" r="46" class="bluep o"/>
  <path d="M-30 10q30-24 60 0t-60 0z" fill="#fffefd"/>
  {''.join(f'<circle cx="{-80+i*46}" cy="-76" r="9" fill="#9aa7b1"/>' for i in range(2))}</g>
<g transform="translate(170 300)">
  <path d="M-80-40h160l-16 80h-128z" fill="#e8ddc9" class="o"/>
  {''.join(f'<path d="M{-60+i*40} -40v80" stroke="#c8b898" stroke-width="4" fill="none"/>' for i in range(4))}
  {''.join(f'<g transform="translate({-40+i*40} -54) rotate({-16+i*14})"><rect x="-26" y="-14" width="52" height="28" rx="6" fill="{c}" stroke="{INK}" stroke-width="2"/></g>' for i, c in enumerate(['#dff4ef', '#fde9e3', '#e1edfb']))}</g>''')

add('lavender', '細長い茎の先に紫の穂をつけた花が、畑いっぱいに並ぶ',
    'ラベンダー＝lavender。', f'''
<path d="M0 280h600v120H0z" class="greenp"/>
{''.join(f'<g transform="translate({{}} {{}})"><path d="M0 40V-20" stroke="#4e7a4e" stroke-width="5" fill="none"/>{{}}</g>'.format(60 + (i % 9) * 60, 330 - (i // 9) * 40, ''.join(f'<ellipse cx="0" cy="{-24-j*14}" rx="9" ry="11" fill="#9a7ac8" stroke="{VIOD}" stroke-width="1.5"/>' for j in range(4))) for i in range(18))}
{sun(520, 80, 34)}
{''.join(f'<path d="M{{}} {{}}q16-18 0-34" fill="none" stroke="{VIO}" stroke-width="4"/>'.format(160 + i * 24, 150 - i * 16) for i in range(2))}''')

add('lawnmower', '車輪のついた芝刈り機を押し、通ったあとの芝が短くなる',
    '芝刈り機＝lawnmower。', f'''
<path d="M0 280h600v120H0z" class="greenp"/>
<path d="M0 300h300v100H0z" fill="#8fc49a"/>
<g transform="translate(340 320)">
  <path d="M-90-50h180v50h-180z" class="coral o"/>
  <circle cx="-60" cy="10" r="26" class="ink"/><circle cx="60" cy="10" r="26" class="ink"/>
  <path d="M60-50l70-100" stroke="{MUTED}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M100-150h60" stroke="{MUTED}" stroke-width="9" fill="none" stroke-linecap="round"/></g>
{person(490, 340, 1.0, -1, 'teal', 'blue', 'reach', 'cap', 'smile')}
{''.join(f'<path d="M{{}} 360q10-16 0-30" fill="none" stroke="{GRND}" stroke-width="4"/>'.format(400 + i * 60) for i in range(3))}''')

add('leash', '首輪につないだ引き綱を手で持ち、犬を連れて歩く',
    '(犬の)引き綱、リード＝leash。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
{person(180, 350, 1.2, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<path d="M246 240q80 30 110 70" fill="none" stroke="{CRL}" stroke-width="6"/>
<g transform="translate(420 320)">
  <ellipse rx="70" ry="34" fill="#c8a05f" class="o"/>
  <circle cx="60" cy="-30" r="26" fill="#c8a05f" class="o"/>
  <path d="M78-48l-4-26 24 16z" fill="#c8a05f" class="o"/>
  <circle cx="70" cy="-36" r="4" class="ink"/>
  <path d="M38-24h46v10H38z" class="coral o"/>
  <path d="M-56 24l-14 40M-16 30l-8 38M24 30l10 38M60 20l20 44" stroke="#c8a05f" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path d="M-66-6q-34-14-36-44" fill="none" stroke="#c8a05f" stroke-width="11" stroke-linecap="round"/></g>''')

add('ledge', '崖から水平に突き出した細い岩棚に、鳥が巣を作る',
    '棚状の出っぱり、岩棚＝ledge。', f'''
<path d="M0 0h240v400H0z" fill="#b5a894" class="o"/>
{''.join(f'<path d="M0 {{}}h240" stroke="#9a8d7e" stroke-width="4" fill="none"/>'.format(70 + i * 80) for i in range(4))}
<g transform="translate(240 200)">
  <path d="M0-20h130v34H0z" fill="#b5a894" class="o"/>
  <path d="M0 14h130l-26 16H0z" fill="#9a8d7e" class="o"/></g>
<g transform="translate(320 172)">
  <ellipse rx="42" ry="16" fill="#8a6a46" class="o"/>
  {''.join(f'<ellipse cx="{-14+i*14}" cy="-8" rx="10" ry="8" fill="#fffefd" stroke="{INK}" stroke-width="2"/>' for i in range(3))}</g>
{''.join(cloud(460 + i * 80, 90 + i * 60, 0.8, 'blue') for i in range(2))}''')

add('lemonade', '氷とレモンの輪切りを浮かべた冷たい飲み物',
    'レモネード＝lemonade。', f'''
{table(352)}
<g transform="translate(280 260)">
  <path d="M-60-90l10 180h100l10-180z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-50-40h100l8 130h-116z" fill="#f5e08a"/>
  {''.join(f'<rect x="{-36+i*28}" y="{-30+(i%2)*30}" width="26" height="26" rx="4" fill="#ffffff" opacity="0.85" stroke="{BLU}" stroke-width="2"/>' for i in range(3))}
  <path d="M-60-90l10 180h100l10-180z" fill="none" class="o"/>
  <path d="M20-90v-50" stroke="{CRL}" stroke-width="9" fill="none"/></g>
<g transform="translate(420 240)">
  <path d="M-34 0a34 34 0 0 1 68 0z" class="gold o"/>
  <path d="M0 0v-34M-24 0l24-24M24 0L0-24" stroke="{GLDD}" stroke-width="3" fill="none"/></g>''')

add('lentil', '小さく平たい豆が皿に山盛りになり、スープにも入る',
    'レンズ豆＝lentil。', f'''
{table(352)}
<g transform="translate(200 290)">
  <path d="M-90-24q0 54 90 54t90-54z" fill="#fffefd" class="o"/>
  <ellipse cy="-24" rx="90" ry="26" fill="#fffefd" class="o"/>
  {''.join(f'<ellipse cx="{-56+ (i%7)*19}" cy="{-30+(i//7)*12}" rx="10" ry="7" fill="#c96a44" stroke="{INK}" stroke-width="1.5"/>' for i in range(14))}</g>
<g transform="translate(430 280)">
  <path d="M-70-30q0 70 70 70t70-70z" fill="#cfd6db" class="o"/>
  <ellipse cy="-30" rx="70" ry="20" fill="#cfd6db" class="o"/>
  <ellipse cy="-28" rx="56" ry="15" fill="#b9714c"/>
  {''.join(f'<ellipse cx="{-26+i*26}" cy="-30" rx="8" ry="5" fill="#c96a44"/>' for i in range(3))}</g>''')

add('leopard', '黒い輪の模様をもつヒョウが、木の枝に体を横たえる',
    'ヒョウ＝leopard。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<g transform="translate(300 250)">
  <path d="M-260 30h520v26h-260z" fill="none"/>
  <path d="M-260 30h520v26h-520z" fill="{BRN}" class="o"/></g>
<g transform="translate(300 230)">
  <ellipse rx="150" ry="46" fill="#e0b862" class="o"/>
  <circle cx="140" cy="-30" r="42" fill="#e0b862" class="o"/>
  <path d="M110-58l-4-28 26 16zM160-60l14-26 10 24z" fill="#e0b862" class="o"/>
  <circle cx="128" cy="-34" r="5" class="ink"/><circle cx="152" cy="-36" r="5" class="ink"/>
  <path d="M-150 10q-56 10-70 50" fill="none" stroke="#e0b862" stroke-width="18" stroke-linecap="round"/>
  {''.join(f'<circle cx="{-120+ (i%8)*34}" cy="{-18+(i//8)*30}" r="8" fill="none" stroke="#5b4030" stroke-width="4"/>' for i in range(16))}
  <path d="M-80 44v34M0 46v32M70 44v34" stroke="#e0b862" stroke-width="14" fill="none" stroke-linecap="round"/></g>''')

add('librarian', '図書館の棚の前で、司書が本を手に案内する',
    '図書館員、司書＝librarian。', f'''
<g transform="translate(400 220)">
  <path d="M-150-180h300v360h-300z" fill="#c9a464" class="o"/>
  <path d="M-134-164h268v328h-268z" fill="#f6efe1" class="o"/>
  {''.join(f'<path d="M-134 {-90+i*84}h268v12h-268z" fill="#a0764a"/>' for i in range(3))}
  {''.join(f'<rect x="{-124+ (i%8)*31}" y="{-156+(i//8)*84}" width="{20+(i%3)*4}" height="{62-(i%2)*8}" rx="3" fill="{c}" stroke="{INK}" stroke-width="2"/>' for i, c in enumerate(['#238b83','#e86452','#d99a2b','#4e86c6','#816eb2','#4e986a','#238b83','#e86452']*3))}</g>
{person(140, 340, 1.2, 1, 'violet', 'blue', 'give', 'bun', 'smile')}
<g transform="translate(212 250) rotate(-10)">
  <path d="M-34-24h68v48h-68z" class="teal o"/>
  <path d="M-34-24h8v48h-8z" class="teald o"/></g>''')

add('lice', '髪の毛の間に、ごく小さな虫が付いている',
    'シラミ(louse の複数形)＝lice。', f'''
<g transform="translate(300 250)">
  <path d="M-200-60q200-120 400 0 20 160 0 220h-400q-20-60 0-220z" fill="{HAIR}"/>
  {''.join(f'<path d="M{-160+i*46} -50q20 100 0 210" fill="none" stroke="#25344a" stroke-width="4"/>' for i in range(8))}</g>
{''.join(f'<g transform="translate({{}} {{}}) scale(1.5)"><ellipse rx="12" ry="8" fill="#c8a87a" stroke="{INK}" stroke-width="2"/><circle cx="-11" cy="-2" r="5" fill="#b08a58" stroke="{INK}" stroke-width="1.5"/><path d="M-4 8l-4 8M2 9l0 8M8 7l5 8M-4-8l-4-8M2-9l0-8M8-7l5-8" stroke="{INK}" stroke-width="1.5" fill="none"/></g>'.format(x, y) for x, y in [(210, 190), (330, 160), (400, 230), (270, 260)])}
{ring(330, 160, 50, True)}''')

add('lid', 'つまみのついた丸いふたを、なべの上に載せる',
    'ふた＝lid。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-110-30h220v50a30 30 0 0 1-30 30h-160a30 30 0 0 1-30-30z" fill="#cfd6db" class="o"/>
  <path d="M-140-30h-30v20h30M110-30h30v20h-30" fill="none" stroke="#9aa7b1" stroke-width="12"/></g>
<g transform="translate(300 200)">
  <ellipse rx="122" ry="26" fill="#dfe6ea" class="o"/>
  <path d="M-122 0q0-30 122-30t122 30" fill="#dfe6ea" class="o"/>
  <path d="M-12-42h24v18h-24z" fill="#9aa7b1"/>
  <circle cy="-50" r="16" fill="#6b7680" class="o"/></g>
{line(300, 236, 300, 260, MUTED, True, 4)}''', arrow=True)

add('lifeboat', '救命ボートが本船から下ろされ、水面へ向かう',
    '救命ボート、救命艇＝lifeboat。', f'''
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(120 200)">
  <path d="M-140 100v-180h280v180z" fill="#dfe6ea" class="o"/>
  {''.join(f'<circle cx="{-100+i*50}" cy="-40" r="12" class="bluep o"/>' for i in range(4))}</g>
<g transform="translate(400 250)">
  <path d="M-110 0h220l-26 50h-168z" class="coral o"/>
  <path d="M-110 0h220v-14h-220z" class="corald o"/>
  {''.join(f'<path d="M{-70+i*70} -14v-60" stroke="{MUTED}" stroke-width="5" fill="none"/>' for i in range(3))}
  <path d="M-80-74h160" stroke="{MUTED}" stroke-width="6" fill="none"/>
  {''.join(head(-50 + i * 50, 20, 15, 'blue', 'short') for i in range(3))}</g>
{line(400, 160, 400, 190, MUTED, True, 4)}''', arrow=True)

add('lifeguard', '高い椅子に座った監視員が、浜辺と海を見張る',
    '監視員、ライフガード＝lifeguard。', f'''
<path d="M0 260h600v140H0z" fill="#f0e0b8"/>
<path d="M330 260h270v140H330z" class="bluep"/>
{''.join(f'<path d="M{{}} 300q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(340 + i * 70) for i in range(3))}
<g transform="translate(180 360)">
  <path d="M-60 0v-140h120V0z" fill="none" stroke="{BRN}" stroke-width="11"/>
  <path d="M-74-140h148v18h-148z" fill="{BRN}" class="o"/></g>
{sit(180, 222, 1.05, 1, 'coral', 'blue', 'cap', 'flat', 'lap')}
<g transform="translate(250 170)">
  <ellipse rx="30" ry="14" fill="#fffefd" class="o"/><circle r="10" class="ink"/></g>
<path d="M280 180h140" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('lightbulb', 'ガラスの球の中でフィラメントが光り、口金がねじ込まれる',
    '電球＝lightbulb。', f'''
<g transform="translate(300 210)">
  <circle r="90" class="goldp o"/>
  <path d="M-30 70h60v30h-60z" fill="#c3cbd1" class="o"/>
  {''.join(f'<path d="M-30 {100+i*16}h60" stroke="#9aa7b1" stroke-width="9" fill="none"/>' for i in range(3))}
  <path d="M-20 40v-30q20-26 40 0v30" fill="none" stroke="{GLDD}" stroke-width="5"/>
  <path d="M-20 40h40" stroke="{GLDD}" stroke-width="5" fill="none"/></g>
{''.join(f'<path d="M0-118v-30" transform="translate(300 210) rotate({{}})" stroke="{GLD}" stroke-width="7" stroke-linecap="round" fill="none"/>'.format(a) for a in (-60, -30, 0, 30, 60))}''')

add('lighthouse', '岬に立つ縞模様の塔が、海へ光を放つ',
    '灯台＝lighthouse。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#3b4557"/></g>
<path d="M0 320h600v80H0z" fill="#2f3a4d"/>
<g transform="translate(300 320)">
  <path d="M-46 0l16-200h60l16 200z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{-40+i*0} {-40-i*50}h80" stroke="{CRL}" stroke-width="22" fill="none"/>' for i in range(3))}
  <path d="M-46 0l16-200h60l16 200z" fill="none" class="o"/>
  <path d="M-40-200h80v-30h-80z" class="goldp o"/>
  <path d="M-46-230h92l-16-24h-60z" fill="#2f3542" class="o"/></g>
<path d="M270 90L60 20 60 170z" fill="#fff6d8" opacity="0.5"/>
<path d="M330 90L540 20 540 170z" fill="#fff6d8" opacity="0.5"/>''')

add('lilac', '房になった薄紫の花をつけた低木が、門のわきに咲く',
    'ライラック＝lilac。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<g transform="translate(300 300)">
  <path d="M-8 0v-80h16V0z" class="goldd"/>
  <path d="M0-70l-60-50M0-70l60-56M0-90v-50" fill="none" stroke="{BRN}" stroke-width="7"/>
  {''.join(f'<g transform="translate({x} {y})">{"".join(f"<circle cx={{}} cy={{}} r={{}} fill=\'#b79ad8\' stroke=\'{VIOD}\' stroke-width=\'1.5\'/>".format(-20 + (j % 3) * 20, -20 + (j // 3) * 18, 11) for j in range(9))}</g>' for x, y in [(-70, -140), (70, -146), (0, -170)])}
  {''.join(f'<ellipse cx="{x}" cy="{y}" rx="20" ry="11" class="green o" transform="rotate({r} {x} {y})"/>' for x, y, r in [(-50, -60, -20), (50, -66, 20), (-20, -30, -10)])}</g>
{''.join(f'<path d="M{{}} 240v-60" stroke="{BRN}" stroke-width="8" fill="none"/>'.format(90 + i * 420) for i in range(2))}''')

add('limestone', '水に溶けてできた石灰岩の洞窟に、つらら状の岩が下がる',
    '石灰岩＝limestone。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#3f3830"/></g>
<path d="M0 0h600v90H0z" fill="#d8cfbe"/>
{''.join(f'<path d="M{{}} 90q-14 0-14 {{}}l14 {{}} 14-{{}}q0-{{}}-14-{{}}z" fill="#cfc5b0" stroke="{INK}" stroke-width="2.5"/>'.format(70 + i * 66, 16 + (i % 3) * 20, 70 + (i % 4) * 40, 70 + (i % 4) * 40, 16 + (i % 3) * 20, 16 + (i % 3) * 20) for i in range(8))}
<path d="M0 330h600v70H0z" fill="#d8cfbe"/>
{''.join(f'<path d="M{{}} 330q-12 0-12-{{}}l12-{{}} 12 {{}}q0 {{}} 12 {{}}z" fill="#cfc5b0" stroke="{INK}" stroke-width="2.5"/>'.format(120 + i * 110, 14, 50 + (i % 3) * 30, 50 + (i % 3) * 30, 14, 14) for i in range(4))}''')

add('lining', 'コートの前を開くと、内側に別の布の裏地が見える',
    '(衣類などの)裏地＝lining。', f'''
<g transform="translate(300 210)">
  <path d="M-120-90h240v250h-240z" class="teal o"/>
  <path d="M-120-90l-56 40 30 90 26-14M120-90l56 40-30 90-26-14" class="teal o"/>
  <path d="M-60-90q60 40 120 0v250h-120z" class="coralp o"/>
  {''.join(f'<path d="M{-50+i*24} -50v200" stroke="{CRL}" stroke-width="3" fill="none" opacity="0.5"/>' for i in range(5))}
  <path d="M-60-90L-90 160M60-90l30 250" fill="none" stroke="{TEAD}" stroke-width="5"/></g>
{ring(300, 220, 0, True)}
{''.join(f'<path d="M{{}} 130h-50" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(500) for _ in range(1))}''', arrow=True)

add('lipstick', '筒から繰り出した口紅の芯が、斜めに角を見せる',
    '口紅＝lipstick。', f'''
{table(352)}
<g transform="translate(280 270)">
  <path d="M-34 20h68v70h-68z" class="goldd o"/>
  <path d="M-30-20h60v40h-60z" class="gold o"/>
  <path d="M-24-90q24-14 48 0v70h-48z" class="coral o"/>
  <path d="M-24-90q24-14 48 0l-10-24h-30z" class="corald o"/></g>
<g transform="translate(430 250)">
  <path d="M-46 0q10-26 24-12 10 8 22-2 12 10 22 2 14-14 24 12-24 30-46 30t-46-30z" class="coral o"/>
  <path d="M-46 0h92" fill="none" stroke="{CRLD}" stroke-width="3"/></g>''')

finish(__file__)
