# -*- coding: utf-8 -*-
"""第169回。c-/d- の句動詞と抽象名詞。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def bed(x, y, s=1, cls='blue'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-130 0v-66h260v66z" fill="#fffefd" class="o"/>'
            f'<path d="M-130-66h56v-46h-56z" class="{cls}p o"/>'
            f'<path d="M-74-54q70-24 204 0v-12H-74z" class="{cls} o"/></g>')

def gear(x, y, r=54, teeth=8, cls='teal'):
    t = ''.join(f'<rect x="-9" y="{-r-14}" width="18" height="18" rx="3" transform="rotate({i*360/teeth})"/>' for i in range(teeth))
    return (f'<g transform="translate({x} {y})"><g class="{cls} o">{t}</g>'
            f'<circle r="{r}" class="{cls} o"/><circle r="{r*0.34}" fill="#fffaf1" class="o"/></g>')

def shop(x, y, s=1, cls='coral', shut=0.0):
    """店先。shut=0 で開店、1 でシャッターが下りきる。"""
    h = 150 * shut
    bars = ''.join(f'<path d="M-100 {-150+i*14}h200" stroke="{MUTED}" stroke-width="8" fill="none"/>' for i in range(int(h / 14) + 1))
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-110 0v-150h220V0z" fill="#fffefd" class="o"/>'
            f'<path d="M-100-150h200v150h-200z" class="{cls}p o"/>'
            f'<g>{bars}</g>'
            f'<path d="M-124-150h248l-20-44h-208z" class="{cls} o"/></g>')

# --- 世話・管理 --------------------------------------------------------------

add('care for', '寝ている人の枕もとで、水とタオルを用意して世話をする',
    '世話をする＝care for。', f'''
{bed(200, 300, 1.1, 'blue')}
{head(110, 226, 22, 'blue', 'bob')}
{person(440, 330, 1.1, -1, 'teal', 'green', 'carry', 'bun', 'smile')}
<g transform="translate(392 246)">
  <path d="M-24-26h48l-8 52h-32z" fill="#fffefd" class="o"/>
  <path d="M-20-14h40l-6 36h-28z" class="bluep"/></g>
<g transform="translate(330 300)"><path d="M-34-10h68v20h-68z" class="coralp o"/></g>
{''.join(spark(150 + i * 40, 160, 0.6, 'gold') for i in range(2))}''')

add('caretaker', '建物の前で、管理人が鍵束とほうきを手に立つ',
    '管理人、暫定政権＝caretaker。', f'''
{tower(430, 306, 0.95, 'teal', 4)}
{person(180, 340, 1.25, 1, 'blue', 'green', 'hold', 'cap', 'smile')}
<g transform="translate(232 264) rotate(12)">
  <path d="M0-70v120" stroke="{BRN}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <path d="M-22 50q22 32 44 0z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-18+i*9} 50v30" stroke="#c9a464" stroke-width="4" fill="none"/>' for i in range(5))}</g>
<g transform="translate(120 250)">
  <circle r="14" fill="none" stroke="{GLDD}" stroke-width="5"/>
  {''.join(f'<g transform="rotate({-30+i*30})"><path d="M0 14v40" stroke="{GLD}" stroke-width="6" fill="none"/><path d="M-7 54h14v8h-14z" fill="{GLD}"/></g>' for i in range(3))}</g>''')

# --- 結託・便乗 --------------------------------------------------------------

add('cartel', '同じ業界の三社が輪になって、そろって同じ値札を掲げる',
    'カルテル、企業連合＝cartel。', f'''
{''.join(f'<g transform="translate({{}} {{}})">{{}}</g>'.format(x, y, building(0, 0, 0.62, c))
         for x, y, c in [(140, 250, 'teal'), (300, 360, 'coral'), (460, 250, 'green')])}
<path d="M170 200q130-60 260 0M170 210q120 130 260 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/>
{''.join(f'<g transform="translate({{}} {{}}) rotate(-12)"><path d="M-30-20h44l16 20-16 20h-44z" class="gold o"/><circle cx="6" cy="0" r="5" fill="#fffaf1"/></g>'.format(x, y)
         for x, y in [(140, 120), (300, 250), (460, 120)])}''')

add('cash in on', '人が集まってできた行列のわきに屋台を出し、次々とコインが入る',
    '(機会を)うまく利用して稼ぐ＝cash in on。', f'''
{''.join(head(90 + i * 54, 220, 24, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('blue', 'bun'), ('violet', 'cap')]))}
<g transform="translate(440 300)">
  <path d="M-110 0v-90h220V0z" fill="#fffefd" class="o"/>
  <path d="M-124-90h248l-16-40h-216z" class="coral o"/>
  <path d="M-70-40h140v40h-140z" class="goldp o"/></g>
{person(440, 300, 0.78, 1, 'gold', 'blue', 'reach', 'short', 'smile')}
{''.join(coin(300 + i * 34, 140 - (i % 2) * 26, 17) for i in range(4))}
{arc(270, 180, 400, 190, 66, GLDD, True, 4)}''', arrow=True)

# --- きっかけ・流行 ----------------------------------------------------------

add('catalyst', '二つの物質の間に小さな粒が入ると反応が一気に進み、粒だけは元のまま残る',
    '触媒、変化のきっかけ＝catalyst。', f'''
{split()}
<g transform="translate(150 200)">
  <circle cx="-44" cy="0" r="38" class="blue o"/><circle cx="44" cy="0" r="38" class="green o"/>
  <path d="M-6 0h12" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="6 7"/></g>
<circle cx="150" cy="316" r="18" class="coral o"/>
{arc(230, 190, 370, 190, 56, MUTED, True, 5)}
<g transform="translate(450 200)">
  <path d="M-58-38h116v76h-116z" class="teal o"/>
  {''.join(spark(-40 + i * 40, -66, 0.8, 'gold') for i in range(3))}</g>
<circle cx="450" cy="316" r="18" class="coral o"/>
{ring(450, 316, 30, True)}''', arrow=True)

add('catch on', '一人がかぶり始めた帽子を、周りの人が次々にまねて広がる',
    '流行する、分かってくる＝catch on。', f'''
{''.join(head(90 + i * 46, 300, 22, 'teal', 'short') for i in range(3))}
{''.join(head(250 + i * 46, 250, 24, 'green', 'cap') for i in range(3))}
{''.join(head(410 + i * 46, 180, 26, 'coral', 'cap') for i in range(3))}
<g transform="translate(80 120)">{head(0, 0, 30, 'violet', 'cap')}</g>
{arc(110, 100, 440, 130, 90, MUTED, True, 5)}
{''.join(spark(470 + i * 40, 90, 0.8, 'gold') for i in range(2))}''', arrow=True)

# --- 主に・取り締まる ---------------------------------------------------------

add('chiefly', '三本の棒のうち、いちばん左の一本だけがずば抜けて高い',
    '主に、おもに＝chiefly。', f'''
{bar(140, 330, [100, 22, 14], 80, 40, 2.5, ['teal', 'tealp', 'tealp'])}
{ring(180, 200, 78, True)}
{''.join(f'<path d="M{{}} 348h{{}}" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(140 + i * 120, 70) for i in range(3))}''')

add('clamp down on', '大きな万力が、はみ出していた箱を上から締めつけて動けなくする',
    '取り締まる、厳しく抑え込む＝clamp down on。', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-140 90V-70h34V90z" fill="{MUTED}" class="o"/>
  <path d="M-140-70h250v34h-250z" fill="{MUTED}" class="o"/>
  <path d="M60-36h34v46H60z" fill="{MUTED}" class="o"/>
  <path d="M94-24h70v22H94z" fill="{MUTED}" class="o"/>
  <circle cx="180" cy="-14" r="22" fill="none" stroke="{MUTED}" stroke-width="10"/></g>
<g transform="translate(280 290)">
  <path d="M-70-36h140v72h-140z" class="coral o"/>
  <path d="M-70-36h140" fill="none" stroke="{CRLD}" stroke-width="4"/></g>
{''.join(f'<path d="M{{}} 250v22" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(x) for x in (240, 300, 360))}''', arrow=True)

add('crack down on', '違反を示す札の前に柵が引かれ、笛を鳴らす手が通行を止める',
    '厳しく取り締まる＝crack down on。', f'''
<g transform="translate(300 300)">
  <path d="M-240 0v-70h480v70z" fill="none"/>
  {''.join(f'<path d="M{-220+i*60} 0v-96" stroke="{CRL}" stroke-width="10" stroke-linecap="round" fill="none"/>' for i in range(8))}
  <path d="M-230-80h460M-230-40h460" stroke="{CRL}" stroke-width="10" stroke-linecap="round" fill="none"/></g>
{hand(300, 140, 1)}
{''.join(f'<g transform="translate({{}} 350)"><circle r="20" class="coralp o"/>{{}}</g>'.format(x, cross(0, 0, 0.36)) for x in (120, 300, 480))}
{''.join(f'<path d="M{{}} {{}}q16 8 0 18" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(360 + i * 20, 96 + i * 10) for i in range(3))}''')

# --- はっきりさせる・閉じる ---------------------------------------------------

add('clarification', '曇っていたガラスを拭くと、向こうの図がくっきり見える',
    '説明、明確化＝clarification。', f'''
<g transform="translate(300 190)">
  <path d="M-220-130h440v260h-440z" fill="#eef4f7" class="o"/>
  <g opacity="0.28"><path d="M-160-60h130v130h-130z" class="teal"/><circle cx="90" cy="10" r="64" class="coral"/></g>
  <path d="M-8-130h16v260h-16z" fill="#fffaf1" opacity="0"/>
  <g clip-path="url(#c)"></g></g>
<g transform="translate(160 200)"><path d="M-70-70h140v140h-140z" class="teal o"/></g>
<g opacity="0.3"><circle cx="410" cy="200" r="64" class="coral o"/></g>
<g transform="translate(280 210) rotate(-16)">
  <path d="M-40-30h80v60h-80z" class="goldp o"/>
  <path d="M-40-30q40 18 80 0" fill="none" stroke="{GLDD}" stroke-width="4"/></g>
{''.join(f'<path d="M{{}} {{}}q22-18 0-36" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(330 + i * 18, 300 - i * 14) for i in range(3))}''')

add('close down', '店のシャッターが下りきり、扉に板が打ちつけられる',
    '閉鎖する、廃業する＝close down。', f'''
{shop(280, 330, 1.05, 'coral', 1.0)}
<g transform="translate(280 250)">
  <path d="M-120-20h240v34h-240z" fill="#c9a464" class="o" transform="rotate(-10)"/>
  <path d="M-120 40h240v34h-240z" fill="#c9a464" class="o" transform="rotate(8)"/></g>
{''.join(f'<path d="M{{}} 350h20" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(430 + i * 34) for i in range(2))}
{cross(500, 150, 0.8)}''')

# --- 植民・生じる ------------------------------------------------------------

add('colonisation', '船で着いた側が島に旗を立て、島がその旗の色に塗り替わる',
    '植民地化＝colonisation。', f'''
<path d="M0 240h600v160H0z" class="bluep"/>
{''.join(f'<path d="M{i*80} 252q20-12 40 0t40 0" fill="none" stroke="{BLU}" stroke-width="4"/>' for i in range(8))}
<g transform="translate(380 240)">
  <path d="M-140 0q30-90 140-90T140 0z" class="violetp o"/>
  <path d="M-140 0q30-90 140-90" fill="none" stroke="{VIOD}" stroke-width="4"/></g>
<g transform="translate(380 150)">
  <path d="M0 0v-110" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M4-110h90l-24 30 24 30H4z" class="violet o"/></g>
<g transform="translate(120 250) rotate(-8)">
  <path d="M-90 0h180l-30 44h-120z" class="teal o"/>
  <path d="M-10 0v-100h86l-76 34" fill="{TEAP}" class="o"/></g>
{arc(200, 200, 320, 180, 70, MUTED, True, 4)}''', arrow=True)

add('come about', '静かな水面に石が落ち、そこから波紋が広がって出来事になる',
    '起こる、生じる＝come about。', f'''
<path d="M0 200h600v200H0z" class="bluep"/>
{''.join(f'<ellipse cx="300" cy="300" rx="{60+i*64}" ry="{18+i*20}" fill="none" stroke="{BLU}" stroke-width="{5-i*0.7:.1f}"/>' for i in range(4))}
<circle cx="300" cy="300" r="16" fill="{STONE}" class="o"/>
<g opacity="0.5"><circle cx="300" cy="200" r="15" fill="{STONE}"/><circle cx="300" cy="130" r="14" fill="{STONE}"/></g>
{line(300, 60, 300, 170, MUTED, True, 4)}
{''.join(drop(240 + i * 60, 250, 0.7, 'blue') for i in range(3))}''', arrow=True)

# --- 印象・ばらける ----------------------------------------------------------

add('come across as', '小柄な人が、向かいの相手の目には大きく厳しい影として映る',
    '〜という印象を与える＝come across as。', f'''
{split()}
{person(150, 330, 0.85, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(430 330)">
  <path d="M-70 0v-160q70-34 140 0V0z" fill="#5b6b7d"/>
  <circle cx="0" cy="-196" r="34" fill="#5b6b7d"/>
  <path d="M-20-204l14 8M20-204l-14 8" fill="none" stroke="#fffefd" stroke-width="4" stroke-linecap="round"/>
  <path d="M-14-176q14-10 28 0" fill="none" stroke="#fffefd" stroke-width="4"/></g>
{arc(220, 180, 350, 160, 56, MUTED, True, 4)}
<g transform="translate(540 120)"><circle r="26" fill="#fffefd" class="o"/><circle r="10" class="ink"/></g>''', arrow=True)

add('come apart', '組み立ててあったいすが、部品ごとにばらばらに外れて落ちる',
    'ばらばらになる、崩れる＝come apart。', f'''
{table(340)}
<g transform="translate(230 230) rotate(-14)"><path d="M-60-14h120v28h-120z" class="gold o"/></g>
<g transform="translate(380 210) rotate(24)"><path d="M-12-70h24v140h-24z" class="gold o"/></g>
<g transform="translate(150 300) rotate(40)"><path d="M-10-54h20v108h-20z" class="goldd o"/></g>
<g transform="translate(460 300) rotate(-32)"><path d="M-10-54h20v108h-20z" class="goldd o"/></g>
<g transform="translate(300 320) rotate(8)"><path d="M-46-10h92v20h-92z" class="goldd o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="7" fill="{MUTED}"/>'.format(x, y) for x, y in [(300, 150), (206, 288), (420, 150)])}
{''.join(f'<path d="M{{}} {{}}l{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>'.format(300, 250, dx, dy) for dx, dy in [(-100, -40), (100, -50), (-130, 60), (140, 50)])}''')

# --- 結局・うまくいく ---------------------------------------------------------

add('come down to', '幾筋もの道が最後に合流し、たった一枚の扉の前に行き着く',
    '結局〜次第である＝come down to。', f'''
{''.join(f'<path d="M{{}} 60Q{{}} 200 300 300" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>'.format(60 + i * 120, 120 + i * 90) for i in range(5))}
<g transform="translate(300 360)">
  <path d="M-56-120h112v120h-112z" class="teal o"/>
  <circle cx="34" cy="-56" r="7" class="goldp o"/></g>
{ring(300, 300, 40, True)}''')

add('come off', '難しい跳躍を決めて着地し、見ていた人から拍手が起きる',
    '(計画が)うまくいく＝come off。', f'''
{table(340)}
<g transform="translate(180 330)" opacity="0.3">{person(0, 0, 1.0, 1, 'teal', 'blue', 'up', 'short', 'flat')}</g>
{arc(220, 200, 380, 210, 110, MUTED, True, 5)}
{person(400, 330, 1.15, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{tick(500, 140, 1.0)}
{''.join(f'<g transform="translate({{}} {{}})">{{}}</g>'.format(x, y, hand(0, 0, f)) for x, y, f in [(80, 150, 1), (120, 220, -1)])}
{''.join(spark(140 + i * 30, 110 - (i % 2) * 24, 0.7, 'gold') for i in range(3))}''', arrow=True)

add('come round', '倒れていた人がまぶたを開け、そばの人が胸をなでおろす',
    '意識を取り戻す、考えを改める＝come round。', f'''
{table(340)}
<g transform="translate(240 300)">
  <path d="M-130 0v-40q130-30 260 0V0z" fill="{TEA}" class="o"/>
  <circle cx="-150" cy="-46" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-178-56q4-34 30-34 26 0 30 32-16-14-30-6-16-8-30 8z" fill="{HAIR}"/>
  <circle cx="-160" cy="-50" r="3" class="ink"/><circle cx="-142" cy="-50" r="3" class="ink"/>
  <path d="M-160-38q10 8 20 0" fill="none" stroke="{INK}" stroke-width="2.2"/></g>
{''.join(f'<path d="M{{}} {{}}q14-18 28 0" fill="none" stroke="{GLD}" stroke-width="4"/>'.format(60 + i * 22, 210 - i * 16) for i in range(3))}
{person(470, 340, 1.05, -1, 'coral', 'green', 'hold', 'bob', 'smile')}
{spark(120, 170, 1.1, 'gold')}''')

# --- 開始・両立 --------------------------------------------------------------

add('commencement', 'スタートラインでピストルが鳴り、走者がいっせいに走り出す',
    '開始、卒業式＝commencement。', f'''
<path d="M180 90v250" fill="none" stroke="{INK}" stroke-width="6"/>
{''.join(f'<rect x="{{}}" y="{{}}" width="18" height="18" fill="{INK}"/>'.format(162 + (i % 2) * 18, 100 + i * 18) for i in range(12))}
{person(260, 330, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{person(380, 330, 1.05, 1, 'coral', 'green', 'walk', 'bob', 'smile')}
{person(490, 330, 1.05, 1, 'gold', 'violet', 'walk', 'cap', 'smile')}
<g transform="translate(110 150) rotate(-40)">
  <path d="M-30 0h44v20h-44z" fill="{INK}"/><path d="M14 4h30v12H14z" fill="{MUTED}"/>
  <path d="M-30 20l-14 20h24z" fill="{INK}"/></g>
{''.join(spark(70 + i * 26, 100 - i * 16, 0.7, 'gold') for i in range(3))}
{arc(300, 240, 470, 240, 50, MUTED, True, 4)}''', arrow=True)

add('compatible', '形の合うプラグと差し込み口がぴたりとはまり、明かりがつく',
    '両立できる、互換性のある＝compatible。', f'''
<g transform="translate(220 210)">
  <path d="M-90-60h90v120h-90z" class="teal o"/>
  <path d="M0-34h50v24H0zM0 10h50v24H0z" class="teald o"/></g>
<g transform="translate(380 210)">
  <path d="M90-60H0v120h90z" class="coral o"/>
  <path d="M0-34h-52v24H0zM0 10h-52v24H0z" fill="#fffaf1" class="o"/></g>
{tick(300, 340, 0.9)}
{''.join(spark(300, 90 - i * 0, 1.0, 'gold') for i in range(1))}
{''.join(f'<path d="M{{}} {{}}l{{}} {{}}" fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round"/>'.format(300 + dx, 90 + dy, dx2, dy2) for dx, dy, dx2, dy2 in [(-56, -14, -24, -12), (56, -14, 24, -12), (0, -46, 0, -24)])}''')

# --- 含み・統合・消費 ---------------------------------------------------------

add('connotation', '一つの語のまわりに、うっすらとした連想の輪がいくつも浮かぶ',
    '言外の意味、含み＝connotation。', f'''
{word(300, 210, 5, 34)}
{ring(300, 210, 110, True)}
{''.join(f'<g opacity="0.42" transform="translate({{}} {{}})"><circle r="42" class="{{}}p o"/></g>'.format(x, y, c) for x, y, c in [(110, 110, 'coral'), (490, 110, 'teal'), (120, 320, 'violet'), (480, 320, 'green')])}
{''.join(f'<path d="M300 210L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 9"/>'.format(x, y) for x, y in [(150, 140), (450, 140), (160, 296), (440, 296)])}''')

add('consolidation', '三つの小さな箱が一つの大きな箱にまとめられる',
    '統合、強化＝consolidation。', f'''
{split()}
{box(100, 160, 70, 54, 18, 'teal')}
{box(100, 250, 70, 54, 18, 'teal')}
{box(190, 210, 70, 54, 18, 'teal')}
{arc(250, 200, 350, 200, 50, MUTED, True, 5)}
{box(460, 220, 180, 140, 44, 'teal')}''', arrow=True)

add('consumerism', '買い物かごから品物があふれ、それでもまだ棚に手を伸ばす',
    '消費主義＝consumerism。', f'''
<g transform="translate(470 200)">
  <path d="M-70-140h140v34h-140zM-70-70h140v34h-140zM-70 0h140v34h-140z" fill="#e2d6bd" class="o"/>
  {''.join(f'<rect x="{{}}" y="{{}}" width="24" height="26" rx="4" class="{{}} o"/>'.format(-58 + (i % 4) * 32, -166 + (i // 4) * 70, c) for i, c in enumerate(['coral', 'teal', 'gold', 'violet', 'green', 'blue', 'coral', 'teal']))}</g>
<g transform="translate(200 300)">
  <path d="M-90-70h180l-20 70h-140z" class="bluep o"/>
  <circle cx="-52" cy="20" r="16" class="ink"/><circle cx="52" cy="20" r="16" class="ink"/>
  <path d="M-90-70l-30-30h-24" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/></g>
{''.join(f'<rect x="{{}}" y="{{}}" width="30" height="32" rx="5" class="{{}} o" transform="rotate({{}} {{}} {{}})"/>'.format(x, y, c, r, x + 15, y + 16) for x, y, c, r in [(140, 200, 'coral', -12), (180, 176, 'gold', 8), (224, 196, 'green', -20), (262, 214, 'violet', 14)])}
{person(320, 340, 1.05, 1, 'teal', 'blue', 'reach', 'bob', 'smile')}''')

# --- 異論・収縮・逆に ---------------------------------------------------------

add('contentious', '真ん中の一枚の案を挟んで、両側の人が同時に声を上げる',
    '議論を呼ぶ、異論の多い＝contentious。', f'''
{doc(300, 200, 150, 200, 3)}
{person(120, 340, 1.15, 1, 'coral', 'blue', 'up', 'short', 'sad')}
{person(480, 340, 1.15, -1, 'teal', 'green', 'up', 'bob', 'sad')}
{''.join(f'<path d="M{{}} {{}}q16 12 0 24" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(186 + i * 16, 130 + i * 16) for i in range(3))}
{''.join(f'<path d="M{{}} {{}}q-16 12 0 24" fill="none" stroke="{TEA}" stroke-width="5"/>'.format(414 - i * 16, 130 + i * 16) for i in range(3))}''')

add('contraction', '大きかった円が、内向きの矢印に押されて小さく縮む',
    '収縮、(経済の)縮小＝contraction。', f'''
<circle cx="300" cy="200" r="150" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 11"/>
<circle cx="300" cy="200" r="72" class="teal o"/>
{''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"/>'.format(
    int(300 + 142 * math.cos(math.radians(a))), int(200 + 142 * math.sin(math.radians(a))),
    int(300 + 88 * math.cos(math.radians(a))), int(200 + 88 * math.sin(math.radians(a)))) for a in range(0, 360, 45))}''', arrow=True)

add('conversely', '左では右上がりの矢印、右ではまったく逆に右下がりの矢印になる',
    '逆に、これとは反対に＝conversely。', f'''
{split()}
<path d="M60 330h180M60 330V90" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
{line(80, 310, 226, 120, TEA, False, 7)}
<path d="M360 330h180M360 330V90" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
{line(380, 120, 526, 310, CRL, False, 7)}
<g transform="translate(300 60)"><path d="M-26 0h52" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>
  <path d="M-26 0l16-12M-26 0l16 12M26 0l-16-12M26 0l-16 12" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/></g>''', arrow=True)

# --- 腐食・うわべ・隠す -------------------------------------------------------

add('corrosive', 'こぼれた液体が金属板を溶かし、ふちのぎざぎざした穴が開く',
    '腐食性の、むしばむ＝corrosive。', f'''
{table(340)}
<g transform="translate(300 260)">
  <path d="M-180-60h360v100h-360z" fill="{STONE}" class="o"/>
  <path d="M-40-60q-20 30 4 46-28 14-10 40 26 16 54 0 22-22-2-40 24-18 0-46z" fill="#fffaf1" class="o"/>
  <path d="M60-20q-16 12 0 24 18 10 30-4-4-18-30-20z" fill="#fffaf1" class="o"/></g>
<g transform="translate(190 120) rotate(34)">
  <path d="M-26-64h52v92a20 20 0 0 1-20 20h-12a20 20 0 0 1-20-20z" class="greenp o"/>
  <path d="M-12-86h24v22h-24z" class="green o"/></g>
{''.join(drop(250 + i * 18, 178 + i * 16, 1.0, 'green') for i in range(3))}
{''.join(f'<path d="M{{}} {{}}q14-18 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(330 + i * 20, 226 - i * 12) for i in range(3))}''')

add('cosmetic', 'ひび割れた壁の上から、薄くペンキを塗って表面だけきれいにする',
    '化粧の、うわべだけの＝cosmetic。', f'''
<g transform="translate(300 200)">
  <path d="M-220-140h440v280h-440z" fill="#e4dccb" class="o"/>
  <path d="M-140-140l30 90-50 50 40 60-24 80M60-140l-36 100 54 46-40 74 20 60" fill="none" stroke="{MUTED}" stroke-width="5"/></g>
<g transform="translate(300 120)"><path d="M-220-60h440v120h-440z" class="tealp"/></g>
<g transform="translate(300 92)"><path d="M-220 0h440" fill="none" stroke="{TEA}" stroke-width="6" stroke-dasharray="0"/></g>
<g transform="translate(430 130) rotate(18)">
  <path d="M-34 0h68v40h-68z" class="teal o"/>
  <path d="M-8 40h16v90h-16z" fill="{BRN}" class="o"/></g>
{''.join(f'<path d="M{{}} 300l6 40" fill="none" stroke="{MUTED}" stroke-width="5"/>'.format(x) for x in (180, 350))}''')

add('cover up', '床のしみの上に敷物をかぶせ、見えないようにする',
    '隠す、もみ消す＝cover up。', f'''
<g transform="translate(300 300)">
  <path d="M-60-20q-30 20-6 40 30 22 66 4 22-24-10-44-30-14-50 0z" class="corald"/></g>
<g transform="translate(300 290) rotate(-6)">
  <path d="M-160-40h320v80h-320z" class="violetp o"/>
  <path d="M-140-24h280v48h-280z" fill="none" stroke="{VIO}" stroke-width="4" stroke-dasharray="10 9"/></g>
{person(140, 340, 1.0, 1, 'teal', 'blue', 'give', 'short', 'flat')}
{arc(180, 190, 280, 240, 50, MUTED, True, 4)}
<g transform="translate(480 160)"><circle r="26" fill="#fffefd" class="o"/>
  <path d="M-30 0q30-24 60 0-30 24-60 0z" fill="#fffefd" class="o"/><circle r="10" class="ink"/>
  <path d="M-34-22l68 44" stroke="{CRL}" stroke-width="7" stroke-linecap="round" fill="none"/></g>''', arrow=True)

# --- 欲する・債権・決定的 -----------------------------------------------------

add('crave', 'のどが渇ききった人の目に、水の入ったコップだけが大きく映る',
    '切望する、無性に欲しがる＝crave。', f'''
{person(160, 340, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'sad')}
<g transform="translate(410 200)">
  <path d="M-70 110l14-190h112l14 190z" fill="#fffefd" class="o"/>
  <path d="M-58-40h116l10 150h-136z" class="bluep"/>
  <path d="M-70 110l14-190h112l14 190z" fill="none" class="o"/></g>
{ring(410, 200, 160, True)}
{''.join(f'<path d="M{{}} {{}}q18-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(240 + i * 18, 170 + i * 14) for i in range(3))}''')

add('creditor', 'お金を渡した側が借用書を受け取り、あとで返済が自分に戻ってくる',
    '債権者、貸した側＝creditor。', f'''
{person(140, 340, 1.15, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
{person(460, 340, 1.15, -1, 'coral', 'green', 'reach', 'short', 'flat')}
{''.join(coin(250 + i * 40, 180, 19) for i in range(3))}
{arc(230, 170, 380, 170, 56, GLDD, False, 5)}
{doc(300, 290, 96, 70, 2)}
{arc(380, 300, 250, 300, -50, MUTED, True, 4)}''', arrow=True)

add('crucially', '積み上げたアーチの中央にある要石が一つ、全体を支えている',
    '決定的に、重要なことに＝crucially。', f'''
<g transform="translate(300 330)">
  {''.join(f'<g transform="rotate({{}} 0 0)"><path d="M-26-206h52v56h-52z" class="tealp o"/></g>'.format(a) for a in (-62, -42, -22, 22, 42, 62))}
  <path d="M-26-206h52v56h-52z" class="coral o"/>
  <path d="M-190 0h380v20h-380z" fill="{STONE}" class="o"/></g>
{ring(300, 154, 52, True)}
{''.join(f'<path d="M300 60v34" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"/>' for _ in range(1))}''', arrow=True)

# --- 治る・切り詰める ---------------------------------------------------------

add('curable', '薬を飲むと、体に出ていた赤い印が消えて元気になる',
    '治療可能な＝curable。', f'''
{split()}
{person(150, 330, 1.15, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="7" class="coral"/>'.format(x, y) for x, y in [(132, 250), (160, 236), (170, 270), (140, 280)])}
<g transform="translate(300 200) rotate(-20)">
  <path d="M-34-16h68v32h-68z" class="coralp o"/>
  <path d="M0-16v32" fill="none" stroke="{CRL}" stroke-width="3"/></g>
{person(450, 330, 1.15, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{tick(520, 150, 0.8)}
{arc(230, 180, 370, 180, 46, MUTED, True, 4)}''', arrow=True)

add('curtail', '長く伸びた巻物を、はさみで途中から切り詰めて短くする',
    '(期間や権利を)切り詰める、制限する＝curtail。', f'''
{table(330)}
<g transform="translate(220 230)">
  <path d="M-160-50h320v100h-320z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="{{}}" y="{{}}" width="120" height="9" rx="4.5" fill="{MUTED}"/>'.format(-140, -28 + i * 24) for i in range(3))}
  <path d="M-160-50a16 50 0 0 0 0 100" fill="#f0e6d2" class="o"/></g>
<g opacity="0.32" transform="translate(470 230)"><path d="M-80-50h160v100h-160z" fill="#fffefd" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"/></g>
<path d="M390 130v210" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="12 10"/>
<g transform="translate(390 120) rotate(90)">
  <path d="M-4 0l-50-40M-4 0l-50 40" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cx="-62" cy="-48" r="14" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="-62" cy="48" r="14" fill="none" stroke="{INK}" stroke-width="6"/></g>''')

add('cut back', 'はさみを入れて、支出の棒グラフを一段低く切り下げる',
    '(費用・量を)減らす＝cut back。', f'''
{bar(120, 330, [90, 70, 50], 78, 44, 2.4, ['coralp', 'coralp', 'coral'])}
<g opacity="0.3">{bar(120, 330, [0, 0, 0], 78, 44, 2.4)}</g>
<path d="M100 176h420" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="12 10"/>
<g opacity="0.3"><path d="M120 132h78v44h-78zM242 152h78v24h-78z" class="coral"/></g>
<g transform="translate(540 176) rotate(180)">
  <path d="M-4 0l-50-40M-4 0l-50 40" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cx="-62" cy="-48" r="14" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="-62" cy="48" r="14" fill="none" stroke="{INK}" stroke-width="6"/></g>''')

# --- ふと分かる・議論の余地 ---------------------------------------------------

add('dawn on', '考えこんでいた人の頭の上で電球がともり、うしろの地平から日が昇る',
    '(考えが)ふと分かる、思い当たる＝dawn on。', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<g transform="translate(470 306)"><circle r="90" class="goldp o"/>
  {''.join(f'<path d="M0-104v-22" transform="rotate({{}})" stroke="{GLD}" stroke-width="6" stroke-linecap="round" fill="none"/>'.format(a) for a in (-60, -30, 0, 30, 60))}</g>
{person(200, 340, 1.25, 1, 'teal', 'blue', 'think', 'short', 'smile')}
<g transform="translate(200 110)">
  <circle r="38" class="goldp o"/>
  <path d="M-16 34h32v16h-32z" fill="{MUTED}" class="o"/>
  <path d="M-10-4q-8-14 4-22 10-6 18 2 8 10-2 22" fill="none" stroke="{GLDD}" stroke-width="4"/>
  {''.join(f'<path d="M0-56v-20" transform="rotate({{}})" stroke="{GLD}" stroke-width="5" stroke-linecap="round" fill="none"/>'.format(a) for a in (-40, 0, 40))}</g>''')

add('debatable', '演台に立った二人が向き合い、同じ問いをめぐって言い分を交わす',
    '議論の余地がある＝debatable。', f'''
{''.join(f'<g transform="translate({{}} 306)"><path d="M-54 0v-120h108V0z" class="goldp o"/><path d="M-62-120h124v18h-124z" class="gold o"/></g>'.format(x) for x in (150, 450))}
{person(150, 260, 0.9, 1, 'teal', 'blue', 'point', 'short', 'flat')}
{person(450, 260, 0.9, -1, 'coral', 'green', 'point', 'bob', 'flat')}
<g transform="translate(300 130)">
  <path d="M-24-40q0-30 26-30t26 30q0 20-26 30v16" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="2" cy="34" r="7" fill="{MUTED}"/></g>
{arc(216, 170, 270, 156, 30, TEA, True, 4)}
{arc(384, 170, 330, 156, 30, CRL, True, 4)}''', arrow=True)

add('decidedly', '目盛りの針が真ん中ではなく、はっきり端まで振り切れている',
    '明らかに、断然＝decidedly。', f'''
<g transform="translate(300 300)">
  <path d="M-190 0A190 190 0 0 1 190 0z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M0-160v-22" transform="rotate({{}})" stroke="{MUTED}" stroke-width="5" fill="none"/>'.format(a) for a in range(-80, 81, 20))}
  <path d="M0 0L128-118" fill="none" stroke="{CRL}" stroke-width="12" stroke-linecap="round"/>
  <circle r="16" class="ink"/>
  <g opacity="0.3"><path d="M0 0v-160" stroke="{MUTED}" stroke-width="8" stroke-dasharray="10 9" fill="none"/></g></g>
{ring(428, 182, 44, True)}''')

# --- 控除・悪化 --------------------------------------------------------------

add('deduction', '給料袋から一部が抜き取られ、別の箱へ移される',
    '天引き、控除／推論＝deduction。', f'''
{table(340)}
<g transform="translate(180 250)">
  <path d="M-70-80h140v160h-140z" fill="#f0e6d2" class="o"/>
  <path d="M-70-80q70 34 140 0" fill="none" stroke="{BRN}" stroke-width="4"/>
  {''.join(coin(-30 + i * 30, 20, 16) for i in range(3))}</g>
{coin(330, 170, 18)}
{arc(250, 180, 400, 190, 70, MUTED, True, 4)}
<g transform="translate(470 280)">
  <path d="M-60-50h120v100h-120z" class="coralp o"/>
  {coin(0, 0, 18)}</g>
<path d="M120 130h44M142 108v44" fill="none" stroke="{CRL}" stroke-width="0"/>
<g transform="translate(300 320)"><path d="M-24 0h48" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round"/></g>''', arrow=True)

add('degenerate', 'つやのあった果実が、段を追うごとに傷んで崩れていく',
    '(質が)悪化する、堕落する＝degenerate。', f'''
{table(340)}
<g transform="translate(130 280)"><circle r="56" class="coral o"/><path d="M0-56v-24" stroke="{GRND}" stroke-width="6" fill="none"/>
  <ellipse cx="24" cy="-70" rx="22" ry="11" class="green o" transform="rotate(-20 24 -70)"/></g>
<g transform="translate(300 280)"><circle r="54" class="corald o"/>
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="9" fill="{BRN}"/>'.format(x, y) for x, y in [(-18, -12), (16, 8), (-6, 24)])}</g>
<g transform="translate(470 284)"><path d="M-50 44q-16-56 10-76 30-22 56-2 26 22 12 78z" fill="{BRN}" class="o"/>
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="7" fill="#6a5040"/>'.format(x, y) for x, y in [(-14, 0), (18, 16), (0, 30)])}</g>
{arc(200, 230, 240, 230, 34, MUTED, True, 4)}
{arc(370, 230, 410, 230, 34, MUTED, True, 4)}''', arrow=True)

add('degradation', '緑におおわれていた丘が、草を失って裸の土地に変わる',
    '劣化、悪化＝degradation。', f'''
{split()}
<path d="M20 340q130-130 260-10v70H20z" class="greenp o"/>
{''.join(f'<g>{{}}</g>'.format(tree(70 + i * 70, 300, 0.7)) for i in range(3))}
<path d="M320 340q130-110 260-10v70H320z" fill="#cbb896" class="o"/>
{''.join(f'<path d="M{{}} 300v-26" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>'.format(370 + i * 70) for i in range(3))}
{''.join(f'<path d="M{{}} 330q20-10 40 0" fill="none" stroke="{BRN}" stroke-width="3"/>'.format(350 + i * 60) for i in range(3))}
{arc(270, 180, 340, 190, 40, MUTED, True, 4)}''', arrow=True)

# --- 熟議・表に出す・示す -----------------------------------------------------

add('deliberation', '会議室で全員が長い時間をかけ、書類を一枚ずつ検討する',
    '熟議、審議＝deliberation。', f'''
{table(280)}
{''.join(sit(150 + i * 100, 280, 0.9, 1, c, 'blue', h, 'flat') for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('gold', 'bun'), ('violet', 'cap')]))}
{''.join(chair(144 + i * 100, 280, 0.84, 'gold', 1) for i in range(4))}
{doc(300, 238, 90, 62, 2)}
{clock(520, 120, 52, 3, 50)}
{''.join(f'<path d="M{{}} 176q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(200 + i * 100) for i in range(3))}''')

add('demonstrative', '再会した相手に思いきり駆け寄って、両腕で大きく抱きしめる',
    '感情を表に出す＝demonstrative。', f'''
{person(230, 340, 1.25, 1, 'coral', 'blue', 'give', 'bob', 'smile')}
{person(390, 340, 1.25, -1, 'teal', 'green', 'give', 'short', 'smile')}
<g transform="translate(310 140)">
  <path d="M0 30q-40-30-40-56 0-20 20-20 12 0 20 14 8-14 20-14 20 0 20 20 0 26-40 56z" class="coral o"/></g>
{''.join(spark(180 + i * 86, 110 + (i % 2) * 34, 0.8, 'gold') for i in range(4))}''')

add('denote', '看板の稲妻の記号が、点線で電気の危険を指し示す',
    '示す、意味する＝denote。', f'''
<g transform="translate(160 200)">
  <path d="M0-110l110 190H-110z" class="goldp o"/>
  {bolt(0, 32, 1.1)}</g>
{arc(280, 170, 400, 170, 56, MUTED, True, 4)}
<g transform="translate(460 220)">
  <path d="M-70-60h140v140h-140z" fill="#fffefd" class="o"/>
  <path d="M-40-20h30v30h-30zM10-20h30v30H10zM-40 30h30v30h-30zM10 30h30v30H10z" class="goldp o"/>
  <path d="M0-60v-40" stroke="{INK}" stroke-width="6" fill="none"/></g>
{bolt(460, 100, 0.9)}''', arrow=True)

add('derivative', '元になった一枚の絵を、そのまま写した複製が何枚も並ぶ',
    '独創性のない、派生物＝derivative。', f'''
<g transform="translate(130 200)">
  <path d="M-80-100h160v200h-160z" fill="#fffefd" class="o"/>
  <circle cx="0" cy="-20" r="40" class="coral o"/>
  <path d="M-56 80q56-80 112 0z" class="teal o"/></g>
{''.join(f'<g transform="translate({{}} 210) scale(0.82)" opacity="0.85"><path d="M-80-100h160v200h-160z" fill="#fffefd" class="o"/><circle cx="0" cy="-20" r="40" class="coral o"/><path d="M-56 80q56-80 112 0z" class="teal o"/></g>'.format(x) for x in (320, 460))}
{arc(220, 150, 260, 160, 36, MUTED, True, 4)}
{arc(390, 150, 410, 160, 30, MUTED, True, 4)}''', arrow=True)

add('detriment', '天秤の片側にコインが増えた分だけ、反対側の鉢が割れて傾く',
    '損害、不利益＝detriment。', f'''
{scales(300, 300, -12, 1.0)}
{''.join(coin(180 + i * 26, 176, 16) for i in range(3))}
<g transform="translate(400 210)">
  <path d="M-40 0q6 40 40 40t40-40z" class="corald o"/>
  <path d="M-16 0l10 34M10 0l-6 36" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M44 4l26-14M-44 4l-26-14" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{cross(500, 130, 0.6)}''')

finish(__file__)
