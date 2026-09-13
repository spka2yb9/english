# -*- coding: utf-8 -*-
"""第142回。in-/im- の形容詞。否定接頭辞は「できない側」に実線の丸を置く。"""
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


# --- 名詞 -------------------------------------------------------------------
add('in-laws', '結婚してできた、配偶者側の親族', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g fill="none" stroke="{BRN}" stroke-width="4">
  <path d="M150 130h300M150 130v40M450 130v40M150 250v40M450 250v40M100 290h100M400 290h100M100 290v30M200 290v30M400 290v30M500 290v30"/>
</g>
{head(150, 200, 24, 'teal', 'short')}
{head(450, 200, 24, 'coral', 'bun')}
{head(100, 350, 20, 'blue', 'cap')}
{head(200, 350, 20, 'green', 'bob')}
{head(400, 350, 20, 'violet', 'short')}
{head(500, 350, 20, 'gold', 'bun')}
<g fill="{TONES['coral'][0]}">
  <path d="M300 118q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10">
  <path d="M356 100h230v300H356z"/>
</g>''', ground=False)

add('intern', '研修生として職場で経験を積む', f'''
{table(380)}
<g transform="translate(300 280)">
  <path d="M-220-20h440v22h-440z" fill="#c9a464" class="o"/>
</g>
{sit(200, 380, 0.95, 1, 'coral', 'blue', 'bob', 'smile', 'lap')}
{chair(200, 380, 0.9, 'gold', 1)}
{person(410, 380, 1.0, -1, 'teal', 'violet', 'point', 'short', 'smile')}
<g transform="translate(290 220)">
  <path d="M-56-40h112v70h-112z" fill="#3b4450" class="o"/>
  <path d="M-48-32h96v54h-96z" fill="#dceaf4"/>
</g>
<g transform="translate(180 210)">
  <path d="M-34-22h68v44h-34l-34-10z" fill="#fffefd" class="o"/>
  <rect x="-24" y="-8" width="40" height="8" rx="4" fill="{TONES['coral'][0]}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M340 150h-90"/></g>''', ground=False)

add('intersection', '二本の道が交わる十字路', f'''
<path d="M0 0h600v400H0z" fill="#dfe8d8"/>
<path d="M0 160h600v90H0z" fill="#6f7b88" class="o"/>
<path d="M240 0h120v400H240z" fill="#6f7b88" class="o"/>
<g fill="none" stroke="#fffefd" stroke-width="5" stroke-dasharray="26 22">
  <path d="M0 205h230M370 205h230M300 0v150M300 260v140"/>
</g>
<g fill="#fffefd">
''' + ''.join(f'<rect x="{250+i*22}" y="130" width="12" height="26"/>' for i in range(5)) + f'''
''' + ''.join(f'<rect x="{250+i*22}" y="252" width="12" height="26"/>' for i in range(5)) + f'''
</g>
<g transform="translate(120 200) scale(0.5)">
  <path d="M-120 40h240v-56q0-20-20-20h-70l-40-40h-70q-20 0-20 20v96z" class="coral o"/>
  <circle cx="-70" cy="40" r="26" fill="{INK}"/><circle cx="70" cy="40" r="26" fill="{INK}"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M470 100l-120 80"/></g>''', ground=False)

# --- 否定接頭辞の形容詞 ---------------------------------------------------------
add('ignorant', '知っているはずのことを知らない', f'''
{split()}
{table(380)}
{person(150, 380, 1.1, 1, 'blue', 'blue', 'up', 'short', 'neutral')}
<g transform="translate(150 190)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-18-18q0-16 18-16t18 16-18 14v8" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="16" r="4.5" fill="{INK}"/>
</g>
{person(450, 380, 1.1, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
<g transform="translate(450 190)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M0-16q18 0 18 16t-10 16v6h-16v-6q-10 0-10-16t18-16z" class="gold"/>
</g>
<circle cx="150" cy="290" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="450" cy="290" r="120"/></g>''', ground=False)

add('illegible', '字がくずれていて読み取れない', f'''
{split()}
{table(380)}
<g transform="translate(150 220)">
  {doc(0, 0, 180, 220, 0)}
  <g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M-64 {-70+i*36}q14 20 0 12t18-6 8 10 16-18 10 16 18-4"/>' for i in range(5)) + f'''
  </g>
</g>
<g transform="translate(450 220)">
  {doc(0, 0, 180, 220, 5)}
</g>
<circle cx="150" cy="220" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="450" cy="220" r="130"/></g>''', ground=False)

add('illustrative', 'ことばの説明に、一枚の図を添えて示す', f'''
{table(380)}
<g transform="translate(180 220)">
  {doc(0, 0, 170, 210, 5)}
</g>
<g transform="translate(430 220)">
  <path d="M-110-90h220v180h-220z" class="paper"/>
  <circle cx="-40" cy="-30" r="30" class="goldp o"/>
  <path d="M-88 60L-24-20l30 34 40-50 60 96z" class="greenp o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M280 220h50"/></g>
<circle cx="430" cy="220" r="140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('illustrious', '長い功績で名を知られた、輝かしい経歴', f'''
{table(380)}
{person(300, 380, 1.2, 1, 'violet', 'gold', 'stand', 'bun', 'smile')}
<g>
''' + ''.join(f'''<g transform="translate({120+i*120} 160)">
  <path d="M-30-24h60v14h-60z" class="gold o"/>
  <path d="M-30-24l-8-42 22 18 16-28 16 28 22-18-8 42z" class="gold o"/>
</g>''' for i in range(2)) + f'''
''' + ''.join(f'''<g transform="translate({380+i*110} 160)">
  <circle r="26" class="gold o"/>
  <path d="M0-14l7 14 15 2-11 12 3 16-14-8-14 8 3-16-11-12 15-2z" class="goldd"/>
</g>''' for i in range(2)) + f'''
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{300+150*math.cos(3.5+i*0.45):.0f} {260+150*math.sin(3.5+i*0.45):.0f}l{20*math.cos(3.5+i*0.45):.0f} {20*math.sin(3.5+i*0.45):.0f}"/>' for i in range(8)) + f'''
</g>''', ground=False)

add('imaginable', '思いつくかぎりの色がすべてそろっている', f'''
{table(380)}
<g class="o">
''' + ''.join(f'<rect x="{60+ (i%8)*60}" y="{200+(i//8)*80}" width="50" height="70" fill="{[TONES["coral"][0], TONES["teal"][0], TONES["gold"][0], TONES["violet"][0], TONES["green"][0], TONES["blue"][0], TONES["coral"][1], TONES["teal"][1], TONES["gold"][1], TONES["violet"][1], TONES["green"][1], TONES["blue"][1], TONES["coral"][2], TONES["teal"][2], TONES["gold"][2], TONES["violet"][2]][i]}"/>' for i in range(16)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M60 140h480"/></g>
<g class="a" marker-end="url(#ar)"><path d="M540 140H60"/></g>''', arrow=True, ground=False)

add('immaculate', 'ちりひとつなく磨き上げられた部屋', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-110-120h220v240h-220z" fill="#f0eee6" class="o"/>
  <path d="M-110 70h220v50h-220z" fill="#c9a464" class="o"/>
''' + ''.join(f'<g transform="translate({-70+ (i%3)*70} {30+(i//3)*0}) rotate({-30+i*22})">{doc(0, 0, 44, 54, 1)}</g>' for i in range(3)) + f'''
  <g fill="{MUTED}"><circle cx="60" cy="50" r="8"/><circle cx="-80" cy="56" r="6"/></g>
</g>
<g transform="translate(450 250)">
  <path d="M-110-120h220v240h-220z" fill="#fffefd" class="o"/>
  <path d="M-110 70h220v50h-220z" fill="#d9b877" class="o"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
    <path d="M60-80l24-20M80-30h26M40 30l24 22"/>
  </g>
</g>
<circle cx="450" cy="250" r="140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('immersive', '画面に囲まれて、その中にいるように感じる', f'''
<path d="M0 0h600v400H0z" fill="#1e2338"/>
<g transform="translate(300 210)">
  <path d="M-280-160h560v320h-560z" fill="#2f4a6a" class="o"/>
  <path d="M-280 40q140-60 280 0t280-20v140h-560z" fill="#1f3a52"/>
  {sun(180, -90, 30)}
  <g fill="none" stroke="#4d7fa4" stroke-width="5"><path d="M-240 90h200M60 130h200"/></g>
</g>
{person(300, 380, 1.05, 1, 'coral', 'blue', 'up', 'bun', 'smile')}
<g transform="translate(300 250)">
  <path d="M-56-20h112v40h-112z" fill="#3b4450" class="o"/>
  <path d="M-56-14h112v10h-112z" fill="#5a6270"/>
  <path d="M-56-6h-16v14h16zM56-6h16v14H56z" fill="#3b4450" class="o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M180 200l-26-20M420 196l26-20"/>
</g>''', ground=False)

add('impartial', 'どちらの側にも寄らず、まん中で見る', f'''
{table(380)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M300 60v320"/></g>
{person(120, 380, 1.0, 1, 'blue', 'blue', 'point', 'short', 'neutral')}
{person(480, 380, 1.0, -1, 'coral', 'blue', 'point', 'bun', 'neutral')}
{person(300, 380, 1.05, 1, 'teal', 'gold', 'up', 'cap', 'neutral')}
<g transform="translate(300 170)">
  <path d="M-10 0h20v60h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-100-8h200v16h-200z" fill="#b8bfc8" class="o"/>
  <circle r="12" fill="#8f9aa6" class="o"/>
  <g class="tealp o"><path d="M-130 8q0 22 30 22t30-22z"/><ellipse cx="-100" ry="8" rx="30"/></g>
  <g class="coralp o"><path d="M70 8q0 22 30 22t30-22z"/><ellipse cx="100" ry="8" rx="30"/></g>
</g>
<circle cx="300" cy="250" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('impeccable', '一分のすきもなく整った身なり', f'''
{split()}
{table(380)}
{person(150, 380, 1.15, 1, 'blue', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(150 260) rotate(-14)">
  <path d="M-8-40h16v70h-16z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M104 300q46 14 92 0"/></g>
{person(450, 380, 1.15, 1, 'violet', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(450 260)">
  <path d="M-8-40h16v70h-16z" class="coral o"/>
  <path d="M-16-44h32v10h-32z" class="corald o"/>
</g>
<g fill="none" stroke="{TONES['violet'][2]}" stroke-width="3"><path d="M404 300h92"/></g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M540 230l-24-18M550 290h-26"/>
</g>
<circle cx="450" cy="290" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('impenetrable', 'すきまのない壁で、どうしても通り抜けられない', f'''
{table(380)}
<g transform="translate(360 220)">
  <path d="M-40-180h80v340h-80z" fill="#8f9aa6" class="o"/>
  <g fill="none" stroke="#6f7b88" stroke-width="4">
''' + ''.join(f'<path d="M-40 {-150+i*50}h80"/>' for i in range(7)) + f'''
  </g>
</g>
{person(160, 380, 1.05, 1, 'coral', 'blue', 'reach', 'cap', 'sad')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M230 220h80"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M300 160l-24-24M300 280l-24 24"/>
</g>
<circle cx="360" cy="220" r="0" fill="none"/>
{cross(500, 130, 0.7)}''', ground=False)

add('impersonal', '名前も呼ばれず、番号で扱われる', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'teal', 'teal', 'give', 'bun', 'smile')}
<g transform="translate(150 200)">
  <path d="M-56-36h112q12 0 12 12v36q0 12-12 12h-72l-20 16v-16q-18 0-18-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, -4, 3, 26, INK)}
</g>
{person(450, 380, 1.05, 1, 'blue', 'blue', 'stand', 'short', 'neutral')}
<g transform="translate(450 200)">
  <path d="M-56-36h112q12 0 12 12v36q0 12-12 12h-72l-20 16v-16q-18 0-18-12v-36q0-12 12-12z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-30" y="-13" width="26" height="26" rx="5"/><rect x="4" y="-13" width="26" height="26" rx="5"/></g>
</g>
<circle cx="450" cy="290" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('implicit', '口には出さないが、うなずきで伝わる了解', f'''
{table(380)}
{person(180, 380, 1.1, 1, 'teal', 'blue', 'stand', 'bun', 'smile')}
{person(430, 380, 1.1, -1, 'coral', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(305 190)">
  <path d="M-70-40h140q12 0 12 12v40q0 12-12 12h-96l-22 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o" opacity="0.5"/>
  {tick(0, -4, 0.4)}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6">
  <path d="M240 240h130"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}" stroke-width="4"><path d="M180 300v-40M430 300v-40"/></g>''', ground=False)

add('improbable', '当たる見込みがきわめて小さいくじ', f'''
{table(380)}
<g transform="translate(300 250)">
  <path d="M-140-70h280v140h-280z" fill="#e0d6c0" class="o"/>
  <g class="o">
''' + ''.join(f'<circle cx="{-110+ (i%9)*28}" cy="{-40+(i//9)*38}" r="12" fill="{MUTED}"/>' for i in range(27)) + f'''
  </g>
  <circle cx="-110" cy="-40" r="12" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M120 130l50 60"/></g>
<circle cx="190" cy="210" r="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 6"/>''', ground=False)

add('impulsive', '考える前に手が出て、その場で買ってしまう', f'''
{table(380)}
<g transform="translate(410 280)">
  <path d="M-70-40h140v80h-140z" class="goldp o"/>
  <path d="M-70-40l14-18h140l-14 18z" fill="{TONES['gold'][1]}" class="o"/>
  <path d="M40-70h50v26H40z" class="coral o"/>
</g>
{person(180, 380, 1.15, 1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M250 230h80"/></g>
<g transform="translate(150 170)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-18-18q0-16 18-16t18 16-18 14v8" fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round"/>
  {cross(0, 0, 0.28)}
</g>''', ground=False)

add('incessant', '止むことなく、ずっと鳴り続ける音', f'''
{table(380)}
<g transform="translate(180 260)">
  <circle r="60" fill="#fffdf6" class="o"/>
  <path d="M-42-42l-24-24M42-42l24-24" stroke="{INK}" stroke-width="10" stroke-linecap="round" fill="none"/>
  <circle cx="-42" cy="-52" r="16" class="coral o"/><circle cx="42" cy="-52" r="16" class="coral o"/>
  <path d="M0 0v-36M0 0l26 16" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{270+i*46} {200-i*16}q{30+i*8} {60+i*16} 0 {120+i*32}"/>' for i in range(5)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 130h420"/></g>''', arrow=True, ground=False)

add('inclusive', '誰も外に置かず、全員を輪の中に入れる', f'''
{split()}
{table(380)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><ellipse cx="140" cy="290" rx="110" ry="80"/></g>
{head(90, 260, 22, 'teal', 'short')}
{head(180, 260, 22, 'coral', 'bun')}
{head(140, 330, 22, 'gold', 'cap')}
<g opacity="0.5">{head(270, 190, 22, 'violet', 'bob')}</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"><ellipse cx="440" cy="290" rx="140" ry="90"/></g>
{head(370, 260, 22, 'teal', 'short')}
{head(450, 250, 22, 'coral', 'bun')}
{head(520, 270, 22, 'violet', 'bob')}
{head(400, 330, 22, 'gold', 'cap')}
{head(490, 335, 22, 'green', 'short')}
<circle cx="440" cy="290" r="0" fill="none"/>
{tick(440, 130, 0.6)}''', ground=False)

add('incoherent', '話の筋がつながらず、ばらばらのまま', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-90+ (i%3)*66}" y="{-60+(i//3)*54}" width="52" height="16" rx="8" transform="rotate({-26+i*12} {-64+(i%3)*66} {-52+(i//3)*54})"/>' for i in range(6)) + f'''
  </g>
</g>
<g transform="translate(450 240)">
  <g fill="{INK}">
''' + ''.join(f'<rect x="-90" y="{-70+i*32}" width="{180-(i%3)*40}" height="16" rx="8"/>' for i in range(5)) + f'''
  </g>
</g>
<circle cx="150" cy="240" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="450" cy="240" r="130"/></g>''', ground=False)

add('incomparable', 'ほかの何とも比べようがないほど抜きん出ている', f'''
<path d="M0 0h600v400H0z" fill="#f0eee6"/>
<g transform="translate(300 320)">
  <path d="M-250 40h500v6h-500z" fill="{INK}"/>
  <g class="tealp o">
''' + ''.join(f'<rect x="{-230+i*54}" y="{-30-(i%3)*14}" width="40" height="{30+(i%3)*14}"/>' for i in range(7)) + f'''
  </g>
  <rect x="160" y="-260" width="60" height="260" class="coral o"/>
</g>
<circle cx="490" cy="200" r="80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M300 100h100"/></g>''', ground=False)

add('inconceivable', '頭では思い描くことすらできない', f'''
{table(380)}
{person(150, 380, 1.1, 1, 'teal', 'blue', 'think', 'bun', 'sad')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><ellipse cx="400" cy="200" rx="160" ry="120"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3">
  <circle cx="250" cy="290" r="12"/><circle cx="290" cy="255" r="16"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round">
  <path d="M320 130l160 140M480 130L320 270"/>
</g>''', ground=False)

add('inconsiderate', '後ろの人を見ずにドアを放して閉めてしまう', f'''
{table(380)}
<g transform="translate(340 200)">
  <path d="M-100-160h200v320h-200z" fill="{BRN}" class="o"/>
  <path d="M-78-136h156v272h-156z" fill="#a0764a"/>
  <path d="M-78-136h156v272h-156z" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
{person(180, 380, 1.0, 1, 'violet', 'blue', 'walk', 'short', 'neutral', 'walk')}
{person(500, 380, 1.0, -1, 'coral', 'blue', 'up', 'bun', 'sad')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M470 150h-90"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M560 240l24-18M566 300h-26"/>
</g>
{cross(100, 160, 0.6)}''', ground=False)

add('incurable', 'どんな薬でも治せない', f'''
{table(380)}
{sit(300, 380, 1.15, 1, 'blue', 'blue', 'bob', 'sad', 'down')}
{chair(300, 380, 1.05, 'gold', 1)}
<g>
''' + ''.join(f'''<g transform="translate({120+i*130} 160)">
  <path d="M-30-40h60v70q0 12-30 12t-30-12z" fill="#e8f0f6" class="o"/>
  <path d="M-14-40v-12h28v12z" class="coral o"/>
  <path d="M-24-14h48v34q0 8-24 8t-24-8z" fill="{TONES['coral'][1]}"/>
  {cross(0, 0, 0.36)}
</g>''' for i in range(4)) + f'''
</g>''', ground=False)

add('indefensible', 'どの証拠を見ても言い訳のしようがない', f'''
{table(380)}
{person(180, 380, 1.1, 1, 'blue', 'blue', 'up', 'short', 'sad')}
<g>
''' + ''.join(f'<g transform="translate({350+ (i%2)*120} {170+(i//2)*120})">{doc(0, 0, 110, 120, 3)}{cross(30, 34, 0.3)}</g>' for i in range(4)) + f'''
</g>
<g transform="translate(180 190)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}" opacity="0.6"><rect x="-24" y="-6" width="48" height="12" rx="6"/></g>
</g>
{cross(180, 300, 0.6)}''', ground=False)

add('indispensable', 'これがないと機械が動かない、欠かせない部品', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90-70h180v140h-180z" fill="#8f9aa6" class="o"/>
  <circle cy="-10" r="40" fill="#c8d0d8" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-6" y="-58" width="12" height="18" rx="6" transform="rotate({i*45} 0 -10)"/>' for i in range(8)) + f'''
  </g>
  <path d="M-56 40h112v20h-112z" fill="#6f7b88"/>
</g>
{tick(150, 130, 0.6)}
<g transform="translate(450 250)">
  <path d="M-90-70h180v140h-180z" fill="#8f9aa6" class="o"/>
  <circle cy="-10" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
  <path d="M-56 40h112v20h-112z" fill="#6f7b88"/>
</g>
{cross(450, 130, 0.6)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M540 250l-60-40"/></g>''', ground=False)

add('inductive', '多くの例を集めて、一つの決まりを導く', f'''
{table(380)}
<g>
''' + ''.join(f'''<g transform="translate({100+i*100} 300)">
  <path d="M-40-40h80v80h-80z" class="coralp o"/>
  {word(0, 0, 2, 26, TONES['coral'][2])}
</g>''' for i in range(5)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke-width="6">
''' + ''.join(f'<path d="M{100+i*100} 250L{300 - (2-i)*10} 190"/>' for i in range(5)) + f'''
</g>
<g transform="translate(300 130)">
  <path d="M-180-50h360v90h-360z" class="tealp o"/>
  {word(0, -6, 6, 40, TONES['teal'][2])}
</g>''', arrow=True, ground=False)

add('industrious', '手を止めず、こつこつ働き続ける', f'''
{table(380)}
<g transform="translate(300 300)">
  <path d="M-240-20h480v22h-480z" fill="#c9a464" class="o"/>
</g>
''' + ''.join(f'{sit(120+i*120, 380, 0.9, 1, ["teal","coral","gold","violet"][i], "blue", ["short","bob","bun","cap"][i], "neutral", "lap")}' for i in range(4)) + f'''
<g>
''' + ''.join(f'<g transform="translate({140+i*120} 250)">{doc(0, 0, 80, 60, 2)}</g>' for i in range(4)) + f'''
</g>
<g transform="translate(520 160)">
  <circle r="44" fill="#fffdf6" class="o"/>
  <path d="M0 0v-28M0 0l20 12" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M80 150h380"/></g>''', ground=False)

add('inexcusable', '一度ならず何度も繰り返され、許す余地がない', f'''
{table(380)}
<g>
''' + ''.join(f'''<g transform="translate({140+i*110} 250)">
  {doc(0, 0, 90, 110, 2)}
  {cross(0, 26, 0.3)}
</g>''' for i in range(4)) + f'''
</g>
{person(530, 380, 0.85, -1, 'violet', 'blue', 'point', 'bun', 'sad')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M100 130h380"/></g>
{cross(300, 130, 0.0) if False else ''}''', ground=False)

add('inferior', '同じ用途でも、明らかに質の落ちる品', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-80-60h160v120h-160z" fill="#b8ac94" class="o"/>
  <path d="M-60-30l40 40M-20-30l-40 40" stroke="{TONES['coral'][0]}" stroke-width="4" fill="none"/>
  <path d="M20 10q30-20 50 4" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g transform="translate(450 260)">
  <path d="M-80-60h160v120h-160z" class="teal o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-60-20h120M-60 20h120"/></g>
</g>
<circle cx="150" cy="260" r="120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M300 130v40"/></g>''', ground=False)

add('infinite', '端のない線が両側どこまでも続く', f'''
{table(380)}
<g transform="translate(300 240)">
  <path d="M-280 0h560" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round" fill="none"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" stroke-linecap="round">
    <path d="M-60 0q0-40 26-40t26 40 26 40 26-40-26-40-26 40-26 40-26-40z" transform="translate(8 -100) scale(1.4)"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}" stroke-width="5"><path d="M300 320h250"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}" stroke-width="5"><path d="M300 320H50"/></g>''', ground=False)

add('inflammatory', 'あおる言葉が火をつけて騒ぎを大きくする', f'''
{table(380)}
{person(140, 380, 1.05, 1, 'violet', 'blue', 'up', 'cap', 'neutral')}
<g transform="translate(270 170)">
  <path d="M-70-40l14 14-14 14 14 14-14 14h140l-14-14 14-14-14-14 14-14z" fill="#fffefd" class="o"/>
  <g fill="{TONES['coral'][0]}"><rect x="-40" y="-9" width="80" height="18" rx="9"/></g>
</g>
{flame(400, 320, 0.9)}
''' + ''.join(person(470+i*60, 380, 0.75, 1, ['coral','gold'][i%2], 'blue', 'up', ['cap','bob'][i%2], 'sad') for i in range(2)) + f'''
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M350 230q40 30 40 60"/></g>''', ground=False)

add('ingenious', 'ありあわせの物で、うまい仕掛けを考え出す', f'''
{table(340)}
<g transform="translate(300 250)">
  <circle cx="-100" r="44" fill="#8f9aa6" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-106" y="-54" width="12" height="18" rx="6" transform="rotate({i*45} -100 0)"/>' for i in range(8)) + f'''
  </g>
  <path d="M-56 0h30v10h-30z" fill="#c9a464" class="o"/>
  <circle cx="20" r="32" fill="#c8d0d8" class="o"/>
  <path d="M52-8h60v16H52z" fill="#c9a464" class="o"/>
  <path d="M112-24h40v48h-40z" class="coral o"/>
  <path d="M-100-44v-40" stroke="{BRN}" stroke-width="8" fill="none"/>
  <circle cx="-100" cy="-96" r="18" class="gold o"/>
</g>
{person(110, 340, 0.9, 1, 'teal', 'blue', 'point', 'bun', 'smile')}
<g transform="translate(130 180)">
  <path d="M-30-26h60q10 0 10 10v28q0 10-10 10h-40l-16 14v-14q-14 0-14-10v-28q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M0-18q20 0 20 18t-10 16v8h-20v-8q-10 0-10-16t20-18z" class="gold"/>
</g>''', ground=False)

add('innate', '教わらなくても、生まれつきできる', f'''
{split()}
{table(380)}
<g transform="translate(150 300)">
  <ellipse cy="-20" rx="34" ry="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cy="-56" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" transform="translate(0 52) scale(0.9)" fill="{HAIR}"/>
  <path d="M-34-24q-30-6-40 14" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
</g>
<g transform="translate(150 180)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.32)}
</g>
{person(450, 380, 0.95, 1, 'coral', 'blue', 'reach', 'bob', 'neutral')}
<g transform="translate(450 190)">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <g fill="{MUTED}"><rect x="-26" y="-6" width="52" height="12" rx="6"/></g>
</g>
<circle cx="150" cy="270" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('innocuous', '見た目はこわいが、実は害のない虫', f'''
{table(380)}
<g transform="translate(300 250)">
  <ellipse rx="90" ry="56" class="green o"/>
  <circle cx="80" cy="-30" r="34" class="green o"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="4" stroke-linecap="round">
    <path d="M100-58q30-40 60-40M110-46q40-24 70-10"/>
  </g>
  <circle cx="88" cy="-36" r="5" fill="{INK}"/>
  <g stroke="{TONES['green'][2]}" stroke-width="8" stroke-linecap="round" fill="none">
    <path d="M-50 50l-20 30M0 54l0 30M50 50l20 30"/>
  </g>
</g>
{person(510, 380, 0.85, -1, 'teal', 'blue', 'stand', 'bun', 'smile')}
{tick(500, 160, 0.6)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M440 250h-30"/></g>''', ground=False)

add('inquisitive', '次々に質問して知りたがる', f'''
{table(380)}
{person(200, 380, 1.1, 1, 'coral', 'blue', 'up', 'bob', 'smile')}
{person(470, 380, 1.0, -1, 'teal', 'blue', 'stand', 'short', 'neutral')}
<g>
''' + ''.join(f'''<g transform="translate({330+ (i%2)*36} {130+i*72})">
  <path d="M-40-30h80q10 0 10 10v30q0 10-10 10h-52l-18 14v-14q-10 0-10-10v-30q0-10 10-10z" fill="#fffefd" class="o"/>
  <path d="M-18-18q0-16 18-16t18 16-18 14v8" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="16" r="4.5" fill="{INK}"/>
</g>''' for i in range(3)) + f'''
</g>''', ground=False)

add('insightful', '表からは見えない中身まで見通した意見', f'''
{table(380)}
<g transform="translate(240 250)">
  <path d="M-110-90h220v180h-220z" fill="#c8d0d8" class="o"/>
  <path d="M-90-70h180v140h-180z" fill="#e8eef2"/>
  <g fill="{MUTED}" opacity="0.45"><circle cx="-40" cy="-20" r="26"/><rect x="10" y="0" width="60" height="50"/></g>
</g>
<g transform="translate(300 220)">
  <circle r="80" fill="#eef6fb" class="o" opacity="0.9"/>
  <g fill="{INK}"><circle cx="-30" cy="-16" r="22"/><rect x="10" y="4" width="50" height="42"/></g>
  <circle r="80" fill="none" stroke="#8f9aa6" stroke-width="11"/>
  <path d="M56 56l50 50" stroke="{INK}" stroke-width="15" stroke-linecap="round" fill="none"/>
</g>
{person(510, 380, 0.85, -1, 'violet', 'blue', 'point', 'bun', 'smile')}''', ground=False)

add('instinctive', '熱いものに触れて、考える前に手を引く', f'''
{table(380)}
{flame(400, 320, 0.7)}
{person(180, 380, 1.15, 1, 'coral', 'blue', 'up', 'short', 'surprised')}
<g>
  <path d="M250 240q40-30 80-10" stroke="{SKINL}" stroke-width="26" stroke-linecap="round" fill="none"/>
  <path d="M250 240q40-30 80-10" stroke="{SKIN}" stroke-width="21" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M330 200h-90"/></g>
<g transform="translate(140 170)">
  <path d="M-36-26h72q10 0 10 10v26q0 10-10 10h-46l-16 14v-14q-18 0-18-10v-26q0-10 10-10z" fill="#fffefd" class="o"/>
  {cross(0, -2, 0.3)}
</g>''', ground=False)

add('instructive', '読むと新しいことが分かって、ためになる本', f'''
{table(380)}
{sit(190, 380, 1.1, 1, 'coral', 'blue', 'bun', 'smile', 'lap')}
{chair(190, 380, 1.0, 'gold', 1)}
<g transform="translate(240 260) rotate(-10)">
  <path d="M-70-50h140v100h-140z" fill="#fffefd" class="o"/>
  <path d="M0-50v100" stroke="{INK}" stroke-width="3" fill="none"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="{-58+ (i%2)*62}" y="{-34+(i//2)*22}" width="46" height="7" rx="3.5"/>' for i in range(6)) + f'''
  </g>
</g>
<g transform="translate(430 200)">
  <circle r="46" class="goldp o"/>
  <path d="M0-24q26 0 26 24t-14 24v10h-24v-10q-14 0-14-24t26-24z" class="gold"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{62*math.cos(i*0.785):.0f} {62*math.sin(i*0.785):.0f}l{18*math.cos(i*0.785):.0f} {18*math.sin(i*0.785):.0f}"/>' for i in range(8)) + f'''
  </g>
</g>''', ground=False)

add('intentional', 'うっかりではなく、ねらってそうする', f'''
{split()}
{table(380)}
{person(150, 380, 1.05, 1, 'blue', 'blue', 'reach', 'short', 'surprised')}
<g transform="translate(230 300) rotate(-70)">
  <path d="M-30-40h60l-8 70q-2 12-22 12t-22-12z" fill="#e8f0f6" class="o"/>
</g>
{cross(150, 140, 0.6)}
{person(450, 380, 1.05, 1, 'violet', 'blue', 'reach', 'short', 'neutral')}
<g transform="translate(530 300) rotate(-70)">
  <path d="M-30-40h60l-8 70q-2 12-22 12t-22-12z" fill="#e8f0f6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M470 240l50 30"/></g>
<circle cx="450" cy="290" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('intermittent', '降ったり止んだりを繰り返す雨', f'''
<path d="M0 0h600v400H0z" fill="#c8d2da"/>
{table(380)}
<g>
{cloud(120, 100, 1.0, 'blue')}
{cloud(320, 100, 1.0, 'blue')}
{cloud(500, 100, 1.0, 'blue')}
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{80+i*30} {170+(i%3)*34}l-12 34"/>' for i in range(4)) + f'''
''' + ''.join(f'<path d="M{460+i*30} {170+(i%3)*34}l-12 34"/>' for i in range(4)) + f'''
</g>
{sun(320, 190, 30)}
<g class="a" marker-end="url(#ar)"><path d="M60 330h480"/></g>''', arrow=True, ground=False)

add('intricate', '細い線が入り組んだ、精巧な模様', f'''
{table(380)}
<g transform="translate(300 220)">
  <circle r="150" fill="#f6ecd4" class="o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3">
''' + ''.join(f'<circle r="{30+i*24}"/>' for i in range(5)) + f'''
''' + ''.join(f'<path d="M0 0l{140*math.cos(i*0.392):.0f} {140*math.sin(i*0.392):.0f}"/>' for i in range(16)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="2.5">
''' + ''.join(f'<circle cx="{86*math.cos(i*0.785):.0f}" cy="{86*math.sin(i*0.785):.0f}" r="26"/>' for i in range(8)) + f'''
  </g>
  <circle r="16" class="gold o"/>
</g>''', ground=False)

add('intrusive', '断りもなく人の作業に割り込んでくる', f'''
{table(380)}
{sit(200, 380, 1.1, 1, 'teal', 'blue', 'bun', 'sad', 'lap')}
{chair(200, 380, 1.0, 'gold', 1)}
<g transform="translate(250 270)">{doc(0, 0, 110, 90, 3)}</g>
{person(470, 380, 1.1, -1, 'violet', 'blue', 'reach', 'short', 'neutral')}
<g>
  <path d="M400 250q-50-10-90 14" stroke="{SKINL}" stroke-width="26" stroke-linecap="round" fill="none"/>
  <path d="M400 250q-50-10-90 14" stroke="{SKIN}" stroke-width="21" stroke-linecap="round" fill="none"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M430 180H310"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M150 240q-14 10-14 26"/>
</g>''', ground=False)

add('intuitive', '説明書を読まなくても、押す所がすぐ分かる', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90-90h180v180h-180z" fill="#c8d0d8" class="o"/>
  <g fill="#8f9aa6">
''' + ''.join(f'<rect x="{-70+ (i%4)*38}" y="{-70+(i//4)*38}" width="28" height="28" rx="4"/>' for i in range(16)) + f'''
  </g>
</g>
<g transform="translate(150 130)">
  <path d="M-18-30q0-24 18-24t18 24-18 20v12" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <circle cy="26" r="5.5" fill="{INK}"/>
</g>
<g transform="translate(450 250)">
  <path d="M-90-90h180v180h-180z" fill="#e8f0f6" class="o"/>
  <circle cy="-10" r="52" class="green o"/>
  <path d="M-24-10l16 20 34-40" fill="none" stroke="#fffefd" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
</g>
{hand(450, 380, 1)}
<circle cx="450" cy="250" r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>''', ground=False)

add('invaluable', '値段のつけようがないほど、非常に貴重な', f'''
{table(380)}
<g transform="translate(300 240)">
  <path d="M-70 0l30-60h80l30 60-70 80z" class="tealp o"/>
  <path d="M-40-60l20 60h100l20-60M-70 0h140" fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
''' + ''.join(f'<path d="M{300+140*math.cos(3.4+i*0.44):.0f} {250+140*math.sin(3.4+i*0.44):.0f}l{20*math.cos(3.4+i*0.44):.0f} {20*math.sin(3.4+i*0.44):.0f}"/>' for i in range(8)) + f'''
</g>
<g transform="translate(480 330) rotate(-14)">
  <path d="M-60-30h110l30 30-30 30H-60z" fill="#fffdf6" class="o"/>
  <circle cx="40" r="9" fill="none" stroke="{INK}" stroke-width="3"/>
  {cross(-20, 0, 0.34)}
</g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
