# -*- coding: utf-8 -*-
"""第168回。a-/b- の残り。形容詞・句動詞・抽象名詞が中心。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

def pie(x, y, r, frac, cls='teal', rest=MUTED):
    a = math.radians(frac * 360 - 90)
    lg = 1 if frac > 0.5 else 0
    ex, ey = x + r * math.cos(a), y + r * math.sin(a)
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fffefd" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M{x} {y}L{x} {y-r}A{r} {r} 0 {lg} 1 {ex:.1f} {ey:.1f}z" class="{cls} o"/>')

def grid(x, y, cols, rows, w, gap, cls='tealp'):
    return ''.join(f'<rect x="{x+c*(w+gap)}" y="{y+r*(w+gap)}" width="{w}" height="{w}" rx="4" class="{cls} o"/>'
                   for r in range(rows) for c in range(cols))

# --- ざらつき・くっつき -------------------------------------------------------

add('abrasive', 'ざらざらした紙やすりで板の表面を削り、細かい粉が飛ぶ',
    '研磨性の。人柄なら「とげとげしい」＝abrasive。', f'''
{table(320)}
<g transform="translate(300 300)">
  <path d="M-220 0h440v18h-440z" fill="#e6d3b4" class="o"/>
  <path d="M-220-4h440" fill="none" stroke="{BRN}" stroke-width="3"/></g>
<g transform="translate(250 250) rotate(-8)">
  <path d="M-100-34h200v56h-200z" fill="#b98a58" class="o"/>
  {''.join(f'<circle cx="{-88+i*11}" cy="{-26+(i%5)*11}" r="2.6" fill="{BRN}"/>' for i in range(34))}
  <path d="M-80-34h160v-22h-160z" class="goldd o"/></g>
{''.join(f'<circle cx="{400+i*17}" cy="{240+(i%4)*16}" r="{3+i%3}" fill="{MUTED}"/>' for i in range(9))}
{''.join(f'<path d="M{370+i*22} {284}q10-12 20 0" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(4))}''')

add('adhesive', '割れた皿の破片を、接着剤のチューブから出したのりでつなぎ合わせる',
    '粘着性の、接着剤＝adhesive。', f'''
{table(330)}
<g transform="translate(310 200)">
  <path d="M-130 60a130 130 0 0 1 118-129l8 129z" class="bluep o"/>
  <path d="M20-69a130 130 0 0 1 110 129H28z" class="bluep o"/>
  <path d="M-4-70l10 130" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="9 8"/></g>
<g transform="translate(120 300) rotate(-30)">
  <path d="M-26-90h52v120a20 20 0 0 1-20 20h-12a20 20 0 0 1-20-20z" class="coral o"/>
  <path d="M-12-112h24v22h-24z" class="corald o"/>
  <path d="M-7-126h14v14h-14z" class="ink"/></g>
{''.join(f'<circle cx="{188+i*14}" cy="{214+i*10}" r="{7-i}" class="goldp o"/>' for i in range(4))}''')

# --- 説明する・占める ---------------------------------------------------------

add('account for', '円グラフの大きな一切れを指さして、その分が何かを説明する',
    '説明する、(割合を)占める＝account for。', f'''
{pie(360, 190, 120, 0.62, 'teal')}
{ring(360, 190, 132, True)}
{person(120, 330, 1.05, 1, 'coral', 'blue', 'point', 'bob', 'smile')}
{arc(190, 200, 250, 180, 40, MUTED, True, 4)}
{''.join(f'<rect x="{460}" y="{150+i*34}" width="{92-i*22}" height="14" rx="7" fill="{MUTED}"/>' for i in range(3))}''', arrow=True)

add('add up', '一列のコインを上から順に足し、下に出た合計が帳簿の数と合う',
    'つじつまが合う、合計する＝add up。', f'''
{''.join(coin(200, 90 + i * 46) for i in range(4))}
<path d="M150 268h100" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
<path d="M120 250h26M133 237v26" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
{coin(200, 312, 28)}
{doc(440, 200, 150, 190, 4)}
<g transform="translate(440 250)">{coin(0, 0, 26)}</g>
{tick(440, 320, 0.9)}
{arc(250, 300, 380, 250, 60, GRN, True, 4)}''', arrow=True)

# --- 認定・許可・権威 ---------------------------------------------------------

add('accredit', '検査を終えた学校の建物に、公印つきの認定証が掲げられる',
    '(機関を)公認する、認定する＝accredit。', f'''
{building(190, 306, 1.1, 'teal')}
<g transform="translate(440 190)">
  {doc(0, 0, 170, 210, 3)}
  <circle cx="0" cy="52" r="40" class="coralp o"/>
  <circle cx="0" cy="52" r="26" fill="none" stroke="{CRL}" stroke-width="5"/>
  <path d="M-14 52l10 12 22-26" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></g>
{arc(360, 150, 268, 170, 46, MUTED, True, 4)}''', arrow=True)

add('authorise', '書類に判を押して、閉じていたゲートが開く',
    '許可する、権限を与える＝authorise。', f'''
{table(320)}
{doc(180, 230, 150, 180, 3)}
<g transform="translate(180 252)">
  <circle r="40" class="coralp o"/><circle r="26" fill="none" stroke="{CRL}" stroke-width="5"/></g>
<g transform="translate(180 110)">
  <path d="M-44 40h88v26h-88z" class="ink"/><path d="M-18 40v-44h36v44z" fill="{BRN}" class="o"/>
  <path d="M-30-4h60v-22h-60z" fill="{BRN}" class="o"/></g>
<g transform="translate(450 306)">
  <path d="M-90 0v-160M90 0v-160" fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-80-140v130" fill="none" stroke="{TEA}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-70-130q80-40 150 10" fill="none" stroke="{TEA}" stroke-width="10" stroke-linecap="round" stroke-dasharray="16 14"/></g>
{tick(450, 200, 1.0)}''')

add('authoritative', '大勢が同じ一冊の分厚い本を開き、その記述を頼りにする',
    '権威ある、信頼できる＝authoritative。', f'''
{book(300, 170, 1.15, 'violet')}
{spark(300, 60, 1.4, 'gold')}
{''.join(head(100 + i * 100, 320, 26, s, h) for i, (s, h) in enumerate([('teal', 'short'), ('coral', 'bob'), ('green', 'bun'), ('blue', 'cap'), ('gold', 'short')]))}
{''.join(f'<path d="M{110+i*100} 288L{280} 232" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"/>' for i in range(5))}''')

# --- 適応・柔軟 --------------------------------------------------------------

add('adaptable', '同じ柔らかいブロックが、四角い穴にも丸い穴にもぴたりと収まる',
    '順応性のある、融通のきく＝adaptable。', f'''
{split()}
<g transform="translate(160 200)">
  <path d="M-90-90h180v180h-180z" fill="#e8ddc9" class="o"/>
  <path d="M-52-52h104v104h-104z" fill="#fffaf1" class="o"/>
  <path d="M-46-46h92v92h-92z" class="teal o"/></g>
<g transform="translate(440 200)">
  <path d="M-90-90h180v180h-180z" fill="#e8ddc9" class="o"/>
  <circle r="54" fill="#fffaf1" class="o"/>
  <circle r="48" class="teal o"/></g>
{tick(160, 340, 0.7)}{tick(440, 340, 0.7)}''')

add('assimilation', '外から来た色の粒が、周りの群れと同じ色に染まって溶け込む',
    '同化、吸収＝assimilation。', f'''
{grid(80, 90, 4, 4, 46, 16, 'tealp')}
{''.join(f'<circle cx="{440+ (i%3)*54}" cy="{120+(i//3)*54}" r="20" class="teal o"/>' for i in range(9))}
<circle cx="180" cy="160" r="22" class="coral o"/>
{arc(220, 170, 410, 150, 70, CRL, True, 5)}
<circle cx="494" cy="174" r="22" class="teal o"/>
{ring(494, 174, 34, True)}''', arrow=True)

# --- 感じる・寄る ------------------------------------------------------------

add('affinity', '二つの磁石が引き合うように、初対面の二人が自然に近づく',
    '親近感、(化学の)親和性＝affinity。', f'''
{person(190, 330, 1.05, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
{person(410, 330, 1.05, -1, 'coral', 'green', 'reach', 'bob', 'smile')}
<g transform="translate(300 150)">
  <path d="M-74 24a74 74 0 0 1 148 0h-36a38 38 0 0 0-76 0z" class="coral o"/>
  <path d="M-74 24h36v30h-36zM38 24h36v30H38z" class="ink"/></g>
{''.join(f'<path d="M{262+i*10} {236+i*8}h{76-i*20}" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(3))}''')

add('ageing', '同じ人の顔が、若いときから年を重ねた姿へ変わっていく',
    '老化、高齢化＝ageing。', f'''
{split()}
{face(160, 190, 86, 'smile')}
<g transform="translate(160 190)"><path d="M-86-18q30-70 90-60 60 10 78 60-40-30-88-24-42 6-80 24z" fill="{HAIR}"/></g>
{face(440, 190, 86, 'smile')}
<g transform="translate(440 190)"><path d="M-86-18q30-70 90-60 60 10 78 60-40-30-88-24-42 6-80 24z" fill="#d7d9dc"/>
  <path d="M-58-6q14-10 28 0M30-6q14-10 28 0M-46 40q10 8 20 2M28 42q10 8 20 2" fill="none" stroke="{SKINL}" stroke-width="3"/></g>
{arc(260, 300, 348, 300, 34, MUTED, True, 5)}
{clock(300, 350, 26, 2, 40)}''', arrow=True)

# --- 見込む・代わりに ---------------------------------------------------------

add('allow for', '箱の実寸の外に点線で余白を取り、その分まで含めて測る',
    '考慮に入れる、見込んでおく＝allow for。', f'''
{table(340)}
{box(280, 250, 200, 130, 40, 'teal')}
<path d="M120 110h380v230h-380z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
{''.join(f'<path d="M{x} 96v-34" fill="none" stroke="{MUTED}" stroke-width="3"/>' for x in (120, 500))}
<path d="M120 74h380" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round" marker-start="url(#ar)" marker-end="url(#ar)"/>
<g opacity="0.85">{ring(500, 226, 30, True)}</g>''', arrow=True)

add('alternatively', '分かれ道で、行き止まりの一本ではなく、もう一本の道を手で示す',
    'あるいは、その代わりに＝alternatively。', f'''
<path d="M300 400L250 200h100z" fill="#d8cdb6"/>
<path d="M250 200L120 60h60L300 190z" fill="#d8cdb6"/>
<path d="M250 200L470 70h60L300 192z" fill="#d8cdb6"/>
{cross(150, 90, 0.8)}
{tick(500, 100, 0.8)}
{person(300, 370, 0.95, 1, 'teal', 'blue', 'point', 'short', 'smile')}
{arc(330, 268, 430, 130, 70, MUTED, True, 4)}''', arrow=True)

# --- あいまい・議論 ----------------------------------------------------------

add('ambiguity', '一つの影が、左右どちらの形とも読めてしまう',
    'あいまいさ、両義性＝ambiguity。', f'''
<g transform="translate(300 200)">
  <path d="M-70 90q-40-70 0-130 26-40 70-40 44 0 70 40 40 60 0 130z" class="violet o"/></g>
<path d="M96 290q-36-72 4-138 24-40 62-52" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/>
<path d="M504 290q36-72-4-138-24-40-62-52" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 10"/>
{''.join(f'<g transform="translate({x} 96)"><path d="M-14-22q0-18 16-18t16 18q0 12-16 18v10" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/><circle cx="2" cy="22" r="5" fill="{CRL}"/></g>' for x in (86, 514))}''')

add('arguable', '同じ一つの主張に、賛成と反対の札が同じ数だけ並ぶ',
    '議論の余地がある＝arguable。', f'''
{doc(300, 120, 200, 130, 3)}
{''.join(f'<g transform="translate({70+i*54} 280)"><circle r="24" class="greenp o"/>{tick(0, 0, 0.45)}</g>' for i in range(3))}
{''.join(f'<g transform="translate({370+i*54} 280)"><circle r="24" class="coralp o"/>{cross(0, 0, 0.45)}</g>' for i in range(3))}
{scales(300, 246, 0, 0.42)}''')

add('argumentative', '会の中で一人だけが、どの発言にも次々と反対の札を返す',
    '理屈っぽい、議論好きの＝argumentative。', f'''
{''.join(head(120 + i * 92, 130, 26, c, h) for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('blue', 'bun'), ('gold', 'cap')]))}
{person(470, 330, 1.15, -1, 'coral', 'violet', 'point', 'short', 'sad')}
{''.join(f'<g transform="translate({{}} 240)"><circle r="22" class="coralp o"/>{{}}</g>'.format(120 + i * 92, cross(0, 0, 0.42)) for i in range(4))}
{''.join(f'<path d="M{380} {214}L{146+i*92} {240}" fill="none" stroke="{CRL}" stroke-width="3" stroke-dasharray="8 8"/>' for i in range(4))}''')

# --- 尋ねる・世話 ------------------------------------------------------------

add('ask after', '電話の向こうの相手に、寝ている家族の様子はどうかと尋ねる',
    '(人の)近況を尋ねる＝ask after。', f'''
{split()}
{person(140, 330, 1.05, 1, 'teal', 'blue', 'think', 'bob', 'smile')}
<g transform="translate(200 160)"><path d="M-50-40h100v72h-32l-14 22-8-22h-46z" fill="#fffefd" class="o"/>
  {head(0, -4, 17, 'coral', 'bun')}</g>
<g transform="translate(440 300)">
  <path d="M-110 0v-70h220v70z" fill="#fffefd" class="o"/>
  <path d="M-110-70h60v-40h-60z" class="bluep o"/>
  <path d="M-52-56q64-22 162 0v-14h-162z" class="coralp o"/>
  {head(-74, -84, 20, 'coral', 'bun')}</g>
{arc(240, 120, 400, 160, 70, MUTED, True, 4)}''', arrow=True)

add('attend to', '窓口の係が、待っていた客のほうへ体を向けて用件に対応する',
    '対応する、世話をする＝attend to。', f'''
{table(250)}
<path d="M40 60h520v190H40z" fill="none" stroke="{MUTED}" stroke-width="0"/>
<g transform="translate(160 250)">{sit(0, 0, 1.0, 1, 'teal', 'blue', 'bob', 'smile', 'lap')}</g>
{chair(150, 250, 0.9, 'gold', 1)}
{person(450, 330, 1.1, -1, 'coral', 'green', 'reach', 'short', 'smile')}
{arc(380, 210, 250, 190, 50, GRN, False, 5)}
{doc(300, 224, 84, 60, 2)}''', arrow=True)

# --- 達成・本物 --------------------------------------------------------------

add('attainable', '背伸びすれば届く高さの枝に、実際に手が届いて実をつかむ',
    '達成可能な＝attainable。', f'''
{tree(420, 330, 1.5)}
<circle cx="320" cy="180" r="22" class="coral o"/>
{person(250, 340, 1.1, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<path d="M270 228L306 190" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
{ring(320, 180, 44, True)}
{tick(150, 180, 0.8)}''')

add('authenticity', '虫めがねで印を確かめると、確かに本物の刻印が見える',
    '本物であること、真正性＝authenticity。', f'''
{table(340)}
<g transform="translate(280 250)">
  <path d="M-120-90h240v180h-240z" fill="#fffefd" class="o"/>
  <circle cx="-30" cy="10" r="46" class="goldp o"/>
  <circle cx="-30" cy="10" r="30" fill="none" stroke="{GLDD}" stroke-width="4"/>
  <path d="M-44 10l10 12 22-26" fill="none" stroke="{GLDD}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  {''.join(f'<rect x="40" y="{-60+i*30}" width="{70-i*16}" height="9" rx="4.5" fill="{MUTED}"/>' for i in range(3))}</g>
<g transform="translate(250 260) rotate(24)">
  <circle r="86" fill="#ffffff" fill-opacity="0.28" stroke="{INK}" stroke-width="7"/>
  <path d="M60 60l70 70" stroke="{BRN}" stroke-width="22" stroke-linecap="round" fill="none"/></g>''')

# --- 自動化 ------------------------------------------------------------------

add('automate', '手で一つずつ運んでいた作業が、ベルトコンベアの流れ作業に置き換わる',
    '自動化する＝automate。', f'''
{split()}
{person(150, 320, 1.0, 1, 'teal', 'blue', 'carry', 'short', 'sad')}
{box(220, 240, 60, 48, 16, 'gold')}
<g opacity="0.4">{person(60, 320, 0.8, 1, 'teal', 'blue', 'carry', 'bob', 'flat')}</g>
<g transform="translate(440 280)">
  <path d="M-130 0h260v26h-260z" class="ink"/>
  {''.join(f'<circle cx="{-110+i*44}" cy="13" r="13" fill="#fffefd" stroke="{INK}" stroke-width="2.5"/>' for i in range(6))}</g>
{''.join(box(360 + i * 80, 258, 58, 44, 14, 'gold') for i in range(3))}
<g transform="translate(440 150)">
  <path d="M-70 0h140v46h-140z" class="teal o"/>
  <path d="M0 46v40" fill="none" stroke="{TEAD}" stroke-width="10"/>
  <circle cx="-32" cy="22" r="8" class="goldp o"/><circle cx="32" cy="22" r="8" class="goldp o"/></g>
{arc(250, 190, 370, 130, 60, MUTED, True, 4)}''', arrow=True)

add('automation', '人のいない工場で、ロボットアームがベルトの上の箱を並べ続ける',
    '自動化＝automation。', f'''
<g transform="translate(300 300)">
  <path d="M-250 0h500v30h-250z" fill="none"/>
  <path d="M-250 0h500v30h-500z" class="ink"/>
  {''.join(f'<circle cx="{-228+i*46}" cy="15" r="14" fill="#fffefd" stroke="{INK}" stroke-width="2.5"/>' for i in range(11))}</g>
{''.join(box(110 + i * 96, 276, 64, 46, 16, 'gold') for i in range(5))}
{''.join(f'<g transform="translate({{}} 120)"><path d="M0 0v60" stroke="{TEAD}" stroke-width="14" fill="none" stroke-linecap="round"/><path d="M0 0l-56-46" stroke="{TEA}" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M-56-46l-10 34" stroke="{TEAD}" stroke-width="12" fill="none" stroke-linecap="round"/><circle r="12" class="goldp o"/></g>'.format(x) for x in (200, 420))}
{''.join(f'<path d="M{{}} 92q14-16 28 0" fill="none" stroke="{MUTED}" stroke-width="3"/>'.format(x) for x in (150, 370))}''')

# --- 独身・譲る --------------------------------------------------------------

add('bachelor', '一人分の食器と一つのいすだけが置かれた食卓に、指輪のない男性がつく',
    '独身男性、学士＝bachelor。', f'''
{table(280)}
{chair(300, 280, 1.0, 'gold', 1)}
{sit(300, 280, 1.05, 1, 'blue', 'green', 'short', 'smile', 'lap')}
<g transform="translate(300 272)">
  <ellipse rx="62" ry="18" fill="#fffefd" class="o"/>
  <ellipse rx="34" ry="9" fill="none" stroke="{MUTED}" stroke-width="2.5"/></g>
<g opacity="0.3">{chair(500, 280, 1.0, 'gold', -1)}</g>
{ring(500, 220, 46, True)}
{hand(150, 250, 1)}
<circle cx="150" cy="250" r="0" fill="none"/>''')

add('back down', '向き合っていた二人のうち、片方が上げた手を下ろして一歩下がる',
    '主張を引っこめる、譲歩する＝back down。', f'''
{person(210, 330, 1.15, 1, 'coral', 'blue', 'up', 'short', 'flat')}
{person(430, 330, 1.15, -1, 'teal', 'green', 'stand', 'bob', 'sad')}
<g opacity="0.35">{person(380, 330, 1.15, -1, 'teal', 'green', 'up', 'bob', 'flat')}</g>
{arc(392, 200, 456, 212, 40, MUTED, True, 4)}
{''.join(f'<path d="M{460+i*22} 350h16" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''', arrow=True)

# --- 救済・あてにする ---------------------------------------------------------

add('bail out', '沈みかけた船に、コインの模様がついた浮き輪が投げ入れられる',
    '(資金を出して)救済する＝bail out。', f'''
<path d="M0 250h600v150H0z" class="bluep"/>
{''.join(f'<path d="M{i*80} 258q20-14 40 0t40 0" fill="none" stroke="{BLU}" stroke-width="4"/>' for i in range(8))}
<g transform="translate(250 250) rotate(18)">
  <path d="M-120 0h240l-40 60h-160z" class="coral o"/>
  <path d="M-20 0v-120h100l-90 40" fill="{GLDP}" class="o"/></g>
<g transform="translate(450 210)">
  <circle r="60" class="gold o"/><circle r="30" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
  {''.join(f'<path d="M{-60*math.cos(math.radians(a)):.0f} {-60*math.sin(math.radians(a)):.0f}l{-14*math.cos(math.radians(a)):.0f} {-14*math.sin(math.radians(a)):.0f}" stroke="#fffefd" stroke-width="0" fill="none"/>' for a in (0,))}</g>
{arc(500, 130, 330, 180, 90, MUTED, True, 5)}''', arrow=True)

add('bank on', '人が一本のロープだけに全体重を預けてぶら下がる',
    'あてにする、当てこむ＝bank on。', f'''
<path d="M300 0v150" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
<path d="M300 150q-8 40 0 60" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
{person(300, 340, 1.25, 1, 'teal', 'blue', 'up', 'short', 'flat')}
<path d="M60 350h480" fill="none" stroke="{MUTED}" stroke-width="0"/>
{ring(300, 80, 44, True)}
{''.join(f'<path d="M{150+i*220} 330q0-60 40-90" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>' for i in range(2))}''')

add('barge in', '会議室のドアを勢いよく押し開け、話の途中に人が飛び込んでくる',
    'どかどか入り込む、割り込む＝barge in。', f'''
{table(280)}
{''.join(sit(180 + i * 110, 280, 0.92, 1, c, 'blue', h, 'flat') for i, (c, h) in enumerate([('teal', 'short'), ('green', 'bob'), ('gold', 'bun')]))}
{''.join(chair(174 + i * 110, 280, 0.85, 'gold', 1) for i in range(3))}
<g transform="translate(520 306)">
  <path d="M-16 0v-240h16v240z" fill="{MUTED}"/>
  <path d="M0-236l70-24v268l-70-16z" fill="#e8ddc9" class="o" transform="rotate(-16 0 -100)"/></g>
{person(430, 330, 1.15, -1, 'coral', 'violet', 'walk', 'short', 'flat')}
{''.join(f'<path d="M{494+i*18} {150+i*22}q14 10 0 22" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}''')

# --- 法・裏づけ・方位 ---------------------------------------------------------

add('barrister', '白いかつらと黒いガウンの弁護士が、法廷で立って話す',
    '法廷弁護士(英)＝barrister。', f'''
<path d="M0 60h600v246H0z" fill="#f4ead9"/>
{table(300)}
<g transform="translate(300 306)">
  <path d="M-70 0v-150q70-30 140 0V0z" fill="#2f3542" class="o"/>
  <path d="M-24-150q24 26 48 0l-16 60h-16z" fill="#fffefd" class="o"/>
  <circle cx="0" cy="-186" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-32-192q0-34 32-34t32 34q0 16-10 24 6 14-8 18h-28q-14-4-8-18-10-8-10-24z" fill="#f2f2f0" class="o"/>
  <circle cx="-9" cy="-188" r="2.4" class="ink"/><circle cx="9" cy="-188" r="2.4" class="ink"/>
  <path d="M-7-176h14" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M-70-150l-34 70M70-150l34 70" fill="none" stroke="#2f3542" stroke-width="14" stroke-linecap="round"/></g>
{doc(470, 240, 110, 140, 3)}
<g transform="translate(110 250)"><path d="M-40 40h80v14h-80z" fill="{BRN}" class="o"/>
  <path d="M-10 40v-46h20v46z" fill="{BRN}"/><path d="M-46-6h92l-46-34z" fill="{BRN}" class="o"/></g>''')

add('bear out', '実測の折れ線が、先に引いた点線の予測とぴたり重なる',
    '(説を)裏づける、証明する＝bear out。', f'''
<path d="M80 320h440M80 320V70" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<path d="M110 280L200 220 290 190 380 130 470 96" fill="none" stroke="{MUTED}" stroke-width="7" stroke-dasharray="12 11" stroke-linecap="round"/>
<path d="M110 286L200 226 290 196 380 136 470 102" fill="none" stroke="{TEA}" stroke-width="6" stroke-linecap="round"/>
{''.join(f'<circle cx="{110+i*90}" cy="{286-i*[0,60,90,150,184][0] if False else [286,226,196,136,102][i]}" r="8" class="teal o"/>' for i in range(5))}
{tick(500, 200, 0.9)}''')

add('bearing', '羅針盤の針が示す方角を、地図の上で読み取る',
    '方位、関係・影響＝bearing。', f'''
{table(330)}
<g transform="translate(300 200)">
  <circle r="120" fill="#fffefd" class="o"/>
  <circle r="100" fill="none" stroke="{MUTED}" stroke-width="3"/>
  {''.join(f'<path d="M0-100v-14" transform="rotate({a})" stroke="{MUTED}" stroke-width="4" fill="none"/>' for a in range(0, 360, 30))}
  <path d="M0-88L20 0 0 26-20 0z" class="coral o"/>
  <path d="M0 88L20 0-20 0z" fill="#fffefd" class="o"/>
  <circle r="9" class="ink"/></g>
<g transform="translate(300 60)"><path d="M-12 14L0-16l12 30" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/></g>''')

# --- 良性・多様・過ぎ去る -----------------------------------------------------

add('benign', '診察の画面に映った丸い影を指して、医師が穏やかに問題なしと伝える',
    '(腫瘍が)良性の、穏やかな＝benign。', f'''
<g transform="translate(200 190)">
  <path d="M-130-110h260v220h-260z" fill="#eef4f7" class="o"/>
  <ellipse rx="66" ry="86" fill="#dfe9ee" stroke="{MUTED}" stroke-width="3"/>
  <circle cx="12" cy="6" r="28" class="tealp o"/>
  {ring(12, 6, 44, True)}</g>
{person(460, 330, 1.15, -1, 'teal', 'blue', 'point', 'bun', 'smile')}
<g transform="translate(470 120)"><path d="M-56-34h112v58h-40l-16 20-8-20h-48z" fill="#fffefd" class="o"/>
  {tick(0, -6, 0.5)}</g>''')

add('biodiversity', 'ひとつの森に、木も花も鳥も蝶も魚も別々の種類がそろっている',
    '生物多様性＝biodiversity。', f'''
<path d="M0 300h600v100H0z" class="greenp"/>
<path d="M60 320q110-50 220 0t250 10v70H60z" class="bluep o"/>
{tree(120, 306, 1.25)}{tree(250, 300, 0.95)}{tree(520, 306, 1.1)}
{flower(330, 330, 0.85, 'coral')}{flower(390, 336, 0.75, 'violet')}{flower(180, 340, 0.7, 'gold')}
<g transform="translate(420 130)"><path d="M-30 0q-24-30 0-40 16-6 24 10 8-16 24-10 24 10 0 40-24 20-48 0z" class="coral o"/>
  <path d="M0-30v40" fill="none" stroke="{INK}" stroke-width="3"/></g>
<g transform="translate(150 140)"><ellipse rx="30" ry="20" class="gold o"/><circle cx="26" cy="-12" r="13" class="gold o"/>
  <path d="M36-16l16 4-16 6z" class="corald o"/><circle cx="30" cy="-14" r="2.6" class="ink"/>
  <path d="M-30 0l-30-10 24 24z" class="goldd o"/></g>
<g transform="translate(300 356)"><ellipse rx="40" ry="20" class="teal o"/><path d="M40 0l30-18v36z" class="teald o"/>
  <circle cx="-22" cy="-5" r="3" class="ink"/></g>''')

add('blow over', '横切っていった嵐の雲が向こうへ流れ、あとには晴れ間が広がる',
    '(騒ぎが)おさまる、過ぎ去る＝blow over。', f'''
{sun(130, 110, 50)}
<g opacity="0.45">{cloud(250, 130, 1.1, 'violet')}</g>
{cloud(460, 120, 1.4, 'violet')}
{''.join(f'<path d="M{430+i*20} {180+i*16}l-14 26h20l-16 30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>' for i in range(2))}
{arc(210, 200, 430, 190, 80, MUTED, True, 5)}
{house(300, 330, 0.95, 'coral')}
{tick(140, 240, 0.8)}''', arrow=True)

add('bluntness', 'オブラートに包まず、太い直線の矢印がそのまま相手に届いて相手が驚く',
    '無遠慮さ、率直さ＝bluntness。', f'''
{person(140, 330, 1.15, 1, 'teal', 'blue', 'point', 'short', 'flat')}
{person(470, 330, 1.15, -1, 'coral', 'green', 'stand', 'bob', 'sad')}
<path d="M210 170h190" fill="none" stroke="{INK}" stroke-width="16" stroke-linecap="round" marker-end="url(#ar)"/>
<g opacity="0.32"><path d="M210 230q60-50 120 0t80-10" fill="none" stroke="{MUTED}" stroke-width="8" stroke-dasharray="12 11"/></g>
{''.join(f'<path d="M{490+i*16} {138-i*10}l10-16" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}''', arrow=True)

# --- 煮詰まる・底を打つ -------------------------------------------------------

add('boil down to', '大鍋いっぱいの汁を煮詰めると、残るのは小さじ一杯だけになる',
    '結局〜ということになる＝boil down to。', f'''
{table(330)}
<g transform="translate(160 260)">
  <path d="M-90-50h180v76a30 30 0 0 1-30 30h-120a30 30 0 0 1-30-30z" fill="#cfd6db" class="o"/>
  <path d="M-90-50h180" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-80-38h160v40a24 24 0 0 1-24 24h-112a24 24 0 0 1-24-24z" class="goldp"/>
  <path d="M-110-50h20M90-50h20" stroke="{INK}" stroke-width="7" stroke-linecap="round" fill="none"/></g>
{''.join(f'<path d="M{120+i*40} 180q14-24 0-44" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}
{arc(280, 230, 420, 250, 70, MUTED, True, 5)}
<g transform="translate(470 280)">
  <ellipse rx="44" ry="16" fill="#cfd6db" class="o"/>
  <ellipse rx="30" ry="9" class="goldp"/>
  <path d="M40 4l70-34" stroke="#cfd6db" stroke-width="10" stroke-linecap="round" fill="none"/></g>''', arrow=True)

add('bottom out', '下がり続けていた折れ線が、いちばん下で止まって横ばいになる',
    '底を打つ、下げ止まる＝bottom out。', f'''
<path d="M70 340h470M70 340V60" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<path d="M100 100L180 180 250 250 320 290" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M320 290h180" fill="none" stroke="{GRN}" stroke-width="7" stroke-linecap="round"/>
<path d="M70 290h460" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="11 10"/>
<circle cx="320" cy="290" r="12" class="green o"/>
{ring(320, 290, 34, True)}''')

# --- 離れる・断つ・繰り上げ ---------------------------------------------------

add('break away', 'つながって進む列から、一人だけが線を切って横へ飛び出す',
    '離脱する、振り切って逃げる＝break away。', f'''
{''.join(f'<g>{{}}</g>'.format(head(100 + i * 80, 260, 26, 'teal', 'short')) for i in range(4))}
<path d="M126 260h188" fill="none" stroke="{TEA}" stroke-width="6"/>
<path d="M346 260h30" fill="none" stroke="{TEA}" stroke-width="6" stroke-dasharray="8 10"/>
{''.join(f'<path d="M{388+i*8} {248+i*6}l14 16" fill="none" stroke="{CRL}" stroke-width="4"/>' for i in range(2))}
{head(470, 150, 30, 'coral', 'bob')}
{arc(400, 250, 452, 180, 40, CRL, True, 5)}''', arrow=True)

add('break off', '握手していた二本の手が離れ、間をつないでいた線が途中で切れる',
    '急にやめる、(関係を)断つ＝break off。', f'''
{hand(160, 190, 1)}
{hand(440, 190, -1)}
<path d="M210 190h60" fill="none" stroke="{TEA}" stroke-width="9" stroke-linecap="round"/>
<path d="M330 190h60" fill="none" stroke="{TEA}" stroke-width="9" stroke-linecap="round"/>
{''.join(f'<path d="M{286+i*14} {166+i*10}l{12-i*4} {16}" fill="none" stroke="{CRL}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
{person(120, 350, 0.8, -1, 'teal', 'blue', 'stand', 'short', 'sad')}
{person(480, 350, 0.8, 1, 'coral', 'green', 'stand', 'bob', 'sad')}''')

add('bring forward', 'カレンダーに留めた予定の札が、右のマスから左のマスへ動く',
    '(日程を)繰り上げる＝bring forward。', f'''
<g transform="translate(300 210)">
  <path d="M-240-130h480v280h-480z" fill="#fffefd" class="o"/>
  <path d="M-240-130h480v52h-480z" class="teal o"/>
  {''.join(f'<path d="M{-240+c*96} -78v228" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for c in range(1, 5))}
  {''.join(f'<path d="M-240 {-78+r*76}h480" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for r in range(1, 3))}</g>
<g opacity="0.3"><rect x="360" y="200" width="72" height="48" rx="8" class="coral o"/></g>
<rect x="168" y="200" width="72" height="48" rx="8" class="coral o"/>
{arc(360, 190, 246, 190, 56, CRL, True, 5)}''', arrow=True)

add('brush aside', '差し出された紙束を、手の甲でさっと横へ払いのける',
    '(意見を)軽くはねつける＝brush aside。', f'''
{person(150, 340, 1.05, 1, 'teal', 'blue', 'give', 'bob', 'sad')}
{doc(250, 200, 90, 116, 3)}
{hand(350, 190, -1)}
{arc(330, 150, 470, 120, 50, CRL, False, 6)}
<g transform="translate(490 190) rotate(28)">{doc(0, 0, 84, 108, 3)}</g>
<g transform="translate(540 260) rotate(-16)" opacity="0.6">{doc(0, 0, 76, 96, 3)}</g>
{person(430, 340, 1.15, -1, 'coral', 'green', 'reach', 'short', 'flat')}''', arrow=True)

# --- 燃え尽き・買い取り・率直 -------------------------------------------------

add('burn out', '溶けきったろうそくから細い煙だけが上がり、その前で人が机に力尽きる',
    '燃え尽きる、働きすぎて動けなくなる＝burn out。', f'''
{table(300)}
<g transform="translate(440 300)">
  <path d="M-34 0q-4-40 0-56h68q4 16 0 56z" fill="#f0e6d2" class="o"/>
  <path d="M0-56v-16" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M0-76q16-20 0-36-14 22-26 4 0 22 26 32z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
  <path d="M0-96q-14-26 6-46" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/></g>
<g transform="translate(200 300)">
  <path d="M-70 0v-46q70-26 140 0V0z" class="teal o"/>
  <path d="M-70-46l-46 34M70-46l50 30" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="10" cy="-62" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5" transform="rotate(24 10 -62)"/>
  <path d="M-18-84q6-30 34-30 26 0 30 28-16-12-32-4-14-10-32 6z" fill="{HAIR}" transform="rotate(24 10 -62)"/>
  <path d="M-1-56l12 2" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-4-68l10 4M16-72l10 6" fill="none" stroke="{INK}" stroke-width="2.5"/></g>''')

add('buy out', '半分ずつだった持ち分の片方をコインで買い取り、円がひとりの色になる',
    '(持ち分を)買い取る＝buy out。', f'''
{split()}
<g transform="translate(160 200)">
  <circle r="96" fill="#fffefd" class="o"/>
  <path d="M0-96A96 96 0 0 1 0 96z" class="teal o"/>
  <path d="M0 96A96 96 0 0 1 0-96z" class="coral o"/></g>
<g transform="translate(440 200)"><circle r="96" class="teal o"/></g>
{arc(270, 190, 336, 190, 44, MUTED, True, 5)}
{''.join(coin(276 + i * 26, 300, 17) for i in range(3))}
{arc(300, 320, 430, 300, 40, GLDD, True, 4)}''', arrow=True)

add('candid', '胸の箱のふたを自分から開けて、中身をそのまま相手に見せる',
    '率直な、包み隠さない＝candid。', f'''
{person(180, 340, 1.2, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(300 210)">
  <path d="M-70-10h140v90h-140z" class="goldp o"/>
  <path d="M-76-10h152" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-76-12l14-58h124l14 58z" class="gold o" transform="rotate(-22 -76 -12)"/></g>
{''.join(spark(280 + i * 34, 120 - (i % 2) * 24, 0.9, 'gold') for i in range(3))}
{person(470, 340, 1.05, -1, 'coral', 'green', 'stand', 'bob', 'smile')}''')


# --- 責任・消毒・見習い -------------------------------------------------------

add('answer for', '割れた窓の前に立った人が、自分の胸を指して自分の行いだと認める',
    '(行いの)責任を負う＝answer for。', f'''
<g transform="translate(430 180)">
  <path d="M-100-110h200v220h-200z" fill="#eaf1f6" class="o"/>
  <path d="M-100-110l92 86-72 58 80 76M100-110l-96 94 92 58-46 68" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-6-14l42-22-32 44 38 8" fill="none" stroke="{INK}" stroke-width="3"/></g>
{person(170, 340, 1.2, 1, 'coral', 'blue', 'hold', 'short', 'sad')}
<circle cx="170" cy="212" r="9" class="ink"/>
{arc(200, 240, 320, 200, 50, MUTED, True, 4)}''', arrow=True)

add('antiseptic', 'ひじの傷に消毒薬をかけると、菌の点が消えていく',
    '消毒薬、消毒性の＝antiseptic。', f'''
<g transform="translate(240 220)">
  <path d="M-150 60q40-120 150-140 110-20 170 40" fill="none" stroke="{SKIN}" stroke-width="66" stroke-linecap="round"/>
  <path d="M-150 60q40-120 150-140 110-20 170 40" fill="none" stroke="{SKINL}" stroke-width="2.5" opacity="0"/>
  <path d="M30-70q26 16 10 40-18 24-44 6" fill="{CRLP}" stroke="{CRL}" stroke-width="4"/></g>
<g transform="translate(430 110) rotate(26)">
  <path d="M-28-80h56v120a22 22 0 0 1-22 22h-12a22 22 0 0 1-22-22z" class="tealp o"/>
  <path d="M-13-102h26v22h-26z" class="teald o"/></g>
{''.join(drop(300 - i * 22, 150 + i * 26, 1.1, 'teal') for i in range(3))}
{''.join(f'<circle cx="{160+i*30}" cy="{300+(i%2)*22}" r="7" fill="{MUTED}" opacity="{0.7-i*0.15:.2f}"/>' for i in range(4))}
{cross(120, 320, 0.55)}''')

add('apprenticeship', '親方の手つきを横で見ながら、見習いが同じ道具で同じ作業をする',
    '徒弟制度、見習い期間＝apprenticeship。', f'''
{table(300)}
{person(180, 300, 1.15, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
{person(400, 300, 0.95, 1, 'coral', 'green', 'hold', 'cap', 'smile')}
<g transform="translate(226 226) rotate(-18)"><path d="M-8-40h16v52h-16z" fill="{BRN}" class="o"/>
  <path d="M-24 12h48v22h-48z" fill="{MUTED}" class="o"/></g>
<g transform="translate(438 238) rotate(-18)"><path d="M-7-34h14v44h-14z" fill="{BRN}" class="o"/>
  <path d="M-20 10h40v18h-20z" fill="{MUTED}" class="o"/><path d="M-20 10h40v18h-40z" fill="{MUTED}" class="o"/></g>
{''.join(f'<path d="M{150+i*26} 290h18" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/>' for i in range(2))}
{arc(300, 170, 386, 190, 40, MUTED, True, 4)}
<g transform="translate(300 130)"><path d="M-26-10q0-16 14-16t12 16" fill="none" stroke="{MUTED}" stroke-width="0"/></g>''', arrow=True)

finish(__file__)
