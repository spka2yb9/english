# -*- coding: utf-8 -*-
"""第163回。me-/mi-/mo-/mu-/n-/o- の名詞と慣用表現。"""
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

def crown(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-46 22l-10-56 28 20 18-34 18 34 28-20-10 56z" class="gold o"/>'
            f'<path d="M-46 22h92v14h-92z" class="goldd o"/></g>')

def flag(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0v-150" fill="none" stroke="{INK}" stroke-width="7"/>'
            f'<path d="M0-150h90l-20 30 20 30H0z" class="{cls} o"/></g>')

def magnifier(x, y, r=60, rot=24):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><circle r="{r}" fill="#ffffff" opacity="0.16" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M0 {r}v{r*0.7:.0f}" stroke="{INK}" stroke-width="15" stroke-linecap="round"/></g>')

# --- 悲しみ・喪 ---------------------------------------------------------------

add('melancholy', '雨の窓辺で、頬づえをついて物思いにふける', f'''
<g transform="translate(390 190)"><rect x="-160" y="-140" width="320" height="280" rx="8" class="teald o"/>
  <rect x="-140" y="-120" width="300" height="240" fill="#cfdde6"/>
  <path d="M0-120v240M-140 0h300" fill="none" stroke="{TEAD}" stroke-width="8"/>
  {''.join(f'<path d="M{-120+i*40} {-96+ (i%3)*40}l-16 40" fill="none" stroke="{BLU}" stroke-width="4"/>' for i in range(14))}</g>
{sit(160, 350, 1.25, 1, 'violet', 'blue', 'bun', 'sad', 'lap')}
{chair(174, 350, 1.15, 'gold', -1)}
<path d="M136 240l24-40" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>''')

add('mourner', '喪の席に立ち、故人を悼む人', f'''
<g transform="translate(300 306)"><path d="M-70 0v-30h140V0z" fill="#c3cbd1" class="o"/>
  <path d="M-46-30v-120h92v120z" fill="#dfe6ea" class="o"/></g>
<g transform="translate(300 300)"><path d="M0 40v-40" fill="none" stroke="{GRND}" stroke-width="5"/>
  {''.join(f'<ellipse cx="0" cy="-24" rx="9" ry="18" class="violetp o" transform="rotate({d} 0 0)"/>' for d in range(0, 360, 72))}</g>
{person(140, 306, 1.2, 1, 'blue', 'blue', 'hold', 'bun', 'sad')}
{ring(140, 210, 122)}
{head(470, 300, 24, 'blue', 'short')}{head(530, 320, 22, 'blue', 'bob')}''')

add('mourning', '黒い装いとリボンで、しばらく喪に服す', f'''
<g transform="translate(300 200)"><rect x="-250" y="-150" width="500" height="300" rx="12" class="paper"/>
  <rect x="-250" y="-150" width="500" height="50" rx="0" fill="#5b6b78"/>
  {''.join(f'<rect x="{-226+ (i%7)*66}" y="{-80+(i//7)*70}" width="52" height="54" rx="6" fill="{"#d9dfe3" if i < 14 else "#eef2f4"}" stroke="{INK}" stroke-width="2"/>' for i in range(21))}
  <rect x="-232" y="-86" width="466" height="146" rx="8" fill="none" stroke="{INK}" stroke-width="5"/></g>
<g transform="translate(90 330)"><path d="M0 0q-26-26-16-44 8-14 20 0 12-14 20 0 10 18-16 44z" fill="{INK}"/>
  <path d="M-6-30l-30 40M6-30l30 40" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/></g>''')

add('moan', '同じぐちを、いつまでもこぼしつづける', f'''
{person(150, 306, 1.25, 1, 'blue', 'blue', 'point', 'short', 'sad')}
{''.join(f'<g transform="translate({350} {110+i*80})"><rect x="-120" y="-32" width="240" height="64" rx="16" class="paper"/>'
         f'<path d="M-100 30l-22 26 4-26z" class="paper"/>'
         f'<path d="M-70 0q30-16 60 0t60 0" fill="none" stroke="{MUTED}" stroke-width="6"/></g>' for i in range(3))}
{head(540, 360, 22, 'teal', 'bob')}
<path d="M566 326q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

# --- 直す・育てる -------------------------------------------------------------

add('mend', '穴のあいたくつ下を、糸で繕う', f'''
{table(340)}
{split()}
<g transform="translate(150 280)"><path d="M-40-90h80v70q40 20 40 50h-120z" fill="#dfe6ea" class="o"/>
  <ellipse cx="30" cy="10" rx="24" ry="16" fill="#fffaf1" stroke="{INK}" stroke-width="3"/></g>
{ring(150, 240, 122, True)}
<g transform="translate(450 280)"><path d="M-40-90h80v70q40 20 40 50h-120z" fill="#dfe6ea" class="o"/>
  <ellipse cx="30" cy="10" rx="24" ry="16" fill="#c9d4da" stroke="{INK}" stroke-width="3"/>
  {''.join(f'<path d="M{12+i*10} -2v22" fill="none" stroke="{CRL}" stroke-width="3"/>' for i in range(4))}</g>
<g transform="translate(520 150) rotate(40)"><path d="M-3-50h6v90h-6z" fill="#c3ccd2" class="o"/>
  <path d="M0-50q-40 20-30 60" fill="none" stroke="{CRL}" stroke-width="3"/></g>
{ring(450, 240, 122)}''')

add('nurture', '手をかけて育て、少しずつ大きくする', f'''
{table(400)}
{person(120, 330, 0.6, 1, 'coral', 'green', 'stand', 'bob', 'smile')}
{person(290, 330, 0.9, 1, 'coral', 'green', 'stand', 'bob', 'smile')}
{person(470, 330, 1.2, 1, 'coral', 'green', 'stand', 'bob', 'smile')}
<path d="M180 210h50M360 210h50" class="a" marker-end="url(#ar)"/>
{hand(120, 150, 1)}
{''.join(spark(x, y, 0.7) for x, y in [(240,120),(400,110)])}''', arrow=True)

add('nourishment', '食べたものが、体の力になる', f'''
{table(320)}
<g transform="translate(170 280)"><ellipse rx="90" ry="24" fill="#fffefd" class="o"/>
  <circle cx="-40" cy="-16" r="22" class="greenp o"/><circle cx="0" cy="-22" r="18" class="coral o"/>
  <path d="M26-18q34-16 50 8-32 16-50-8z" class="gold o"/></g>
<path d="M290 200h60" class="a" marker-end="url(#ar)"/>
{person(460, 306, 1.25, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{''.join(spark(x, y, 0.8) for x, y in [(390,120),(540,140)])}''', arrow=True)

# --- 失敗・災難 ---------------------------------------------------------------

add('mishap', 'ちょっとした不注意で、書類にこぼしてしまう', f'''
{table(330)}
{doc(390, 260, 170, 200, 4)}
<g transform="translate(250 250) rotate(70)"><path d="M-30 0v-70h60V0z" fill="#fffefd" class="o"/>
  <path d="M30-56q26 0 26 18t-26 18" fill="none" class="o"/></g>
<path d="M300 270q60 10 90 30" fill="none" stroke="#8a5a3a" stroke-width="12" stroke-linecap="round"/>
<ellipse cx="400" cy="320" rx="70" ry="24" fill="#8a5a3a" opacity="0.8"/>
{head(130, 250, 26, 'coral', 'short')}
<path d="M104 214q16-16 0-30" fill="none" stroke="{MUTED}" stroke-width="4"/>''')

add('miss out', 'ぎりぎりで間に合わず、そのバスに乗りそこねる', f'''
<path d="M0 340h600v14H0z" class="goldd o"/>
<g transform="translate(430 280)"><path d="M-140 60V-40q0-24 24-24h230V60z" class="teal o"/>
  {''.join(f'<rect x="{-116+i*60}" y="-16" width="44" height="40" rx="5" class="tealp o"/>' for i in range(4))}
  <circle cx="-96" cy="66" r="18" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="70" cy="66" r="18" fill="none" stroke="{INK}" stroke-width="7"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M250 250h-40M260 300h-50"/></g>
{person(120, 340, 1.2, 1, 'coral', 'blue', 'up', 'short', 'sad', 'walk')}
{drop(90, 210, 0.9)}''')

add('misconduct', '職場の決まりを破って、レジから金を抜く', f'''
{table(280)}
<g transform="translate(340 210)"><rect x="-110" y="-70" width="220" height="140" rx="10" class="teald o"/>
  <rect x="-90" y="-50" width="180" height="50" rx="4" fill="#dfe6ea"/>
  <rect x="-70" y="14" width="140" height="40" rx="6" class="goldp o"/></g>
{person(150, 380, 1.2, 1, 'violet', 'blue', 'reach', 'short', 'neutral')}
{''.join(coin(240 + i*24, 250, 16) for i in range(2))}
<path d="M230 300h-60" class="a" stroke="{CRL}" marker-end="url(#ar)"/>
<g transform="translate(510 150)"><rect x="-70" y="-56" width="140" height="112" rx="8" class="paper"/>
  <path d="M-46 0h92" fill="none" stroke="{CRL}" stroke-width="10"/></g>''', arrow=True)

add('nuisance', 'となりから響く音がやまず、ずっと迷惑する', f'''
<g transform="translate(300 200)"><rect x="-20" y="-160" width="40" height="330" fill="#c3ccd2" class="o"/></g>
<g transform="translate(440 230)"><path d="M-46-50h34l56-46v190l-56-46h-34z" class="coral o"/></g>
{''.join(f'<path d="M280 {200-40-i*30}q-{40+i*30} {40+i*30} 0 {(40+i*30)*2}" fill="none" stroke="{CRL}" stroke-width="7" stroke-linecap="round"/>' for i in range(3))}
{sit(130, 340, 1.15, 1, 'teal', 'blue', 'short', 'sad', 'lap')}
{chair(144, 340, 1.05, 'gold', -1)}
{''.join(f'<path d="M{70+i*0} {200+i*40}h-30" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(2))}''')

add('obstruction', '倒れた木が道をふさぎ、車が通れない', f'''
<path d="M0 240h600v160H0z" fill="#c3cbd1"/>
<path d="M0 320h600" fill="none" stroke="#ffffff" stroke-width="6" stroke-dasharray="30 24"/>
<g transform="translate(320 300) rotate(-12)"><rect x="-200" y="-24" width="400" height="48" rx="20" fill="#8c6b42" class="o"/>
  {''.join(f'<path d="M{-160+i*80} -24q20 12 0 24" fill="none" stroke="#6d5335" stroke-width="4"/>' for i in range(5))}
  <path d="M200-30q60-40 90 10-50 40-90-10z" class="greenp o"/></g>
<g transform="translate(120 200)"><path d="M-70 0v-24l20-30h100l22 30V0z" class="coral o"/>
  <path d="M-40-54l12-18h66l14 18z" class="bluep o"/>
  <circle cx="-40" cy="6" r="16" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cx="44" cy="6" r="16" fill="none" stroke="{INK}" stroke-width="6"/></g>
<g transform="translate(120 110)"><path d="M0-30l30 52h-60z" class="gold o"/>
  <path d="M0-10v10" fill="none" stroke="{INK}" stroke-width="4"/><circle cy="12" r="3" class="ink"/></g>''')

# --- 態度・性格 ---------------------------------------------------------------

add('modesty', '光を当てられても、一歩下がって前に出ない', f'''
<g transform="translate(300 60)"><path d="M-40 40h80l-24-40h-32z" class="teald o"/>
  <g opacity="0.4"><path d="M-40 40L-130 306h260L40 40z" fill="#ffe9a8"/></g></g>
{person(430, 306, 1.2, -1, 'teal', 'blue', 'stand', 'bun', 'smile')}
<path d="M370 240h-60" class="a" marker-end="url(#ar)"/>
{hand(340, 240, -1)}
{''.join(spark(x, y, 0.7) for x, y in [(140,140),(500,140)])}''', arrow=True)

add('neutrality', 'どちらの側にもつかず、まん中に立つ', f'''
{flag(120, 306, 1.0, 'teal')}
{flag(480, 306, 1.0, 'coral')}
<path d="M300 60v300" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"/>
{person(300, 306, 1.25, 1, 'violet', 'blue', 'stand', 'short', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8">
  <path d="M250 250h-60M350 250h60"/></g>
{ring(300, 210, 128)}''')

add('nobility', '家紋をかかげ、冠をいただく家がら', f'''
{person(300, 306, 1.3, 1, 'violet', 'blue', 'stand', 'short', 'neutral')}
{crown(300, 130, 0.9)}
<g transform="translate(300 250)"><path d="M-46-40l46-24 46 24v40q0 40-46 60-46-20-46-60z" class="gold o"/>
  <path d="M-20-10h40M0-30v40" fill="none" stroke="{GLDD}" stroke-width="6"/></g>
{''.join(spark(x, y, 0.9) for x, y in [(140,140),(470,140)])}''')

add('neatness', '引き出しのなかが、きちんとそろっている', f'''
{split()}
<g transform="translate(150 210)"><rect x="-110" y="-90" width="220" height="180" rx="8" fill="#c9a06c" class="o"/>
  {''.join(f'<rect x="-24" y="-22" width="48" height="44" rx="6" fill="#eef2f4" stroke="{INK}" stroke-width="2.5" transform="translate({-60+ (i%3)*60} {-40+(i//3)*54}) rotate({-30+i*18})"/>' for i in range(6))}</g>
{ring(150, 210, 132, True)}
<g transform="translate(450 210)"><rect x="-110" y="-90" width="220" height="180" rx="8" fill="#c9a06c" class="o"/>
  {''.join(f'<rect x="{-90+ (i%3)*62}" y="{-70+(i//3)*80}" width="52" height="60" rx="6" fill="#eef2f4" stroke="{INK}" stroke-width="2.5"/>' for i in range(6))}</g>
{''.join(spark(x, y, 0.7) for x, y in [(370,110),(540,120)])}
{ring(450, 210, 132)}''')

add('obsessed with', '部屋じゅうがひとつのことで埋まっている', f'''
<g transform="translate(300 200)"><rect x="-260" y="-160" width="520" height="320" rx="10" fill="#f4f7f8" class="o"/>
  {''.join(f'<g transform="translate({-200+ (i%6)*80} {-110+(i//6)*80})"><rect x="-30" y="-34" width="60" height="68" rx="4" class="paper"/>'
           f'<circle cy="-6" r="18" class="coral o"/></g>' for i in range(18))}</g>
{person(300, 380, 1.0, 1, 'teal', 'blue', 'up', 'short', 'smile')}''')

add('moderation', '多すぎず少なすぎず、めもりを真ん中に合わせる', f'''
<g transform="translate(300 250)"><path d="M-180 0a180 180 0 0 1 360 0z" fill="#f2f5f6" class="o"/>
  <path d="M-180 0a180 180 0 0 1 60-134" fill="none" stroke="{BLU}" stroke-width="22"/>
  <path d="M120-134a180 180 0 0 1 60 134" fill="none" stroke="{CRL}" stroke-width="22"/>
  <path d="M-60-170a180 180 0 0 1 120 0" fill="none" stroke="{GRN}" stroke-width="22"/>
  <path d="M0 0v-130" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <circle r="16" class="ink"/></g>
{ring(300, 100, 66)}''')

# --- 集まる・動く -------------------------------------------------------------

add('mobilisation', '呼びかけに応じ、人も車も一気に集まる', f'''
<g transform="translate(300 190)"><circle r="70" class="coralp o"/>
  {''.join(f'<path d="M0 -86v-24" transform="rotate({d})" fill="none" stroke="{CRL}" stroke-width="5"/>' for d in range(0, 360, 45))}</g>
{''.join(f'<g transform="translate({80+i*90} 340)">{person(0, 0, 0.85, 1, c, "blue", "walk", h, "neutral", "walk")}</g>'
         for i, (c, h) in enumerate([('teal','cap'),('violet','short'),('gold','bun'),('green','cap'),('blue','short')]))}
{''.join(f'<path d="M{110+i*140} 280l{80-i*20} -50" class="a" marker-end="url(#ar)"/>' for i in range(3))}''', arrow=True)

add('newcomer', 'すでにある輪に、あとから新しく加わる人', f'''
{''.join(f'<g transform="translate({200+110*math.cos(math.radians(a)):.0f} {210+90*math.sin(math.radians(a)):.0f})">{head(0, 0, 26, c, h)}</g>'
         for a, (c, h) in zip([180, 250, 320, 30, 100], [('teal','short'),('coral','bob'),('gold','bun'),('green','short'),('blue','cap')]))}
<circle cx="200" cy="210" r="150" fill="none" stroke="{TEA}" stroke-width="5"/>
{person(500, 306, 1.15, -1, 'violet', 'blue', 'walk', 'short', 'smile')}
<path d="M450 210h-80" class="a" marker-end="url(#ar)"/>
{ring(500, 210, 110)}''', arrow=True)

add('newlywed', '指輪を交わしたばかりのふたり', f'''
{person(220, 306, 1.25, 1, 'blue', 'blue', 'give', 'short', 'smile')}
<g transform="translate(390 306)">
  <path d="M-14-8l-8 34M14-8l8 34" fill="none" stroke="#e8e2d4" stroke-width="13" stroke-linecap="round"/>
  <path d="M-56-80q56-24 112 0l-14 88h-84z" fill="#fffefd" class="o"/>
  <path d="M-26-74l-26 40M26-74l26 40" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
  <circle cx="0" cy="-114" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bob']}" transform="translate(0 -6) scale(1.06)" fill="{HAIR}"/>
  <circle cx="-9" cy="-110" r="2.6" class="ink"/><circle cx="9" cy="-110" r="2.6" class="ink"/>
  <path d="M-8-98q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
<path d="M290 220h50" fill="none" stroke="{SKIN}" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(310 150)"><circle r="24" fill="none" stroke="{GLD}" stroke-width="8"/></g>
<g transform="translate(360 150)"><circle r="24" fill="none" stroke="{GLD}" stroke-width="8"/></g>
{''.join(spark(x, y, 0.8) for x, y in [(140,130),(510,130)])}''')

add('negotiator', '自分の側を代表して、条件を詰める人', f'''
{table(260)}
{person(150, 380, 1.25, 1, 'violet', 'blue', 'point', 'bun', 'neutral')}
{person(450, 380, 1.25, -1, 'teal', 'blue', 'point', 'short', 'neutral')}
{doc(300, 300, 130, 100, 3)}
<g transform="translate(240 160)"><rect x="-60" y="-36" width="120" height="72" rx="16" class="paper"/>
  {word(0, 0, 3, 26, VIO)}</g>
{ring(150, 280, 122)}''')

# --- ことば・数 ---------------------------------------------------------------

add('multiplication', '縦と横のますの数をかけ合わせる', f'''
{''.join(f'<circle cx="{140+ (i%5)*70}" cy="{130+(i//5)*60}" r="22" class="tealp o"/>' for i in range(20))}
<path d="M90 100v250" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M110 90h330" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M60 130h20M60 190h20M60 250h20M60 310h20" fill="none" stroke="{MUTED}" stroke-width="3"/>
<g transform="translate(520 220)"><path d="M-24-24l48 48M24-24l-48 48" fill="none" stroke="{CRL}" stroke-width="9" stroke-linecap="round"/></g>''')

add('negation', 'あるという言い分に、ないと打ち消しをかける', f'''
<g transform="translate(160 200)"><rect x="-100" y="-70" width="200" height="140" rx="16" class="paper"/>
  <circle r="34" class="teal o"/></g>
<path d="M280 200h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 200)"><rect x="-100" y="-70" width="200" height="140" rx="16" class="paper"/>
  <circle r="34" class="tealp o"/>
  <circle r="52" fill="none" stroke="{CRL}" stroke-width="10"/>
  <path d="M-36 36L36-36" stroke="{CRL}" stroke-width="10" stroke-linecap="round"/></g>''', arrow=True)

add('nuance', '見くらべてやっと分かる、ほんのわずかな差', f'''
<rect x="90" y="130" width="180" height="180" rx="10" fill="#4e86c6" class="o"/>
<rect x="330" y="130" width="180" height="180" rx="10" fill="#5a8ec9" class="o"/>
{magnifier(300, 230, 74, 24)}
<path d="M180 350h240" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('murmur', '耳もとに、ごく小さな声でささやく', f'''
{head(200, 250, 44, 'teal', 'short')}
{hand(266, 250, -1)}
{head(430, 250, 44, 'coral', 'bob')}
<g transform="translate(330 160)"><rect x="-50" y="-28" width="100" height="56" rx="14" class="paper"/>
  <path d="M-20 26l-10 18 22-18z" class="paper"/>
  {''.join(f'<circle cx="{-20+i*20}" cy="0" r="4" fill="{MUTED}"/>' for i in range(3))}</g>
{''.join(f'<path d="M{310+i*16} {230+i*10}q10 10 0 20" fill="none" stroke="{MUTED}" stroke-width="3"/>' for i in range(2))}''')

add('notification', 'ベルの印がともって、知らせが届く', f'''
<g transform="translate(300 210)"><rect x="-130" y="-190" width="260" height="380" rx="26" class="teald o"/>
  <rect x="-110" y="-160" width="220" height="310" rx="6" fill="#f4f7f8"/>
  <g transform="translate(0 -40)"><path d="M0-60q46 0 46 60 0 24 14 30h-120q14-6 14-30 0-60 46-60z" class="goldp o"/>
    <path d="M0-60v-16" fill="none" stroke="{INK}" stroke-width="5"/>
    <path d="M-16 34q16 20 32 0" fill="none" stroke="{INK}" stroke-width="5"/></g>
  <circle cx="40" cy="-96" r="20" class="coral o"/>
  {''.join(f'<rect x="-80" y="{40+i*36}" width="{160-(i%2)*50}" height="14" rx="7" fill="{MUTED}"/>' for i in range(3))}</g>
{''.join(f'<path d="M{160-i*24} {100-i*22}q-16 16 0 32" fill="none" stroke="{CRL}" stroke-width="5"/>' for i in range(2))}''')

# --- 時・国 ------------------------------------------------------------------

add('millennium', '百年を十ならべた、千年の長さ', f'''
{''.join(f'<rect x="{60+i*50}" y="180" width="40" height="80" rx="5" class="tealp o"/>' for i in range(10))}
<path d="M60 300h480" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
<path d="M60 150h480" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"/>
{''.join(f'<path d="M{80+i*50} 260v-90" fill="none" stroke="{MUTED}" stroke-width="0"/>' for i in range(0))}
<g transform="translate(300 90)"><rect x="-120" y="-30" width="240" height="60" rx="14" class="coral o"/></g>''', arrow=True)

add('monarchy', '冠をいただく王が、国のいただきに立つしくみ', f'''
<g transform="translate(300 130)">{crown(0, 0, 1.2)}</g>
<g transform="translate(300 230)"><path d="M-70 60v-60h140v60z" class="goldd o"/>
  <path d="M-56 0v-70q0-30 56-30t56 30V0z" class="gold o"/></g>
<path d="M300 300v30" fill="none" stroke="{MUTED}" stroke-width="4"/>
<path d="M120 330h360" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(f'<g transform="translate({120+i*90} 370)">{head(0, 0, 22, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('blue','cap'),('violet','bun')]))}''')

add('nationalism', '一本の旗のもとに集まり、国を第一とする', f'''
{flag(300, 306, 1.3, 'coral')}
{''.join(f'<g transform="translate({100+i*90} 340)">{person(0, 0, 0.9, 1, "teal", "blue", "up", h, "neutral")}</g>'
         for i, h in enumerate(['short','bob','cap','short','bun']))}
<path d="M60 60h480" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"/>
<path d="M60 60v60M540 60v60" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"/>''')

add('menopause', '月ごとの周期が、ある年ごろで終わりを迎える', f'''
<path d="M60 250h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
{''.join(f'<path d="M{90+i*50} 250q25-70 50 0" fill="none" stroke="{CRL}" stroke-width="6"/>' for i in range(6))}
<path d="M390 130v170" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="14 10"/>
{''.join(f'<path d="M{400+i*50} 250q25-70 50 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="8 7"/>' for i in range(2))}
{head(150, 340, 26, 'violet', 'bun')}
{head(470, 340, 26, 'violet', 'bun')}
<path d="M60 340h60" fill="none" stroke="{MUTED}" stroke-width="0"/>''')

add('mutation', '写しとるうちに、ひとつだけ形が変わる', f'''
{''.join(f'<circle cx="{100+i*90}" cy="200" r="40" class="teal o"/>' for i in range(4))}
<g transform="translate(460 200)"><path d="M-40-40h80v80h-80z" class="coral o" transform="rotate(20)"/></g>
{''.join(f'<path d="M{152+i*90} 200h30" class="a" marker-end="url(#ar)"/>' for i in range(4))}
{ring(460, 200, 70)}
<g transform="translate(460 90)"><path d="M0-30l30 52h-60z" class="gold o"/>
  <path d="M0-10v10" fill="none" stroke="{INK}" stroke-width="4"/><circle cy="12" r="3" class="ink"/></g>''', arrow=True)

add('nucleus', '原子や細胞の、まん中にある核', f'''
<circle cx="300" cy="200" r="56" class="coral o"/>
{''.join(f'<ellipse cx="300" cy="200" rx="180" ry="70" fill="none" stroke="{MUTED}" stroke-width="4" transform="rotate({a} 300 200)"/>' for a in [0, 60, 120])}
{''.join(f'<circle cx="{300+180*math.cos(math.radians(a))*math.cos(math.radians(r))-70*math.sin(math.radians(a))*math.sin(math.radians(r)):.0f}" cy="{200+180*math.cos(math.radians(a))*math.sin(math.radians(r))+70*math.sin(math.radians(a))*math.cos(math.radians(r)):.0f}" r="14" class="tealp o"/>' for a, r in [(20, 0), (200, 60), (110, 120)])}
{ring(300, 200, 84)}''')

# --- 見せ方・評判 -------------------------------------------------------------

add('mural', '建物の壁いっぱいに描かれた絵', f'''
<g transform="translate(300 220)"><rect x="-250" y="-180" width="500" height="360" rx="6" fill="#e8dfcd" class="o"/>
  <path d="M-230 160l120-170 90 100 80-120 170 190z" class="greenp o"/>
  {sun(120, -100, 40)}
  {''.join(f'<circle cx="{-160+i*70}" cy="{60+ (i%2)*30}" r="24" class="{c} o"/>' for i, c in enumerate(['coral','violet','gold','teal','blue']))}</g>
{person(80, 380, 0.8, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(530, 380, 0.8, -1, 'coral', 'blue', 'stand', 'bob', 'smile')}''')

add('likeness', 'その人にそっくりに描かれた似顔', f'''
{head(150, 240, 42, 'teal', 'bob')}
<path d="M230 230h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
<g transform="translate(430 230)"><rect x="-110" y="-120" width="220" height="240" rx="6" class="goldd o"/>
  <rect x="-92" y="-102" width="184" height="204" fill="#f7f3e8"/></g>
{head(430, 244, 42, 'teal', 'bob')}
{''.join(spark(x, y, 0.8) for x, y in [(300,140),(300,320)])}''')

add('obscurity', '棚のすみで、だれにも借りられないまま', f'''
{''.join(f'<path d="M40 {130+i*90}h520v12H40z" class="goldd o"/>' for i in range(3))}
{''.join(f'<rect x="{70+ (i%8)*60}" y="{60+(i//8)*90}" width="40" height="70" rx="3" class="{c} o"/>'
         for i, c in enumerate(['teal','coral','gold','violet','green','blue','teal','coral',
                                 'gold','violet','green','blue','coral','teal','gold','violet']))}
<g transform="translate(540 200)"><rect x="-20" y="-36" width="40" height="70" rx="3" fill="#a9a79c" class="o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M516 168q40-14 46 0M516 240q40-12 46 4"/></g>
{ring(540, 198, 62)}
{person(180, 380, 0.9, 1, 'teal', 'blue', 'reach', 'short', 'neutral')}''')

add('notorious for', '悪いことで、みんなに名を知られている', f'''
<g transform="translate(400 306)"><path d="M-110 0v-130h220V0z" fill="#fffefd" class="o"/>
  <path d="M-124-130h248l-30-40h-188z" class="corald o"/>
  <path d="M-40 0v-70h80V0z" class="coral o"/></g>
{''.join(f'<g transform="translate({400+ (i-1)*70} -30)"><path d="M0 130l8 18 20 2-14 14 4 20-18-10-18 10 4-20-14-14 20-2z" fill="#8b9196" stroke="{INK}" stroke-width="2"/></g>' for i in range(3))}
{''.join(f'<g transform="translate({70+i*80} 340)">{head(0, 0, 24, c, h)}</g>' for i, (c, h) in enumerate([('teal','short'),('violet','bob'),('gold','bun')]))}
{''.join(f'<path d="M{110+i*80} 280l60-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>' for i in range(3))}''')

add('observance', '決まった日に、決まったとおりの行いをする', f'''
<g transform="translate(160 150)"><rect x="-110" y="-100" width="220" height="200" rx="10" class="paper"/>
  <rect x="-110" y="-100" width="220" height="36" rx="0" class="teal o"/>
  {''.join(f'<rect x="{-92+ (i%5)*38}" y="{-50+(i//5)*38}" width="28" height="28" rx="4" fill="#eef2f4"/>' for i in range(10))}
  <rect x="-16" y="-12" width="28" height="28" rx="4" class="coral o"/></g>
<path d="M290 200h50" class="a" marker-end="url(#ar)"/>
{''.join(f'<g transform="translate({410+i*80} 340)">{person(0, 0, 0.9, 1, c, "blue", "hold", h, "neutral")}</g>' for i, (c, h) in enumerate([('violet','bun'),('teal','short')]))}
<g transform="translate(450 180)"><path d="M-30 0v-30h60v30z" class="goldd o"/>
  <path d="M0-30v-40M-20-50h40" fill="none" stroke="{GLDD}" stroke-width="7" stroke-linecap="round"/></g>''', arrow=True)

# --- もの ---------------------------------------------------------------------

add('mould', 'しばらく置いたパンに、緑のかびが生える', f'''
{table(340)}
<g transform="translate(300 290)"><path d="M-90 20q-16-90 0-104 90-20 180 0 16 14 0 104z" fill="#c98f52" class="o"/>
  <path d="M-70-76q70-16 140 0" fill="none" stroke="#a8703a" stroke-width="4"/>
  {''.join(f'<g transform="translate({-56+ (i%4)*40} {-50+(i//4)*40})"><circle r="{14-(i%3)*3}" fill="#7d9a5e" opacity="0.85"/>'
           f'<circle cx="8" cy="-6" r="{8-(i%2)*2}" fill="#5f7a44" opacity="0.85"/></g>' for i in range(8))}</g>
{''.join(f'<path d="M{160+i*24} {170-i*14}q-14 14 0 28" fill="none" stroke="{GRN}" stroke-width="4"/>' for i in range(2))}''')

add('mutton', '成長した羊からとれる肉', f'''
{table(340)}
<g transform="translate(180 300)"><ellipse rx="70" ry="46" fill="#fffefd" class="o"/>
  <circle cx="-56" cy="-30" r="26" fill="#5b6b78" class="o"/>
  <path d="M-76-44l-16-14 20-8M-40-50l6-22 14 18" fill="#5b6b78" class="o"/>
  <circle cx="-62" cy="-32" r="4" fill="#fffefd"/>
  <path d="M-40 40l-8 30M20 44l8 30M50 30l14 28" fill="none" stroke="#5b6b78" stroke-width="9" stroke-linecap="round"/>
  {''.join(f'<circle cx="{-30+ (i%4)*26}" cy="{-24+(i//4)*24}" r="16" fill="#fffefd" stroke="{INK}" stroke-width="2"/>' for i in range(8))}</g>
<path d="M290 260h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 300)"><ellipse rx="80" ry="44" fill="#d98a80" class="o"/>
  <ellipse cx="-10" cy="-6" rx="44" ry="24" fill="#c26a60"/>
  <path d="M60-20q26 6 24 30" fill="none" stroke="#e8e2d4" stroke-width="14" stroke-linecap="round"/></g>''', arrow=True)

add('oar', '水をかいて舟を進める、長いかい', f'''
<path d="M0 260h600v140H0z" fill="{BLUP}"/>
<g transform="translate(300 290)"><path d="M-130 0h260l-30 40h-200z" class="coral o"/></g>
{sit(300, 290, 1.0, 1, 'teal', 'blue', 'cap', 'neutral', 'lap')}
{''.join(f'<g transform="translate({300+f*70} 250) rotate({f*36})"><path d="M0 0l{f*110} 60" fill="none" stroke="{GLDD}" stroke-width="10" stroke-linecap="round"/>'
         f'<ellipse cx="{f*126}" cy="70" rx="26" ry="16" class="goldp o" transform="rotate({f*30} {f*126} 70)"/></g>' for f in [-1, 1])}
{ring(180, 320, 66)}''')

# --- 慣用表現 ----------------------------------------------------------------

add('needless to say', 'わざわざ言うまでもなく、みんな分かっている', f'''
{sun(300, 110, 56)}
{''.join(f'<g transform="translate({100+i*100} 330)">{head(0, 0, 26, c, h)}</g>'
         for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun'),('violet','cap')]))}
{''.join(f'<path d="M{100+i*100} 280a40 40 0 0 0 0-30" fill="none" class="a" stroke-width="4" marker-end="url(#ar)"/>' for i in range(5))}
<g transform="translate(300 220)"><rect x="-80" y="-30" width="160" height="60" rx="16" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/></g>''', arrow=True)

add('not to mention', 'それだけでなく、さらにこれも加わる', f'''
{''.join(f'<g transform="translate(200 {130+i*70})"><rect x="-130" y="-26" width="260" height="52" rx="10" class="tealp o"/></g>' for i in range(3))}
<g transform="translate(200 340)"><rect x="-130" y="-26" width="260" height="52" rx="10" class="coral o"/></g>
<path d="M400 300h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(510 340)"><path d="M-24 0h48M0-24v48" stroke="{CRL}" stroke-width="12" stroke-linecap="round" fill="none"/></g>
{ring(200, 340, 0) if False else ''}''', arrow=True)

add('no sooner than', '一方が終わるのとほとんど同時に、次が起きる', f'''
<path d="M60 250h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
<circle cx="270" cy="250" r="18" class="teal o"/>
<circle cx="320" cy="250" r="18" class="coral o"/>
<path d="M270 200v-70M320 300v70" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g transform="translate(270 100)">{box(0, 0, 90, 62, 18, 'teal')}</g>
<g transform="translate(330 380)">{box(0, 0, 90, 62, 18, 'coral')}</g>
<path d="M254 320h82" class="a" marker-end="url(#ar)" marker-start="url(#ar)"/>
{ring(295, 250, 62)}''', arrow=True)

add('notwithstanding', '大雨のなかでも、予定どおり行われる', f'''
{cloud(160, 90, 1.6, 'violet')}{cloud(430, 80, 1.5, 'violet')}
{''.join(f'<path d="M{60+i*40} {160+(i%3)*20}l-16 40" fill="none" stroke="{BLU}" stroke-width="5" stroke-linecap="round"/>' for i in range(13))}
<path d="M40 340h520" fill="none" stroke="{GLDD}" stroke-width="9" stroke-dasharray="18 14"/>
{person(300, 340, 1.2, 1, 'coral', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g transform="translate(520 300)"><path d="M0 40v-120" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M0-80h-70l18 22-18 22h70z" class="green o"/></g>
<path d="M360 250h100" class="a" stroke-width="6" marker-end="url(#ar)"/>''', arrow=True)

add('normality', '乱れていた線が、ふだんの幅にもどる', f'''
<path d="M60 340h480M90 360V70" fill="none" stroke="{MUTED}" stroke-width="4"/>
<rect x="90" y="180" width="450" height="60" fill="{TONES['green'][1]}"/>
<path d="M90 210h450" fill="none" stroke="{GRN}" stroke-width="3" stroke-dasharray="10 9"/>
<path d="M100 210l40-100 40 200 40-160 40 130 50-70 60 20 60 0 60 0" fill="none" stroke="{TEA}" stroke-width="7"/>
{''.join(f'<circle cx="{410+i*60}" cy="210" r="8" class="teal o"/>' for i in range(3))}''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
