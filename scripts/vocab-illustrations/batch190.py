# -*- coding: utf-8 -*-
"""第190回。plus38 の50語。shawl / slate の描き直しも含む。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('shawl', '大判の布を肩から背に巻き、ふちに房が下がる',
    'ショール、肩掛け＝shawl。', f'''
<g transform="translate(300 330)">
  <path d="M-70 0v-130q70-30 140 0V0z" class="blue o"/>
  <circle cx="0" cy="-176" r="36" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-38-184q4-42 38-42t38 40q-20-18-38-8-20-12-38 10z" fill="{HAIR}"/>
  <circle cx="-13" cy="-176" r="4" class="ink"/><circle cx="13" cy="-176" r="4" class="ink"/>
  <path d="M-11-156q11 9 22 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-110-120q110-50 220 0 20 90-110 120-130-30-110-120z" class="violet o"/>
  <path d="M-92-104q92-34 184 0" fill="none" stroke="{VIOD}" stroke-width="4"/>
  <path d="M-30-120L0-30l30-90" fill="none" stroke="{VIOD}" stroke-width="4"/>
  {''.join(f'<path d="M{-96+i*24} {int(-10 + abs(math.cos((i - 4) / 8 * math.pi)) * -10)}v26" stroke="{VIOD}" stroke-width="5" fill="none" stroke-linecap="round"/>' for i in range(9))}</g>''')

add('slate', '灰色の薄い石の板を重ねてふいた屋根',
    '粘板岩、スレート＝slate。', f'''
<g transform="translate(300 330)">
  <path d="M-240 0v-90h480V0z" fill="#e8ddc9" class="o"/>
  <path d="M-30 0v-60h60V0z" class="corald o"/></g>
<path d="M0 360h600v40H0z" class="ground"/>
<g transform="translate(300 160)">
  <path d="M-270 80L0-90l270 170z" fill="#6b7680" class="o"/></g>
{''.join(f'<rect x="{int(300 - 22 - (row) * 42 + col * 44)}" y="{int(84 + row * 26)}" width="40" height="24" rx="2" fill="{"#7a8690" if (row + col) % 2 else "#5f6a74"}" stroke="{INK}" stroke-width="1.5"/>' for row in range(6) for col in range(row * 2 + 1))}
<g transform="translate(470 250) rotate(14)">
  <rect x="-34" y="-22" width="68" height="44" rx="3" fill="#7a8690" stroke="{INK}" stroke-width="2.5"/></g>''')

# --- plus38 ------------------------------------------------------------------

add('snowman', '三段に丸めた雪の上に、帽子とにんじんの鼻がつく',
    '雪だるま＝snowman。', f'''
<path d="M0 300h600v100H0z" fill="#eef4f7"/>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#ffffff" stroke="{MUTED}" stroke-width="1.2"/>'.format(60 + (i * 83) % 500, 50 + (i * 41) % 200) for i in range(9))}
<g transform="translate(300 320)">
  <circle cy="-46" r="76" fill="#fffefd" class="o"/>
  <circle cy="-150" r="54" fill="#fffefd" class="o"/>
  <circle cy="-226" r="38" fill="#fffefd" class="o"/>
  <path d="M-44-250h88v14h-88zM-30-250h60v-40h-60z" fill="#2f3542" class="o"/>
  <path d="M4-228l34 8-34 10z" class="coral o"/>
  <circle cx="-12" cy="-234" r="4" class="ink"/><circle cx="12" cy="-234" r="4" class="ink"/>
  {''.join(f'<circle cy="{-166+i*30}" r="7" class="ink"/>' for i in range(3))}
  <path d="M-54-160l-60-40M54-160l60-40" stroke="{BRN}" stroke-width="7" fill="none" stroke-linecap="round"/></g>''')

add('sow', '畑のうねに、手から種をまいていく',
    '(種を)まく＝sow。', f'''
<path d="M0 260h600v140H0z" fill="#5b4636"/>
{''.join(f'<path d="M{{}} 400q20-70 0-140" fill="none" stroke="#3f3126" stroke-width="9"/>'.format(70 + i * 90) for i in range(6))}
{person(180, 330, 1.25, 1, 'teal', 'blue', 'give', 'cap', 'smile')}
<g transform="translate(140 250)">
  <path d="M-40-30h80l-10 60h-60z" fill="{BRN}" class="o"/></g>
{''.join(f'<ellipse cx="{{}}" cy="{{}}" rx="6" ry="4" fill="#c8a05f" stroke="{INK}" stroke-width="1.2"/>'.format(280 + (i * 41) % 200, 220 + (i * 29) % 90) for i in range(12))}
{arc(270, 200, 420, 240, 60, MUTED, True, 4)}''', arrow=True)

add('spanner', '口の開いた金具でボルトをはさみ、回して締める',
    'スパナ、レンチ＝spanner。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-160-30h320v60h-320z" fill="#c3cbd1" class="o"/>
  <path d="M-30-60l30-16 30 16v44l-30 16-30-16z" fill="#8a97a3" class="o"/>
  <circle cy="-16" r="16" fill="#6b7680"/></g>
<g transform="translate(300 190) rotate(-16)">
  <path d="M-16-10h32v150h-32z" fill="#b5bec4" class="o"/>
  <path d="M-40-60h80v40h-30v-18h-20v18h-30z" fill="#b5bec4" class="o"/></g>
<g transform="translate(300 150)"><path d="M-50 0a50 50 0 0 1 34-48" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="9 8" marker-end="url(#ar)"/></g>''', arrow=True)

add('sparkler', '手に持った細い花火の先から、火花が飛び散る',
    '線香花火、手持ち花火＝sparkler。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#2f3a4d"/></g>
{hand(220, 330, 1)}
<g transform="translate(320 230) rotate(-30)">
  <path d="M-6 0h12v140h-12z" fill="#8a97a3" class="o"/></g>
{''.join(f'<path d="M{int(370+30*math.cos(math.radians(a)))} {int(180+30*math.sin(math.radians(a)))}l{int(50*math.cos(math.radians(a)))} {int(50*math.sin(math.radians(a)))}" stroke="{GLD}" stroke-width="4" fill="none" stroke-linecap="round"/>' for a in range(0, 360, 20))}
{''.join(spark(370 + int(90 * math.cos(math.radians(a))), 180 + int(90 * math.sin(math.radians(a))), 0.5, 'gold') for a in (-140, -60, 20, 140, 200))}
<circle cx="370" cy="180" r="14" fill="#fff6d8"/>''')

add('spatula', '平たいへらでパンケーキを持ち上げ、返す',
    'フライ返し、へら＝spatula。', f'''
{table(352)}
<g transform="translate(320 300)">
  <ellipse rx="120" ry="34" fill="#4e5a66" class="o"/>
  <ellipse cy="-8" rx="104" ry="28" fill="#2f3542"/>
  <path d="M116-8h120v22h-120z" fill="#4e5a66" class="o"/></g>
<g transform="translate(290 230) rotate(-24)">
  <path d="M-60-16h120v40h-120z" fill="#c3cbd1" class="o"/>
  {''.join(f'<path d="M{-40+i*26} -10v28" stroke="#8a97a3" stroke-width="4" fill="none"/>' for i in range(4))}
  <path d="M-10-120h20v104h-20z" fill="{BRN}" class="o"/></g>
<g transform="translate(360 210) rotate(20)">
  <ellipse rx="54" ry="16" fill="#e0b872" class="o"/></g>''')

add('spike', '壁の上にとがった鉄の突起が並び、登れなくしている',
    'とがった棒、突起＝spike。', f'''
<g transform="translate(300 300)">
  <path d="M-260 100v-140h520v140z" fill="{STONE}" class="o"/>
  {''.join(f'<path d="M-260 {-20+i*40}h520" stroke="#a9b3ba" stroke-width="4" fill="none"/>' for i in range(3))}</g>
{''.join(f'<path d="M{{}} 260l14-70 14 70z" fill="#6b7680" stroke="{INK}" stroke-width="2.5"/>'.format(60 + i * 56) for i in range(9))}
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{CRL}" stroke-width="4"/>'.format(500 + i * 20, 160 - i * 14) for i in range(2))}''')

add('spire', '教会の屋根から、細くとがった塔が高く伸びる',
    '(教会の)尖塔＝spire。', f'''
<path d="M0 360h600v40H0z" class="greenp"/>
<g transform="translate(300 360)">
  <path d="M-140 0v-140h280V0z" fill="#e8ddc9" class="o"/>
  <path d="M-40 0v-90q40-34 80 0V0z" class="corald o"/>
  {''.join(f'<path d="M{-110+i*70} -110h40v50h-40z" class="bluep o"/>' for i in range(2))}
  <path d="M-60-140h120v-40h-120z" fill="#d8cdb6" class="o"/>
  <path d="M-50-180L0-330l50 150z" fill="#8a97a3" class="o"/>
  <path d="M0-330v-30" stroke="{GLDD}" stroke-width="5" fill="none"/>
  <circle cy="-368" r="9" class="gold o"/></g>
{ring(300, 100, 0, True)}''')

add('spout', 'やかんの細い注ぎ口から、湯気を上げて湯が出る',
    '(やかんなどの)注ぎ口＝spout。', f'''
{table(352)}
<g transform="translate(300 280) rotate(20)">
  <path d="M-80-50h160v80a40 40 0 0 1-40 40h-80a40 40 0 0 1-40-40z" fill="#c3cbd1" class="o"/>
  <path d="M-80-20q-60 0-70-50 30-16 70 26z" fill="#c3cbd1" class="o"/>
  <path d="M-24-70h48v20h-48z" fill="#8a97a3" class="o"/>
  <path d="M-40-70q40-46 80 0" fill="none" stroke="#8a97a3" stroke-width="10"/></g>
{ring(210, 230, 54, True)}
{''.join(f'<path d="M{{}} {{}}q14-20 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(160 + i * 22, 180 - i * 14) for i in range(2))}''')

add('sprinkler', '回る散水器から、細い水が扇のように芝へ広がる',
    'スプリンクラー、散水器＝sprinkler。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<g transform="translate(280 300)">
  <path d="M-16 0h32v-40h-32z" fill="#4e5a66" class="o"/>
  <path d="M-40-40h80v-20h-80z" fill="#6b7680" class="o"/>
  <path d="M-10-60h20v-20h-20z" fill="#6b7680" class="o"/></g>
{''.join(f'<path d="M280 220q{{}} -60 {{}} 20" fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round"/>'.format(dx, dx * 2) for dx in (-70, -30, 30, 70))}
{''.join(drop(210 + i * 60, 200 + (i % 2) * 26, 0.9, 'blue') for i in range(5))}
{''.join(f'<path d="M{{}} 340q12-16 0-30" fill="none" stroke="{GRND}" stroke-width="4"/>'.format(60 + i * 110) for i in range(5))}''')

add('stack', '同じ皿を上へきちんと重ね、高い山にする',
    '積み重ね、山＝stack。', f'''
{table(352)}
<g transform="translate(300 300)">
  {''.join(f'<ellipse cy="{-i*22}" rx="{100-i*5}" ry="{26-i}" fill="#fffefd" stroke="{INK}" stroke-width="2.5"/>' for i in range(8))}</g>
<path d="M470 130v180" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

add('starfish', '五本の腕を持つヒトデが、岩場に張りついている',
    'ヒトデ＝starfish。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#cfe4f0"/></g>
<path d="M0 330h600v70H0z" fill="#d8cdb6"/>
<g transform="translate(300 220)">
  {''.join(f'<g transform="rotate({{}})"><path d="M-34 0q10-130 34-130t34 130q-34 24-68 0z" fill="#e0834a" stroke="{INK}" stroke-width="3"/></g>'.format(i * 72) for i in range(5))}
  <circle r="44" fill="#e0834a" class="o"/>
  {''.join(f'<circle cx="{int(26*math.cos(math.radians(a)))}" cy="{int(26*math.sin(math.radians(a)))}" r="6" fill="#c06a34"/>' for a in range(0, 360, 60))}</g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="none" stroke="#9fc8dd" stroke-width="2.5"/>'.format(90 + (i * 97) % 420, 70 + (i * 53) % 140, 6 + i % 3) for i in range(6))}''')

add('steeple', '教会の塔と尖塔から、鐘の音が響く',
    '(教会の)塔と尖塔＝steeple。', f'''
<path d="M0 360h600v40H0z" class="greenp"/>
<g transform="translate(300 360)">
  <path d="M-170 0v-110h340V0z" fill="#e8ddc9" class="o"/>
  <path d="M-70 0v-240h140V0z" fill="#e8ddc9" class="o"/>
  <path d="M-80-240L0-360l80 120z" fill="#8a97a3" class="o"/>
  <path d="M-40-200h80v70h-80z" fill="#2f3542" class="o"/>
  <path d="M-24-186q24-16 48 0v40q-24 12-48 0z" class="goldp o"/>
  <path d="M-30 0v-70h60V0z" class="corald o"/></g>
{''.join(f'<path d="M{{}} {{}}q16-18 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(400 + i * 22, 160 - i * 14) for i in range(2))}''')

add('stencil', '切り抜いた型紙の上から塗り、同じ形を写し取る',
    '型紙、ステンシル＝stencil。', f'''
{table(352)}
<g transform="translate(240 280) rotate(-6)">
  <path d="M-120-70h240v140h-240z" fill="#c9a464" class="o"/>
  <path d="M-40-30h80v60h-80z" fill="#fffaf1"/>
  <circle cx="-72" cy="0" r="22" fill="#fffaf1"/>
  <path d="M52-28l30 56h-60z" fill="#fffaf1"/></g>
<g transform="translate(440 300)">
  <path d="M-80-40h160v80h-160z" class="paper"/>
  <path d="M-30-20h60v40h-60z" class="teal"/>
  <circle cx="-56" cy="0" r="14" class="teal"/>
  <path d="M46-18l20 36h-40z" class="teal"/></g>
{arc(370, 230, 420, 240, 40, MUTED, True, 4)}''', arrow=True)

add('stepladder', '自立するA字形の脚立に登って、高い所へ手を伸ばす',
    '脚立＝stepladder。', f'''
<path d="M0 360h600v40H0z" class="ground"/>
<g transform="translate(280 360)">
  <path d="M-70 0L-20-200h40L-30 0z" fill="{BRN}" class="o"/>
  <path d="M70 0L20-200" stroke="{BRN}" stroke-width="14" fill="none" stroke-linecap="round"/>
  {''.join(f'<path d="M{-58+i*8} {-40-i*40}h{56-i*8}" stroke="#c9a464" stroke-width="11" fill="none" stroke-linecap="round"/>' for i in range(4))}
  <path d="M-40-110h80" stroke="{MUTED}" stroke-width="5" fill="none"/></g>
{person(268, 250, 0.95, 1, 'teal', 'blue', 'up', 'cap', 'smile')}
<g transform="translate(420 110)"><circle r="30" class="goldp o"/>
  {''.join(f'<path d="M0-40v-16" transform="rotate({a})" stroke="{GLD}" stroke-width="5" stroke-linecap="round" fill="none"/>' for a in (-40, 0, 40))}</g>''')

add('sticker', 'はがして貼るシールが、ノートの表紙に並ぶ',
    'シール、ステッカー＝sticker。', f'''
{table(352)}
<g transform="translate(280 280)">
  <path d="M-120-90h240v180h-240z" class="tealp o"/>
  <path d="M-120-90h20v180h-20z" class="teald o"/>
  {''.join(f'<g transform="translate({-50+ (i%3)*60} {-40+(i//3)*60})"><circle r="24" fill="{c}" stroke="#fffefd" stroke-width="5"/></g>' for i, c in enumerate(['#e86452', '#d99a2b', '#4e86c6', '#816eb2', '#4e986a', '#238b83']))}</g>
<g transform="translate(460 200) rotate(14)">
  <circle r="30" fill="#e86452" stroke="#fffefd" stroke-width="6"/>
  <path d="M22-22q30-4 34 16-24 8-34-16z" fill="#f6efe1" stroke="{INK}" stroke-width="2"/></g>
{arc(440, 150, 390, 200, 40, MUTED, True, 4)}''', arrow=True)

add('stilts', '長い二本の棒に足を乗せ、背を高くして歩く',
    '竹馬、高足＝stilts。', f'''
<path d="M0 360h600v40H0z" class="ground"/>
{''.join(f'<g transform="translate({{}} 360)"><path d="M-9 0v-300h18V0z" fill="{BRN}" class="o"/><path d="M-26-170h52v18h-52z" fill="#a0764a" class="o"/></g>'.format(250 + i * 100) for i in range(2))}
{person(300, 190, 1.15, 1, 'coral', 'blue', 'up', 'cap', 'smile')}
{''.join(f'<path d="M{{}} 190v-30" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}
{''.join(f'<path d="M{{}} 340h40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>'.format(100 + i * 380) for i in range(2))}''')

add('stomachache', 'おなかを両手で押さえ、つらそうに体を折る',
    '腹痛＝stomachache。', f'''
<g transform="translate(300 340)">
  <path d="M-80 0v-140q80-30 160 0V0z" class="teal o"/>
  <path d="M-80-140q-16 70 50 78M80-140q16 70-50 78" fill="none" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>
  <circle cx="0" cy="-186" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-38-194q4-40 38-40 32 0 38 38-20-18-38-8-20-10-38 10z" fill="{HAIR}"/>
  <path d="M-22-186l18 8M22-186l-18 8" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-12-160q12-12 24 0" fill="none" stroke="{INK}" stroke-width="3"/></g>
{''.join(f'<path d="M{int(300+82*math.cos(math.radians(a)))} {int(258+70*math.sin(math.radians(a)))}l{int(28*math.cos(math.radians(a)))} {int(28*math.sin(math.radians(a)))}" stroke="{CRL}" stroke-width="6" fill="none" stroke-linecap="round"/>' for a in (-150, -120, -60, -30, 180, 0))}''')

add('stopper', 'びんの口にはめたガラスの栓を、引き抜く',
    '栓＝stopper。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-60-60h120v90a24 24 0 0 1-24 24h-72a24 24 0 0 1-24-24z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-24-100h48v40h-48z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-50-20h100v50a20 20 0 0 1-20 20h-60a20 20 0 0 1-20-20z" class="violetp"/></g>
<g transform="translate(300 150)">
  <path d="M-20 20h40v30h-40z" fill="#dff1f8" class="o"/>
  <path d="M-34-30h68v50h-68z" fill="#dff1f8" class="o"/></g>
{line(300, 210, 300, 186, MUTED, True, 4)}''', arrow=True)

add('stork', '長い足とくちばしのコウノトリが、屋根の巣に立つ',
    'コウノトリ＝stork。', f'''
<g transform="translate(300 330)">
  <path d="M-200 70L0-40l200 110z" class="corald o"/>
  <path d="M-40-60h40v-70h-40z" fill="{STONE}" class="o"/></g>
<g transform="translate(230 190)">
  <ellipse rx="40" ry="16" fill="#8a6a46" class="o"/>
  {''.join(f'<path d="M{-30+i*15} -10l14-10" stroke="#6a4a2a" stroke-width="3" fill="none"/>' for i in range(5))}</g>
<g transform="translate(250 130)">
  <ellipse rx="54" ry="36" fill="#fffefd" class="o"/>
  <path d="M20-26q36-10 46-46" fill="none" stroke="#fffefd" stroke-width="20" stroke-linecap="round"/>
  <circle cx="66" cy="-72" r="18" fill="#fffefd" class="o"/>
  <path d="M82-76l50 8-48 16z" class="coral o"/>
  <circle cx="72" cy="-78" r="3.4" class="ink"/>
  <path d="M-50-10q-40 6-46 30" fill="none" stroke="#2f3542" stroke-width="10" stroke-linecap="round"/>
  <path d="M-10 34v26M14 34v26" stroke="{CRL}" stroke-width="7" fill="none" stroke-linecap="round"/></g>''')

add('strainer', '網の張った茶こしを通して、紅茶を注ぐ',
    'こし器、茶こし＝strainer。', f'''
{table(352)}
<g transform="translate(200 200) rotate(24)">
  <path d="M-60-60h120v80a40 40 0 0 1-40 40h-40a40 40 0 0 1-40-40z" fill="#fffefd" class="o"/>
  <path d="M-60-20q-50 0-56-40 30-12 56 20z" fill="#fffefd" class="o"/>
  <path d="M60-40q40 0 40 34t-40 34" fill="none" stroke="{INK}" stroke-width="9"/></g>
<g transform="translate(330 250)">
  <path d="M-54-20q0 46 54 46t54-46z" fill="#c3cbd1" class="o"/>
  <ellipse cy="-20" rx="54" ry="14" fill="#dfe6ea" class="o"/>
  {''.join(f'<circle cx="{-30+ (i%4)*20}" cy="{4+(i//4)*14}" r="3" fill="#8a97a3"/>' for i in range(8))}
  <path d="M54-20h40v10H54z" fill="#9aa7b1" class="o"/></g>
{''.join(drop(330, 296 + i * 22, 0.9, 'gold') for i in range(2))}
<g transform="translate(330 330)">
  <path d="M-50-30h100v40a24 24 0 0 1-24 24h-52a24 24 0 0 1-24-24z" fill="#fffefd" class="o"/>
  <path d="M-42-22h84v30a18 18 0 0 1-18 18h-48a18 18 0 0 1-18-18z" fill="#a2703a"/></g>''')

add('straw', '細い管をグラスに差し、飲み物を吸い上げる',
    'ストロー、麦わら＝straw。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-60-90l10 180h100l10-180z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="3"/>
  <path d="M-50-30h100l8 120h-116z" class="corald"/>
  <path d="M-60-90l10 180h100l10-180z" fill="none" class="o"/></g>
<g transform="translate(320 160) rotate(14)">
  <path d="M-10 0h20v190h-20z" class="coral o"/>
  {''.join(f'<path d="M-10 {20+i*40}h20v14h-20z" fill="#fffefd"/>' for i in range(4))}
  <path d="M-10-30q0-30 30-30h20v20h-20q-10 0-10 10z" class="coral o"/></g>''')

add('striker', 'ゴール前で走りこんだ選手が、ボールを強く蹴る',
    '(サッカーの)ストライカー＝striker。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<g transform="translate(470 320)">
  <path d="M-120-160h240v160h-240z" fill="none" stroke="#fffefd" stroke-width="10"/>
  {''.join(f'<path d="M{-110+i*40} -156v152" stroke="#fffefd" stroke-width="2.5" fill="none" opacity="0.8"/>' for i in range(6))}</g>
{person(210, 340, 1.35, 1, 'coral', 'blue', 'walk', 'cap', 'flat')}
<g transform="translate(310 320)">
  <circle r="30" fill="#fffefd" class="o"/>
  <path d="M0-18l16 12-6 20h-20l-6-20z" class="ink"/></g>
{arc(350, 290, 470, 240, 60, MUTED, True, 5)}''', arrow=True)

add('stripe', '布の上に、色の帯が等間隔で並ぶ',
    '縞、ストライプ＝stripe。', f'''
<g transform="translate(300 210)">
  <path d="M-230-140h460v280h-460z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="{-230+i*80}" y="-140" width="40" height="280" fill="{"#238b83" if i%2 else "#4e86c6"}"/>' for i in range(6))}
  <path d="M-230-140h460v280h-460z" fill="none" class="o"/></g>
<path d="M60 350h60" fill="none" stroke="{MUTED}" stroke-width="0"/>
<path d="M70 356h80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

add('stroller', '折りたためる軽いベビーカーに、子どもが座る',
    'ベビーカー＝stroller。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(300 300)">
  <path d="M-90-60h180v60a30 30 0 0 1-30 30h-120a30 30 0 0 1-30-30z" class="bluep o"/>
  <path d="M-90-60q20-70 90-70t90 70z" class="blue o"/>
  <circle cx="-70" cy="46" r="24" class="ink"/><circle cx="70" cy="46" r="24" class="ink"/>
  <path d="M-70 30L-90-60M70 30l20-90" stroke="{MUTED}" stroke-width="7" fill="none"/>
  <path d="M90-60l50-50h40" fill="none" stroke="{MUTED}" stroke-width="9" stroke-linecap="round"/></g>
{head(300, 250, 22, 'coral', 'short')}''')

add('stud', '革のベルトの表面に、金属の飾りびょうが並ぶ',
    '飾りびょう、スタッド＝stud。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-240-30h480v60h-480z" fill="#5b3a20" class="o"/>
  {''.join(f'<circle cx="{-200+i*50}" cy="0" r="13" fill="#c3cbd1" stroke="{INK}" stroke-width="2.5"/><circle cx="{-200+i*50}" cy="-3" r="6" fill="#eef2f4"/>' for i in range(9))}</g>
{ring(300, 260, 0, True)}
{''.join(f'<path d="M{{}} 160h-60" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(420) for _ in range(1))}''', arrow=True)

add('stump', '切り倒した木のあとに残った切り株が、年輪を見せる',
    '切り株＝stump。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<g transform="translate(300 320)">
  <path d="M-90 0v-90h180V0z" fill="#a0764a" class="o"/>
  <ellipse cy="-90" rx="90" ry="30" fill="#d8b478" class="o"/>
  {''.join(f'<ellipse cy="-90" rx="{74-i*18}" ry="{24-i*6}" fill="none" stroke="#b08a52" stroke-width="3"/>' for i in range(4))}
  <path d="M-90-40q-30 10-40 40 30 6 46-16" fill="#8a6a46" class="o"/>
  <path d="M90-50q30 14 36 44-30 4-44-20" fill="#8a6a46" class="o"/></g>
{''.join(flower(120 + i * 380, 350, 0.45, 'coral') for i in range(2))}''')

add('sugar', '角砂糖が容器に入り、コーヒーに落とされる',
    '砂糖＝sugar。', f'''
{table(352)}
<g transform="translate(190 280)">
  <path d="M-70-50h140v70a24 24 0 0 1-24 24h-92a24 24 0 0 1-24-24z" fill="#fffefd" class="o"/>
  <ellipse cy="-50" rx="70" ry="18" fill="#f2f6f8" class="o"/>
  {''.join(f'<rect x="{-40+ (i%3)*30}" y="{-62-(i//3)*24}" width="26" height="22" rx="3" fill="#fffefd" stroke="{INK}" stroke-width="2"/>' for i in range(5))}</g>
<g transform="translate(430 280)">
  <path d="M-60-40h120v56a40 40 0 0 1-40 40h-40a40 40 0 0 1-40-40z" fill="#fffefd" class="o"/>
  <path d="M60-24q40 0 40 30t-40 30" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-50-30h100v42a32 32 0 0 1-32 32h-36a32 32 0 0 1-32-32z" fill="#7a4a28"/></g>
<g transform="translate(430 180) rotate(20)"><rect x="-15" y="-13" width="30" height="26" rx="3" fill="#fffefd" stroke="{INK}" stroke-width="2.5"/></g>
{line(430, 210, 430, 234, MUTED, True, 4)}''', arrow=True)

add('sundial', '日時計の板に立てた針の影が、時刻を指す',
    '日時計＝sundial。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
{sun(120, 90, 40)}
<g transform="translate(330 300)">
  <path d="M-20 30v60h40V30z" fill="{STONE}" class="o"/>
  <ellipse rx="140" ry="42" fill="#cfd6db" class="o"/>
  <ellipse rx="118" ry="34" fill="#dfe6ea" class="o"/>
  {''.join(f'<path d="M{int(108*math.cos(math.radians(a)))} {int(30*math.sin(math.radians(a)))}l{int(-16*math.cos(math.radians(a)))} {int(-6*math.sin(math.radians(a)))}" stroke="{INK}" stroke-width="3" fill="none"/>' for a in range(180, 361, 20))}
  <path d="M-6 0h12l40-70h-20z" fill="#8a97a3" class="o"/>
  <path d="M6 0L96 16" stroke="{MUTED}" stroke-width="9" fill="none" opacity="0.6"/></g>''')

add('sunhat', 'つばの広い麦わらの帽子が、日差しをさえぎる',
    '日よけ帽＝sunhat。', f'''
{sun(490, 90, 40)}
{table(352)}
<g transform="translate(280 270)">
  <ellipse rx="150" ry="40" fill="#e0c48c" class="o"/>
  <path d="M-70-10q0-80 70-80t70 80z" fill="#e0c48c" class="o"/>
  <path d="M-74-14q74-26 148 0v14h-148z" class="coral o"/>
  {''.join(f'<ellipse rx="{150-i*24}" ry="{40-i*7}" fill="none" stroke="#c8a05f" stroke-width="2.5"/>' for i in range(1, 4))}</g>''')

add('sunscreen', 'チューブから出した白いクリームを、腕に塗る',
    '日焼け止め＝sunscreen。', f'''
{sun(500, 80, 36)}
<g transform="translate(300 280)">
  <path d="M-200 60q40-120 160-140 110-18 180 30" fill="none" stroke="{SKIN}" stroke-width="66" stroke-linecap="round"/></g>
<g transform="translate(180 130) rotate(34)">
  <path d="M-30-56h60v100a22 22 0 0 1-22 22h-16a22 22 0 0 1-22-22z" fill="#fffefd" class="o"/>
  <path d="M-16-78h32v22h-32z" class="gold o"/>
  <circle cy="-20" r="14" class="goldp o"/></g>
{''.join(f'<path d="M{{}} {{}}q22-10 44 0" fill="none" stroke="#fffefd" stroke-width="10" stroke-linecap="round"/>'.format(250 + i * 50, 230 + (i % 2) * 24) for i in range(3))}''')

add('supper', '夜おそく、軽い食事とスープが食卓に並ぶ',
    '夕食、夜食＝supper。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v250h-600z" fill="#3b4557"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="2.5" fill="#fff6d8"/>'.format(50 + (i * 79) % 500, 30 + (i * 41) % 70) for i in range(7))}
{table(300)}
<g transform="translate(250 286)">
  <path d="M-70-22q0 44 70 44t70-44z" fill="#fffefd" class="o"/>
  <ellipse cy="-22" rx="70" ry="20" fill="#fffefd" class="o"/>
  <ellipse cy="-20" rx="56" ry="14" fill="#c8873f"/></g>
<g transform="translate(410 280)">
  <path d="M-16 0q-4-50 0-60h32q4 10 0 60z" fill="#f0e6d2" class="o"/>
  {flame(0, -66, 0.22)}</g>
{clock(120, 140, 38, 9, 0)}''')

add('surfing', '波の上に立った人が、板に乗って滑る',
    'サーフィン＝surfing。', f'''
<path d="M0 200h600v200H0z" class="bluep"/>
<path d="M0 260q80-70 180-40t180 40 240-20v160H0z" fill="#8fc0e0" class="o"/>
{''.join(f'<path d="M{{}} 320q22-14 44 0" fill="none" stroke="#6aa8d0" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(280 240) rotate(-16)">
  <ellipse rx="110" ry="22" class="coral o"/>
  <path d="M-90 0h180" fill="none" stroke="{CRLD}" stroke-width="3"/></g>
{person(280, 226, 1.05, 1, 'teal', 'gold', 'up', 'short', 'smile')}
{sun(510, 80, 34)}''')

add('tablecloth', '食卓いっぱいに布をかけ、ふちが垂れ下がる',
    'テーブルクロス＝tablecloth。', f'''
<g transform="translate(300 300)">
  <path d="M-200-40h400v20h-400z" fill="#c9a464" class="o"/>
  <path d="M-160 0v80M160 0v80" stroke="{BRN}" stroke-width="14" fill="none"/></g>
<g transform="translate(300 250) rotate(0)">
  <path d="M-230-30h460v60l-30 60h-400l-30-60z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{-200+i*66} -30v112" stroke="#d8e8e4" stroke-width="9" fill="none"/>' for i in range(7))}
  {''.join(f'<path d="M-230 {-10+i*24}h460" stroke="#d8e8e4" stroke-width="9" fill="none"/>' for i in range(2))}
  <path d="M-230-30h460v60l-30 60h-400l-30-60z" fill="none" class="o"/></g>''')

add('tadpole', '丸い頭と細い尾をもつオタマジャクシが、池を泳ぐ',
    'オタマジャクシ＝tadpole。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#cfe4f0"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><ellipse rx="30" ry="24" fill="#3f3830" stroke="{INK}" stroke-width="2.5"/><path d="M-28 0q-40 0-60-20 10 24 0 40 20-20 60-20z" fill="#3f3830" stroke="{INK}" stroke-width="2"/><circle cx="12" cy="-6" r="4" fill="#fffefd"/></g>'.format(x, y, r) for x, y, r in [(200, 150, -10), (350, 220, 14), (250, 300, -20), (430, 120, 8)])}
{''.join(f'<path d="M{{}} 380q0-120 20-180" fill="none" stroke="#3f8f6a" stroke-width="12" stroke-linecap="round"/>'.format(60 + i * 60) for i in range(3))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="none" stroke="#9fc8dd" stroke-width="2.5"/>'.format(120 + (i * 97) % 400, 70 + (i * 53) % 220, 6 + i % 3) for i in range(6))}''')

add('tanker', '油を運ぶ大きなタンカーが、港に停まっている',
    'タンカー、タンク車＝tanker。', f'''
<path d="M0 260h600v140H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 300q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 270)">
  <path d="M-250 0h500l-40 50h-420z" fill="#2f3542" class="o"/>
  <path d="M-250-40h500v40h-500z" class="coral o"/>
  {''.join(f'<ellipse cx="{-180+i*70}" cy="-70" rx="34" ry="30" fill="#c3cbd1" stroke="{INK}" stroke-width="2.5"/>' for i in range(5))}
  <path d="M170-100h90v60h-90z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="{184+i*28}" y="-88" width="18" height="16" class="bluep o"/>' for i in range(3))}</g>''')

add('tapestry', '絵柄を織りこんだ厚い布が、壁に掛かる',
    'つづれ織り、タペストリー＝tapestry。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#e4dccb"/></g>
<g transform="translate(300 210)">
  <path d="M-180-50h360v12h-360z" fill="{BRN}" class="o"/>
  <path d="M-160-38h320v230h-320z" fill="#8a5c6a" class="o"/>
  <path d="M-140-18h280v190h-280z" fill="#a2707c" class="o"/>
  {tree(-80, 130, 0.55)}
  <g transform="translate(60 60)"><path d="M-40 60v-80q40-24 80 0v80z" class="gold o"/><circle cy="-40" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/></g>
  {''.join(f'<path d="M-160 {-30+i*40}h320" stroke="#8a5c6a" stroke-width="2" fill="none" opacity="0.5"/>' for i in range(6))}
  {''.join(f'<path d="M-150 192v18" stroke="#a2707c" stroke-width="0"/>' for _ in range(0))}
  {''.join(f'<path d="M{-140+i*40} 192v20" stroke="#a2707c" stroke-width="6" fill="none" stroke-linecap="round"/>' for i in range(8))}</g>''')

add('tar', '黒くねばるタールを道路に流し、ならしていく',
    'タール、コールタール＝tar。', f'''
<path d="M0 240h600v160H0z" fill="#cbb896"/>
<g transform="translate(300 300)">
  <path d="M-260-30h520v70h-520z" fill="#2f2a24" class="o"/>
  <path d="M-260-30q80-16 160 0t180 0 180 0v14h-520z" fill="#4a443c"/></g>
<g transform="translate(180 210) rotate(30)">
  <path d="M-40-60h80v100a24 24 0 0 1-24 24h-32a24 24 0 0 1-24-24z" fill="#4e5a66" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q-10 22 0 40" fill="none" stroke="#2f2a24" stroke-width="10" stroke-linecap="round"/>'.format(250 + i * 10, 220 + i * 10) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}q14-20 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(430 + i * 22, 230 - i * 14) for i in range(2))}''')

add('tarpaulin', '青い防水シートを広げて、荷の上をおおう',
    '防水シート、ブルーシート＝tarpaulin。', f'''
{table(352)}
{''.join(box(250 + i * 80, 290, 70, 50, 16, 'gold') for i in range(2))}
<g transform="translate(300 250) rotate(-4)">
  <path d="M-190-40q190-40 380 0 20 80 0 110-190 34-380 0-20-30 0-110z" fill="#3f78c0" class="o"/>
  {''.join(f'<circle cx="{-170+i*85}" cy="-14" r="8" fill="#dfeaf2" stroke="{INK}" stroke-width="2"/>' for i in range(5))}
  <path d="M-190-40q190-40 380 0" fill="none" stroke="#2f5a94" stroke-width="4"/></g>''')

add('tassel', '糸を束ねて垂らした房飾りが、カーテンの端に下がる',
    '房飾り、タッセル＝tassel。', f'''
<g transform="translate(300 190)">
  <path d="M-240-160h480v20h-480z" fill="{BRN}" class="o"/>
  <path d="M-220-140q-20 180 0 290h140q-20-110 0-290z" class="violet o"/>
  <path d="M220-140q20 180 0 290H80q20-110 0-290z" class="violet o"/></g>
<g transform="translate(300 220)">
  <path d="M-90 0q90 40 180 0" fill="none" stroke="{GLD}" stroke-width="8"/>
  <circle cx="0" cy="36" r="18" class="gold o"/>
  {''.join(f'<path d="M{-22+i*8} 52v66" stroke="{GLDD}" stroke-width="5" fill="none" stroke-linecap="round"/>' for i in range(7))}
  <path d="M-26 52h52v12h-52z" class="goldd o"/></g>''')

add('teapot', '注ぎ口と取っ手とふたのついた急須から、茶を注ぐ',
    'ティーポット、急須＝teapot。', f'''
{table(352)}
<g transform="translate(280 260) rotate(20)">
  <path d="M-90-40h180v60a70 70 0 0 1-70 70h-40a70 70 0 0 1-70-70z" class="coral o"/>
  <path d="M-90-10q-60 0-70-50 36-16 70 26z" class="coral o"/>
  <path d="M90-10q50 0 50 40t-50 40" fill="none" stroke="{CRL}" stroke-width="16"/>
  <path d="M-50-40q50-26 100 0z" class="corald o"/>
  <circle cy="-52" r="12" class="corald o"/></g>
{''.join(drop(160, 250 + i * 26, 1.0, 'gold') for i in range(2))}
<g transform="translate(150 320)">
  <path d="M-44-24h88v30a20 20 0 0 1-20 20h-48a20 20 0 0 1-20-20z" fill="#fffefd" class="o"/>
  <path d="M-36-16h72v22a16 16 0 0 1-16 16h-40a16 16 0 0 1-16-16z" fill="#a2703a"/></g>''')

add('thermos', '外が銀色の保温ボトルのふたに、湯気の立つ湯を注ぐ',
    '魔法びん、保温ボトル＝thermos。', f'''
{table(352)}
<g transform="translate(260 260) rotate(24)">
  <path d="M-46-90h92v170a22 22 0 0 1-22 22h-48a22 22 0 0 1-22-22z" fill="#c3cbd1" class="o"/>
  <path d="M-34-112h68v22h-68z" class="coral o"/>
  <path d="M-46-20h92v60h-92z" fill="#9aa7b1"/></g>
<g transform="translate(410 300)">
  <path d="M-44-30h88v40a24 24 0 0 1-24 24h-40a24 24 0 0 1-24-24z" fill="#dfe6ea" class="o"/>
  <path d="M-36-22h72v30a18 18 0 0 1-18 18h-36a18 18 0 0 1-18-18z" fill="#a2703a"/></g>
{''.join(f'<path d="M{{}} {{}}q14-20 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(390 + i * 26, 240 - i * 12) for i in range(2))}''')

add('thimble', '針を押すため、指先に金属のふたをはめる',
    '指ぬき＝thimble。', f'''
{table(352)}
<g transform="translate(280 280)">
  <path d="M-70 70q-14-40 10-56 24-16 60 0 30 14 20 56z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40 20q0-80 40-80t40 80z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-36-14q0-46 36-46t36 46z" fill="#c3cbd1" class="o"/>
  {''.join(f'<circle cx="{-22+ (i%4)*15}" cy="{-24-(i//4)*14}" r="2.6" fill="#8a97a3"/>' for i in range(8))}</g>
<g transform="translate(430 200) rotate(20)">
  <path d="M-3-80h6v160h-6z" fill="#c3cbd1" class="o"/>
  <circle cy="-86" r="7" fill="none" stroke="#c3cbd1" stroke-width="4"/></g>
{ring(280, 240, 66, True)}''')

add('tick', '正しい答えの横に、チェックの印が書き入れられる',
    'チェック印／ダニ＝tick。', f'''
{table(352)}
<g transform="translate(280 250)">
  <path d="M-160-110h320v220h-320z" class="paper"/>
  {''.join(f'<g><rect x="-130" y="{-84+i*54}" width="24" height="24" rx="4" fill="none" stroke="{MUTED}" stroke-width="3"/><rect x="-90" y="{-80+i*54}" width="{190-(i%3)*50}" height="14" rx="7" fill="{MUTED}"/></g>' for i in range(4))}
  {''.join(tick(-118 + 0, -72 + i * 54, 0.3) for i in range(3))}</g>
<g transform="translate(480 160) rotate(34)">
  <path d="M-8-70h16v100l-8 20-8-20z" class="green o"/></g>''')

add('tile', '正方形のタイルを並べて、壁を貼りそろえる',
    'タイル、瓦＝tile。', f'''
<g transform="translate(300 210)">
  <path d="M-240-150h480v300h-480z" fill="#e4dccb" class="o"/>
  {''.join(f'<rect x="{-230+ (i%7)*66}" y="{-140+(i//7)*66}" width="60" height="60" rx="4" fill="{"#dff4ef" if (i//7+i%7)%2 else "#bfe4dc"}" stroke="{INK}" stroke-width="2"/>' for i in range(28))}</g>
<g transform="translate(460 300) rotate(14)">
  <rect x="-30" y="-30" width="60" height="60" rx="4" fill="#bfe4dc" stroke="{INK}" stroke-width="2.5"/></g>
{hand(460, 220, 1)}
{line(460, 250, 460, 270, MUTED, True, 4)}''', arrow=True)

add('toffee', '包み紙をひねった粘る飴が、皿に盛られる',
    'タフィー、砂糖とバターの飴＝toffee。', f'''
{table(352)}
<g transform="translate(300 290)">
  <ellipse rx="130" ry="34" fill="#fffefd" class="o"/>
  {''.join(f'<g transform="translate({-70+ (i%4)*46} {-20-(i//4)*26}) rotate({-20+i*12})"><rect x="-24" y="-14" width="48" height="28" rx="5" fill="#c8873f" stroke="{INK}" stroke-width="2"/><path d="M-24-6l-16-8v28l16-8zM24-6l16-8v28l-16-8z" fill="#e0b872" stroke="{INK}" stroke-width="2"/></g>' for i in range(7))}</g>''')

add('toothache', '片ほおを手で押さえ、歯の痛みに顔をしかめる',
    '歯痛＝toothache。', f'''
<g transform="translate(280 220)">
  <circle r="110" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-108-40q10-80 108-80t108 80q-46-36-108-24-62-12-108 24z" fill="{HAIR}"/>
  <path d="M-44-14l24 12M44-14l-24 12" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-26 54q26-22 52 0" fill="none" stroke="{INK}" stroke-width="5"/>
  <circle cx="66" cy="30" r="30" class="coralp"/></g>
{hand(400, 260, -1)}
{''.join(f'<path d="M{int(280+124*math.cos(math.radians(a)))} {int(220+124*math.sin(math.radians(a)))}l{int(28*math.cos(math.radians(a)))} {int(28*math.sin(math.radians(a)))}" stroke="{CRL}" stroke-width="6" fill="none" stroke-linecap="round"/>' for a in (-40, -10, 20, 50))}''')

add('torch', '手に持った懐中電灯が、暗がりに光の筋を投げる',
    '懐中電灯、たいまつ＝torch。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#2f3a4d"/></g>
<g transform="translate(180 240) rotate(16)">
  <path d="M-70-24h120v48h-120z" fill="#4e5a66" class="o"/>
  <path d="M50-34h30v68H50z" fill="#8a97a3" class="o"/>
  <path d="M-70-18h20v36h-20z" fill="#2f3542"/></g>
<path d="M270 220L560 130 560 330z" fill="#fff6d8" opacity="0.45"/>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#fff6d8" opacity="0.6"/>'.format(340 + (i * 61) % 200, 180 + (i * 43) % 120) for i in range(6))}''')

add('tractor', '大きな後輪をもつトラクターが、畑を走る',
    'トラクター＝tractor。', f'''
<path d="M0 320h600v80H0z" fill="#5b4636"/>
{''.join(f'<path d="M{{}} 400q20-50 0-80" fill="none" stroke="#3f3126" stroke-width="8"/>'.format(60 + i * 100) for i in range(6))}
<g transform="translate(300 300)">
  <circle cx="80" cy="20" r="64" class="ink"/>
  <circle cx="80" cy="20" r="34" fill="#9aa7b1"/>
  <circle cx="-90" cy="44" r="36" class="ink"/>
  <circle cx="-90" cy="44" r="18" fill="#9aa7b1"/>
  <path d="M-120-10h150v50h-150z" class="green o"/>
  <path d="M10-70h90v60h-90z" class="green o"/>
  <path d="M20-66h70v40H20z" fill="#dfeaf2" class="o"/>
  <path d="M-120-10v-30h40v30" fill="#2a6b4c" class="o"/>
  <path d="M-104-40v-30h14v30z" fill="#2f3542"/></g>
{''.join(f'<path d="M{{}} {{}}q12-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(190 + i * 18, 200 - i * 14) for i in range(2))}''')

add('trainers', 'ゴム底のスニーカーが、ひもを結んで一足並ぶ',
    'スニーカー、運動靴＝trainers。', f'''
{table(352)}
{''.join(f'<g transform="translate({{}} 290) rotate({{}})"><path d="M-90 30q0-56 46-56h40l70 34v22z" fill="#fffefd" class="o"/><path d="M-90 30h156v16h-156z" class="teal o"/><path d="M-50-20h50v40h-50z" fill="#dff4ef" class="o"/>{{}}<path d="M-40-26q-20-24 0-30 14-4 18 12" fill="none" stroke="{TEAD}" stroke-width="5"/></g>'.format(x, r, ''.join(f'<path d="M{-44+j*18} {-14+j*2}l16 14" stroke="{TEAD}" stroke-width="4" fill="none"/>' for j in range(3))) for x, r in [(190, -4), (410, 4)])}''')

add('tram', '道路の線路の上を、架線につながれた路面電車が走る',
    '路面電車＝tram。', f'''
<path d="M0 320h600v80H0z" fill="#9aa7b1"/>
<path d="M0 350h600M0 372h600" stroke="#6b7680" stroke-width="6" fill="none"/>
<path d="M40 100h520" fill="none" stroke="{INK}" stroke-width="5"/>
{''.join(f'<path d="M{{}} 320v-220" stroke="{MUTED}" stroke-width="9" fill="none"/>'.format(60 + i * 480) for i in range(2))}
<g transform="translate(300 340)">
  <path d="M-170 0v-150h340V0z" class="coral o"/>
  <path d="M-150-130h100v60h-100zM-30-130h100v60H-30zM90-130h60v60H90z" class="bluep o"/>
  <path d="M-40-60h80v60h-80z" class="corald o"/>
  <path d="M0-150l-40-50h80z" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="-100" cy="10" r="20" class="ink"/><circle cx="100" cy="10" r="20" class="ink"/></g>''')

finish(__file__)
