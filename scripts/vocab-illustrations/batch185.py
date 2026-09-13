# -*- coding: utf-8 -*-
"""第185回。plus33 の50語。crate / flannel / corkscrew の描き直しも含む。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

add('crate', '縦板の隙間から中身が見える木箱に、果物が入っている',
    '木箱、輸送用の箱＝crate。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-140-60h280v110h-280z" fill="#fffaf1" class="o"/>
  {''.join(f'<rect x="{-134+i*40}" y="-60" width="24" height="110" fill="#c9a464" stroke="{INK}" stroke-width="2"/>' for i in range(7))}
  <path d="M-140-60h280v16h-280zM-140 34h280v16h-280z" fill="#a0764a" class="o"/>
  <path d="M-140-60h280v110h-280z" fill="none" class="o"/></g>
{''.join(f'<circle cx="{{}}" cy="184" r="26" class="{{}} o"/>'.format(240 + i * 60, c) for i, c in enumerate(['coral', 'gold', 'coral']))}''')

add('corkscrew', 'T字の柄のついた栓抜きのらせんが、コルクにねじこまれている',
    'コルク抜き、栓抜き＝corkscrew。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-40-60h80v100h-80z" fill="#3a6b3a" class="o"/>
  <path d="M-40-60h80v-20h-80z" fill="#2a5a2a" class="o"/>
  <path d="M-30-40h60v34h-60z" fill="#fffefd" class="o"/></g>
<g transform="translate(300 200)">
  <path d="M-70-70h140v24h-140z" fill="{BRN}" class="o"/>
  <path d="M-12-46h24v40h-24z" fill="#9aa7b1" class="o"/>
  <path d="M0-6q-24 12 0 24t0 24-24 24 0 24" fill="none" stroke="#9aa7b1" stroke-width="8" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} 150q10-14 0-26" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(420 + i * 20) for i in range(2))}''')

add('flannel', 'やわらかい格子模様のフランネルのシャツが掛かっている',
    'フランネル＝flannel。', f'''
<g transform="translate(300 210)">
  <path d="M-110-90h220v240h-220z" fill="#c96a5a" class="o"/>
  {''.join(f'<path d="M{-92+i*38} -90v240" stroke="#e28a78" stroke-width="10" fill="none" opacity="0.8"/>' for i in range(5))}
  {''.join(f'<path d="M-110 {-60+i*44}h220" stroke="#e28a78" stroke-width="10" fill="none" opacity="0.8"/>' for i in range(5))}
  <path d="M-110-90l-60 40 34 90 26-14" fill="#c96a5a" class="o"/>
  <path d="M110-90l60 40-34 90-26-14" fill="#c96a5a" class="o"/>
  <path d="M-30-90q30 30 60 0l-18 60h-24z" fill="#fffaf1" class="o"/>
  <path d="M-4-30v180" fill="none" stroke="#8f4438" stroke-width="4"/>
  {''.join(f'<circle cx="-4" cy="{0+i*40}" r="6" class="goldp o"/>' for i in range(4))}
  <path d="M-110-90h220v240h-220z" fill="none" class="o"/></g>
<g transform="translate(300 96)"><path d="M-20-20h40v20h-40z" fill="{MUTED}"/><path d="M0-20v-30" stroke="{MUTED}" stroke-width="5" fill="none"/></g>''')

# --- plus33 ------------------------------------------------------------------

add('foam', 'コーヒーの表面に、細かい白い泡の層がのっている',
    '泡、発泡素材＝foam。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-90-60h180v90a40 40 0 0 1-40 40h-100a40 40 0 0 1-40-40z" fill="#fffefd" class="o"/>
  <path d="M90-40q40 0 40 30t-40 30" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-78-20h156v46a32 32 0 0 1-32 32h-92a32 32 0 0 1-32-32z" fill="#7a4a28"/>
  <path d="M-80-34q80-30 160 0v18h-160z" fill="#f4efe2"/>
  {''.join(f'<circle cx="{-60+i*24}" cy="{-36+(i%2)*8}" r="{10-(i%3)*2}" fill="#fffefd" stroke="{MUTED}" stroke-width="2"/>' for i in range(6))}
  <ellipse cy="66" rx="110" ry="20" fill="#fffefd" class="o"/></g>''')

add('foggy', '霧が濃く、少し先の木も家もぼんやりとしか見えない',
    '霧の深い＝foggy。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<g opacity="0.3">{house(200, 320, 0.9, 'coral')}{tree(430, 320, 1.0)}</g>
{''.join(f'<g opacity="0.75"><path d="M{{}} {{}}h220" stroke="#e6eaec" stroke-width="{{}}" fill="none" stroke-linecap="round"/></g>'.format(40 + (i % 2) * 140, 100 + i * 40, 26 - (i % 3) * 4) for i in range(7))}
{person(110, 350, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'flat')}
{''.join(f'<g opacity="0.6"><path d="M{{}} {{}}h180" stroke="#eef1f2" stroke-width="22" fill="none" stroke-linecap="round"/></g>'.format(220 + (i % 2) * 120, 250 + i * 36) for i in range(3))}''')

add('foil', '銀色のアルミホイルを広げ、魚を包む',
    'アルミホイル＝foil。', f'''
{table(352)}
<g transform="translate(300 270)">
  <path d="M-160-60q40 20 80 0t80 0 80 0 80 0v100q-40-20-80 0t-80 0-80 0-80 0z" fill="#d6dde1" class="o"/>
  {''.join(f'<path d="M{-120+i*60} -50v90" stroke="#b9c2c8" stroke-width="3" fill="none"/>' for i in range(5))}</g>
<g transform="translate(300 260)">
  <ellipse rx="80" ry="34" fill="#a8c8d8" class="o"/>
  <path d="M76 0l34-22v44z" fill="#a8c8d8" class="o"/>
  <circle cx="-46" cy="-8" r="4" class="ink"/></g>
<g transform="translate(120 160)">
  <path d="M-40-40h80v70l-40 20-40-20z" fill="#d6dde1" class="o"/></g>''')

add('footpath', '車の通れない細い小道が、草の間を抜けていく',
    '歩道、小道＝footpath。', f'''
<path d="M0 200h600v200H0z" class="greenp"/>
<path d="M260 400q10-140 60-200t20-50h-80q-30 60-60 250z" fill="#d8cdb6" class="o"/>
{''.join(f'<g transform="translate({{}} {{}}) rotate(-10)"><ellipse rx="11" ry="17" class="ink" opacity="0.4"/></g>'.format(300 + (i % 2) * 26 - 10, 360 - i * 40) for i in range(4))}
{tree(110, 300, 1.1)}{tree(500, 290, 0.9)}
{''.join(flower(180 + i * 60, 340, 0.45, c) for i, c in enumerate(['coral', 'gold']))}''')

add('footprint', '雪の上に、かかとからつま先までの形がくっきり残る',
    '足あと＝footprint。', f'''
<path d="M0 150h600v250H0z" fill="#eef4f7"/>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><ellipse rx="26" ry="42" class="ink"/><ellipse cy="-52" rx="19" ry="15" class="ink"/></g>'.format(110 + i * 90, 330 - i * 42, -12 + (i % 2) * 8) for i in range(5))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#ffffff" stroke="{MUTED}" stroke-width="1.2"/>'.format(60 + (i * 83) % 500, 60 + (i * 37) % 60) for i in range(6))}
{ring(110, 320, 62, True)}''')

add('fountain', '広場の噴水から水が高く上がり、下の池に落ちる',
    '噴水、泉＝fountain。', f'''
<path d="M0 320h600v80H0z" class="ground"/>
<g transform="translate(300 320)">
  <ellipse rx="180" ry="44" class="bluep o"/>
  <path d="M-30 0v-70h60V0z" fill="{STONE}" class="o"/>
  <ellipse cy="-70" rx="80" ry="20" fill="{STONE}" class="o"/>
  <path d="M-12-70v-70h24V70z" fill="none" stroke="{STONE}" stroke-width="0"/>
  <path d="M-10-70v-60h20v60z" fill="{STONE}" class="o"/></g>
{''.join(f'<path d="M300 190q{{}} -60 {{}} 40" fill="none" stroke="{BLU}" stroke-width="8" stroke-linecap="round"/>'.format(dx, dx * 2) for dx in (-50, -20, 20, 50))}
{''.join(drop(300 + (i - 1) * 60, 160 + (i % 2) * 20, 1.0, 'blue') for i in range(3))}
{''.join(f'<path d="M{{}} 330q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(150 + i * 100) for i in range(3))}''')

add('foyer', '劇場の入口の広いホールで、開場を待つ人が立つ',
    'ロビー、玄関ホール＝foyer。', f'''
<g transform="translate(300 200)">
  <path d="M-280-180h560v360h-560z" fill="#f2e9d8" class="o"/>
  <path d="M-280-180h560v40h-560z" class="goldp o"/></g>
<g transform="translate(300 340)">
  <path d="M-110-190h220v190h-220z" class="corald o"/>
  <path d="M-90-170h180v170h-180z" fill="#8a3a30" class="o"/>
  <path d="M0-170v170" stroke="{GLD}" stroke-width="6" fill="none"/></g>
{person(120, 330, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(480, 330, 1.0, -1, 'violet', 'green', 'stand', 'bun', 'smile')}
<g transform="translate(300 90)"><path d="M0 0v40" stroke="{GLDD}" stroke-width="6" fill="none"/>
  {''.join(f'<path d="M0 40q{dx} 20 {dx} 36" fill="none" stroke="{GLDD}" stroke-width="4"/><circle cx="{dx}" cy="84" r="10" class="goldp o"/>' for dx in (-40, 0, 40))}</g>''')

add('frosty', '朝の草や窓が白い霜におおわれている',
    '霜の降りた、凍えるような＝frosty。', f'''
<path d="M0 260h600v140H0z" fill="#e8f0f2"/>
{''.join(f'<g transform="translate({{}} 300)"><path d="M0 60V0" stroke="#b8c8c4" stroke-width="6" fill="none"/><path d="M0 20q-20-14-24-34 22 4 24 34zM0 6q20-14 24-34-22 4-24 34z" fill="#dfeceb" stroke="{MUTED}" stroke-width="2"/></g>'.format(80 + i * 70) for i in range(7))}
<g transform="translate(300 120)">
  <path d="M-130-80h260v160h-260z" fill="#dfeaf2" class="o"/>
  {''.join(f'<g transform="translate({-70+ (i%3)*70} {-40+(i//3)*70})">{"".join(f"<path d=\'M0 0v-26\' transform=\'rotate({a})\' stroke=\'#ffffff\' stroke-width=\'4\' fill=\'none\'/>" for a in range(0, 360, 60))}</g>' for i in range(6))}
  <path d="M0-80v160M-130 0h260" fill="none" stroke="{INK}" stroke-width="4"/></g>''')

add('rolling pin', '木のめん棒で、台の上の生地を平らに伸ばす',
    'めん棒＝rolling pin。', f'''
{table(352)}
<g transform="translate(300 300)">
  <path d="M-180-24q180-30 360 0v24h-360z" fill="#f0e0c0" class="o"/></g>
<g transform="translate(280 250)">
  <path d="M-110-24h220v48h-220z" fill="#c9a464" class="o"/>
  <ellipse cx="-110" cy="0" rx="12" ry="24" fill="#a0764a" class="o"/>
  <ellipse cx="110" cy="0" rx="12" ry="24" fill="#a0764a" class="o"/>
  <path d="M-150-10h40v20h-40zM110-10h40v20h-40z" fill="#a0764a" class="o"/></g>
{''.join(f'<path d="M{{}} 200h50" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(400) for _ in range(1))}''', arrow=True)

add('furnace', '真っ赤に燃える炉の中で、金属が溶けている',
    '炉、溶鉱炉＝furnace。', f'''
<g transform="translate(300 250)">
  <path d="M-170-140h340v280h-340z" fill="#6b5a4a" class="o"/>
  <path d="M-120-90h240v190h-240z" fill="#2f2620" class="o"/>
  <path d="M-100-70h200v150h-200z" fill="#e8402b"/>
  {flame(-40, 70, 0.7)}{flame(40, 70, 0.6)}{flame(0, 60, 0.9)}
  <path d="M-170-140h340v-30h-340z" fill="#5b4c3e" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{GLD}" stroke-width="5"/>'.format(500 + i * 18, 180 - i * 16) for i in range(2))}''')

add('gardening', '手袋をした人が、土に苗を植えて水をやる',
    '園芸、庭いじり＝gardening。', f'''
<path d="M0 280h600v120H0z" fill="#5b4636"/>
<path d="M0 280h600v14H0z" class="greenp"/>
{person(180, 330, 1.15, 1, 'teal', 'blue', 'reach', 'cap', 'smile')}
{hand(250, 250, 1)}
<g transform="translate(340 300)">
  <path d="M0 30v-50" stroke="{GRND}" stroke-width="7" fill="none"/>
  <path d="M0-30q-34-4-38-32 32-4 38 32z" class="green o"/>
  <path d="M0-40q34-4 38-32-32-4-38 32z" class="green o"/></g>
<g transform="translate(470 280) rotate(-14)">
  <path d="M-40-40h80v70h-80z" class="bluep o"/>
  <path d="M40-30h50l-10 20h-40z" class="bluep o"/>
  <path d="M-40-40q40-20 80 0" fill="none" stroke="{BLU}" stroke-width="6"/></g>
{''.join(drop(430 + i * 10, 290 + i * 18, 0.8, 'blue') for i in range(2))}''')

add('garland', '花と葉をつないだ飾りが、弧を描いて掛けられている',
    '花輪、花づな＝garland。', f'''
<g transform="translate(300 130)">
  <path d="M-230 0q230 190 460 0" fill="none" stroke="{GRND}" stroke-width="10"/>
  {''.join(f'<g transform="translate({-200+i*50} {abs(math.sin(i/8*math.pi))*150:.0f})"><ellipse rx="22" ry="13" class="green o" transform="rotate({-30+i*8})"/></g>' for i in range(9))}
  {''.join(flower(-170 + i * 74, abs(math.sin((i * 1.5 + 1) / 8 * math.pi)) * 150, 0.42, c) for i, c in enumerate(['coral', 'gold', 'violet', 'coral', 'gold']))}</g>
{''.join(f'<path d="M{{}} 120v-40" stroke="{MUTED}" stroke-width="5" fill="none"/>'.format(70 + i * 460) for i in range(2))}''')

add('gel', 'チューブから出したジェルが、手のひらでとろりと光る',
    'ジェル、ゲル状のもの＝gel。', f'''
{table(352)}
<g transform="translate(190 220) rotate(30)">
  <path d="M-34-80h68v130a24 24 0 0 1-24 24h-20a24 24 0 0 1-24-24z" class="violetp o"/>
  <path d="M-16-102h32v22h-32z" class="violet o"/></g>
{hand(340, 280, 1)}
<g transform="translate(340 256)">
  <path d="M-40 10q-14-30 10-40 20-8 36 6 20 16 4 34z" fill="#d8c8f0" stroke="{VIO}" stroke-width="3"/></g>
{''.join(spark(300 + i * 50, 200, 0.6, 'violet') for i in range(2))}''')

add('gemstone', '多面にカットされた石が、光を受けてきらめく',
    '宝石の原石、宝石＝gemstone。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-90-40h180l-30-50h-120z" class="tealp o"/>
  <path d="M-90-40h180L0 90z" class="teal o"/>
  <path d="M-90-40L0 90 -30-40zM90-40L0 90 30-40z" class="teald o"/>
  <path d="M-60-90h120" fill="none" stroke="#fffefd" stroke-width="4"/></g>
{''.join(spark(150 + i * 300, 140, 0.8, 'gold') for i in range(2))}
{''.join(f'<path d="M{{}} {{}}l20-22" fill="none" stroke="{GLD}" stroke-width="4"/>'.format(390 + i * 20, 200 - i * 16) for i in range(2))}''')

add('geyser', '地面の穴から熱い湯が柱のように高く噴き上がる',
    '間欠泉＝geyser。', f'''
<path d="M0 320h600v80H0z" fill="#cbb896"/>
<g transform="translate(300 320)">
  <ellipse rx="90" ry="26" fill="#8a7a6a" class="o"/>
  <ellipse rx="50" ry="14" fill="#4a3a2a"/></g>
<path d="M300 310q-30-160 0-240 30 80 0 240z" class="bluep o"/>
{''.join(f'<path d="M300 {{}}q{{}}-40 {{}}-60" fill="none" stroke="{BLU}" stroke-width="7" stroke-linecap="round"/>'.format(180, dx, dx * 2) for dx in (-40, 40))}
{''.join(f'<path d="M{{}} {{}}q16-22 0-40" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(380 + i * 30, 150 - i * 16) for i in range(3))}
{''.join(drop(260 + i * 80, 200 + (i % 2) * 30, 1.0, 'blue') for i in range(3))}''')

add('gingerbread', '人の形に焼いた菓子に、砂糖の飾りがついている',
    'ジンジャーブレッド＝gingerbread。', f'''
{table(352)}
<g transform="translate(300 250)">
  <circle cy="-80" r="46" fill="#c8873f" class="o"/>
  <path d="M-40-40q40-18 80 0 20 70 0 110h-80q-20-40 0-110z" fill="#c8873f" class="o"/>
  <path d="M-40-30l-70 40 14 30 60-30M40-30l70 40-14 30-60-30" fill="#c8873f" class="o"/>
  <path d="M-30 70l-20 66h30l20-56M30 70l20 66h-30l-20-56" fill="#c8873f" class="o"/>
  <circle cx="-16" cy="-88" r="6" fill="#fffefd"/><circle cx="16" cy="-88" r="6" fill="#fffefd"/>
  <path d="M-16-64q16 12 32 0" fill="none" stroke="#fffefd" stroke-width="5"/>
  {''.join(f'<circle cx="0" cy="{-10+i*36}" r="7" fill="#fffefd"/>' for i in range(3))}
  <path d="M-40-34q40 14 80 0" fill="none" stroke="#fffefd" stroke-width="4" stroke-dasharray="8 8"/></g>''')

add('glider', 'エンジンのない細長い翼の機体が、音もなく滑空する',
    'グライダー、滑空機＝glider。', f'''
{''.join(cloud(130 + i * 300, 90, 1.1, 'blue') for i in range(2))}
<g transform="translate(300 220) rotate(-8)">
  <path d="M-150 0h300v18h-300z" fill="#fffefd" class="o"/>
  <path d="M-30-6q30-30 70-6l-10 12z" fill="#dfe6ea" class="o"/>
  <path d="M-260-4h520v8h-520z" class="teal o"/>
  <path d="M-150 0l-30-40h20l40 40z" class="teald o"/>
  <path d="M-150 0l-30 40h20l40-40z" class="teald o"/>
  <circle cx="60" cy="4" r="8" fill="#dfeaf2" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q80-16 160 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>'.format(80, 300 + i * 34) for i in range(2))}''')

add('goalkeeper', 'ゴールの前で手袋をした選手が、飛んできたボールを止める',
    'ゴールキーパー＝goalkeeper。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<g transform="translate(300 320)">
  <path d="M-220-180h440v180h-440z" fill="none" stroke="#fffefd" stroke-width="10"/>
  {''.join(f'<path d="M{-210+i*40} -176v172" stroke="#fffefd" stroke-width="2.5" fill="none" opacity="0.8"/>' for i in range(11))}
  {''.join(f'<path d="M-216 {-160+i*40}h432" stroke="#fffefd" stroke-width="2.5" fill="none" opacity="0.8"/>' for i in range(4))}</g>
{person(280, 320, 1.3, 1, 'gold', 'violet', 'up', 'cap', 'flat')}
<g transform="translate(360 160)">
  <circle r="30" fill="#fffefd" class="o"/>
  <path d="M0-18l16 12-6 20h-20l-6-20z" class="ink"/></g>
{''.join(f'<path d="M{{}} {{}}h-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>'.format(470, 130 + i * 26) for i in range(2))}''')

add('godmother', '洗礼に立ち会う名づけ親が、赤ん坊にそっと手を添える',
    '名づけ親(女性)、代母＝godmother。', f'''
<g transform="translate(300 200)"><path d="M-260-160h520v320h-520z" fill="#f2e9d8" class="o"/></g>
<g transform="translate(300 300)">
  <path d="M-70-30h140v70h-140z" fill="{STONE}" class="o"/>
  <path d="M-90-30q90-40 180 0z" fill="#dfe6ea" class="o"/>
  <path d="M-56-46q56-26 112 0" fill="none" stroke="{BLU}" stroke-width="5"/></g>
{person(160, 340, 1.15, 1, 'violet', 'blue', 'reach', 'bun', 'smile')}
{person(450, 340, 1.05, -1, 'coral', 'green', 'carry', 'bob', 'smile')}
<g transform="translate(392 246) rotate(14)">
  <path d="M-40-14q40-20 80 0 8 30-8 38h-64q-16-8-8-38z" class="goldp o"/>
  <circle cx="-40" cy="-22" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/></g>
{''.join(spark(140 + i * 320, 130, 0.6, 'gold') for i in range(2))}''')

add('goggles', 'ゴムバンドのついた保護めがねで、目をおおう',
    'ゴーグル、保護めがね＝goggles。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-130-50h260v100h-260z" fill="none"/>
  <path d="M-120-50q-24 50 0 100h240q24-50 0-100z" class="tealp o"/>
  <circle cx="-56" cy="0" r="40" fill="#cfe4f0" class="o"/>
  <circle cx="56" cy="0" r="40" fill="#cfe4f0" class="o"/>
  <path d="M-16 0h32" stroke="{TEAD}" stroke-width="14" fill="none"/>
  <path d="M-120-20h-60v40h60M120-20h60v40h-60" fill="#2f3a4d" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q14-14 0-28" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(470 + i * 20, 170 - i * 14) for i in range(2))}''')

add('granddaughter', '祖母と並んで座る、幼い女の子の孫',
    '孫娘＝granddaughter。', f'''
{table(320)}
{chair(210, 320, 1.0, 'gold', 1)}
<g transform="translate(210 320)">{sit(0, 0, 1.05, 1, 'violet', 'blue', 'bun', 'smile', 'lap')}</g>
<g transform="translate(210 212)"><path d="M-26-16q26-22 52 0-8 18-26 18t-26-18z" fill="#d7d9dc"/></g>
<g transform="translate(390 320)">{sit(0, 0, 0.72, 1, 'coral', 'green', 'bob', 'smile', 'lap')}</g>
{chair(384, 320, 0.68, 'gold', 1)}
<path d="M250 250h100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{''.join(spark(120 + i * 380, 140, 0.6, 'gold') for i in range(2))}''')

add('grandfather', '白いひげの祖父が、いすに腰かけてほほえむ',
    '祖父＝grandfather。', f'''
{table(330)}
{chair(300, 330, 1.25, 'gold', 1)}
<g transform="translate(300 330)">{sit(0, 0, 1.3, 1, 'blue', 'green', 'short', 'smile', 'lap')}</g>
<g transform="translate(300 190)">
  <path d="M-34-18q4-38 34-38t34 36q-18-16-34-8-16-10-34 10z" fill="#d7d9dc"/>
  <path d="M-30 14q30 50 60 0-10 30-30 30t-30-30z" fill="#d7d9dc"/></g>
<g transform="translate(410 300)">
  <path d="M0-100v100" stroke="{BRN}" stroke-width="10" fill="none" stroke-linecap="round"/>
  <path d="M0-100q-26 0-26 20" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/></g>''')

add('grandmother', '眼鏡をかけた祖母が、編み物をしながら座る',
    '祖母＝grandmother。', f'''
{table(330)}
{chair(280, 330, 1.25, 'gold', 1)}
<g transform="translate(280 330)">{sit(0, 0, 1.3, 1, 'coral', 'violet', 'bun', 'smile', 'lap')}</g>
<g transform="translate(280 190)">
  <path d="M-36-16q4-38 36-38t36 36q-20-16-36-8-18-10-36 10z" fill="#d7d9dc"/>
  <circle cx="-12" cy="0" r="12" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="14" cy="0" r="12" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-1 0h4" stroke="{INK}" stroke-width="3" fill="none"/></g>
<g transform="translate(410 290)">
  <circle r="34" class="coral o"/>
  <path d="M-30-14q30 30 60 0" fill="none" stroke="{CRLD}" stroke-width="3"/>
  <path d="M28-16l40-30M34-6l44-14" stroke="{CRL}" stroke-width="4" fill="none"/></g>''')

add('grandson', '祖父の横に立つ、小さな男の子の孫',
    '孫息子＝grandson。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
{person(220, 350, 1.3, 1, 'blue', 'green', 'stand', 'short', 'smile')}
<g transform="translate(220 208)">
  <path d="M-32-16q4-36 32-36t32 34q-16-16-32-8-16-10-32 10z" fill="#d7d9dc"/></g>
{person(400, 350, 0.78, 1, 'coral', 'gold', 'up', 'cap', 'smile')}
<path d="M268 270h90" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{''.join(spark(120 + i * 380, 140, 0.6, 'gold') for i in range(2))}''')

add('granite', '粒の模様が見える硬い石で作られた階段',
    '花こう岩、御影石＝granite。', f'''
{table(352)}
{''.join(f'<g transform="translate(300 {{}})"><path d="M{{}} -22h{{}}v44h{{}}z" fill="#b9b4ae" stroke="{INK}" stroke-width="2.5"/></g>'.format(300 - i * 44, -(180 - i * 40), (180 - i * 40) * 2, -(180 - i * 40) * 2) for i in range(4))}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="{{}}"/>'.format(140 + (i * 53) % 320, 180 + (i * 37) % 140, 3 + i % 3, ['#8a857f', '#d8d3cc', '#6f6a64'][i % 3]) for i in range(30))}''')

add('grater', '四面のおろし金の粗い面で、チーズをすりおろす',
    'おろし金＝grater。', f'''
{table(352)}
<g transform="translate(280 250)">
  <path d="M-50-110h100l24 190h-148z" fill="#c3cbd1" class="o"/>
  {''.join(f'<path d="M{-40+ (i%4)*26} {-80+(i//4)*30}l10 10-10 10z" fill="#8a97a3"/>' for i in range(16))}
  <path d="M-50-110q50-26 100 0" fill="none" stroke="#8a97a3" stroke-width="8"/></g>
<g transform="translate(430 210) rotate(-20)">
  <path d="M-40-24h80v48h-80z" fill="#f2dc8e" class="o"/>
  <ellipse cx="-10" cy="0" rx="10" ry="6" fill="#d9b455"/></g>
{''.join(f'<path d="M{{}} {{}}l-6 16" fill="none" stroke="#f2dc8e" stroke-width="7" stroke-linecap="round"/>'.format(280 + (i * 23) % 60 - 30, 320 + (i * 17) % 20) for i in range(5))}''')

add('gravel', '砂利を敷いた小道の上を、足が踏んでいく',
    '砂利＝gravel。', f'''
<path d="M0 200h600v200H0z" class="greenp"/>
<path d="M180 400q20-160 40-200h160q30 60 40 200z" fill="#cfd6db" class="o"/>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="{{}}" stroke="{INK}" stroke-width="1.5"/>'.format(200 + (i * 61) % 200, 220 + (i * 43) % 160, 5 + i % 4, ['#b5bec4', '#dfe6ea', '#9aa7b1'][i % 3]) for i in range(40))}
<g transform="translate(300 300)"><path d="M-40 20q0-40 34-40h18l30 24v16z" fill="{INK}" opacity="0.8"/></g>''')

add('grocer', '食料品店の主人が、カウンター越しに品を差し出す',
    '食料品店の主人＝grocer。', f'''
<g transform="translate(300 330)">
  <path d="M-180 0v-150h360V0z" fill="#fffefd" class="o"/>
  <path d="M-196-150h392l-20-44h-352z" class="green o"/>
  {''.join(f'<g transform="translate({-120+i*80} -100)"><path d="M-30-14h60v28h-60z" class="{c}p o"/></g>' for i, c in enumerate(['coral', 'gold', 'violet', 'teal']))}</g>
{table(300)}
{person(300, 300, 0.9, 1, 'teal', 'blue', 'give', 'short', 'smile')}
<g transform="translate(380 268)"><path d="M-30-20h60l-6 40h-48z" class="goldp o"/></g>
{person(490, 340, 1.0, -1, 'coral', 'green', 'reach', 'bun', 'smile')}''')

add('groceries', '紙袋いっぱいの食料品から、パンと野菜がのぞく',
    '食料品、日用の買い物＝groceries。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-100-60h200v120h-200z" fill="#c9a464" class="o"/>
  <path d="M-100-60q100-20 200 0" fill="none" stroke="#a0764a" stroke-width="4"/></g>
<g transform="translate(250 200)">
  <path d="M-50 20q-8-48 16-56 6-18 34-18t34 18q24 8 16 56z" fill="#d9a45e" class="o"/></g>
<g transform="translate(350 190)">
  <path d="M0 30v-40" stroke="{GRND}" stroke-width="6" fill="none"/>
  <ellipse cx="-20" cy="-20" rx="20" ry="11" class="green o"/>
  <ellipse cx="20" cy="-30" rx="20" ry="11" class="green o"/></g>
<g transform="translate(390 230)"><circle r="20" class="coral o"/></g>''')

add('groove', 'レコード盤の表面に細い溝が刻まれ、針がその上をたどる',
    '溝、筋＝groove。', f'''
{table(352)}
<g transform="translate(280 250)">
  <circle r="140" fill="#2f3542" class="o"/>
  {''.join(f'<circle r="{40+i*18}" fill="none" stroke="#4e5a66" stroke-width="3"/>' for i in range(6))}
  <circle r="34" class="coral o"/>
  <circle r="6" fill="#fffaf1"/></g>
<g transform="translate(420 130) rotate(34)">
  <path d="M-8 0h16v130h-16z" fill="{MUTED}" class="o"/>
  <path d="M-4 130h8v20h-8z" class="ink"/></g>
{ring(340, 300, 40, True)}''')

add('hailstorm', '空から氷の粒が激しく降り、地面ではね返る',
    'ひょうを伴う嵐＝hailstorm。', f'''
{cloud(180, 90, 1.6, 'violet')}{cloud(430, 80, 1.4, 'violet')}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="#eef4f7" stroke="{BLU}" stroke-width="2.5"/>'.format(70 + (i * 71) % 480, 180 + (i * 47) % 150, 7 + i % 4) for i in range(16))}
<path d="M0 340h600v60H0z" class="ground"/>
{''.join(f'<path d="M{{}} 340l-14-22M{{}} 340l14-22" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(120 + i * 100, 120 + i * 100) for i in range(4))}
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{CRL}" stroke-width="4"/>'.format(520 + i * 0, 200 + i * 30) for i in range(2))}''')

add('hairbrush', '柄のついたブラシの毛の面が、上を向いて置かれている',
    'ヘアブラシ＝hairbrush。', f'''
{table(352)}
<g transform="translate(300 250) rotate(-16)">
  <path d="M-40-110q40-24 80 0 16 90 0 130-40 20-80 0-16-40 0-130z" fill="#a2825e" class="o"/>
  {''.join(f'<circle cx="{-24+(i%4)*16}" cy="{-80+(i//4)*30}" r="5" fill="#5b4636"/>' for i in range(16))}
  <path d="M-16 20h32v130a16 16 0 0 1-32 0z" fill="#a2825e" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}q14-16 0-30" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(430 + i * 20, 170 - i * 14) for i in range(2))}''')

add('hairdryer', '持ち手のついた送風機から、温かい風が吹き出す',
    'ドライヤー＝hairdryer。', f'''
{table(352)}
<g transform="translate(240 230) rotate(-10)">
  <path d="M-90-46h150v92h-150z" class="tealp o"/>
  <path d="M-90-36q-40 0-40 36t40 36z" class="teald o"/>
  <path d="M60-36h30v72H60z" fill="#c3cbd1" class="o"/>
  <path d="M-20 46h50l14 100h-64z" class="teal o"/>
  <path d="M20 146l50 30" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}h60" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(350, 180 + i * 34) for i in range(3))}''', arrow=True)

add('hammock', '二本の木の間に張られた網の寝床が、ゆるく垂れている',
    'ハンモック＝hammock。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
{tree(100, 330, 1.3)}{tree(500, 330, 1.3)}
<g transform="translate(300 200)">
  <path d="M-190 0q190 170 380 0" fill="none" stroke="{BRN}" stroke-width="9"/>
  <path d="M-190 30q190 170 380 0" fill="none" stroke="{BRN}" stroke-width="9"/>
  {''.join(f'<path d="M{-170+i*38} {abs(math.sin(i/10*math.pi))*118:.0f}v30" stroke="{BRN}" stroke-width="4" fill="none"/>' for i in range(10))}
  <path d="M-190 0l-20-24M190 0l20-24" stroke="{BRN}" stroke-width="6" fill="none"/></g>
<g transform="translate(300 296)">{head(0, -30, 22, 'coral', 'bob')}</g>''')

add('handbag', '肩ひものついた革のバッグが、留め具で閉じられている',
    'ハンドバッグ＝handbag。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-90-40h180v110h-180z" fill="#8a5c2b" class="o"/>
  <path d="M-90-40h180v-16h-180z" fill="#6a4020" class="o"/>
  <path d="M-50-56q50-60 100 0" fill="none" stroke="#6a4020" stroke-width="12"/>
  <path d="M-20-52h40v40h-40z" class="goldd o"/></g>''')

add('handlebars', '自転車の左右に伸びたハンドルを、両手で握る',
    '(自転車などの)ハンドル＝handlebars。', f'''
<g transform="translate(300 250)">
  <path d="M-160-20h320v22h-320z" fill="#8a97a3" class="o"/>
  <path d="M-160-30h60v42h-60zM100-30h60v42h-60z" fill="#2f3542" class="o"/>
  <path d="M-10 2h20v110h-20z" fill="#8a97a3" class="o"/>
  <path d="M-40 112h80v24h-80z" fill="#6b7680" class="o"/></g>
{hand(135, 250, 1)}
{hand(465, 250, -1)}''')

add('handrail', 'エスカレーターの横を動く手すりに、手をのせる',
    '手すり＝handrail。', f'''
<g transform="translate(300 250)">
  {''.join(f'<path d="M{-220+i*44} {100-i*30}h58v30h-58z" fill="#c3cbd1" stroke="{INK}" stroke-width="2.5"/>' for i in range(9))}
  <path d="M-250 130L200-80" fill="none" stroke="#2f3a4d" stroke-width="18" stroke-linecap="round"/></g>
{hand(340, 156, 1)}
{''.join(f'<path d="M{{}} {{}}h50" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(400, 120) for _ in range(1))}''', arrow=True)

add('hanger', 'かぎ形の金具のついた洋服かけに、上着が掛かっている',
    'ハンガー、洋服かけ＝hanger。', f'''
<path d="M0 90h600v14H0z" fill="{MUTED}"/>
<g transform="translate(300 200)">
  <path d="M0-70q-20-26 0-36 18-10 22 14" fill="none" stroke="#9aa7b1" stroke-width="8"/>
  <path d="M0-70L-120 10h240z" fill="none" stroke="#9aa7b1" stroke-width="9" stroke-linejoin="round"/>
  <path d="M-120 10h240" stroke="#9aa7b1" stroke-width="9" fill="none"/></g>
<g transform="translate(300 210)">
  <path d="M-110 0l110-56 110 56 10 140h-240z" class="teal o"/>
  <path d="M-30-56q30 26 60 0l-16 46h-28z" fill="#fffaf1" class="o"/></g>''')

add('harp', '三角の枠に弦が何本も張られたハープを、指ではじく',
    'ハープ、たて琴＝harp。', f'''
{table(352)}
<g transform="translate(300 250)">
  <path d="M-70 100V-90q70-30 110 10" fill="none" stroke="{BRN}" stroke-width="18" stroke-linecap="round"/>
  <path d="M-70 100h140" stroke="{BRN}" stroke-width="18" fill="none" stroke-linecap="round"/>
  <path d="M60-70L66 92" stroke="{BRN}" stroke-width="14" fill="none" stroke-linecap="round"/>
  {''.join(f'<path d="M{-58+i*12} {-76+i*14}L{62} {92-i*4}" stroke="#e6d8b8" stroke-width="2.5" fill="none"/>' for i in range(10))}</g>
{hand(400, 240, -1)}''')

add('hatch', '割れた殻を押しのけて、ひなが顔を出す',
    '卵からかえる／昇降口＝hatch。', f'''
{table(352)}
<g transform="translate(300 280)">
  <path d="M-70 40q-14-40 10-56 40-26 100 0 24 16 10 56z" fill="#fffefd" class="o"/>
  <path d="M-70-16l24-22 20 18 22-22 20 20 24-20" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cy="-50" r="40" class="gold o"/>
  <path d="M30-56l30 10-30 12z" class="corald o"/>
  <circle cx="14" cy="-62" r="5" class="ink"/></g>
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{GLD}" stroke-width="4"/>'.format(400 + i * 20, 190 - i * 14) for i in range(2))}''')

add('hay', '刈って乾かした草が、丸い束にまとめられて畑に置かれる',
    '干し草＝hay。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
{''.join(f'<g transform="translate({{}} 310)"><ellipse rx="{{}}" ry="{{}}" fill="#e0c48c" stroke="{INK}" stroke-width="2.5"/>{{}}</g>'.format(x, r, r * 0.86, ''.join(f'<ellipse rx="{r-14-j*16}" ry="{(r-14-j*16)*0.86:.0f}" fill="none" stroke="#c0a468" stroke-width="3"/>' for j in range(2))) for x, r in [(160, 80), (380, 64), (520, 48)])}
{''.join(f'<path d="M{{}} 360q20-12 40 0" fill="none" stroke="{GRND}" stroke-width="4"/>'.format(60 + i * 140) for i in range(4))}
{sun(90, 90, 36)}''')

add('headlight', '車の前の灯りがともり、前方に光の帯が伸びる',
    '(車の)前照灯、ヘッドライト＝headlight。', f'''
<g transform="translate(300 200)"><path d="M-300-200h600v400h-600z" fill="#2f3a4d"/></g>
<g transform="translate(400 300)">
  <path d="M-150 0v-50l50-70h200l50 70V0z" class="teal o"/>
  <path d="M-90-114h170l34 54h-238z" fill="#3f4a5c" class="o"/>
  <circle cx="-130" cy="6" r="34" class="ink"/>
  <circle cx="-150" cy="-34" r="22" class="goldp o"/></g>
<path d="M250 256L40 180 40 330z" fill="#fff6d8" opacity="0.55"/>
{ring(250, 266, 50, True)}''')

add('headphones', '左右の耳あてがつながったヘッドホンを、頭にかける',
    'ヘッドホン＝headphones。', f'''
<g transform="translate(300 230)">
  <circle cy="-10" r="90" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-88-46q10-64 88-64t88 64q-38-28-88-20-52-8-88 20z" fill="{HAIR}"/>
  <circle cx="-30" cy="-10" r="5" class="ink"/><circle cx="30" cy="-10" r="5" class="ink"/>
  <path d="M-20 24q20 16 40 0" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-110-10a110 110 0 0 1 220 0" fill="none" stroke="{TEAD}" stroke-width="18"/>
  <rect x="-136" y="-26" width="48" height="76" rx="20" class="teal o"/>
  <rect x="88" y="-26" width="48" height="76" rx="20" class="teal o"/></g>
{''.join(f'<path d="M{{}} {{}}q16-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(490 + i * 22, 180 - i * 14) for i in range(2))}''')

add('hearth', '暖炉の前の石の床で、火のそばに猫が丸まる',
    '炉床、暖炉の前の床＝hearth。', f'''
<g transform="translate(300 250)">
  <path d="M-160-140h320v260h-320z" fill="#b5a894" class="o"/>
  <path d="M-100-100h200v180h-200z" fill="#2f2620" class="o"/>
  {flame(-30, 70, 0.55)}{flame(30, 70, 0.5)}
  <path d="M-70 60h140v20h-140z" fill="#5b4636" class="o"/></g>
<g transform="translate(300 350)"><path d="M-200-30h400v60h-400z" fill="#cfd6db" class="o"/></g>
<g transform="translate(430 330)">
  <ellipse rx="46" ry="26" fill="#8a7a6a" class="o"/>
  <circle cx="30" cy="-16" r="18" fill="#8a7a6a" class="o"/>
  <path d="M20-30l-4-14 14 8zM40-32l10-12 2 14z" fill="#8a7a6a" class="o"/>
  <path d="M-40 8q-30 6-24 22" fill="none" stroke="#8a7a6a" stroke-width="9" stroke-linecap="round"/></g>''')

add('heater', '電気ヒーターの赤い棒が光り、前へ熱を送る',
    '暖房器具、ヒーター＝heater。', f'''
{table(352)}
<g transform="translate(280 260)">
  <path d="M-110-60h220v110h-220z" fill="#c3cbd1" class="o"/>
  <path d="M-90-40h180v70h-180z" fill="#2f3542" class="o"/>
  {''.join(f'<path d="M-80 {-24+i*24}h160" stroke="#e8402b" stroke-width="10" fill="none" stroke-linecap="round"/>' for i in range(3))}
  <path d="M-40 50h80v20h-80z" fill="#9aa7b1" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}h60" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(400, 210 + i * 40) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}q14-18 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(150 + i * 22, 180 - i * 14) for i in range(2))}''', arrow=True)

add('hiking', '登山靴とリュックの人が、丘の道を歩いて登る',
    'ハイキング、山歩き＝hiking。', f'''
<path d="M0 360h600v40H0z" class="ground"/>
<path d="M0 360L180 180l100 90 120-150 200 240z" fill="#d8cdb6" class="o"/>
{person(250, 300, 1.05, 1, 'teal', 'blue', 'walk', 'cap', 'smile')}
<g transform="translate(216 230)"><path d="M-30-40h60v80h-60z" fill="{BRN}" class="o"/></g>
<g transform="translate(300 290)"><path d="M0-90v110" stroke="{BRN}" stroke-width="7" fill="none" stroke-linecap="round"/></g>
{sun(500, 80, 34)}
{''.join(f'<path d="M{{}} 340q20-10 40 0" fill="none" stroke="{GRND}" stroke-width="4"/>'.format(60 + i * 120) for i in range(2))}''')

add('hinge', '扉と枠をつなぐちょうつがいを軸に、扉が開く',
    'ちょうつがい＝hinge。', f'''
<g transform="translate(220 200)">
  <path d="M-40-160h40v320h-40z" fill="#e8ddc9" class="o"/></g>
<g transform="translate(300 200) rotate(-16)">
  <path d="M-70-160h200v320h-200z" class="teal o"/>
  <circle cx="100" cy="0" r="9" class="goldp o"/></g>
{''.join(f'<g transform="translate(190 {{}})"><path d="M-24-26h24v52h-24z" fill="#8a97a3" class="o"/><path d="M0-26h24v52H0z" fill="#8a97a3" class="o"/><circle cy="0" r="8" fill="#6b7680" class="o"/></g>'.format(120 + i * 160) for i in range(2))}
<g transform="translate(190 280)"><path d="M-70 0a70 70 0 0 1 24-52" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="9 8" marker-end="url(#ar)"/></g>''', arrow=True)

add('hippo', '大きな口を開けたカバが、体を半分水につけている',
    'カバ＝hippo。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 262q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<g transform="translate(300 250)">
  <ellipse rx="180" ry="70" fill="#9a8a9a" class="o"/>
  <path d="M-180-16q180-60 360 0v16h-360z" fill="#a898a8"/>
  <ellipse rx="180" ry="70" fill="none" class="o"/>
  <ellipse cx="140" cy="-40" rx="70" ry="46" fill="#9a8a9a" class="o"/>
  <ellipse cx="186" cy="-40" rx="26" ry="20" fill="#8a7a8a" class="o"/>
  <circle cx="176" cy="-50" r="4" class="ink"/><circle cx="196" cy="-50" r="4" class="ink"/>
  <circle cx="100" cy="-70" r="12" fill="#9a8a9a" class="o"/>
  <circle cx="102" cy="-72" r="4" class="ink"/>
  <path d="M120-12q60 20 110 0" fill="none" stroke="#7a6a7a" stroke-width="4"/></g>''')

add('homework', '机の上のノートに宿題の問題を解き、教科書を開く',
    '宿題＝homework。', f'''
{table(352)}
<g transform="translate(260 260)">
  <path d="M-130-80h260v160h-260z" class="paper"/>
  {''.join(f'<g><rect x="-100" y="{-56+i*32}" width="{120-(i%2)*30}" height="10" rx="5" fill="{MUTED}"/><path d="M40 {-52+i*32}h50" stroke="{INK}" stroke-width="4" fill="none"/></g>' for i in range(4))}</g>
<g transform="translate(480 300) rotate(-10)">
  <path d="M-70-40h140v80h-140z" class="tealp o"/>
  <path d="M-70-40h10v80h-10z" class="teald o"/></g>
<g transform="translate(300 140) rotate(30)">
  <path d="M-8-70h16v100l-8 20-8-20z" class="coral o"/></g>''')

add('honeycomb', '六角形が規則正しく並んだ巣板に、蜜が満ちる',
    'ハチの巣＝honeycomb。', f'''
{''.join(f'<g transform="translate({{}} {{}})"><path d="M-30-17l30-17 30 17v34l-30 17-30-17z" fill="{{}}" stroke="{GLDD}" stroke-width="3"/></g>'.format(140 + (i % 6) * 62 + (i // 6 % 2) * 31, 130 + (i // 6) * 52, '#f0c04a' if i % 3 else '#fde9a8') for i in range(24))}
<g transform="translate(480 100)">
  <ellipse rx="30" ry="20" class="gold o"/>
  <path d="M-24-8h48" stroke="{INK}" stroke-width="5" fill="none"/><path d="M-20 6h44" stroke="{INK}" stroke-width="5" fill="none"/>
  <circle cx="-28" cy="-8" r="12" class="ink"/>
  <path d="M-4-18q24-30 40-10-20 2-30 16z" fill="#e6f2f6" opacity="0.9" stroke="{INK}" stroke-width="2"/></g>''')

finish(__file__)
