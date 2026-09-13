# -*- coding: utf-8 -*-
"""第170回。d-/e-/f- の前半。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def stomach(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-10-120v56" fill="none" stroke="{CRLD}" stroke-width="22" stroke-linecap="round"/>'
            f'<path d="M-30-64q-52 20-46 76 6 58 62 62 56 4 62-56 6-52-38-76z" class="coralp o"/>'
            f'<path d="M40 70q10 40-20 56-34 18-56-6" fill="none" stroke="{CRLD}" stroke-width="20" stroke-linecap="round"/></g>')

def ring_obj(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle r="22" fill="none" stroke="{GLD}" stroke-width="9"/>'
            f'<path d="M-11-24l11-18 11 18z" class="goldp o"/></g>')

def coinstack(x, y, n=5, r=22):
    return ''.join(f'<ellipse cx="{x}" cy="{y-i*16}" rx="{r}" ry="{r*0.42}" class="gold o"/>' for i in range(n))

# --- 独裁・絶滅・区別 ---------------------------------------------------------

add('dictatorship', '高い台に一人だけが立ち、下の人々へ一方向にだけ指示が下りる',
    '独裁、独裁政権＝dictatorship。', f'''
<g transform="translate(300 210)"><path d="M-70 0h140v90h-140z" fill="{STONE}" class="o"/></g>
{person(300, 210, 1.1, 1, 'coral', 'violet', 'point', 'cap', 'flat')}
{''.join(head(90 + i * 84, 340, 24, 'teal', h) for i, h in enumerate(['short', 'short', 'short', 'short', 'short', 'short']))}
{''.join(f'<path d="M300 250L{110+i*84} 302" fill="none" stroke="{CRL}" stroke-width="4" marker-end="url(#ar)"/>' for i in range(6))}''', arrow=True)

add('die out', '同じ生きものの姿が一頭ずつ減り、最後の一頭は輪郭だけになって消える',
    '絶滅する、すたれる＝die out。', f'''
{beast(120, 320, 0.42, '#6b5a4a', 1)}
<g opacity="0.6">{beast(300, 320, 0.42, '#6b5a4a', 1)}</g>
<g opacity="0.22">{beast(470, 320, 0.42, '#6b5a4a', 1)}</g>
{''.join(f'<path d="M{190+i*170} 200h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9" marker-end="url(#ar)"/>' for i in range(2))}
{cross(540, 200, 0.6)}''', arrow=True)

add('differentiation', '同じ形の品が並ぶ中で、一つだけ色と印を変えて見分けがつくようにする',
    '区別、差別化＝differentiation。', f'''
{table(340)}
{''.join(f'<g transform="translate({{}} 290)"><path d="M-34-70h68v70h-68z" class="tealp o"/></g>'.format(90 + i * 84) for i in range(3))}
<g transform="translate(342 290)"><path d="M-34-70h68v70h-68z" class="coral o"/>
  {spark(0, -100, 1.0, 'gold')}</g>
{''.join(f'<g transform="translate({{}} 290)"><path d="M-34-70h68v70h-68z" class="tealp o"/></g>'.format(426 + i * 84) for i in range(2))}
{ring(342, 274, 78, True)}''')

# --- 消化 --------------------------------------------------------------------

add('digestion', '飲みこんだ食べ物が胃に入り、中で細かく分かれていく',
    '消化＝digestion。', f'''
{stomach(300, 200, 1.15)}
<g transform="translate(288 40)"><circle r="26" class="green o"/><path d="M0-26v-16" stroke="{GRND}" stroke-width="5" fill="none"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" class="greenp o"/>'.format(x, y, r) for x, y, r in [(272, 210, 14), (310, 230, 11), (288, 252, 9), (326, 196, 8)])}
{line(288, 76, 288, 124, MUTED, True, 4)}
{''.join(f'<path d="M{{}} {{}}q12 12 0 24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(400 + i * 18, 180 + i * 14) for i in range(3))}''', arrow=True)

add('digestive', '体の中の胃と腸のつながりを取り出して示した図',
    '消化の＝digestive。', f'''
<g transform="translate(300 200)">
  <path d="M-150-150h300v300h-300z" fill="#eef4f7" class="o"/></g>
<g transform="translate(300 130)">
  <path d="M0-70v40" fill="none" stroke="{CRLD}" stroke-width="20" stroke-linecap="round"/>
  <path d="M-24-30q-46 18-40 66 6 50 56 54 48 4 54-48 6-46-34-68z" class="coralp o"/></g>
<g transform="translate(300 280)">
  <path d="M-70-30h140v110h-140z" fill="none" stroke="{CRLD}" stroke-width="18" stroke-linejoin="round"/>
  <path d="M-40-4h80v56h-80z" fill="none" stroke="{CRL}" stroke-width="14" stroke-linejoin="round"/></g>
{ring(300, 210, 128, True)}''')

# --- 捨てる・かき乱す ---------------------------------------------------------

add('dispose of', 'いらなくなった書類を、ふたを開けたごみ箱へ落とす',
    '処分する、捨てる＝dispose of。', f'''
{person(150, 340, 1.15, 1, 'teal', 'blue', 'give', 'short', 'flat')}
<g transform="translate(430 306)">
  <path d="M-70 0l14-140h112L470 0z" fill="none"/>
  <path d="M-70 0l14-140h112L70 0z" fill="{MUTED}" class="o"/>
  <path d="M-80-140h160v20h-160z" fill="{INK}"/>
  {''.join(f'<path d="M{{}} -120v110" stroke="#9aa7b1" stroke-width="4" fill="none"/>'.format(-40 + i * 40) for i in range(3))}</g>
<g transform="translate(340 170) rotate(-24)">{doc(0, 0, 80, 104, 3)}</g>
{arc(230, 200, 400, 180, 80, MUTED, True, 5)}''', arrow=True)

add('disruptive', 'きれいに並んでいた列に横から割り込みが入り、並びが崩れる',
    '混乱させる、一変させる＝disruptive。', f'''
{''.join(f'<rect x="{{}}" y="250" width="46" height="80" rx="6" class="tealp o"/>'.format(70 + i * 58) for i in range(3))}
<g transform="translate(300 290) rotate(-18)"><rect x="-23" y="-40" width="46" height="80" rx="6" class="coral o"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-23" y="-40" width="46" height="80" rx="6" class="tealp o"/></g>'.format(x, y, r) for x, y, r in [(380, 280, 26), (450, 300, -34), (520, 268, 48)])}
{arc(300, 120, 300, 216, 0, CRL, False, 6)}
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{CRL}" stroke-width="4"/>'.format(400 + i * 30, 220 - i * 10) for i in range(3))}''', arrow=True)

add('dissent', 'みなが同じ色の札を上げる中で、一人だけ違う色の札を上げる',
    '異議、反対意見＝dissent。', f'''
{''.join(head(90 + i * 86, 320, 26, 'teal', 'short') for i in range(3))}
{head(348, 320, 26, 'coral', 'bob')}
{''.join(head(434 + i * 86, 320, 26, 'teal', 'bun') for i in range(2))}
{''.join(f'<rect x="{{}}" y="150" width="52" height="66" rx="6" class="teal o"/>'.format(64 + i * 86) for i in range(3))}
<rect x="322" y="130" width="52" height="66" rx="6" class="coral o"/>
{''.join(f'<rect x="{{}}" y="150" width="52" height="66" rx="6" class="teal o"/>'.format(408 + i * 86) for i in range(2))}
{ring(348, 164, 56, True)}''')

# --- 論文・多角化・廃止 -------------------------------------------------------

add('dissertation', '机の上に、分厚くとじた論文と積み上げた参考書が並ぶ',
    '学位論文＝dissertation。', f'''
{table(330)}
<g transform="translate(250 250)">
  <path d="M-90-80h180v160h-180z" fill="#fffefd" class="o"/>
  <path d="M-90-80h180v160h-180z" fill="none" class="o"/>
  <path d="M-96-80h14v160h-14z" class="teald o"/>
  {''.join(f'<rect x="-64" y="{{}}" width="{{}}" height="9" rx="4.5" fill="{MUTED}"/>'.format(-52 + i * 24, 130 - (i % 3) * 30) for i in range(5))}</g>
{''.join(f'<g transform="translate(460 {{}})"><path d="M-66-16h132v32h-132z" class="{{}} o"/></g>'.format(314 - i * 34, c) for i, c in enumerate(['coral', 'green', 'violet', 'blue']))}
{spark(160, 140, 1.0, 'gold')}''')

add('diversify', '一種類だけだった畑が、何種類もの作物に分かれて植えられる',
    '多角化する、多様にする＝diversify。', f'''
{split()}
<path d="M20 240h250v120H20z" class="greenp o"/>
{''.join(flower(60 + i * 48, 300, 0.55, 'green') for i in range(5))}
<path d="M330 240h250v120H330z" class="greenp o"/>
{''.join(flower(370 + i * 48, 300, 0.55, c) for i, c in enumerate(['coral', 'gold', 'violet', 'blue', 'teal']))}
{arc(276, 180, 340, 190, 40, MUTED, True, 4)}''', arrow=True)

add('do away with', '掲げてあった古い規則の札を外し、そのまま捨てる',
    '廃止する、取り除く＝do away with。', f'''
<g transform="translate(200 160)">
  <path d="M-90-70h180v140h-180z" fill="#f0e6d2" class="o" transform="rotate(-14)"/>
  {''.join(f'<rect x="-60" y="{{}}" width="{{}}" height="9" rx="4.5" fill="{MUTED}" transform="rotate(-14 0 0)"/>'.format(-40 + i * 28, 120 - (i % 2) * 34) for i in range(3))}</g>
{cross(200, 160, 1.2)}
{arc(300, 180, 440, 230, 80, MUTED, True, 5)}
<g transform="translate(480 306)">
  <path d="M-60 0l12-120h96L60 0z" fill="{MUTED}" class="o"/>
  <path d="M-70-120h140v18h-140z" fill="{INK}"/></g>
{person(90, 340, 1.0, 1, 'teal', 'blue', 'reach', 'short', 'flat')}''', arrow=True)

# --- 急激・頼って使う ---------------------------------------------------------

add('drastically', '折れ線が一段で大きく落ちこみ、落差がひときわ大きい',
    '大幅に、劇的に＝drastically。', f'''
<path d="M70 350h460M70 350V50" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<path d="M100 110L220 96" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>
<path d="M220 96L300 310" fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round"/>
<path d="M300 310L500 300" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>
<path d="M360 96h-56M360 310h-46" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>
<path d="M360 100v200" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

add('draw on', '蓄えのたるから管を引き、たまっていた分を必要なだけ使う',
    '(経験・資金を)頼りに使う＝draw on。', f'''
{table(340)}
<g transform="translate(170 230)">
  <path d="M-80-90q-24 90 0 180h160q24-90 0-180z" fill="#c9a464" class="o"/>
  <path d="M-86-40h172M-86 30h172" fill="none" stroke="{BRN}" stroke-width="8"/>
  <path d="M80 40h34v18H80z" fill="{MUTED}" class="o"/></g>
<path d="M290 280q80 0 80-40" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
{''.join(drop(370, 260 + i * 26, 1.0, 'gold') for i in range(2))}
<g transform="translate(430 300)">
  <path d="M-44 30l8-70h72l8 70z" fill="#fffefd" class="o"/>
  <path d="M-32-14h64l6 44h-76z" class="goldp"/></g>
{arc(230, 150, 400, 200, 80, MUTED, True, 4)}''', arrow=True)

# --- 正式に・耐久 ------------------------------------------------------------

add('duly', 'カレンダーの期日ちょうどに書類が受理され、判が押される',
    '正式に、しかるべく＝duly。', f'''
<g transform="translate(190 190)">
  <path d="M-130-120h260v240h-260z" fill="#fffefd" class="o"/>
  <path d="M-130-120h260v44h-260z" class="teal o"/>
  {''.join(f'<path d="M{{}} -76v196" fill="none" stroke="{MUTED}" stroke-width="2.5"/>'.format(-130 + c * 65) for c in range(1, 4))}
  {''.join(f'<path d="M-130 {{}}h260" fill="none" stroke="{MUTED}" stroke-width="2.5"/>'.format(-76 + r * 66) for r in range(1, 3))}
  <circle cx="-33" cy="24" r="26" class="coralp o"/></g>
{doc(450, 230, 150, 190, 3)}
<g transform="translate(450 250)"><circle r="40" class="coralp o"/><circle r="26" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{tick(450, 96, 0.8)}''')

add('durability', 'ハンマーで何度たたいても、その板は割れずに残る',
    '耐久性、長持ちすること＝durability。', f'''
{table(340)}
<g transform="translate(300 300)"><path d="M-170-34h340v34h-340z" fill="#c9a464" class="o"/></g>
<g transform="translate(300 180) rotate(-30)">
  <path d="M-14 0h28v150h-28z" fill="{BRN}" class="o"/>
  <path d="M-56-44h112v44h-112z" fill="{MUTED}" class="o"/></g>
{''.join(f'<path d="M{{}} {{}}l18-22" fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round"/>'.format(190 + i * 22, 268 - i * 14) for i in range(3))}
{tick(480, 200, 0.9)}
{''.join(f'<path d="M{{}} 240q16-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(410 + i * 18) for i in range(2))}''')

add('durable', '何年たっても形の変わらない同じかばんが、ずっと使われ続ける',
    '長持ちする、耐久性のある＝durable。', f'''
{split()}
{''.join(f'<g transform="translate({{}} 230)"><path d="M-70-50h140v110h-140z" class="goldd o"/><path d="M-40-50q40-40 80 0" fill="none" stroke="{BRN}" stroke-width="10"/><path d="M-70-10h140" fill="none" stroke="{BRN}" stroke-width="5"/></g>'.format(x) for x in (160, 440))}
{clock(160, 350, 26, 10, 10)}
{''.join(clock(410 + i * 60, 350, 26, 10, 10) for i in range(3))}
{arc(250, 180, 350, 180, 44, MUTED, True, 4)}
{tick(440, 90, 0.8)}''', arrow=True)

# --- くよくよ・食いつぶす -----------------------------------------------------

add('dwell on', '一度の失敗の場面が、頭の中でぐるぐると回り続けてやまない',
    'くよくよ考える、長々と述べる＝dwell on。', f'''
{person(160, 350, 1.15, 1, 'teal', 'blue', 'think', 'short', 'sad')}
<g transform="translate(380 170)">
  <circle r="120" fill="#fffefd" class="o"/>
  <path d="M-54-20h108v56h-108z" class="coralp o"/>
  {cross(0, 6, 0.7)}</g>
<path d="M380 30a140 140 0 1 0 100 42" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"/>
<circle cx="236" cy="238" r="13" fill="#fffefd" class="o"/>
<circle cx="212" cy="266" r="9" fill="#fffefd" class="o"/>''', arrow=True)

add('eat into', '積んだコインの山が、横からかじられるように少しずつ欠けていく',
    '(貯えや時間を)食いつぶす＝eat into。', f'''
{table(340)}
{coinstack(180, 300, 6, 54)}
<g opacity="0.25">{coinstack(400, 300, 6, 54)}</g>
{coinstack(400, 300, 2, 54)}
<path d="M340 250q40-30 0-60" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="10 9"/>
{''.join(f'<path d="M{{}} {{}}q-16 14 0 28" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(470 + i * 20, 200 + i * 14) for i in range(3))}
{arc(250, 190, 360, 200, 60, MUTED, True, 4)}''', arrow=True)

# --- 詳述・弾力・電化 ---------------------------------------------------------

add('elaboration', '一行だけだったメモが、図と説明のついた詳しい紙に膨らむ',
    '詳しい説明、精緻化＝elaboration。', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-70-90h140v180h-140z" class="paper"/>
  <rect x="-50" y="-10" width="100" height="10" rx="5" fill="{MUTED}"/></g>
<g transform="translate(440 200)">
  <path d="M-90-120h180v240h-180z" class="paper"/>
  <path d="M-66-96h60v54h-60z" class="tealp o"/>
  <circle cx="46" cy="-68" r="26" class="coralp o"/>
  {''.join(f'<rect x="-66" y="{{}}" width="{{}}" height="9" rx="4.5" fill="{MUTED}"/>'.format(-24 + i * 26, 132 - (i % 3) * 30) for i in range(5))}</g>
{arc(240, 170, 330, 170, 50, MUTED, True, 5)}''', arrow=True)

add('elasticity', '輪ゴムを引っ張ると長く伸び、手を離すと元の形に戻る',
    '弾力性＝elasticity。', f'''
{split()}
<g transform="translate(150 200)"><ellipse rx="66" ry="66" fill="none" stroke="{CRL}" stroke-width="16"/></g>
{hand(150, 320, 1)}
<g transform="translate(440 200)"><ellipse rx="40" ry="120" fill="none" stroke="{CRL}" stroke-width="12"/></g>
{hand(440, 60, 1)}
{hand(440, 340, -1)}
{arc(240, 150, 340, 150, 44, MUTED, True, 4)}
{arc(520, 130, 520, 260, -70, MUTED, True, 4)}''', arrow=True)

add('electrify', '線路の上に架線が引かれ、電車がその電気で走り出す',
    '電化する、興奮させる＝electrify。', f'''
{''.join(f'<path d="M{{}} 306v-190" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>'.format(70 + i * 230) for i in range(3))}
<path d="M70 120h460" fill="none" stroke="{INK}" stroke-width="6"/>
<g transform="translate(320 306)">
  <path d="M-140 0v-120h280V0z" class="teal o"/>
  <path d="M-110-100h90v50h-90zM20-100h90v50H20z" class="tealp o"/>
  <path d="M0-120l-40-60h80z" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="-80" cy="6" r="18" class="ink"/><circle cx="80" cy="6" r="18" class="ink"/></g>
<path d="M20 330h560" fill="none" stroke="{BRN}" stroke-width="8"/>
{bolt(320, 90, 1.1)}''')

# --- 資格 --------------------------------------------------------------------

add('eligibility', '受付で条件表と照らし合わせ、条件を満たした人に証が渡される',
    '資格があること＝eligibility。', f'''
{table(280)}
{person(140, 340, 1.05, 1, 'teal', 'blue', 'reach', 'bob', 'smile')}
{person(470, 280, 1.0, -1, 'coral', 'green', 'give', 'short', 'smile')}
<g transform="translate(470 170)">
  {''.join(f'<g transform="translate(0 {{}})"><rect x="-50" y="-11" width="72" height="18" rx="6" fill="{MUTED}"/>{{}}</g>'.format(-34 + i * 34, tick(44, 0, 0.3)) for i in range(3))}</g>
{doc(300, 210, 96, 64, 2)}
{arc(400, 210, 250, 230, 50, MUTED, True, 4)}''', arrow=True)

add('eligible for', '身長の線を越えた人だけが、乗り物の列に進める',
    '〜の資格がある＝eligible for。', f'''
<g transform="translate(180 306)">
  <path d="M-16 0v-260h32V0z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M16 {{}}h22" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(-40 - i * 40) for i in range(5))}
  <path d="M-40-176h100" fill="none" stroke="{CRL}" stroke-width="6" stroke-dasharray="12 10"/></g>
{person(110, 340, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{tick(110, 90, 0.7)}
{person(400, 340, 0.78, 1, 'coral', 'green', 'stand', 'bob', 'sad')}
{cross(400, 180, 0.6)}
<g transform="translate(520 306)">
  <path d="M-50 0v-70h100V0z" class="gold o"/><circle cx="-26" cy="10" r="14" class="ink"/><circle cx="26" cy="10" r="14" class="ink"/></g>''')

# --- 制定・暗号 --------------------------------------------------------------

add('enactment', '議場で多数の手が挙がり、法の書に印が押されて成立する',
    '(法律の)制定＝enactment。', f'''
{''.join(f'<g transform="translate({{}} 300)">{{}}</g>'.format(90 + i * 76, person(0, 0, 0.86, 1, c, 'blue', 'up', h, 'smile')) for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('blue', 'bun'), ('violet', 'cap')]))}
<g transform="translate(460 250)">
  <path d="M-80-90h160v180h-160z" fill="#fffefd" class="o"/>
  <path d="M-86-90h14v180h-14z" class="teald o"/>
  <circle cx="10" cy="10" r="36" class="coralp o"/>
  <circle cx="10" cy="10" r="22" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{tick(460, 100, 0.8)}''')

add('encryption', '読める文が鍵をかけたとたん、意味の取れない記号の列に変わる',
    '暗号化＝encryption。', f'''
{split()}
<g transform="translate(150 180)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  {''.join(f'<rect x="-66" y="{{}}" width="{{}}" height="10" rx="5" fill="{INK}"/>'.format(-46 + i * 30, 132 - (i % 3) * 30) for i in range(4))}</g>
<g transform="translate(450 180)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  {''.join(f'<rect x="{{}}" y="{{}}" width="16" height="16" rx="3" fill="{VIO}" transform="rotate({{}} {{}} {{}})"/>'.format(-70 + (i % 5) * 32, -46 + (i // 5) * 34, 20 * (i % 3), -62 + (i % 5) * 32, -38 + (i // 5) * 34) for i in range(15))}</g>
<g transform="translate(300 300)">
  <circle cy="-30" r="30" fill="none" stroke="{GLD}" stroke-width="12"/>
  <path d="M-38 0h76v60h-76z" class="gold o"/>
  <circle cy="26" r="8" class="ink"/></g>
{arc(250, 150, 350, 150, 46, MUTED, True, 5)}''', arrow=True)

# --- 従事・向上・豊かに ---------------------------------------------------------

add('engage in', '外から見ていた人が輪の中に入り、一緒に手を動かして加わる',
    '(活動に)従事する、関わる＝engage in。', f'''
{ring(340, 230, 140, True, 'teal')}
{''.join(f'<g transform="translate({{}} {{}})">{{}}</g>'.format(x, y, head(0, 0, 26, c, h)) for x, y, c, h in [(250, 170, 'teal', 'short'), (430, 170, 'green', 'bob'), (250, 300, 'blue', 'bun'), (430, 300, 'gold', 'cap')])}
{person(90, 340, 1.05, 1, 'coral', 'violet', 'walk', 'short', 'smile')}
{arc(150, 240, 224, 240, 50, CRL, False, 5)}''', arrow=True)

add('enhancement', '同じ写真が、色と明るさを足されていっそう良く見えるようになる',
    '向上、強化＝enhancement。', f'''
{split()}
<g transform="translate(150 200)" opacity="0.42">
  <path d="M-100-80h200v160h-200z" fill="#fffefd" class="o"/>
  <circle cx="-40" cy="-30" r="26" fill="{MUTED}"/>
  <path d="M-90 80q60-90 120-30t70 30z" fill="{MUTED}"/></g>
<g transform="translate(450 200)">
  <path d="M-100-80h200v160h-200z" fill="#fffefd" class="o"/>
  <circle cx="-40" cy="-30" r="26" class="gold o"/>
  <path d="M-90 80q60-90 120-30t70 30z" class="green o"/></g>
{arc(266, 160, 336, 160, 46, MUTED, True, 5)}
{''.join(spark(520 + i * 0, 100 + i * 0, 1.0, 'gold') for i in range(1))}
{spark(370, 90, 0.8, 'gold')}''', arrow=True)

add('enrichment', 'やせた土に養分を足すと、細かった苗がしっかり実をつける',
    '豊かにすること、強化＝enrichment。', f'''
{split()}
<path d="M20 300h250v60H20z" fill="#cbb896" class="o"/>
<g transform="translate(150 300)"><path d="M0 0v-70" stroke="{GRND}" stroke-width="6" fill="none"/>
  <ellipse cx="-14" cy="-74" rx="14" ry="8" class="greenp o"/></g>
<path d="M330 300h250v60H330z" fill="#8b6437" class="o"/>
<g transform="translate(450 300)"><path d="M0 0v-120" stroke="{GRND}" stroke-width="9" fill="none"/>
  <ellipse cx="-26" cy="-100" rx="24" ry="13" class="green o"/>
  <ellipse cx="26" cy="-76" rx="24" ry="13" class="green o"/>
  <circle cx="0" cy="-130" r="18" class="coral o"/></g>
<g transform="translate(300 150) rotate(26)">
  <path d="M-30-50h60v80l-30 34-30-34z" class="goldp o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="6" class="gold"/>'.format(350 + i * 26, 236 + (i % 2) * 20) for i in range(4))}''')

# --- 権利・持ち分・浸食 -------------------------------------------------------

add('entitlement', '券を持った人が、当然の顔で窓口から自分の分を受け取る',
    '権利、受給資格＝entitlement。', f'''
{table(270)}
{person(150, 340, 1.1, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
<g transform="translate(250 200) rotate(-8)">
  <path d="M-50-30h100v60h-100z" class="goldp o"/>
  <path d="M-20-30v60" fill="none" stroke="{GLDD}" stroke-width="3" stroke-dasharray="7 7"/></g>
{person(460, 270, 1.0, -1, 'coral', 'green', 'give', 'bun', 'smile')}
{box(370, 236, 74, 56, 18, 'violet')}
{arc(420, 190, 300, 200, 50, MUTED, True, 4)}''', arrow=True)

add('equity', '家の値段を表す積み木から、借り入れ分を除いた上の段が自分の取り分',
    '純資産、株式／公平＝equity。', f'''
<g transform="translate(300 330)">
  <path d="M-120-90h240v90h-240z" fill="{MUTED}" class="o"/>
  <path d="M-120-190h240v100h-240z" class="teal o"/></g>
{ring(300, 190, 100, True, 'teal')}
{house(300, 100, 0.5, 'coral')}
{''.join(f'<path d="M440 {{}}h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>'.format(y) for y in (140, 240, 330))}
<path d="M500 150v80" fill="none" stroke="{TEA}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M500 250v72" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

add('erosion', '波が繰り返し打ち寄せ、崖のふちが削られて後ろへ下がる',
    '浸食、侵食＝erosion。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 262q22-14 44 0t44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
<path d="M0 60h300v190l-40 30-20-40-30 20V60z" fill="#cbb896" class="o"/>
<path d="M0 60h230v170l-30 24-18-34-26 18V60z" fill="#d9c9a8"/>
<g opacity="0.3"><path d="M300 60v230" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/></g>
{''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{BLU}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"/>'.format(430, 200 + i * 46, 290, 200 + i * 46) for i in range(3))}''', arrow=True)

add('escalation', '小さな火から始まり、段を上がるごとに炎が大きくなっていく',
    '段階的な激化、拡大＝escalation。', f'''
{''.join(f'<path d="M{{}} 340v-{{}}h110v{{}}z" fill="{STONE}" class="o"/>'.format(60 + i * 110, 40 + i * 60, 40 + i * 60) for i in range(4))}
{flame(110, 292, 0.30)}
{flame(220, 232, 0.46)}
{flame(330, 172, 0.62)}
{flame(440, 112, 0.82)}
{arc(120, 250, 430, 80, 90, MUTED, True, 5)}''', arrow=True)

# --- 不動産・ならす・明らか ---------------------------------------------------

add('estate agent', '売り出し看板の立つ家の前で、業者が客に鍵を手渡す',
    '不動産業者(英)＝estate agent。', f'''
{house(440, 306, 1.0, 'coral')}
<g transform="translate(300 306)">
  <path d="M-8 0v-110h16V0z" fill="{BRN}"/>
  <path d="M-70-170h140v66h-140z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="-50" y="{{}}" width="{{}}" height="9" rx="4.5" fill="{MUTED}"/>'.format(-152 + i * 22, 100 - i * 34) for i in range(2))}</g>
{person(140, 340, 1.1, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
{person(240, 340, 1.05, -1, 'coral', 'green', 'reach', 'short', 'smile')}
<g transform="translate(192 236)">
  <circle r="12" fill="none" stroke="{GLD}" stroke-width="5"/>
  <path d="M12 0h36" stroke="{GLD}" stroke-width="6" fill="none"/>
  <path d="M40 0v12h10V0z" fill="{GLD}"/></g>''')

add('even out', 'でこぼこだった面をならして、どこも同じ高さにそろえる',
    'ならす、平均化する＝even out。', f'''
{split()}
{''.join(f'<rect x="{{}}" y="{{}}" width="44" height="{{}}" rx="4" class="tealp o"/>'.format(50 + i * 54, 330 - h, h) for i, h in enumerate([140, 60, 190, 90]))}
{''.join(f'<rect x="{{}}" y="210" width="44" height="120" rx="4" class="teal o"/>'.format(350 + i * 54) for i in range(4))}
<path d="M340 204h250" fill="none" stroke="{GRN}" stroke-width="5" stroke-dasharray="12 10"/>
{arc(272, 190, 330, 190, 40, MUTED, True, 4)}
<g transform="translate(150 120)"><path d="M-90 0h180v20h-180z" fill="{BRN}" class="o"/>
  <path d="M-10-46h20v46h-20z" fill="{BRN}"/></g>''', arrow=True)

add('evidently', '雪の上にくっきり足あとが残り、誰が通ったかひと目で分かる',
    'どうやら、明らかに＝evidently。', f'''
<path d="M0 250h600v150H0z" fill="#eef4f7"/>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><ellipse rx="15" ry="24" class="ink"/><ellipse cy="-26" rx="11" ry="9" class="ink"/></g>'.format(80 + i * 62, 340 - (i % 2) * 34, -14) for i in range(7))}
{person(520, 240, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
<g transform="translate(130 140)">
  <circle r="54" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M38 38l44 44" stroke="{BRN}" stroke-width="16" stroke-linecap="round" fill="none"/></g>''')

# --- 悪化・きわめて・直視 -----------------------------------------------------

add('exacerbate', '燃えている火に油を注ぎ足して、炎をいっそう大きくする',
    '(状況を)悪化させる＝exacerbate。', f'''
{flame(320, 330, 1.25)}
<g transform="translate(160 130) rotate(40)">
  <path d="M-34-70h68v110a24 24 0 0 1-24 24h-20a24 24 0 0 1-24-24z" class="goldp o"/>
  <path d="M-16-94h32v24h-32z" class="gold o"/></g>
{''.join(drop(226 + i * 16, 190 + i * 24, 1.1, 'gold') for i in range(3))}
{''.join(f'<path d="M{{}} {{}}l14-20" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>'.format(430 + i * 22, 210 - i * 20) for i in range(3))}''')

add('exceedingly', '温度計の赤い柱が目盛りの上端を突き抜けて、さらに上へ伸びる',
    'きわめて、非常に＝exceedingly。', f'''
{thermometer(300, 330, 1.0, 1.0)}
<path d="M293 176v-120" fill="none" stroke="{CRL}" stroke-width="14" stroke-linecap="round"/>
{''.join(f'<path d="M{{}} {{}}l16-22" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>'.format(340 + i * 22, 110 - i * 18) for i in range(3))}
<path d="M240 160h-46" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('face up to', '目をそらさず、壁に貼られた見たくない数字の紙に正面から向き合う',
    '(いやな事実を)直視する、受け入れる＝face up to。', f'''
<g transform="translate(400 180)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <path d="M-70 70L50-70" fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round"/>
  <path d="M50-70h-56M50-70v56" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/></g>
{person(160, 340, 1.3, 1, 'teal', 'blue', 'stand', 'short', 'flat')}
{line(220, 190, 280, 190, MUTED, True, 4)}
<g transform="translate(160 196)"><circle cx="-10" cy="0" r="0"/></g>''', arrow=True)

# --- 頼る・だめになる ---------------------------------------------------------

add('fall back on', '主の綱が切れても、下に張っておいた網が落ちる人を受け止める',
    '(いざというとき)頼りにする＝fall back on。', f'''
<path d="M300 20v70" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/>
{''.join(f'<path d="M{{}} {{}}l14 14" fill="none" stroke="{CRL}" stroke-width="4"/>'.format(276 + i * 16, 96 + i * 8) for i in range(3))}
{person(300, 230, 1.0, 1, 'teal', 'blue', 'up', 'short', 'flat')}
<g transform="translate(300 330)">
  <path d="M-190 0h380" fill="none" stroke="{GRN}" stroke-width="8" stroke-linecap="round"/>
  {''.join(f'<path d="M{{}} 0l{{}} -34" fill="none" stroke="{GRN}" stroke-width="4"/>'.format(-170 + i * 34, 18) for i in range(11))}
  {''.join(f'<path d="M{{}} 0l{{}} -34" fill="none" stroke="{GRN}" stroke-width="4"/>'.format(-170 + i * 34, -18) for i in range(11))}
  <path d="M-190-34h380" fill="none" stroke="{GRN}" stroke-width="5"/></g>
{line(300, 260, 300, 300, MUTED, True, 4)}''', arrow=True)

add('fall through', '床板が抜けて、進めていた計画の書類がそのまま穴へ落ちる',
    '(計画が)だめになる、流れる＝fall through。', f'''
{table(280)}
<g transform="translate(300 280)">
  <path d="M-260 0h150v20h-150zM110 0h150v20H110z" fill="#c9a464" class="o"/>
  <path d="M-110 0l14 20h30zM110 0l-14 20h-30z" fill="{BRN}"/></g>
<g transform="translate(300 350) rotate(18)">{doc(0, 0, 100, 130, 3)}</g>
{''.join(f'<path d="M{{}} {{}}l-20 30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>'.format(270 + i * 30, 290) for i in range(2))}
{person(120, 330, 1.0, 1, 'teal', 'blue', 'reach', 'bob', 'sad')}
{cross(480, 150, 0.7)}''')

# --- 農・平等・自力 ----------------------------------------------------------

add('farmer', '畑のうねの前で、麦を手にした人がくわを持って立つ',
    '農場主、農業をする人＝farmer。', f'''
<path d="M0 280h600v120H0z" class="greenp"/>
{''.join(f'<path d="M{{}} 380q30-40 60 0" fill="none" stroke="{GRND}" stroke-width="5"/>'.format(i * 120) for i in range(6))}
{''.join(f'<g transform="translate({{}} 300)"><path d="M0 0v-80" stroke="{GLDD}" stroke-width="6" fill="none"/><ellipse cy="-92" rx="14" ry="24" class="gold o"/></g>'.format(430 + i * 50) for i in range(3))}
{person(200, 330, 1.35, 1, 'blue', 'green', 'hold', 'cap', 'smile')}
<g transform="translate(262 250) rotate(16)">
  <path d="M0-90v150" stroke="{BRN}" stroke-width="9" stroke-linecap="round" fill="none"/>
  <path d="M-34 60h68v20h-68z" fill="{MUTED}" class="o"/></g>
{sun(520, 90, 42)}''')

add('feminism', '男女の記号が同じ高さの台に並び、掲げられた旗が二つを結ぶ',
    'フェミニズム、女性の権利の主張＝feminism。', f'''
{''.join(f'<path d="M{{}} 340v-60h140v60z" fill="{STONE}" class="o"/>'.format(70 + i * 220) for i in range(2))}
<g transform="translate(140 210)">
  <circle r="46" fill="none" stroke="{TEA}" stroke-width="12"/>
  <path d="M34-34l44-44M78-78h-36M78-78v36" fill="none" stroke="{TEA}" stroke-width="12" stroke-linecap="round"/></g>
<g transform="translate(360 200)">
  <circle r="46" fill="none" stroke="{CRL}" stroke-width="12"/>
  <path d="M0 46v56M-28 74h56" fill="none" stroke="{CRL}" stroke-width="12" stroke-linecap="round"/></g>
<path d="M110 90h340" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/>
<g transform="translate(500 306)"><path d="M0 0v-190" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M4-190h80l-20 30 20 30H4z" class="violet o"/></g>''')

add('fend for', 'だれの助けも借りず、自分で火をおこして自分の食事を用意する',
    '(fend for oneself で)自分でなんとかする＝fend for。', f'''
{flame(400, 320, 0.7)}
<g transform="translate(400 250)">
  <path d="M-60 0h120" stroke="{MUTED}" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M-70-30q70-30 140 0v14q-70 26-140 0z" fill="{STONE}" class="o"/></g>
{person(170, 340, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'flat')}
<g opacity="0.28">{person(80, 340, 0.9, 1, 'coral', 'green', 'stand', 'bob', 'flat')}</g>
{cross(80, 150, 0.55)}
{''.join(f'<path d="M{{}} {{}}q10-14 0-26" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(470 + i * 18, 230 - i * 12) for i in range(2))}''')

add('fend off', '飛んでくる石を盾で受け、はね返してわきへそらす',
    '(攻撃・質問を)かわす、はねのける＝fend off。', f'''
{person(400, 340, 1.25, -1, 'teal', 'blue', 'reach', 'short', 'flat')}
<g transform="translate(320 200)">
  <path d="M-56-70h112v80q0 56-56 84-56-28-56-84z" class="bluep o"/>
  <path d="M0-70v164" fill="none" stroke="{BLUD}" stroke-width="5"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="{{}}" fill="{STONE}" class="o"/>'.format(x, y, r) for x, y, r in [(120, 160, 20), (150, 250, 16)])}
{line(140, 170, 250, 190, MUTED, False, 5)}
{arc(260, 170, 160, 80, 60, CRL, False, 5)}
<circle cx="150" cy="86" r="18" fill="{STONE}" class="o"/>''', arrow=True)

add('fertility', '肥えた黒い土から、太い茎の作物がいくつも実をつけて育つ',
    '肥沃さ、繁殖力＝fertility。', f'''
<path d="M0 300h600v100H0z" fill="#5b4636"/>
{''.join(f'<g transform="translate({{}} 300)"><path d="M0 0v-140" stroke="{GRND}" stroke-width="10" fill="none"/><ellipse cx="-30" cy="-110" rx="28" ry="14" class="green o"/><ellipse cx="30" cy="-86" rx="28" ry="14" class="green o"/><circle cy="-152" r="22" class="coral o"/></g>'.format(110 + i * 130) for i in range(4))}
{''.join(f'<path d="M{{}} 340q20 14 40 0" fill="none" stroke="#3f3126" stroke-width="4"/>'.format(40 + i * 110) for i in range(5))}
{sun(520, 80, 40)}''')

add('fiance', '指輪をはめた左手を見せる男性が、婚約相手と並んで立つ',
    '婚約者(男性)＝fiancé。fiancée(女性)と対になる語です。', f'''
{person(200, 340, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
{person(420, 340, 1.25, -1, 'coral', 'green', 'stand', 'bob', 'smile')}
{ring_obj(288, 200, 1.5)}
{ring(200, 250, 84, True, 'teal')}
<g transform="translate(310 100)">
  <path d="M0 26q-34-26-34-48 0-18 18-18 10 0 16 12 6-12 16-12 18 0 18 18 0 22-34 48z" class="coralp o"/></g>''', key='fiancé')

finish(__file__)
