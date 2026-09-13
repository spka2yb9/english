# -*- coding: utf-8 -*-
"""第179回。un-/up-/ur-/us-/ut-/v- の語。talon / tendon / thump の描き直しも含む。"""
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

def flag(x, y, s=1, cls='violet', pole=110):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0v-{pole}" stroke="{BRN}" stroke-width="8" stroke-linecap="round" fill="none"/>'
            f'<path d="M5-{pole}h100l-24 30 24 30H5z" class="{cls} o"/></g>')

# --- 第178回の描き直し -------------------------------------------------------

add('talon', '猛禽の太い足の先から、鋭く曲がったかぎづめが枝をつかむ',
    '(猛禽の)かぎづめ＝talon。', f'''
<g transform="translate(300 330)"><path d="M-240-24h480v48h-480z" fill="{BRN}" class="o"/></g>
<g transform="translate(300 150)">
  <path d="M-40 0q40-30 80 0 10 60-40 90-50-30-40-90z" fill="#c8a05f" class="o"/>
  <path d="M0-40v-70" stroke="#a0764a" stroke-width="40" fill="none" stroke-linecap="round"/>
  <path d="M-38 70q-46 24-50 90 34-8 58-46" fill="#c8a05f" stroke="{INK}" stroke-width="3.5"/>
  <path d="M38 70q46 24 50 90-34-8-58-46" fill="#c8a05f" stroke="{INK}" stroke-width="3.5"/>
  <path d="M0 90q-6 50 0 90 20-24 22-70" fill="#c8a05f" stroke="{INK}" stroke-width="3.5"/>
  <path d="M-88 160q-30 20-24 44 24-4 36-26M88 160q30 20 24 44-24-4-36-26" fill="#5b5348" stroke="{INK}" stroke-width="3"/>
  <path d="M22 180q10 32 0 44-16-8-18-30" fill="#5b5348" stroke="{INK}" stroke-width="3"/></g>''')

add('tendon', 'ふくらはぎの筋肉とかかとの骨を、丈夫なひもがつないでいる',
    '腱(けん)＝tendon。', f'''
<g transform="translate(300 200)">
  <path d="M-70-160q70-30 140 0 30 90 0 150-70 26-140 0-30-60 0-150z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40-10q40 20 80 0 10 100 0 130l70 40v30h-180v-40l30-30z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M10 0q16 90 0 126" fill="none" stroke="#eadbbc" stroke-width="30" stroke-linecap="round"/>
  <path d="M10 0q16 90 0 126" fill="none" stroke="#c3ad85" stroke-width="4"/>
  <path d="M-40-120q40 40 80 0" fill="none" stroke="{SKINL}" stroke-width="4"/></g>
{ring(312, 260, 66, True)}''')

add('thump', 'にぎりこぶしで机をドンとたたき、上の紙が跳ね上がる',
    'ドンと打つ／ドンという音＝thump。', f'''
{table(300)}
<g transform="translate(270 240)">
  <path d="M-56-70h112v40h-112z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-62-30h124v56a26 26 0 0 1-26 26h-72a26 26 0 0 1-26-26z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  {''.join(f'<path d="M{-36+i*24} -30v34" stroke="{SKINL}" stroke-width="3" fill="none"/>' for i in range(4))}
  <path d="M-10-70v-40h30v40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>
{''.join(f'<path d="M{int(270+110*math.cos(math.radians(a)))} {int(300+34*math.sin(math.radians(a)))}l{int(38*math.cos(math.radians(a)))} {int(16*math.sin(math.radians(a)))}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for a in (-160, -200, 20, -20))}
<g transform="translate(470 220) rotate(18)">{doc(0, 0, 80, 54, 2)}</g>
{''.join(f'<path d="M{440+i*30} 186v-24" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

# --- 異論なし・統一・均一 -----------------------------------------------------

add('undisputed', '一位の台に立つ人に、だれひとり異を唱える手が挙がらない',
    '誰も異論のない＝undisputed。', f'''
<g transform="translate(300 330)">
  <path d="M-50 0v-120h100V0z" fill="{STONE}" class="o"/>
  <path d="M-160 0v-60h110v60zM50 0v-80h110v80z" fill="#b5bec4" class="o"/></g>
{person(300, 210, 1.0, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{''.join(head(105 + i * 0, 300, 26, 'teal', 'short') for i in range(1))}
{head(475, 290, 26, 'green', 'bob')}
{''.join(f'<g opacity="0.28"><path d="M{{}} 240v-40" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="9 8"/></g>'.format(x) for x in (105, 475))}
{''.join(cross(x, 170, 0.4) for x in (105, 475))}
{tick(300, 90, 0.8)}''')

add('unification', '分かれていた二つの地域が、線を消して一つにまとまる',
    '統一＝unification。', f'''
{split()}
<g transform="translate(150 220)">
  <path d="M-110 80q-10-110 50-130 60-20 80 40t-20 90z" class="tealp o"/>
  <path d="M20 80q40-40 40-90t-40-40" fill="{CRLP}" stroke="{INK}" stroke-width="2.5"/>
  <path d="M20-50v130" fill="none" stroke="{INK}" stroke-width="6"/></g>
<g transform="translate(450 220)">
  <path d="M-110 80q-10-110 50-130 60-20 80 40t-20 90z" class="tealp o"/></g>
{arc(280, 160, 340, 160, 44, MUTED, True, 5)}
{tick(450, 350, 0.6)}''', arrow=True)

add('uniformity', '同じ形と同じ大きさの品が、ずれなくきれいに並んでいる',
    '均一性、一様であること＝uniformity。', f'''
{''.join(f'<rect x="{{}}" y="{{}}" width="90" height="70" rx="8" class="teal o"/>'.format(70 + (i % 5) * 100, 120 + (i // 5) * 110) for i in range(10))}
{''.join(f'<path d="M{{}} 100v-28" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(115 + i * 100) for i in range(5))}
<path d="M115 68h400" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>''')

add('uniformly', '広い面のどこを取っても、同じ濃さで色が塗られている',
    '一様に、均一に＝uniformly。', f'''
<g transform="translate(300 200)">
  <path d="M-240-140h480v280h-480z" fill="#238b83" stroke="{INK}" stroke-width="2.5"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="26" fill="none" stroke="#fffefd" stroke-width="3" stroke-dasharray="8 8"/>'.format(x, y) for x, y in [(120, 110), (300, 200), (480, 300), (480, 110), (120, 300)])}
{''.join(tick(x, y, 0.32) for x, y in [(120, 110), (300, 200), (480, 300)])}''')

# --- 違法・不必要・資格なし -----------------------------------------------------

add('unlawful', '法の枠の内側ではなく、外へはみ出した行いに×がつく',
    '違法の＝unlawful。', f'''
<g transform="translate(260 200)">
  <path d="M-160-130h320v260h-320z" fill="none" stroke="{TEA}" stroke-width="7"/>
  {''.join(f'<circle cx="{{}}" cy="{{}}" r="24" class="tealp o"/>'.format(-90 + (i % 3) * 90, -60 + (i // 3) * 90) for i in range(6))}</g>
<circle cx="520" cy="290" r="30" class="coral o"/>
{cross(520, 290, 0.6)}
{''.join(f'<path d="M{{}} 250h60" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}''')

add('unnecessarily', '小さな品が、必要のない包みで何重にもくるまれている',
    '不必要に、むだに＝unnecessarily。', f'''
{table(352)}
{''.join(f'<g transform="translate(300 250)"><rect x="{{}}" y="{{}}" width="{{}}" height="{{}}" rx="10" class="{{}} o"/></g>'.format(-(150 - i * 30), -(120 - i * 26), (150 - i * 30) * 2, (120 - i * 26) * 2, c) for i, c in enumerate(['goldp', 'coralp', 'tealp', 'violetp']))}
<g transform="translate(300 250)"><rect x="-24" y="-20" width="48" height="40" rx="6" class="teal o"/></g>
{cross(500, 120, 0.7)}''')

add('unqualified', '資格の証を持たない人が、その席に座ろうとして止められる',
    '資格のない／無条件の＝unqualified。', f'''
{table(300)}
{chair(420, 300, 1.0, 'gold', -1)}
{person(180, 350, 1.2, 1, 'teal', 'blue', 'reach', 'short', 'flat')}
<g opacity="0.3" transform="translate(280 210)">
  <path d="M-60-44h120v88h-120z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
  <circle cy="0" r="22" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/></g>
{cross(280, 210, 0.7)}
{hand(400, 190, -1)}''')

add('unreasonable', 'ひとりでは到底運べない量の荷を、平気で背負わせようとする',
    '理不尽な、法外な＝unreasonable。', f'''
{''.join(box(300, 250 - i * 62, 180 - i * 24, 54, 18, 'gold') for i in range(4))}
{person(300, 350, 1.1, 1, 'teal', 'blue', 'up', 'short', 'sad')}
{''.join(f'<path d="M{{}} {{}}q14 12 0 24" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(190 + i * 16, 300 - i * 14) for i in range(2))}
{cross(500, 130, 0.7)}''')

# --- 不安・気づかず・宙に浮く ---------------------------------------------------

add('unrest', '通りに人が散らばり、倒れた柵と割れた物が落ち着かない様子を示す',
    '(社会の)不安、騒乱＝unrest。', f'''
<path d="M0 320h600v80H0z" class="ground"/>
{''.join(f'<g transform="translate({{}} 350) rotate({{}})">{{}}</g>'.format(x, r, person(0, 0, 0.9, f, c, 'blue', 'up', h, 'sad')) for x, r, f, c, h in [
  (110, -6, 1, 'teal', 'short'), (250, 8, -1, 'coral', 'bob'), (400, -10, 1, 'green', 'bun'), (520, 6, -1, 'violet', 'cap')])}
<g transform="translate(320 330) rotate(74)">
  <path d="M-90-10h180v20h-180z" fill="{BRN}" class="o"/>
  {''.join(f'<path d="M{-70+i*46} -40v80" stroke="{BRN}" stroke-width="10" fill="none"/>' for i in range(4))}</g>
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M-20-14h40v28h-40z" fill="{STONE}" stroke="{INK}" stroke-width="2.5"/></g>'.format(x, y, r) for x, y, r in [(180, 360, 24), (460, 366, -30)])}
{''.join(cloud(120 + i * 340, 90, 1.1, 'violet') for i in range(2))}''')

add('unwittingly', '本人は気づかないまま、歩きながら持ち物を落としていく',
    '知らないうちに、うっかり＝unwittingly。', f'''
{person(430, 350, 1.25, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><rect x="-22" y="-16" width="44" height="32" rx="5" class="goldp o"/></g>'.format(90 + i * 90, 340 - (i % 2) * 16, -20 + i * 18) for i in range(3))}
<g transform="translate(350 240) rotate(28)"><rect x="-22" y="-16" width="44" height="32" rx="5" class="goldp o"/></g>
{''.join(f'<path d="M{{}} {{}}q-30 40-60 60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>'.format(360, 200) for _ in range(1))}
{cross(140, 160, 0.5)}''')

add('up in the air', '決まらないままの予定表が、地に着かず宙に浮いている',
    '未定で、宙に浮いて＝up in the air。', f'''
{''.join(cloud(120 + i * 340, 90, 1.0, 'blue') for i in range(2))}
<g transform="translate(300 170) rotate(-8)">
  <path d="M-110-80h220v160h-220z" class="paper"/>
  {''.join(f'<rect x="-84" y="{-50+i*34}" width="{170-(i%2)*50}" height="12" rx="6" fill="{MUTED}"/>' for i in range(3))}
  <g transform="translate(60 46)"><path d="M-16-22q0-18 16-18t16 18q0 12-16 18v8" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>
    <circle cy="20" r="5" fill="{CRL}"/></g></g>
<path d="M60 340h480" fill="none" stroke="{BRN}" stroke-width="8"/>
{''.join(f'<path d="M{{}} 280v40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>'.format(220 + i * 160) for i in range(2))}''')

add('up to a point', '坂の途中に「ここまで」の旗が立ち、その先へは進まない',
    'ある程度までは＝up to a point。', f'''
<path d="M40 350L540 120v230H40z" fill="#d8cdb6" class="o"/>
{flag(300, 235, 0.5, 'coral', 110)}
{person(230, 270, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
<g opacity="0.28"><path d="M320 230L520 140" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="11 10"/></g>
{arc(110, 300, 220, 250, 50, MUTED, True, 5)}
{cross(500, 100, 0.5)}''', arrow=True)

# --- 育ち・激変・大騒ぎ -------------------------------------------------------

add('upbringing', '家の中で、親が子に手を添えながら少しずつ教えていく',
    '育て方、育ち＝upbringing。', f'''
<g transform="translate(300 200)">
  <path d="M-230-140h460v280h-460z" fill="#f6efe1" class="o"/></g>
{person(230, 340, 1.2, 1, 'coral', 'blue', 'give', 'bun', 'smile')}
{person(390, 340, 0.72, -1, 'teal', 'green', 'reach', 'short', 'smile')}
<g transform="translate(320 250)"><path d="M-40-30h80v60h-80z" class="goldp o"/>
  {''.join(f'<rect x="-28" y="{-18+i*18}" width="{56-(i%2)*20}" height="8" rx="4" fill="{GLDD}"/>' for i in range(2))}</g>
{''.join(spark(120 + i * 360, 120, 0.6, 'gold') for i in range(2))}''')

add('upheaval', '地面が大きく持ち上がり、その上のものがすべてひっくり返る',
    '大変動、激変＝upheaval。', f'''
<path d="M0 360h180l120-170 120 170h180v40H0z" fill="#cbb896" class="o"/>
<g opacity="0.24"><path d="M0 330h600" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/></g>
<g transform="translate(140 340) rotate(-34)">{house(0, 0, 0.55, 'coral')}</g>
<g transform="translate(470 344) rotate(40)">{tree(0, 0, 0.9)}</g>
{''.join(f'<path d="M{{}} 240v-60" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round" marker-end="url(#ar)"/>'.format(240 + i * 60) for i in range(3))}''', arrow=True)

add('uproar', '大勢がいっせいに声を上げ、その場が騒然となる',
    '大騒ぎ、騒然＝uproar。', f'''
{''.join(f'<g transform="translate({{}} {{}})"><circle r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/><path d="{HAIRS["short"]}" transform="translate(0 180) scale(1.67)" fill="{HAIR}"/><path d="M-16-6l10 6M16-6l-10 6" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/><ellipse cy="20" rx="13" ry="17" class="ink"/></g>'.format(80 + (i % 4) * 148, 130 + (i // 4) * 150) for i in range(8))}
{''.join(f'<path d="M{{}} {{}}q14 14 0 28" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(128 + (i % 4) * 148, 100 + (i // 4) * 150) for i in range(8))}''')

# --- 都市化・緊急・幕開け -----------------------------------------------------

add('urbanisation', '田畑の広がっていた土地が、建物の並ぶ街に変わる',
    '都市化＝urbanisation。', f'''
{split()}
<path d="M20 300h250v60H20z" class="greenp o"/>
{''.join(flower(60 + i * 48, 320, 0.45, 'green') for i in range(5))}
{house(160, 300, 0.42, 'coral')}
{''.join(tower(360 + i * 90, 340, 0.62, 'teal', 4 + i) for i in range(3))}
<path d="M320 340h260v20H320z" fill="{STONE}"/>
{arc(280, 180, 340, 190, 40, MUTED, True, 5)}''', arrow=True)

add('urgently', '赤いランプが回り、いますぐ動かなければならないと知らせる',
    '緊急に、至急＝urgently。', f'''
<g transform="translate(300 200)">
  <path d="M-60 60h120v20h-120z" fill="{MUTED}" class="o"/>
  <path d="M-50 60q0-90 50-90t50 90z" class="coral o"/>
  <path d="M-50 20q50-24 100 0" fill="none" stroke="{CRLD}" stroke-width="4"/></g>
{''.join(f'<path d="M{int(300+130*math.cos(math.radians(a)))} {int(220+130*math.sin(math.radians(a)))}l{int(40*math.cos(math.radians(a)))} {int(40*math.sin(math.radians(a)))}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for a in (-160, -130, -100, -80, -50, -20))}
{clock(120, 320, 40, 11, 55)}
{person(500, 350, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'flat')}''')

add('usher in', '扉を大きく開け放ち、新しい時代を中へ迎え入れる',
    '(新しい時代を)もたらす、幕開けとなる＝usher in。', f'''
<g transform="translate(300 380)">
  <path d="M-120-320h240v320h-240z" fill="#e8ddc9" class="o"/>
  <path d="M-96-300h100v300h-100z" class="teal o"/>
  <path d="M96-300L4-266v266l92 34z" class="tealp o"/></g>
{sun(300, 130, 46)}
{''.join(f'<path d="M300 180L{{}} 300" fill="none" stroke="{GLD}" stroke-width="5" stroke-dasharray="10 9"/>'.format(220 + i * 80) for i in range(3))}
{person(110, 350, 1.05, 1, 'coral', 'blue', 'give', 'short', 'smile')}
{arc(170, 230, 250, 240, 50, MUTED, True, 4)}''', arrow=True)

# --- 活用・最大限・ワクチン -----------------------------------------------------

add('utilisation', '置きっぱなしだった道具が、いまはどれも使われている',
    '活用、利用率＝utilisation。', f'''
{split()}
{table(352)}
{''.join(f'<g opacity="0.32" transform="translate({{}} 290)"><path d="M-10-50h20v50h-20z" fill="{MUTED}"/><path d="M-28 0h56v-14h-56z" fill="{MUTED}"/></g>'.format(80 + i * 60) for i in range(4))}
{cross(150, 130, 0.6)}
{''.join(f'<g transform="translate({{}} 300)">{{}}</g>'.format(370 + i * 80, person(0, 0, 0.72, 1, c, 'blue', 'hold', 'short', 'smile')) for i, c in enumerate(['teal', 'coral', 'green']))}
{''.join(f'<g transform="translate({{}} 250) rotate(-16)"><path d="M-7-40h14v60h-14z" fill="{BRN}" class="o"/><path d="M-20 20h40v16h-40z" fill="{MUTED}" class="o"/></g>'.format(400 + i * 80) for i in range(3))}
{tick(450, 130, 0.6)}''')

add('utmost', '出せる力の目盛りをいっぱいまで振り切って、全力で踏ん張る',
    '最大限の、最大限＝utmost。', f'''
{gauge(400, 300, 150, 1.0, 'coral')}
{person(140, 350, 1.35, -1, 'teal', 'blue', 'reach', 'short', 'flat')}
{''.join(f'<path d="M{{}} {{}}l16-20" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(80 + i * 20, 170 - i * 14) for i in range(2))}
<path d="M60 350h150" fill="none" stroke="{BRN}" stroke-width="8"/>''')

add('vaccine', '小びんから吸い上げた薬が、注射器に満たされる',
    'ワクチン＝vaccine。', f'''
{table(352)}
<g transform="translate(170 280)">
  <path d="M-40-70h80v20h-80z" class="tealp o"/>
  <path d="M-34-50h68v90a16 16 0 0 1-16 16h-36a16 16 0 0 1-16-16z" fill="#fffefd" class="o"/>
  <path d="M-34 0h68v40a16 16 0 0 1-16 16h-36a16 16 0 0 1-16-16z" class="tealp"/></g>
<g transform="translate(400 230) rotate(-22)">
  <path d="M-110-24h180v48h-180z" fill="#fffefd" class="o"/>
  <path d="M-100-16h120v32h-120z" class="tealp"/>
  <path d="M70-10h50v20H70z" fill="{MUTED}" class="o"/>
  <path d="M120 0h60" stroke="{MUTED}" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path d="M-110-34h20v68h-20z" fill="{MUTED}" class="o"/></g>
{''.join(drop(240 + i * 16, 200 + i * 14, 0.9, 'teal') for i in range(2))}''')

# --- あいまい・確認 ----------------------------------------------------------

add('vagueness', '形の輪郭そのものがぼやけて、どこまでが境目か分からない',
    'あいまいさ＝vagueness。', f'''
{''.join(f'<g opacity="{0.1+i*0.07:.2f}"><circle cx="300" cy="200" r="{140-i*12}" class="teal"/></g>' for i in range(9))}
{''.join(f'<g transform="translate({{}} 340)"><path d="M-16-26q0-20 18-20t18 20q0 14-18 20v10" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/><circle cy="24" r="5" fill="{MUTED}"/></g>'.format(160 + i * 140) for i in range(2))}''')

add('validate', '出された券を控えと突き合わせ、一致したので有効の印を押す',
    '正当性を確かめる、有効にする＝validate。', f'''
{table(352)}
{''.join(f'<g transform="translate({{}} 230)"><path d="M-80-50h160v100h-160z" class="paper"/><rect x="-56" y="-24" width="112" height="14" rx="7" fill="{MUTED}"/><rect x="-56" y="4" width="80" height="14" rx="7" fill="{MUTED}"/></g>'.format(x) for x in (150, 340))}
<g transform="translate(245 230)"><path d="M-20-16h40M-20 16h40" fill="none" stroke="{GRN}" stroke-width="7" stroke-linecap="round"/></g>
<g transform="translate(470 150)">
  <path d="M-44 40h88v26h-88z" class="ink"/><path d="M-18 40v-44h36v44z" fill="{BRN}" class="o"/>
  <path d="M-30-4h60v-22h-60z" fill="{BRN}" class="o"/></g>
{tick(470, 290, 0.7)}''')

add('validation', '検査を通ったしるしとして、確かな印が押されている',
    '検証、承認／認めてもらうこと＝validation。', f'''
{doc(300, 200, 240, 280, 4)}
<g transform="translate(300 250)">
  <circle r="64" class="greenp o"/>
  <circle r="44" fill="none" stroke="{GRN}" stroke-width="5"/>
  <path d="M-22 0l14 20 32-38" fill="none" stroke="{GRN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></g>
{''.join(spark(120 + i * 360, 130, 0.7, 'gold') for i in range(2))}''')

add('valuation', '品物を天秤にかけ、いくらの値がつくかを見立てる',
    '評価額、査定＝valuation。', f'''
{scales(300, 320, 6, 1.0)}
<g transform="translate(180 190)"><path d="M-40-28h80v56h-80z" class="gold o"/></g>
{''.join(coin(392 + i * 28, 210, 16) for i in range(3))}
{person(500, 350, 0.9, -1, 'teal', 'blue', 'think', 'bun', 'smile')}''')

add('vantage', '高い岩の上に立つと、下の景色がひと目で見渡せる',
    '有利な位置、見晴らしのきく地点＝vantage。', f'''
<path d="M0 330h600v70H0z" class="greenp"/>
<path d="M60 330q40-160 130-160t120 160z" fill="#cbb896" class="o"/>
{person(190, 170, 1.0, 1, 'teal', 'blue', 'point', 'cap', 'smile')}
{''.join(f'<path d="M240 130L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"/>'.format(560, 120 + i * 90) for i in range(3))}
{''.join(house(400 + i * 90, 340, 0.34, 'coral') for i in range(2))}
{tree(540, 336, 0.7)}''')

# --- はるかに・菜食・速度 -----------------------------------------------------

add('vastly', '並べて比べると、片方がもう片方より桁違いに大きい',
    '大幅に、はるかに＝vastly。', f'''
<circle cx="420" cy="220" r="150" class="teal o"/>
<circle cx="110" cy="330" r="26" class="tealp o"/>
<path d="M110 290h-60M420 60h-60" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>
<path d="M64 70v220" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>''', arrow=True)

add('vegetarianism', '皿に野菜だけが盛られ、肉の料理には×がついている',
    '菜食主義＝vegetarianism。', f'''
{table(330)}
<g transform="translate(200 300)">
  <ellipse rx="120" ry="30" fill="#fffefd" class="o"/>
  {''.join(f'<ellipse cx="{{}}" cy="{{}}" rx="26" ry="16" class="green o"/>'.format(-60 + i * 40, -14 + (i % 2) * 12) for i in range(4))}
  <circle cx="40" cy="-6" r="18" class="coral o"/></g>
<g opacity="0.32" transform="translate(460 300)">
  <ellipse rx="90" ry="24" fill="#fffefd" class="o"/>
  <path d="M-50-26q50-24 100 0 6 30-50 30t-50-30z" fill="#b5744a" class="o"/></g>
{cross(460, 210, 0.7)}
{tick(200, 160, 0.6)}''')

add('velocity', '進む向きまで示す矢印が、速さの分だけ長く伸びる',
    '速度(向きを含む)＝velocity。', f'''
<g transform="translate(150 250)"><circle r="40" class="teal o"/></g>
<path d="M195 250h300" fill="none" stroke="{CRL}" stroke-width="12" stroke-linecap="round" marker-end="url(#ar)"/>
<g opacity="0.3"><circle cx="150" cy="120" r="30" class="teal"/></g>
<path d="M188 120h130" fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round" marker-end="url(#ar)"/>
{''.join(f'<path d="M{{}} {{}}h50" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(70, 220 + i * 60) for i in range(2))}''', arrow=True)

add('velvet', '毛足のある厚い布が、光の当たり方でつやを変えて垂れる',
    'ビロード、ベルベット＝velvet。', f'''
<g transform="translate(300 200)">
  <path d="M-220-140h440v280h-440z" fill="#6b3f8a"/>
  {''.join(f'<path d="M{-220+i*44} -140q22 140 0 280" fill="none" stroke="#8a58ab" stroke-width="{16-(i%3)*5}"/>' for i in range(11))}
  {''.join(f'<path d="M{-200+i*88} -140q20 140 0 280" fill="none" stroke="#5a3175" stroke-width="10"/>' for i in range(6))}
  <path d="M-220-140h440v280h-440z" fill="none" class="o"/></g>
{hand(500, 320, -1)}''')

# --- 売り手・復讐・照合 -------------------------------------------------------

add('vendor', '屋台に品を並べ、通りかかった客に売る人',
    '売り手、販売業者＝vendor。', f'''
<g transform="translate(300 320)">
  <path d="M-140 0v-90h280V0z" fill="#fffefd" class="o"/>
  <path d="M-156-90h312l-20-44h-272z" class="coral o"/>
  {''.join(f'<rect x="{-110+i*72}" y="-66" width="56" height="40" rx="6" class="goldp o"/>' for i in range(3))}</g>
{person(300, 320, 0.82, 1, 'teal', 'blue', 'reach', 'bun', 'smile')}
{person(490, 350, 1.05, -1, 'violet', 'green', 'reach', 'short', 'smile')}
{''.join(coin(420, 210 + i * 40, 17) for i in range(2))}''')

add('vengeance', '受けた一撃を、そっくりそのまま相手に返す',
    '復讐＝vengeance。', f'''
{person(140, 350, 1.2, 1, 'coral', 'blue', 'point', 'short', 'sad')}
{person(460, 350, 1.2, -1, 'teal', 'green', 'point', 'bob', 'sad')}
<g opacity="0.3"><path d="M210 150h180" fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round" marker-end="url(#ar)"/></g>
<path d="M390 250H210" fill="none" stroke="{CRL}" stroke-width="10" stroke-linecap="round" marker-end="url(#ar)"/>
{''.join(f'<path d="M{{}} {{}}l-14-18" fill="none" stroke="{CRL}" stroke-width="4"/>'.format(190 - i * 16, 220 - i * 14) for i in range(2))}''', arrow=True)

add('verification', '二枚の記録を並べて突き合わせ、食い違いがないか確かめる',
    '検証、確認＝verification。', f'''
{''.join(f'<g transform="translate({{}} 200)"><path d="M-100-130h200v260h-200z" class="paper"/>{{}}</g>'.format(x, ''.join(f'<rect x="-76" y="{-90+i*44}" width="{152-(i%3)*40}" height="14" rx="7" fill="{MUTED}"/>' for i in range(5))) for x in (160, 440))}
{''.join(f'<path d="M270 {{}}h60" fill="none" stroke="{GRN}" stroke-width="4" stroke-dasharray="8 8"/>'.format(117 + i * 44) for i in range(5))}
{tick(300, 350, 0.7)}''')

add('versatility', 'ひとつの道具が、切る・開ける・締めると何通りにも役立つ',
    '多才さ、用途の広さ＝versatility。', f'''
<g transform="translate(300 200)">
  <path d="M-40-50h80v100h-80z" class="coral o"/>
  <path d="M40-30l90-14-90 30z" fill="{MUTED}" class="o"/>
  <path d="M40 10l90 24-90 12z" fill="{MUTED}" class="o"/>
  <path d="M-40-30l-90-16 90 34z" fill="{MUTED}" class="o"/>
  <path d="M-40 16l-90 26 90 10z" fill="{MUTED}" class="o"/></g>
{''.join(f'<g transform="translate({{}} {{}})">{{}}</g>'.format(x, y, o) for x, y, o in [
  (110, 90, f'<rect x="-30" y="-22" width="60" height="44" rx="6" class="tealp o"/>'),
  (490, 90, f'<circle r="26" class="goldp o"/>'),
  (110, 320, f'<path d="M-26 20l26-44 26 44z" class="greenp o"/>'),
  (490, 320, f'<rect x="-26" y="-26" width="52" height="52" rx="26" class="violetp o"/>')])}
{''.join(f'<path d="M300 200L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(x, y) for x, y in [(160, 110), (440, 110), (160, 300), (440, 300)])}''')

# --- 不当な扱い・視聴者・警戒 ---------------------------------------------------

add('victimisation', '同じ列の中で、一人にだけ重い荷と×が集まってくる',
    '不当な扱い、いじめ＝victimisation。', f'''
{''.join(person(90 + i * 110, 350, 1.0, 1, 'teal', 'blue', 'stand', 'short', 'smile') for i in range(2))}
{person(310, 350, 1.0, 1, 'coral', 'blue', 'up', 'bob', 'sad')}
{''.join(person(420 + i * 110, 350, 1.0, 1, 'teal', 'blue', 'stand', 'bun', 'smile') for i in range(2))}
{''.join(f'<g transform="translate({{}} {{}})"><circle r="22" class="coralp o"/>{{}}</g>'.format(310 + (i - 1) * 60, 110 + (i % 2) * 40, cross(0, 0, 0.34)) for i in range(3))}
{''.join(f'<path d="M{{}} {{}}L310 200" fill="none" stroke="{CRL}" stroke-width="3" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(310 + (i - 1) * 60, 140 + (i % 2) * 40) for i in range(3))}''', arrow=True)

add('viewership', '一つの画面の前に、それを見ている人の数がずらりと並ぶ',
    '視聴者数、視聴者層＝viewership。', f'''
<g transform="translate(300 130)">
  <path d="M-160-90h320v180h-320z" class="teal o"/>
  <path d="M-130-64h260v128h-260z" fill="#fffefd" class="o"/>
  {head(0, 10, 32, 'coral', 'bob')}
  <path d="M-20 90h40v20h-40z" fill="{MUTED}"/></g>
{''.join(head(70 + (i % 6) * 92, 290 + (i // 6) * 0, 26, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('blue', 'bun'), ('gold', 'cap'), ('violet', 'short'), ('coral', 'bob')]))}
{''.join(f'<path d="M{{}} 252v-20" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"/>'.format(70 + i * 92) for i in range(6))}''')

add('vigilance', '夜通し見張り台に立ち、目を離さずあたりをうかがう',
    '警戒、油断のなさ＝vigilance。', f'''
<g transform="translate(300 190)"><path d="M-260-150h520v300h-520z" fill="#2f3a4d"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#fff6d8"/>'.format(60 + (i * 71) % 480, 40 + (i * 37) % 90) for i in range(9))}
<g transform="translate(430 360)">
  <path d="M-70 0v-120h140V0z" fill="none" stroke="{BRN}" stroke-width="10"/>
  <path d="M-84-120h168v20h-168z" fill="{BRN}" class="o"/></g>
{person(430, 240, 1.0, -1, 'teal', 'blue', 'point', 'cap', 'flat')}
<path d="M380 190L120 140" fill="none" stroke="#fff6d8" stroke-width="4" stroke-dasharray="10 9"/>
<g transform="translate(120 140)"><path d="M-40 0q40-30 80 0-40 30-80 0z" fill="#fff6d8"/><circle r="13" class="ink"/></g>''')

add('vigorously', '腕にぐっと力を込め、勢いよくこすって磨く',
    '力強く、精力的に＝vigorously。', f'''
{table(352)}
<g transform="translate(300 290)"><path d="M-200-20h400v34h-400z" fill="#c9a464" class="o"/></g>
{person(180, 350, 1.3, 1, 'teal', 'blue', 'reach', 'short', 'flat')}
{hand(320, 250, 1)}
{''.join(f'<path d="M{{}} {{}}h60" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(360, 200 + i * 34) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}h-60" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)"/>'.format(360, 217 + i * 34) for i in range(2))}
{''.join(spark(440 + i * 40, 190 + (i % 2) * 40, 0.7, 'gold') for i in range(2))}''', arrow=True)

# --- 潔白・事実上・見通し -----------------------------------------------------

add('vindication', 'かけられていた疑いの×が取り消され、潔白が示される',
    '潔白の証明、正当性の立証＝vindication。', f'''
{split()}
{person(150, 350, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(150 230) rotate(-8)"><path d="M-50-40h100v80h-100z" class="paper"/>{cross(0, 0, 0.62)}</g>
{person(450, 350, 1.2, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<g transform="translate(450 220)"><circle r="46" class="greenp o"/>{tick(0, 0, 0.7)}</g>
{arc(260, 170, 340, 170, 44, MUTED, True, 5)}''', arrow=True)

add('virtually', '目盛りは上端のすぐ手前まで来ていて、満杯とほぼ変わらない',
    '事実上、ほとんど＝virtually。', f'''
<g transform="translate(300 210)">
  <path d="M-90-160h180v320h-180z" fill="#fffefd" class="o"/>
  <path d="M-80-130h160v280h-160z" class="teal"/>
  <path d="M-90-160h180v320h-180z" fill="none" class="o"/>
  <path d="M-110-160h220" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="10 9"/></g>
<path d="M430 50v30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
{ring(430, 66, 30, True)}
{tick(120, 120, 0.6)}''', arrow=True)

add('visibility', '霧の中では先が見えず、晴れれば遠くまで見通せる',
    '視界、見通し＝visibility。', f'''
{split()}
<g opacity="0.75"><path d="M20 60h260v300H20z" fill="#dfe4e6"/></g>
<g opacity="0.28">{house(150, 330, 0.7, 'coral')}{tree(250, 330, 0.8)}</g>
{''.join(f'<path d="M{{}} {{}}h120" fill="none" stroke="#ffffff" stroke-width="10"/>'.format(30 + (i % 2) * 60, 120 + i * 50) for i in range(5))}
{house(430, 330, 0.7, 'coral')}{tree(540, 330, 0.8)}
{sun(360, 100, 32)}
{cross(150, 110, 0.5)}{tick(480, 110, 0.5)}''')

add('visualisation', '数字の並びが、ひと目で分かる図に置き換わる',
    '視覚化、イメージ化＝visualisation。', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-100-120h200v240h-200z" class="paper"/>
  {''.join(f'<rect x="-76" y="{-92+i*40}" width="{152-(i%3)*40}" height="16" rx="8" fill="{INK}"/>' for i in range(5))}</g>
<g transform="translate(450 210)">
  <path d="M-110 100h220M-110 100v-200" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  {''.join(f'<rect x="{-92+i*52}" y="{100-(50+i*36)}" width="40" height="{50+i*36}" rx="5" class="teal o"/>' for i in range(4))}</g>
{arc(270, 140, 330, 140, 44, MUTED, True, 5)}''', arrow=True)

add('vitality', '青々と勢いよく茂る草木の中で、人が伸びやかに腕を広げる',
    '活力、生き生きしていること＝vitality。', f'''
<path d="M0 310h600v90H0z" class="greenp"/>
{tree(110, 330, 1.4)}{tree(500, 330, 1.3)}
{''.join(flower(200 + i * 70, 340, 0.55, c) for i, c in enumerate(['coral', 'gold', 'violet']))}
{person(320, 330, 1.35, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{sun(480, 90, 44)}
{''.join(spark(200 + i * 200, 120, 0.7, 'gold') for i in range(2))}''')

add('vocational', '教室ではなく作業場で、実際の工具の使い方を学ぶ',
    '職業訓練の＝vocational。', f'''
{table(320)}
{''.join(f'<g transform="translate({{}} 320)">{{}}</g>'.format(180 + i * 110, person(0, 0, 0.95, 1, c, 'blue', 'hold', 'cap', 'smile')) for i, c in enumerate(['teal', 'coral', 'green']))}
{''.join(f'<g transform="translate({{}} 250) rotate(-16)"><path d="M-8-46h16v60h-16z" fill="{BRN}" class="o"/><path d="M-24 14h48v20h-48z" fill="{MUTED}" class="o"/></g>'.format(216 + i * 110) for i in range(3))}
<g transform="translate(480 180)">
  <path d="M-70-60h140v120h-140z" fill="#fffefd" class="o"/>
  <path d="M-40-20h80v40h-80z" class="tealp o"/>
  <path d="M-40-40h40v12h-40z" fill="{MUTED}"/></g>
{''.join(f'<path d="M{{}} 290h40" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>'.format(90 + i * 0) for i in range(1))}''')

add('voltage', '電池を重ねるほど、計器の針が高いほうへ大きく振れる',
    '電圧＝voltage。', f'''
{''.join(f'<g transform="translate(140 {{}})"><path d="M-60-24h120v48h-120z" class="goldp o"/><path d="M60-12h16v24H60z" fill="{MUTED}" class="o"/></g>'.format(150 + i * 66) for i in range(3))}
<path d="M216 216h60" fill="none" stroke="{INK}" stroke-width="5"/>
{gauge(420, 290, 140, 0.82, 'coral')}
{bolt(300, 110, 1.2)}''')

add('voluntarily', 'だれに言われたわけでもなく、自分から手を挙げて前へ出る',
    '自発的に、任意で＝voluntarily。', f'''
{''.join(head(90 + i * 90, 330, 26, 'teal', 'short') for i in range(3))}
{''.join(head(400 + i * 90, 330, 26, 'teal', 'bob') for i in range(2))}
{person(340, 350, 1.2, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{''.join(spark(280 + i * 120, 110, 0.7, 'gold') for i in range(2))}
<g opacity="0.3"><path d="M340 60v40" fill="none" stroke="{MUTED}" stroke-width="0"/></g>
{cross(120, 150, 0.45)}
{''.join(f'<path d="M{{}} 190v-40" fill="none" stroke="{MUTED}" stroke-width="0"/>'.format(x) for x in (0,))}''')

finish(__file__)
