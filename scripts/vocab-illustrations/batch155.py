# -*- coding: utf-8 -*-
"""第155回。ca-/ce-/ch-/cl-/co- の名詞と慣用表現。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
W = []
def add(slug, alt, body, **k): W.append(emit(slug, alt, body, **k))
BRN='#8b6437'
def table(y=300):
    return (f'<path d="M40 {y}h520v20H40z" fill="#c9a464" class="o"/>'
            f'<path d="M80 {y+20}v60M520 {y+20}v60" stroke="#a0764a" stroke-width="14" stroke-linecap="round" fill="none"/>')
def split():
    return f'<path d="M300 20v360" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" fill="none"/>'
def coin(x, y, r=20):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" class="gold o"/>'
            f'<circle cx="{x}" cy="{y}" r="{r*0.62}" fill="none" stroke="{TONES["gold"][2]}" stroke-width="2.5"/>')
def cross(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["coral"][0]}" stroke-width="{9*s}" stroke-linecap="round">'
            f'<path d="M{x-26*s} {y-26*s}l{52*s} {52*s}M{x+26*s} {y-26*s}l{-52*s} {52*s}"/></g>')
def tick(x, y, s=1):
    return (f'<g fill="none" stroke="{TONES["green"][0]}" stroke-width="{9*s}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x-30*s} {y}l{22*s} {24*s} {42*s}-{52*s}"/></g>')
def doc(x, y, w=100, h=130, lines=4):
    g = [f'<g transform="translate({x} {y})"><path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" class="paper"/>']
    for i in range(lines):
        g.append(f'<rect x="{-w/2+14}" y="{-h/2+22+i*(h-50)/max(lines,1):.0f}" width="{w-28-(i%3)*16}" height="8" rx="4" fill="{MUTED}"/>')
    g.append('</g>')
    return ''.join(g)
def head(x, y, r=22, shirt='teal', hair='short'):
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>'
            f'<path d="{HAIRS[hair]}" transform="translate(0 108) scale({r/24:.2f})" fill="{HAIR}"/>'
            f'<circle cx="{-r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<circle cx="{r*0.33:.0f}" cy="{-r*0.17:.0f}" r="2.4" fill="{INK}"/>'
            f'<path d="M{-r*0.3:.0f} {r*0.35:.0f}q{r*0.3:.0f} {r*0.3:.0f} {r*0.6:.0f} 0" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{-r*1.1:.0f} {r*1.5:.0f}q{r*1.1:.0f}-{r*0.6:.0f} {r*2.2:.0f} 0l-{r*0.3:.0f} {r*1.2:.0f}h-{r*1.6:.0f}z" fill="{TONES[shirt][0]}" class="o"/></g>')
def word(x, y, n=5, w=26, cls=None, bad=-1):
    """文字は描けないので、語を四角の並びで表す。bad の位置だけ形を崩す。"""
    g = [f'<g transform="translate({x} {y})">']
    for i in range(n):
        cx = -(n-1)*w/2 + i*w
        if i == bad:
            g.append(f'<rect x="{cx-9}" y="-11" width="18" height="22" rx="4" fill="{TONES["coral"][0]}" transform="rotate(18 {cx} 0)"/>')
        else:
            g.append(f'<rect x="{cx-9}" y="-11" width="18" height="22" rx="4" fill="{cls or INK}"/>')
    g.append('</g>')
    return ''.join(g)

GLD, GLDP, GLDD = TONES['gold']
CRL, CRLP, CRLD = TONES['coral']
GRN, GRNP, GRND = TONES['green']
BLU, BLUP, BLUD = TONES['blue']
TEA, TEAP, TEAD = TONES['teal']
VIO, VIOP, VIOD = TONES['violet']

def spark(x, y, s=1, cls='gold'):
    return (f'<path d="M{x} {y-16*s}l{5*s} {11*s} {11*s} {5*s}-{11*s} {5*s}-{5*s} {11*s}'
            f'-{5*s}-{11*s}-{11*s}-{5*s} {11*s}-{5*s}z" class="{cls} o"/>')

def ring(x, y, r=64, dash=False, cls='coral'):
    d = ' stroke-dasharray="11 10"' if dash else ''
    c = MUTED if dash else TONES[cls][0]
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="4"{d}/>'

def torso(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0-190a44 44 0 1 1 0 88 44 44 0 1 1 0-88z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>'
            f'<path d="M-90-96q90-30 180 0 20 130 0 226h-180q-20-96 0-226z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>')

def bars(x, y, n=6, h=200, gap=34):
    return ''.join(f'<path d="M{x+i*gap} {y}v{-h}" fill="none" stroke="{INK}" stroke-width="8"/>' for i in range(n))

def clock(x, y, s=1, h=5, m=0):
    ah = math.radians(h*30 + m*0.5 - 90); am = math.radians(m*6 - 90)
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="54" fill="#fffefd" class="o"/>'
            f'<path d="M0 0l{42*math.cos(am):.0f} {42*math.sin(am):.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M0 0l{28*math.cos(ah):.0f} {28*math.sin(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle r="4" class="ink"/></g>')

# --- からだ・食べもの ---------------------------------------------------------

add('capillary', '太い血管から枝分かれした、髪の毛ほどの細い管', f'''
<path d="M40 200h150" fill="none" stroke="{CRL}" stroke-width="28" stroke-linecap="round"/>
<g fill="none" stroke="{CRL}" stroke-linecap="round">
  <path d="M190 200q60-60 110-70" stroke-width="14"/><path d="M190 200q60 60 110 70" stroke-width="14"/>
  <path d="M300 130q50-30 90-30M300 130q40 10 70 40M300 270q50 30 90 30M300 270q40-10 70-40" stroke-width="7"/>
  {''.join(f'<path d="M{390+ (i%2)*10} {70+i*22}q50-6 90 {-10+i*6}" stroke-width="3"/>' for i in range(11))}</g>
{ring(490, 200, 100)}''')

add('cartilage', 'ひざの骨の先にある、やわらかい層', f'''
<g transform="translate(300 200)">
  <path d="M-40-160h80v120h-80z" fill="#e8e2d4" class="o"/>
  <path d="M-46 40h92v130h-92z" fill="#e8e2d4" class="o"/>
  <path d="M-52-40q52-26 104 0 10 46-52 60-62-14-52-60z" class="tealp o"/>
  <path d="M-46 22q46-20 92 0" fill="none" stroke="{TEA}" stroke-width="4"/></g>
{ring(300, 190, 106)}''')

add('carbohydrate', 'ごはん・パン・めん。力のもとになる栄養', f'''
{table(330)}
<g transform="translate(140 280)"><path d="M-64 0q0 24 64 24t64-24z" fill="#fffefd" class="o"/>
  <path d="M-64 0q10-56 64-56t64 56z" class="goldp o"/></g>
<g transform="translate(300 280)"><path d="M-70 0q-14-70 0-84 70-16 140 0 14 14 0 84z" fill="#c98f52" class="o"/>
  <path d="M-50-70q50-12 100 0" fill="none" stroke="#a8703a" stroke-width="4"/></g>
<g transform="translate(460 286)"><ellipse rx="80" ry="22" fill="#fffefd" class="o"/>
  {''.join(f'<path d="M{-56+i*24} -6q14-24 28 0" fill="none" stroke="{GLD}" stroke-width="6" stroke-linecap="round"/>' for i in range(5))}</g>''')

add('caregiver', 'お年寄りに寄りそって、歩くのを支える', f'''
{person(230, 306, 1.25, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
<g transform="translate(380 306)">
  <path d="M-12-8l-6 30M10-8l6 30" fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-72q26-14 52 0l-9 66h-36z" fill="{VIOP}" class="o"/>
  <path d="M-24-64l-30 10M24-66l26 24" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="0" cy="-100" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 4)" fill="#c9cfd4"/>
  <circle cx="-8" cy="-96" r="2.4" class="ink"/><circle cx="8" cy="-96" r="2.4" class="ink"/>
  <path d="M-7-82q7 6 14 0" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
<path d="M310 232l46-6" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
<path d="M430 282v70" fill="none" stroke="{GLDD}" stroke-width="8" stroke-linecap="round"/>
<path d="M416 282h28" fill="none" stroke="{GLDD}" stroke-width="8" stroke-linecap="round"/>''')

add('carer', '寝ている人のそばで、食事と薬の世話をする', f'''
<g transform="translate(340 340)"><path d="M-160 0v-40h320V0z" class="goldd o"/>
  <path d="M-160-40v-90h30v90zM130-40v-56h30v56z" class="goldd o"/>
  <path d="M-130-40v-30h260v30z" class="tealp o"/>
  <path d="M-124-70q-6-26 30-26h50v26z" fill="#fffefd" class="o"/></g>
{head(216, 262, 26, 'violet', 'short')}
{person(120, 340, 1.2, 1, 'coral', 'blue', 'carry', 'bun', 'smile')}
<g transform="translate(134 246)"><ellipse rx="54" ry="14" fill="#fffefd" class="o"/>
  <circle cx="-14" cy="-10" r="12" class="greenp o"/>
  <rect x="12" y="-16" width="26" height="14" rx="7" class="coral o"/></g>''')

# --- 捕らわれ・停止 -----------------------------------------------------------

add('captive', 'つかまって、囲いの中から出られない人', f'''
<g transform="translate(300 306)"><path d="M-140 0v-230h280V0z" fill="#fffefd" class="o"/></g>
{person(300, 306, 1.2, 1, 'coral', 'blue', 'stand', 'short', 'sad')}
{bars(180, 306, 8, 230, 34)}
<path d="M160 76h300" fill="none" stroke="{INK}" stroke-width="8"/>
{ring(300, 210, 118)}''')

add('captivity', '野に生きるはずの動物が、おりの中で暮らす', f'''
{split()}
<g transform="translate(150 306)"><path d="M-130 0q10-90 130-110 120 20 130 110z" class="greenp o"/>
  {tree(-90, 0, 0.6)}{tree(96, 0, 0.5)}</g>
<g transform="translate(150 250) scale(0.34)">{beast(0, 0, 1, '#8a6a48', 1)}</g>
{ring(150, 250, 122, True)}
<g transform="translate(450 306)"><path d="M-130 0v-200h260V0z" fill="#f2f5f6" class="o"/></g>
<g transform="translate(450 250) scale(0.34)">{beast(0, 0, 1, '#8a6a48', 1)}</g>
{bars(330, 306, 8, 200, 34)}
<path d="M316 106h270" fill="none" stroke="{INK}" stroke-width="8"/>
{ring(450, 230, 132)}''')

add('ceasefire', '決めた時刻を境に、撃ち合いがぴたりと止まる', f'''
<path d="M60 260h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
{''.join(f'<path d="M{90+i*40} 260v-{40+(i%3)*24}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for i in range(6))}
<path d="M340 130v170" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="14 10"/>
{''.join(f'<path d="M{380+i*40} 260v-{40+(i%3)*24}" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="8 7"/>' for i in range(4))}
{clock(340, 90, 0.6, 12, 0)}
{person(120, 340, 0.9, 1, 'teal', 'blue', 'stand', 'cap', 'neutral')}
{person(500, 340, 0.9, -1, 'coral', 'blue', 'stand', 'cap', 'neutral')}''')

add('cessation', '出ていたものが、栓を閉めてぴたりと止まる', f'''
<g transform="translate(200 130)"><path d="M-90-40h40v50h-40z" class="teald o"/>
  <path d="M-50-30h100v22h-30v40h-24v-40h-46z" class="teal o"/>
  <path d="M40-40q26 0 26-20t-26-20" fill="none" stroke="{TEAD}" stroke-width="9"/></g>
<path d="M224 152v56" fill="none" stroke="{BLU}" stroke-width="14" stroke-linecap="round"/>
<path d="M224 220v100" fill="none" stroke="{MUTED}" stroke-width="8" stroke-dasharray="12 12"/>
<g transform="translate(224 320)"><ellipse rx="70" ry="18" fill="{BLUP}" class="o"/></g>
{hand(330, 110, -1)}''')

add('coercion', 'いやがる手を押さえつけて、無理に署名させる', f'''
{table(280)}
{doc(220, 210, 170, 200, 4)}
{person(120, 380, 1.15, 1, 'teal', 'blue', 'reach', 'short', 'sad')}
<g transform="translate(300 180)">{hand(0, 0, 1)}</g>
<g transform="translate(300 96) scale(1.6 1.2)">{hand(0, 0, 1)}</g>
<path d="M300 130v26" class="a" stroke-width="6" marker-end="url(#ar)"/>
{person(470, 380, 1.3, -1, 'violet', 'blue', 'reach', 'short', 'neutral')}''', arrow=True)

add('concealment', '布をかぶせて、そこにあるものを見えなくする', f'''
{table(340)}
<g opacity="0.35">{box(200, 290, 110, 76, 24, 'coral')}</g>
<g transform="translate(200 280)"><path d="M-96 26q-20-70 0-96 96-40 192 0 20 26 0 96q-96 20-192 0z" fill="#dfe6ea" class="o"/>
  <path d="M-96 26q96 20 192 0" fill="none" stroke="{MUTED}" stroke-width="4"/></g>
{hand(360, 180, -1)}
{head(510, 250, 26, 'teal', 'short')}
<path d="M470 240l-60 20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

# --- 検閲・調査 --------------------------------------------------------------

add('censor', '筆で塗りつぶして、都合の悪い部分を消す人', f'''
{doc(230, 200, 220, 260, 0)}
{''.join(f'<rect x="{140+ (i%2)*0}" y="{110+i*46}" width="{180-(i%2)*50}" height="14" rx="7" fill="{MUTED}"/>' for i in range(5))}
<rect x="140" y="156" width="130" height="14" fill="{INK}"/>
<rect x="140" y="248" width="160" height="14" fill="{INK}"/>
<g transform="translate(400 150) rotate(28)"><path d="M-9-90h18v110h-18z" class="goldd o"/>
  <path d="M-13 20h26l-13 40z" fill="{INK}"/></g>
{head(510, 300, 26, 'violet', 'short')}''')

add('censorship', '出す前に必ず削られる、そのしくみ', f'''
{doc(150, 200, 170, 210, 0)}
{''.join(f'<rect x="86" y="{120+i*40}" width="{130-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}
<path d="M250 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(340 200)"><rect x="-34" y="-140" width="68" height="280" rx="8" class="teald o"/>
  <circle cy="0" r="24" class="ink"/></g>
{doc(470, 200, 170, 210, 0)}
{''.join(f'<rect x="406" y="{120+i*40}" width="{130-(i%2)*40}" height="12" rx="6" fill="{INK if i in (1,3) else MUTED}"/>' for i in range(4))}''', arrow=True)

add('census', '一軒ずつたずねて、住む人の数を書きとめる', f'''
{''.join(f'<g transform="translate({120+i*160} 300)"><path d="M-56 0v-70h112V0z" fill="#fffefd" class="o"/>'
         f'<path d="M-66-70L0-116l66 46z" class="{c}d o"/></g>' for i, c in enumerate(['coral','teal','violet']))}
{''.join(f'<g transform="translate({120+i*160} 340)">{head(0, 0, 18, c, h)}</g>' for i, (c, h) in enumerate([('gold','short'),('green','bob'),('blue','short')]))}
{person(500, 380, 1.1, -1, 'violet', 'blue', 'carry', 'bun', 'neutral')}
<g transform="translate(486 280) rotate(-8)"><rect x="-46" y="-58" width="92" height="116" rx="6" class="paper"/>
  {''.join(f'<rect x="-32" y="{-40+i*26}" width="64" height="8" rx="4" fill="{MUTED}"/>' for i in range(4))}
  <rect x="-16" y="-70" width="32" height="14" rx="4" class="ink"/></g>''')

add('citation', '引用のしるしをつけて、もとの本を示す', f'''
{doc(200, 190, 220, 260, 0)}
{''.join(f'<rect x="110" y="{110+i*46}" width="{180-(i%2)*50}" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}
<g transform="translate(200 260)"><rect x="-80" y="-18" width="160" height="36" rx="6" class="tealp o"/>
  <path d="M-92-18q-14 20 0 36M92-18q14 20 0 36" fill="none" stroke="{TEA}" stroke-width="7"/></g>
<path d="M320 280h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 300)"><path d="M-70-100h140v200h-140z" class="coral o"/>
  <path d="M-70-100h20v200h-20z" class="corald o"/>
  <rect x="-32" y="-60" width="90" height="12" rx="6" fill="#fffefd"/></g>''', arrow=True)

add('caveat', '本文の下に小さく添えた、ただし書き', f'''
{doc(300, 190, 340, 290, 0)}
{''.join(f'<rect x="150" y="{100+i*40}" width="{300-(i%2)*80}" height="14" rx="7" fill="{MUTED}"/>' for i in range(4))}
<path d="M150 280h300" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(180 306)"><path d="M0-20l20 34h-40z" class="gold o"/>
  <path d="M0-8v6" fill="none" stroke="{INK}" stroke-width="3"/><circle cy="8" r="2" class="ink"/></g>
{''.join(f'<rect x="210" y="{300+i*20}" width="{200-(i%2)*60}" height="8" rx="4" fill="{CRL}"/>' for i in range(2))}
{ring(300, 314, 140)}''')

# --- 音・もの ----------------------------------------------------------------

add('clang', '金属をひとつ打って、大きくひびく音', f'''
<g transform="translate(220 200)"><path d="M0-110q70 0 70 90 0 30 20 40h-180q20-10 20-40 0-90 70-90z" class="goldp o"/>
  <path d="M-100 20h200v16h-200z" class="goldd o"/>
  <path d="M0-110v-24" fill="none" stroke="{INK}" stroke-width="6"/>
  <ellipse cy="52" rx="16" ry="20" class="goldd o"/></g>
{''.join(f'<path d="M330 {200-40-i*34}q{40+i*34} {40+i*34} 0 {(40+i*34)*2}" fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round"/>' for i in range(3))}''')

add('clatter', '食器がいくつも重なって、がちゃがちゃ鳴る', f'''
{table(340)}
{''.join(f'<g transform="translate({200+ (i%3)*80} {250+(i//3)*40}) rotate({-30+i*22})">'
         f'<ellipse rx="46" ry="12" fill="#fffefd" class="o"/></g>' for i in range(6))}
{''.join(f'<path d="M{110+ (i%3)*34} {150+(i//3)*40}q14 14 0 28" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(6))}
{''.join(f'<path d="M{440+ (i%3)*34} {140+(i//3)*40}q-14 14 0 28" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(6))}''')

add('chord', '鍵盤を三つ同時に押して出す、重なった音', f'''
<g transform="translate(300 280)">
  {''.join(f'<rect x="{-238+i*68}" y="-90" width="66" height="180" rx="5" fill="#fffefd" class="o"/>' for i in range(7))}
  {''.join(f'<rect x="{-190+i*68}" y="-90" width="34" height="110" rx="4" class="ink"/>' for i in [0, 1, 3, 4, 5])}
  <rect x="-238" y="-90" width="66" height="180" rx="5" class="tealp o"/>
  <rect x="-102" y="-90" width="66" height="180" rx="5" class="tealp o"/>
  <rect x="34" y="-90" width="66" height="180" rx="5" class="tealp o"/></g>
{''.join(f'<g transform="translate({150+i*60} {110-i*22})"><ellipse rx="16" ry="12" class="coral o" transform="rotate(-20)"/>'
         f'<path d="M15-6v-50" fill="none" stroke="{CRLD}" stroke-width="5"/></g>' for i in range(3))}''')

add('chapel', '小さな礼拝堂', f'''
<g transform="translate(300 306)">
  <path d="M-110 0v-150h220V0z" fill="#fffefd" class="o"/>
  <path d="M-124-150L0-250l124 100z" class="corald o"/>
  <path d="M-30 0v-90q0-30 30-30t30 30V0z" class="coral o"/>
  <path d="M-70-116q0-30 30-30t30 30v40h-60zM10-116q0-30 30-30t30 30v40h-60z" class="tealp o"/>
  <path d="M0-258v-40M-18-282h36" fill="none" stroke="{GLDD}" stroke-width="9" stroke-linecap="round"/></g>
{tree(90, 330, 0.6)}{tree(520, 330, 0.55)}''')

add('clover', '三つ葉のなかに、まれな四つ葉', f'''
<path d="M0 330h600v70H0z" class="ground"/>
{''.join(f'<g transform="translate({110+i*130} 300)"><path d="M0 0v-46" fill="none" stroke="{GRND}" stroke-width="5"/>'
         f'{"".join(f2 for f2 in [f"<circle cx=@{26*math.cos(math.radians(a)):.0f}@ cy=@{-46+26*math.sin(math.radians(a)):.0f}@ r=@22@ class=@greenp o@/>".replace("@", chr(34)) for a in [210, 330, 90]])}</g>' for i in range(3))}
<g transform="translate(500 300)"><path d="M0 0v-46" fill="none" stroke="{GRND}" stroke-width="5"/>
  {''.join(f'<circle cx="{28*math.cos(math.radians(a)):.0f}" cy="{-46+28*math.sin(math.radians(a)):.0f}" r="24" class="green o"/>' for a in [225, 315, 45, 135])}</g>
{ring(500, 254, 78)}''')

add('cockroach', '長いひげをもつ、平たい虫', f'''
<g transform="translate(300 220)">
  <ellipse rx="110" ry="70" fill="#6b4a2c" class="o"/>
  <ellipse cy="-56" rx="56" ry="36" fill="#5a3d24" class="o"/>
  <path d="M0-70v130" fill="none" stroke="#4a3220" stroke-width="4"/>
  <path d="M-40-84q-60-40-90-90M40-84q60-40 90-90" fill="none" stroke="#4a3220" stroke-width="7" stroke-linecap="round"/>
  {''.join(f'<path d="M{-96+ (i%3)*0} {-30+ (i%3)*44}l-70 {-20+(i%3)*30}" fill="none" stroke="#4a3220" stroke-width="7" stroke-linecap="round"/>' for i in range(3))}
  {''.join(f'<path d="M{96} {-30+ (i%3)*44}l70 {-20+(i%3)*30}" fill="none" stroke="#4a3220" stroke-width="7" stroke-linecap="round"/>' for i in range(3))}
  <circle cx="-22" cy="-64" r="5" fill="#fffefd"/><circle cx="22" cy="-64" r="5" fill="#fffefd"/></g>''')

add('cocoon', '枝にぶら下がる、糸で包まれたまゆ', f'''
<path d="M60 110q120 20 240 30" fill="none" stroke="{GRND}" stroke-width="12"/>
<g transform="translate(250 250)"><ellipse rx="60" ry="106" fill="#e6dcc0" class="o"/>
  {''.join(f'<path d="M-58 {-70+i*34}q58 20 116 0" fill="none" stroke="#c9bb96" stroke-width="4"/>' for i in range(5))}
  <path d="M0-106v-30" fill="none" stroke="#c9bb96" stroke-width="5"/></g>
<g transform="translate(460 280)"><path d="M-60 0q-16-30 16-40 26-8 44 8t44-8q32 10 16 40-40 20-120 0z" class="violetp o"/>
  <ellipse rx="16" ry="34" class="violet o"/>
  <path d="M-8-34l-16-24M8-34l16-24" fill="none" stroke="{VIOD}" stroke-width="4"/></g>''')

add('cod', 'あごの下にひげが一本ある、大きな白身の魚', f'''
<path d="M0 260h600v140H0z" fill="{BLUP}"/>
<g transform="translate(300 210)">
  <path d="M-160 0q60-80 170-60 70 14 110 60-40 46-110 60-110 20-170-60z" fill="#8fa2a8" class="o"/>
  <path d="M120 0l60-46v92z" fill="#8fa2a8" class="o"/>
  <path d="M-40-56q30-40 50-6-30 8-50 6zM-30 56q30 40 50 6-30-8-50-6z" fill="#7d8f96" class="o"/>
  <circle cx="-104" cy="-14" r="9" fill="#fffefd" class="o"/><circle cx="-104" cy="-14" r="4" class="ink"/>
  <path d="M-140 22q-6 34-26 40" fill="none" stroke="#7d8f96" stroke-width="6" stroke-linecap="round"/>
  <path d="M-80-20q60-16 120 0" fill="none" stroke="#7d8f96" stroke-width="4"/></g>
{ring(180, 250, 66)}''')

# --- 社会 --------------------------------------------------------------------

add('civility', 'ぶつからないよう、たがいに会釈して道をゆずる', f'''
<g transform="translate(200 306)">
  <path d="M-14-8l-8 30M14-8l8 30" fill="none" stroke="{BLUD}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-76q26-13 52 0l-8 68h-36z" fill="{TEA}" class="o"/>
  <path d="M-22-70l6 44M22-70l-6 44" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="6" cy="-104" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5" transform="rotate(16 0 -80)"/>
  <path d="{HAIRS['short']}" transform="translate(6 4) rotate(16 0 -104)" fill="{HAIR}"/>
  <path d="M-2-100l8 4M14-102l-8 4" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
<g transform="translate(410 306) scale(-1 1)">
  <path d="M-14-8l-8 30M14-8l8 30" fill="none" stroke="{BLUD}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-76q26-13 52 0l-8 68h-36z" fill="{CRL}" class="o"/>
  <path d="M-22-70l6 44M22-70l-6 44" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="6" cy="-104" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5" transform="rotate(16 0 -80)"/>
  <path d="{HAIRS['bob']}" transform="translate(6 4) rotate(16 0 -104)" fill="{HAIR}"/></g>
{''.join(spark(x, y, 0.7) for x, y in [(300,120),(300,220)])}''')

add('clan', '同じ紋を分けもつ、ひとつの一族', f'''
<g transform="translate(300 90)"><path d="M0-56l48 28v56L0 56l-48-28v-56z" class="violet o"/>
  <circle r="18" fill="#fffefd" class="o"/></g>
<path d="M300 150v40M140 190h320M140 190v30M300 190v30M460 190v30" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<g transform="translate({140+i*160} 250)">{head(0, 0, 30, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun')]))}
{''.join(f'<g transform="translate({140+i*160} 296)"><path d="M0-16l14 8v16L0 32l-14-8v-16z" class="violetp o"/></g>' for i in range(3))}
<path d="M140 330v20M460 330v20M100 350h80M420 350h80" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<g transform="translate({x} 380)">{head(0, 0, 20, c, h)}</g>' for x, (c, h) in zip([100, 180, 420, 500], [('green','short'),('blue','bob'),('violet','short'),('gold','cap')]))}''')

add('comrade', '同じしるしを胸につけて、肩を並べる', f'''
{person(210, 306, 1.25, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
{person(390, 306, 1.25, 1, 'teal', 'blue', 'stand', 'cap', 'neutral')}
<path d="M210 200q90-40 180 0" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/>
{''.join(f'<g transform="translate({x} 232)"><path d="M0-18l16 10v18L0 38l-16-10v-18z" class="coral o"/></g>' for x in [232, 368])}
<g transform="translate(300 90)"><path d="M0 0v-40" fill="none" stroke="{INK}" stroke-width="0"/></g>''')

add('companionship', 'ひとりで歩く道と、連れがいる道の対比', f'''
{split()}
{person(150, 320, 1.1, 1, 'blue', 'blue', 'walk', 'short', 'sad')}
{ring(150, 220, 122, True)}
{person(400, 320, 1.1, 1, 'coral', 'blue', 'walk', 'short', 'smile')}
{person(500, 320, 1.1, 1, 'teal', 'blue', 'walk', 'bob', 'smile')}
<path d="M400 214q50-30 100 0" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
{ring(450, 220, 132)}''')

add('coexistence', 'ちがう生きものが、同じ場所で共に暮らす', f'''
<path d="M0 300q140-30 300-26t300 26v100H0z" class="greenp o"/>
{tree(120, 320, 1.0)}{tree(500, 320, 0.9)}
<g transform="translate(240 300) scale(0.36)">{beast(0, 0, 1, '#8a6a48', 1)}</g>
<g transform="translate(400 306)"><ellipse rx="46" ry="34" class="teal o"/>
  <circle cx="-34" cy="-30" r="22" class="teal o"/>
  <path d="M-50-44l-10-24 26 12" class="teal o"/>
  <circle cx="-38" cy="-32" r="5" class="ink"/>
  <path d="M40 10l30 24" fill="none" stroke="{TEAD}" stroke-width="7" stroke-linecap="round"/></g>
{''.join(spark(x, y, 0.7) for x, y in [(320,150)])}''')

add('cohesion', 'ばらばらの粒が、しっかりまとまってくっつく', f'''
{split()}
{''.join(f'<circle cx="{80+ (i%3)*60}" cy="{130+(i//3)*70}" r="24" class="tealp o"/>' for i in range(9))}
{ring(150, 200, 132, True)}
<g transform="translate(450 200)">
  {''.join(f'<circle cx="{52*math.cos(math.radians(a)):.0f}" cy="{52*math.sin(math.radians(a)):.0f}" r="28" class="teal o"/>' for a in range(0, 360, 60))}
  <circle r="28" class="teal o"/>
  <circle r="96" fill="none" stroke="{TEAD}" stroke-width="6"/></g>
{ring(450, 200, 132)}''')

add('coldness', 'よそよそしく背を向け、あいだに冷たい空気が流れる', f'''
{person(160, 306, 1.2, -1, 'teal', 'blue', 'stand', 'bun', 'neutral')}
{person(440, 306, 1.2, 1, 'coral', 'blue', 'stand', 'short', 'neutral')}
{''.join(f'<path d="M{280+ (i%2)*40} {130+i*44}l6 14 14 6-14 6-6 14-6-14-14-6 14-6z" fill="{BLU}"/>' for i in range(4))}
<g fill="none" stroke="{BLU}" stroke-width="4" stroke-dasharray="10 9">
  <path d="M240 200h-40M400 200h40"/></g>''')

add('commemoration', '記念の日に集まり、碑に花をささげる', f'''
<g transform="translate(300 306)"><path d="M-90 0v-30h180V0z" fill="#c3cbd1" class="o"/>
  <path d="M-60-30v-160h120v160z" fill="#dfe6ea" class="o"/>
  <path d="M-40-150h80v14h-80zM-40-110h80v14h-80z" fill="{MUTED}"/></g>
<g transform="translate(300 300)"><circle r="46" fill="none" stroke="{GRN}" stroke-width="14"/>
  {''.join(f'<circle cx="{46*math.cos(math.radians(a)):.0f}" cy="{46*math.sin(math.radians(a)):.0f}" r="9" class="coral o"/>' for a in range(0, 360, 60))}</g>
{''.join(f'<g transform="translate({x} 366)">{head(0, 0, 24, c, h)}</g>' for x, (c, h) in zip([120, 190, 410, 480], [('teal','short'),('violet','bob'),('gold','bun'),('blue','short')]))}''')

add('commonplace', 'どこにでもあるので、だれも目を留めない', f'''
{''.join(f'<path d="M40 {130+i*90}h520v10H40z" class="goldd o"/>' for i in range(2))}
{''.join(f'<g transform="translate({80+ (i%6)*88} {110+(i//6)*90})"><rect x="-28" y="-30" width="56" height="60" rx="6" class="tealp o"/></g>' for i in range(12))}
{person(300, 380, 1.0, 1, 'coral', 'blue', 'walk', 'short', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M340 300h120"/></g>''')

add('compilation', 'ばらばらの紙を集めて、一冊にまとめる', f'''
{''.join(f'<g transform="translate({100+ (i%2)*70} {150+(i//2)*80}) rotate({-16+i*12})">'
         f'<rect x="-40" y="-52" width="80" height="104" rx="4" class="paper"/>'
         f'<rect x="-26" y="-34" width="52" height="8" rx="4" fill="{MUTED}"/></g>' for i in range(6))}
<path d="M290 220h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 220)"><path d="M-90-130h180v260h-180z" class="teal o"/>
  <path d="M-90-130h22v260h-22z" class="teald o"/>
  <rect x="-36" y="-70" width="100" height="14" rx="7" fill="#fffefd"/>
  <rect x="-36" y="-40" width="70" height="10" rx="5" fill="#fffefd" opacity="0.7"/></g>''', arrow=True)

add('comprehension', '読んだ文が、頭の中で絵になって分かる', f'''
{doc(160, 200, 190, 240, 0)}
{''.join(f'<rect x="90" y="{120+i*46}" width="{150-(i%2)*40}" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}
{head(300, 330, 26, 'teal', 'short')}
<path d="M270 250l-40-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
<g transform="translate(450 170)"><ellipse rx="126" ry="92" fill="#fffefd" class="o"/>
  <path d="M-90 50l60-80 44 44 40-56 66 92z" class="greenp o"/>
  {sun(66, -40, 24)}</g>
<circle cx="336" cy="280" r="9" fill="#fffefd" class="o"/>''')

add('compression', '高く積んだものを、小さく押しかためる', f'''
{''.join(f'<rect x="90" y="{300-i*40}" width="130" height="34" rx="5" class="tealp o"/>' for i in range(6))}
<path d="M270 200h60" class="a" marker-end="url(#ar)"/>
<rect x="400" y="252" width="130" height="52" rx="5" class="teal o"/>
<path d="M465 190v46" class="a" stroke-width="6" marker-end="url(#ar)"/>
<path d="M400 170h130" fill="none" stroke="{INK}" stroke-width="10"/>''', arrow=True)

add('come to terms with', '押しのけていた事実を、やがて受け入れる', f'''
{split()}
{person(90, 306, 1.05, 1, 'coral', 'blue', 'reach', 'short', 'sad')}
<g transform="translate(210 230)">{doc(0, 0, 110, 140, 3)}</g>
<path d="M170 240h-30" fill="none" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/>
{person(380, 306, 1.05, 1, 'teal', 'blue', 'carry', 'short', 'neutral')}
<g transform="translate(400 226)">{doc(0, 0, 110, 140, 3)}</g>
{ring(430, 220, 130)}''', arrow=True)

# --- 慣用・その他 -------------------------------------------------------------

add('cannot help but', '止めようとしても、つい笑ってしまう', f'''
{person(240, 306, 1.3, 1, 'teal', 'blue', 'hold', 'short', 'smile')}
<path d="M212 190q28 24 56 0" fill="none" stroke="{INK}" stroke-width="5"/>
{''.join(f'<path d="M{330+i*34} {150+i*18}q14-16 28 0" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(3))}
{hand(240, 240, 1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M240 268v30"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(140,150),(460,270)])}''')

add('clear up', '散らかった机を、きれいに片づける', f'''
{split()}
{table(320)}
{''.join(f'<g transform="translate({100+ (i%3)*50} {270-(i//3)*40}) rotate({-30+i*24})">'
         f'<rect x="-30" y="-20" width="60" height="40" rx="4" class="paper"/></g>' for i in range(6))}
{ring(150, 250, 120, True)}
{''.join(f'<g transform="translate({450} {280-i*32})"><rect x="-56" y="-14" width="112" height="28" rx="4" class="paper"/></g>' for i in range(3))}
{''.join(spark(x, y, 0.8) for x, y in [(370,150),(540,160)])}
{ring(450, 244, 128)}''')

add('clearance', '売り切ってしまうための、値下げの札', f'''
<g transform="translate(300 306)"><path d="M-190 0v-140h380V0z" fill="#fffefd" class="o"/>
  <path d="M-204-140h408l-30-40h-348z" class="coral o"/>
  {''.join(f'<path d="M{-150+i*100} 0v-70h70v70z" fill="#eef2f4" class="o"/>' for i in range(4))}</g>
{''.join(f'<g transform="translate({140+i*110} 120) rotate({-8+i*6})"><path d="M-46-26h72l20 26-20 26h-72z" class="gold o"/>'
         f'<circle cx="26" cy="0" r="6" class="ink"/><path d="M-30-8h30" fill="none" stroke="{CRLD}" stroke-width="6"/></g>' for i in range(4))}''')

add('clickbait', 'あおる見出しを餌にして、思わずかからせる', f'''
<g transform="translate(240 200)"><rect x="-160" y="-70" width="320" height="140" rx="10" class="paper"/>
  {word(0, -20, 4, 50, CRL)}
  <rect x="-120" y="24" width="240" height="12" rx="6" fill="{MUTED}"/>
  <g class="corals" stroke-width="5">{''.join(f'<path d="M0 -100v-24" transform="rotate({d})"/>' for d in [-30, 0, 30])}</g></g>
<path d="M400 90v100q0 60-56 60t-56-40" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
<g transform="translate(420 320)"><path d="M0-40l40 76-18 4 12 24-14 6-12-24-14 12z" fill="#fffefd" class="o"/></g>''')

add('collateral', '借りるかわりに、家の権利を預ける', f'''
{table(280)}
{person(120, 380, 1.15, 1, 'teal', 'blue', 'give', 'short', 'neutral')}
<g transform="translate(240 210)"><path d="M-56 0v-56h112V0z" fill="#fffefd" class="o"/>
  <path d="M-66-56L0-100l66 44z" class="corald o"/></g>
<path d="M310 160h60" class="a" marker-end="url(#ar)"/>
<path d="M370 250h-60" class="a" marker-end="url(#ar)"/>
{''.join(coin(410 + i*44, 210, 22) for i in range(2))}
{person(530, 380, 1.15, -1, 'violet', 'blue', 'give', 'bun', 'neutral')}''', arrow=True)

add('colon', 'ことばの後ろに置いて、次を導く二つの点', f'''
{word(180, 200, 3, 40, INK)}
<g transform="translate(310 200)"><circle cy="-26" r="13" class="coral o"/><circle cy="26" r="13" class="coral o"/></g>
{word(450, 200, 4, 34, TEA)}
{ring(310, 200, 62)}''')

add('combustion', '燃えるものと空気がそろって、炎が上がる', f'''
{table(340)}
<g transform="translate(230 306)"><path d="M-70 0q-10-30 20-34l90-6q30 0 24 24l-10 16z" fill="#8c6b42" class="o"/>
  <path d="M-40-34l30-30h70l-24 30" fill="#a8804f" class="o"/></g>
<g transform="translate(230 250) scale(0.8)">{flame(0, 0, 1)}</g>
<g transform="translate(470 210)"><circle r="56" class="bluep o"/>
  {''.join(f'<circle cx="{28*math.cos(math.radians(a)):.0f}" cy="{28*math.sin(math.radians(a)):.0f}" r="12" class="blue o"/>' for a in [90, 210, 330])}</g>
<path d="M400 220h-60" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('chore', '毎日くり返す、こまごました家の用事', f'''
{doc(150, 200, 200, 250, 0)}
{''.join(f'<g><rect x="80" y="{116+i*50}" width="18" height="18" rx="4" fill="none" stroke="{INK}" stroke-width="3"/>'
         f'<rect x="112" y="{118+i*50}" width="{110-(i%2)*30}" height="12" rx="6" fill="{MUTED}"/></g>' for i in range(4))}
<g transform="translate(360 280)"><ellipse rx="52" ry="14" fill="#fffefd" class="o"/>
  <ellipse cy="-16" rx="46" ry="14" fill="#fffefd" class="o"/></g>
<g transform="translate(470 300)"><path d="M-50 0l8-70h84l8 70z" fill="#c3cbd1" class="o"/>
  <path d="M-58-70h116v-16h-116z" fill="#9aa6ae" class="o"/></g>
<g transform="translate(400 160) rotate(24)"><path d="M-8 0h16v100h-16z" class="goldd o"/>
  <path d="M-34-30h68v32h-68z" class="goldp o"/></g>''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
