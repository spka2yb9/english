# -*- coding: utf-8 -*-
"""第192回: plus41 の100語(candy〜sardine)。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *

# --- この回で使う小物 ---------------------------------------------------------

def snow(x, y, s=1, c='#8fc0e8'):
    return (f'<g transform="translate({x} {y})" fill="none" stroke="{c}" stroke-width="{3*s}" stroke-linecap="round">'
            + ''.join(f'<path d="M0 {-16*s}v{32*s}" transform="rotate({d})"/>' for d in (0, 60, 120))
            + ''.join(f'<path d="M0 {-15*s}l{-6*s} {7*s}M0 {-15*s}l{6*s} {7*s}" transform="rotate({d})"/>'
                      for d in (0, 60, 120, 180, 240, 300)) + '</g>')

def tshirt(x, y, s=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-32-40l-28 16 12 24 16-8v62h64v-62l16 8 12-24-28-16q-32 20-64 0z" class="{cls} o"/></g>')

def hanger(x, y, s=1, cls='gold'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0-58q0-18 16-18t16 18" fill="none" stroke="{MUTED}" stroke-width="5"/>'
            f'<path d="M-44 14L0-46l44 60z" fill="none" stroke="{TONES[cls][0]}" stroke-width="7" stroke-linejoin="round"/></g>')

def heart(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 10C-6 0-22-8-30 2-38 12-30 26-18 34'
            f'-10 39-4 44 0 50 4 44 10 39 18 34 30 26 38 12 30 2 22-8 6 0 0 10z" class="{cls} o"/></g>')

def star(x, y, r=26, cls='gold'):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.44
        a = math.radians(-90 + i * 36)
        pts.append(f'{x+rr*math.cos(a):.0f} {y+rr*math.sin(a):.0f}')
    return f'<path d="M{"L".join(pts)}z" class="{cls} o"/>'

def door(x, y, w=130, h=210, cls='teal', open=0):
    """(x,y)は敷居の左端。open>0 で右へ開いた扉。"""
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M-12 0h{w+24}v-{h+12}H-12z" fill="#f6efe2" class="o"/>'
            f'<path d="M-12 0h{w+24}v-{h+12}H-12z" fill="none" class="a"/>'
            f'<g transform="rotate({open} 0 0)">'
            f'<path d="M0 0h{w}v-{h}H0z" fill="#fffdf6" class="{cls} o"/>'
            f'<path d="M0 0h{w}v-{h}H0z" fill="none" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="{w-20}" cy="{-h*0.45:.0f}" r="7" class="ink"/></g></g>')

def mug(x, y, s=1, cls='teal', liquid=None):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-34-40h68v46a24 24 0 0 1-24 24h-20a24 24 0 0 1-24-24z" fill="#fffefd" class="o"/>'
            + (f'<path d="M-30-34h60v40a20 20 0 0 1-20 20h-20a20 20 0 0 1-20-20z" fill="{liquid}"/>' if liquid else '')
            + f'<path d="M34-28q26 0 26 22t-26 22" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/></g>')

def steam(x, y, s=1, c=None):
    return ''.join(f'<path d="M{x+i*26*s} {y}q{10*s}-{14*s} 0-{28*s}t0-{28*s}" fill="none" '
                   f'stroke="{c or MUTED}" stroke-width="{4*s}" stroke-linecap="round"/>' for i in range(2))

def ball(x, y, r=36, cls='teal'):
    return (f'<g transform="translate({x} {y})"><circle r="{r}" fill="#fffdf6" class="o"/>'
            f'<path d="M0 {-r}l{r*0.6} {r*0.44}-{r*0.37} {r*0.76}h-{r*0.46}l-{r*0.37}-{r*0.76}z" class="{cls} o"/>'
            f'<path d="M0 {-r}v{r*0.3}M{-r*0.97} {-r*0.28}l{r*0.6} {r*0.58}M{r*0.97} {-r*0.28}l-{r*0.6} {r*0.58}" '
            f'fill="none" stroke="{INK}" stroke-width="3"/></g>')

def girl(x, y, s=1, shirt='coral', hair='bob', cls='coral', mood='smile'):
    return (person(x, y, s, 1, shirt, 'coral', 'stand', hair, mood)
            + f'<g transform="translate({x} {y}) scale({s})"><path d="M-28-36h56l30 50h-116z" class="{cls}p o"/></g>')

def bike(x, y, s=1, cls='teal', rot=0):
    """(x,y)は車輪の中心。"""
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({rot})">'
            f'<circle cx="-72" cy="0" r="42" fill="#fffdf6" class="o"/>'
            f'<circle cx="72" cy="0" r="42" fill="#fffdf6" class="o"/>'
            f'<circle cx="-72" cy="0" r="7" class="ink"/><circle cx="72" cy="0" r="7" class="ink"/>'
            f'<path d="M-72 0L0 0 40-62-36-62z" fill="none" stroke="{TONES[cls][0]}" stroke-width="8" stroke-linejoin="round"/>'
            f'<path d="M40-62L72 0" fill="none" stroke="{TONES[cls][0]}" stroke-width="8"/>'
            f'<path d="M-48-70h24M28-74h22" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
            f'<circle cx="0" cy="0" r="9" fill="{MUTED}" class="o"/></g>')

def rider(x, y, s=1, rot=0, shirt='coral', cls='teal'):
    """自転車と乗っている人。(x,y)は車輪の中心。"""
    return bike(x, y, s, cls, rot) + person(x - 34 * s, y - 46 * s, 0.82 * s, 1, shirt, 'blue', 'hold', 'cap', 'smile')

def web(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{MUTED}" stroke-width="2.5">'
            f'<path d="M0 0h96M0 0l86 42M0 0l86-42M0 0l60 76"/>'
            + ''.join(f'<path d="M{a} {b}q{14} {18} {6} {36}" />' for a, b in ((28, 14), (52, 26), (74, 38)))
            + '</g>')

def girl2(x, y, s=1, shirt='violet', hair='bun', mood='smile'):
    return person(x, y, s, 1, shirt, 'blue', 'stand', hair, mood)

def tube(x, y, s=1, cls='teal', rot=0):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({rot})">'
            f'<path d="M-58-18h92v36h-92z" fill="#fffdf6" class="o"/>'
            f'<path d="M-58-18h18v36h-18z" class="{cls} o"/>'
            f'<path d="M34-18l26 18-26 18z" fill="#8a97a3" class="o"/>'
            f'<path d="M56-6h22v12H56z" fill="#8a97a3" class="o"/></g>')

def blob(x, y, s=1, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-46 0q0-26 24-26 30 0 30 18 0-12 24-12 24 0 24 20 0 22-26 22h-52q-24 0-24-22z" '
            f'class="{cls} o"/></g>')

TABS = ['teal', 'coral', 'gold', 'blue', 'violet', 'green']

def broom(x, y, s=1, rot=0):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({rot})">'
            f'<path d="M-6-110h12v112h-12z" fill="#8b6437" class="o"/>'
            f'<path d="M-18 2h36v16h-36z" fill="#8a97a3" class="o"/>'
            f'<path d="M-34 18h68l-10 50h-48z" fill="#d9b96a" class="o"/>'
            f'<path d="M-26 22v44M-9 22v46M9 22v46M26 22v44" fill="none" stroke="#b08a3a" stroke-width="3"/></g>')

def fork(x, y, s=1, rot=0):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({rot})">'
            f'<path d="M-6 0h12v92h-12z" fill="#c3cbd1" class="o"/>'
            f'<path d="M-22-40h44v34h-44z" fill="#c3cbd1" class="o"/>'
            f'<path d="M-18-58h7v20h-7zM-4-58h7v20h-7zM10-58h7v20h-7z" fill="#c3cbd1" class="o"/></g>')

def knife(x, y, s=1, rot=0):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({rot})">'
            f'<path d="M-7 0h14v92h-14z" fill="#c3cbd1" class="o"/>'
            f'<path d="M-13-64h26v44q0 14-13 14t-13-14z" fill="#c3cbd1" class="o"/></g>')

def apple(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0q-32-6-32 24 0 34 32 42 32-8 32-42 0-30-32-24z" class="{cls} o"/>'
            f'<path d="M0 0q0-18 13-24" fill="none" stroke="#6b4a2a" stroke-width="5"/>'
            f'<path d="M13-24q22-10 26 8-22 10-26-8z" class="green o"/></g>')

def puff(x, y, s=1, c='#c9d2d8'):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="{c}">'
            f'<circle cx="-30" cy="0" r="22"/><circle cx="0" cy="-16" r="26"/><circle cx="30" cy="2" r="20"/></g>')

def fish(x, y, s=1, cls='blue', flip=1):
    return (f'<g transform="translate({x} {y}) scale({s*flip} {s})">'
            f'<path d="M76 0l54-32v64z" class="{cls} o"/>'
            f'<ellipse rx="80" ry="34" class="{cls} o"/>'
            f'<path d="M-14-32q18-24 40-8" fill="none" stroke="{INK}" stroke-width="2.5"/>'
            f'<path d="M-26-30q-12 30 0 60" fill="none" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="-46" cy="-8" r="6" class="ink"/></g>')

# --- 語 ----------------------------------------------------------------------

add('candy', '両端をひねった包み紙のキャンディーが中央に置かれている',
    'キャンディー＝candy。砂糖を煮固めた菓子で、英国では sweets とも言う。', f'''
<g transform="translate(300, 230)">
  <path d="M-58-34l-72-34v136l72-34z" class="coralp o"/>
  <path d="M58-34l72-34v136l-72-34z" class="coralp o"/>
  <ellipse rx="60" ry="44" class="coral o"/>
  <path d="M-22-40q12 40 0 80M0-44q12 44 0 88M22-40q12 40 0 80" fill="none" stroke="#fffdf6" stroke-width="7"/>
</g>
{spark(170, 120, 1.6)}
{spark(440, 320, 1.3)}''')

add('cannot', '閉じたドアの前に立ち、手をのばす人と、取っ手の上に出た禁止の印',
    '〜できない＝cannot。can と not を1語にした形で、話しことばでは can\'t。', f'''
{door(380, 356, 130, 210, 'teal', 0)}
{ban(462, 262, 50)}
{person(170, 356, 1.15, 1, 'coral', 'blue', 'reach', 'short', 'sad')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"><path d="M250 300q60 30 110 4"/></g>
<path d="M380 356v-220" class="a"/>''')

add('capital', '建物の並ぶ街で、中央のいちばん高い塔に旗が立ち、その上に星が光る',
    '首都＝capital。国や州の中心となる都市。大文字の意味でも使う。', f'''
{building(140, 330, 0.7, 'teal')}
{building(470, 330, 0.62, 'blue')}
{tower(300, 330, 0.9, 'coral', 4)}
<path d="M300 212v-44h54l-16 22 16 22z" class="gold o"/>
{star(300, 138, 32)}
<path d="M60 340h480" class="a"/>''')

add('car', '道路に止まった乗用車を横から見たところ',
    '車、自動車＝car。', f'''
<g transform="translate(300, 250)">
  <path d="M-176-26h352v62a22 22 0 0 1-22 22h-308a22 22 0 0 1-22-22z" class="teal o"/>
  <path d="M-86-26l36-58h86l42 58z" class="tealp o"/>
  <path d="M-76-34l28-42h30v42z" fill="#fffdf6" class="o"/>
  <path d="M10-76h26l30 42H10z" fill="#fffdf6" class="o"/>
  <path d="M-176-14h352" fill="none" stroke="{TEAD}" stroke-width="3"/>
  <circle cx="-106" cy="38" r="34" fill="#3a4756" class="o"/><circle cx="106" cy="38" r="34" fill="#3a4756" class="o"/>
  <circle cx="-106" cy="38" r="13" fill="#c3cbd1"/><circle cx="106" cy="38" r="13" fill="#c3cbd1"/>
  <path d="M-176-16h24" stroke="{GLD}" stroke-width="10" stroke-linecap="round" fill="none"/>
</g>''')

add('card', '開いた状態で立てたカードの表にハートが描かれている',
    'カード＝card。はがきやトランプの札の意味もある。', f'''
<g transform="translate(300, 340)">
  <path d="M0-220l-116 34v188L0-32z" fill="#fffefd" class="o"/>
  <path d="M0-220l116 34v188L0-32z" fill="#fffdf6" class="o"/>
  <path d="M0-220l-116 34v188L0-32z" fill="none" class="a"/>
</g>
{heart(222, 190, 1.1)}
{spark(400, 160, 1.5)}
{spark(160, 120, 1.2)}''')

add('cardboard', '茶色の段ボール箱が二つ積んであり、上の箱が少し開いている',
    '厚紙、段ボール＝cardboard。', f'''
{box(250, 330, 160, 100, 30)}
{box(300, 214, 120, 92, 26)}
<path d="M300 168v92" fill="none" stroke="#a0764a" stroke-width="3"/>
<path d="M250 280v100" fill="none" stroke="#a0764a" stroke-width="3"/>
<g transform="translate(300, 190) rotate(-8)">
  <path d="M-60-8h120v16h-120z" fill="#e0cba8" class="o"/>
</g>
<path d="M70 380h460" class="a"/>''')

add('carnival', '観覧車の上に色とりどりの旗が並び、遊園地のにぎわいが見える',
    'カーニバル、移動遊園地＝carnival。', f'''
<path d="M30 34h540" class="a"/>
{''.join(f'<path d="M{44+i*62} 34h50l-25 36z" class="{"coral" if i%2==0 else "gold"} o"/>' for i in range(8))}
<g transform="translate(290, 230)">
  <path d="M-58 0L0 150M58 0L0 150" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <circle r="132" fill="none" stroke="{TEAD}" stroke-width="8"/>
  <circle r="132" fill="none" stroke="{TEA}" stroke-width="8"/>
  {''.join(f'<path d="M0 0L{132*math.cos(math.radians(a)):.0f} {132*math.sin(math.radians(a)):.0f}" fill="none" stroke="{MUTED}" stroke-width="3"/>' for a in range(0, 360, 45))}
  {''.join(f'<circle cx="{132*math.cos(math.radians(a)):.0f}" cy="{132*math.sin(math.radians(a)):.0f}" r="17" class="{"tealp" if a%90 else "goldp"} o"/>' for a in range(0, 360, 45))}
  <circle r="18" class="gold o"/>
</g>
<path d="M60 356h480" class="a"/>''')

add('carry', '両腕で段ボール箱をいくつも抱えて運んでいる',
    '運ぶ、持ち歩く＝carry。', f'''
{person(220, 356, 1.15, 1, 'teal', 'blue', 'carry', 'short', 'smile')}
<g transform="translate(238, 236)">
  <path d="M-56-32h112v64h-112z" class="gold o"/>
  <path d="M-56-32l14-16h112l-14 16z" class="goldp o"/>
  <path d="M56-32l14-16v64l-14 16z" class="goldd o"/>
  <path d="M0-32v64" fill="none" stroke="#a0764a" stroke-width="3"/>
</g>
<g transform="translate(238, 172)">
  <path d="M-34-20h68v40h-68z" class="gold o"/>
  <path d="M-34-20l10-12h68l-10 12z" class="goldp o"/>
</g>
{arc(330, 300, 400, 260, 26, MUTED, True, 4)}''', arrow=True)

add('cat', 'しっぽを立ててすわる猫を正面から見たところ',
    '猫＝cat。', f'''
<g transform="translate(300, 300)">
  <path d="M64 6q64 6 52-60" fill="none" stroke="{GLDD}" stroke-width="16" stroke-linecap="round"/>
  <ellipse rx="76" ry="58" class="gold o"/>
  <path d="M-44-114l-16-48 44 28zM26-116l22-44 20 40z" class="gold o"/>
  <circle cx="-4" cy="-88" r="48" class="gold o"/>
  <circle cx="-22" cy="-96" r="5" class="ink"/><circle cx="16" cy="-96" r="5" class="ink"/>
  <path d="M-6-78l12 0-6 9z" fill="{CRL}" stroke="{CRL}" stroke-width="2"/>
  <path d="M-32-76h-38M-32-68h-36M24-76h38M24-68h36" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-9-64q9 9 18 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>''')

add('cd', '光を反射する円盤の中央に丸い穴があいたCD',
    'CD、コンパクトディスク＝cd。', f'''
<g transform="translate(300, 214)">
  <circle r="132" fill="#dfe9f2" class="o"/>
  <circle r="104" fill="none" stroke="{VIO}" stroke-width="10"/>
  <circle r="76" fill="none" stroke="{TEA}" stroke-width="9"/>
  <circle r="38" fill="#fffaf1" class="o"/>
  <path d="M-118-44a124 124 0 0 1 62-84" fill="none" stroke="#fffdf6" stroke-width="15" stroke-linecap="round"/>
  <path d="M-86 62a110 110 0 0 0 44 48" fill="none" stroke="#fffdf6" stroke-width="11" stroke-linecap="round"/>
</g>
{spark(468, 120, 1.3, 'gold')}''')

add('ceiling fan', '天井から吊られた扇風機の羽根が回り、回転の矢印がついている',
    '天井扇、シーリングファン＝ceiling fan。天井の fan は「扇」の意味。', f'''
<path d="M50 26h500" class="a"/>
<path d="M300 26v78" fill="none" stroke="{INK}" stroke-width="6"/>
<g transform="translate(300, 152)">
  <circle r="26" class="teal o"/>
  {''.join(f'<ellipse cx="0" cy="-64" rx="17" ry="44" class="tealp o" transform="rotate({i*90})"/>' for i in range(4))}
</g>
<path d="M300 178v66" fill="none" stroke="{MUTED}" stroke-width="3"/>
<circle cx="300" cy="252" r="9" class="gold o"/>
{arc(430, 208, 486, 272, 50, MUTED, True, 5)}
<path d="M60 380h480" class="a"/>''', arrow=True)

add('cent', '百の粒のうち一つだけが大きく色づき、そばに小さな硬貨が置かれている',
    'セント＝cent。1ドルの100分の1の金額。', f'''
{''.join(f'<circle cx="{52+i*26}" cy="{88+j*26}" r="6" fill="{STONE}"/>' for i in range(10) for j in range(10))}
<circle cx="52" cy="88" r="15" class="goldd o"/>
{arc(80, 110, 400, 220, 80, MUTED, True, 5)}
{coin(462, 230, 46)}
{ring(462, 230, 62, True)}
{spark(400, 320, 1.3, 'gold')}''', arrow=True)

add('center', '何重もの輪のいちばん内側に矢が当たり、中心の点が目立っている',
    '中心、中央＝center。施設、センターの意味でも使う。', f'''
<g transform="translate(320, 214)">
  <circle r="140" fill="#fffefd" class="o"/>
  <circle r="104" fill="none" stroke="{CRL}" stroke-width="7"/>
  <circle r="68" fill="none" stroke="{INK}" stroke-width="5"/>
  <circle r="30" class="corald o"/>
  {spark(320+0, 214-0, 1.1, 'gold')}
</g>
{line(96, 366, 296, 218, INK, False, 7)}
{ring(320, 214, 46, False, 'gold')}''', arrow=True)

add('chalk', '黒板に白い文字の列が書かれ、下の受けにチョークと黒板消しがのっている',
    'チョーク、白墨＝chalk。', f'''
<g transform="translate(300, 186)">
  <rect x="-230" y="-116" width="460" height="232" fill="#33475a" class="o"/>
  <path d="M-190-70h300M-190-26h250M-190 18h210M-190 62h150" fill="none" stroke="#f4f6f8" stroke-width="7" stroke-linecap="round"/>
  <path d="M-246 116h492v18h-492z" fill="#c9a464" class="o"/>
</g>
<g transform="translate(200, 296) rotate(-6)"><path d="M-72-12h144v24h-144z" fill="#fffefd" class="o"/></g>
<g transform="translate(404, 288)"><path d="M-46-22h92v44h-92z" fill="#8a97a3" class="o"/><path d="M-46-22h92v14h-92z" fill="#c3cbd1"/></g>
<path d="M60 356h480" class="a"/>''')

add('child', '背の高い大人のそばに、小さな子どもが手をつないで立っている',
    '子ども＝child。複数形は children と不規則に変わる。', f'''
{person(210, 356, 1.25, 1, 'violet', 'blue', 'hold', 'short', 'smile')}
{person(322, 356, 0.72, 1, 'coral', 'teal', 'hold', 'bob', 'smile')}
<path d="M212 302q60 6 108 22" fill="none" stroke="{SKIN}" stroke-width="9" stroke-linecap="round"/>
{heart(390, 200, 0.8)}''')

add('chimpanzee', '太い枝に両腕でぶら下がり、長い腕と丸い耳が目立つチンパンジー',
    'チンパンジー＝chimpanzee。', f'''
<path d="M40 62h520" fill="none" stroke="#8b6437" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(300, 262)">
  <path d="M-34-14q-22-72-18-180M34-14q22-72 18-180" fill="none" stroke="#6b5a4a" stroke-width="26" stroke-linecap="round"/>
  <path d="M-40 46q-32 40-6 66M40 46q32 40 6 66" fill="none" stroke="#6b5a4a" stroke-width="22" stroke-linecap="round"/>
  <ellipse rx="68" ry="62" fill="#6b5a4a" class="o"/>
  <ellipse rx="34" ry="40" fill="#a98f74" class="o"/>
  <circle cx="-42" cy="-94" r="19" fill="#6b5a4a" class="o"/><circle cx="42" cy="-94" r="19" fill="#6b5a4a" class="o"/>
  <circle cx="0" cy="-86" r="36" fill="#6b5a4a" class="o"/>
  <ellipse cx="0" cy="-74" rx="21" ry="15" fill="#c8ad92" class="o"/>
  <circle cx="-13" cy="-98" r="4" class="ink"/><circle cx="13" cy="-98" r="4" class="ink"/>
  <path d="M-11-68q11 9 22 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>''')

add('chocolate', '四角に区切られた茶色の板チョコと、欠けて外れた一かけら',
    'チョコレート＝chocolate。', f'''
<g transform="translate(268, 226)">
  <path d="M-120-88h240v176h-240z" fill="#5a3d24" class="o"/>
  {''.join(f'<rect x="{-114+i*76}" y="{-82+j*88}" width="68" height="80" rx="7" fill="#7d5730" class="o"/>' for i in range(3) for j in range(2))}
</g>
<g transform="translate(404, 320) rotate(16)">
  <path d="M-34-34h68v68h-68z" rx="7" fill="#7d5730" class="o"/>
</g>
{spark(470, 160, 1.4, 'gold')}
<path d="M60 380h480" class="a"/>''')

add('choose', '並んだ四つの箱のうち一つを指さし、その上に印がついている',
    '選ぶ、選択する＝choose。どれか一つを選び取ること。', f'''
{table(300)}
{''.join(box(150 + i * 100, 268, 62, 54, 18, 'blue') for i in range(4))}
{tick(350, 190)}
{person(88, 366, 1.05, 1, 'teal', 'blue', 'point', 'short', 'smile')}
<path d="M0 368h34" class="a"/>''')

add('cinema', '入口にしま模様のひさしがつき、屋根の上にフィルムの巻きが光る映画館',
    '映画館＝cinema。映画そのものを指すこともある。', f'''
{building(300, 330, 1.15, 'coral')}
<g transform="translate(300, 268)">
  <path d="M-172-30h344l22 44H-194z" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{-166+i*56}-30h28l-8 44h-28z" class="coral"/>' for i in range(6))}
</g>
<g transform="translate(300, 112)">
  <circle r="48" fill="#3a4756" class="o"/>
  {''.join(f'<circle cx="{30*math.cos(math.radians(a)):.0f}" cy="{30*math.sin(math.radians(a)):.0f}" r="10" fill="#fffdf6"/>' for a in range(0, 360, 90))}
  <circle r="8" fill="#fffdf6"/>
  <path d="M-48 0h-56v-34h56z" fill="#3a4756" class="o"/>
  {''.join(f'<rect x="{-92+i*22}" y="-30" width="10" height="10" fill="#fffdf6"/>' for i in range(4))}
</g>
{spark(200, 120, 1.2, 'gold')}''')

add('city', '高い建物がいくつも並んで立ち、道が横に走る都市の風景',
    '都市、市＝city。', f'''
{building(110, 330, 0.72, 'teal')}
{tower(252, 322, 0.82, 'blue', 4)}
{building(392, 330, 0.68, 'violet')}
{tower(502, 322, 0.62, 'gold', 3)}
<path d="M40 340h520" class="a"/>
<path d="M60 354h480" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="18 14"/>''')

add('clap', '向かい合った両手が打ち合わされ、上下に動きの線が出ている',
    '拍手する＝clap。手をたたく音の意味でも使う。', f'''
{hand(228, 220, 1)}
{hand(372, 220, -1)}
<g fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round">
  <path d="M300 122l-26-34M300 122l26-34M300 318l-26 34M300 318l26 34"/>
</g>
{spark(300, 70, 1.5)}
{spark(170, 330, 1.2)}
{spark(430, 330, 1.2)}''')

add('class', '黒板の前で先生が説明し、教えられた生徒が机に向かって座っている',
    '授業、クラス＝class。組や階級の意味もある。', f'''
<g transform="translate(452, 158)">
  <rect x="-108" y="-82" width="216" height="156" fill="#33475a" class="o"/>
  <path d="M-78-40h124M-78 2h150M-78 44h96" fill="none" stroke="#f4f6f8" stroke-width="6" stroke-linecap="round"/>
  <path d="M-124 74h248v16h-248z" fill="#c9a464" class="o"/>
</g>
{person(330, 356, 1.1, 1, 'violet', 'blue', 'point', 'bun', 'smile')}
{chair(72, 356, 0.82, 'gold')}
{sit(88, 356, 0.82, 1, 'teal', 'blue', 'bob', 'smile')}
<g transform="translate(150, 322)">
  <path d="M-104-14h208v18h-208z" fill="#c9a464" class="o"/>
  <path d="M-92 4v48M92 4v48" fill="none" stroke="#a0764a" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(120, 300)"><path d="M-34-22h68v44h-68z" class="paper"/></g>''')

add('clean', 'モップで床をふき、通ったあとが光ってきれいになっている',
    '清潔な、掃除する＝clean。形容詞と動詞の両方で使う。', f'''
<path d="M40 340h300v18H40z" fill="#e6efe6"/>
{person(210, 356, 1.15, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(250 350) rotate(12)">
  <path d="M-7-104h14v110h-14z" fill="#8b6437" class="o"/>
  <path d="M-40 4h80v14h-80z" fill="#8a97a3" class="o"/>
  <path d="M-40 18h80v26q-40 16-80 0z" fill="#dfe6ea" class="o"/>
</g>
{spark(120, 326, 1.6)}
{spark(190, 348, 1.2)}
{spark(452, 300, 1.3)}''')

add('cleaner', 'つなぎ服の人が洗剤のスプレーを持ち、足もとにバケツが置いてある',
    '掃除人、洗剤＝cleaner。clean に -er がついた形。', f'''
{person(210, 356, 1.15, 1, 'blue', 'violet', 'hold', 'cap', 'smile')}
<g transform="translate(292, 306)">
  <path d="M-24-44h48v88h-48z" fill="#fffdf6" class="o"/>
  <path d="M-26-16h52v14h-52z" class="teal"/>
  <path d="M-14-60h28v16h-28z" fill="#8a97a3" class="o"/>
  <path d="M14-56h24v12H14z" fill="#8a97a3" class="o"/>
</g>
{''.join(f'<circle cx="{344+i*26}" cy="{236-i*16}" r="6" class="teal"/>' for i in range(4))}
{spark(404, 176, 1.3)}
<g transform="translate(432, 338)">
  <path d="M-46-6h92v48h-92z" fill="#c9a464" class="o"/>
  <path d="M-52-6h104v14h-104z" fill="#a0764a" class="o"/>
  <path d="M-44-6q44-50 88 0" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <path d="M-46 42h92" fill="none" stroke="#a0764a" stroke-width="4"/>
</g>''')

add('clipboard', '上を金具ではさんだ紙ばさみに、書きこみ欄と印が並んでいる',
    'クリップボード、紙ばさみ＝clipboard。パソコンの一時保存領域の意味もある。', f'''
<g transform="translate(300, 236)">
  <path d="M-104-134h208v268h-208z" rx="12" fill="#c9a464" class="o"/>
  <path d="M-88-118h176v246h-176z" class="paper"/>
  <path d="M-42-152h84v38h-84z" rx="8" fill="#8a97a3" class="o"/>
  <circle cx="0" cy="-133" r="9" fill="#dfe6ea" class="o"/>
  {''.join(f'<path d="M-70 {-62+i*56}h34v34h-34z" fill="none" stroke="{INK}" stroke-width="3"/>' for i in range(3))}
  {''.join(f'<rect x="-16" y="{-48+i*56}" width="{130-(i%2)*30}" height="10" rx="5" fill="{MUTED}"/>' for i in range(3))}
</g>
{tick(276, 172, 0.6)}''')

add('clothes', '横棒にハンガーでシャツが三枚つるされている',
    '衣服、服＝clothes。いつも複数形で使う。', f'''
<path d="M110 152h380" fill="none" stroke="#8a97a3" stroke-width="10" stroke-linecap="round"/>
<path d="M130 152v212M470 152v212" fill="none" stroke="#8a97a3" stroke-width="8" stroke-linecap="round"/>
{''.join(hanger(160 + i * 120, 190, 1, ['teal', 'coral', 'gold'][i]) for i in range(3))}
{''.join(tshirt(160 + i * 120, 238, 0.95, ['teal', 'coral', 'gold'][i]) for i in range(3))}
<path d="M60 368h480" class="a"/>''')

add('clothesline', '二本の支柱の間に張った綱に、洗濯ばさみで服がとめてある',
    '物干し綱、洗濯ひも＝clothesline。', f'''
<path d="M96 356V130M504 356V130" fill="none" stroke="#8b6437" stroke-width="11" stroke-linecap="round"/>
<path d="M96 132q204 34 408 0" fill="none" stroke="{INK}" stroke-width="4"/>
{''.join(f'<circle cx="{x}" cy="146" r="9" class="goldd o"/>' for x in (200, 300, 400))}
{tshirt(200, 186, 0.9, 'teal')}
{tshirt(300, 186, 0.9, 'coral')}
{tshirt(400, 186, 0.9, 'gold')}
<path d="M60 368h480" class="a"/>''')

add('club', 'そろいの服を着た仲間が輪になり、旗とボールを囲んでいる',
    'クラブ、部活動＝club。仲間の集まりのこと。', f'''
<path d="M0 340h600" class="a"/>
{person(170, 356, 1.05, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(430, 356, 1.05, -1, 'teal', 'blue', 'give', 'short', 'smile')}
{ball(300, 300, 34, 'coral')}
<g transform="translate(300, 160)">
  <path d="M-6 90V-56" fill="none" stroke="#8b6437" stroke-width="8"/>
  <path d="M-6-56h96l-22 24 22 24H-6z" class="teal o"/>
  {star(24, -32, 13, 'goldp')}
</g>''')

add('coat', 'ハンガーにかけられた、丈の長い前開きのコート',
    'コート、上着＝coat。', f'''
{hanger(300, 160, 1.4, 'blue')}
<g transform="translate(300, 218)">
  <path d="M-40-38q40 22 80 0l26 54-22 90h-88l-22-90z" class="blue o"/>
  <path d="M-6-30q6 130 0 240M6-30q-6 130 0 240" fill="none" stroke="{BLUD}" stroke-width="3"/>
  <path d="M-40-38l40 26 40-26-16-14h-48z" class="bluep o"/>
  {''.join(f'<circle cy="{-4+i*52}" r="6" class="ink"/>' for i in range(3))}
  <path d="M-54 44h108" fill="none" stroke="{BLUD}" stroke-width="10"/>
</g>''')

add('coffee', '湯気の立つカップに濃い色のコーヒーが入っている',
    'コーヒー＝coffee。', f'''
{steam(276, 176)}
<g transform="translate(300, 260)">
  <path d="M-74 44h148" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  {mug(0, 0, 1, 'gold', '#6b4a2a')}
</g>
<g transform="translate(300, 176)"><path d="M-6 34h12v22H-6z" fill="#6b4a2a" class="o"/></g>''')

add('coffee maker', '上のタンクからコーヒーが落ち、ガラスのポットにたまっていく',
    'コーヒーメーカー＝coffee maker。二語で一つの道具を表す。', f'''
<g transform="translate(300, 250)">
  <path d="M-130 60h260v26h-260z" fill="#3a4756" rx="8" class="o"/>
  <path d="M-130 60V-104h84v164z" fill="#5a6673" class="o"/>
  <path d="M-118-92h60v44h-60z" fill="#8fa8bd" class="o"/>
  <path d="M-112 26h48v20h-48z" fill="#3a4756" class="o"/>
  <path d="M-70-36h70v10h-70z" fill="#8a97a3" class="o"/>
  <path d="M-24-46h14v14h-14z" fill="#8a97a3" class="o"/>
  <path d="M-118 66h236v20h-236z" fill="#c3cbd1" class="o"/>
</g>
<g transform="translate(298, 300)">
  <path d="M-52-30h104v40a26 26 0 0 1-26 26h-52a26 26 0 0 1-26-26z" fill="#dfe9f2" class="o"/>
  <path d="M-44 2h88v8a20 20 0 0 1-20 20h-48a20 20 0 0 1-20-20z" fill="#6b4a2a"/>
  <path d="M52-16q26 0 26 20t-26 20" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
</g>
{drop(288, 258, 1.1, 'gold')}
{drop(302, 274, 0.9, 'gold')}''')

add('cold', '厚いコートを着た人が腕をさすり、周りに雪の結晶が舞っている',
    '寒い、冷たい＝cold。風邪の意味でも使う。', f'''
{snow(120, 90, 1.5)}
{snow(470, 120, 1.9)}
{snow(400, 300, 1.3)}
{snow(180, 320, 1.1)}
{person(290, 356, 1.2, 1, 'blue', 'violet', 'hold', 'cap', 'sad')}
<g transform="translate(290, 210)">
  <path d="M-46-6q46-26 92 0l-8 44h-76z" class="blue o"/>
  <path d="M-46-6l46 22 46-22-14-14h-64z" class="bluep o"/>
</g>
<path d="M212 316l-24 12M214 336l-26 6M368 316l24 12M366 336l26 6" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>
{thermometer(510, 330, 0.18, 0.8)}''')

add('college', '柱の並んだ大きな学び舎の前に、木が立っている',
    '大学、単科大学＝college。', f'''
<g transform="translate(300, 330)">
  <path d="M-190 0v-120h380V0z" fill="#fffdf6" class="o"/>
  <path d="M-206-120L0-206l206 86z" class="coral o"/>
  <path d="M-150-96h300v20h-300z" fill="#c9a464" class="o"/>
  {''.join(f'<path d="M{-118+i*58} 0v-80h30v80z" fill="#fffefd" class="o"/>' for i in range(5))}
  <path d="M-150 0h300" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
{''.join(f'<path d="M{-100+i*46} -196l{-18} {-44}h36z" class="corald o"/>' for i in range(5))}
{tree(486, 340, 1.05)}
<path d="M40 348h520" class="a"/>''')

add('color', '手に持ったパレットに、いくつもの色の絵の具がのっている',
    '色、色合い＝color。米国式のつづり。', f'''
<g transform="translate(310, 240) rotate(-12)">
  <path d="M-150 0q0-104 116-104 118 0 118 92 0 52-52 56-40 4-40 34 0 32-40 34-102 8-102-112z" fill="#fffdf6" class="o"/>
  <circle cx="-96" cy="34" r="26" fill="#fffaf1" class="o"/>
  {''.join(f'<circle cx="{-100+i*54}" cy="{-56+(i%2)*6}" r="22" class="{["teal","blue","gold","green","coral","violet"][i]} o"/>' for i in range(6))}
</g>
<path d="M150 336l-70 30M160 344l-64 34" fill="none" stroke="#8b6437" stroke-width="9" stroke-linecap="round"/>
{spark(470, 130, 1.4)}''')

add('colour', '絵の具のチューブから、いくつもの色が絞り出されている',
    '色、色合い＝colour。英国式のつづりで、米国式は color。', f'''
{''.join(tube(180 + i * 120, 150 + i * 20, 1, ['teal', 'coral', 'gold'][i], -14 + i * 12) for i in range(3))}
{''.join(blob(180 + i * 120, 320, 1.1, ['teal', 'coral', 'gold'][i]) for i in range(3))}
{spark(470, 110, 1.3)}''')

add('come', '歩いてきた人が、待っている人のほうへ近づいていく',
    '来る、着く＝come。話し手のほうへ向かう動き。', f'''
{''.join(f'<path d="M{40-i*22} {244+i*22}h-46" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
{person(140, 356, 1.2, 1, 'coral', 'blue', 'walk', 'short', 'smile')}
{person(430, 356, 1.2, -1, 'teal', 'blue', 'give', 'bun', 'smile')}
{arc(240, 200, 350, 200, 70, MUTED, True, 5)}
{spark(470, 210, 1.2)}''', arrow=True)

add('come in', '開いたドアから部屋の中へ入ってくる人と、招き入れる人',
    '入ってくる＝come in。ノックへの返事としても使う。', f'''
{door(300, 356, 128, 206, 'gold', 38)}
{person(150, 356, 1.15, 1, 'teal', 'blue', 'give', 'bob', 'smile')}
{person(300, 356, 1.1, -1, 'coral', 'blue', 'walk', 'short', 'smile')}
{arc(268, 150, 176, 176, 50, MUTED, True, 5)}
{ring(300, 356, 12)}''', arrow=True)

add('coming', 'バス停で待つ人のほうへ、バスが近づいてくる',
    '来るべき、やって来る＝coming。come の現在分詞。', f'''
{arc(560, 130, 340, 166, 60, MUTED, True, 5)}
<g transform="translate(400, 258)">
  <path d="M-140-70h250v150h-250z" class="gold o"/>
  <path d="M110-70l34 44v106h-34z" class="gold o"/>
  <path d="M104-40h30v44h-30z" fill="#dfe9f2" class="o"/>
  {''.join(f'<rect x="{-114+i*78}" y="-56" width="60" height="46" fill="#dfe9f2" class="o"/>' for i in range(3))}
  <circle cx="-70" cy="76" r="32" fill="#3a4756" class="o"/><circle cx="80" cy="76" r="32" fill="#3a4756" class="o"/>
</g>
<path d="M96 356V216" fill="none" stroke="{INK}" stroke-width="8"/>
<rect x="70" y="172" width="54" height="44" class="bluep o"/>
{person(164, 356, 1.05, 1, 'teal', 'blue', 'stand', 'short', 'smile')}''', arrow=True)

add('commuting', '電車の車内で、つり革をつかんだ人たちが立っている',
    '通勤＝commuting。家と職場を往復すること。', f'''
<g transform="translate(300, 240)">
  <path d="M-250-114h500v228h-500z" fill="#e1edfb" class="o"/>
  <path d="M-250-114h500v40h-500z" fill="#9aa7b1" class="o"/>
  {''.join(f'<rect x="{-190+i*160}" y="-58" width="110" height="56" fill="#fffdf6" class="o"/>' for i in range(3))}
</g>
<path d="M70 216h460" fill="none" stroke="{INK}" stroke-width="6"/>
{''.join(f'<path d="M{x} 216v36" fill="none" stroke="{INK}" stroke-width="4"/>' for x in (150, 300, 450))}
{person(150, 354, 0.82, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{person(300, 354, 0.82, -1, 'coral', 'blue', 'up', 'bun', 'smile')}
{person(450, 354, 0.82, 1, 'blue', 'violet', 'up', 'short', 'smile')}''')

add('company', '窓の並んだ会社の建物へ、かばんを持った人が向かっていく',
    '会社＝company。同席している仲間の意味もある。', f'''
{tower(400, 344, 1.15, 'blue', 4)}
<g transform="translate(400, 344)"><path d="M-34 0v-80h68V0z" class="blued o"/></g>
{person(170, 356, 1.15, 1, 'violet', 'blue', 'walk', 'short', 'smile')}
<g transform="translate(228, 306)"><path d="M-28-22h56v44h-56z" fill="#8b6437" class="o"/><path d="M-16-30h32v10h-32z" fill="none" stroke="#8b6437" stroke-width="6"/></g>
<path d="M300 328h56" fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"/>
<path d="M40 344h120" class="a"/>''', arrow=True)

add('complete', '四つのピースが組み合わさって、絵が仕上がっている',
    '完全な、完成させる＝complete。すきまなく全部そろうこと。', f'''
<g transform="translate(300, 226)">
  <path d="M-96-96h192v192h-192z" fill="#fffdf6" class="o"/>
  <path d="M-90-90h90v90h-90z" class="teal o"/>
  <path d="M0-90h90v90H0z" class="coral o"/>
  <path d="M-90 0h90v90h-90z" class="gold o"/>
  <path d="M0 0h90v90H0z" class="green o"/>
  <circle cx="-46" cy="0" r="14" class="greenp o"/><circle cx="46" cy="0" r="14" class="coral o"/>
  <circle cx="0" cy="-46" r="14" class="coral o"/><circle cx="0" cy="46" r="14" class="teal o"/>
</g>
{tick(486, 140)}
{spark(160, 130, 1.5)}''', arrow=False)

add('computer', '画面とキーボードのつながった机の上のコンピューター',
    'コンピューター＝computer。', f'''
<g transform="translate(300, 206)">
  <path d="M-166-124h332v212h-332z" rx="14" fill="#3a4756" class="o"/>
  <path d="M-148-106h296v176h-296z" fill="#dfe9f2"/>
  <rect x="-124" y="-86" width="126" height="86" class="paper"/>
  <path d="M-108-66h84M-108-44h94M-108-24h60" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  <rect x="26" y="-86" width="106" height="60" class="paper"/>
  <circle cx="79" cy="-56" r="18" class="tealp o"/>
  <path d="M-40 88h80v30h-80z" fill="#5a6673" class="o"/>
  <path d="M-96 118h192v16h-192z" fill="#8a97a3" class="o"/>
  <path d="M30 12l26 20-14 4 12 20-12 6-12-20-10 12z" class="ink"/>
</g>
<g transform="translate(300, 348)">
  <path d="M-160-16h320v34h-320z" rx="8" fill="#5a6673" class="o"/>
  {''.join(f'<rect x="{-140+i*24}" y="-10" width="18" height="22" rx="4" fill="#dfe6ea"/>' for i in range(12))}
</g>
<g transform="translate(516, 330)"><ellipse rx="26" ry="38" fill="#8a97a3" class="o"/><path d="M0-16v16" fill="none" stroke="{INK}" stroke-width="4"/></g>''')

add('concert', '舞台の上で歌う人に、客席から頭が集まっている',
    'コンサート、演奏会＝concert。', f'''
<path d="M60 20l140 280h150z" class="goldp" fill-opacity="0.55"/>
<path d="M540 20L400 300H250z" class="goldp" fill-opacity="0.55"/>
<circle cx="60" cy="20" r="16" class="goldd o"/><circle cx="540" cy="20" r="16" class="goldd o"/>
<path d="M50 300h500v22H50z" fill="#8b6437" class="o"/>
{person(300, 300, 1.25, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
{''.join(f'<g transform="translate({x} {y})"><circle cy="-40" r="26" fill="#3a4756"/><path d="M-44 26q0-42 44-42t44 42z" fill="#3a4756"/></g>' for x, y in ((120, 396), (250, 404), (430, 400), (550, 392)))}
{spark(150, 120, 1.4, 'goldp')}
{spark(460, 96, 1.2, 'goldp')}''')

add('conversation', '向かい合った二人の間で、ことばの吹き出しが行き交っている',
    '会話、話し合い＝conversation。', f'''
{person(180, 356, 1.15, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{person(420, 356, 1.15, -1, 'coral', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(206, 148)">
  <path d="M-84-52h168v80h-46l-20 28-16-28h-86z" class="paper"/>
  {''.join(f'<rect x="-62" y="{-30+i*22}" width="{104-(i%2)*34}" height="9" rx="4.5" fill="{MUTED}"/>' for i in range(3))}
</g>
<g transform="translate(424, 196)">
  <path d="M-78-46h156v72h-42l-18 26-14-26h-82z" class="tealp"/>
  <path d="M-78-46h156v72h-42l-18 26-14-26h-82z" fill="none" class="o"/>
  {''.join(f'<rect x="-56" y="{-26+i*20}" width="{88-(i%2)*28}" height="8" rx="4" fill="{TEAD}"/>' for i in range(3))}
</g>''')

add('cooler', 'ふたを開けた保冷箱に、氷と飲み物が入っている',
    '保冷箱、クーラーボックス＝cooler。cool に -er がついた形。', f'''
<g transform="translate(300, 306)">
  <g transform="translate(-150, -40) rotate(-56)"><path d="M0 0h300v30H0z" class="teal o"/><path d="M-55 0h20v30h-20z" fill="#8a97a3"/></g>
  <path d="M-150-40h300v104a16 16 0 0 1-16 16h-268a16 16 0 0 1-16-16z" class="teal o"/>
  <path d="M-150-40h300v26h-300z" class="tealp o"/>
  <path d="M-140-34h280v14h-280z" fill="#fffdf6"/>
  {''.join(f'<rect x="{-120+i*60}" y="-72" width="46" height="40" rx="8" fill="#fffdf6" class="o"/>' for i in range(4))}
  {''.join(f'<g transform="translate({-84+i*76} -58) rotate({-16+i*14})"><path d="M-14-46h28v72h-28z" rx="8" class="blue o"/><path d="M-8-56h16v12h-16z" fill="#8a97a3"/></g>' for i in range(3))}
</g>
{snow(140, 130, 1.2)}
{spark(470, 170, 1.4)}
<path d="M60 380h480" class="a"/>''')

add('correct', 'まちがえた語を書き直し、正しいほうに印がついている',
    '正しい、訂正する＝correct。形容詞と動詞の両方で使う。', f'''
{word(190, 150, 5, 32, INK, 2)}
{cross(190, 236, 1.2)}
{arc(250, 180, 330, 250, 40, MUTED, True, 5)}
{word(430, 300, 5, 32, INK)}
{tick(430, 196)}
<path d="M240 300h140" class="a"/>''', arrow=True)

add('cost', '商品のそばに値札が下がり、硬貨が積まれている',
    '費用がかかる、費用＝cost。代金がかかること。', f'''
<g transform="translate(250, 250)">
  <path d="M-96-70h192v140h-192z" class="teal o"/>
  <path d="M-96-70l24-24h192l-24 24z" class="tealp o"/>
  <path d="M96-70l24-24v140l-24 24z" class="teald o"/>
</g>
<path d="M250 118v30" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g transform="translate(250, 118) rotate(-10)">
  <path d="M-96-32l34-32h158v64h-158z" fill="#fffdf6" class="o"/>
  <circle cx="-56" cy="0" r="9" fill="#fffaf1" class="o"/>
  {''.join(f'<rect x="{-30+i*54}" y="-9" width="40" height="18" rx="9" fill="{INK}"/>' for i in range(3))}
</g>
{coin(474, 300, 34)}
{coin(474, 262, 34)}
{coin(440, 330, 34)}
{spark(470, 160, 1.3)}''')

add('cot', '柵のついたベッドに赤ちゃんが寝ている',
    '（柵付きの）ベビーベッド、簡易ベッド＝cot。', f'''
<g transform="translate(300, 306)">
  <path d="M-150 30h300v22h-300z" fill="#c9a464" class="o"/>
  <path d="M-150 52v40M-110 52v40M110 52v40M150 52v40" fill="none" stroke="#a0764a" stroke-width="10" stroke-linecap="round"/>
  <path d="M-140-28h280v58h-280z" fill="#fffdf6" class="o"/>
  {''.join(f'<rect x="{-136+i*34}" y="-84" width="13" height="58" class="greenp o"/>' for i in range(9))}
  <path d="M-150-96h300v14h-300z" class="goldd o"/>
  <path d="M-14-28h154v58h-154z" class="bluep o"/>
  <circle cx="-72" cy="-54" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-100-64q6-30 30-28 22 2 26 22-16-12-30-4-14-8-26 10z" fill="{HAIR}"/>
  <circle cx="-80" cy="-56" r="2.4" class="ink"/><circle cx="-62" cy="-56" r="2.4" class="ink"/>
  <path d="M-78-44q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>''')

add('could', '山の頂上まで登りきり、両腕を上げて旗のそばに立っている',
    '〜できた、〜してもいいですか＝could。can の過去形。', f'''
<path d="M-40 400L300 160 640 400z" class="greenp o"/>
<path d="M126 290q80-62 158-118" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12"/>
{person(92, 306, 0.9, 1, 'teal', 'blue', 'walk', 'short', 'neutral')}
<g transform="translate(392, 226)">
  <path d="M0 0v-146" fill="none" stroke="#8b6437" stroke-width="9"/>
  <path d="M0-146h84l-20 26 20 26H0z" class="coral o"/>
</g>
{person(300, 172, 0.92, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{star(196, 108, 24)}''')

add('country', '丘の向こうに畑と農家が広がり、旗が立っている',
    '国、田舎＝country。土地そのものを指す言い方。', f'''
<path d="M0 314q130-76 280-30t320-46v162H0z" class="greenp"/>
<path d="M0 314q130-76 280-30t320-46" fill="none" stroke="{GRND}" stroke-width="4"/>
{house(150, 320, 0.78, 'coral')}
{tree(470, 328, 0.95)}
<g transform="translate(330, 330)">
  <path d="M0 0v-176" fill="none" stroke="#8b6437" stroke-width="8"/>
  <path d="M0-176h96l-24 26 24 26H0z" class="teal o"/>
</g>
{''.join(f'<path d="M{44+i*54} 350h6v-34h-6z" fill="#c9a464"/><path d="M{20+i*54} 322h54v7h-54z" fill="#c9a464"/>' for i in range(4))}
<path d="M40 368h520" class="a"/>''')

add('courgette', '緑のとれたズッキーニと、切った輪切りが並んでいる',
    'ズッキーニ＝courgette。米国では zucchini。', f'''
<g transform="translate(280, 240) rotate(-16)">
  <rect x="-160" y="-46" width="320" height="92" rx="46" class="green o"/>
  <path d="M-150-6q-30-12-42-36" fill="none" stroke="{GRND}" stroke-width="13" stroke-linecap="round"/>
  {''.join(f'<path d="M{-110+i*44} {-36}v72" fill="none" stroke="{GRND}" stroke-width="6" stroke-linecap="round"/>' for i in range(6))}
</g>
<g transform="translate(492, 306)">
  <circle r="46" class="greenp o"/>
  <circle r="32" fill="#eef7ec" class="o"/>
  {''.join(f'<ellipse cx="{22*math.cos(math.radians(a)):.0f}" cy="{22*math.sin(math.radians(a)):.0f}" rx="7" ry="10" fill="#cfe3c8" class="o" transform="rotate({a} {22*math.cos(math.radians(a)):.0f} {22*math.sin(math.radians(a)):.0f})"/>' for a in range(0, 360, 60))}
</g>
<path d="M60 366h240" class="a"/>''')

add('courier', '荷物をかかえた配達の人が、玄関先へ運んでいく',
    '宅配業者、配達人＝courier。', f'''
{door(24, 356, 104, 184, 'blue', 0)}
{person(232, 356, 1.15, -1, 'coral', 'blue', 'carry', 'cap', 'smile')}
<g transform="translate(214, 232)">
  <path d="M-52-30h104v60h-104z" class="gold o"/>
  <path d="M-52-30l12-14h104l-12 14z" class="goldp o"/>
  <path d="M0-30v60" fill="none" stroke="#a0764a" stroke-width="3"/>
  <path d="M-30-30v60M30-30v60" fill="none" stroke="#a0764a" stroke-width="3"/>
</g>
<g transform="translate(450, 258)">
  <path d="M-120-74h220v148h-220z" class="gold o"/>
  <path d="M100-74l40 46v102h-40z" class="gold o"/>
  <path d="M96-42h30v40h-30z" fill="#dfe9f2" class="o"/>
  <circle cx="-64" cy="74" r="30" fill="#3a4756" class="o"/><circle cx="74" cy="74" r="30" fill="#3a4756" class="o"/>
</g>
<path d="M160 236H132" fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('cow', '白と黒のまだらの体に乳のふくらみがついた雌牛',
    '雌牛、乳牛＝cow。', f'''
<g transform="translate(310, 300)">
  <path d="M118-64q50 12 32 82" fill="none" stroke="#3a4756" stroke-width="12" stroke-linecap="round"/>
  <path d="M-96 20v36M-36 24v32M40 24v32M96 20v36" fill="none" stroke="#3a4756" stroke-width="16" stroke-linecap="round"/>
  <ellipse cx="0" cy="-40" rx="122" ry="66" fill="#fffefd" class="o"/>
  <path d="M-72-80q42-22 62 8t-22 42q-32 10-46-16z" fill="#3a4756"/>
  <path d="M34-70q30-16 46 6t-14 34q-24 8-34-12z" fill="#3a4756"/>
  <ellipse cx="-46" cy="24" rx="32" ry="22" class="coralp o"/>
  <ellipse cx="-158" cy="-56" rx="58" ry="44" fill="#fffefd" class="o"/>
  <path d="M-186-92l-8-34 30 22zM-134-92l8-34-30 22z" fill="#3a4756" class="o"/>
  <ellipse cx="-196" cy="-40" rx="26" ry="20" class="coralp o"/>
  <circle cx="-176" cy="-72" r="5" class="ink"/><circle cx="-146" cy="-72" r="5" class="ink"/>
</g>''')  # noqa: E501

add('crosswalk', '道路に白いしまが並び、その上を人が歩いて渡っている',
    '横断歩道＝crosswalk。', f'''
<path d="M0 300h600v104H0z" fill="#5a6673"/>
{''.join(f'<path d="M{52+i*76} 300h44v104h-44z" fill="#fffdf6"/>' for i in range(7))}
{person(300, 356, 1.15, 1, 'coral', 'blue', 'walk', 'short', 'smile')}
<path d="M96 356V236" fill="none" stroke="{INK}" stroke-width="8"/>
<g transform="translate(96, 200)"><path d="M-24-32h48v64h-48z" rx="8" fill="#3a4756" class="o"/><circle cy="-14" r="8" class="coral"/><circle cy="14" r="8" class="green"/></g>
<path d="M180 216h90" fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('cup', '受け皿の上にのった、取っ手つきのカップ',
    'カップ、茶わん＝cup。優勝カップの意味でも使う。', f'''
{steam(276, 178)}
<g transform="translate(300, 300)">
  <ellipse rx="142" ry="30" fill="#fffdf6" class="o"/>
  <ellipse rx="100" ry="18" fill="#f4ead9"/>
  <path d="M-68-74h136v54a46 46 0 0 1-46 46h-44a46 46 0 0 1-46-46z" fill="#fffefd" class="o"/>
  <path d="M-60-66h120v10a8 8 0 0 1-8 8h-104a8 8 0 0 1-8-8z" fill="#f4e2c4"/>
  <path d="M68-52q32 0 32 26t-32 26" fill="none" stroke="#fffefd" stroke-width="14"/>
  <path d="M68-52q32 0 32 26t-32 26" fill="none" stroke="{INK}" stroke-width="5"/>
</g>''')

add('customer', '店のカウンターごしに、買い物客が店員と向き合っている',
    '客、顧客＝customer。', f'''
{person(300, 300, 0.92, 1, 'teal', 'blue', 'give', 'short', 'smile')}
<g transform="translate(300, 334)">
  <path d="M-160-20h320v30h-320z" fill="#c9a464" class="o"/>
  <path d="M-146 10h292v34h-292z" fill="#e0cba8" class="o"/>
  <path d="M-40-46h80v26h-80z" fill="#8a97a3" class="o"/>
</g>
{person(300, 396, 1.0, -1, 'violet', 'blue', 'give', 'bob', 'smile')}
<g transform="translate(384, 372)"><path d="M-28-24h56v48h-56z" class="coral o"/><path d="M-16-32q16-16 32 0" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{coin(232, 384, 22)}''')

add('cyclist', '自転車にまたがり、前かがみでペダルをこぐ人',
    '自転車に乗る人＝cyclist。', f'''
{rider(300, 258, 1.15, 0, 'coral', 'teal')}
{''.join(f'<path d="M{120-i*26} {222+i*8}h-44" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
<path d="M60 340h480" class="a"/>''')

add('dad', '父親の肩に子どもをのせて、いっしょに歩いている',
    'お父さん、パパ＝dad。幼い子どもが使うくだけた言い方。', f'''
<g transform="translate(300, 240)">
  <path d="M-34-30q34-16 68 0l-8 66h-52z" class="coral o"/>
  <path d="M-26 22q-30 4-34 40M26 22q30 4 34 40" fill="none" stroke="{TONES['blue'][2]}" stroke-width="15" stroke-linecap="round"/>
</g>
{person(300, 356, 1.3, 1, 'blue', 'gold', 'hold', 'short', 'smile')}
<circle cx="300" cy="162" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M272-18q6-30 28-28 22 2 26 24-16-12-28-4-12-8-26 8z" transform="translate(0, 172)" fill="{HAIR}"/>
<circle cx="291" cy="156" r="3" class="ink"/><circle cx="309" cy="156" r="3" class="ink"/>
<path d="M293 172q7 7 14 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
<circle cx="268" cy="196" r="13" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<circle cx="332" cy="196" r="13" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
{spark(468, 160, 1.3)}''')

add('dance', '手をつないだ二人が、腕を上げて踊っている',
    '踊る、ダンス＝dance。動詞と名詞の両方で使う。', f'''
{person(208, 356, 1.15, 1, 'coral', 'violet', 'up', 'bob', 'smile')}
{person(392, 356, 1.15, -1, 'teal', 'blue', 'up', 'bun', 'smile')}
<path d="M263 214h74" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
{arc(230, 150, 370, 150, 60, MUTED, True, 4)}
{arc(236, 96, 364, 96, 46, MUTED, True, 4)}
{spark(160, 180, 1.3)}
{spark(440, 180, 1.3)}
<path d="M100 340h400" class="a"/>''', arrow=True)

add('dandelion', '黄色い花をつけたタンポポから、綿毛が風に飛んでいく',
    'タンポポ＝dandelion。', f'''
<path d="M60 366h480" class="a"/>
<g transform="translate(210, 362)">
  <path d="M0 0q-14-96-8-140" fill="none" stroke="{GRND}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-8-40q-78 8-92-42 50-8 92 42z" class="green o"/>
  <path d="M-6-84q66 6 78-40-42-6-78 40z" class="greenp o"/>
</g>
<g transform="translate(204, 210)">
  <circle r="30" class="goldp o"/>
  <g fill="none" stroke="{GLD}" stroke-width="4" stroke-linecap="round">
  {''.join(f'<path d="M0-30v-16" transform="rotate({a})"/>' for a in range(0, 360, 30))}
  </g>
</g>
<path d="M262 168q80-56 168-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
{''.join(f'<g transform="translate({x} {y})"><circle r="5" class="ink"/><g fill="none" stroke="{MUTED}" stroke-width="2.5"><path d="M0-4l-14-16M0-4l0-20M0-4l14-16"/><path d="M-14-20h28"/></g></g>' for x, y in ((318, 136), (390, 106), (452, 148), (478, 214)))}''')  # noqa: E501

add('daughter', 'おさげの女の子が、親の手をとって立っている',
    '娘＝daughter。親から見た女の子。', f'''
{person(208, 356, 1.22, 1, 'violet', 'blue', 'give', 'bun', 'smile')}
{girl(348, 356, 0.86, 'coral', 'bob')}
<g transform="translate(348, 356) scale(0.86)">
  <circle cx="-30" cy="-104" r="14" class="coral o"/><circle cx="30" cy="-104" r="14" class="coral o"/>
</g>
<path d="M286 282q30 4 48 12" fill="none" stroke="{SKIN}" stroke-width="9" stroke-linecap="round"/>
{heart(300, 196, 1.0)}''')

add('day', '空高くのぼった太陽の下に、家と木が広がっている',
    '日、1日、昼間＝day。', f'''
<path d="M60 122q240-92 480 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="16 13"/>
{sun(300, 108, 46)}
<path d="M120 250q16-12 32 0M168 268q13-9 26 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
{house(456, 340, 0.8, 'coral')}
{tree(140, 344, 1.05)}
{flower(330, 344, 1.0, 'violet')}''')

add('decide', '二つに分かれた道の前で、片方の道に足を踏み出している',
    '決める、決心する＝decide。いくつかから一つに決めること。', f'''
<path d="M300 356q-120-140-200-206" fill="none" stroke="{MUTED}" stroke-width="9" stroke-dasharray="18 14"/>
<path d="M300 356q130-140 210-206" fill="none" stroke="{MUTED}" stroke-width="9" stroke-dasharray="18 14"/>
<path d="M0 356h600" class="a"/>
{person(300, 356, 1.1, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{tick(492, 108)}
{ring(110, 108, 40, True)}
{spark(520, 180, 1.3)}''')

add('dentistry', 'いすに寝かせた患者の口もとを、歯科医がのぞきこんでいる',
    '歯科、歯科医術＝dentistry。dentist は歯科医。', f'''
<g transform="translate(360, 320)">
  <path d="M-150-40h250v44h-250z" class="blue o"/>
  <path d="M100-40v-96h34v96z" class="blue o"/>
  <path d="M-150 4v40M-90 4v40M-30 4v40" fill="none" stroke="#315f98" stroke-width="12" stroke-linecap="round"/>
  <circle cx="140" cy="-160" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M116-172q10-26 30-22 18 4 20 22-16-10-26-2-12-8-24 2z" fill="{HAIR}"/>
</g>
{person(120, 356, 1.05, 1, 'teal', 'blue', 'give', 'short', 'smile')}
<g transform="translate(196, 268) rotate(-28)"><path d="M0 0h96" fill="none" stroke="#8a97a3" stroke-width="9"/><circle cx="100" r="14" class="paper"/></g>
<g transform="translate(150, 106)">
  <path d="M0 44q-42 0-42-38 0-52 42-52t42 52q0 38-42 38z" fill="#fffefd" class="o"/>
  <path d="M-22 34q-8 34 4 46M22 34q8 34-4 46" fill="none" stroke="#fffefd" stroke-width="20" stroke-linecap="round"/>
  <path d="M-22 34q-8 34 4 46M22 34q8 34-4 46" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M0 44q-42 0-42-38 0-52 42-52t42 52q0 38-42 38z" fill="none" class="o"/>
</g>
{spark(92, 54, 1.3)}''')

add('deodorant', '両腕を上げた人のわきに、スプレーが吹きつけられている',
    '制汗剤、デオドラント＝deodorant。においを抑える化粧品。', f'''
{person(230, 356, 1.2, 1, 'teal', 'blue', 'up', 'short', 'smile')}
<g transform="translate(398, 308)">
  <path d="M-30-26h60v86h-60z" rx="10" class="blue o"/>
  <path d="M-30-8h60v16h-60z" class="bluep"/>
  <path d="M-14-40h28v14h-28z" fill="#8a97a3" class="o"/>
  <path d="M14-52h22v12H14z" fill="#8a97a3" class="o"/>
</g>
{''.join(f'<circle cx="{332-i*14}" cy="{272-i*14}" r="{4+i}" class="teal"/>' for i in range(5))}
{spark(440, 200, 1.4)}
{spark(420, 120, 1.1)}''')

add('desk', '引き出しのついた机の上に、電気と文房具が置いてある',
    '机、事務机＝desk。受付などの窓口の意味もある。', f'''
<g transform="translate(300, 300)">
  <path d="M-230-16h460v28h-460z" fill="#c9a464" class="o"/>
  <path d="M-214 12h180v88h-180z" fill="#e0cba8" class="o"/>
  <path d="M-200 24h152v18h-152z" fill="#c9a464" class="o"/>
  <path d="M-200 56h152v18h-152z" fill="#c9a464" class="o"/>
  <path d="M120 12h84v82h-84z" fill="#e0cba8" class="o"/>
</g>
<g transform="translate(112, 284)">
  <path d="M0 0v-96q0-24 26-24" fill="none" stroke="#8a97a3" stroke-width="8"/>
  <path d="M26-140l-40 34h80z" class="gold o"/>
  <path d="M-22-40h44v40h-44z" fill="#8a97a3" class="o"/>
</g>
<rect x="242" y="250" width="128" height="34" class="paper"/>
<rect x="258" y="238" width="128" height="34" class="paper"/>
{mug(430, 284, 0.85, 'teal', '#6b4a2a')}
<g transform="translate(320, 284)"><path d="M-16-46h32v46h-32z" class="coral o"/><path d="M-12-56v10M0-56v10M12-56v10" fill="none" stroke="{CRLD}" stroke-width="5"/></g>''')

add('dictionary', '背の厚い辞書に、色分けされた見出しのつまみが並んでいる',
    '辞書、事典＝dictionary。', f'''
<g transform="translate(272, 240)">
  <path d="M-100-124h200v248h-200z" class="teald o"/>
  <path d="M-78-102h156v204h-156z" class="paper"/>
  <rect x="-78" y="-30" width="156" height="46" class="goldp o"/>
  <path d="M-58-14h116M-58 6h96" fill="none" stroke="{GLDD}" stroke-width="6" stroke-linecap="round"/>
  <path d="M100-124h28v248h-28z" fill="#fffdf6" class="o"/>
  {''.join(f'<path d="M100 {-104+i*34}v24" fill="none" stroke="{MUTED}" stroke-width="2.5"/>' for i in range(7))}
  {''.join(f'<path d="M128 {-100+i*40}h34v24h-34z" class="{TABS[i%6]} o"/>' for i in range(6))}
</g>
{spark(452, 128, 1.3)}''')

add('die', '花をそえた墓石が、草の上にひっそりと立っている',
    '死ぬ、亡くなる＝die。', f'''
<path d="M120 356h360v30H120z" class="greenp"/>
<g transform="translate(300, 356)">
  <path d="M-96 0v-152a96 96 0 0 1 192 0V0z" fill="#c3cbd1" class="o"/>
  <path d="M-118 0h236v16h-236z" fill="#aeb8bf" class="o"/>
  <circle cx="0" cy="-108" r="34" fill="none" stroke="#8a97a3" stroke-width="6"/>
  <path d="M-16-108h32M0-124v32" fill="none" stroke="#8a97a3" stroke-width="6"/>
</g>
<g transform="translate(400, 356)">
  <path d="M0 0q-6-52 24-58" fill="none" stroke="{GRND}" stroke-width="7" stroke-linecap="round"/>
  <g transform="translate(24, -58) rotate(58)"><ellipse rx="13" ry="20" class="coral o"/><ellipse cx="-18" ry="14" rx="11" class="coralp o"/></g>
</g>
<path d="M96 112q22-14 40 6" fill="none" stroke="{MUTED}" stroke-width="4"/>
{spark(510, 300, 1.0, 'greenp')}''')

add('difference', '高さのちがう二本の棒と、その差をはかる矢印',
    '違い、差＝difference。different の名詞形。', f'''
{bar(170, 356, [110, 68], 92, 66, 2.2, ['teal', 'blue'])}
<path d="M170 114h92v93h-92z" class="coral o"/>
<path d="M110 207h300" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
{line(286, 300, 286, 128, INK, False, 6)}
<path d="M306 128v172" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M270 128h36M270 300h36" fill="none" stroke="{CRL}" stroke-width="6" class="o"/>''', arrow=True)

add('different', 'まる、しかく、さんかくが並び、それぞれ形も色もちがう',
    '違う、異なる＝different。さまざまな、という意味でも使う。', f'''
<path d="M212 60v280" class="muted"/>
<path d="M388 60v280" class="muted"/>
<circle cx="140" cy="240" r="72" class="teal o"/>
<path d="M230 168h140v140H230z" class="coral o"/>
<path d="M452 168l72 140h-144z" class="gold o"/>
{spark(140, 96, 1.3)}
{spark(300, 96, 1.3)}
{spark(452, 96, 1.3)}''')

add('difficult', 'もつれた縄を前に、頭をかかえて困っている',
    '難しい、困難な＝difficult。', f'''
{person(140, 356, 1.1, 1, 'coral', 'blue', 'think', 'short', 'sad')}
<g transform="translate(368, 244)" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round">
  <path d="M-116-44q116-72 232 0"/>
  <path d="M116 44q-116 72-232 0"/>
  <path d="M-62-98q-64 98 0 196"/>
  <path d="M62 98q64-98 0-196"/>
  <path d="M-116-40q116 128 232 0"/>
  <path d="M-116 40q116-128 232 0"/>
</g>
{drop(228, 214, 1.0, 'blue')}
<path d="M60 366h480" class="a"/>''')

add('dinosaur', '長い首を高くのばした恐竜が、大きな体で立っている',
    '恐竜＝dinosaur。', f'''
<g transform="translate(280, 356)">
  <path d="M-150-116q-70-16-124 24" fill="none" stroke="{GRN}" stroke-width="40" stroke-linecap="round"/>
  <ellipse cx="0" cy="-116" rx="152" ry="78" class="green o"/>
  <path d="M-100-46v46M-34-40v40M40-40v40M104-46v46" fill="none" stroke="{GRND}" stroke-width="36" stroke-linecap="round"/>
  <path d="M108-150q56-30 70-90 6-26 6-50" fill="none" stroke="{GRN}" stroke-width="46" stroke-linecap="round"/>
  <ellipse cx="186" cy="-290" rx="54" ry="36" class="green o"/>
  <circle cx="208" cy="-302" r="6" class="ink"/>
  <path d="M-40-190l-8-38 30 24zM20-196l-4-38 28 26z" class="greend o"/>
</g>
<path d="M40 356h520" class="a"/>''')

add('dirty', 'よごれたシャツに、茶色のしみと泥のはねがついている',
    '汚い、汚れた＝dirty。反対は clean。', f'''
{tshirt(300, 214, 1.9, 'blue')}
<g fill="#8b6437">
  <ellipse cx="248" cy="256" rx="32" ry="24"/>
  <ellipse cx="352" cy="236" rx="26" ry="18"/>
  <ellipse cx="300" cy="196" rx="20" ry="15"/>
</g>
{drop(168, 330, 1.3, 'goldd')}
{drop(432, 348, 1.1, 'goldd')}
{drop(452, 282, 0.9, 'goldd')}
{puff(150, 200, 1.0, '#d8cbb4')}''')

add('diving', '板から空高く跳び上がり、水面へ頭から落ちていく',
    'ダイビング、飛び込み＝diving。dive の名詞形。', f'''
<g transform="translate(96, 356)">
  <path d="M-46 0h92v-186h-92z" fill="#c3cbd1" class="o"/>
  <path d="M-34-186h46v-16h-46z" fill="#8a97a3" class="o"/>
</g>
<path d="M40 158h240v16H40z" fill="#8a97a3" class="o"/>
<path d="M280 166q60 40 80 110" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"/>
<g transform="rotate(126 400 176)">{person(400, 266, 1.0, 1, 'coral', 'blue', 'up', 'short', 'smile')}</g>
<path d="M0 330h600v70H0z" fill="#cfe3f5"/>
<path d="M180 330h280" fill="none" stroke="#9cc0e2" stroke-width="6"/>
<path d="M420 330l-24-30M440 330l22-32M470 330l40-24M400 330l-48-22" fill="none" stroke="#9cc0e2" stroke-width="7" stroke-linecap="round"/>''')

add('do', 'ほうきで床をはき、そばのメモにはすんだ印が並んでいる',
    'する、行う＝do。疑問文や否定文を作る働きもある。', f'''
{person(190, 356, 1.15, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
{broom(216, 350, 1.0, 8)}
{''.join(f'<path d="M{300-i*24} {300+i*14}h-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"/>' for i in range(3))}
<g transform="translate(468, 226)">
  <path d="M-84-116h168v232h-168z" class="paper"/>
  {''.join(f'<path d="M-60 {-76+i*54}h30v30h-30z" fill="none" stroke="{INK}" stroke-width="3"/>' for i in range(3))}
  {''.join(f'<rect x="-16" y="{-64+i*54}" width="70" height="9" rx="4.5" fill="{MUTED}"/>' for i in range(3))}
</g>
{tick(422, 110, 0.7)}
{tick(422, 164, 0.7)}
{tick(422, 218, 0.7)}''')

add('does', '一人だけがはきそうじをしており、二人のほうには印がついていない',
    'do の三人称単数現在＝does。he や she のように一人を指すときの形。', f'''
{ring(190, 240, 130)}
{person(190, 356, 1.15, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
{broom(216, 350, 1.0, 8)}
{tick(190, 110)}
<path d="M330 60v316" class="muted"/>
<g opacity="0.45">
{person(430, 356, 0.95, -1, 'violet', 'blue', 'stand', 'bob', 'neutral')}
{person(530, 356, 0.95, -1, 'violet', 'blue', 'stand', 'short', 'neutral')}
</g>
{ban(480, 170, 40)}''')

add('dog', '尾を立てた四つ足の犬が、こちらを向いて立っている',
    '犬＝dog。', f'''
<g transform="translate(300, 356)">
  <path d="M100-84q46-30 30-78" fill="none" stroke="{GLD}" stroke-width="15" stroke-linecap="round"/>
  <path d="M-96-32v32M-42-26v26M50-26v26M98-32v32" fill="none" stroke="#8b6437" stroke-width="16" stroke-linecap="round"/>
  <ellipse cx="0" cy="-66" rx="106" ry="54" class="gold o"/>
  <path d="M-140-138q-34-10-34 28 26 16 46-2z" class="goldd o"/>
  <ellipse cx="-116" cy="-98" rx="54" ry="46" class="gold o"/>
  <ellipse cx="-162" cy="-84" rx="32" ry="24" fill="#fffefd" class="o"/>
  <circle cx="-188" cy="-92" r="9" class="ink"/>
  <circle cx="-126" cy="-112" r="6" class="ink"/>
  <path d="M-100-140q24 14 48 0l-6 22q-18 10-36 0z" class="coral o"/>
  <path d="M-160-70q14 20 30 4" fill="none" stroke="{INK}" stroke-width="3"/>
</g>''')

add('doing', '同じ人が少しずつずれて重なり、動きが続いていることがわかる',
    'している（進行形）＝doing。do の現在分詞。', f'''
<g opacity="0.28">{person(120, 356, 1.1, 1, 'teal', 'blue', 'walk', 'short', 'flat')}</g>
<g opacity="0.28">{person(210, 356, 1.1, 1, 'teal', 'blue', 'walk', 'short', 'flat')}</g>
{person(300, 356, 1.1, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{''.join(f'<path d="M{180-i*30} {252+i*22}h-40" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
{arc(360, 216, 470, 296, 60, MUTED, True, 5)}
{clock(492, 128, 50, 2, 12)}
{spark(430, 100, 1.2)}''', arrow=True)

add('dollar', '緑色の紙幣が一枚置かれ、そばに金貨が積まれている',
    'ドル＝dollar。米国などの通貨の単位。', f'''
<g transform="translate(300, 206) rotate(-6)">
  <path d="M-196-104h392v208h-392z" class="greenp o"/>
  <path d="M-176-84h352v168h-352z" fill="none" stroke="{GRND}" stroke-width="5"/>
  <circle r="62" fill="none" stroke="{GRND}" stroke-width="7"/>
  <path d="M0-72v144" fill="none" stroke="{GRND}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="-146" cy="-56" r="20" class="green o"/><circle cx="146" cy="-56" r="20" class="green o"/>
  <circle cx="-146" cy="56" r="20" class="green o"/><circle cx="146" cy="56" r="20" class="green o"/>
</g>
{coin(470, 348, 34)}
{coin(470, 312, 34)}
{coin(432, 372, 30)}
{spark(470, 200, 1.4)}''')

add('done', '食べ終わった皿にフォークとナイフが置かれ、印がついている',
    '終わった、済んだ＝done。料理ができあがったという意味でも使う。', f'''
<g transform="translate(280, 280)">
  <ellipse rx="156" ry="92" fill="#fffefd" class="o"/>
  <ellipse rx="114" ry="66" fill="#f4ead9" class="o"/>
</g>
{fork(196, 288, 1.0, -64)}
{knife(372, 288, 1.0, 64)}
{tick(480, 150)}
{spark(120, 130, 1.5)}
{spark(480, 320, 1.2)}''')

add('door', '開きかけのとに、動いた跡の弧が描かれている',
    'ドア、扉＝door。戸口の意味もある。', f'''
{door(180, 356, 150, 220, 'gold', 42)}
{arc(180, 136, 327, 193, 27, MUTED, True, 4)}
{arc(455, 250, 520, 320, 34, CRL, True, 5)}
<path d="M60 356h480" class="a"/>''', arrow=True)

add('down', '階段を下りていく人と、下向きの矢印',
    '下へ、下に＝down。〜を下って、という前置詞でも使う。', f'''
<path d="M40 120h90v46h90v46h90v46h90v46h90" fill="none" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
{person(266, 212, 0.86, 1, 'coral', 'blue', 'walk', 'short', 'smile')}
{line(548, 96, 548, 246, CRL, False, 9)}
{''.join(f'<path d="M{96-i*26} {54+i*30}v{-26-i*10}" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(2))}
<circle cx="86" cy="100" r="18" class="gold o"/>''', arrow=True)

add('downhill', '坂を自転車で一気に下っていく',
    '下り坂で、悪化して＝downhill。下り方向を表す。', f'''
<path d="M0 146L600 336V400H0z" class="greenp"/>
<path d="M0 146L600 336" fill="none" stroke="{GRND}" stroke-width="5"/>
{rider(300, 214, 1.05, 17, 'coral', 'teal')}
{''.join(f'<path d="M{190-i*30} {180+i*10}h-44" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}
{line(500, 262, 566, 284, CRL, False, 8)}
{tree(90, 176, 0.7)}
{cloud(500, 130, 1.0)}''', arrow=True)

add('dress', 'ハンガーにかけられた、すそが広がったワンピース',
    'ワンピース＝dress。服を着せるという動詞でも使う。', f'''
{hanger(300, 106, 1.5, 'violet')}
<g transform="translate(300, 160)">
  <path d="M-34-40q34 22 68 0l14 44 28 176h-152l-6-176z" class="coral o"/>
  <path d="M-30-38l30 24 30-24z" class="coralp o"/>
  <path d="M-52 6h104v20h-104z" class="corald o"/>
  {''.join(f'<circle cx="{-16+i*32}" cy="120" r="7" class="coralp o"/>' for i in range(2))}
</g>
{spark(468, 150, 1.3)}
{spark(140, 220, 1.2)}''')

add('drills', '同じ行をなんども書き写し、丸い矢印で繰り返しを表している',
    '反復練習、ドリル＝drills。穴あけ工具の意味もある。', f'''
<g transform="translate(300, 236)">
  <path d="M-176-124h352v248h-352z" class="paper"/>
  {''.join(word(0, -66 + i * 62, 4, 28, INK) for i in range(3))}
  {''.join(f'<path d="M120 {-66+i*62}h34" fill="none" stroke="{MUTED}" stroke-width="5"/>' for i in range(3))}
</g>
<ellipse cx="300" cy="236" rx="216" ry="158" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="16 13"/>
{spark(300, 62, 1.3)}
{tick(190, 328, 0.8)}
{tick(190, 266, 0.8)}
{tick(190, 204, 0.8)}''')

add('drink', 'グラスを口もとにあてて、飲みものを飲んでいる',
    '飲む、飲み物＝drink。', f'''
{person(220, 356, 1.2, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
<g transform="translate(276, 288)">
  <path d="M-28-44h56v58a28 28 0 0 1-28 28 28 28 0 0 1-28-28z" fill="#dfe9f2" class="o"/>
  <path d="M-24-14h48v30a24 24 0 0 1-24 24 24 24 0 0 1-24-24z" class="blue"/>
  <path d="M-4-70l-16-46" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
</g>
<g transform="translate(420, 300)">
  <path d="M-34-40h68v96h-68z" rx="10" class="gold o"/>
  <path d="M-34-8h68v16h-68z" class="goldp"/>
  <path d="M-14-56h28v16h-28z" fill="#8a97a3" class="o"/>
</g>
{''.join(f'<path d="M{120-i*26} {268+i*20}h-38" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}''')

add('driver', 'ハンドルをにぎって運転席にすわっている人',
    '運転手、ドライバー＝driver。drive する人。', f'''
<g transform="translate(96, 356)">
  <path d="M-46 0v-206h48v206z" fill="#5a6673" class="o"/>
</g>
<g transform="translate(480, 140)">
  <path d="M-84-72h168v144h-168z" fill="#dfe9f2" class="o"/>
  <path d="M-84 14h168" fill="none" stroke="#fffdf6" stroke-width="8"/>
  {''.join(f'<path d="M{-60+i*54} 14v58" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 9"/>' for i in range(3))}
</g>
{person(216, 356, 1.2, 1, 'coral', 'blue', 'hold', 'cap', 'smile')}
<g transform="translate(352, 250)">
  <circle r="92" fill="none" stroke="#3a4756" stroke-width="17"/>
  <path d="M0 0h92M-84-40l84 40M-84 40l84-40" fill="none" stroke="#3a4756" stroke-width="14" stroke-linecap="round"/>
  <circle r="26" class="gold o"/>
</g>
<path d="M60 356h480" class="a"/>''')

add('drop by', '通りから外れて、玄関先にちょっと立ち寄るところ',
    '立ち寄る、ふらっと訪ねる＝drop by。短く寄る感じの句動詞。', f'''
<path d="M40 376h520" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="18 14"/>
<path d="M96 372q180-34 284-96" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="5 18" stroke-linecap="round"/>
{house(430, 320, 0.92, 'blue')}
{person(320, 356, 1.05, 1, 'teal', 'blue', 'give', 'short', 'smile')}
{arc(360, 300, 414, 284, 30, MUTED, True, 4)}
{spark(378, 218, 1.3)}
<path d="M60 330h200" class="a"/>''', arrow=True)

add('dryer', '丸い窓のドラムの中で、洗濯物が回って乾いている',
    '乾燥機、ドライヤー＝dryer。dry する道具。', f'''
<g transform="translate(300, 286)">
  <path d="M-156-98h312v196h-312z" rx="16" class="paper"/>
  <path d="M-156-98h312v60h-312z" fill="#dfe6ea" class="o"/>
  <circle cx="-92" cy="-68" r="18" class="gold o"/>
  <path d="M-46-68h108v14h-108z" fill="#8a97a3"/>
  <circle cy="34" r="74" fill="#dfe9f2" class="o"/>
  <circle cy="34" r="58" fill="none" stroke="#9cc0e2" stroke-width="4"/>
  {tshirt(0, 44, 0.62, 'coral')}
  {arc(58, 4, 24, 56, 30, MUTED, True, 5)}
  {arc(24, 76, 62, 72, -22, MUTED, True, 5)}
</g>
{spark(492, 178, 1.3)}
{spark(118, 190, 1.1)}
<path d="M60 384h480" class="a"/>''', arrow=True)

add('dummy', '赤ちゃんの口にふくませる、輪のついたおしゃぶり',
    '（英国）おしゃぶり、マネキン、にせ物＝dummy。', f'''
<g transform="translate(300, 214)">
  <circle cy="104" r="46" fill="none" stroke="{VIO}" stroke-width="17"/>
  <path d="M-16 44v26M16 44v26" fill="none" stroke="{VIO}" stroke-width="13" stroke-linecap="round"/>
  <ellipse rx="84" ry="38" class="violetp o"/>
  <path d="M-32-32q0-66 32-66t32 66z" class="tealp o"/>
  <path d="M-32-32q0-66 32-66t32 66z" fill="none" class="o"/>
  <path d="M-16-32q0-42 16-42t16 42z" class="teal"/>
</g>
{spark(474, 128, 1.4)}
{spark(140, 300, 1.2)}''')

add('during', '二つの時計の間の時間に、本を読んで過ごしている',
    '〜の間（ずっと・のどこかで）＝during。ある期間の中を表す。', f'''
{clock(110, 120, 54, 10, 0)}
{clock(490, 120, 54, 4, 0)}
<path d="M110 120h380" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"/>
<path d="M118 176q0 24-24 24h388q-24 0-24-24" fill="none" stroke="{MUTED}" stroke-width="4"/>
{person(300, 356, 1.05, 1, 'violet', 'blue', 'hold', 'bun', 'smile')}
<g transform="translate(300, 296)">
  <path d="M-92-34h86v68h-86z" class="paper"/>
  <path d="M6-34h86v68H6z" class="paper"/>
  <path d="M-7-42h14v84h-14z" class="teal o"/>
  {''.join(f'<path d="M{-76+i*30} {-16}h22M{-76+i*30} 4h22" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
  {''.join(f'<path d="M{22+i*30} {-16}h22M{22+i*30} 4h22" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}
</g>''')

add('dusty', 'ほこりをかぶった棚に、ほこりのたまりとくもの巣ができている',
    'ほこりっぽい、ほこりをかぶった＝dusty。', f'''
{web(24, 118, 1.5)}
{puff(190, 244, 1.4, '#d5dce1')}
{puff(402, 158, 1.5, '#d5dce1')}
{puff(250, 300, 1.1, '#d5dce1')}
<g transform="translate(300, 322)">
  <path d="M-224-16h448v22h-448z" fill="#c9a464" class="o"/>
  <path d="M-208 6v58M208 6v58" fill="none" stroke="#a0764a" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(206, 288)">
  <path d="M-56-58h112v74h-112z" fill="#e0cba8" class="o"/>
  <path d="M-56-58l14-16h112l-14 16z" fill="#f0e2c8" class="o"/>
</g>
<g transform="translate(410, 288)">
  <path d="M-34-72h68v88h-68z" rx="10" class="paper"/>
  <path d="M-34-72h68v20h-68z" fill="#8a97a3"/>
</g>
{''.join(f'<circle cx="{132+i*72}" cy="{116+(i%3)*46}" r="5" fill="{STONE}"/>' for i in range(6))}
<path d="M60 380h480" class="a"/>''')

add('each', '三つのさらの上に、それぞれりんごが一つずつのっている',
    'それぞれの、おのおの＝each。一つずつを指すことば。', f'''
<path d="M205 120v280" class="muted"/>
<path d="M395 120v280" class="muted"/>
{''.join(f'<g transform="translate({110+i*190} 330)"><ellipse rx="80" ry="26" fill="#fffdf6" class="o"/><ellipse rx="54" ry="16" fill="#f4ead9"/>{apple(0, -62, 0.9)}</g>' for i in range(3))}
{tick(110, 190)}
{tick(300, 190)}
{tick(490, 190)}''')

add('ear', '横を向いた顔の耳が大きく描かれ、音がそこへ届いている',
    '耳＝ear。音を聞き分ける力の意味でも使う。', f'''
<g transform="translate(266, 224)">
  <ellipse rx="118" ry="146" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-104-118q92-66 168-6 44 34 34 106" fill="none" stroke="{HAIR}" stroke-width="26"/>
  <path d="M-118 24q-48 24-8 52l30 16" fill="#fffaf1" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cx="-58" cy="-30" r="8" class="ink"/>
  <path d="M-30 34q22 16 46 4" fill="none" stroke="{INK}" stroke-width="3.5"/>
  <path d="M34-26q50-8 50 58 0 62-44 70-26 5-26-20" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M30 0q26-6 26 34 0 34-22 40" fill="none" stroke="{INK}" stroke-width="4"/>
  {ring(58, 30, 88)}
</g>
<path d="M540 106q-56 62 0 150" fill="none" stroke="{MUTED}" stroke-width="5"/>
<path d="M498 140q-30 30 0 72" fill="none" stroke="{MUTED}" stroke-width="4"/>
{spark(560, 96, 1.3)}''')

add('early', '時計が朝の六時をさし、丘の向こうから日がのぼりかけている',
    '早い、早く、初期の＝early。', f'''
{clock(198, 168, 96, 6, 0)}
<path d="M416 306a54 54 0 0 1 108 0z" class="goldp o"/>
<g fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round">
  <path d="M470 232v-28M418 244l-18-22M522 244l18-22M378 278l-26-12M562 278l26-12"/>
</g>
<path d="M340 400v-62q140-50 260-18v80z" class="greenp"/>
{person(120, 356, 1.0, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
{''.join(f'<path d="M{64-i*24} {266+i*20}h-36" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>' for i in range(3))}''')

add('easel', '三本足の画架にキャンバスをのせ、絵の具で描いている',
    '画架、イーゼル＝easel。', f'''
<g transform="translate(320, 356)">
  <path d="M-118 0l118-250M118 0L0-250M0 22v-272" fill="none" stroke="#8b6437" stroke-width="13" stroke-linecap="round"/>
  <path d="M-116-92h232v16h-232z" fill="#c9a464" class="o"/>
  <path d="M-94-298h188v212h-188z" class="o" fill="#fffefd"/>
  {blob(0, -230, 0.8, 'coral')}
  {blob(-40, -160, 0.7, 'teal')}
  {blob(38, -136, 0.6, 'gold')}
</g>
{person(118, 356, 1.1, 1, 'violet', 'blue', 'reach', 'short', 'smile')}
<path d="M172 240l42-26" fill="none" stroke="#8b6437" stroke-width="7" stroke-linecap="round"/>
<g transform="translate(216, 206)"><path d="M-8-10h16v14h-16z" class="coral o"/><path d="M-14 4h28l10 22h-48z" class="coralp o"/></g>
<g transform="translate(96, 296)"><ellipse rx="42" ry="30" class="goldp o"/><circle cx="-14" cy="-6" r="9" class="coral"/><circle cx="12" cy="2" r="9" class="teal"/></g>''')

add('east', '方位計の針が右をさし、右手の空から日がのぼる',
    '東、東の＝east。地図では右側にあたる方角。', f'''
<g transform="translate(212, 214)">
  <circle r="128" fill="#fffefd" class="o"/>
  <circle r="106" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M0-128v24M0 128v-24M128 0h-24M-128 0h24" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <path d="M0-18L-92 0 0 18z" fill="#fffdf6" class="o"/>
  <path d="M0-18l122 18L0 18z" class="coral o"/>
  <circle r="17" class="gold o"/>
</g>
<path d="M398 322a60 60 0 0 1 120 0z" class="goldp o"/>
<g fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round">
  <path d="M458 262v-26M404 274l-18-20M512 274l18-20"/>
</g>
<path d="M330 360h200" fill="none" stroke="{CRL}" stroke-width="8" stroke-linecap="round" marker-end="url(#ar)"/>''', arrow=True)

add('easy', '障害のないまっすぐな道を歩き、らくらくと目印に着く',
    '簡単な、やさしい、気楽な＝easy。', f'''
<path d="M60 348h480" class="a"/>
<path d="M110 348q190-26 336-8" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12"/>
{person(118, 356, 1.05, 1, 'teal', 'blue', 'walk', 'short', 'smile')}
<g transform="translate(470, 348)">
  <path d="M0 0v-142" fill="none" stroke="#8b6437" stroke-width="9"/>
  <path d="M0-142h88l-20 24 20 24H0z" class="green o"/>
</g>
{spark(280, 200, 1.7)}
{spark(360, 268, 1.3)}
{spark(210, 274, 1.2)}''')

add('eat', 'フォークで食べ物を口に運び、食事をとっている',
    '食べる＝eat。過去形は ate。', f'''
{table(300)}
<g transform="translate(330, 276)">
  <ellipse rx="88" ry="28" fill="#fffdf6" class="o"/>
  <ellipse rx="58" ry="16" fill="#f4ead9"/>
  <ellipse cx="0" cy="-4" rx="34" ry="16" class="gold o"/>
  <ellipse cx="-26" cy="2" rx="16" ry="10" class="green o"/>
</g>
{person(150, 356, 1.15, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
{fork(190, 292, 0.85, -20)}
<g transform="translate(170, 234)"><ellipse rx="18" ry="12" class="gold o"/><ellipse cx="12" cy="-4" rx="10" ry="8" class="green o"/></g>
<g transform="translate(452, 284)">
  <path d="M-28-40h56v78a28 28 0 0 1-28 28 28 28 0 0 1-28-28z" fill="#dfe9f2" class="o"/>
  <path d="M-24-16h48v26a24 24 0 0 1-24 24 24 24 0 0 1-24-24z" class="blue"/>
</g>''')

add('sardine', '開けた缶に小さなイワシが並び、手前に一匹が置かれている',
    'イワシ、イワシの缶詰＝sardine。', f'''
{fish(300, 168, 1.2, 'blue')}
{spark(486, 118, 1.3)}
<g transform="translate(296, 328)">
  <path d="M-146-30h292v60h-292z" rx="12" class="paper"/>
  <path d="M-146-30h292v60h-292z" fill="none" class="o"/>
  <path d="M146-30q40 0 40 30t-40 30z" fill="#c3cbd1" class="o"/>
  <path d="M146-30q-24 30 0 60" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
{fish(236, 320, 0.52, 'blue', 1)}
{fish(308, 318, 0.52, 'blue', -1)}
{fish(378, 320, 0.52, 'blue', 1)}
<path d="M60 386h480" class="a"/>''')

finish(__file__)
