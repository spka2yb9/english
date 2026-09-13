# -*- coding: utf-8 -*-
"""第130回。mis- と out- の動詞。mis- は「正しい／誤った」、out- は「相手を上回る」で描く。"""
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

# --- mis- の動詞 --------------------------------------------------------------
add('misspell', '語のつづりを一字まちがえて赤い波線が引かれる', f'''
{table(380)}
<g transform="translate(300 190)">
  <path d="M-220-120h440v240h-440z" class="paper"/>
  {word(0, -60, 7, 30, INK)}
  {word(0, 10, 7, 30, INK, 4)}
  <path d="M-84 34q10-8 20 0t20 0 20 0 20 0 20 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
</g>
{tick(120, 320, 0.7)}
{cross(300, 320, 0.7)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M470 320l-100-90"/></g>''', arrow=True, ground=False)

add('misread', '同じ文を読んで、まったく違う内容だと受け取る', f'''
{table(380)}
<g transform="translate(180 200)">
  {doc(0, 0, 170, 210, 5)}
</g>
{person(430, 380, 1.1, -1, 'coral', 'blue', 'hold', 'bun', 'neutral')}
<g transform="translate(420 160)">
  <path d="M-70-40h140q12 0 12 12v40q0 12-12 12h-96l-22 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, 0, 4, 28, TONES['coral'][0])}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M280 200h60"/></g>
{cross(300, 320, 0.7)}''', ground=False)

add('misinterpret', 'ほほえみを怒りだと取り違える', f'''
{table(380)}
{person(150, 380, 1.05, 1, 'teal', 'blue', 'stand', 'bun', 'smile')}
{person(450, 380, 1.05, -1, 'coral', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(310 170)">
  <path d="M-70-50h140q12 0 12 12v56q0 12-12 12h-96l-22 16v-16q-12 0-12-12v-56q0-12 12-12z" fill="#fffefd" class="o"/>
  <circle cy="6" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-30-12q12-14 22 0M8-12q12-14 22 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-12 20q12-12 24 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M230 250h60"/></g>
{cross(300, 320, 0.8)}''', ground=False)

add('misjudge', '見た目で弱そうだと判断して読み違える', f'''
{split()}
{table(380)}
{person(150, 380, 0.85, 1, 'gold', 'blue', 'stand', 'bob', 'smile')}
<g transform="translate(150 200)">
  <path d="M-60-40h120q12 0 12 12v40q0 12-12 12h-84l-20 16v-16q-16 0-16-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-30 6q30-20 60 0" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
{person(450, 380, 0.85, 1, 'gold', 'blue', 'up', 'bob', 'smile')}
<g transform="translate(450 300)">
  <g fill="{INK}"><rect x="-70" y="-14" width="140" height="18" rx="9"/><rect x="-96" y="-34" width="26" height="58" rx="8"/><rect x="70" y="-34" width="26" height="58" rx="8"/></g>
</g>
{cross(150, 100, 0.7)}
{tick(450, 100, 0.7)}''', ground=False)

add('mislead', 'まちがった方向を指す道しるべに従わせる', f'''
<path d="M0 0h600v250H0z" fill="#dceaf4"/>
<path d="M0 250h600v150H0z" fill="#dfe8d8"/>
<path d="M0 250h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M60 380h480" fill="none" stroke="#c9a464" stroke-width="22" stroke-dasharray="20 16"/>
<g transform="translate(300 250)">
  <path d="M-6 0v-120h12V0z" fill="{BRN}" class="o"/>
  <path d="M6-110h110l24 24-24 24H6z" class="coral o"/>
</g>
{person(200, 380, 0.95, 1, 'teal', 'blue', 'walk', 'cap', 'neutral', 'walk')}
<g transform="translate(500 300)">
  <path d="M-40 60l40-90 40 90z" class="gold o"/>
  <path d="M-4-16h8v34h-8z" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M340 180h120"/></g>
{cross(120, 160, 0.7)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="4"><path d="M260 200H120"/></g>''', ground=False)

add('miscalculate', '計算を間違えて答えがずれる', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-150-140h300v280h-300z" fill="#c8d0d8" class="o"/>
  <path d="M-120-116h240v60h-240z" fill="#2c333d" class="o"/>
  <g fill="{TONES['green'][0]}">
''' + ''.join(f'<rect x="{-40+i*30}" y="-98" width="20" height="26" rx="3"/>' for i in range(4)) + f'''
  </g>
  <g fill="#8f9aa6" class="o">
''' + ''.join(f'<rect x="{-116+ (i%4)*62}" y="{-32+(i//4)*46}" width="46" height="34" rx="6"/>' for i in range(12)) + f'''
  </g>
</g>
<g transform="translate(470 130)">
  <path d="M-56-40h112v80h-112z" class="paper"/>
  {word(0, 0, 3, 26, TONES['coral'][0])}
</g>
{cross(470, 250, 0.8)}''', ground=False)

add('misplace', 'かばんをどこに置いたか分からなくなる', f'''
{table(380)}
<g transform="translate(140 330)">
  <path d="M-50-30h100v60h-100z" class="coral o"/>
  <path d="M-24-30q0-16 24-16t24 16" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g fill="{MUTED}" opacity="0.35"><path d="M90 300h100v60H90z"/></g>
{person(400, 380, 1.1, -1, 'teal', 'blue', 'up', 'bun', 'sad')}
<g transform="translate(490 180)">
  <path d="M-40-40h80q12 0 12 12v40q0 12-12 12h-52l-20 16v-16q-20 0-20-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-18-24q0-20 18-20t18 20-18 16v10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="18" r="4.5" fill="{INK}"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M330 300q-90 40-160 20"/></g>''', ground=False)

add('mishandle', 'こわれ物を乱暴に扱って割ってしまう', f'''
{table(380)}
{person(180, 380, 1.1, 1, 'blue', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(400 260)">
  <path d="M-60-70h120v20h-120z" class="gold o"/>
  <path d="M-50-50h100v100h-100z" class="goldp o"/>
  <path d="M-50-50l100 100M50-50l-100 100" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<g fill="#e8f0f6" class="o">
''' + ''.join(f'<path d="M{330+i*36} {340+(i%3)*20}l24 8-10 20-24-10z"/>' for i in range(5)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M270 200q80-40 100 20"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M470 180l24-20M490 240h26"/>
</g>''', ground=False)

add('mismatch', '合うはずの二つの部品が形が違ってはまらない', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <path d="M-100-50h90v40q0 20 10 20t10-20v-40h90v100h-190z" class="tealp o"/>
  <path d="M-100 70h190v50h-190z" class="teal o"/>
  <path d="M-6 60h12v14h-12z" fill="none"/>
  <path d="M-100 70h90v-20q0-20 10-20t10 20v20h90" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(450 230)">
  <path d="M-100-50h90v40q0 20 10 20t10-20v-40h90v100h-190z" class="coralp o"/>
  <path d="M-100 80h190v50h-190z" class="coral o"/>
  <path d="M-100 80h190" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-40 80h80v-20h-80z" class="coral o"/>
</g>
{tick(150, 120, 0.7)}
{cross(450, 120, 0.7)}''', ground=False)

add('misbehave', '静かにすべき場所で騒いで行儀悪くする', f'''
{table(380)}
<g transform="translate(300 240)">
  <path d="M-260-160h520v20h-520z" fill="#c9a464" class="o"/>
</g>
{sit(150, 380, 0.9, 1, 'blue', 'blue', 'short', 'neutral', 'lap')}
{sit(450, 380, 0.9, 1, 'blue', 'blue', 'bob', 'neutral', 'lap')}
{chair(150, 380, 0.85, 'gold', 1)}
{chair(450, 380, 0.85, 'gold', 1)}
<g transform="translate(300 320)">
  <path d="M-12-8l-36 30M12-8l38 26" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-27-78q27-14 54 0l-8 72h-38z" class="coral o"/>
  <path d="M-22-70l-32-30M22-70l32-30" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cy="-108" r="25" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" fill="{HAIR}"/>
  <circle cx="-8" cy="-104" r="2.2" fill="{INK}"/><circle cx="8" cy="-104" r="2.2" fill="{INK}"/>
  <path d="M-10-90q10 12 20 0z" fill="{INK}" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M360 200q30 34 0 68M400 174q46 60 0 120"/>
</g>
{cross(150, 130, 0.7)}''', ground=False)

add('misuse', '工具を本来と違う使い方をして壊す', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-10-70h20v90h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-30 20h40v40q0 10-20 10t-20-10z" fill="{INK}"/>
  <path d="M-10-70l-16-18h52l-16 18z" fill="#b8bfc8" class="o"/>
  <path d="M-6 100h12v40h-12z" fill="#c9a464" class="o"/>
  <path d="M-30 140h60v14h-60z" fill="#a0764a"/>
</g>
{tick(150, 120, 0.7)}
<g transform="translate(450 250) rotate(30)">
  <path d="M-10-70h20v90h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-30 20h40v40q0 10-20 10t-20-10z" fill="{INK}"/>
</g>
<g transform="translate(470 320)">
  <path d="M-60-20h120v40h-120z" class="tealp o"/>
  <path d="M-30-20l30 40 30-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
{cross(450, 120, 0.7)}''', ground=False)

add('mistrust', '差し出された書類を疑って受け取らない', f'''
{table(380)}
{person(170, 380, 1.05, 1, 'gold', 'blue', 'give', 'short', 'smile')}
{person(440, 380, 1.05, -1, 'teal', 'blue', 'hold', 'bun', 'sad')}
<g transform="translate(300 250)">{doc(0, 0, 110, 130, 3)}</g>
<g transform="translate(440 240)">
  <path d="M-30-6q14-16 26 0M0-6q14-16 26 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" transform="translate(-8 0)"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M356 200l40 40M396 200l-40 40"/>
</g>
<g transform="translate(500 150)">
  <path d="M-36-30h72q10 0 10 10v30q0 10-10 10h-48l-16 14v-14q-18 0-18-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-14-18q0-14 14-14t14 14-14 12v8" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle cy="14" r="3.5" fill="{INK}"/>
</g>''', ground=False)

# --- out- の動詞 --------------------------------------------------------------
add('outdo', '相手より高く跳んで上を行く', f'''
{table(380)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 250h520M40 160h520"/></g>
{person(180, 300, 0.95, 1, 'blue', 'blue', 'up', 'short', 'neutral')}
{person(420, 210, 1.0, 1, 'coral', 'gold', 'up', 'cap', 'smile')}
<g fill="none" stroke="{MUTED}" stroke-width="3"><ellipse cx="180" cy="382" rx="40" ry="8"/><ellipse cx="420" cy="382" rx="40" ry="8"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M540 250v-90"/></g>''', ground=False)

add('outlast', '同じろうそくのうち、片方だけが長く燃え続ける', f'''
{table(380)}
<g transform="translate(180 380)">
  <path d="M-30-40h60v40h-60z" fill="#e8dcc0" class="o"/>
  <path d="M-30-40h60v-10h-60z" fill="#d8ccb0"/>
  <path d="M0-50v-14" stroke="{INK}" stroke-width="4" fill="none"/>
  <g fill="{MUTED}" opacity="0.7"><circle cx="0" cy="-80" r="12"/><circle cx="8" cy="-100" r="9"/></g>
</g>
<g transform="translate(420 380)">
  <path d="M-30-180h60v180h-60z" fill="#e8dcc0" class="o"/>
  <path d="M-30-180h60v-10h-60z" fill="#d8ccb0"/>
  {flame(0, -190, 0.4)}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 200h520"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M540 340v-160"/></g>
{cross(180, 300, 0.6)}''', ground=False)

add('outnumber', '片方の陣営が人数で大きく上回る', f'''
{split()}
{table(380)}
<g>
''' + ''.join(head(70+ (i%3)*60, 240+(i//3)*70, 22, 'blue', 'short') for i in range(3)) + f'''
</g>
<g>
''' + ''.join(head(340+ (i%5)*54, 200+(i//5)*66, 20, 'coral', ['short','bob','bun','cap'][i%4]) for i in range(15)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M280 130H180"/></g>''', ground=False)

add('outperform', '二本の折れ線のうち片方が大きく上を行く', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 220)">
  <path d="M-250 140h500v6h-500z" fill="{INK}"/>
  <path d="M-250-160v300h6v-300z" fill="{INK}"/>
  <path d="M-230 110l60-30 60-40 60-70 60-60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linejoin="round"/>
  <path d="M-230 120l60-6 60-14 60-10 60-14" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linejoin="round"/>
  <g fill="{TONES['coral'][2]}"><circle cx="10" cy="-90" r="8"/></g>
  <g fill="{MUTED}"><circle cx="10" cy="76" r="7"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M480 250v-120"/></g>''', ground=False)

add('outsmart', 'わなを見抜いて回り道し、相手を出し抜く', f'''
{table(380)}
<g transform="translate(330 340)">
  <path d="M-70-16h140v16h-140z" fill="#6b4c28" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="5">
''' + ''.join(f'<path d="M{-60+i*24} -16v-30"/>' for i in range(6)) + f'''
  </g>
</g>
{person(120, 380, 1.0, 1, 'blue', 'blue', 'point', 'cap', 'sad')}
{person(510, 300, 0.95, 1, 'coral', 'gold', 'up', 'bun', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 8"><path d="M200 300q80-160 280-40"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M40 380h520"/></g>
{cross(330 , 240, 0.6)}''', ground=False)

add('outsource', '社内でやっていた仕事を外の会社に出す', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-110-120h220v240h-220z" fill="#e0d6c0" class="o"/>
  <path d="M-110-120h220v-20h-220z" class="teal o"/>
</g>
{head(110, 250, 20, 'teal', 'short')}
{head(190, 250, 20, 'coral', 'bob')}
{head(150, 320, 20, 'gold', 'bun')}
<g transform="translate(450 240)">
  <path d="M-110-120h220v240h-220z" fill="#e0d6c0" class="o"/>
  <path d="M-110-120h220v-20h-220z" class="violet o"/>
</g>
{head(410, 250, 20, 'violet', 'cap')}
{head(490, 250, 20, 'green', 'short')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M270 150h60"/></g>
<g transform="translate(300 150)">
  <path d="M-30-24h60v48h-60z" class="paper"/>
</g>''', ground=False)

add('outweigh', 'てんびんの片側が重くてもう一方を押し下げる', f'''
{table(380)}
<g transform="translate(300 160)">
  <path d="M-10 0h20v180h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-70 180h140v20h-140z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(300 160) rotate(14)">
  <path d="M-200-8h400v16h-400z" fill="#b8bfc8" class="o"/>
  <circle r="16" fill="#8f9aa6" class="o"/>
  <path d="M-190 8v40M190 8v40" stroke="{INK}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(252 234)">
  <path d="M-56 0q0 30 56 30t56-30z" class="coralp o"/>
  <ellipse ry="10" rx="56" class="coralp o"/>
  <g class="coral o"><circle cx="-20" cy="-14" r="18"/><circle cx="16" cy="-18" r="20"/></g>
</g>
<g transform="translate(348 132)">
  <path d="M-56 0q0 30 56 30t56-30z" class="tealp o"/>
  <ellipse ry="10" rx="56" class="tealp o"/>
  <circle cy="-12" r="12" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M140 200v70"/></g>''', ground=False)

add('outdated', '型の古い機械と、今の機械が並んでいる', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90-90h180v140h-180z" fill="#c8b8a0" class="o"/>
  <path d="M-64-64h128v90h-128z" fill="#8f9aa6" class="o"/>
  <path d="M-40 50h80v30h-80z" fill="#a89880" class="o"/>
  <g fill="#7d8894"><rect x="-40" y="-40" width="80" height="46" rx="6"/></g>
</g>
<g transform="translate(450 250)">
  <path d="M-110-70h220v130h-220z" fill="#3b4450" class="o"/>
  <path d="M-100-60h200v110h-200z" fill="#dceaf4"/>
  <path d="M-30 60h60v14h-60z" fill="#5a6270"/>
  <g fill="{TONES['teal'][0]}"><rect x="-76" y="-40" width="60" height="40" rx="6"/><rect x="-8" y="-40" width="80" height="18" rx="6"/><rect x="-8" y="-14" width="60" height="18" rx="6"/></g>
</g>
{cross(150, 120, 0.7)}
{tick(450, 120, 0.7)}''', ground=False)

# --- 物と人 -----------------------------------------------------------------
add('login', '名前と合い言葉を入れて中に入る', f'''
{table(380)}
<g transform="translate(300 200)">
  <path d="M-190-140h380v260h-380z" fill="#3b4450" class="o"/>
  <path d="M-170-120h340v220h-340z" fill="#eef2f6"/>
  <g transform="translate(0 -70)">
    <circle r="30" fill="{TONES['teal'][1]}" class="o"/>
    <circle cy="-8" r="11" fill="{TONES['teal'][0]}"/>
    <path d="M-18 20q18-20 36 0z" fill="{TONES['teal'][0]}"/>
  </g>
  <g>
    <path d="M-120-20h240v34h-240z" fill="#fffefd" class="o"/>
    <path d="M-120 30h240v34h-240z" fill="#fffefd" class="o"/>
    {word(-40, -3, 4, 22, MUTED)}
    <g fill="{MUTED}"><circle cx="-100" cy="47" r="7"/><circle cx="-80" cy="47" r="7"/><circle cx="-60" cy="47" r="7"/><circle cx="-40" cy="47" r="7"/></g>
  </g>
  <path d="M-60 80h120v30h-120z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M300 350v-30"/></g>''', ground=False)

add('logout', '扉から外へ出て、画面から抜ける', f'''
{table(380)}
<g transform="translate(260 200)">
  <path d="M-160-140h320v260h-320z" fill="#3b4450" class="o"/>
  <path d="M-140-120h280v220h-280z" fill="#eef2f6"/>
  <path d="M-60-70h120v170h-120z" fill="#c9a464" class="o"/>
  <circle cx="40" cy="10" r="8" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M300 210h150"/></g>
<g transform="translate(510 210)">
  <circle r="30" fill="{TONES['teal'][1]}" class="o"/>
  <circle cy="-8" r="11" fill="{TONES['teal'][0]}"/>
  <path d="M-18 20q18-20 36 0z" fill="{TONES['teal'][0]}"/>
</g>''', ground=False)

add('mat', '玄関に敷いた四角い敷物', f'''
<path d="M0 0h600v400H0z" fill="#e8e2d6"/>
<path d="M0 300h600v100H0z" fill="#c9a464" class="o"/>
<g transform="translate(300 170)">
  <path d="M-130-140h260v270h-260z" fill="{BRN}" class="o"/>
  <path d="M-104-114h208v240h-208z" fill="#a0764a" class="o"/>
  <circle cx="70" cy="10" r="11" class="gold o"/>
</g>
<g transform="translate(300 340)">
  <path d="M-140-40h280v80h-280z" fill="#8b6437" class="o"/>
  <path d="M-120-24h240v48h-240z" fill="#a0764a"/>
  <g fill="none" stroke="#6b4c28" stroke-width="3">
''' + ''.join(f'<path d="M{-110+i*28} -24v48"/>' for i in range(9)) + f'''
    <path d="M-120 0h240"/>
  </g>
</g>''', ground=False)

add('melon', '網目のある大きなメロンを切って中を見せる', f'''
{table(330)}
<g transform="translate(200 240)">
  <circle r="90" fill="#c8d49c" class="o"/>
  <g fill="none" stroke="#e8f0d0" stroke-width="4">
    <path d="M-80-30q80 30 160-10M-70 20q70 30 148-6M-30-76q-20 80 10 156M40-80q20 80-14 152"/>
  </g>
</g>
<g transform="translate(420 250)">
  <path d="M-100 0a100 100 0 0 1 200 0z" fill="#c8d49c" class="o"/>
  <path d="M-86 0a86 86 0 0 1 172 0z" fill="#f0d8a8" class="o"/>
  <path d="M-56 0a56 56 0 0 1 112 0z" fill="#f6e8c4" class="o"/>
  <g fill="#e0c890"><circle cx="-24" cy="-18" r="6"/><circle cx="0" cy="-24" r="6"/><circle cx="24" cy="-18" r="6"/></g>
</g>''', ground=False)

add('menu', '料理の名前と値段が並んだ献立表', f'''
{table(380)}
<g transform="translate(300 200) rotate(-3)">
  <path d="M-150-150h300v300h-300z" class="paper"/>
  <rect x="-90" y="-124" width="180" height="18" rx="9" fill="{INK}"/>
  <path d="M-110-88h220" stroke="{INK}" stroke-width="3" fill="none"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-52+i*44})">
  <rect x="-110" y="-7" width="{130-(i%3)*30}" height="14" rx="7" fill="{MUTED}"/>
  <rect x="60" y="-7" width="50" height="14" rx="7" fill="{TONES['coral'][0]}"/>
  <path d="M{50-(i%3)*30} 0h4" stroke="{MUTED}" stroke-width="2" stroke-dasharray="4 4"/>
</g>''' for i in range(5)) + f'''
  </g>
</g>
<g transform="translate(500 330)">
  <ellipse rx="50" ry="14" fill="#fffdf6" class="o"/>
  <path d="M-50 0q0 18 50 18t50-18z" fill="#fffdf6" class="o"/>
</g>''', ground=False)

add('midnight', '時計の針が両方とも真上を指す真夜中', f'''
<path d="M0 0h600v400H0z" fill="#1e2338"/>
<g fill="#fffefd"><circle cx="90" cy="70" r="4"/><circle cx="520" cy="60" r="3"/><circle cx="140" cy="330" r="3"/><circle cx="500" cy="340" r="4"/></g>
<circle cx="490" cy="90" r="34" fill="#f0e6c0" class="o"/>
<g transform="translate(280 210)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <circle r="112" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-5" y="-108" width="10" height="22" rx="5" transform="rotate({i*30})"/>' for i in range(12)) + f'''
  </g>
  <path d="M0 0v-70" stroke="{INK}" stroke-width="10" stroke-linecap="round" fill="none"/>
  <path d="M0 0v-92" stroke="{INK}" stroke-width="6" stroke-linecap="round" fill="none"/>
  <circle r="10" fill="{INK}"/>
</g>
<g fill="#2b3242"><path d="M0 340h600v60H0z"/></g>''', ground=False)

add('necklace', '首にかけた鎖と飾り', f'''
{table(380)}
<g transform="translate(300 190)">
  <circle r="90" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-80-24q6-64 80-64t80 64q-40-30-80-30t-80 30z" fill="{HAIR}"/>
  <circle cx="-32" cy="-4" r="6" fill="{INK}"/><circle cx="32" cy="-4" r="6" fill="{INK}"/>
  <path d="M-18 38q18 16 36 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
  <path d="M-40 84h80v40h-80z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-100 130q100-50 200 0l-20 100h-160z" class="teal o"/>
</g>
<g>
  <path d="M234 274q66 70 132 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="6"/>
  <g fill="{TONES['gold'][0]}" class="o">
''' + ''.join(f'<circle cx="{250+i*20}" cy="{292+ int(-abs(i-3)*abs(i-3)*2.2+20)}" r="6"/>' for i in range(7)) + f'''
  </g>
  <path d="M300 330l16 28-16 22-16-22z" class="teal o"/>
</g>''', ground=False)

add('nephew', '家系図で兄弟姉妹の息子にあたる位置', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g fill="none" stroke="{BRN}" stroke-width="4">
  <path d="M300 90v30M170 120h260M170 120v40M430 120v40M170 210v40M430 210v40M120 250h100M380 250h100M120 250v30M220 250v30M380 250v30M480 250v30"/>
</g>
{head(300, 60, 24, 'gold', 'bun')}
{head(170, 190, 22, 'teal', 'short')}
{head(430, 190, 22, 'coral', 'bob')}
{head(120, 310, 19, 'blue', 'cap')}
{head(220, 310, 19, 'green', 'bob')}
{head(380, 310, 19, 'violet', 'cap')}
{head(480, 310, 19, 'gold', 'bun')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="10 8"><circle cx="170" cy="196" r="48"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"><circle cx="380" cy="316" r="44"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M540 380l-110-50"/></g>''', arrow=True, ground=False)

add('niece', '家系図で兄弟姉妹の娘にあたる位置', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g fill="none" stroke="{BRN}" stroke-width="4">
  <path d="M300 90v30M170 120h260M170 120v40M430 120v40M170 210v40M430 210v40M120 250h100M380 250h100M120 250v30M220 250v30M380 250v30M480 250v30"/>
</g>
{head(300, 60, 24, 'gold', 'bun')}
{head(170, 190, 22, 'teal', 'short')}
{head(430, 190, 22, 'coral', 'bob')}
{head(120, 310, 19, 'blue', 'cap')}
{head(220, 310, 19, 'green', 'bob')}
{head(380, 310, 19, 'violet', 'cap')}
{head(480, 310, 19, 'gold', 'bun')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="10 8"><circle cx="170" cy="196" r="48"/></g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="5" stroke-dasharray="10 8"><circle cx="480" cy="316" r="44"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['violet'][0]}"><path d="M560 380l-70-40"/></g>''', arrow=True, ground=False)

add('orphan', '両親を亡くした子どもを親族が引き取る', f'''
{table(380)}
<g opacity="0.3">
  {head(160, 240, 24, 'teal', 'short')}
  {head(250, 240, 24, 'coral', 'bun')}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8">
  <path d="M120 200h180v120H120z"/>
</g>
{person(205, 380, 0.8, 1, 'gold', 'blue', 'stand', 'cap', 'sad')}
{person(430, 380, 1.05, -1, 'violet', 'blue', 'reach', 'bun', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M370 280h-90"/></g>''', ground=False)

add('lever', 'てこを使って重い石を持ち上げる', f'''
{table(380)}
<g transform="translate(360 330)">
  <path d="M-40 50l40-70 40 70z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(360 260) rotate(-20)">
  <path d="M-230-10h420v20h-420z" fill="#c9a464" class="o"/>
  <path d="M180-14h30v28h-30z" fill="#a0764a"/>
</g>
<g transform="translate(560 190)">
  <path d="M-50-40h100v70h-100z" fill="#9aa5b0" class="o"/>
</g>
{person(130, 380, 0.95, 1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M170 240v60"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M540 300v-70"/></g>''', ground=False)

# --- 増減と動作 --------------------------------------------------------------
add('lessen', '痛みを表す赤い印が小さくなっていく', f'''
{table(380)}
<g class="coral o" opacity="0.7">
  <circle cx="110" cy="220" r="70"/><circle cx="260" cy="230" r="52"/><circle cx="390" cy="240" r="34"/><circle cx="490" cy="248" r="18"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M110 130l-14-30M110 130l14-30M40 220l-30-10"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M110 330h400"/></g>''', ground=False)

add('lighten', '背負った荷物を減らして軽くする', f'''
{split()}
{table(380)}
{person(150, 380, 1.1, 1, 'teal', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(150 250)">
  <path d="M-56-70h112v130h-112z" class="gold o"/>
  <path d="M-56-70q56-24 112 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
</g>
{person(450, 380, 1.1, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(450 290)">
  <path d="M-34-34h68v56h-68z" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M540 300v-60"/></g>''', arrow=True, ground=False)

add('loosen', 'きつく締めたねじを回してゆるめる', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-100-20h200v40h-200z" fill="#c9a464" class="o"/>
  <path d="M-30-50l16-24h28l16 24-16 24h-28z" fill="#9aa5b0" class="o"/>
  <path d="M-30-50h60v70h-60z" fill="none"/>
  <circle cy="-26" r="12" fill="#7d8894"/>
</g>
<g transform="translate(450 260)">
  <path d="M-100-20h200v40h-200z" fill="#c9a464" class="o"/>
  <path d="M-30-90l16-24h28l16 24-16 24h-28z" fill="#9aa5b0" class="o"/>
  <path d="M-8-70h16v70h-16z" fill="#b8bfc8" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5">
''' + ''.join(f'<path d="M-8 {-60+i*16}l16 8"/>' for i in range(4)) + f'''
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M450 150v-40"/></g>''', arrow=True, ground=False)

add('lure', '光る餌で魚をおびき寄せる', f'''
<path d="M0 0h600v130H0z" fill="#dceaf4"/>
<path d="M0 130h600v270H0z" fill="#5b8caa"/>
<path d="M0 130h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<path d="M120 0v130" stroke="{MUTED}" stroke-width="3" fill="none"/>
<path d="M120 130v90" stroke="{MUTED}" stroke-width="3" fill="none"/>
<g transform="translate(120 240)">
  <path d="M-24-20h48l-6 40q-2 10-18 10t-18-10z" class="coral o"/>
  <g fill="{TONES['gold'][1]}" opacity="0.4"><circle r="50"/></g>
  <path d="M0 30v20M-14 50h28" stroke="{INK}" stroke-width="4" fill="none"/>
</g>
<g transform="translate(360 260)">
  <path d="M-70 0q30-40 70-40t60 40q-20 40-60 40t-70-40z" fill="#b8c8d4" class="o"/>
  <path d="M60 0l40-26v52z" fill="#b8c8d4" class="o"/>
  <circle cx="-40" cy="-8" r="5" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M270 250H190"/></g>''', ground=False)

add('magnify', '虫めがねで小さな文字を大きく見せる', f'''
{table(380)}
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-160" y="{-110+i*40}" width="{320-(i%3)*70}" height="10" rx="5"/>' for i in range(6)) + f'''
  </g>
</g>
<g transform="translate(360 240)">
  <circle r="90" fill="#eef6fb" class="o" opacity="0.9"/>
  <g fill="{INK}">
    <rect x="-64" y="-30" width="128" height="20" rx="10"/>
    <rect x="-64" y="6" width="96" height="20" rx="10"/>
  </g>
  <circle r="90" fill="none" stroke="#8f9aa6" stroke-width="12"/>
  <path d="M64 64l60 60" stroke="{INK}" stroke-width="18" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('mediate', '争う二人の間に立って話をまとめる', f'''
{table(380)}
{person(120, 380, 1.0, 1, 'blue', 'blue', 'point', 'short', 'sad')}
{person(480, 380, 1.0, -1, 'coral', 'blue', 'point', 'bun', 'sad')}
{person(300, 380, 1.1, 1, 'teal', 'gold', 'up', 'cap', 'neutral')}
{hand(230, 250, -1)}
{hand(370, 250, 1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M200 170l-24-20M400 165l24-20"/>
</g>
<g transform="translate(300 130)">
  <path d="M-50-30h100q10 0 10 10v30q0 10-10 10h-66l-18 14v-14q-16 0-16-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.4)}
</g>''', ground=False)

add('minimise', '大きく開いた画面を小さく縮める', f'''
{split()}
{table(380)}
<g transform="translate(150 200)">
  <path d="M-120-120h240v240h-240z" fill="#3b4450" class="o"/>
  <path d="M-108-108h216v216h-216z" fill="#eef2f6"/>
  <path d="M-108-108h216v26h-216z" class="teal"/>
</g>
<g transform="translate(450 260)">
  <path d="M-60-40h120v80h-120z" fill="#3b4450" class="o"/>
  <path d="M-52-32h104v64h-104z" fill="#eef2f6"/>
  <path d="M-52-32h104v14h-104z" class="teal"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>
<g class="a" marker-end="url(#ar)"><path d="M380 120l40 40M520 120l-40 40"/></g>''', arrow=True, ground=False)

add('moisten', 'かわいたスポンジに水をたらして湿らせる', f'''
{split()}
{table(340)}
<g transform="translate(150 260)">
  <path d="M-80-40h160v70h-160z" class="goldp o"/>
  <g fill="#e8d8a8">
''' + ''.join(f'<circle cx="{-64+ (i%6)*26}" cy="{-20+(i//6)*30}" r="8"/>' for i in range(12)) + f'''
  </g>
</g>
<g transform="translate(450 260)">
  <path d="M-80-40h160v70h-160z" fill="#c8bc8c" class="o"/>
  <g fill="#a8a070">
''' + ''.join(f'<circle cx="{-64+ (i%6)*26}" cy="{-20+(i//6)*30}" r="8"/>' for i in range(12)) + f'''
  </g>
</g>
<g fill="{TONES['blue'][0]}">
''' + ''.join(f'<path d="M{410+i*30} {150+ (i%2)*24}q9 10 9 17t-9 8-9-8 9-17z"/>' for i in range(4)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>''', arrow=True, ground=False)

add('mutter', '不満そうに眉をひそめて小声でぶつぶつ言う', f'''
{table(380)}
{person(230, 380, 1.2, 1, 'blue', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(230 248)">
  <path d="M-26-14q14-16 26 0M2-14q14-16 26 0" fill="none" stroke="{HAIR}" stroke-width="5" stroke-linecap="round" transform="translate(-2 0)"/>
</g>
<g transform="translate(410 200)">
  <path d="M-70-40h140q12 0 12 12v40q0 12-12 12h-96l-24 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o" opacity="0.85"/>
  <g fill="{MUTED}" opacity="0.6">
''' + ''.join(f'<rect x="{-50+ (i%3)*38}" y="{-16+(i//3)*20}" width="30" height="9" rx="4.5"/>' for i in range(6)) + f'''
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6"><path d="M280 250l60-20"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M180 200l-24-18M300 190l20-20"/>
</g>''', ground=False)

add('omit', '一覧から一項目だけ抜かして飛ばす', f'''
{split()}
{table(380)}
<g transform="translate(150 200)">
  <path d="M-110-140h220v280h-220z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-100+i*46})">
  <circle cx="-76" r="9" fill="{INK}"/>
  <rect x="-58" y="-7" width="{130-(i%3)*30}" height="14" rx="7" fill="{MUTED}"/>
</g>''' for i in range(5)) + f'''
  </g>
</g>
<g transform="translate(450 200)">
  <path d="M-110-140h220v280h-220z" class="paper"/>
  <g>
''' + ''.join(f'''<g transform="translate(0 {-100+i*46})">
  <circle cx="-76" r="9" fill="{INK}"/>
  <rect x="-58" y="-7" width="{130-(i%3)*30}" height="14" rx="7" fill="{MUTED}"/>
</g>''' for i in [0, 1, 3, 4]) + f'''
  </g>
  <path d="M-96 90h190" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('ooze', '傷んだ果実から汁がじわじわしみ出る', f'''
{table(340)}
<g transform="translate(280 240)">
  <circle r="90" class="corald o"/>
  <path d="M0-90q-16-30 8-38 20 8 8 38z" class="greend o"/>
  <g fill="#8b3a2c"><ellipse cx="-30" cy="20" rx="30" ry="20"/><ellipse cx="34" cy="-10" rx="22" ry="15"/></g>
</g>
<g fill="#8b3a2c">
  <path d="M250 320q10 14 10 22t-10 10-10-10 10-22z"/>
  <path d="M300 336q9 12 9 19t-9 8-9-8 9-19z"/>
</g>
<g fill="#8b3a2c" opacity="0.6"><ellipse cx="280" cy="374" rx="60" ry="10"/></g>
<g class="a" marker-end="url(#ar)"><path d="M440 220q-40 60-100 90"/></g>''', arrow=True, ground=False)

add('overcharge', '本来より高い額を請求される', f'''
{split()}
{table(380)}
<g transform="translate(150 200)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-66" y="{-80+i*30}" width="{100-(i%3)*24}" height="10" rx="5"/>' for i in range(4)) + f'''
  </g>
  <rect x="0" y="60" width="66" height="18" rx="9" class="green"/>
</g>
<g transform="translate(450 200)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-66" y="{-80+i*30}" width="{100-(i%3)*24}" height="10" rx="5"/>' for i in range(4)) + f'''
  </g>
  <rect x="-30" y="56" width="96" height="26" rx="13" class="coral"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M270 200h60"/></g>
{cross(450, 350, 0.7)}''', arrow=True, ground=False)

add('let-off', '軽い違反を大目に見て見逃す', f'''
{table(380)}
{person(180, 380, 1.05, 1, 'blue', 'gold', 'point', 'cap', 'neutral')}
{person(420, 380, 1.05, -1, 'coral', 'blue', 'stand', 'bob', 'sad')}
<g transform="translate(300 180)">
  <path d="M-56-40h112q12 0 12 12v40q0 12-12 12h-72l-22 16v-16q-18 0-18-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.42)}
</g>
<g transform="translate(430 250)">
  <path d="M-30-24h60v48h-60z" class="paper"/>
  {cross(0, 0, 0.4)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M480 320h70"/></g>''', ground=False)

add('level-off', '上がり続けていた線が横ばいになる', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 240)">
  <path d="M-250 120h500v6h-500z" fill="{INK}"/>
  <path d="M-250-180v300h6v-300z" fill="{INK}"/>
  <path d="M-230 100l60-50 60-70 60-60 60-4 60-2 60-4" fill="none" stroke="{TONES['teal'][0]}" stroke-width="7" stroke-linejoin="round"/>
  <g fill="{TONES['teal'][2]}">
''' + ''.join(f'<circle cx="{-230+i*60}" cy="{[100,50,-20,-80,-84,-86,-90][i]}" r="7"/>' for i in range(7)) + f'''
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M-90-86h340"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M340 100h180"/></g>''', ground=False)

add('liberate', 'かごの戸を開けて鳥を自由にする', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-80 90h160v20h-160z" fill="#8f9aa6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="5">
''' + ''.join(f'<path d="M{-74+i*26} -60v150"/>' for i in range(7)) + f'''
    <path d="M-80-60h160"/>
  </g>
  <path d="M-80-60q80-60 160 0z" fill="#c8d0d8" class="o"/>
  <g transform="translate(0 30)">
    <ellipse rx="34" ry="26" class="gold o"/>
    <circle cx="26" cy="-18" r="17" class="gold o"/>
    <path d="M40-22l18 6-18 6z" class="corald o"/>
  </g>
</g>
<g transform="translate(450 280)">
  <path d="M-80 50h160v20h-160z" fill="#8f9aa6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="5">
''' + ''.join(f'<path d="M{-74+i*26} -100v150"/>' for i in [0,1,2,5,6]) + f'''
    <path d="M-80-100h160"/>
  </g>
  <path d="M8-100h72v150H8z" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="10 8" transform="rotate(24 8 -100)"/>
</g>
<g transform="translate(470 120)">
  <ellipse rx="34" ry="24" class="gold o"/>
  <circle cx="26" cy="-16" r="16" class="gold o"/>
  <path d="M40-20l18 6-18 6z" class="corald o"/>
  <path d="M-8-16q30-20 46 4-28 22-46-4z" class="goldd o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M400 240q40-80 60-100"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
