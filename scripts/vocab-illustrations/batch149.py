# -*- coding: utf-8 -*-
"""第149回。s- の形容詞と、学校・食事まわりの名詞。"""
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

def house(x, y, s=1, cls='coral', w=100):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M{-w} 0v-110h{2*w}V0z" fill="#fffefd" class="o"/>'
            f'<path d="M{-w-16} -110L0-180l{w+16} 70z" class="{cls}d o"/>'
            f'<path d="M-26 0v-60h52V0z" class="{cls} o"/>'
            f'<rect x="{-w+22}" y="-90" width="36" height="32" class="{cls}p o"/></g>')

def clock(x, y, s=1, h=2, m=0):
    ah = math.radians(h*30 + m*0.5 - 90); am = math.radians(m*6 - 90)
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="54" fill="#fffefd" class="o"/>'
            f'<path d="M0 0l{42*math.cos(am):.0f} {42*math.sin(am):.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M0 0l{28*math.cos(ah):.0f} {28*math.sin(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
            f'<circle r="4" class="ink"/></g>')

def bed(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-160 0v-40h320V0z" class="goldd o"/>'
            f'<path d="M-160-40v-90h30v90zM130-40v-56h30v56z" class="goldd o"/>'
            f'<path d="M-130-40v-30h260v30z" class="tealp o"/>'
            f'<path d="M-124-70q-6-26 30-26h50v26z" fill="#fffefd" class="o"/></g>')

# --- 態度 --------------------------------------------------------------------

add('ruthless', 'ためらいなく、つながりを断ち切っていく', f'''
{''.join(head(90 + i*90, 240, 26, c, h) for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun')]))}
<path d="M60 300h330" fill="none" stroke="{GLDD}" stroke-width="9"/>
<g transform="translate(400 300) rotate(-14)">
  <path d="M-6 6l-56 48M-6-6l-56-48" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="-66" cy="58" r="15" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="-66" cy="-58" r="15" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M0 0l60 6" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g>
{head(520, 160, 28, 'violet', 'short')}
<path d="M506 132l14 6M534 132l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>''')

add('sarcastic', '失敗を前に、わざとらしく拍手してみせる', f'''
<g transform="translate(180 306)">
  {''.join(f'<rect x="{-70+i*14}" y="{-30-i*8}" width="{110-i*22}" height="26" rx="4" class="teal o" transform="rotate({-20+i*14} 0 0)"/>' for i in range(4))}
</g>
{person(430, 306, 1.2, -1, 'coral', 'blue', 'hold', 'short', 'neutral')}
<g transform="translate(374 216)">{hand(-14, 0, 1)}{hand(14, 0, -1)}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M320 170h-26M330 250h-26"/></g>
<g transform="translate(300 100)"><rect x="-70" y="-38" width="140" height="76" rx="18" class="paper"/>
  <path d="M40 34l24 30-42-30z" class="paper"/>
  <path d="M-30 4q30 26 60 0" fill="none" stroke="{MUTED}" stroke-width="6"/>
  <circle cx="-24" cy="-14" r="5" class="ink"/><circle cx="24" cy="-14" r="5" class="ink"/></g>''')

add('scornful', '見下ろして、鼻で笑って払いのける', f'''
{person(190, 306, 1.3, 1, 'violet', 'blue', 'point', 'short', 'neutral')}
<path d="M156 190l16 8M226 190l-16 8" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
<path d="M256 220l90 60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{box(420, 300, 84, 56, 18, 'gold')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M470 220q26-16 44 4M486 174q26-16 44 4"/></g>''')

add('snobbish', 'つんと上を向き、質素なほうには目もくれない', f'''
{split()}
{table(320)}
<g transform="translate(120 290)"><ellipse rx="56" ry="16" fill="#fffefd" class="o"/>
  <circle cx="0" cy="-10" r="15" class="goldp o"/></g>
<g transform="translate(470 280)"><path d="M-46 0q-16-54 0-70h92q16 16 0 70z" class="violetp o"/>
  <path d="M-52-70h104v-14h-104z" class="violet o"/>
  {spark(0, -110, 0.9)}</g>
<g transform="translate(300 200) rotate(-16)">
  <circle r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bun']}" transform="translate(0 132) scale(1.25)" fill="{HAIR}"/>
  <path d="M-16-8l12 6M16-8l-12 6" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 14h20" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0l14 10-14 4z" fill="{SKINL}" opacity="0.6"/></g>
<path d="M348 176l90-30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('spiteful', 'わざと相手のいすに画びょうを置く', f'''
{chair(420, 306, 1.3, 'gold', -1)}
<g transform="translate(400 214)"><circle r="12" class="coral o"/><path d="M0 12v22" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></g>
{person(190, 306, 1.15, 1, 'violet', 'blue', 'point', 'short', 'neutral')}
<path d="M164 200q16 12 32 0" fill="none" stroke="{INK}" stroke-width="3"/>
{head(540, 250, 24, 'teal', 'bob')}
<path d="M300 150q60-40 110 30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>''')

add('sheepish', 'こぼしてしまい、頭をかいてきまり悪そうに笑う', f'''
{table(320)}
<g transform="translate(400 290)"><path d="M-24 0v-40h48V0z" fill="#fffefd" class="o" transform="rotate(70 0 0)"/>
  <path d="M-40 6q60-26 110 4-56 16-110-4z" class="coralp o"/></g>
{person(190, 306, 1.25, 1, 'teal', 'blue', 'think', 'short', 'smile')}
<path d="M166 200l14 6M214 200l-14 6" fill="none" stroke="{INK}" stroke-width="3"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M120 170q16-16 0-32M266 176q-16-16 0-32"/></g>
{drop(240, 170, 0.9)}''')

add('shameless', 'とがめられても、平気な顔でやってのける', f'''
{table(300)}
<g transform="translate(340 268)"><ellipse rx="76" ry="20" fill="#fffefd" class="o"/></g>
{person(200, 306, 1.2, 1, 'coral', 'blue', 'give', 'short', 'smile')}
<g transform="translate(300 216)"><circle r="24" class="goldp o"/></g>
{head(500, 250, 28, 'teal', 'bun')}
<path d="M540 210q16-16 0-34" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g transform="translate(120 130)"><rect x="-70" y="-40" width="140" height="80" rx="18" class="paper"/>
  <path d="M40 36l26 30-44-30z" class="paper"/>
  <path d="M-30 6q30 24 60 0" fill="none" stroke="{GRN}" stroke-width="6"/>
  <circle cx="-24" cy="-12" r="5" class="ink"/><circle cx="24" cy="-12" r="5" class="ink"/></g>''')

add('shyness', 'ほかの人のかげにかくれて、うつむいてしまう', f'''
{person(330, 306, 1.3, 1, 'teal', 'blue', 'stand', 'bun', 'smile')}
<g transform="translate(216 306)">
  <path d="M-12-8l-6 30M10-8l6 30" fill="none" stroke="{BLUD}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-24-70q24-12 48 0l-8 64h-32z" fill="{CRL}" class="o"/>
  <path d="M-20-64l6 40M20-64l-6 40" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="0" cy="-98" r="23" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['bob']}" transform="translate(0 12) scale(0.96)" fill="{HAIR}"/>
  <path d="M-11-92l10 4M11-92l-10 4" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-7-78h14" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"><path d="M150 190q16-16 0-32"/></g>
{head(480, 300, 24, 'violet', 'short')}''')

add('self-assured', '大勢を前にしても、背すじを伸ばして落ち着いている', f'''
{person(200, 306, 1.35, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{''.join(head(360 + (i % 3) * 84, 250 + (i // 3) * 66, 26, c, h)
         for i, (c, h) in enumerate([('coral','short'),('violet','bob'),('green','short'),('gold','bun'),('blue','cap'),('teal','short')]))}
{''.join(spark(x, y, 0.8) for x, y in [(120,120),(280,110)])}
<path d="M130 306h140" fill="none" stroke="{GRN}" stroke-width="6"/>''')

add('selfless', '自分の分をゆずって、皿を空にする', f'''
{table(300)}
{person(150, 306, 1.2, 1, 'teal', 'blue', 'give', 'bun', 'smile')}
<g transform="translate(150 270)"><ellipse rx="52" ry="15" fill="#fffefd" class="o"/></g>
<g transform="translate(300 240)"><ellipse rx="52" ry="15" fill="#fffefd" class="o"/>
  <circle cx="-14" cy="-12" r="14" class="coral o"/><circle cx="14" cy="-10" r="12" class="greenp o"/></g>
<path d="M240 190h80" class="a" marker-end="url(#ar)"/>
{person(450, 306, 1.15, -1, 'coral', 'green', 'reach', 'short', 'smile')}''', arrow=True)

add('sober', '酔ってふらつく側と、しらふで落ち着いている側の対比', f'''
{split()}
{person(150, 306, 1.15, 1, 'coral', 'blue', 'reach', 'short', 'neutral', 'walk')}
<g transform="translate(60 300)"><path d="M-20-60h40v60h-40z" class="green o"/><path d="M-8-60v-26h16v26z" class="greend o"/></g>
<g transform="translate(150 150)"><path d="M0 0a22 22 0 1 1 18-12 15 15 0 1 0 12 20" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/></g>
{person(450, 306, 1.15, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(540 290)"><path d="M-22 0v-56h44V0z" fill="#eaf4fb" class="o"/>
  <path d="M-18-40h36v36h-36z" class="bluep"/></g>''')

add('submissive-placeholder' if False else 'sluggish', '足が重く、なかなか前に進まない', f'''
<path d="M40 336h520" fill="none" stroke="{GLDD}" stroke-width="8" stroke-dasharray="18 14"/>
{person(180, 330, 1.25, 1, 'blue', 'blue', 'reach', 'short', 'sad', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M100 250h-34M96 290h-30"/></g>
<g transform="translate(430 320)"><path d="M-40 0q0-30 34-30 30 0 30 26" fill="none" stroke="{GRND}" stroke-width="10"/>
  <circle cx="20" cy="-20" r="26" fill="none" stroke="{GRND}" stroke-width="10"/>
  <path d="M-40 0q-24-2-24-22" fill="none" stroke="{GRND}" stroke-width="8"/>
  <path d="M-62-24v-16M-50-26v-14" fill="none" stroke="{GRND}" stroke-width="5" stroke-linecap="round"/></g>
<path d="M240 200h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="7 9"/>''')

add('sloppy', 'はみ出したまま、雑に塗ってしまう', f'''
{split()}
<g transform="translate(150 200)"><rect x="-90" y="-90" width="180" height="180" rx="8" fill="none" stroke="{INK}" stroke-width="4"/>
  <rect x="-86" y="-86" width="172" height="172" rx="6" class="teal"/></g>
{ring(150, 200, 122, True)}
<g transform="translate(450 200)"><rect x="-90" y="-90" width="180" height="180" rx="8" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-110-70q60-30 130 0t80 40q-20 60-90 66t-120-20q-20-50 0-86z" class="teal"/></g>
{ring(450, 200, 130)}''')

add('spotless', '汚れの残る面と、ちりひとつない面の対比', f'''
{split()}
<g transform="translate(150 200)"><rect x="-96" y="-96" width="192" height="192" rx="10" fill="#e6e2d8" class="o"/>
  {''.join(f'<ellipse cx="{-60+i*44}" cy="{-50+(i%3)*54}" rx="{14+(i%3)*5}" ry="{9+(i%2)*5}" fill="#b6ab94"/>' for i in range(6))}</g>
{ring(150, 200, 128, True)}
<g transform="translate(450 200)"><rect x="-96" y="-96" width="192" height="192" rx="10" fill="#fffefd" class="o"/>
  <path d="M-70 90l120-186h34l-120 186z" fill="#f2f7fa"/></g>
{''.join(spark(x, y, 0.9) for x, y in [(390,130),(500,250),(520,120)])}
{ring(450, 200, 128)}''')

add('shabby', 'すり切れて、つぎはぎだらけの上着', f'''
{table(340)}
<g transform="translate(300 200)">
  <path d="M-110 110V-40l50-40h120l50 40v150z" fill="#b8ab92" class="o"/>
  <path d="M-60-80q60 40 120 0l-30 40h-60z" fill="#a2957e" class="o"/>
  <path d="M-110-40l-40 30 30 40 26-22M110-40l40 30-30 40-26-22" fill="#b8ab92" class="o"/>
  <rect x="-70" y="20" width="52" height="46" fill="#8d8271" class="o" transform="rotate(-8 -44 43)"/>
  <rect x="24" y="52" width="44" height="40" fill="#8d8271" class="o" transform="rotate(10 46 72)"/>
  <path d="M-20 110l14-40 16 40z" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
  <path d="M74-6l16 18-18 16" fill="none" stroke="{INK}" stroke-width="3"/>
</g>''')

# --- 程度・ようす ------------------------------------------------------------

add('simplistic', 'こみいったものを、単純にしすぎて中身が落ちる', f'''
<g transform="translate(150 190)"><circle r="70" class="teal o"/>
  {''.join(f'<circle cx="{96*math.cos(math.radians(a)):.0f}" cy="{96*math.sin(math.radians(a)):.0f}" r="22" class="tealp o"/>' for a in range(0, 360, 60))}
  {''.join(f'<path d="M{70*math.cos(math.radians(a)):.0f} {70*math.sin(math.radians(a)):.0f}L{78*math.cos(math.radians(a)):.0f} {78*math.sin(math.radians(a)):.0f}" stroke="{INK}" stroke-width="4"/>' for a in range(0, 360, 60))}</g>
<path d="M290 190h60" class="a" marker-end="url(#ar)"/>
<circle cx="450" cy="190" r="70" class="teal o"/>
{''.join(f'<circle cx="{380+i*46}" cy="{330-(i%2)*20}" r="20" class="tealp o" opacity="0.6"/>' for i in range(4))}
{''.join(f'<path d="M{392+i*46} 290v20" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6"/>' for i in range(3))}''', arrow=True)

add('simultaneous', '二つのことが、まったく同じ時刻に起こる', f'''
{split()}
{clock(150, 140, 0.9, 3, 0)}
{clock(450, 140, 0.9, 3, 0)}
{person(150, 330, 1.0, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{person(450, 330, 1.0, 1, 'teal', 'blue', 'up', 'bob', 'smile')}
<path d="M300 240v100" fill="none" stroke="{CRL}" stroke-width="5"/>''')

add('sequential', '番号どおりに、順を追って進む', f'''
{''.join(f'<g transform="translate({100+i*110} {300-i*54})"><rect x="-44" y="-36" width="88" height="72" rx="10" class="teal o"/>'
         f'{"".join(chr(60)+"circle cx="+chr(34)+str(-24+j*16)+chr(34)+" cy="+chr(34)+"0"+chr(34)+" r="+chr(34)+"6"+chr(34)+" fill="+chr(34)+"#fffefd"+chr(34)+"/"+chr(62) for j in range(i+1))}</g>' for i in range(5))}
{''.join(f'<path d="M{150+i*110} {266-i*54}l24-26" class="a" marker-end="url(#ar)"/>' for i in range(4))}''', arrow=True)

add('serene', '風のない朝の湖のように、静かで落ち着いている', f'''
<path d="M0 210h600v190H0z" fill="{BLUP}"/>
<path d="M0 210h600" fill="none" stroke="{BLU}" stroke-width="4"/>
<g transform="translate(430 170)"><path d="M-130 40l80-104 54 56 46-58 76 106z" fill="#c3cbd1" class="o"/></g>
{sun(120, 110, 40)}
<g transform="translate(430 254) scale(1 -1)" opacity="0.35"><path d="M-130 40l80-104 54 56 46-58 76 106z" fill="#c3cbd1"/></g>
{''.join(f'<path d="M{60+i*70} {290+(i%3)*34}h60" fill="none" stroke="#ffffff" stroke-width="3" opacity="0.75"/>' for i in range(7))}
{sit(160, 380, 1.0, 1, 'teal', 'blue', 'bun', 'smile', 'lap')}''')

add('scenic', '見晴らし台のベンチから、谷を見わたす', f'''
<path d="M0 250q120-120 300-96t300-64v310H0z" class="greenp o"/>
<path d="M0 180L160 40l110 116 90-96 240 160z" fill="#c3cbd1" class="o"/>
<path d="M0 306h600v94H0z" class="ground"/>
<g transform="translate(300 306)"><path d="M-90-30h180v20h-180z" class="goldd o"/>
  <path d="M-70-10v10M70-10v10M-70-30v-40h140v10h-130" fill="none" stroke="{GLDD}" stroke-width="8"/></g>
{head(250, 268, 22, 'coral', 'bob')}{head(340, 268, 22, 'teal', 'short')}
{sun(80, 70, 34)}''')

add('sensational', '大見出しで、人の目をあおり立てる新聞', f'''
{doc(300, 200, 330, 290, 0)}
<path d="M160 100h280" fill="none" stroke="{INK}" stroke-width="4"/>
{word(300, 140, 4, 62, CRL)}
<path d="M300 190h6" fill="none"/>
{''.join(f'<rect x="{160+ (i%2)*172}" y="{210+(i//2)*36}" width="150" height="12" rx="6" fill="{MUTED}"/>' for i in range(4))}
<g class="corals" stroke-width="5">{''.join(f'<path d="M300 42v-24" transform="rotate({d} 300 140)"/>' for d in [-30, 0, 30])}</g>
{head(90, 320, 24, 'teal', 'short')}{head(520, 320, 24, 'violet', 'bob')}''')

add('speculative', 'たしかな土台はほんの少しで、上はぜんぶ当て推量', f'''
{table(340)}
<rect x="250" y="270" width="100" height="36" rx="6" class="teal o"/>
<g fill="none" stroke="{MUTED}" stroke-width="4.5" stroke-dasharray="12 10">
  <rect x="200" y="204" width="200" height="60" rx="8"/>
  <rect x="150" y="138" width="300" height="60" rx="8"/>
  <rect x="110" y="72" width="380" height="60" rx="8"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M116 250q16-20 0-40M484 250q-16-20 0-40"/></g>''')

add('sparse', 'びっしり生えた側と、まばらな側の対比', f'''
{split()}
{''.join(f'<path d="M{56+ (i%7)*30} {306-(i//7)*0}v-{40+(i%5)*14}" fill="none" stroke="{GRND}" stroke-width="6" stroke-linecap="round"/>' for i in range(21))}
{ring(150, 260, 118, True)}
{''.join(f'<path d="M{x} 306v-{h}" fill="none" stroke="{GRND}" stroke-width="6" stroke-linecap="round"/>' for x, h in [(370,50),(440,40),(510,56)])}
{ring(450, 260, 118)}''')

add('sporadic', 'ばらばらの間かくで、思い出したように起こる', f'''
<path d="M60 200h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
{''.join(f'<circle cx="{x}" cy="200" r="13" class="coral o"/>' for x in [96, 130, 260, 400, 424, 512])}
{''.join(f'<path d="M{x} 236v26" fill="none" stroke="{MUTED}" stroke-width="3"/>' for x in [96, 130, 260, 400, 424, 512])}
{''.join(f'<path d="M{a+8} 280h{b-a-16}" fill="none" stroke="{MUTED}" stroke-width="3" marker-end="url(#ar)"/>' for a, b in [(96,130),(130,260),(260,400),(400,424),(424,512)])}''', arrow=True)

add('spacious', '家具が少なく、広々とした部屋', f'''
<g transform="translate(300 200)"><path d="M-250-140h500v300h-500z" fill="#fffefd" class="o"/>
  <path d="M-190-90h380v210h-380z" fill="#f4f7f8" class="o"/>
  <path d="M-250-140l60 50M250-140l-60 50M-250 160l60-40M250 160l-60-40" fill="none" stroke="{MUTED}" stroke-width="3"/></g>
{chair(300, 300, 0.7, 'gold', -1)}
<path d="M80 340h440" fill="none" class="a" stroke-width="4" marker-end="url(#ar)" marker-start="url(#ar)"/>''', arrow=True)

add('solitary', '広い野原に、ぽつんと一本だけ立つ木', f'''
<path d="M0 280q140-30 300-30t300 26v124H0z" class="greenp o"/>
{tree(300, 290, 1.3)}
{''.join(f'<path d="M{60+i*90} {330+(i%3)*22}h40" fill="none" stroke="{GRND}" stroke-width="3"/>' for i in range(6))}
{cloud(120, 90, 1.1, 'blue')}''')

add('sleek', 'なめらかで、つやのある車体', f'''
<g transform="translate(300 250)">
  <path d="M-200 40q0-46 40-52 40-58 110-58t110 58q40 6 40 52z" class="teal o"/>
  <path d="M-110-18q40-46 96-46t94 46z" class="bluep o"/>
  <path d="M-160-6q120-26 320 0" fill="none" stroke="#fffefd" stroke-width="8" opacity="0.7"/>
  <circle cx="-110" cy="46" r="30" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle cx="112" cy="46" r="30" fill="none" stroke="{INK}" stroke-width="9"/></g>
{''.join(spark(x, y, 0.9) for x, y in [(130,150),(470,140)])}''')

add('sparkle', '水面のあちこちが、きらきらと光る', f'''
<path d="M0 200h600v200H0z" fill="{BLUP}"/>
<path d="M0 200h600" fill="none" stroke="{BLU}" stroke-width="4"/>
{sun(500, 90, 40)}
{''.join(spark(x, y, s) for x, y, s in [(110,250,1.2),(210,300,1),(300,240,1.4),(390,310,1.1),(470,260,1),(160,350,0.9),(520,340,1.2)])}''')

add('sleepless', '夜がふけても目が冴えて、眠れない', f'''
<path d="M0 0h600v400H0z" fill="#e9ecf2"/>
{bed(300, 340, 1.0)}
<g transform="translate(178 262)"><circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 108) scale(1.08)" fill="{HAIR}"/>
  <circle cx="-9" cy="-2" r="5" class="ink"/><circle cx="9" cy="-2" r="5" class="ink"/>
  <path d="M-8 14h16" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
<path d="M520 100a44 44 0 1 1-34-42 34 34 0 0 0 34 42z" class="goldp o"/>
{clock(90, 100, 0.7, 3, 0)}
{''.join(f'<path d="M{206+i*20} {230-i*10}v-16" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in range(3))}''')

add('sickness', '熱を出して、ふとんで休む', f'''
{bed(300, 340, 1.0)}
<g transform="translate(178 262)"><circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 108) scale(1.08)" fill="{HAIR}"/>
  <path d="M-14-6l12 6M14-6l-12 6" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-8 16q8-8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/></g>
<g transform="translate(178 210)"><rect x="-40" y="-12" width="80" height="22" rx="10" class="bluep o"/></g>
{''.join(f'<path d="M{240+i*28} 200q-14-20 0-40" fill="none" stroke="{CRL}" stroke-width="4"/>' for i in range(2))}
{thermometer(500, 200, 0.9, 0.7)}''')

add('sore', 'ひざが赤くはれて、ひりひり痛む', f'''
<g transform="translate(280 200)">
  <path d="M-60-140q60-24 120 0l-20 130q-40 16-80 0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-60-10q40 18 80 0l16 150q-56 16-112 0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-4" cy="0" r="46" class="coralp o"/>
  <circle cx="-4" cy="0" r="26" class="coral o"/></g>
<g class="corals" stroke-width="5">{''.join(f'<path d="M276 120v-24" transform="rotate({d} 276 200)"/>' for d in range(0, 360, 45))}</g>''')

add('skilful', 'ぶれずに三つを回して、みごとにあやつる', f'''
{person(300, 306, 1.25, 1, 'teal', 'blue', 'up', 'short', 'smile')}
{''.join(f'<circle cx="{x}" cy="{y}" r="24" class="{c} o"/>' for x, y, c in [(220,120,'coral'),(300,70,'gold'),(380,120,'green')])}
<path d="M230 160q70-90 140 0" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"/>
{''.join(spark(x, y, 0.8) for x, y in [(140,120),(470,130)])}''')

# --- 名詞 --------------------------------------------------------------------

add('savings', 'こつこつ入れて、たまっていく貯金', f'''
{table(330)}
<g transform="translate(300 300)"><ellipse cx="0" cy="-70" rx="100" ry="76" class="coralp o"/>
  <path d="M-100-70q-20 0-24-26 20-8 30 6" class="coralp o"/>
  <path d="M96-92q30-10 34-34-8 34-24 46" class="coralp o"/>
  <ellipse cx="-66" cy="-90" rx="10" ry="8" class="ink"/>
  <path d="M-14-140h34v10h-34z" class="corald o"/>
  <path d="M-60 0v6M-20 4v6M20 4v6M60 0v6" stroke="{CRLD}" stroke-width="12" stroke-linecap="round"/></g>
{coin(300, 100, 24)}
<path d="M300 130v22" class="a" marker-end="url(#ar)"/>
{coin(130, 300, 20)}{coin(180, 306, 20)}''', arrow=True)

add('semester', '一年を二つに分けた、前半の学期', f'''
<g transform="translate(300 130)"><rect x="-250" y="-60" width="500" height="120" rx="12" class="paper"/>
  <path d="M0-60v120" fill="none" stroke="{MUTED}" stroke-width="4"/>
  {''.join(f'<rect x="{-234+i*40}" y="-28" width="28" height="56" rx="5" class="{"tealp" if i < 6 else "goldp"} o"/>' for i in range(12))}</g>
{ring(180, 130, 120)}
<g transform="translate(300 306)">{building(0, 0, 0.8, 'teal')}</g>''')

add('semi-detached', '壁を共有して、二軒がくっついた家', f'''
<g transform="translate(300 306)">
  <path d="M-200 0v-120h400V0z" fill="#fffefd" class="o"/>
  <path d="M-214-120L-100-190 0-120zM0-120l100-70 114 70z" class="corald o"/>
  <path d="M0-190v190" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-130 0v-56h48V0zM82 0v-56h48V0z" class="coral o"/>
  <rect x="-70" y="-100" width="40" height="34" class="coralp o"/>
  <rect x="30" y="-100" width="40" height="34" class="coralp o"/></g>''')

add('semifinal', '勝ち残った四人で行う、決勝の一つ前', f'''
{''.join(f'<path d="M100 {90+i*80}h60v{40}h-60" fill="none" stroke="{MUTED}" stroke-width="4"/>' for i in [0, 2])}
<g fill="none" stroke="{CRL}" stroke-width="6">
  <path d="M160 110h50v70h60M160 190h50M160 270h50v-70"/>
  <path d="M160 350h50v-70"/></g>
<path d="M100 110h60M100 190h60M100 270h60M100 350h60" fill="none" stroke="{MUTED}" stroke-width="4"/>
{''.join(head(76, 90 + i*80, 22, c, h) for i, (c, h) in enumerate([('teal','short'),('coral','bob'),('green','short'),('gold','bun')]))}
<path d="M280 180h70" fill="none" stroke="{MUTED}" stroke-width="4"/>
{ring(215, 230, 96)}
<g transform="translate(420 180)"><path d="M-40 40l10-60h60l10 60z" class="gold o"/>
  <path d="M-30-20q-30 0-30-30h30M30-20q30 0 30-30h-30" fill="none" stroke="{GLDD}" stroke-width="6"/></g>''')

add('server', '料理を運ぶ給仕係と、通信を受けもつ機械', f'''
{split()}
{person(150, 330, 1.2, 1, 'teal', 'blue', 'carry', 'bun', 'smile')}
<g transform="translate(164 210)"><ellipse rx="66" ry="16" fill="#fffefd" class="o"/>
  <circle cx="-20" cy="-12" r="14" class="coral o"/><circle cx="16" cy="-14" r="12" class="greenp o"/></g>
<g transform="translate(450 220)"><rect x="-90" y="-140" width="180" height="280" rx="10" class="teald o"/>
  {''.join(f'<g><rect x="-72" y="{-120+i*54}" width="144" height="40" rx="5" fill="#dfe6ea"/>'
           f'<circle cx="52" cy="{-100+i*54}" r="7" class="green"/></g>' for i in range(5))}</g>''')

add('serving', '大なべから、ひとり分をすくって取り分ける', f'''
{table(320)}
<g transform="translate(180 280)"><path d="M-90 0q0 20 90 20t90-20v-56h-180z" class="teal o"/>
  <ellipse cy="-56" rx="90" ry="22" class="tealp o"/></g>
<g transform="translate(320 190) rotate(28)"><path d="M-8 0h16v90h-16z" class="goldd o"/>
  <ellipse cy="-16" rx="30" ry="20" class="goldp o"/></g>
<path d="M380 250h40" class="a" marker-end="url(#ar)"/>
<g transform="translate(490 280)"><ellipse rx="70" ry="20" fill="#fffefd" class="o"/>
  <ellipse cy="-8" rx="30" ry="14" class="goldp o"/></g>''', arrow=True)

add('spinach', '根が赤い、緑の濃い葉もの', f'''
{table(330)}
<g transform="translate(300 306)">
  {''.join(f'<path d="M0 0q-{40+i*18} -{60+i*20} -{10+i*30} -{120+i*24}q{50+i*20} {20+i*10} {14+i*30} {120+i*24}z" class="{"green" if i%2 else "greenp"} o" transform="rotate({-40+i*26} 0 0)"/>' for i in range(5))}
  <path d="M-16 0h32l-8 34h-16z" class="coral o"/>
  <path d="M0 34v20" fill="none" stroke="{CRLD}" stroke-width="5"/></g>''')

add('spray', '霧のように、細かく吹きかける', f'''
<g transform="translate(160 280)"><path d="M-40 0v-84h80V0z" class="bluep o"/>
  <path d="M-20-84v-24h40v24z" class="blued o"/>
  <path d="M-24-108h48v-16h-48z" class="blue o"/>
  <path d="M24-118h30v-14" fill="none" stroke="{INK}" stroke-width="7"/></g>
{''.join(f'<circle cx="{250+i*20+ (i%3)*10}" cy="{160+(i%5)*26+(i//5)*10}" r="{3+(i%3)}" class="blue"/>' for i in range(24))}
<g transform="translate(500 300)"><path d="M0 0v-70" fill="none" stroke="{GRND}" stroke-width="6"/>
  <path d="M0-46q-34-6-40-40 32 2 40 30z" class="greenp o"/>
  <path d="M0-62q34-8 40-42-34 4-40 32z" class="greenp o"/></g>''')

add('spreadsheet', 'ますに数を並べて、下で合計を出す表', f'''
<g transform="translate(300 190)"><rect x="-250" y="-140" width="500" height="280" rx="10" class="paper"/>
  <rect x="-250" y="-140" width="500" height="44" rx="0" class="teal o"/>
  {''.join(f'<path d="M-250 {-96+i*46}h500" fill="none" stroke="#dde4e8" stroke-width="3"/>' for i in range(5))}
  {''.join(f'<path d="M{-150+i*100} -140v280" fill="none" stroke="#dde4e8" stroke-width="3"/>' for i in range(4))}
  {''.join(f'<rect x="{-130+ (i%4)*100}" y="{-84+(i//4)*46}" width="{50+(i%3)*14}" height="14" rx="7" fill="{MUTED}"/>' for i in range(12))}
  <path d="M-250 94h500" fill="none" stroke="{INK}" stroke-width="4"/>
  <rect x="120" y="108" width="110" height="18" rx="9" class="coral"/></g>''')

add('sprint', '短い距離を、全力で走りぬける', f'''
<path d="M0 340h600v10H0z" class="goldd o"/>
{''.join(f'<path d="M{60+i*90} 350v40" fill="none" stroke="#ffffff" stroke-width="5"/>' for i in range(6))}
{person(360, 340, 1.3, 1, 'coral', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round">
  <path d="M230 180h-90M210 240h-110M240 300h-90"/></g>
<path d="M540 200v160" fill="none" stroke="{CRL}" stroke-width="8"/>
<path d="M540 200h-70v40h70z" class="coral o"/>''')

add('spontaneous', 'だれが決めたわけでもなく、その場で自然に始まる', f'''
{person(300, 306, 1.25, 1, 'coral', 'blue', 'up', 'short', 'smile')}
{person(150, 306, 1.05, 1, 'teal', 'green', 'up', 'bob', 'smile')}
{person(450, 306, 1.05, -1, 'violet', 'blue', 'up', 'short', 'smile')}
{''.join(spark(x, y, 1.1) for x, y in [(230,110),(370,100),(90,180),(520,170)])}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8">
  <path d="M256 160q44-40 88 0"/></g>''')

add('sooner or later', '早いか遅いかの違いで、どちらにせよそうなる', f'''
{split()}
{clock(150, 130, 0.8, 2, 0)}
{clock(450, 130, 0.8, 10, 0)}
<g transform="translate(150 300)"><path d="M-60 0v-40h120V0z" class="teal o"/><circle cy="-64" r="26" class="coral o"/></g>
<g transform="translate(450 300)"><path d="M-60 0v-40h120V0z" class="teal o"/><circle cy="-64" r="26" class="coral o"/></g>
<path d="M150 200v40" class="a" marker-end="url(#ar)"/>
<path d="M450 200v40" class="a" marker-end="url(#ar)"/>''', arrow=True)

add('sonic', '空気をふるわせて伝わる音そのもの', f'''
<g transform="translate(150 200)"><circle r="34" class="coral o"/></g>
{''.join(f'<circle cx="150" cy="200" r="{70+i*46}" fill="none" stroke="{CRL}" stroke-width="6" opacity="{1-i*0.18:.2f}"/>' for i in range(5))}
{head(520, 250, 30, 'teal', 'short')}
<path d="M480 200l-40 20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"/>''')

print(sheet(W, '/tmp/vocab-sheet.html', 5))
print(len(W))
