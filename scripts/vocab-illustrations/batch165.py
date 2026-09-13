# -*- coding: utf-8 -*-
"""第165回。pa-/pe-/ph-/pi-/pl-/po-/pr- の名詞。"""
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

def flag(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0v-120" fill="none" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M0-120h70l-16 24 16 24H0z" class="{cls} o"/></g>')

def flower(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 60V0" fill="none" stroke="{GRND}" stroke-width="6"/>'
            + ''.join(f'<ellipse cx="0" cy="-26" rx="14" ry="26" class="{cls} o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 60))
            + f'<circle r="14" class="goldp o"/></g>')

def bee(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><ellipse rx="20" ry="14" fill="{GLD}" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M-8-12v24M2-14v28" fill="none" stroke="{INK}" stroke-width="4"/>'
            f'<ellipse cx="-4" cy="-16" rx="14" ry="7" fill="#dfe6ea" opacity="0.85" stroke="{INK}" stroke-width="1.5"/>'
            f'<circle cx="20" cy="-4" r="4" class="ink"/></g>')

def cap(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-60-10L0-36l60 26L0 16z" class="ink"/>'
            f'<path d="M-30 2v26q30 16 60 0V2" fill="none" stroke="{INK}" stroke-width="5"/>'
            f'<path d="M58-8v40" fill="none" stroke="{GLDD}" stroke-width="4"/><circle cx="58" cy="34" r="6" class="gold o"/></g>')

# --- 国・気持ち ---------------------------------------------------------------

add('patriotism', '国の旗をふって、みんなで自分の国を思う', f'''
{''.join(f'<g transform="translate({80+i*110} 340)">{person(0, 0, 1.0, 1, c, "blue", "up", h, "smile")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('gold','bun'),('green','cap'),('violet','short')]))}
{''.join(flag(120 + i*110, 260, 0.6, 'coral') for i in range(4))}
{''.join(spark(x, y, 0.8) for x, y in [(60,120),(540,110)])}''')

add('perseverance', '風雨のなかを、休まず登りつづける', f'''
<path d="M0 400q160-200 600-300v300z" fill="#c3cbd1" class="o"/>
{cloud(160, 90, 1.5, 'violet')}
{''.join(f'<path d="M{70+i*40} {150+(i%3)*20}l-16 40" fill="none" stroke="{BLU}" stroke-width="5"/>' for i in range(8))}
<g transform="translate(330 260) rotate(-16)">{person(0, 0, 1.15, 1, 'coral', 'blue', 'reach', 'cap', 'neutral', 'walk')}</g>
<path d="M100 330q160-90 380-150" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"/>
{drop(300, 160, 0.9)}''', arrow=True)

add('persistence', '一滴ずつ落ちつづけて、ついに石をうがつ', f'''
{''.join(drop(300, 90 + i*50, 1.1) for i in range(3))}
<g transform="translate(300 320)"><path d="M-140 60q-16-90 30-110 110-46 220 0 46 20 30 110z" fill="#9aa6ae" class="o"/>
  <ellipse cx="0" cy="-46" rx="30" ry="18" fill="#6f787d"/>
  <ellipse cx="0" cy="-46" rx="16" ry="9" fill="#4f585d"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M120 240h80M400 240h80"/></g>
{''.join(spark(x, y, 0.7) for x, y in [(140,120),(470,120)])}''')

add('persecution', '目じるしのちがう人たちが、責め立てられ追われる', f'''
{''.join(f'<g transform="translate({390+ (i%2)*90} {250+(i//2)*90})">{head(0, 0, 26, "violet", "bob")}'
         f'<path d="M-13 12q13 10 26 0" fill="none" stroke="{INK}" stroke-width="3" transform="scale(1 -1) translate(0 -24)"/></g>' for i in range(4))}
{''.join(f'<g transform="translate({70+i*90} 306)">{person(0, 0, 1.0, 1, c, "blue", "point", h, "neutral")}</g>'
         for i, (c, h) in enumerate([('teal','short'),('gold','cap'),('green','short')]))}
{''.join(f'<path d="M{140+i*90} 230h50" fill="none" stroke="{CRL}" stroke-width="5" marker-end="url(#ar)"/>' for i in range(3))}''', arrow=True)

add('persuasion', 'ていねいに説いて、反対を賛成に変えさせる', f'''
{person(130, 306, 1.2, 1, 'teal', 'blue', 'point', 'bun', 'neutral')}
<g transform="translate(280 170)"><rect x="-70" y="-46" width="140" height="92" rx="18" class="paper"/>
  <path d="M-50 40l-22 28 4-28z" class="paper"/>
  {word(0, 0, 3, 30, TEA)}</g>
{split()}
{person(450, 306, 1.2, -1, 'coral', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(390 150)"><circle r="26" fill="none" stroke="{MUTED}" stroke-width="6"/>
  <path d="M-16 0h32" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/></g>
<path d="M424 150h30" class="a" marker-end="url(#ar)"/>
<g transform="translate(510 150)"><path d="M-24 0l20 22 40-46" fill="none" stroke="{GRN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>''', arrow=True)

add('philanthropy', '築いた財を出して、学びの場をつくる', f'''
{person(120, 306, 1.2, 1, 'violet', 'blue', 'give', 'bun', 'smile')}
{''.join(coin(210 + i*40, 240, 22) for i in range(3))}
<path d="M330 200h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 306)">{building(0, 0, 0.9, 'teal')}</g>
{''.join(spark(x, y, 0.8) for x, y in [(240,110),(540,120)])}''', arrow=True)

# --- 危なさ・苦しさ -----------------------------------------------------------

add('peril', '細くなった綱一本で、深い谷につり下がる', f'''
<path d="M0 306h180v94H0zM420 306h180v94H420z" class="ground"/>
<path d="M180 306l30 94h-30zM420 306l-30 94h30z" fill="#5b6b78"/>
<path d="M300 40v130" fill="none" stroke="{GLDD}" stroke-width="10"/>
<path d="M300 170l-6 20 12 16-10 18" fill="none" stroke="{CRL}" stroke-width="7"/>
<path d="M300 224v40" fill="none" stroke="{GLDD}" stroke-width="6"/>
{person(300, 380, 1.05, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
<g transform="translate(480 150)"><path d="M0-40l40 70h-80z" class="gold o"/>
  <path d="M0-14v14" fill="none" stroke="{INK}" stroke-width="5"/><circle cy="16" r="4" class="ink"/></g>''')

add('pitfall', '草でおおわれた穴に、気づかず足をふみ入れる', f'''
<path d="M0 300h600v100H0z" class="ground"/>
<path d="M300 300q-10 90 60 100h-140q60-10 60-100z" fill="#3d372f"/>
<path d="M230 300h150" fill="none" stroke="{GRND}" stroke-width="8" stroke-dasharray="14 12"/>
{''.join(f'<path d="M{240+i*30} 300q6-24 14-30" fill="none" stroke="{GRND}" stroke-width="4"/>' for i in range(5))}
{person(180, 300, 1.15, 1, 'teal', 'blue', 'walk', 'short', 'smile', 'walk')}
<path d="M40 340h180" fill="none" stroke="{GLDD}" stroke-width="8" stroke-dasharray="18 14"/>
<g transform="translate(470 160)"><path d="M0-40l40 70h-80z" class="gold o"/>
  <path d="M0-14v14" fill="none" stroke="{INK}" stroke-width="5"/><circle cy="16" r="4" class="ink"/></g>''')

add('plight', '水につかった家で、身動きがとれずにいる', f'''
<path d="M0 280h600v120H0z" fill="{BLU}"/>
{''.join(f'<path d="M{-20+i*90} 300q45-30 90 0" fill="none" stroke="#fffefd" stroke-width="5" opacity="0.6"/>' for i in range(8))}
<g transform="translate(300 300)"><path d="M-110 0v-140h220V0z" fill="#fffefd" class="o"/>
  <path d="M-124-140L0-220l124 80z" class="corald o"/>
  <rect x="-70" y="-120" width="50" height="46" class="coralp o"/>
  <rect x="20" y="-120" width="50" height="46" class="coralp o"/></g>
{head(300, 216, 24, 'teal', 'bob')}
{hand(360, 200, -1)}
{''.join(f'<path d="M{120+i*70} 250h1" fill="none"/>' for i in range(0))}''')

add('predicament', '前も後ろもふさがれ、どちらにも進めない', f'''
<g transform="translate(300 210)"><rect x="-200" y="-150" width="90" height="300" rx="8" fill="#c3cbd1" class="o"/>
  <rect x="110" y="-150" width="90" height="300" rx="8" fill="#c3cbd1" class="o"/></g>
{person(300, 340, 1.15, 1, 'coral', 'blue', 'up', 'short', 'sad')}
<g fill="none" class="a" stroke="{CRL}" stroke-width="6">
  <path d="M240 200h-40" marker-end="url(#ar)"/><path d="M360 200h40" marker-end="url(#ar)"/></g>
{drop(260, 180, 0.9)}''', arrow=True)

# --- 高み・柱 ----------------------------------------------------------------

add('pinnacle', '山の、これより上はないという一点', f'''
<path d="M0 340h600v60H0z" class="ground"/>
<path d="M40 340L300 60l260 280z" fill="#c3cbd1" class="o"/>
<path d="M300 60l56 62h-112z" fill="#fffefd" class="o"/>
{flag(300, 60, 0.6, 'coral')}
{ring(300, 70, 62)}
<path d="M120 320q100-90 170-190" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>''')

add('pillar', '屋根の重みを、下からささえる太い柱', f'''
<g transform="translate(300 306)"><path d="M-230 0v-20h460v20z" fill="#c3cbd1" class="o"/>
  <path d="M-250-240h500l-40-50h-420z" fill="#dfe6ea" class="o"/>
  {''.join(f'<g transform="translate({-170+i*113} 0)"><path d="M-26-20v-200h52v200z" fill="#e6ebee" class="o"/>'
           f'<path d="M-36-220h72v-20h-72zM-36-20h72v-14h-72z" fill="#c3cbd1" class="o"/>'
           f'{"".join(f2 for f2 in ["<path d=@M" + str(-16+j*11) + " -216v192@ fill=@none@ stroke=@#c3cbd1@ stroke-width=@3@/>" for j in range(4)])}</g>'.replace('@', chr(34)) for i in range(4))}</g>
{ring(130, 210, 74)}''')

add('penthouse', 'ビルのいちばん上にある、広いすまい', f'''
{tower(300, 306, 1.4, 'teal', 5)}
<g transform="translate(300 100)"><path d="M-86 0v-70h172V0z" fill="#fffefd" class="o"/>
  <path d="M-96-70h192v-14h-192z" class="goldd o"/>
  <rect x="-66" y="-54" width="56" height="40" class="goldp o"/>
  <rect x="10" y="-54" width="56" height="40" class="goldp o"/>
  <path d="M86 0h56v-40h-56" fill="none" stroke="{GLDD}" stroke-width="6"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(140,80),(480,70)])}
{ring(300, 70, 116)}''')

add('perfection', 'すべての項目に、ひとつの欠けもなく印がつく', f'''
{doc(300, 200, 300, 300, 0)}
{''.join(f'<g><rect x="180" y="{110+i*54}" width="26" height="26" rx="5" fill="none" stroke="{INK}" stroke-width="3"/>'
         f'<path d="M182 {124+i*54}l9 10 18-20" fill="none" stroke="{GRN}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
         f'<rect x="222" y="{116+i*54}" width="{180-(i%2)*50}" height="16" rx="8" fill="{MUTED}"/></g>' for i in range(4))}
{''.join(spark(x, y, 0.9) for x, y in [(120,110),(500,110),(120,320),(500,320)])}''')

# --- お金・仕事 ---------------------------------------------------------------

add('perk', '給料のほかに、おまけの特典がつく', f'''
<g transform="translate(200 250)"><rect x="-90" y="-70" width="180" height="140" rx="8" class="goldp o"/>
  <path d="M-90-70L0-10l90-60" fill="none" class="o"/>
  {coin(0, 20, 22)}</g>
<path d="M310 250h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 250)">{box(0, 0, 130, 96, 28, 'coral')}
  <path d="M-65-48h130M0-96v144" fill="none" stroke="{GLD}" stroke-width="10"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(360,120),(550,140)])}''', arrow=True)

add('paywall', '途中まで読めるが、その先は壁でさえぎられる', f'''
<g transform="translate(300 200)"><rect x="-250" y="-150" width="500" height="300" rx="10" class="paper"/>
  <rect x="-220" y="-120" width="300" height="18" rx="9" class="coral"/>
  {''.join(f'<rect x="-220" y="{-80+i*34}" width="{280-(i%2)*70}" height="14" rx="7" fill="{MUTED}"/>' for i in range(3))}</g>
<g transform="translate(300 250)"><rect x="-250" y="-30" width="500" height="180" rx="0" fill="#c3ccd2" class="o"/>
  {''.join(f'<path d="M{-230+i*44} -30v180" fill="none" stroke="#a9b3ba" stroke-width="4"/>' for i in range(11))}
  <g transform="translate(0 60)"><rect x="-30" y="-24" width="60" height="48" rx="8" class="gold o"/>
    <path d="M-16-24v-14a16 16 0 0 1 32 0v14" fill="none" class="a"/></g></g>
{coin(500, 90, 24)}''')

add('press release', '会社の発表文を、記者たちに配る', f'''
{person(140, 306, 1.2, 1, 'violet', 'blue', 'give', 'bun', 'neutral')}
{''.join(f'<g transform="translate({260+i*70} {230+ (i%2)*20}) rotate({-8+i*6})">'
         f'<rect x="-46" y="-58" width="92" height="116" rx="5" class="paper"/>'
         f'<rect x="-32" y="-40" width="64" height="10" rx="5" class="coral"/>'
         f'{"".join(f2 for f2 in ["<rect x=@-32@ y=@" + str(-16+j*18) + "@ width=@" + str(58-(j%2)*16) + "@ height=@7@ rx=@3.5@ fill=@" + MUTED + "@/>" for j in range(3)])}</g>'.replace('@', chr(34)) for i in range(3))}
{''.join(f'<g transform="translate({420+i*70} 360)">{head(0, 0, 22, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob')]))}
<g transform="translate(520 240)"><rect x="-40" y="-28" width="80" height="56" rx="8" class="teald o"/>
  <circle cx="0" cy="0" r="16" fill="#9fb3c0" class="o"/></g>''')

add('prestige', '飾られた賞を前に、みなが一目置く', f'''
{table(340)}
<g transform="translate(300 250)"><path d="M-56 60l16-90h80l16 90z" class="gold o"/>
  <path d="M-40-30q-46 0-46-40h46M40-30q46 0 46-40h-46" fill="none" stroke="{GLDD}" stroke-width="8"/>
  <path d="M-70 60h140v20h-140z" class="goldd o"/></g>
{''.join(spark(x, y, 0.9) for x, y in [(190,140),(410,130)])}
{''.join(f'<g transform="translate({x} 360)">{head(0, 0, 24, c, h)}</g>' for x, (c, h) in zip([80, 150, 460, 530], [('teal','short'),('violet','bob'),('green','short'),('gold','bun')]))}''')

add('porter', '駅で、客の荷物をまとめて運ぶ人', f'''
{person(180, 340, 1.25, 1, 'blue', 'blue', 'carry', 'cap', 'smile')}
<g transform="translate(300 300)"><path d="M-90 40h180v10h-180z" class="ink"/>
  <circle cx="-60" cy="60" r="16" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="60" cy="60" r="16" fill="none" stroke="{INK}" stroke-width="6"/>
  {''.join(box(0, -20 - i*54, 130, 46, 14, c) for i, c in enumerate(['gold','violet','coral']))}</g>
<path d="M230 250h40" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
{person(510, 340, 1.15, -1, 'coral', 'blue', 'stand', 'bob', 'smile')}
{ring(180, 240, 122)}''')

add('probation', '入って数か月は、ようすを見る試しの期間', f'''
<g transform="translate(300 190)"><rect x="-250" y="-140" width="500" height="280" rx="12" class="paper"/>
  <rect x="-250" y="-140" width="500" height="50" rx="0" class="teal o"/>
  {''.join(f'<rect x="{-226+ (i%6)*76}" y="{-70+(i//6)*66}" width="60" height="50" rx="6" fill="{"#f7e2c8" if i < 6 else "#eef2f4"}" stroke="{INK}" stroke-width="2"/>' for i in range(18))}
  <rect x="-232" y="-76" width="466" height="62" rx="8" fill="none" stroke="{CRL}" stroke-width="5"/></g>
{person(90, 360, 0.8, 1, 'teal', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(500 360)"><rect x="-36" y="-16" width="72" height="32" rx="8" class="coralp o"/></g>''')

# --- 学び・書きもの -----------------------------------------------------------

add('postgraduate', '学部を出たあと、さらに深く学ぶ人', f'''
{table(340)}
{person(200, 340, 1.25, 1, 'violet', 'blue', 'carry', 'short', 'smile')}
{cap(200, 190, 1.0)}
{''.join(f'<g transform="translate({420+ (i%2)*8} {300-i*40}) rotate({-4+i*3})">'
         f'<rect x="-70" y="-18" width="140" height="36" rx="4" class="{c} o"/>'
         f'<rect x="-70" y="-18" width="16" height="36" class="{c}d o"/></g>' for i, c in enumerate(['teal','coral','gold','violet']))}
{''.join(spark(x, y, 0.7) for x, y in [(120,120),(330,110)])}''')

add('preface', '本文の前に、著者が置くまえがき', f'''
<g transform="translate(300 210)"><path d="M-230 130q110-40 226-16v-250q-116-26-226 14z" fill="#fffefd" class="o"/>
  <path d="M230 130q-110-40-226-16v-250q116-26 226 14z" fill="#fffefd" class="o"/>
  <path d="M-4-122v246" fill="none" stroke="{MUTED}" stroke-width="3"/>
  {''.join(f'<path d="M-200 {-90+i*42}q90-20 190-8" fill="none" stroke="{TEA}" stroke-width="6"/>' for i in range(4))}
  {''.join(f'<path d="M200 {-90+i*42}q-90-20-190-8" fill="none" stroke="{MUTED}" stroke-width="5"/>' for i in range(5))}
  <path d="M-190 70q60-14 100 4" fill="none" stroke="{TEA}" stroke-width="5"/></g>
{ring(180, 210, 150)}''')

add('portrayal', 'その人物を、こう見えるように描いて演じる', f'''
{doc(150, 200, 170, 210, 4)}
<path d="M260 200h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(430 306)"><path d="M-160 0v-30h320v30z" class="goldd o"/></g>
{person(430, 276, 1.2, 1, 'violet', 'blue', 'up', 'bun', 'neutral')}
<g transform="translate(430 130)"><path d="M-46 0q0-40 46-40t46 40q0 46-46 60-46-14-46-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-16" cy="0" r="5" class="ink"/><circle cx="16" cy="0" r="5" class="ink"/>
  <path d="M-14 24q14 12 28 0" fill="none" stroke="{INK}" stroke-width="3"/></g>''')

add('plagiarism', 'よその文をそっくり写して、自分の名で出す', f'''
<g transform="translate(150 200)"><rect x="-100" y="-120" width="200" height="240" rx="8" class="paper"/>
  {''.join(f'<rect x="-76" y="{-86+i*46}" width="{150-(i%2)*44}" height="14" rx="7" class="teal"/>' for i in range(4))}
  <rect x="-76" y="86" width="90" height="12" rx="6" fill="{MUTED}"/></g>
<path d="M270 200h50" class="a" stroke="{CRL}" marker-end="url(#ar)"/>
<g transform="translate(450 200)"><rect x="-100" y="-120" width="200" height="240" rx="8" class="paper"/>
  {''.join(f'<rect x="-76" y="{-86+i*46}" width="{150-(i%2)*44}" height="14" rx="7" class="teal"/>' for i in range(4))}
  <rect x="-76" y="86" width="90" height="12" rx="6" class="coral"/></g>
{ring(450, 292, 62)}''', arrow=True)

add('postulate', 'まずこれを認めることにして、そこから話を積む', f'''
<g transform="translate(300 100)"><rect x="-190" y="-40" width="380" height="80" rx="10" class="violetp o"/>
  {''.join(f'<rect x="{-150+i*110}" y="-10" width="90" height="20" rx="10" fill="{VIOD}"/>' for i in range(3))}</g>
{ring(300, 100, 0) if False else ''}
<rect x="60" y="46" width="480" height="110" rx="14" fill="none" stroke="{CRL}" stroke-width="5"/>
{''.join(f'<g transform="translate(300 {220+i*70})"><rect x="-150" y="-26" width="300" height="52" rx="8" class="tealp o"/></g>' for i in range(2))}
{''.join(f'<path d="M300 {166+i*70}v22" class="a" marker-end="url(#ar)"/>' for i in range(2))}''', arrow=True)

add('preconception', '会う前から、こういう人だと決めてかかる', f'''
{head(150, 280, 34, 'teal', 'short')}
<g transform="translate(320 130)"><ellipse rx="120" ry="80" fill="#fffefd" class="o"/>
  <g opacity="0.8">{head(320, 130, 34, 'coral', 'short')}</g>
  <ellipse rx="120" ry="80" fill="{VIO}" opacity="0.2"/></g>
<circle cx="222" cy="222" r="9" fill="#fffefd" class="o"/>
<path d="M450 240h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g opacity="0.35">{head(540, 280, 34, 'coral', 'short')}</g>
<path d="M240 330h180" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

add('presumption', '見えていない部分を、こうだろうと決めて話を進める', f'''
<g transform="translate(280 210)"><path d="M-140 90v-180h140v180z" class="teal o"/>
  <path d="M0 90v-180h140v180z" fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="12 10"/></g>
{head(140, 330, 26, 'violet', 'bun')}
<g transform="translate(470 120)"><rect x="-90" y="-50" width="180" height="100" rx="20" class="paper"/>
  <path d="M-70 44l-22 28 4-28z" class="paper"/>
  <path d="M-40 10l24 26 44-52" fill="none" stroke="{GRN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></g>''')

# --- しくみ・自然 -------------------------------------------------------------

add('photosynthesis', '光と水と空気から、葉が養分と酸素をつくる', f'''
{sun(90, 90, 44)}
<g transform="translate(320 250)"><path d="M0 130V0" fill="none" stroke="{GRND}" stroke-width="9"/>
  <path d="M0-10q-70-14-84-70 66 6 84 54zM0-40q70-16 84-74-66 8-84 58z" class="greenp o"/></g>
{''.join(f'<path d="M{140+i*30} {130+i*20}l60 40" class="a" stroke="{GLD}" stroke-width="5" marker-end="url(#ar)"/>' for i in range(3))}
{''.join(drop(280 + i*20, 350 + i*10, 0.9) for i in range(2))}
<path d="M520 300h-100" class="a" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"/>
{''.join(f'<circle cx="{500+ (i%2)*36}" cy="{130+(i//2)*40}" r="14" class="bluep o"/>' for i in range(4))}
<path d="M420 190l60-30" class="a" stroke="{BLU}" stroke-width="5" marker-end="url(#ar)"/>''', arrow=True)

add('pollination', 'はちが花粉を運び、別の花へ受けわたす', f'''
{flower(140, 306, 1.1, 'coral')}
{flower(460, 306, 1.1, 'violet')}
{bee(300, 160, 1.6)}
<path d="M180 220q100-90 240-10" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9" marker-end="url(#ar)"/>
{''.join(f'<circle cx="{220+i*30}" cy="{200+ (i%2)*20}" r="6" class="goldp o"/>' for i in range(4))}''', arrow=True)

add('penetration', 'かたい壁をつらぬいて、向こう側まで届く', f'''
<g transform="translate(300 200)"><rect x="-40" y="-150" width="80" height="300" fill="#c3ccd2" class="o"/>
  {''.join(f'<path d="M-40 {-120+i*50}h80" fill="none" stroke="#a9b3ba" stroke-width="4"/>' for i in range(6))}
  <circle cx="0" cy="0" r="30" fill="#fffaf1" class="o"/></g>
<path d="M60 200h190" class="a" stroke="{CRL}" stroke-width="12" marker-end="url(#ar)"/>
<path d="M350 200h190" class="a" stroke="{CRL}" stroke-width="12" marker-end="url(#ar)"/>
{''.join(f'<path d="M{300+ 46*math.cos(math.radians(a)):.0f} {200+46*math.sin(math.radians(a)):.0f}l{20*math.cos(math.radians(a)):.0f} {20*math.sin(math.radians(a)):.0f}" fill="none" stroke="{MUTED}" stroke-width="4"/>' for a in [40, 90, 140, 220, 270, 320])}''', arrow=True)

add('proliferation', 'ひとつが二つ、二つが四つと、みるみる増える', f'''
<circle cx="80" cy="200" r="26" class="teal o"/>
{''.join(f'<circle cx="200" cy="{140+i*120}" r="24" class="teal o"/>' for i in range(2))}
{''.join(f'<circle cx="330" cy="{100+i*60}" r="20" class="teal o"/>' for i in range(5))}
{''.join(f'<circle cx="{460+ (i%2)*60}" cy="{80+(i//2)*50}" r="16" class="teal o"/>' for i in range(12))}
<g fill="none" class="a" stroke-width="4">
  <path d="M110 190l60-40" marker-end="url(#ar)"/><path d="M110 214l60 40" marker-end="url(#ar)"/></g>''', arrow=True)

add('propagation', '切った枝から根が出て、新しい株になる', f'''
{table(340)}
<g transform="translate(140 306)"><path d="M0 0v-140" fill="none" stroke="{GRND}" stroke-width="8"/>
  <path d="M0-100q-46-8-54-52 44 4 54 38zM0-124q46-10 54-54-44 6-54 40z" class="greenp o"/></g>
<path d="M230 200h50" class="a" marker-end="url(#ar)"/>
{''.join(f'<g transform="translate({350+i*100} 306)"><path d="M-46 0l8-56h76l8 56z" class="corald o"/>'
         f'<path d="M-50-56h100v-14h-100z" class="coral o"/>'
         f'<path d="M0-70v-70" fill="none" stroke="{GRND}" stroke-width="6"/>'
         f'<path d="M0-110q-34-6-40-40 32 2 40 30zM0-124q34-8 40-42-34 4-40 32z" class="greenp o"/></g>' for i in range(3))}''', arrow=True)

add('proton', '原子核のなかにある、プラスの粒', f'''
{''.join(f'<ellipse cx="300" cy="200" rx="180" ry="70" fill="none" stroke="{MUTED}" stroke-width="4" transform="rotate({a} 300 200)"/>' for a in [0, 60, 120])}
<g transform="translate(300 200)">
  {''.join(f'<circle cx="{28*math.cos(math.radians(a)):.0f}" cy="{28*math.sin(math.radians(a)):.0f}" r="26" class="{"coral" if i % 2 == 0 else "tealp"} o"/>' for i, a in enumerate(range(0, 360, 60)))}</g>
<g transform="translate(328 200)"><path d="M-11 0h22M0-11v22" stroke="#fffefd" stroke-width="6" stroke-linecap="round" fill="none"/></g>
{ring(328, 200, 44)}''')

# --- 情報・だます -------------------------------------------------------------

add('phishing', '本物そっくりの入力画面で、情報を釣り上げる', f'''
<g transform="translate(260 210)"><rect x="-170" y="-130" width="340" height="230" rx="10" class="teald o"/>
  <rect x="-150" y="-110" width="300" height="190" rx="4" fill="#fffefd"/>
  <g transform="translate(0 -50)"><rect x="-30" y="-24" width="60" height="46" rx="8" class="gold o"/>
    <path d="M-16-24v-14a16 16 0 0 1 32 0v14" fill="none" class="a"/></g>
  {''.join(f'<rect x="-110" y="{10+i*38}" width="220" height="26" rx="6" fill="#dfe6ea" stroke="{INK}" stroke-width="2"/>' for i in range(2))}</g>
<path d="M500 40v170q0 60-56 60t-56-40" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
<g transform="translate(520 340)"><path d="M0-40l40 76-18 4 12 24-14 6-12-24-14 12z" fill="#fffefd" class="o"/></g>''')

add('plausibility', 'どれくらいありそうかを、めもりで測る', f'''
<g transform="translate(300 250)"><path d="M-180 0a180 180 0 0 1 360 0z" fill="#f2f5f6" class="o"/>
  <path d="M-180 0a180 180 0 0 1 90-156" fill="none" stroke="{CRL}" stroke-width="22"/>
  <path d="M-90-156a180 180 0 0 1 180 0" fill="none" stroke="{GLD}" stroke-width="22"/>
  <path d="M90-156a180 180 0 0 1 90 156" fill="none" stroke="{GRN}" stroke-width="22"/>
  <path d="M0 0L96-88" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <circle r="16" class="ink"/></g>
<g transform="translate(120 120)"><rect x="-60" y="-40" width="120" height="80" rx="16" class="paper"/>
  {word(0, 0, 3, 26, MUTED)}</g>''')

add('proclamation', '高いところから、決まりを読み上げて告げる', f'''
<g transform="translate(160 306)"><path d="M-90 0v-160h180V0z" fill="#dfe6ea" class="o"/>
  <path d="M-110-160h220v20h-220z" class="goldd o"/></g>
{person(160, 140, 1.05, 1, 'violet', 'blue', 'up', 'bun', 'neutral')}
<g transform="translate(210 60) rotate(10)"><rect x="-40" y="-50" width="80" height="100" rx="4" class="paper"/>
  {''.join(f'<rect x="-28" y="{-34+i*22}" width="{56-(i%2)*16}" height="7" rx="3.5" fill="{MUTED}"/>' for i in range(3))}</g>
{''.join(f'<path d="M{260} {130-30-i*26}q{30+i*26} {30+i*26} 0 {(30+i*26)*2}" fill="none" stroke="{CRL}" stroke-width="6" stroke-linecap="round"/>' for i in range(3))}
{''.join(f'<g transform="translate({420+i*70} 350)">{head(0, 0, 24, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob')]))}''')

add('predominance', '全体のうち、これだけで大半を占める', f'''
<g transform="translate(300 200)"><circle r="150" class="tealp o"/>
  <path d="M0 0v-150a150 150 0 1 1-106 256z" class="teal o"/>
  {''.join(f'<path d="M0 0l{150*math.cos(math.radians(a)):.0f} {150*math.sin(math.radians(a)):.0f}" fill="none" stroke="{TEAD}" stroke-width="3"/>' for a in [-90, 135, 170, 210])}</g>
{ring(250, 250, 0) if False else ''}
<path d="M60 380h480" fill="none" stroke="{MUTED}" stroke-width="0"/>''')

# --- 予定・順序 ---------------------------------------------------------------

add('postponement', '入っていた日を、あとの日へずらす', f'''
<g transform="translate(300 200)"><rect x="-250" y="-150" width="500" height="300" rx="12" class="paper"/>
  <rect x="-250" y="-150" width="500" height="50" rx="0" class="teal o"/>
  {''.join(f'<rect x="{-226+ (i%6)*76}" y="{-70+(i//6)*66}" width="60" height="50" rx="6" fill="#eef2f4" stroke="{INK}" stroke-width="2"/>' for i in range(18))}
  <rect x="-150" y="-70" width="60" height="50" rx="6" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
  <rect x="78" y="62" width="60" height="50" rx="6" class="coral o"/>
  <path d="M-110-40q110 60 190 90" class="a" stroke="{CRL}" stroke-width="6" marker-end="url(#ar)"/></g>''', arrow=True)

add('prior to', 'その前に、まずこちらが来る', f'''
<path d="M60 220h480" fill="none" stroke="{MUTED}" stroke-width="6" marker-end="url(#ar)"/>
<circle cx="200" cy="220" r="22" class="teal o"/>
<circle cx="420" cy="220" r="22" class="coral o"/>
{box(200, 130, 90, 62, 18, 'teal')}
{box(420, 130, 90, 62, 18, 'coral')}
<path d="M180 300h1" fill="none"/>
<path d="M200 270v40M420 270v40" fill="none" stroke="{MUTED}" stroke-width="3"/>
<path d="M210 330h200" class="a" marker-end="url(#ar)"/>
{ring(200, 220, 52)}''', arrow=True)

add('prime time', '夜のいちばん見られる時間帯', f'''
<path d="M60 340h480" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<rect x="{80+i*54}" y="{340-h}" width="40" height="{h}" rx="5" class="{"coral" if 4 <= i <= 5 else "tealp"} o"/>' for i, h in enumerate([40, 60, 70, 110, 210, 230, 130, 80, 50]))}
<rect x="290" y="90" width="106" height="260" rx="8" fill="none" stroke="{CRL}" stroke-width="5"/>
<g transform="translate(470 130)"><rect x="-70" y="-50" width="140" height="100" rx="10" class="teald o"/>
  <rect x="-56" y="-36" width="112" height="72" rx="4" fill="#bcd6e6"/></g>
<path d="M120 100a44 44 0 1 1-34-42 34 34 0 0 0 34 42z" class="goldp o"/>''')

add('play it by ear', '決めておかず、その場のようすで動く', f'''
<g transform="translate(160 200)"><rect x="-110" y="-120" width="220" height="240" rx="8" class="paper"/>
  {''.join(f'<rect x="-86" y="{-84+i*46}" width="160" height="16" rx="8" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 8"/>' for i in range(4))}</g>
{person(400, 306, 1.2, 1, 'teal', 'blue', 'think', 'short', 'smile')}
<g fill="none" class="a" stroke-width="5">
  <path d="M470 200q60-40 90 0" marker-end="url(#ar)"/>
  <path d="M470 240q60 40 90 0" marker-end="url(#ar)"/></g>
<path d="M290 200h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''', arrow=True)

add('precaution', '始める前に、ヘルメットと手袋をつけておく', f'''
{person(300, 306, 1.3, 1, 'teal', 'blue', 'stand', 'cap', 'neutral')}
<g transform="translate(300 158)"><path d="M-40 12q0-46 40-46t40 46z" class="gold o"/>
  <path d="M-48 12h96v14h-96z" class="goldd o"/></g>
{hand(220, 240, 1)}{hand(380, 240, -1)}
<g transform="translate(470 300)"><rect x="-50" y="-40" width="100" height="80" rx="10" class="teald o"/>
  <path d="M-30-20h60v40h-60z" fill="#dfe6ea"/></g>
<path d="M420 250h-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>
{''.join(spark(x, y, 0.7) for x, y in [(150,140),(470,150)])}''')

# --- 場所・もの ---------------------------------------------------------------

add('porch', '玄関の前に張り出した、屋根つきの場所', f'''
<g transform="translate(300 306)"><path d="M-180 0v-190h360V0z" fill="#fffefd" class="o"/>
  <path d="M-196-190L0-280l196 90z" class="corald o"/>
  <path d="M-40 0v-110h80V0z" class="coral o"/></g>
<g transform="translate(300 306)"><path d="M-140-100h280v20h-280z" class="goldd o"/>
  <path d="M-120-80v80M120-80v80" fill="none" stroke="{GLDD}" stroke-width="12"/>
  <path d="M-150-100L0-160l150 60z" class="goldd o"/>
  <path d="M-120 0h240v18h-240z" fill="#dfe6ea" class="o"/></g>
{ring(300, 260, 158)}''')

add('pendant', '鎖の先に飾りを下げた、首かざり', f'''
<g transform="translate(300 180)"><path d="M-120 0q120 130 240 0" fill="none" stroke="{GLD}" stroke-width="8"/>
  {''.join(f'<circle cx="{-110+i*22}" cy="{4+ (60 - abs(i-5)*12)}" r="5" fill="none" stroke="{GLDD}" stroke-width="3"/>' for i in range(11))}</g>
<g transform="translate(300 268)"><path d="M-40-26h80l-40 70z" class="violet o"/>
  <path d="M-40-26l20-22h40l20 22z" class="violetp o"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(200,120),(420,130)])}
{table(360)}''')

add('polyester', '工場でつくる、なめらかで丈夫な化学繊維', f'''
<g transform="translate(140 306)"><path d="M-90 0v-100h180V0z" fill="#dfe6ea" class="o"/>
  <path d="M-60-100v-40h26v40zM10-100v-56h26v56z" class="teald o"/></g>
{''.join(f'<circle cx="{240+ (i%3)*24}" cy="{280+(i//3)*22}" r="10" class="bluep o"/>' for i in range(6))}
<path d="M330 250h40" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 230)"><rect x="-100" y="-100" width="200" height="200" rx="8" class="blue o"/>
  <path d="M-80 80l160-160" fill="none" stroke="#ffffff" stroke-width="10" opacity="0.5"/>
  {''.join(f'<path d="M-100 {-70+i*34}h200" fill="none" stroke="{BLUD}" stroke-width="2.5"/>' for i in range(5))}</g>''', arrow=True)

add('plugin', '本体のさし口に、追加の機能をはめこむ', f'''
<g transform="translate(230 200)"><rect x="-170" y="-130" width="340" height="260" rx="12" class="teald o"/>
  <rect x="-150" y="-110" width="300" height="220" rx="6" fill="#dfe6ea"/>
  <path d="M150-40h30v80h-30z" fill="#fffaf1" stroke="{INK}" stroke-width="3"/></g>
<g transform="translate(470 200)"><rect x="-60" y="-70" width="120" height="140" rx="10" class="coral o"/>
  <path d="M-60-40h-40v80h40z" class="corald o"/>
  <circle cx="0" cy="0" r="24" class="coralp o"/></g>
<path d="M420 200h-60" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('pilgrimage', '長い道のりを歩いて、聖なる場所をめざす', f'''
<path d="M0 306h600v94H0z" class="ground"/>
<path d="M40 380q160-50 300-70t260-60" fill="none" stroke="{GLDD}" stroke-width="9" stroke-dasharray="18 14"/>
<g transform="translate(500 250)"><path d="M-70 56v-70h140v70z" fill="#fffefd" class="o"/>
  <path d="M-84-14L0-90l84 76z" class="corald o"/>
  <path d="M0-92v-30M-18-112h36" fill="none" stroke="{GLDD}" stroke-width="7" stroke-linecap="round"/></g>
{''.join(f'<g transform="translate({100+i*80} {370-i*14})">{person(0, 0, 0.9 - i*0.05, 1, c, "blue", "hold", h, "neutral", "walk")}</g>'
         for i, (c, h) in enumerate([('violet','bun'),('teal','short'),('coral','cap')]))}
{''.join(f'<path d="M{130+i*80} {286-i*14}v-56" fill="none" stroke="{GLDD}" stroke-width="6"/>' for i in range(3))}''')

add('plaintiff', '法廷で、訴えを起こした側', f'''
<g transform="translate(300 130)"><path d="M-110 60v-40h220v40z" class="goldd o"/>
  <path d="M-90 20v-40h180v40z" fill="#fffefd" class="o"/></g>
{head(300, 96, 26, 'violet', 'bun')}
<g transform="translate(430 150) rotate(24)"><path d="M-10 0h20v60h-20z" class="goldd o"/>
  <path d="M-34-32h68v34h-68z" class="goldd o"/></g>
<g transform="translate(140 306)"><path d="M-70 0v-70h140V0z" class="goldd o"/></g>
{person(140, 306, 1.1, 1, 'teal', 'blue', 'point', 'short', 'neutral')}
{ring(140, 210, 118)}
<g transform="translate(480 306)"><path d="M-60 0v-60h120V0z" class="goldd o"/></g>
{head(480, 262, 22, 'coral', 'short')}''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
