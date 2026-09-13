# -*- coding: utf-8 -*-
"""第175回。sa-/sc-/se-/sh-/si-/sl-/sm- の語。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def gauge(x, y, r=110, frac=0.5, cls='coral'):
    a = math.radians(180 + frac * 180)
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M{-r} 0A{r} {r} 0 0 1 {r} 0z" fill="#fffefd" class="o"/>'
            + ''.join(f'<path d="M0-{r-14}v-14" transform="rotate({-90+i*30})" stroke="{MUTED}" stroke-width="4" fill="none"/>' for i in range(7))
            + f'<path d="M0 0l{r*0.78*math.cos(a):.0f} {r*0.78*math.sin(a):.0f}" stroke="{TONES[cls][0]}" stroke-width="11" stroke-linecap="round" fill="none"/>'
            f'<circle r="13" class="ink"/></g>')

def torii(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-100 0v-170h22V0zM78 0v-170h22V0z" class="coral o"/>'
            f'<path d="M-130-170h260v22h-260z" class="corald o"/>'
            f'<path d="M-140-196h280l-14 26h-252z" class="corald o"/>'
            f'<path d="M-90-120h180v18h-180z" class="coral o"/></g>')

def fence(x, y, s=1, n=7):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            + ''.join(f'<path d="M{-180+i*60} 0v-120" stroke="{BRN}" stroke-width="14" fill="none" stroke-linecap="round"/>' for i in range(n))
            + f'<path d="M-190-100h380M-190-50h380" stroke="{BRN}" stroke-width="12" fill="none" stroke-linecap="round"/></g>')

# --- 楽々・縮小・ほとんどない ---------------------------------------------------

add('sail through', '追い風を受けた帆船が、関門をするりと抜けていく',
    '楽々と通過する＝sail through。', f'''
<path d="M0 280h600v120H0z" class="bluep"/>
{''.join(f'<path d="M{i*90} 292q22-14 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>' for i in range(7))}
<g transform="translate(300 280)">
  <path d="M-110 0h220l-34 46h-152z" class="coral o"/>
  <path d="M-10 0v-180h110l-98 44v40l86-14-88 40" fill="{GLDP}" class="o"/></g>
{''.join(f'<path d="M40 {70+i*46}q90-24 180 0" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}
{''.join(f'<path d="M{500} 60v240" fill="none" stroke="{MUTED}" stroke-width="10" stroke-dasharray="26 20"/>' for _ in range(1))}
{tick(540, 120, 0.7)}''')

add('scale back', '大きく描いていた建物の計画が、ひと回り小さな図に描き直される',
    '規模を縮小する＝scale back。', f'''
{split()}
<g transform="translate(150 220)">
  <path d="M-110-120h220v240h-220z" class="paper"/>
  <path d="M-70-40h140v160h-140z" fill="none" stroke="{BLU}" stroke-width="5"/>
  <path d="M-80-40L0-100l80 60" fill="none" stroke="{BLU}" stroke-width="5"/></g>
<g transform="translate(450 220)">
  <path d="M-110-120h220v240h-220z" class="paper"/>
  <path d="M-40 20h80v100h-80z" fill="none" stroke="{BLU}" stroke-width="5"/>
  <path d="M-50 20L0-16l50 36" fill="none" stroke="{BLU}" stroke-width="5"/>
  <g opacity="0.25"><path d="M-70-40h140v160h-140zM-80-40L0-100l80 60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g></g>
{arc(270, 160, 330, 160, 44, MUTED, True, 5)}''', arrow=True)

add('scarcely', '大きな器の底に、粒がたったひとつだけ残っている',
    'ほとんど〜ない＝scarcely。', f'''
{table(352)}
<g transform="translate(300 260)">
  <path d="M-160-90q160 200 320 0v-10q-160 60-320 0z" fill="none"/>
  <path d="M-160-100q0 180 160 180t160-180z" fill="#fffefd" class="o"/></g>
<circle cx="300" cy="316" r="14" class="gold o"/>
{ring(300, 316, 40, True)}
{''.join(f'<path d="M{{}} 200q14-16 0-30" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(490 + i * 20) for i in range(2))}''')

# --- 意見一致・見抜く・分離 -----------------------------------------------------

add('see eye to eye', '向かい合う二人の目の高さがぴたりと合い、視線が一本に重なる',
    '意見が一致する＝see eye to eye。', f'''
{person(160, 350, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(440, 350, 1.25, -1, 'coral', 'green', 'stand', 'bob', 'smile')}
<path d="M200 215h200" fill="none" stroke="{GRN}" stroke-width="6" stroke-linecap="round"/>
<path d="M60 215h500" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"/>
{tick(300, 120, 0.8)}''')

add('see through', '差し出された笑顔の仮面ごしに、その裏の表情までが見えている',
    '(うそを)見抜く＝see through。', f'''
{person(430, 350, 1.25, -1, 'coral', 'blue', 'give', 'short', 'sad')}
<g transform="translate(330 190)" opacity="0.55">
  <ellipse rx="76" ry="94" fill="#fffefd" class="o"/>
  <circle cx="-26" cy="-14" r="6" class="ink"/><circle cx="26" cy="-14" r="6" class="ink"/>
  <path d="M-30 34q30 26 60 0" fill="none" stroke="{INK}" stroke-width="5"/></g>
{person(130, 350, 1.15, 1, 'teal', 'green', 'stand', 'bob', 'flat')}
<path d="M180 200h100" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>
{''.join(f'<path d="M{{}} {{}}l14-16" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x, y) for x, y in [])}''', arrow=True)

add('segregation', '一つの広場が線で二つに分けられ、二つの群れが行き来できない',
    '分離、隔離＝segregation。', f'''
<g transform="translate(300 220)"><path d="M-250-140h500v280h-500z" fill="#f1efe8" class="o"/></g>
<path d="M300 80v280" fill="none" stroke="{INK}" stroke-width="10"/>
{''.join(head(110 + (i % 2) * 90, 160 + (i // 2) * 90, 28, 'teal', 'short') for i in range(4))}
{''.join(head(400 + (i % 2) * 90, 160 + (i // 2) * 90, 28, 'coral', 'bob') for i in range(4))}
<path d="M240 120h120" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>
{cross(300, 120, 0.5)}''')

add('seismic', '地面に大きな裂け目が走り、その上の建物が激しく揺れる',
    '地震の、地殻変動的な＝seismic。', f'''
<path d="M0 300h600v100H0z" fill="#cbb896"/>
<path d="M240 300l30 100h60l-40-60 34-40z" fill="#fffaf1" class="o"/>
<g transform="translate(150 300) rotate(-7)">{house(0, 0, 0.8, 'coral')}</g>
<g transform="translate(450 300) rotate(9)">{tower(0, 0, 0.7, 'teal', 4)}</g>
{''.join(f'<path d="M{110+i*34} {170-i*10}q16-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
{''.join(f'<path d="M{470+i*30} {150+i*10}q16-16 0-32" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
<path d="M40 360q40-20 80 0t80 0" fill="none" stroke="{BRN}" stroke-width="5"/>''')

# --- 自営・意味・半円 ---------------------------------------------------------

add('self-employed', '自分ひとりの小さな店で、自分の名の看板を出して働く',
    '自営の、個人事業の＝self-employed。', f'''
<g transform="translate(330 330)">
  <path d="M-130 0v-140h260V0z" fill="#fffefd" class="o"/>
  <path d="M-146-140h292l-20-46h-252z" class="teal o"/>
  <path d="M-90-96h180v50h-180z" class="tealp o"/></g>
{person(330, 330, 0.9, 1, 'coral', 'blue', 'reach', 'short', 'smile')}
<g transform="translate(120 220)">
  <path d="M-8 130V0h16v130z" fill="{BRN}"/>
  <path d="M-70-60h140v60h-140z" class="paper"/>
  <rect x="-48" y="-42" width="96" height="12" rx="6" fill="{MUTED}"/>
  <rect x="-48" y="-20" width="60" height="10" rx="5" fill="{MUTED}"/></g>
{ring(330, 250, 96, True)}''')

add('semantic', '同じ形の語が、場面によってまったく別の中身を指す',
    '意味の、語義の＝semantic。', f'''
{''.join(f'<g transform="translate({{}} 110)">{{}}</g>'.format(x, word(0, 0, 4, 30)) for x in (150, 450))}
{''.join(f'<path d="M{{}} 150v46" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(x) for x in (150, 450))}
<g transform="translate(150 280)">
  <path d="M-80-60h160v120h-160z" fill="#fffefd" class="o"/>
  <circle r="34" class="coral o"/></g>
<g transform="translate(450 280)">
  <path d="M-80-60h160v120h-160z" fill="#fffefd" class="o"/>
  <path d="M-34 34h68l-34-68z" class="teal o"/></g>
{split()}''', arrow=True)

add('semicircle', '円をちょうど半分に切った、まっすぐな辺をもつ半円',
    '半円＝semicircle。', f'''
<g opacity="0.26"><circle cx="300" cy="200" r="150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 11"/></g>
<path d="M150 200a150 150 0 0 1 300 0z" class="teal o"/>
<path d="M150 200h300" fill="none" stroke="{INK}" stroke-width="6"/>
<path d="M150 330h300" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M300 200v-150" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>''', arrow=True)

add('semicolon', '点と読点を縦に重ねた記号が、文と文のあいだに置かれる',
    'セミコロン(;)＝semicolon。', f'''
{''.join(f'<rect x="{{}}" y="120" width="{{}}" height="24" rx="12" fill="{INK}"/>'.format(60 + i * 90, 66 - (i % 2) * 14) for i in range(3))}
<g transform="translate(340 132)">
  <circle cy="-22" r="13" class="coral"/>
  <g transform="translate(0 22)"><circle r="13" class="coral"/>
    <path d="M0 13q-9 16-18 20" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round"/></g></g>
{''.join(f'<rect x="{{}}" y="120" width="{{}}" height="24" rx="12" fill="{INK}"/>'.format(390 + i * 90, 66 - (i % 2) * 14) for i in range(2))}
<g transform="translate(300 280) scale(2.4)">
  <circle cy="-22" r="13" class="coral"/>
  <g transform="translate(0 22)"><circle r="13" class="coral"/>
    <path d="M0 13q-9 16-18 20" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round"/></g></g>''')

# --- 無意味・賢明・敏感 -------------------------------------------------------

add('senseless', 'ばらばらの向きに並んだ記号の列が、どう読んでも意味をなさない',
    '無意味な、正気を失った＝senseless。', f'''
<g transform="translate(300 190)">
  <path d="M-220-110h440v220h-440z" class="paper"/>
  {''.join(f'<rect x="{{}}" y="{{}}" width="26" height="26" rx="4" fill="{VIO}" transform="rotate({{}} {{}} {{}})"/>'.format(-180 + (i % 7) * 54, -70 + (i // 7) * 60, 25 * (i % 5) - 40, -167 + (i % 7) * 54, -57 + (i // 7) * 60) for i in range(21))}</g>
{''.join(f'<g transform="translate({{}} 350)"><path d="M-16-26q0-20 18-20t18 20q0 14-18 20v10" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/><circle cy="24" r="5" fill="{MUTED}"/></g>'.format(200 + i * 100) for i in range(3))}''')

add('sensibly', '雨の予報を見て、出かける前にきちんと傘を用意する',
    '賢明に、分別をもって＝sensibly。', f'''
<g transform="translate(150 170)">
  <path d="M-110-110h220v220h-220z" fill="#fffefd" class="o"/>
  {cloud(0, -30, 0.9, 'violet')}
  {''.join(f'<path d="M{{}} 20l-12 26" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>'.format(-40 + i * 40) for i in range(3))}</g>
{person(420, 350, 1.3, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(470 230) rotate(12)">
  <path d="M-70 0a70 70 0 0 1 140 0z" class="coral o"/>
  <path d="M0 0v92q0 20 20 20" fill="none" stroke="{BRN}" stroke-width="7"/></g>
{arc(270, 180, 360, 200, 50, MUTED, True, 4)}
{tick(160, 340, 0.6)}''', arrow=True)

add('sensitive to', 'ごくわずかな重みでも、はかりの針が大きく振れる',
    '〜に敏感な、〜に配慮した＝sensitive to。', f'''
{gauge(330, 300, 150, 0.86, 'coral')}
<g transform="translate(330 120)"><circle r="12" class="teal o"/></g>
{line(330, 140, 330, 176, MUTED, True, 4)}
{''.join(f'<path d="M{{}} {{}}q14-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(510 + i * 20, 210 - i * 14) for i in range(2))}''', arrow=True)

# --- 説教・後退 --------------------------------------------------------------

add('sermon', '高い説教壇から語られる話を、席についた人々が静かに聞く',
    '説教＝sermon。', f'''
<g transform="translate(140 330)">
  <path d="M-70 0v-130h140V0z" class="goldp o"/>
  <path d="M-82-130h164v22h-164z" class="gold o"/></g>
{person(140, 200, 0.95, 1, 'violet', 'blue', 'point', 'short', 'flat')}
{''.join(f'<g transform="translate({{}} 330)">{{}}</g>'.format(330 + i * 90, sit(0, 0, 0.86, -1, c, 'blue', h, 'flat')) for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('coral', 'bun')]))}
{''.join(chair(336 + i * 90, 330, 0.8, 'gold', -1) for i in range(3))}
{arc(230, 150, 380, 170, 60, MUTED, True, 4)}''', arrow=True)

add('set back', '前へ進んでいた駒が押し戻され、いくつか後ろのマスに下がる',
    '(進行を)遅らせる＝set back。', f'''
{''.join(f'<rect x="{{}}" y="200" width="80" height="80" rx="8" class="{{}} o"/>'.format(40 + i * 90, 'tealp' if i % 2 else 'paper') for i in range(6))}
<g opacity="0.3"><circle cx="440" cy="240" r="26" class="coral"/></g>
<circle cx="170" cy="240" r="26" class="coral o"/>
{arc(420, 170, 190, 170, 60, CRL, True, 6)}
{hand(510, 240, -1)}''', arrow=True)

add('setback', '順調に登っていた道の途中で石につまずき、勢いが止まる',
    'つまずき、後退＝setback。', f'''
<path d="M40 350L520 140" fill="none" stroke="{STONE}" stroke-width="34" stroke-linecap="round"/>
<g transform="translate(330 214) rotate(-24)"><path d="M-34-28h68v56h-68z" fill="{STONE}" class="o"/></g>
<g transform="translate(280 240) rotate(-24)">{person(0, 0, 1.15, 1, 'teal', 'blue', 'up', 'short', 'sad')}</g>
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(370 + i * 22, 150 - i * 16) for i in range(3))}
<g opacity="0.28">{arc(340, 180, 490, 110, 50, MUTED, True, 5)}</g>''', arrow=True)

add('set in', '空一面が雲におおわれ、その天気がそのまま居座り始める',
    '(悪い状態が)始まって続く＝set in。', f'''
{sun(90, 90, 40)}
<g opacity="0.5">{cloud(180, 110, 1.2, 'violet')}</g>
{cloud(340, 100, 1.8, 'violet')}
{cloud(510, 120, 1.5, 'violet')}
{''.join(f'<path d="M{{}} {{}}l-14 30" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>'.format(280 + i * 40, 190 + (i % 2) * 26) for i in range(7))}
{arc(160, 180, 460, 190, 60, MUTED, True, 5)}
{house(300, 350, 0.62, 'coral')}''', arrow=True)

# --- 訂正・深刻さ・急激 -------------------------------------------------------

add('set the record straight', '曲がって書かれていた記録の線を、まっすぐな線に引き直す',
    '誤りを正す、事実を明らかにする＝set the record straight。', f'''
<g transform="translate(300 200)">
  <path d="M-230-130h460v260h-460z" class="paper"/>
  <g opacity="0.3"><path d="M-180-50q60 60 120-20t120 40" fill="none" stroke="{MUTED}" stroke-width="10" stroke-dasharray="10 9"/></g>
  <path d="M-180 40h360" fill="none" stroke="{GRN}" stroke-width="11" stroke-linecap="round"/></g>
<g transform="translate(450 110) rotate(34)">
  <path d="M-9-90h18v130l-9 24-9-24z" class="green o"/></g>
{tick(120, 320, 0.6)}''')

add('severity', '傷の重さを示す目盛りが、いちばん強いところまで振り切れている',
    '深刻さ、厳しさ＝severity。', f'''
{gauge(300, 300, 170, 0.94, 'coral')}
{''.join(f'<rect x="{{}}" y="{{}}" width="52" height="26" rx="6" fill="{{}}"/>'.format(120 + i * 60, 348, c) for i, c in enumerate(['#fde9e3', '#f6b3a6', '#ef8a76', '#e86452', '#b74338']))}
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(450 + i * 20, 130 - i * 14) for i in range(2))}''')

add('sharply', '折れ線がゆるやかな道から一転して、鋭い角度で跳ね上がる',
    '急激に／鋭く＝sharply。', f'''
<path d="M60 350h460M60 350V50" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<path d="M90 300L240 280" fill="none" stroke="{TEA}" stroke-width="6" stroke-linecap="round"/>
<path d="M240 280L420 80" fill="none" stroke="{TEA}" stroke-width="10" stroke-linecap="round"/>
<path d="M240 280h130" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>
<path d="M300 280a60 60 0 0 0 26-48" fill="none" stroke="{CRL}" stroke-width="4"/>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="8" class="teal o"/>'.format(x, y) for x, y in [(240, 280), (420, 80)])}''')

# --- きらめき・出荷・支える ---------------------------------------------------

add('shimmer', '静かな水面の上で、光の粒がちらちらと揺れて反射する',
    'かすかに揺らめいて光る＝shimmer。', f'''
<path d="M0 200h600v200H0z" class="bluep"/>
{''.join(f'<path d="M{{}} {{}}q22-12 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 46 % 600, 230 + (i * 37) % 130) for i in range(22))}
{''.join(spark(70 + (i * 83) % 470, 220 + (i * 53) % 140, 0.4 + (i % 3) * 0.16, 'gold') for i in range(14))}
{sun(90, 90, 40)}''')

add('shipment', '荷物を積みこんだ貨物が、行き先へ向けて送り出される',
    '発送、積み荷＝shipment。', f'''
<g transform="translate(330 300)">
  <path d="M-180 0v-110h230V0z" class="tealp o"/>
  <path d="M50 0v-70h60l40 70z" class="teal o"/>
  <circle cx="-120" cy="8" r="26" class="ink"/><circle cx="90" cy="8" r="26" class="ink"/>
  <circle cx="-120" cy="8" r="10" fill="#fffefd"/><circle cx="90" cy="8" r="10" fill="#fffefd"/></g>
{''.join(box(200 + i * 80, 230, 66, 50, 16, 'gold') for i in range(2))}
{''.join(f'<path d="M{{}} 340h{{}}" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(480, 60) for _ in range(1))}
<path d="M0 360h600" fill="none" stroke="{BRN}" stroke-width="8"/>''', arrow=True)

add('shore up', '傾きかけた壁に太い斜めの支柱をあてがい、倒れるのを止める',
    '下支えする、てこ入れする＝shore up。', f'''
<g transform="translate(240 340) rotate(-10)">
  <path d="M-90-260h180v260h-180z" fill="{STONE}" class="o"/>
  {''.join(f'<path d="M-90 {{}}h180" fill="none" stroke="#a9b3ba" stroke-width="4"/>'.format(-220 + i * 54) for i in range(4))}</g>
{''.join(f'<path d="M{{}} {{}}L{{}} 346" fill="none" stroke="{BRN}" stroke-width="20" stroke-linecap="round"/>'.format(330, 160 + i * 70, 470 + i * 40) for i in range(2))}
<path d="M40 350h520" fill="none" stroke="{BRN}" stroke-width="8"/>
{tick(120, 130, 0.7)}''')

# --- 欠点・不足・悲鳴 ---------------------------------------------------------

add('shortcoming', 'そろっているはずの部品のうち、一か所だけが欠けたままになっている',
    '欠点、至らない点＝shortcoming。', f'''
<g transform="translate(300 220)">
  <path d="M-200-120h400v240h-400z" class="tealp o"/>
  {''.join(f'<rect x="{{}}" y="{{}}" width="70" height="70" rx="8" class="teal o"/>'.format(-170 + (i % 5) * 76, -86 + (i // 5) * 96) for i in range(10) if i != 7)}
  <rect x="-18" y="10" width="70" height="70" rx="8" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="10 9"/></g>
{ring(317, 265, 66, True)}''')

add('shortfall', '積み上げた高さが目標の線に届かず、その差が空いたまま残る',
    '不足額、不足分＝shortfall。', f'''
<path d="M70 350h460" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<path d="M90 110h420" fill="none" stroke="{GRN}" stroke-width="6" stroke-dasharray="14 12"/>
<rect x="180" y="210" width="150" height="140" rx="8" class="teal o"/>
<path d="M255 200V120" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
<g opacity="0.22"><rect x="180" y="110" width="150" height="100" rx="8" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/></g>
{''.join(f'<path d="M{{}} 110h40" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}''', arrow=True)

add('shriek', '大きく口を開けて叫び、鋭い線が四方へ飛び散る',
    '金切り声をあげる、悲鳴＝shriek。', f'''
<g transform="translate(300 220)">
  <circle r="90" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="{HAIRS['short']}" transform="translate(0 486) scale(3.75)" fill="{HAIR}"/>
  <path d="M-40-26l24 12M40-26l-24 12" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <ellipse cy="44" rx="30" ry="38" class="ink"/></g>
{''.join(f'<path d="M{int(300+160*math.cos(math.radians(a)))} {int(220+160*math.sin(math.radians(a)))}l{int(46*math.cos(math.radians(a)))} {int(46*math.sin(math.radians(a)))}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for a in range(-180, 181, 30))}''')

# --- 聖地・受け流す・よろい戸 ---------------------------------------------------

add('shrine', '石段の上に鳥居が立ち、その奥に小さな社がまつられている',
    '聖堂、神社、聖地＝shrine。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
{''.join(f'<path d="M{{}} {{}}h{{}}v14h-{{}}z" fill="{STONE}" class="o"/>'.format(200 + i * 14, 330 - i * 14, 200 - i * 28, 200 - i * 28) for i in range(3))}
{torii(300, 290, 0.62)}
<g transform="translate(300 200)">
  <path d="M-60 0v-64h120V0z" fill="#f0e6d2" class="o"/>
  <path d="M-78-64L0-108l78 44z" class="corald o"/>
  <path d="M-18 0v-40h36V0z" class="coral o"/></g>
{tree(90, 330, 1.0)}{tree(520, 330, 0.9)}''')

add('shrug off', '厳しい言葉を向けられても、肩をすくめて気にとめない',
    '軽く受け流す、意に介さない＝shrug off。', f'''
{person(450, 350, 1.2, -1, 'coral', 'blue', 'point', 'bob', 'sad')}
<g transform="translate(190 330)">
  <path d="M-70 0v-110q70-30 140 0V0z" class="teal o"/>
  <path d="M-70-110q-26-30-40-8M70-110q26-30 40-8" fill="none" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>
  <circle cx="0" cy="-156" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-34-164q4-36 34-36 28 0 34 34-18-16-34-6-16-10-34 8z" fill="{HAIR}"/>
  <circle cx="-11" cy="-158" r="3" class="ink"/><circle cx="11" cy="-158" r="3" class="ink"/>
  <path d="M-10-142h20" fill="none" stroke="{INK}" stroke-width="2.4"/></g>
{''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>'.format(370, 150 + i * 40, 300, 180 + i * 40) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}l-30 26" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>'.format(280, 170 + i * 50) for i in range(2))}''')

add('shutter', '窓の外側によろい戸がついていて、左右に開け閉めできる',
    'よろい戸、シャッター＝shutter。', f'''
<g transform="translate(300 200)">
  <path d="M-230-150h460v300h-460z" fill="#e4dccb" class="o"/>
  <path d="M-100-110h200v220h-200z" fill="#dfeaf2" class="o"/>
  <path d="M0-110v220M-100 0h200" fill="none" stroke="{INK}" stroke-width="5"/></g>
{''.join(f'<g transform="translate({{}} 200)"><path d="M-44-110h88v220h-88z" class="teal o"/>{{}}</g>'.format(x, ''.join(f'<path d="M-32 {{}}h64" stroke="{TEAD}" stroke-width="6" fill="none"/>'.format(-86 + i * 28) for i in range(7))) for x in (156, 444))}
{''.join(f'<path d="M{{}} 90h{{}}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-end="url(#ar)"/>'.format(x, d) for x, d in [(200, -40), (400, 40)])}''', arrow=True)

# --- 包囲・登録・示す ---------------------------------------------------------

add('siege', '城のまわりを幾重にも囲み、出入りを断って動けなくする',
    '包囲、攻囲＝siege。', f'''
<g transform="translate(300 250)">
  <path d="M-110 90v-150h220v150z" fill="#e8ddc9" class="o"/>
  <path d="M-110-60v-30h30v-20h30v20h40v-20h30v20h30v30z" fill="#e8ddc9" class="o"/>
  <path d="M-26 90V20h52v70z" class="corald o"/></g>
{''.join(f'<g transform="translate({{}} {{}})"><path d="M-18-30h36v60h-36z" class="teal o"/><path d="M0-30v-30" stroke="{BRN}" stroke-width="5" fill="none"/></g>'.format(x, y) for x, y in [(80, 200), (80, 320), (520, 200), (520, 320), (180, 110), (420, 110)])}
{''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="10 9" marker-end="url(#ar)"/>'.format(x, y, 300 + (x - 300) * 0.42, 240 + (y - 240) * 0.42) for x, y in [(110, 200), (110, 320), (490, 200), (490, 320), (180, 140), (420, 140)])}''', arrow=True)

add('sign up', '申込用紙に自分の名を書き入れ、受付に差し出す',
    '申し込む、登録する＝sign up。', f'''
{table(340)}
<g transform="translate(280 230)">
  <path d="M-130-100h260v200h-260z" class="paper"/>
  {''.join(f'<rect x="-100" y="{{}}" width="{{}}" height="12" rx="6" fill="{MUTED}"/>'.format(-70 + i * 34, 200 - (i % 3) * 44) for i in range(3))}
  <path d="M-100 50h200" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-80 46q40-26 70 0t70-14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></g>
<g transform="translate(430 130) rotate(34)">
  <path d="M-9-90h18v130l-9 24-9-24z" class="teal o"/></g>
{tick(120, 180, 0.7)}''')

add('signify', '掲げられた旗の色が、決まった合図として意味を伝える',
    '意味する、示す＝signify。', f'''
<g transform="translate(150 306)">
  <path d="M0 0v-200" stroke="{BRN}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <path d="M6-200h120l-30 36 30 36H6z" class="coral o"/></g>
{arc(300, 180, 390, 180, 50, MUTED, True, 5)}
<g transform="translate(470 200)">
  <path d="M-80-80h160v160h-160z" fill="#fffefd" class="o"/>
  <path d="M0-50q44 56 44 78a44 44 0 0 1-88 0q0-22 44-78z" class="coral o"/>
  <path d="M-30-64l60 60M30-64l-60 60" fill="none" stroke="{CRL}" stroke-width="0"/></g>
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{CRL}" stroke-width="0"/>'.format(x, y) for x, y in [])}''', arrow=True)

# --- 直喩・単純さ ------------------------------------------------------------

add('simile', '人の横に獅子の姿を並べ、「〜のようだ」と重ねて示す',
    '直喩(like や as を使うたとえ)＝simile。', f'''
{person(140, 350, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(300 200)">
  <path d="M-40-20h80M-40 20h80" fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round"/></g>
{beast(470, 330, 0.5, '#c08b3e', -1)}
{ring(140, 260, 96, True, 'teal')}
{ring(470, 290, 96, True, 'gold')}''')

add('simplicity', 'ごちゃごちゃと入り組んだ形の隣に、線が一本きりの形が並ぶ',
    '単純さ、簡素さ＝simplicity。', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-100 60q40-90 0-120t60-20 40 60-60 40 70 40 20-90-60-20" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  <path d="M-70-60q60 50 120-10t-40 120" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/></g>
<path d="M370 200h170" fill="none" stroke="{TEA}" stroke-width="12" stroke-linecap="round"/>
{tick(450, 320, 0.7)}''')

add('simplification', '線の多い複雑な図が、要点だけを残した簡単な図に置きかわる',
    '単純化＝simplification。', f'''
{split()}
<g transform="translate(150 200)">
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="18" class="tealp o"/>'.format(-80 + (i % 3) * 80, -80 + (i // 3) * 80) for i in range(9))}
  {''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(-80 + (i % 3) * 80, -80 + (i // 3) * 80, -80 + ((i + 1) % 3) * 80, -80 + ((i + 2) // 3) * 80) for i in range(9))}</g>
<g transform="translate(450 200)">
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="22" class="teal o"/>'.format(0, -80 + i * 80) for i in range(3))}
  <path d="M0-58v36M0 22v36" fill="none" stroke="{INK}" stroke-width="5"/></g>
{arc(270, 130, 340, 130, 44, MUTED, True, 5)}''', arrow=True)

add('simplify', '長く続いた式から余分なところを消し、短い形にまとめ直す',
    '単純にする、簡略化する＝simplify。', f'''
<g transform="translate(300 150)">
  <path d="M-240-40h480v80h-480z" class="paper"/>
  {''.join(f'<rect x="{{}}" y="-12" width="{{}}" height="24" rx="12" fill="{INK}"/>'.format(-216 + i * 62, 46 - (i % 2) * 12) for i in range(7))}</g>
<g transform="translate(300 290)">
  <path d="M-120-40h240v80h-240z" class="paper"/>
  {''.join(f'<rect x="{{}}" y="-12" width="{{}}" height="24" rx="12" fill="{INK}"/>'.format(-96 + i * 62, 46 - (i % 2) * 12) for i in range(3))}</g>
{arc(300, 200, 300, 240, -0, MUTED, True, 5)}
{''.join(f'<path d="M{{}} 150l0 0" fill="none"/>'.format(x) for x in (0,))}''', arrow=True)

# --- 心から・名指し・しみ込む ---------------------------------------------------

add('sincerely', '胸に手を当て、心からの気持ちとして相手に伝える',
    '心から＝sincerely。', f'''
<g transform="translate(230 330)">
  <path d="M-80 0v-140q80-34 160 0V0z" class="teal o"/>
  <path d="M-80-140q-14 60 46 62" fill="none" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>
  <path d="M80-140l22 56" fill="none" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>
  <circle cx="0" cy="-186" r="32" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-36-194q4-38 36-38 30 0 36 36-20-16-36-6-18-10-36 8z" fill="{HAIR}"/>
  <circle cx="-11" cy="-186" r="3" class="ink"/><circle cx="11" cy="-186" r="3" class="ink"/>
  <path d="M-11-170q11 9 22 0" fill="none" stroke="{INK}" stroke-width="2.4"/>
  <path d="M-24-104q24-22 48 0-10 34-24 44-14-10-24-44z" class="coral o"/></g>
{person(470, 350, 1.1, -1, 'coral', 'green', 'stand', 'bob', 'smile')}
{''.join(spark(120 + i * 40, 120 + (i % 2) * 34, 0.7, 'gold') for i in range(2))}''')

add('single out', '大勢が並ぶ中から、たった一人だけを名指しで指し示す',
    '(一人・一つを)選び出す、名指しする＝single out。', f'''
{''.join(head(90 + i * 84, 250, 30, 'teal', 'short') for i in range(6) if i != 3)}
{head(342, 250, 30, 'coral', 'bob')}
{ring(342, 250, 62, False, 'coral')}
{hand(342, 100, 1)}
{line(342, 150, 342, 190, CRL, False, 5)}''', arrow=True)

add('sink in', '布に落ちた水が、時間をかけてじわじわと奥まで染み込む',
    '(意味が)じわじわ分かってくる＝sink in。', f'''
{table(352)}
{''.join(f'<g transform="translate({{}} 250)"><path d="M-80-60h160v120h-160z" fill="#fffefd" class="o"/><circle cy="-10" r="{{}}" class="bluep"/><circle cy="-10" r="{{}}" class="blue"/></g>'.format(110 + i * 190, 14 + i * 26, 8 + i * 8) for i in range(3))}
{''.join(f'<path d="M{{}} 140h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(220 + i * 190) for i in range(2))}
{drop(110, 110, 1.3, 'blue')}''', arrow=True)

# --- 中立・状況・値踏み -------------------------------------------------------

add('sit on the fence', '柵の上に腰かけたまま、左右どちらの側にも降りようとしない',
    'どっちつかずでいる＝sit on the fence。', f'''
{fence(300, 340, 1.0, 7)}
<g transform="translate(300 240)">{sit(0, 0, 1.05, 1, 'teal', 'blue', 'short', 'flat', 'lap')}</g>
{''.join(f'<path d="M{{}} 300h{{}}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>'.format(x, d) for x, d in [(250, -80), (350, 80)])}
{''.join(cross(x, 300, 0.4) for x in (140, 460))}''', arrow=True)

add('situational', '同じ人が、場面に合わせて別々のかっこうで現れる',
    '状況による＝situational。', f'''
{''.join(f'<g transform="translate({{}} 200)"><path d="M-84-130h168v260h-168z" fill="#fffefd" class="o"/></g>'.format(110 + i * 190) for i in range(3))}
{person(110, 300, 0.82, 1, 'blue', 'blue', 'stand', 'short', 'smile')}
{person(300, 300, 0.82, 1, 'coral', 'gold', 'stand', 'cap', 'smile')}
{person(490, 300, 0.82, 1, 'green', 'violet', 'stand', 'bun', 'smile')}
{''.join(f'<g transform="translate({{}} 96)">{{}}</g>'.format(110 + i * 190, o) for i, o in enumerate([
  f'<rect x="-30" y="-20" width="60" height="40" rx="6" class="bluep o"/>',
  f'<circle r="24" class="goldp o"/>',
  f'<path d="M-26 20l26-44 26 44z" class="greenp o"/>']))}''')

add('size up', '相手の姿を上から下まで、目でひととおり測るように見る',
    '(人・状況を)見定める、値踏みする＝size up。', f'''
{person(180, 350, 1.1, 1, 'teal', 'blue', 'think', 'short', 'flat')}
{person(440, 350, 1.35, -1, 'coral', 'green', 'stand', 'bob', 'flat')}
<path d="M250 200q90-60 150-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>
<path d="M250 220q90 60 150 110" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"/>
<path d="M530 130v220" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

# --- しくじり・ナメクジ・なめらかさ ---------------------------------------------

add('slip up', '足もとの皮に気づかず踏んで、つるりと足をとられる',
    'うっかりミスをする＝slip up。', f'''
<g transform="translate(340 350) rotate(38)">{person(0, 0, 1.25, 1, 'teal', 'blue', 'up', 'short', 'sad')}</g>
<g transform="translate(280 350) rotate(16)">
  <path d="M-50 0q-10-24 10-30 20 30 50 22 10 10-14 16-30 6-46-8z" class="gold o"/>
  <path d="M-40-28l-14-14" stroke="{GLDD}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}l-18 14" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(200 + i * 14, 300 + i * 16) for i in range(2))}
{cross(500, 130, 0.7)}''')

add('slug', 'からを持たない細長い体が、地面を這って光る跡を残す',
    'ナメクジ＝slug。', f'''
<path d="M0 300h600v100H0z" class="ground"/>
<g transform="translate(320 290)">
  <path d="M-160 20q-10-46 40-52 60-8 100-30 50-26 84 8 26 26-4 50-60 30-160 20z" fill="#9aa06a" class="o"/>
  <path d="M180-24q8-28 30-22 18 6 10 28M150-38q6-30 28-24 18 6 12 28" fill="none" stroke="#9aa06a" stroke-width="8" stroke-linecap="round"/>
  <circle cx="210" cy="-18" r="4" class="ink"/><circle cx="190" cy="-32" r="4" class="ink"/></g>
<path d="M60 316q60 14 120 0t120 0" fill="none" stroke="#cfd8b4" stroke-width="12" stroke-linecap="round"/>
{''.join(flower(80 + i * 80, 330, 0.4, 'coral') for i in range(2))}''')

add('smoothness', 'でこぼこした面の横に、指がすっと滑るなめらかな面が並ぶ',
    'なめらかさ、円滑さ＝smoothness。', f'''
{split()}
<path d="M40 300q20-40 40 0t40-40 40 40 40-30 40 30" fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round"/>
{cross(150, 140, 0.6)}
<path d="M340 290h220" fill="none" stroke="{TEA}" stroke-width="12" stroke-linecap="round"/>
{hand(400, 220, 1)}
{''.join(f'<path d="M{{}} 240h60" fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"/>'.format(450) for _ in range(1))}
{tick(450, 130, 0.6)}''', arrow=True)

finish(__file__)
