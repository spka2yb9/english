# -*- coding: utf-8 -*-
"""第178回。ta-/te-/th-/ti-/to-/tr-/tu-/tw-/u- の語。stamp out の描き直しも含む。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def body(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cy="-192" r="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-84-140q84-30 168 0 24 140 0 280h-168q-24-140 0-280z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>')

def plane_small(x, y, s=1, r=0):
    return plane(x, y, s, r, 'teal')

# --- 第176/177回の描き直し ---------------------------------------------------

add('stamp out', '燃え残った小さな火を、靴の裏で踏みつけて完全に消す',
    '根絶する、踏み消す＝stamp out。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<g opacity="0.45">{flame(330, 344, 0.4)}</g>
<g transform="translate(270 290)">
  <path d="M-40-140h70q14 0 14 16v96l90 34q14 6 14 20v14h-188z" fill="{INK}"/>
  <path d="M-40 40h188v18h-188z" fill="#1f2a38"/>
  <path d="M-40-140h70v30h-70z" fill="{BLUD}"/>
  <path d="M60-16l60 22" stroke="#1f2a38" stroke-width="4" fill="none"/></g>
{''.join(f'<path d="M{398+i*22} {286-i*18}l16-20" fill="none" stroke="{GLD}" stroke-width="5"/>' for i in range(2))}
{cross(510, 150, 0.7)}''')

# --- 説得・集計・かぎづめ -----------------------------------------------------

add('talk into', 'しぶる相手に言葉で押し続け、とうとうその気にさせる',
    '説得して〜させる＝talk into。', f'''
{person(130, 350, 1.2, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<g transform="translate(300 170)">
  <path d="M-90-56h180v112h-30l-18 28-14-28h-118z" fill="#fffefd" class="o"/>
  <path d="M-56-10h112" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} {{}}h44" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(398, 150 + i * 46) for i in range(2))}
<g opacity="0.3">{person(500, 350, 1.2, -1, 'coral', 'green', 'stand', 'bob', 'sad')}</g>
{person(470, 350, 1.2, -1, 'coral', 'green', 'up', 'bob', 'smile')}''', arrow=True)

add('tally', '棒を数えて出した数が、帳面の数とぴたり一致する',
    '集計する、一致する／集計＝tally。', f'''
{table(352)}
<g transform="translate(180 220)">
  <path d="M-110-90h220v180h-220z" class="paper"/>
  {''.join(f'<g transform="translate({-70+(i%2)*100} {-40+(i//2)*60})">{"".join(f"<path d=\'M{-24+j*12} -22v44\' stroke=\'{INK}\' stroke-width=\'5\' fill=\'none\'/>" for j in range(4))}<path d="M-30 22l60-44" stroke="{INK}" stroke-width="5" fill="none"/></g>' for i in range(4))}</g>
<g transform="translate(430 220)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <rect x="-60" y="-20" width="120" height="40" rx="20" class="teal"/></g>
{tick(300, 330, 0.7)}
<path d="M290 220h50" fill="none" stroke="{GRN}" stroke-width="6"/>
<path d="M290 206h50M290 234h50" fill="none" stroke="{GRN}" stroke-width="6"/>''')

add('talon', '猛禽の足先の、鋭く曲がったかぎづめが枝をつかむ',
    '(猛禽の)かぎづめ＝talon。', f'''
<g transform="translate(300 300)">
  <path d="M-200 0h400v26h-400z" fill="{BRN}" class="o"/>
  <path d="M0-160v120" stroke="#a0764a" stroke-width="34" fill="none" stroke-linecap="round"/>
  {''.join(f'<g transform="rotate({a} 0 -34)"><path d="M0-34q34 14 40 50-20-6-34-22" fill="#c8a05f" stroke="{INK}" stroke-width="3"/></g>' for a in (-52, 0, 52))}
  <path d="M0-34q-26 26-24 66 18-10 24-32" fill="#c8a05f" stroke="{INK}" stroke-width="3"/></g>
{''.join(f'<path d="M{{}} 300l-10 34" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(200 + i * 200) for i in range(2))}''')

# --- 関税・協力・取り壊し -----------------------------------------------------

add('tariff', '国境の線を越える荷に、通るたび追加の金が課される',
    '関税、料金表＝tariff。', f'''
<path d="M300 40v320" fill="none" stroke="{CRL}" stroke-width="6" stroke-dasharray="16 12"/>
{box(140, 260, 120, 90, 30, 'gold')}
{arc(220, 200, 400, 200, 60, MUTED, True, 5)}
{box(450, 260, 120, 90, 30, 'gold')}
{''.join(coin(300, 140 + i * 50, 22) for i in range(2))}
<g transform="translate(300 60)"><path d="M-20 0h40M0-20v40" stroke="{CRL}" stroke-width="8" stroke-linecap="round" fill="none"/></g>''', arrow=True)

add('team up', '別々に動いていた二人が手を組み、同じ方向へ並んで進む',
    '組む、協力する＝team up。', f'''
<g opacity="0.28">
  {person(110, 180, 0.7, 1, 'teal', 'blue', 'walk', 'short', 'flat')}
  {person(110, 330, 0.7, 1, 'coral', 'green', 'walk', 'bob', 'flat')}</g>
{person(330, 350, 1.2, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{person(430, 350, 1.2, 1, 'coral', 'green', 'walk', 'bob', 'smile')}
<path d="M372 240h46" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
{arc(200, 200, 300, 230, 50, MUTED, True, 4)}
{arc(200, 320, 300, 290, -50, MUTED, True, 4)}
{tick(520, 130, 0.7)}''', arrow=True)

add('tear down', '鉄球が壁にぶつかり、建物が崩れて瓦礫になる',
    '(建物を)取り壊す＝tear down。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<g transform="translate(410 330)">
  <path d="M-100 0v-190h100V0z" fill="#fffdf6" class="o"/>
  <path d="M-70-160h40v40h-40zM-70-90h40v40h-40z" class="tealp o"/>
  <path d="M0-190l30 10-20 40 40 20-26 40 40 20-30 60" fill="none" stroke="{MUTED}" stroke-width="5"/></g>
<path d="M180 40v60" fill="none" stroke="{MUTED}" stroke-width="8"/>
<path d="M180 100L280 200" fill="none" stroke="{MUTED}" stroke-width="7"/>
<circle cx="300" cy="220" r="46" fill="#6b7680" class="o"/>
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(350 + i * 20, 180 - i * 16) for i in range(2))}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-22" y="-14" width="44" height="28" rx="3" fill="{STONE}" stroke="{INK}" stroke-width="2.5"/></g>'.format(x, y, r) for x, y, r in [(500, 350, 20), (550, 320, -30), (460, 370, 40)])}''')

# --- 叱る・速さ・賃借 ---------------------------------------------------------

add('tell off', '人差し指を立て、相手にきつく言い聞かせる',
    '叱る、小言を言う＝tell off。', f'''
{person(180, 350, 1.35, 1, 'teal', 'blue', 'point', 'bun', 'sad')}
<g transform="translate(300 210)"><path d="M-8 0h16v-40h-16z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/></g>
{person(470, 350, 1.15, -1, 'coral', 'green', 'stand', 'short', 'sad')}
{''.join(f'<path d="M{{}} {{}}h40" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(330, 150 + i * 44) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{CRL}" stroke-width="4"/>'.format(500 + i * 18, 150 - i * 14) for i in range(2))}''', arrow=True)

add('tempo', '振り子のついた拍子の道具が、左右に一定の速さで振れる',
    'テンポ、速度＝tempo。', f'''
<g transform="translate(300 340)">
  <path d="M-90 0h180L60-260h-120z" class="goldp o"/>
  <path d="M-60-240h120" fill="none" stroke="{GLDD}" stroke-width="4"/>
  <path d="M0-20v-240" stroke="{INK}" stroke-width="6" fill="none"/>
  <rect x="-20" y="-160" width="40" height="26" rx="5" class="coral o"/>
  {''.join(f'<path d="M20 {-40-i*36}h22" stroke="{MUTED}" stroke-width="4" fill="none"/>' for i in range(5))}</g>
<g opacity="0.28">
  <path d="M300 320L214 100M300 320L386 100" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/></g>
<g transform="translate(300 70)"><path d="M-70 0q70-30 140 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/></g>''', arrow=True)

add('tenancy', '部屋を借りている期間が、カレンダーの上で帯になって示される',
    '賃借、賃貸借契約期間＝tenancy。', f'''
{house(150, 200, 0.62, 'coral')}
<g transform="translate(400 250)">
  <path d="M-160-130h320v260h-320z" fill="#fffefd" class="o"/>
  <path d="M-160-130h320v46h-320z" class="teal o"/>
  {''.join(f'<path d="M{-160+c*64} -84v214" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for c in range(1, 5))}
  {''.join(f'<path d="M-160 {-84+r*72}h320" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for r in range(1, 3))}
  <path d="M-130-56h290v24h-290zM-160 16h290v24h-290z" class="tealp"/></g>
<g transform="translate(150 320)">
  <circle r="16" fill="none" stroke="{GLD}" stroke-width="7"/>
  <path d="M16 0h54" stroke="{GLD}" stroke-width="8" fill="none"/>
  <path d="M56 0v16h12V0z" fill="{GLD}"/></g>''')

# --- 腱・張り・終了 ----------------------------------------------------------

add('tendon', 'かかとの上で、筋肉と骨をつなぐ丈夫なひもが張っている',
    '腱(けん)＝tendon。', f'''
<g transform="translate(300 210)">
  <path d="M-60-160q60-24 120 0 24 90 0 140h-120q-24-50 0-140z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60-20q60 30 120 0v100l60 40v30h-180v-50z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M20-30q10 80 0 120" fill="none" stroke="#e8d7b8" stroke-width="24" stroke-linecap="round"/>
  <path d="M20-30q10 80 0 120" fill="none" stroke="#c9b48e" stroke-width="4"/></g>
{ring(320, 250, 68, True)}
{''.join(f'<path d="M{{}} 120h50" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}''')

add('tense', '弓の弦がぴんと張りつめ、少しの力でも震えそうになる',
    '緊張した、張りつめた＝tense。', f'''
<g transform="translate(300 200)">
  <path d="M60-160q80 160 0 320" fill="none" stroke="{BRN}" stroke-width="14" stroke-linecap="round"/>
  <path d="M60-160L-70 0 60 160" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-110 0h190" fill="none" stroke="{BRN}" stroke-width="7"/>
  <path d="M-110 0l30-14v28z" class="ink"/></g>
{''.join(f'<path d="M{{}} {{}}q14-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(400 + i * 20, 130 + i * 0) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}q14-14 0-28" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(400 + i * 20, 290) for i in range(2))}''')

add('termination', 'つながっていた線が終わりの印で断たれ、その先はもうない',
    '終了、解雇＝termination。', f'''
<path d="M60 200h240" fill="none" stroke="{TEA}" stroke-width="16" stroke-linecap="round"/>
<path d="M300 130v140" fill="none" stroke="{CRL}" stroke-width="10" stroke-linecap="round"/>
<g opacity="0.28"><path d="M340 200h200" fill="none" stroke="{MUTED}" stroke-width="14" stroke-dasharray="14 12"/></g>
{cross(460, 200, 0.7)}
{doc(150, 330, 120, 60, 1)}''')

add('termite', '木の柱の中に穴を掘り進む、白っぽい小さなアリ',
    'シロアリ＝termite。', f'''
{table(352)}
<g transform="translate(240 240)">
  <path d="M-70-140h140v240h-140z" fill="#c9a464" class="o"/>
  {''.join(f'<circle cx="{-40+(i%3)*40}" cy="{-90+(i//3)*60}" r="{12+(i%3)*4}" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>' for i in range(9))}</g>
<g transform="translate(440 250) scale(1.5)">
  <ellipse rx="34" ry="20" fill="#e8dcc2" class="o"/>
  <circle cx="-32" cy="-4" r="14" fill="#e0d2b2" class="o"/>
  <circle cx="-48" cy="-6" r="10" fill="#d8c8a2" class="o"/>
  <path d="M-56-12l-14-8M-56-2l-14 6" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M-14 18l-8 18M4 20l0 18M22 16l10 18M-14-18l-8-16M4-20l0-16M22-16l10-16" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
  <circle cx="-42" cy="-10" r="2.4" class="ink"/></g>''')

# --- 言い換え・解凍・枠の外 -----------------------------------------------------

add('that is to say', '同じ中身を、別の言い方に置き換えて示す',
    'すなわち、つまり＝that is to say。', f'''
<g transform="translate(150 200)">
  <path d="M-100-70h200v140h-200z" fill="#fffefd" class="o"/>
  {''.join(f'<rect x="-76" y="{-44+i*32}" width="{152-(i%2)*50}" height="14" rx="7" fill="{INK}"/>' for i in range(3))}</g>
<g transform="translate(300 200)">
  <path d="M-36-18h72M-36 18h72" fill="none" stroke="{MUTED}" stroke-width="9" stroke-linecap="round"/></g>
<g transform="translate(450 200)">
  <path d="M-100-70h200v140h-200z" fill="#fffefd" class="o"/>
  <circle cx="-40" cy="-20" r="24" class="coral o"/>
  <path d="M-10 40h100v18h-100z" class="teal o"/>
  <path d="M20-44h70v40H20z" class="goldp o"/></g>''')

add('thaw', 'かたい氷がゆるんでとけ、下に水がたまっていく',
    '解凍する、とける／雪解け＝thaw。', f'''
{split()}
{table(352)}
<g transform="translate(150 280)">
  <path d="M-60-60h120v120h-120z" fill="#dff1f8" class="o"/>
  <path d="M-40-40h44v44h-44zM4 4h44v44H4z" fill="#ffffff" opacity="0.7"/></g>
<g transform="translate(450 300)">
  <path d="M-34-40h68v40h-68z" fill="#dff1f8" class="o"/>
  <ellipse cy="24" rx="100" ry="20" class="bluep o"/></g>
{''.join(drop(450 + (i - 1) * 24, 270 + i * 0, 1.0, 'blue') for i in range(2))}
{arc(250, 220, 350, 230, 44, MUTED, True, 4)}
{sun(520, 90, 36)}''', arrow=True)

add('think outside the box', '四角の枠の外まで線を伸ばして、内側だけでは解けない問いを解く',
    '既成の枠を超えて考える＝think outside the box。', f'''
<g transform="translate(280 220)">
  <path d="M-120-120h240v240h-240z" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 11"/>
  {''.join(f'<circle cx="{-80+(i%3)*80}" cy="{-80+(i//3)*80}" r="12" class="ink"/>' for i in range(9))}
  <path d="M-80-80L120 120M-80-80h240M-80-80L-80 200" fill="none" stroke="{CRL}" stroke-width="0"/>
  <path d="M-80 80L200-80 -80-80 80 200" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></g>
{spark(510, 110, 1.0, 'gold')}''')

add('think over', '結論を急がず、一晩おいてじっくり考え直す',
    'よく考える、検討する＝think over。', f'''
<g transform="translate(300 190)"><path d="M-260-150h520v300h-520z" fill="#2f3a4d"/></g>
<g transform="translate(480 100)"><path d="M0-46a46 46 0 1 0 34 78A56 56 0 0 1 0-46z" class="goldp o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#fff6d8"/>'.format(90 + (i * 67) % 400, 60 + (i * 43) % 120) for i in range(10))}
<g transform="translate(230 330)">
  <path d="M-130 0v-50h260v50z" fill="#fffefd" class="o"/>
  <path d="M-130-50h70v-40h-70z" class="bluep o"/>
  {head(-96, -74, 22, 'blue', 'short', 'flat')}</g>
<g transform="translate(150 150)">
  <path d="M-60-40h120v70h-120z" fill="#fffefd" class="o" rx="14"/>
  {''.join(f'<circle cx="{-30+i*30}" cy="-4" r="8" class="ink"/>' for i in range(3))}</g>
<circle cx="98" cy="222" r="11" fill="#fffefd" class="o"/>''')

# --- 打つ・結びつく・傾ける -----------------------------------------------------

add('thump', 'こぶしで机をドンと打ちつけ、上の物が跳ね上がる',
    'ドンと打つ／ドンという音＝thump。', f'''
{table(300)}
<g transform="translate(280 250)">
  <ellipse rx="60" ry="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60-10q60-24 120 0" fill="none" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30-46v-70h60v70" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>
{''.join(f'<path d="M{int(280+90*math.cos(math.radians(a)))} {int(292+30*math.sin(math.radians(a)))}l{int(34*math.cos(math.radians(a)))} {int(14*math.sin(math.radians(a)))}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for a in (-160, -200, 20, -20))}
<g transform="translate(460 230) rotate(16)">
  <path d="M-34-16h68v32h-68z" class="goldp o"/></g>
{''.join(f'<path d="M{{}} {{}}l-6 20" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(440 + i * 30, 190) for i in range(2))}''')

add('tie in with', '別々に見えた二つの形が、ぴたりとかみ合って一つになる',
    '〜と結びつく、つじつまが合う＝tie in with。', f'''
<g transform="translate(210 200)">
  <path d="M-110-90h110v50a30 30 0 0 1 0 60v70h-110z" class="teal o"/></g>
<g transform="translate(390 200)">
  <path d="M110-90H0v50a30 30 0 0 0 0 60v70h110z" class="coral o"/></g>
{''.join(f'<path d="M{{}} 100h{{}}" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(x, d) for x, d in [(160, 40), (440, -40)])}
{tick(300, 340, 0.7)}''', arrow=True)

add('tilt', 'まっすぐ立っていた板が、片側だけ持ち上がって斜めになる',
    '傾ける、傾く／傾き＝tilt。', f'''
{table(352)}
<g opacity="0.28"><path d="M160 300h280v-30H160z" fill="{MUTED}"/></g>
<g transform="translate(300 290) rotate(-22)">
  <path d="M-140-16h280v32h-280z" fill="#c9a464" class="o"/></g>
<g transform="translate(300 290)"><path d="M-90 0a90 90 0 0 1 24-60" fill="none" stroke="{CRL}" stroke-width="5" marker-end="url(#ar)"/></g>
{hand(470, 200, -1)}
{''.join(f'<path d="M{{}} 250v0" fill="none"/>'.format(x) for x in (0,))}''', arrow=True)

add('tip off', '手で口もとを隠し、相手の耳もとにそっと知らせる',
    'こっそり知らせる、通報する＝tip off。', f'''
{head(200, 220, 60, 'teal', 'short')}
{head(400, 220, 60, 'coral', 'bob')}
<g transform="translate(270 230)">{hand(0, 0, 1)}</g>
{''.join(f'<path d="M{{}} {{}}q14-12 0-24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(320 + i * 16, 200 + i * 0) for i in range(2))}
<g transform="translate(470 110)">
  <path d="M-50-34h100v58h-30l-14 20-8-20h-48z" fill="#fffefd" class="o"/>
  <path d="M-28-6h56" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/></g>
{line(430, 170, 452, 148, MUTED, True, 3)}''', arrow=True)

# --- 言い換え・程度 ----------------------------------------------------------

add('to put it simply', '入り組んだ図を、たった一本の線に置き換えて言い直す',
    '簡単に言えば＝to put it simply。', f'''
<g transform="translate(160 190)">
  <path d="M-100 90q40-90 0-120t60-20 40 60-60 40 70 40 20-90-60-20" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/></g>
{arc(290, 160, 360, 170, 46, MUTED, True, 5)}
<path d="M400 200h150" fill="none" stroke="{TEA}" stroke-width="14" stroke-linecap="round"/>
{person(150, 350, 0.95, 1, 'teal', 'blue', 'point', 'short', 'smile')}''', arrow=True)

add('to say the least', '「これくらい」と示した幅より、実際の幅はずっと大きい',
    '控えめに言っても＝to say the least。', f'''
<path d="M170 160h100" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M70 120v80M370 120v80" fill="none" stroke="{MUTED}" stroke-width="0"/>
<path d="M70 260h460" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
<g opacity="0.28"><path d="M170 170v80M270 170v80" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/></g>
{head(120, 340, 26, 'teal', 'short')}
<g transform="translate(300 90)"><path d="M-60-34h120v58h-40l-14 20-8-20h-58z" fill="#fffefd" class="o"/>
  <path d="M-30-6h60" fill="none" stroke="{MUTED}" stroke-width="6"/></g>''', arrow=True)

add('to some degree', 'つまみの目盛りが、端まで回さず途中で止めてある',
    'ある程度は＝to some degree。', f'''
<g transform="translate(300 210)">
  <circle r="130" fill="#fffefd" class="o"/>
  <circle r="90" class="tealp o"/>
  {''.join(f'<path d="M0-134v-18" transform="rotate({-120+i*30})" stroke="{MUTED}" stroke-width="5" fill="none"/>' for i in range(9))}
  <path d="M0 0v-84" stroke="{INK}" stroke-width="14" stroke-linecap="round" fill="none" transform="rotate(-30)"/>
  <circle r="16" class="ink"/></g>
<g opacity="0.28"><path d="M300 210L404 106" fill="none" stroke="{MUTED}" stroke-width="0"/></g>
{''.join(f'<path d="M{{}} 360h60" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}''')

add('to some extent', '帯が端までではなく、途中までしか塗られていない',
    'ある程度は＝to some extent。', f'''
<g transform="translate(300 200)">
  <path d="M-240-50h480v100h-480z" fill="#fffefd" class="o"/>
  <path d="M-230-40h250v80h-250z" class="teal"/>
  <path d="M-240-50h480v100h-480z" fill="none" class="o"/></g>
<path d="M20 300h60v0" fill="none" stroke="{MUTED}" stroke-width="0"/>
<path d="M60 290h240" fill="none" stroke="{TEA}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
<g opacity="0.3"><path d="M300 290h240" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/></g>
<path d="M300 120v170" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>''', arrow=True)

# --- しるし・墓・和らげる -----------------------------------------------------

add('token', '本物の貨幣の代わりに使われる、しるしだけの丸い札',
    'しるし、代用貨幣／形ばかりの＝token。', f'''
{table(352)}
{coin(180, 260, 60)}
<g transform="translate(420 260)">
  <circle r="60" class="violetp o"/>
  <circle r="38" fill="none" stroke="{VIO}" stroke-width="5"/>
  <path d="M-18 0l12 16 26-32" fill="none" stroke="{VIO}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>
<g transform="translate(300 260)"><path d="M-24-18h48M-24 18h48" fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} 130h60" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}''')

add('tomb', '草の上に立つ石の墓標の前に、花がそっと供えられている',
    '墓、墓所＝tomb。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<g transform="translate(300 300)">
  <path d="M-90 0v-150a90 90 0 0 1 180 0V0z" fill="{STONE}" class="o"/>
  <path d="M-56-40h112v14h-112zM-56-80h112v14h-112zM-56-120h80v14h-80z" fill="{MUTED}"/>
  <path d="M-110 0h220v26h-220z" fill="#b5bec4" class="o"/></g>
{flower(200, 330, 0.7, 'coral')}{flower(400, 336, 0.6, 'violet')}
{tree(70, 330, 0.8)}''')

add('tone down', 'まぶしい色の面に落ち着いた色を重ね、目に痛くない色に変える',
    '(表現を)和らげる、控えめにする＝tone down。', f'''
{split()}
<rect x="60" y="110" width="180" height="180" rx="10" fill="#e8402b" stroke="{INK}" stroke-width="2.5"/>
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(250 + i * 0, 90 + i * 26) for i in range(2))}
<rect x="360" y="110" width="180" height="180" rx="10" fill="#e0a79c" stroke="{INK}" stroke-width="2.5"/>
{arc(270, 80, 330, 80, 40, MUTED, True, 5)}
{''.join(f'<path d="M{{}} 340h60" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}''', arrow=True)

# --- 扁桃・倒す・リクガメ -----------------------------------------------------

add('tonsil', '大きく開けた口の奥、左右の壁ぎわにふくらみが見える',
    '扁桃腺＝tonsil。', f'''
<g transform="translate(300 200)">
  <ellipse rx="200" ry="140" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <ellipse rx="150" ry="104" fill="#8c3c3a" class="o"/>
  <path d="M-150 40q150-56 300 0 0 64-150 64T-150 40z" class="coral o"/>
  <ellipse cx="0" cy="-90" rx="60" ry="22" fill="#a34a44"/>
  {''.join(f'<ellipse cx="{x}" cy="-10" rx="26" ry="40" class="coralp o"/>' for x in (-88, 88))}
  <path d="M0-40q-16 50 0 76" fill="none" stroke="#a34a44" stroke-width="8"/></g>
{''.join(ring(x, 190, 44, True) for x in (212, 388))}''')

add('topple', '高く積まれた塔がかたむき、そのまま倒れていく',
    '倒れる、倒す／(政権を)転覆させる＝topple。', f'''
{table(352)}
<g opacity="0.28">
  {''.join(f'<rect x="{{}}" y="{{}}" width="80" height="46" rx="6" fill="{MUTED}"/>'.format(110, 296 - i * 52) for i in range(5))}</g>
<g transform="translate(300 300) rotate(62)">
  {''.join(f'<rect x="-40" y="{{}}" width="80" height="46" rx="6" class="teal o"/>'.format(-50 - i * 52) for i in range(5))}</g>
{arc(160, 180, 300, 180, 60, MUTED, True, 5)}
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(480 + i * 20, 250 - i * 16) for i in range(2))}''', arrow=True)

add('tortoise', '厚い甲羅を背負い、短い四本の足でゆっくり歩く',
    'リクガメ＝tortoise。', f'''
<path d="M0 320h600v80H0z" class="ground"/>
<g transform="translate(300 300)">
  <path d="M-140 0q0-100 140-100t140 100z" fill="#8a7a4a" class="o"/>
  <path d="M-140 0q0-100 140-100t140 100" fill="none" stroke="#6b5c34" stroke-width="4"/>
  {''.join(f'<path d="M{-90+i*60} 0q0-70 0-76" fill="none" stroke="#6b5c34" stroke-width="4"/>' for i in range(4))}
  <path d="M-140-10q60-30 280 0v20h-280z" fill="#c8b87f" class="o"/>
  <path d="M140 0q46-6 60-30 14-24-16-34-34-10-44 24" fill="#c8b87f" class="o"/>
  <circle cx="176" cy="-46" r="4" class="ink"/>
  {''.join(f'<path d="M{-90+i*90} 10v30" stroke="#c8b87f" stroke-width="26" fill="none" stroke-linecap="round"/>' for i in range(3))}
  <path d="M-140 0q-30 6-34 26" fill="none" stroke="#c8b87f" stroke-width="16" stroke-linecap="round"/></g>
{''.join(f'<path d="M{{}} 350q20 10 40 0" fill="none" stroke="{GRND}" stroke-width="4"/>'.format(60 + i * 160) for i in range(3))}''')

# --- 軽く触れる・けん引・追跡 ---------------------------------------------------

add('touch on', '話題の面には指の先がほんの少し触れるだけで、深くは入らない',
    '(話題に)軽く触れる＝touch on。', f'''
<g transform="translate(300 300)">
  <path d="M-200-40h400v120h-400z" class="tealp o"/>
  <path d="M-200-40h400" fill="none" stroke="{TEA}" stroke-width="5"/></g>
{hand(300, 200, 1)}
<circle cx="330" cy="258" r="20" fill="none" stroke="{CRL}" stroke-width="4"/>
{''.join(f'<path d="M{{}} 300v50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>'.format(140 + i * 320) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}q12-12 0-24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(400 + i * 18, 210 - i * 12) for i in range(2))}''')

add('tow', '動かなくなった車を、太いロープでつないで前の車が引く',
    'けん引する、レッカー移動する＝tow。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(150 320)">
  <path d="M-80 0v-40l30-26h100l30 26V0z" class="teal o"/>
  <circle cx="-46" cy="6" r="18" class="ink"/><circle cx="46" cy="6" r="18" class="ink"/></g>
<path d="M232 310q34 20 68 0" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>
<g transform="translate(410 320)">
  <path d="M-80 0v-40l30-26h100l30 26V0z" class="coralp o"/>
  <circle cx="-46" cy="6" r="18" class="ink"/><circle cx="46" cy="6" r="18" class="ink"/></g>
{arc(200, 220, 80, 220, 46, MUTED, True, 5)}
{cross(500, 200, 0.5)}''', arrow=True)

add('track down', '残された足あとを一つずつたどり、隠れていた相手を見つけ出す',
    '追跡して見つけ出す＝track down。', f'''
<path d="M0 300h600v100H0z" class="ground"/>
{''.join(f'<g transform="translate({{}} {{}}) rotate(-12)"><ellipse rx="13" ry="20" class="ink"/><ellipse cy="-22" rx="9" ry="7" class="ink"/></g>'.format(70 + i * 62, 340 - (i % 2) * 26) for i in range(6))}
{person(120, 290, 0.9, 1, 'teal', 'blue', 'think', 'short', 'flat')}
<g transform="translate(470 300)">
  <path d="M-70 0v-120h140V0z" fill="#e8ddc9" class="o"/>
  <path d="M-40-90h40v60h-40z" class="tealp o"/></g>
{head(500, 260, 24, 'coral', 'bob')}
<g transform="translate(250 180)">
  <circle r="44" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M32 32l40 40" stroke="{BRN}" stroke-width="14" stroke-linecap="round" fill="none"/></g>''')

# --- 腫瘍・乱気流・混乱 -------------------------------------------------------

add('tumour', '体の中に、本来ないはずの丸いかたまりができている',
    '腫瘍(しゅよう)＝tumour。', f'''
{body(290, 180, 0.66)}
<circle cx="308" cy="190" r="30" class="coralp o"/>
<circle cx="308" cy="190" r="30" fill="none" stroke="{CRL}" stroke-width="4"/>
{ring(308, 190, 58, True)}
<g transform="translate(480 120)">
  <circle r="46" class="coralp o"/><circle r="46" fill="none" stroke="{CRL}" stroke-width="4"/></g>
{line(430, 150, 360, 178, MUTED, True, 3)}''', arrow=True)

add('turbulence', '乱れた気流に入り、飛行機が上下に大きく揺さぶられる',
    '乱気流、動乱＝turbulence。', f'''
{''.join(cloud(90 + i * 200, 90 + (i % 2) * 40, 1.1, 'violet') for i in range(3))}
<g transform="translate(300 240) rotate(-16)">{plane(0, 0, 0.85, 0, 'teal')}</g>
<g opacity="0.28" transform="translate(300 240) rotate(18)">{plane(0, 0, 0.85, 0, 'teal')}</g>
{''.join(f'<path d="M{{}} {{}}q30-30 60 0t60 0" fill="none" stroke="{MUTED}" stroke-width="5"/>'.format(80, 300 + i * 40) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}q30 30 60 0t60 0" fill="none" stroke="{MUTED}" stroke-width="5"/>'.format(340, 300 + i * 40) for i in range(2))}''')

add('turmoil', '人も物も入り乱れ、どこも落ち着かずに渦を巻く',
    '混乱、動揺＝turmoil。', f'''
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-30" y="-22" width="60" height="44" rx="6" class="{{}} o"/></g>'.format(x, y, r, c) for x, y, r, c in [
  (110, 120, 24, 'coral'), (480, 110, -30, 'gold'), (120, 320, -18, 'green'), (490, 330, 34, 'violet'), (300, 70, 12, 'blue')])}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})">{{}}</g>'.format(x, y, r, person(0, 0, 0.8, f, c, 'blue', 'up', h, 'sad')) for x, y, r, f, c, h in [
  (240, 340, -14, 1, 'teal', 'short'), (380, 330, 18, -1, 'coral', 'bob')])}
<g transform="translate(300 210)"><path d="M-130 0a130 70 0 1 0 60-58" fill="none" stroke="{MUTED}" stroke-width="7" stroke-dasharray="14 12" marker-end="url(#ar)"/></g>''', arrow=True)

# --- 見て見ぬふり・頼る -------------------------------------------------------

add('turn a blind eye to', '目の前で起きていることに、手で目を覆って見ないふりをする',
    '〜を見て見ぬふりをする＝turn a blind eye to。', f'''
{person(170, 350, 1.3, 1, 'teal', 'blue', 'think', 'short', 'flat')}
{hand(210, 210, 1)}
<g transform="translate(430 210)">
  <path d="M-90-90h180v180h-180z" fill="#eaf1f6" class="o"/>
  <path d="M-90-90l84 80-64 54 74 66M90-90l-88 86 84 54-42 60" fill="none" stroke="{INK}" stroke-width="3"/></g>
{''.join(f'<path d="M{{}} {{}}l-26 16" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>'.format(330, 180 + i * 60) for i in range(2))}
{cross(300, 120, 0.5)}''')

add('turn to', '困りはてた人が、そばにいる相手のほうへ向き直って助けを求める',
    '(助けを求めて)頼る＝turn to。', f'''
{person(200, 350, 1.25, 1, 'teal', 'blue', 'reach', 'short', 'sad')}
{person(440, 350, 1.2, -1, 'coral', 'green', 'give', 'bob', 'smile')}
{arc(260, 200, 380, 200, 50, MUTED, True, 5)}
<g transform="translate(320 120)">
  <path d="M-24-40q0-30 26-30t26 30q0 20-26 30v16" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="2" cy="34" r="7" fill="{MUTED}"/></g>''', arrow=True)

# --- 道具・薄明かり・潰瘍 -----------------------------------------------------

add('tweezers', '細い先のピンセットで、皮膚に刺さった小さなとげをつまみ出す',
    'ピンセット、毛抜き＝tweezers。', f'''
<g transform="translate(280 300)">
  <path d="M-200 40q60-90 200-90t200 90z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>
<g transform="translate(300 180) rotate(14)">
  <path d="M-16-120q-10 120 4 140M16-120q10 120-4 140" fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-16-120h32v-14h-32z" fill="{MUTED}" class="o"/></g>
<g transform="translate(308 330) rotate(14)"><path d="M-4-30h8v34h-8z" fill="#6b5a4a"/></g>
{ring(308, 320, 46, True)}''')

add('twilight', '日が沈んだあと、空にはまだうっすらと明かりが残っている',
    '薄明かり、たそがれ＝twilight。', f'''
<path d="M0 0h600v300H0z" fill="#4a5570"/>
<path d="M0 180h600v120H0z" fill="#8a7d8f"/>
<path d="M0 250h600v50H0z" fill="#d79a6a"/>
<path d="M0 300h600v100H0z" fill="#2f3a4d"/>
<g transform="translate(300 300)"><path d="M-90 0a90 90 0 0 1 180 0z" fill="#f0b26a" class="o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#fff6d8"/>'.format(60 + (i * 71) % 480, 40 + (i * 37) % 100) for i in range(9))}
<g opacity="0.9"><path d="M60 300q40-70 80 0zM480 300q50-90 100 0z" fill="#232b3b"/></g>''')

add('ulcer', '胃の内側の壁に、赤くえぐれた傷ができている',
    '潰瘍(かいよう)＝ulcer。', f'''
<g transform="translate(300 210)">
  <path d="M-40-130q-90 34-80 120 10 86 100 90 88 4 96-86 8-80-66-124z" class="coralp o"/>
  <path d="M-40-130v-50" stroke="{CRLD}" stroke-width="24" fill="none" stroke-linecap="round"/>
  <path d="M80 70q16 54-30 74-50 22-80-16" fill="none" stroke="{CRLD}" stroke-width="22" stroke-linecap="round"/>
  <path d="M-6-6q-26 14-16 42 12 30 44 18 28-12 16-42-12-26-44-18z" fill="#b5352b" class="o"/></g>
{ring(294, 234, 62, True)}
{''.join(f'<path d="M{{}} {{}}l16-18" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(430 + i * 20, 190 - i * 14) for i in range(2))}''')

# --- 審判・全員一致・無条件 -----------------------------------------------------

add('umpire', '高い椅子に座った審判が、腕を上げて判定を示す',
    '審判＝umpire。', f'''
<path d="M0 320h600v80H0z" class="greenp"/>
<path d="M60 300h480" fill="none" stroke="{MUTED}" stroke-width="6"/>
<g transform="translate(300 320)">
  <path d="M-50 0v-140h100V0z" fill="none" stroke="{BRN}" stroke-width="10"/>
  <path d="M-56-140h112v20h-112z" fill="{BRN}" class="o"/></g>
{sit(300, 180, 1.0, 1, 'violet', 'blue', 'cap', 'flat', 'up')}
{person(110, 350, 0.85, 1, 'teal', 'blue', 'stand', 'short', 'flat')}
{person(500, 350, 0.85, -1, 'coral', 'green', 'stand', 'bob', 'flat')}
{''.join(f'<path d="M{{}} {{}}q12-12 0-24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(390 + i * 18, 130 + i * 0) for i in range(2))}''')

add('unanimously', '会場の全員の手がひとつ残らず挙がり、反対はひとつもない',
    '全員一致で＝unanimously。', f'''
{''.join(person(80 + i * 90, 350, 1.0, 1, c, 'blue', 'up', h, 'smile') for i, (c, h) in enumerate([('teal', 'short'), ('coral', 'bob'), ('green', 'bun'), ('blue', 'cap'), ('violet', 'short'), ('gold', 'bob')]))}
{tick(300, 90, 1.0)}''')

add('unconditional', '条件の札はひとつも付かず、そのまま相手に手渡される',
    '無条件の＝unconditional。', f'''
{person(140, 350, 1.2, 1, 'teal', 'blue', 'give', 'short', 'smile')}
<g transform="translate(300 210)"><rect x="-60" y="-46" width="120" height="92" rx="10" class="gold o"/>
  <path d="M-60-10h120M0-46v92" fill="none" stroke="{GLDD}" stroke-width="6"/></g>
{person(470, 350, 1.2, -1, 'coral', 'green', 'reach', 'bob', 'smile')}
<g opacity="0.3" transform="translate(300 340)">
  <path d="M-70-30h140v60h-140z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/></g>
{cross(300, 340, 0.55)}''')

add('undeniably', 'はっきり写った証拠が目の前にあり、もう否定のしようがない',
    '否定しようもなく、確かに＝undeniably。', f'''
<g transform="translate(330 200)">
  <path d="M-150-130h300v260h-300z" class="paper"/>
  <path d="M-120-100h240v180h-240z" class="tealp o"/>
  {person(0, 60, 0.62, 1, 'coral', 'blue', 'point', 'short', 'flat')}</g>
{person(110, 350, 1.0, 1, 'teal', 'green', 'up', 'bun', 'flat')}
{tick(500, 330, 0.8)}
{''.join(spark(120 + i * 40, 120 + (i % 2) * 30, 0.6, 'gold') for i in range(2))}''')

finish(__file__)
