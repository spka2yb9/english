# -*- coding: utf-8 -*-
"""第180回。vo-/w-/y-/z- の語。unlawful の描き直しも含む。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def scissors_like(x, y, r=0, s=1):
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})">'
            f'<path d="M-70-10h110l30 10-30 10h-110z" fill="{MUTED}" class="o"/>'
            f'<path d="M-120-16h50v32h-50z" fill="{BRN}" class="o"/></g>')

# --- 第179回の描き直し -------------------------------------------------------

add('unlawful', '法の枠の内側ではなく、外へはみ出した行いに×がつく',
    '違法の＝unlawful。', f'''
<g transform="translate(240 200)">
  <path d="M-170-130h340v260h-340z" fill="none" stroke="{TEA}" stroke-width="7"/>
  {''.join(f'<circle cx="{-100+(i%3)*100}" cy="{-70+(i//3)*100}" r="26" class="tealp o"/>' for i in range(6))}</g>
<circle cx="500" cy="300" r="30" class="coral o"/>
{cross(500, 180, 0.7)}
<path d="M500 218v50" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="8 8"/>
{tick(120, 350, 0.5)}''')

# --- 投票・引換券・弱さ -------------------------------------------------------

add('voter', '記入した票を、自分の手で投票箱に入れる',
    '有権者、投票者＝voter。', f'''
{table(352)}
<g transform="translate(360 290)">
  <path d="M-110-60h220v120h-220z" class="tealp o"/>
  <path d="M-50-64h100v14h-100z" fill="{INK}"/>
  <path d="M-110-60h220" fill="none" stroke="{TEA}" stroke-width="4"/></g>
<g transform="translate(340 180) rotate(-14)">
  <path d="M-50-36h100v72h-100z" class="paper"/>
  {tick(0, 0, 0.42)}</g>
{person(160, 350, 1.2, 1, 'coral', 'blue', 'give', 'short', 'smile')}
{line(250, 200, 300, 200, MUTED, True, 4)}''', arrow=True)

add('voucher', '引換券を差し出すと、その場で品と交換してもらえる',
    '引換券、商品券＝voucher。', f'''
{table(300)}
{person(130, 350, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
<g transform="translate(250 220) rotate(-8)">
  <path d="M-70-40h140v80h-140z" class="goldp o"/>
  <path d="M-20-40v80" fill="none" stroke="{GLDD}" stroke-width="3" stroke-dasharray="7 7"/>
  <rect x="0" y="-16" width="52" height="12" rx="6" fill="{GLDD}"/></g>
<g transform="translate(400 230)"><rect x="-46" y="-36" width="92" height="72" rx="8" class="coral o"/></g>
{person(510, 300, 1.0, -1, 'violet', 'green', 'give', 'bun', 'smile')}
{''.join(f'<path d="M{{}} {{}}h{{}}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(x, y, d) for x, y, d in [(320, 170, 50), (370, 290, -50)])}''', arrow=True)

add('vulnerable to', '盾を持たない側にだけ、飛んできた矢がまともに当たる',
    '〜に弱い、〜を受けやすい＝vulnerable to。', f'''
{split()}
{person(150, 350, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
{person(450, 350, 1.2, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(390 250)">
  <path d="M-46-64h92v72q0 50-46 76-46-26-46-76z" class="bluep o"/></g>
{''.join(f'<g transform="translate({{}} {{}}) rotate(6)"><path d="M-90 0h90" stroke="{BRN}" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M0 0l-24-12v24z" class="ink"/></g>'.format(150, 220 + i * 40) for i in range(2))}
{''.join(f'<g transform="translate({{}} {{}}) rotate(6)"><path d="M-90 0h90" stroke="{BRN}" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M0 0l-24-12v24z" class="ink"/></g>'.format(348, 220 + i * 40) for i in range(2))}
{cross(150, 120, 0.5)}{tick(450, 120, 0.5)}''')

# --- 骨折り・服・寄せつけない ---------------------------------------------------

add('wade through', '腰まで水につかりながら、書類の山を一歩ずつ進む',
    '(退屈な作業を)苦労して進める＝wade through。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
{''.join(f'<path d="M{{}} 260q22-14 44 0" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(i * 88) for i in range(7))}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})">{{}}</g>'.format(x, y, r, doc(0, 0, 70, 90, 3)) for x, y, r in [(430, 210, 12), (490, 250, -16), (380, 260, 22), (520, 190, 8)])}
<g transform="translate(200 250)">
  <path d="M-60 0v-60q60-24 120 0V0z" class="teal o"/>
  <path d="M-60-60l-30 40M60-60l34 34" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
  <circle cx="0" cy="-100" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-34-108q4-36 34-36 28 0 34 34-18-16-34-6-16-10-34 8z" fill="{HAIR}"/>
  <circle cx="-11" cy="-100" r="3" class="ink"/><circle cx="11" cy="-100" r="3" class="ink"/>
  <path d="M-10-82q10 8 20 0" fill="none" stroke="{INK}" stroke-width="2.4"/></g>
{arc(270, 200, 380, 200, 46, MUTED, True, 5)}''', arrow=True)

add('waistcoat', 'そでのない前開きの上着に、ボタンが縦に並んでいる',
    'ベスト、チョッキ(英)＝waistcoat。', f'''
{table(352)}
<g transform="translate(300 220)">
  <path d="M-110-100h220l20 220h-260z" class="violet o"/>
  <path d="M-110-100q40 60 0 110l-20 110" fill="#fffaf1" class="o" opacity="0"/>
  <path d="M-30-100q30 50 60 0l14 220h-88z" fill="#fffaf1" class="o"/>
  <path d="M-110-100l-24 60 24 60M110-100l24 60-24 60" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
  {''.join(f'<circle cx="0" cy="{40+i*40}" r="9" class="goldp o"/>' for i in range(3))}
  <path d="M-110-100h220" fill="none" class="o"/></g>''')

add('ward off', 'さした傘が雨つぶを受け止め、体には一滴も届かせない',
    '(危険・病気を)寄せつけない＝ward off。', f'''
{''.join(f'<path d="M{{}} {{}}l-12 26" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>'.format(70 + i * 46, 50 + (i % 3) * 30) for i in range(11))}
<g transform="translate(300 190)">
  <path d="M-140 0a140 140 0 0 1 280 0z" class="coral o"/>
  <path d="M-140 0q40-24 70 0t70 0 70 0" fill="none" stroke="{CRLD}" stroke-width="4"/>
  <path d="M0 0v130q0 26 26 26" fill="none" stroke="{BRN}" stroke-width="8"/></g>
{person(300, 350, 1.05, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{''.join(f'<path d="M{{}} {{}}l-14 30" fill="none" stroke="{BLU}" stroke-width="4"/>'.format(170 + i * 280, 200) for i in range(2))}
{tick(520, 320, 0.6)}''')

# --- 保証・注意・薄める -------------------------------------------------------

add('warranty', '品物に付いた保証書に、いつまで有効かの期間が示される',
    '保証、保証書＝warranty。', f'''
{table(352)}
<g transform="translate(180 270)"><rect x="-70" y="-56" width="140" height="112" rx="10" class="teal o"/></g>
<g transform="translate(420 230)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <circle cy="-40" r="44" class="greenp o"/>
  {tick(0, -40, 0.6)}
  <rect x="-80" y="40" width="160" height="18" rx="9" fill="{MUTED}"/>
  <rect x="-80" y="72" width="100" height="18" rx="9" class="coral"/></g>
{line(266, 250, 306, 240, MUTED, True, 4)}''', arrow=True)

add('watch out for', '前方の地面に開いた穴を、標識が指して注意をうながす',
    '〜に気をつける＝watch out for。', f'''
<path d="M0 330h600v70H0z" class="ground"/>
<path d="M380 330q40 70 110 0z" fill="#3f3126" class="o"/>
<g transform="translate(250 330)">
  <path d="M-8 0v-140h16V0z" fill="{MUTED}"/>
  <path d="M0-240l100 100H-100z" class="goldp o"/>
  <path d="M-8-200h16v34h-16z" class="ink"/><circle cy="-152" r="9" class="ink"/></g>
{person(110, 350, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'flat')}
{line(320, 250, 400, 300, MUTED, True, 4)}''', arrow=True)

add('water down', '濃い色の液に水を足していくと、色がどんどん薄くなる',
    '薄める、骨抜きにする＝water down。', f'''
{table(352)}
{split()}
<g transform="translate(150 270)">
  <path d="M-60-80l10 160h100l10-160z" fill="#fffefd" class="o"/>
  <path d="M-48-20h96l8 100h-112z" fill="#b74338"/>
  <path d="M-60-80l10 160h100l10-160z" fill="none" class="o"/></g>
<g transform="translate(450 270)">
  <path d="M-60-80l10 160h100l10-160z" fill="#fffefd" class="o"/>
  <path d="M-56-60h112l14 140h-140z" fill="#f2bfb6"/>
  <path d="M-60-80l10 160h100l10-160z" fill="none" class="o"/></g>
<g transform="translate(380 110) rotate(40)">
  <path d="M-30-50h60v90a22 22 0 0 1-22 22h-16a22 22 0 0 1-22-22z" class="bluep o"/></g>
{''.join(drop(430 + i * 10, 160 + i * 22, 1.0, 'blue') for i in range(2))}
{arc(250, 180, 330, 180, 44, MUTED, True, 4)}''', arrow=True)

add('wear off', '塗った色が日を追うごとに薄れ、やがてほとんど消える',
    '(効果・痛みが)だんだん消える＝wear off。', f'''
{''.join(f'<g transform="translate({{}} 220)"><rect x="-56" y="-70" width="112" height="140" rx="10" fill="{{}}" stroke="{INK}" stroke-width="2.5"/></g>'.format(100 + i * 130, c) for i, c in enumerate(['#238b83', '#6fb3ac', '#b7d9d5', '#eaf6f4']))}
{''.join(f'<path d="M{{}} 330h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(130 + i * 130) for i in range(3))}
{clock(540, 110, 40, 3, 30)}''', arrow=True)

add('weigh up', '二つの案を天秤の左右に載せ、どちらが重いかを見比べる',
    '(選択肢を)比べて検討する＝weigh up。', f'''
{scales(300, 320, -8, 1.0)}
<g transform="translate(190 190)"><rect x="-40" y="-28" width="80" height="56" rx="8" class="teal o"/></g>
<g transform="translate(408 210)"><rect x="-36" y="-24" width="72" height="48" rx="8" class="coral o"/></g>
{person(500, 350, 0.95, -1, 'violet', 'blue', 'think', 'bun', 'flat')}
<g transform="translate(120 110)">
  <path d="M-22-34q0-26 24-26t24 26q0 18-24 26v12" fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="2" cy="26" r="6" fill="{MUTED}"/></g>''')

# --- 波止場・そのうえ・旋回 -----------------------------------------------------

add('wharf', '岸に寄せた船から、板づたいに荷が陸へ揚げられる',
    '波止場、荷揚げ場＝wharf。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h240v150H0z" fill="#d8cdb6" class="o"/>
{''.join(f'<path d="M{{}} 400v-40" stroke="{BRN}" stroke-width="12" fill="none"/>'.format(60 + i * 60) for i in range(3))}
<g transform="translate(420 250) rotate(4)">
  <path d="M-140 0h280l-36 54h-208z" class="coral o"/>
  <path d="M-40 0v-120h120l-104 44" fill="{GLDP}" class="o"/></g>
<path d="M240 260L300 236" fill="none" stroke="{BRN}" stroke-width="12"/>
{box(160, 230, 74, 56, 18, 'gold')}
{box(90, 230, 74, 56, 18, 'gold')}''')

add('what is more', '積み上げた理由の上に、さらにもう一つの理由が加えられる',
    'さらに、そのうえ＝what is more。', f'''
{''.join(f'<rect x="180" y="{{}}" width="240" height="46" rx="8" class="tealp o"/>'.format(280 - i * 56) for i in range(3))}
<g transform="translate(300 130)"><rect x="-120" y="-23" width="240" height="46" rx="8" class="coral o"/></g>
{arc(500, 60, 380, 120, 50, CRL, True, 5)}
<path d="M120 350h360" fill="none" stroke="{BRN}" stroke-width="8"/>''', arrow=True)

add('whirl', '広げたすそが回転にあおられ、ぐるぐると旋回する',
    'ぐるぐる回る、旋回＝whirl。', f'''
<g transform="translate(300 240)">
  <path d="M-120 100q30-130 120-130t120 130z" class="violet o"/>
  <path d="M-40-30q40-24 80 0l-10 60h-60z" class="violetd o"/>
  <circle cx="0" cy="-64" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-34-72q4-36 34-36 28 0 34 34-18-16-34-6-16-10-34 8z" fill="{HAIR}"/>
  <circle cx="-11" cy="-66" r="3" class="ink"/><circle cx="11" cy="-66" r="3" class="ink"/>
  <path d="M-10-50q10 8 20 0" fill="none" stroke="{INK}" stroke-width="2.4"/>
  <path d="M-40-30l-70-24M40-30l70-24" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/></g>
<g transform="translate(300 300)"><path d="M-180 0a180 60 0 1 0 70-52" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"/></g>''', arrow=True)

# --- 告発・削る・卸 ----------------------------------------------------------

add('whistleblower', '内側で起きている不正に気づいた人が、笛を鳴らして外へ知らせる',
    '内部告発者＝whistleblower。', f'''
<g transform="translate(420 220)">
  <path d="M-130-140h260v280h-260z" fill="#f1efe8" class="o"/>
  {''.join(f'<g transform="translate({-70+(i%2)*140} {-70+(i//2)*140})"><circle r="24" class="tealp o"/></g>' for i in range(4))}
  <g transform="translate(0 0)"><circle r="26" class="coral o"/>{cross(0, 0, 0.34)}</g></g>
{person(140, 350, 1.25, 1, 'teal', 'blue', 'think', 'short', 'flat')}
<g transform="translate(196 234) rotate(-16)">
  <path d="M-30-14h44l20 14-20 14h-44z" fill="{MUTED}" class="o"/>
  <circle cx="24" cy="6" r="7" fill="none" stroke="{INK}" stroke-width="3"/></g>
{''.join(f'<path d="M{{}} {{}}q16 12 0 24" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(250 + i * 18, 190 + i * 14) for i in range(3))}''')

add('whittle down', 'ナイフで木の棒を少しずつ削り、細く小さくしていく',
    '少しずつ削って減らす＝whittle down。', f'''
{table(352)}
<g opacity="0.28" transform="translate(300 270)"><path d="M-170-40h340v80h-340z" fill="{MUTED}"/></g>
<g transform="translate(300 270)"><path d="M-170-24h340v48h-340z" fill="#c9a464" class="o"/></g>
{scissors_like(300, 190, 18, 1.0)}
{''.join(f'<g transform="translate({{}} {{}}) rotate({{}})"><path d="M-16-6h32l-6 12h-26z" fill="#e0c48c" class="o"/></g>'.format(160 + i * 60, 330 - (i % 2) * 16, -20 + i * 25) for i in range(4))}
{arc(480, 160, 480, 240, 40, MUTED, True, 4)}''', arrow=True)

add('wholesaler', '大きな荷をまとめて受け取り、複数の小売店へ分けて送る',
    '卸売業者＝wholesaler。', f'''
<g transform="translate(140 280)">
  <path d="M-90 0v-120h180V0z" fill="#fffdf6" class="o"/>
  <path d="M-50-90h100v50h-100z" class="tealp o"/></g>
{box(140, 340, 130, 46, 16, 'gold')}
{''.join(f'<g transform="translate({{}} {{}})"><path d="M-60 0v-70h120V0z" fill="#fffefd" class="o"/><path d="M-70-70h140l-12-30h-116z" class="coral o"/></g>'.format(430, 130 + i * 110) for i in range(2))}
<g transform="translate(430 350)"><path d="M-60 0v-70h120V0z" fill="#fffefd" class="o"/><path d="M-70-70h140l-12-30h-116z" class="coral o"/></g>
{''.join(f'<path d="M240 280L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(350, 120 + i * 110) for i in range(3))}''', arrow=True)

# --- 男やもめ・かつら・快く -----------------------------------------------------

add('widower', '亡くなった妻の写真の前に、男性がひとりで静かに座る',
    '男やもめ＝widower。', f'''
{table(300)}
<g transform="translate(420 250)">
  <path d="M-70-90h140v180h-140z" class="paper"/>
  {head(0, -10, 34, 'coral', 'bob')}
  <path d="M-70 60h140" fill="none" stroke="{MUTED}" stroke-width="3"/></g>
{chair(180, 300, 1.0, 'gold', 1)}
{sit(180, 300, 1.1, 1, 'blue', 'green', 'short', 'sad', 'lap')}
{flower(320, 300, 0.5, 'violet')}
{''.join(f'<path d="M{{}} {{}}q12 12 0 24" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(250 + i * 16, 170 + i * 14) for i in range(2))}''')

add('wig', '髪の形につくられたかぶり物が、台の上に置かれている',
    'かつら＝wig。', f'''
{table(352)}
<g transform="translate(300 290)">
  <ellipse rx="70" ry="16" fill="#e8ddc9" class="o"/>
  <path d="M-44 0q-6-60 44-60t44 60z" fill="#f0e6d2" class="o"/></g>
<g transform="translate(300 200)">
  <path d="M-90 60q-16-130 90-130t90 130q-40-40-90-34-52-6-90 34z" fill="{HAIR}"/>
  <path d="M-90 60q-20 40-6 64 18-18 24-50M90 60q20 40 6 64-18-18-24-50" fill="{HAIR}"/></g>
{''.join(f'<path d="M{{}} {{}}q12-14 0-26" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(470 + i * 20, 190 - i * 14) for i in range(2))}''')

add('willingly', '頼まれた仕事を、いやな顔ひとつせず笑顔で引き受ける',
    '進んで、快く＝willingly。', f'''
{person(160, 350, 1.15, -1, 'coral', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(290 220)">{doc(0, 0, 96, 120, 3)}</g>
{person(450, 350, 1.25, -1, 'teal', 'green', 'reach', 'short', 'smile')}
{arc(240, 170, 350, 180, 46, MUTED, True, 4)}
{''.join(spark(500 + i * 0, 120 + i * 40, 0.7, 'gold') for i in range(2))}''', arrow=True)

# --- 車・一掃・配線 ----------------------------------------------------------

add('windscreen', '運転席の前の大きなガラスが、風と雨をさえぎる',
    'フロントガラス(英)＝windscreen。', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<g transform="translate(300 300)">
  <path d="M-220 0v-60l70-110h180l70 110V0z" class="teal o"/>
  <path d="M-130-160h150l58 94h-236z" fill="#dfeaf2" class="o"/>
  <path d="M-90-70l50-90M10-160l40 90" fill="none" stroke="{INK}" stroke-width="3"/>
  <circle cx="-130" cy="10" r="34" class="ink"/><circle cx="130" cy="10" r="34" class="ink"/>
  <circle cx="-130" cy="10" r="14" fill="#fffefd"/><circle cx="130" cy="10" r="14" fill="#fffefd"/></g>
{ring(292, 224, 130, True)}
{''.join(f'<path d="M{{}} {{}}l-12 26" fill="none" stroke="{BLU}" stroke-width="4" stroke-linecap="round"/>'.format(120 + i * 80, 60 + (i % 2) * 26) for i in range(6))}''')

add('wipe out', 'ぎっしり並んでいたものが、ひとふきで跡形もなく消える',
    '全滅させる、一掃する＝wipe out。', f'''
{split()}
{''.join(f'<circle cx="{{}}" cy="{{}}" r="20" class="teal o"/>'.format(60 + (i % 4) * 62, 130 + (i // 4) * 70) for i in range(12))}
<g transform="translate(320 200) rotate(-10)">
  <path d="M-30-120h60v240h-60z" class="coralp o"/>
  <path d="M-30-120h60v40h-60z" class="coral o"/></g>
{arc(300, 90, 300, 320, -70, CRL, True, 6)}
<g opacity="0.22">{''.join(f'<circle cx="{{}}" cy="{{}}" r="20" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(400 + (i % 3) * 62, 160 + (i // 3) * 70) for i in range(6))}</g>''', arrow=True)

add('wiring', '壁の内側を、色分けされた電線が何本も通っている',
    '配線＝wiring。', f'''
<g transform="translate(300 200)">
  <path d="M-240-150h480v300h-480z" fill="#e4dccb" class="o"/>
  <path d="M-160-150h320v300h-320z" fill="#f6efe1" class="o"/></g>
{''.join(f'<path d="M-160 {{}}q80 60 160 0t160 0" transform="translate(300 200)" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round"/>'.format(-90 + i * 60) for i, c in enumerate(['#e86452', '#4e86c6', '#4e986a']))}
<g transform="translate(300 330)">
  <path d="M-50-40h100v80h-100z" fill="#fffefd" class="o"/>
  <circle cx="-18" cy="0" r="9" class="ink"/><circle cx="18" cy="0" r="9" class="ink"/></g>
{''.join(f'<path d="M{{}} 290v20" fill="none" stroke="{MUTED}" stroke-width="4"/>'.format(280 + i * 40) for i in range(2))}''')

# --- 〜に関して・例外・確実に ---------------------------------------------------

add('with regard to', '書類の中の一項だけを指し、その点について話す',
    '〜に関して＝with regard to。', f'''
<g transform="translate(330 200)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  {''.join(f'<rect x="-140" y="{-104+i*48}" width="{280-(i%3)*60}" height="16" rx="8" fill="{MUTED}"/>' for i in range(5))}
  <rect x="-140" y="-8" width="220" height="16" rx="8" class="coral"/></g>
{hand(130, 200, 1)}
{line(178, 200, 220, 198, CRL, False, 5)}
{ring(310, 200, 0, True)}''', arrow=True)

add('with respect to', '広がる図の中の、たった一点に向けて矢印が集まる',
    '〜に関して＝with respect to。', f'''
{''.join(f'<circle cx="{{}}" cy="{{}}" r="22" class="tealp o"/>'.format(x, y) for x, y in [(90, 90), (510, 90), (90, 320), (510, 320), (300, 60), (300, 350)])}
<circle cx="300" cy="200" r="48" class="coral o"/>
{''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"/>'.format(x, y, 300 + (x - 300) * 0.36, 200 + (y - 200) * 0.36) for x, y in [(120, 110), (480, 110), (120, 300), (480, 300), (300, 92), (300, 318)])}''', arrow=True)

add('with the exception of', 'そろって同じ印がつく中で、一つだけが枠の外に置かれる',
    '〜を除いて＝with the exception of。', f'''
<g transform="translate(260 200)">
  <path d="M-180-130h360v260h-360z" fill="none" stroke="{TEA}" stroke-width="6"/>
  {''.join(f'<circle cx="{-110+(i%3)*110}" cy="{-70+(i//3)*100}" r="30" class="teal o"/>' for i in range(6))}</g>
<circle cx="530" cy="200" r="30" class="coral o"/>
{cross(530, 100, 0.5)}
<path d="M530 134v34" fill="none" stroke="{CRL}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('without doubt', '迷いの?はどこにもなく、ためらわず一つに手を伸ばす',
    '疑いなく＝without doubt。', f'''
<g opacity="0.28">
  {''.join(f'<g transform="translate({{}} {{}})"><path d="M-16-26q0-20 18-20t18 20q0 14-18 20v10" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/><circle cy="24" r="5" fill="{MUTED}"/></g>'.format(110 + i * 40, 110) for i in range(2))}</g>
{''.join(cross(110 + i * 40, 110, 0.3) for i in range(2))}
<g transform="translate(390 210)"><rect x="-70" y="-54" width="140" height="108" rx="10" class="teal o"/></g>
{hand(250, 230, 1)}
{line(300, 220, 310, 216, MUTED, True, 4)}
{tick(500, 100, 0.8)}''', arrow=True)

add('without fail', 'カレンダーのどの日にも、ひとつ残らず印がついている',
    '必ず、間違いなく＝without fail。', f'''
<g transform="translate(300 200)">
  <path d="M-230-150h460v300h-460z" fill="#fffefd" class="o"/>
  <path d="M-230-150h460v50h-460z" class="teal o"/>
  {''.join(f'<path d="M{-230+c*92} -100v250" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for c in range(1, 5))}
  {''.join(f'<path d="M-230 {-100+r*84}h460" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for r in range(1, 3))}
  {''.join(tick(-184 + c * 92, -58 + r * 84, 0.36) for c in range(5) for r in range(3))}</g>''')

# --- ぐらつき・胎内・仕上がり ---------------------------------------------------

add('wobble', '積み上げた品が左右にぐらつき、いまにも倒れそうになる',
    'ぐらぐらする、ぐらつき＝wobble。', f'''
{table(352)}
<g transform="translate(300 300) rotate(9)">
  {''.join(f'<ellipse cy="{-24-i*44}" rx="{70-i*10}" ry="18" fill="#fffefd" class="o"/>' for i in range(5))}</g>
<g opacity="0.26" transform="translate(300 300) rotate(-9)">
  {''.join(f'<ellipse cy="{-24-i*44}" rx="{70-i*10}" ry="18" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>' for i in range(5))}</g>
<g transform="translate(300 70)"><path d="M-60 0q60-30 120 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/></g>''', arrow=True)

add('womb', '母の体の中、丸くやわらかな場所に赤ん坊がおさまっている',
    '子宮＝womb。', f'''
<g transform="translate(300 220)">
  <path d="M-140 30q-20-110 60-140 80-30 140 20 50 44 24 130-30 90-124 84-80-6-100-94z" class="coralp o"/>
  <path d="M-140-20q-40-30-56-70M140-30q40-30 56-70" fill="none" stroke="{CRL}" stroke-width="14" stroke-linecap="round"/></g>
<g transform="translate(300 230) rotate(16)">
  <circle cx="0" cy="-40" r="42" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40 0q40-26 80 0 16 46-10 70h-60q-26-24-10-70z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40 30q-30 6-36 34M40 30q30 6 36 34" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
  <circle cx="-14" cy="-44" r="3" class="ink"/><circle cx="14" cy="-44" r="3" class="ink"/>
  <path d="M-10-26q10 8 20 0" fill="none" stroke="{INK}" stroke-width="2.4"/></g>''')

add('workmanship', '角も継ぎ目もきれいにそろった、丁寧な仕上がりの椅子',
    '仕上がり、作りのよさ＝workmanship。', f'''
{table(352)}
{chair(300, 300, 1.6, 'gold', 1)}
{''.join(spark(140 + i * 320, 130 + (i % 2) * 40, 0.8, 'gold') for i in range(2))}
<g transform="translate(480 250)">
  <circle r="40" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M28 28l36 36" stroke="{BRN}" stroke-width="12" stroke-linecap="round" fill="none"/>
  {tick(0, 0, 0.3)}</g>''')

add('worsen', '傷んだ箇所が日ごとに広がり、状態がもっと悪くなる',
    '悪化する、悪化させる＝worsen。', f'''
{''.join(f'<g transform="translate({{}} 210)"><path d="M-70-80h140v160h-140z" fill="#fffefd" class="o"/>{{}}</g>'.format(110 + i * 190, ''.join(f'<circle cx="{-40+(j%3)*40}" cy="{-30+(j//3)*40}" r="{10+i*4}" class="coral o"/>' for j in range(1 + i * 3))) for i in range(3))}
{''.join(f'<path d="M{{}} 340h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8" marker-end="url(#ar)"/>'.format(150 + i * 190) for i in range(2))}
{''.join(f'<path d="M{{}} {{}}l14-18" fill="none" stroke="{CRL}" stroke-width="5"/>'.format(490 + i * 18, 90 - i * 14) for i in range(2))}''', arrow=True)

# --- 値する・言い逃れ・ものさし -------------------------------------------------

add('worthy of', '差し出された賞が、その働きにふさわしいと認められる',
    '〜に値する＝worthy of。', f'''
{person(180, 350, 1.25, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<g transform="translate(400 210)">
  <circle r="70" class="gold o"/>
  <circle r="46" fill="none" stroke="{GLDD}" stroke-width="5"/>
  <path d="M-40 62l-16 90 56-34 56 34-16-90z" class="coral o"/></g>
{arc(300, 150, 340, 160, 44, MUTED, True, 5)}
{tick(120, 130, 0.7)}''', arrow=True)

add('wriggle out of', '結んだはずの縄からするりと身をかわして、責めを逃れる',
    '言い逃れて避ける＝wriggle out of。', f'''
<g transform="translate(220 250)">
  <path d="M-90-70q90-40 180 0 20 70 0 140-90 40-180 0-20-70 0-140z" fill="none" stroke="{BRN}" stroke-width="12"/>
  {''.join(f'<path d="M-90 {-30+i*44}q90 40 180 0" fill="none" stroke="{BRN}" stroke-width="10"/>' for i in range(3))}</g>
<g transform="translate(420 320) rotate(-24)">{person(0, 0, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'smile')}</g>
{arc(300, 210, 400, 230, 60, MUTED, True, 5)}
{doc(130, 110, 90, 70, 2)}
{cross(130, 110, 0.5)}''', arrow=True)

add('yardstick', '同じものさしを当てて、どれがどれだけかを同じ基準で測る',
    '判断の基準、ものさし＝yardstick。', f'''
{table(352)}
<g transform="translate(300 150)">
  <path d="M-240-24h480v48h-480z" fill="#f0e6d2" class="o"/>
  {''.join(f'<path d="M{-220+i*40} -24v{24 if i%2 else 34}" stroke="{INK}" stroke-width="3" fill="none"/>' for i in range(12))}</g>
{''.join(f'<rect x="{{}}" y="{{}}" width="80" height="{{}}" rx="6" class="teal o"/>'.format(110 + i * 130, 300 - (40 + i * 40), 40 + i * 40) for i in range(3))}
{''.join(f'<path d="M{{}} {{}}v-{{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>'.format(150 + i * 130, 300 - (40 + i * 40), 84 - i * 40) for i in range(3))}''')

add('yearn for', '遠くの灯りをじっと見つめ、胸を押さえて焦がれる',
    '切望する、恋い焦がれる＝yearn for。', f'''
<g transform="translate(300 190)"><path d="M-260-150h520v300h-520z" fill="#3b4557"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="3" fill="#fff6d8"/>'.format(60 + (i * 71) % 480, 40 + (i * 31) % 90) for i in range(9))}
<g transform="translate(470 260)">
  <path d="M-46 40v-70h92v70z" fill="#2f3a4d" stroke="#8a93a5" stroke-width="3"/>
  <path d="M-26-10h24v24h-24z" fill="#ffe6a8"/>
  <path d="M-56-70L0-110l56 40z" fill="#2f3a4d" stroke="#8a93a5" stroke-width="3"/></g>
<g transform="translate(170 340)">
  <path d="M-70 0v-120q70-30 140 0V0z" class="teal o"/>
  <path d="M-70-120q-14 56 46 60" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
  <circle cx="0" cy="-166" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-34-174q4-36 34-36 28 0 34 34-18-16-34-6-16-10-34 8z" fill="{HAIR}"/>
  <circle cx="-11" cy="-166" r="3" class="ink"/><circle cx="11" cy="-166" r="3" class="ink"/>
  <path d="M-10-146q10 8 20 0" fill="none" stroke="{INK}" stroke-width="2.4"/>
  <path d="M-24-96q24-20 48 0-10 32-24 42-14-10-24-42z" class="coral o"/></g>
<path d="M230 220h170" fill="none" stroke="#8a93a5" stroke-width="4" stroke-dasharray="10 9"/>''')

# --- 酵母・拡大 --------------------------------------------------------------

add('yeast', '酵母を混ぜたパン生地が、時間とともにふくらんで倍になる',
    '酵母、イースト＝yeast。', f'''
{split()}
{table(352)}
<g transform="translate(150 300)">
  <ellipse rx="80" ry="16" fill="#fffefd" class="o"/>
  <path d="M-56 0q0-46 56-46t56 46z" fill="#e8d2a8" class="o"/></g>
<g transform="translate(450 300)">
  <ellipse rx="80" ry="16" fill="#fffefd" class="o"/>
  <path d="M-80 0q0-110 80-110t80 110z" fill="#e8d2a8" class="o"/></g>
<g transform="translate(230 130) rotate(20)">
  <path d="M-26-40h52v70a20 20 0 0 1-20 20h-12a20 20 0 0 1-20-20z" class="goldp o"/></g>
{''.join(f'<circle cx="{{}}" cy="{{}}" r="4" fill="{GLDD}"/>'.format(190 + i * 12, 200 + i * 14) for i in range(3))}
{arc(260, 200, 340, 200, 44, MUTED, True, 4)}
{clock(540, 120, 34, 2, 30)}''', arrow=True)

add('zoom in', '小さく見えていた一部分が、画面いっぱいに大きく引き寄せられる',
    '拡大する、寄る＝zoom in。', f'''
{split()}
<g transform="translate(150 200)">
  <path d="M-110-90h220v180h-220z" fill="#fffefd" class="o"/>
  {house(0, 40, 0.34, 'coral')}
  <path d="M-30 0h60v40h-60z" fill="none" stroke="{CRL}" stroke-width="4"/></g>
<g transform="translate(450 200)">
  <path d="M-110-90h220v180h-220z" fill="#fffefd" class="o"/>
  <path d="M-70-50h140v120h-140z" class="coralp o"/>
  <path d="M-40-20h60v60h-60z" fill="#fffefd" class="o"/></g>
{arc(270, 150, 330, 150, 44, MUTED, True, 5)}
{''.join(f'<path d="M{{}} {{}}L{{}} {{}}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"/>'.format(x1, y1, x2, y2) for x1, y1, x2, y2 in [(120, 200), (340, 110)] and [(120, 200, 340, 110), (180, 240, 340, 290)])}''', arrow=True)

finish(__file__)
