# -*- coding: utf-8 -*-
"""第132回。re- の動詞。「一度目 → 二度目」を split() の左右に置く。"""
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


# --- re- の動詞 ---------------------------------------------------------------
add('reassemble', 'ばらばらの部品を組み立て直してもとの形にする', f'''
{split()}
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({80+ (i%3)*66} {200+(i//3)*80}) rotate({-24+i*14})"><path d="M-26-20h52v40h-52z" class="tealp o"/></g>' for i in range(6)) + f'''
</g>
<g transform="translate(450 250)">
  <path d="M-90-70h180v140h-180z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="3"><path d="M-30-70v140M30-70v140M-90 0h180"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('reassess', '一度出した点数をもう一度つけ直す', f'''
{split()}
{table(380)}
<g transform="translate(150 220)">
  {doc(0, 0, 170, 210, 4)}
  <circle cx="46" cy="66" r="28" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
<g transform="translate(450 220)">
  {doc(0, 0, 170, 210, 4)}
  <circle cx="46" cy="66" r="28" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 6"/>
  <circle cx="-30" cy="66" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g transform="translate(520 320) rotate(30)">
  <path d="M0-70l10 22v60h-20V-48z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 220h60"/></g>''', arrow=True, ground=False)

add('recapture', '逃げた鳥をもう一度つかまえてかごに戻す', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-70 60h140v20h-140z" fill="#8f9aa6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="5">
''' + ''.join(f'<path d="M{-64+i*26} -60v120"/>' for i in [0,1,2,5,6]) + f'''
    <path d="M-70-60h140"/>
  </g>
</g>
<g transform="translate(200 150)">
  <ellipse rx="30" ry="22" class="gold o"/>
  <circle cx="24" cy="-14" r="15" class="gold o"/>
  <path d="M36-18l16 6-16 6z" class="corald o"/>
</g>
<g transform="translate(450 260)">
  <path d="M-70 60h140v20h-140z" fill="#8f9aa6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="5">
''' + ''.join(f'<path d="M{-64+i*26} -60v120"/>' for i in range(6)) + f'''
    <path d="M-70-60h140"/>
  </g>
  <g transform="translate(0 20)">
    <ellipse rx="30" ry="22" class="gold o"/>
    <circle cx="24" cy="-14" r="15" class="gold o"/>
    <path d="M36-18l16 6-16 6z" class="corald o"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('reconstruct', 'こわれた家を建て直してもとどおりにする', f'''
{split()}
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g transform="translate(150 300)">
  <path d="M-60 0v-70h50V0z" fill="#c8b8a0" class="o"/>
  <path d="M-10 0v-40h40V0z" fill="#c8b8a0" class="o"/>
  <g fill="#a89880"><path d="M40 0l30-20 10 20zM-90 0l24-16 6 16z"/></g>
</g>
<g transform="translate(450 300)">
  <path d="M-60 0v-90h120V0z" fill="#fffdf6" class="o"/>
  <path d="M-72-90L0-140l72 50z" class="coral o"/>
  <path d="M-40-70h34v30h-34z" class="bluep o"/>
  <path d="M10-40h30V0H10z" class="corald o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('redefine', '言葉の意味の枠を引き直して新しくする', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <path d="M-100-70h200v140h-200z" fill="none" stroke="{INK}" stroke-width="5"/>
  <circle cx="-40" cy="-20" r="24" class="tealp o"/>
  <circle cx="34" cy="10" r="28" class="goldp o"/>
</g>
<g transform="translate(450 230)">
  <path d="M-100-70h200v140h-200z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
  <path d="M-70-100h200v170h-200z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
  <circle cx="-40" cy="-20" r="24" class="tealp o"/>
  <circle cx="34" cy="10" r="28" class="goldp o"/>
  <circle cx="80" cy="-64" r="22" class="violetp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 230h60"/></g>''', arrow=True, ground=False)

add('rediscover', '忘れていた古い写真を再び見つけ出す', f'''
{table(380)}
<g transform="translate(200 300)">
  <path d="M-110-40h220v100h-220z" fill="#c9a464" class="o"/>
  <path d="M-110-40l24-30h220l-24 30z" fill="#d9b877" class="o"/>
  <g fill="{MUTED}" opacity="0.4">
''' + ''.join(f'<circle cx="{-70+i*40}" cy="{-60+(i%3)*8}" r="9"/>' for i in range(5)) + f'''
  </g>
</g>
<g transform="translate(330 180) rotate(-14)">
  <path d="M-70-56h140v112h-140z" fill="#fffdf6" class="o"/>
  <path d="M-56-42h112v76h-112z" class="tealp o"/>
  {sun(30, -18, 12)}
  <path d="M-50 34L-14-6l24 22 22-30 34 48z" class="greenp o"/>
</g>
{person(500, 380, 1.0, -1, 'coral', 'blue', 'reach', 'bun', 'smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M420 110l24-20M446 170h26"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 210q40-40 60-40"/></g>''', arrow=True, ground=False)

add('redistribute', '偏っていた分を配り直して均す', f'''
{split()}
{table(380)}
<g>
''' + ''.join(coin(90+ (i%3)*36, 300-(i//3)*36, 16) for i in range(9)) + f'''
  {coin(230, 300, 16)}
</g>
<g>
''' + ''.join(coin(360+i*54, 300, 16) for i in range(4)) + f'''
''' + ''.join(coin(360+i*54, 264, 16) for i in range(2)) + f'''
</g>
{head(90, 350, 16, 'teal', 'short')}
{head(230, 350, 16, 'coral', 'bob')}
{head(360, 350, 16, 'teal', 'short')}
{head(414, 350, 16, 'coral', 'bob')}
{head(468, 350, 16, 'gold', 'bun')}
{head(522, 350, 16, 'violet', 'cap')}
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('refuel', '空になった機体に燃料を入れ直す', f'''
{table(380)}
{plane(340, 200, 0.85, 0, 'teal')}
<g transform="translate(160 320)">
  <path d="M-70-60h140v130h-140z" fill="#c8d0d8" class="o"/>
  <path d="M-56-46h112v50h-112z" fill="#2c333d" class="o"/>
  <g fill="{TONES['green'][0]}"><rect x="-40" y="-36" width="18" height="30"/><rect x="-16" y="-36" width="18" height="30"/></g>
  <path d="M70-20q40 0 40 30v40" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
<g transform="translate(280 280) rotate(-20)">
  <path d="M-30-14h50v28h-50z" class="coral o"/>
  <path d="M20-8h40v16H20z" fill="#8f9aa6" class="o"/>
</g>
<g transform="translate(470 130)">
  <circle r="46" fill="#fffdf6" class="o"/>
  <path d="M0 0l30-22" stroke="{TONES['green'][0]}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <circle r="6" fill="{INK}"/>
  <path d="M-34-34A46 46 0 0 1 34-34" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M470 200v-30"/></g>''', ground=False)

add('regroup', 'ばらけた隊列がもう一度集まって隊を組み直す', f'''
{split()}
{table(380)}
{head(70, 200, 20, 'teal', 'cap')}
{head(240, 160, 20, 'coral', 'short')}
{head(120, 330, 20, 'gold', 'bun')}
{head(230, 300, 20, 'green', 'cap')}
{head(160, 240, 20, 'violet', 'bob')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><ellipse cx="450" cy="270" rx="130" ry="90"/></g>
{head(370, 240, 20, 'teal', 'cap')}
{head(450, 230, 20, 'coral', 'short')}
{head(530, 240, 20, 'gold', 'bun')}
{head(410, 310, 20, 'green', 'cap')}
{head(490, 310, 20, 'violet', 'bob')}
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('rehabilitate', 'けがをした人が訓練で歩けるように戻る', f'''
{split()}
{table(380)}
{sit(150, 380, 1.05, 1, 'coral', 'blue', 'bob', 'sad', 'down')}
<g transform="translate(180 340)">
  <path d="M-30-16h70v32h-70z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-20-16v32M0-16v32M20-16v32"/></g>
</g>
{chair(150, 380, 1.0, 'gold', 1)}
{person(450, 380, 1.05, 1, 'coral', 'blue', 'walk', 'bob', 'smile', 'walk')}
<g fill="none" stroke="#8f9aa6" stroke-width="9">
  <path d="M370 250h180M370 250v130M550 250v130"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h60"/></g>''', arrow=True, ground=False)

add('reinstate', '外された人がもとの席に戻される', f'''
{split()}
{table(380)}
{chair(150, 380, 1.0, 'gold', 1)}
<g opacity="0.35">{person(260, 380, 0.85, -1, 'coral', 'blue', 'walk', 'bun', 'sad', 'walk')}</g>
{cross(150, 200, 0.7)}
{chair(450, 380, 1.0, 'gold', 1)}
{sit(450, 380, 1.05, 1, 'coral', 'blue', 'bun', 'smile', 'lap')}
{tick(450, 160, 0.7)}
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M270 280h60"/></g>''', ground=False)

add('reintroduce', 'いなくなった動物を森にもう一度放す', f'''
{split()}
<path d="M0 0h600v260H0z" fill="#dceaf4"/>
<path d="M0 260h600v140H0z" fill="#c9d8c0"/>
<path d="M0 260h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
''' + ''.join(tree(50+i*60, 300, 0.85) for i in range(4)) + f'''
''' + ''.join(tree(340+i*60, 300, 0.85) for i in range(4)) + f'''
<g transform="translate(480 330)">
  <ellipse rx="48" ry="30" fill="#a0764a" class="o"/>
  <circle cx="42" cy="-22" r="24" fill="#a0764a" class="o"/>
  <path d="M30-42q-8-32 6-32 12 6 8 32zM56-42q8-30 20-24 4 10-8 26z" fill="#a0764a" class="o"/>
  <circle cx="52" cy="-26" r="3.5" fill="{INK}"/>
  <g stroke="#8b6437" stroke-width="8" stroke-linecap="round" fill="none"><path d="M-20 28v14M18 28v14"/></g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M270 200h60"/></g>
{cross(150, 200, 0.6)}''', ground=False)

add('reiterate', '同じことを何度も繰り返して言う', f'''
{table(380)}
{person(140, 380, 1.1, 1, 'violet', 'blue', 'point', 'bun', 'neutral')}
<g>
''' + ''.join(f'''<g transform="translate({330+ (i%2)*30} {130+i*80})">
  <path d="M-90-34h180q12 0 12 12v34q0 12-12 12h-120l-22 16v-16q-10 0-10-12v-34q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(-10, -4, 5, 26, INK)}
</g>''' for i in range(3)) + f'''
</g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M540 190q40 40 0 76"/></g>
<g class="a" marker-end="url(#ar)" stroke="{MUTED}"><path d="M540 270q40 40 0 76"/></g>''', arrow=True, ground=False)

add('remarry', '一度別れた人が新しい相手と再び結婚する', f'''
{split()}
{table(380)}
{person(100, 380, 0.9, -1, 'teal', 'blue', 'walk', 'short', 'sad', 'walk')}
{person(220, 380, 0.9, 1, 'coral', 'violet', 'walk', 'bun', 'sad', 'walk')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M140 230l40 40M180 230l-40 40"/>
</g>
{person(410, 380, 0.9, 1, 'teal', 'blue', 'stand', 'short', 'smile')}
{person(500, 380, 0.9, -1, 'gold', 'gold', 'stand', 'bob', 'smile')}
<g fill="{TONES['coral'][0]}">
  <path d="M455 230q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5"><circle cx="455" cy="150" r="20"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 320h60"/></g>''', ground=False)

add('reorganise', '書類の並びを分類し直して組み直す', f'''
{split()}
{table(380)}
<g>
''' + ''.join(f'<g transform="translate({80+ (i%3)*70} {200+(i//3)*80}) rotate({-20+i*13})"><path d="M-30-38h60v76h-60z" fill="{["#dff4ef","#fde9e3","#fff0c5"][i%3]}" stroke="{INK}" stroke-width="2.5"/></g>' for i in range(6)) + f'''
</g>
<g>
''' + ''.join(f'<g transform="translate({360+i*70} {230})">' + ''.join(f'<path d="M-28 {-30+j*34}h56v30h-56z" fill="{["#dff4ef","#fde9e3","#fff0c5"][i]}" stroke="{INK}" stroke-width="2.5"/>' for j in range(2)) + '</g>' for i in range(3)) + f'''
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('rephrase', '同じ内容を別の言い方に置き換える', f'''
{split()}
{table(380)}
<g transform="translate(150 230)">
  <path d="M-110-50h220q14 0 14 14v60q0 14-14 14h-150l-26 20v-20q-14 0-14-14v-60q0-14 14-14z" fill="#fffefd" class="o"/>
  {word(0, -10, 6, 30, INK)}
  {word(-30, 24, 4, 30, INK)}
</g>
<g transform="translate(450 230)">
  <path d="M-110-50h220q14 0 14 14v60q0 14-14 14h-150l-26 20v-20q-14 0-14-14v-60q0-14 14-14z" fill="#fffefd" class="o"/>
  {word(-14, -10, 5, 30, TONES['teal'][0])}
  {word(-44, 24, 3, 30, TONES['teal'][0])}
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 230h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M150 330h300"/></g>
{tick(300, 350, 0.5)}''', arrow=True, ground=False)

add('replicate', '同じ実験をもう一度行って同じ結果を出す', f'''
{split()}
{table(380)}
<g transform="translate(150 260)">
  <path d="M-24-60h48l32 64q6 12-6 12h-96q-12 0-6-12z" fill="#e8f0f6" class="o"/>
  <path d="M-34 16h68l8 14q6 12-6 12h-72q-12 0-6-12z" class="teald"/>
</g>
<g transform="translate(150 150)">{doc(0, 0, 90, 90, 3)}</g>
<g transform="translate(450 260)">
  <path d="M-24-60h48l32 64q6 12-6 12h-96q-12 0-6-12z" fill="#e8f0f6" class="o"/>
  <path d="M-34 16h68l8 14q6 12-6 12h-72q-12 0-6-12z" class="teald"/>
</g>
<g transform="translate(450 150)">{doc(0, 0, 90, 90, 3)}</g>
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>
{tick(300, 130, 0.6)}''', arrow=True, ground=False)

add('reshape', '粘土のかたまりを別の形に作りかえる', f'''
{split()}
{table(340)}
<g transform="translate(150 260)">
  <path d="M-70-40h140v80h-140z" fill="#b08c6c" class="o"/>
</g>
<g transform="translate(450 250)">
  <path d="M-40 50h80v20h-80z" fill="#b08c6c" class="o"/>
  <path d="M-30-30h60v80h-60z" fill="#b08c6c" class="o"/>
  <path d="M-30-30q0-40 30-40t30 40z" fill="#b08c6c" class="o"/>
  <path d="M30 0q40 0 40 20t-40 20" fill="none" stroke="#b08c6c" stroke-width="12"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 260h60"/></g>
{hand(180, 150, 1)}''', arrow=True, ground=False)

add('retell', '聞いた話を自分の言葉で語り直す', f'''
{table(380)}
{person(130, 380, 1.0, 1, 'teal', 'blue', 'point', 'short', 'smile')}
{person(470, 380, 1.0, -1, 'coral', 'blue', 'point', 'bun', 'smile')}
<g transform="translate(230 160)">
  <path d="M-70-40h140q12 0 12 12v40q0 12-12 12h-96l-22 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  {word(0, 0, 5, 26, INK)}
</g>
<g transform="translate(380 260)">
  <path d="M70-40H-70q-12 0-12 12v40q0 12 12 12h96l22 16v-16q12 0 12-12v-40q0-12-12-12z" fill="#fffefd" class="o"/>
  {word(0, 0, 5, 26, TONES['teal'][0])}
</g>
<g class="a" marker-end="url(#ar)"><path d="M310 200q40 30 30 50"/></g>''', arrow=True, ground=False)

add('reunite', '長く離れていた家族が再び会う', f'''
{split()}
{table(380)}
{person(80, 380, 0.9, -1, 'teal', 'blue', 'stand', 'short', 'sad')}
{person(240, 380, 0.9, 1, 'coral', 'violet', 'stand', 'bun', 'sad')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 10"><path d="M160 100v280"/></g>
{person(420, 380, 0.9, 1, 'teal', 'blue', 'reach', 'short', 'smile')}
{person(500, 380, 0.9, -1, 'coral', 'violet', 'reach', 'bun', 'smile')}
<g fill="{TONES['coral'][0]}">
  <path d="M460 230q-14-20 0-28 14-6 18 10 4-16 18-10 14 8 0 28l-18 20z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 320h60"/></g>''', ground=False)

add('revisit', '前に行った場所をもう一度たずねる', f'''
{table(380)}
{building(400, 340, 0.9, 'coral')}
{person(140, 380, 1.0, 1, 'teal', 'blue', 'walk', 'cap', 'smile', 'walk')}
<g opacity="0.3">{person(230, 380, 0.9, 1, 'teal', 'blue', 'walk', 'cap', 'smile', 'walk')}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M60 350q140-40 260 0"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M200 240q90-70 160 20"/></g>
<g transform="translate(120 150)">
  <circle r="36" fill="#fffdf6" class="o"/>
  <path d="M0 0v-24M0 0l16 10" stroke="{INK}" stroke-width="4" stroke-linecap="round" fill="none"/>
</g>''', ground=False)

add('revoke', '一度出した免許証を取り消して回収する', f'''
{split()}
{table(380)}
<g transform="translate(150 240)">
  <path d="M-90-56h180v112h-180z" class="paper"/>
  <circle cx="-46" cy="-14" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2"/>
  <g fill="{MUTED}"><rect x="-10" y="-24" width="80" height="10" rx="5"/><rect x="-10" y="-4" width="60" height="10" rx="5"/></g>
  {tick(40, 30, 0.4)}
</g>
<g transform="translate(450 240)">
  <path d="M-90-56h180v112h-180z" class="paper"/>
  <circle cx="-46" cy="-14" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2"/>
  <g fill="{MUTED}"><rect x="-10" y="-24" width="80" height="10" rx="5"/><rect x="-10" y="-4" width="60" height="10" rx="5"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round">
    <path d="M-80-46l160 92M80-46l-160 92"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}"><path d="M270 240h60"/></g>''', arrow=True, ground=False)

add('recycling', '使い終わった瓶や缶を分けて再生に回す', f'''
{table(380)}
<g>
''' + ''.join(f'''<g transform="translate({130+i*120} 300)">
  <path d="M-50-70h100l-10 120q-2 16-40 16t-40-16z" fill="{[TONES['teal'][1], TONES['gold'][1], TONES['blue'][1]][i]}" class="o"/>
  <path d="M-50-70h100v-14h-100z" fill="{[TONES['teal'][0], TONES['gold'][0], TONES['blue'][0]][i]}" class="o"/>
</g>''' for i in range(3)) + f'''
</g>
<g transform="translate(470 220)">
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="14" stroke-linejoin="round">
    <path d="M0-60l52 90H-52z"/>
  </g>
  <g fill="{TONES['green'][0]}">
    <path d="M-52 30l-16 8 20 22z"/><path d="M52 30l16 8-20 22z"/><path d="M0-60l-14-14 28 0z"/>
  </g>
</g>
<g transform="translate(150 200)">
  <path d="M-24-40h48v70q0 12-24 12t-24-12z" fill="#e8f0f6" class="o"/>
</g>
<g transform="translate(270 190)">
  <path d="M-22-40h44v70q0 12-22 12t-22-12z" fill="#c8d0d8" class="o"/>
</g>''', ground=False)

# --- そのほかの動詞 -----------------------------------------------------------
add('quantify', 'ばくぜんとした量をはかって数で示す', f'''
{split()}
{table(380)}
<g transform="translate(150 250)">
  <path d="M-90 40q-30-60 10-90 50-36 110-14 60 22 60 66 0 40-80 46-80 6-100-8z" fill="{TONES['teal'][1]}" class="o"/>
</g>
<g transform="translate(450 250)">
  <path d="M-90 40q-30-60 10-90 50-36 110-14 60 22 60 66 0 40-80 46-80 6-100-8z" fill="{TONES['teal'][1]}" class="o"/>
  <path d="M-110 90h220v20h-220z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
''' + ''.join(f'<path d="M{-100+i*22} 90v{10 if i%2 else 18}"/>' for i in range(10)) + f'''
  </g>
</g>
<g transform="translate(450 130)">
  <path d="M-50-24h100v48h-100z" class="paper"/>
  {word(0, 0, 3, 26, INK)}
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('quicken', 'ゆっくりだった歩みが速くなる', f'''
{split()}
{table(380)}
{person(150, 380, 1.0, 1, 'blue', 'blue', 'stand', 'short', 'neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M90 250h30"/></g>
{person(430, 380, 1.05, 1, 'coral', 'blue', 'walk', 'cap', 'smile', 'walk')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M330 240h60M320 290h44M350 340h56"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M270 160h60"/></g>''', ground=False)

add('radiate', '熱源から熱と光が四方へ広がる', f'''
<path d="M0 0h600v400H0z" fill="#2c2a30"/>
<g transform="translate(300 200)">
  <circle r="60" class="gold o"/>
  <circle r="34" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="6" stroke-linecap="round">
''' + ''.join(f'<path d="M{78*math.cos(i*0.524):.0f} {78*math.sin(i*0.524):.0f}L{130*math.cos(i*0.524):.0f} {130*math.sin(i*0.524):.0f}"/>' for i in range(12)) + f'''
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round" opacity="0.7">
''' + ''.join(f'<path d="M{150*math.cos(i*0.524+0.26):.0f} {150*math.sin(i*0.524+0.26):.0f}L{190*math.cos(i*0.524+0.26):.0f} {190*math.sin(i*0.524+0.26):.0f}"/>' for i in range(12)) + f'''
  </g>
</g>
<g fill="none" stroke="{TONES['gold'][1]}" stroke-width="2" opacity="0.4">
  <circle cx="300" cy="200" r="150"/><circle cx="300" cy="200" r="190"/>
</g>''', ground=False)

add('ratify', '各国が署名して条約を正式に承認する', f'''
{table(380)}
<g transform="translate(300 200) rotate(-3)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <rect x="-110" y="-112" width="200" height="18" rx="9" fill="{INK}"/>
  <g fill="{MUTED}">
''' + ''.join(f'<rect x="-130" y="{-64+i*30}" width="{260-(i%3)*50}" height="10" rx="5"/>' for i in range(4)) + f'''
  </g>
  <g>
''' + ''.join(f'<path d="M{-120+i*90} 84q30-20 50 0t40-8" fill="none" stroke="{TONES["blue"][0]}" stroke-width="4"/>' for i in range(3)) + f'''
  </g>
  <circle cx="120" cy="96" r="26" class="coral o"/>
</g>
{head(100, 350, 20, 'teal', 'short')}
{head(300, 360, 20, 'coral', 'bun')}
{head(500, 350, 20, 'gold', 'cap')}''', ground=False)

add('reap', '実った麦を刈り取って収穫する', f'''
<path d="M0 0h600v230H0z" fill="#dceaf4"/>
<path d="M0 230h600v170H0z" fill="#e0d6b0"/>
<path d="M0 230h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
<g stroke="{TONES['gold'][2]}" stroke-width="4" fill="none">
''' + ''.join(f'<path d="M{330+i*26} 380v-90"/>' for i in range(11)) + f'''
</g>
<g class="gold o">
''' + ''.join(f'<ellipse cx="{330+i*26}" cy="278" rx="9" ry="22"/>' for i in range(11)) + f'''
</g>
{person(150, 380, 1.1, 1, 'coral', 'blue', 'reach', 'cap', 'smile')}
<g transform="translate(250 260) rotate(20)">
  <path d="M-10-70h20v90h-20z" fill="#c9a464" class="o"/>
  <path d="M10-70q60 0 80 60-70 6-80-60z" fill="#c8d0d8" class="o"/>
</g>
<g class="gold o">
  <path d="M60 340q40-20 70 0-30 20-70 0z"/>
</g>''', ground=False)

add('rebuke', '上司が部下を厳しくとがめる', f'''
{table(380)}
{person(180, 380, 1.15, 1, 'violet', 'blue', 'point', 'bun', 'sad')}
{person(430, 380, 1.0, -1, 'coral', 'blue', 'stand', 'short', 'sad')}
<g transform="translate(310 170)">
  <path d="M-70-40h140q12 0 12 12v40q0 12-12 12h-96l-22 16v-16q-12 0-12-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-6-20h12v28h-12z" fill="{TONES['coral'][0]}"/>
  <circle cy="18" r="5" fill="{TONES['coral'][0]}"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M130 210l-26-22M240 190l6-26"/>
</g>
<g transform="translate(430 250)">
  <path d="M-14-6q10-12 20 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
</g>''', ground=False)

add('rectify', '曲がっていた棚を直して水平に戻す', f'''
{split()}
{table(380)}
<g transform="translate(150 250) rotate(-14)">
  <path d="M-100-14h200v28h-200z" fill="#c9a464" class="o"/>
  <g class="o"><rect x="-70" y="-54" width="40" height="40" class="tealp"/><rect x="0" y="-54" width="40" height="40" class="coralp"/></g>
</g>
{cross(150, 130, 0.6)}
<g transform="translate(450 250)">
  <path d="M-100-14h200v28h-200z" fill="#c9a464" class="o"/>
  <g class="o"><rect x="-70" y="-54" width="40" height="40" class="tealp"/><rect x="0" y="-54" width="40" height="40" class="coralp"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="3" stroke-dasharray="8 6"><path d="M-120 0h240"/></g>
</g>
{tick(450, 130, 0.6)}
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>''', arrow=True, ground=False)

add('rejoice', '知らせを聞いて手を取り合って大喜びする', f'''
<path d="M0 0h600v400H0z" fill="#fff6e0"/>
{table(380)}
{person(230, 380, 1.15, 1, 'coral', 'gold', 'up', 'bun', 'smile')}
{person(380, 380, 1.15, -1, 'teal', 'blue', 'up', 'short', 'smile')}
<g class="o">
''' + ''.join(f'<circle cx="{90+i*70}" cy="{70+(i%3)*44}" r="11" class="{["coral","teal","violet","gold"][i%4]}"/>' for i in range(7)) + f'''
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M130 240l-26-22M480 230l26-22M110 300l-30 8M500 300l30 8"/>
</g>''', ground=False)

add('relegate', '一軍の枠から外れて下の組へ落とされる', f'''
{table(380)}
<g transform="translate(300 130)">
  <path d="M-230-70h460v120h-460z" class="goldp o"/>
  <g>
''' + ''.join(head(150+i*100, 130, 22, 'gold', ['short','bob','cap'][i%3]) for i in range(3)) + f'''
  </g>
</g>
<g transform="translate(300 320)">
  <path d="M-230-40h460v100h-460z" fill="#dde3e8" class="o"/>
</g>
{head(160, 320, 22, 'blue', 'short')}
{head(400, 320, 22, 'coral', 'bun')}
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M520 180v100"/></g>''', ground=False)

add('relinquish', '持っていた王冠を差し出して手放す', f'''
{table(380)}
{person(180, 380, 1.1, 1, 'violet', 'blue', 'give', 'bun', 'neutral')}
{person(440, 380, 1.05, -1, 'teal', 'blue', 'give', 'short', 'neutral')}
<g transform="translate(310 230)">
  <path d="M-46 20h92v14h-92z" class="gold o"/>
  <path d="M-46 20l-8-54 28 24 26-38 26 38 28-24-8 54z" class="gold o"/>
  <circle cx="0" cy="-8" r="7" class="corald"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 170q70-40 130 10"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M180 300v-40"/></g>''', arrow=True, ground=False)

add('repel', '磁石の同じ極どうしが押し合って離れる', f'''
{table(380)}
<g transform="translate(180 250)">
  <path d="M-60 40V-10q0-60 60-60t60 60v50h-40V-10q0-20-20-20t-20 20v50z" class="coral o"/>
  <path d="M-60 40h40v30h-40zM20 40h40v30H20z" fill="#c8d0d8" class="o"/>
</g>
<g transform="translate(420 250) scale(-1 1)">
  <path d="M-60 40V-10q0-60 60-60t60 60v50h-40V-10q0-20-20-20t-20 20v50z" class="coral o"/>
  <path d="M-60 40h40v30h-40zM20 40h40v30H20z" fill="#c8d0d8" class="o"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M270 250H160"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M330 250h110"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M300 130v240"/></g>''', ground=False)

add('restrain', '暴れかけた人を後ろから押さえて止める', f'''
{table(380)}
{person(380, 380, 1.15, 1, 'coral', 'blue', 'up', 'short', 'sad')}
{person(200, 380, 1.15, 1, 'teal', 'blue', 'reach', 'cap', 'neutral')}
<g>
  <path d="M248 250q60-16 110 4" stroke="{SKIN}" stroke-width="22" stroke-linecap="round" fill="none"/>
  <path d="M248 250q60-16 110 4" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M470 200h60"/></g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M470 300H370"/></g>''', ground=False)

add('elicit', '質問して相手から答えを引き出す', f'''
{table(380)}
{person(150, 380, 1.05, 1, 'teal', 'blue', 'point', 'bun', 'smile')}
{person(450, 380, 1.05, -1, 'coral', 'blue', 'stand', 'short', 'smile')}
<g transform="translate(240 160)">
  <path d="M-50-40h100q12 0 12 12v40q0 12-12 12h-66l-20 16v-16q-14 0-14-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-16-24q0-18 16-18t16 18-16 14v10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="18" r="4.5" fill="{INK}"/>
</g>
<g transform="translate(400 250)">
  <path d="M50-34H-50q-12 0-12 12v34q0 12 12 12h66l20 16v-16q14 0 14-12v-34q0-12-12-12z" fill="#fffefd" class="o"/>
  {word(0, -4, 4, 24, INK)}
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}" stroke-width="5"><path d="M400 320l-120-40"/></g>''', ground=False)

add('envisage', 'まだない建物を頭の中に思い描く', f'''
<path d="M0 0h600v300H0z" fill="#dceaf4"/>
<path d="M0 300h600v100H0z" fill="#c9d8c0"/>
<path d="M0 300h600" stroke="{INK}" stroke-width="2.5" fill="none"/>
{person(120, 380, 1.05, 1, 'teal', 'blue', 'think', 'bun', 'smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
  <path d="M400 300v-200h100v200M400 100l50-40 50 40"/>
  <path d="M420 160h30v30h-30zM450 220h30v30h-30z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3">
  <circle cx="200" cy="200" r="12"/><circle cx="240" cy="170" r="16"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><ellipse cx="450" cy="190" rx="120" ry="140"/></g>''', ground=False)

add('equate', '重さの違う二つを同じだとみなしてしまう', f'''
{table(380)}
<g transform="translate(300 160)">
  <path d="M-10 0h20v180h-20z" fill="#8f9aa6" class="o"/>
  <path d="M-70 180h140v20h-140z" fill="#8f9aa6" class="o"/>
  <path d="M-200-8h400v16h-400z" fill="#b8bfc8" class="o"/>
  <circle r="16" fill="#8f9aa6" class="o"/>
  <path d="M-190 8v40M190 8v40" stroke="{INK}" stroke-width="3" fill="none"/>
</g>
<g transform="translate(110 208)">
  <path d="M-56 0q0 30 56 30t56-30z" class="tealp o"/>
  <ellipse ry="10" rx="56" class="tealp o"/>
  <circle cy="-20" r="26" class="teal o"/>
</g>
<g transform="translate(490 208)">
  <path d="M-56 0q0 30 56 30t56-30z" class="coralp o"/>
  <ellipse ry="10" rx="56" class="coralp o"/>
  <circle cy="-12" r="14" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M266 320h68M266 348h68"/>
</g>
{cross(300, 334, 0.0)}''', ground=False)

add('exemplify', 'たくさんの中から一つを取り出して典型として示す', f'''
{table(380)}
<g>
''' + ''.join(f'<circle cx="{90+ (i%6)*54}" cy="{300+(i//6)*0}" r="22" class="tealp o"/>' for i in range(6)) + f'''
''' + ''.join(f'<circle cx="{90+ (i%6)*54}" cy="248" r="22" class="tealp o"/>' for i in range(6)) + f'''
</g>
<g transform="translate(460 180)">
  <circle r="60" class="teal o"/>
  <circle r="80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M250 260q100-70 150-40"/></g>''', ground=False)

add('instil', '同じ習慣を毎日少しずつ子に植えつける', f'''
{table(380)}
{person(150, 380, 1.05, 1, 'violet', 'blue', 'reach', 'bun', 'smile')}
{person(430, 380, 0.8, 1, 'coral', 'blue', 'stand', 'cap', 'smile')}
<g fill="{TONES['gold'][0]}">
''' + ''.join(f'<path d="M{250+i*46} {200+ (i%2)*30}q9 10 9 17t-9 8-9-8 9-17z"/>' for i in range(4)) + f'''
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M230 210q90-30 170 40"/></g>
<g transform="translate(430 250)">
  <circle r="30" fill="{TONES['gold'][1]}" class="o"/>
  <path d="M0-16q14 0 14 14t-14 18q-14-4-14-18 0-14 14-14z" class="gold"/>
</g>''', ground=False)

add('lull', '荒れていた海が一時的に静かになる', f'''
{split()}
<path d="M0 0h300v170H0z" fill="#8f9aa6"/>
<path d="M300 0h300v170H300z" fill="#dceaf4"/>
<path d="M0 170h300v230H0z" fill="#4d6f8a"/>
<path d="M300 170h300v230H300z" fill="#7aa8c4"/>
<g fill="none" stroke="#3a5a72" stroke-width="6">
  <path d="M0 220q40-40 80 0t80 0 80 0 60 0M0 290q40-40 80 0t80 0 80 0 60 0M0 350q40-40 80 0t80 0 80 0 60 0"/>
</g>
<g fill="none" stroke="#a8c8dd" stroke-width="4">
  <path d="M320 240h250M320 300h250M320 360h250"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M20 80q60-24 120 0t120-10"/>
</g>
{sun(500, 70, 30)}
<g class="a" marker-end="url(#ar)"><path d="M270 120h60"/></g>''', ground=False)

# --- 名詞・慣用表現 -----------------------------------------------------------
add('purse', '小銭を入れる小さな財布', f'''
{table(340)}
<g transform="translate(300 250)">
  <path d="M-90-30h180v80q0 16-90 16t-90-16z" class="corald o"/>
  <path d="M-90-30q0-50 90-50t90 50z" class="coral o"/>
  <path d="M-90-30h180" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
  <circle cy="-30" r="12" class="gold o"/>
  <path d="M-50-72q50-20 100 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
{coin(160, 300, 18)}
{coin(196, 316, 15)}
{coin(440, 306, 16)}''', ground=False)

add('of-course', '当たり前のことをきかれて、もちろんとうなずく', f'''
{table(380)}
{person(160, 380, 1.05, 1, 'teal', 'blue', 'point', 'bun', 'smile')}
{person(440, 380, 1.05, -1, 'coral', 'blue', 'up', 'short', 'smile')}
<g transform="translate(250 170)">
  <path d="M-50-40h100q12 0 12 12v40q0 12-12 12h-66l-20 16v-16q-14 0-14-12v-40q0-12 12-12z" fill="#fffefd" class="o"/>
  <path d="M-16-24q0-18 16-18t16 18-16 14v10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <circle cy="18" r="4.5" fill="{INK}"/>
</g>
<g transform="translate(410 250)">
  <path d="M50-34H-50q-12 0-12 12v34q0 12 12 12h66l20 16v-16q14 0 14-12v-34q0-12-12-12z" fill="#fffefd" class="o"/>
  {tick(0, -4, 0.42)}
</g>''', ground=False)

add('on-time', '約束の時刻ちょうどに着く', f'''
{table(380)}
<g transform="translate(180 200)">
  <circle r="110" fill="#fffdf6" class="o"/>
  <g fill="{INK}">
''' + ''.join(f'<rect x="-5" y="-92" width="10" height="20" rx="5" transform="rotate({i*30})"/>' for i in range(12)) + f'''
  </g>
  <path d="M0 0v-70" stroke="{INK}" stroke-width="8" stroke-linecap="round" fill="none"/>
  <path d="M0 0v-90" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <circle r="9" fill="{INK}"/>
</g>
{person(430, 380, 1.05, 1, 'coral', 'blue', 'up', 'cap', 'smile', 'walk')}
{tick(500, 180, 0.8)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M310 300h180"/></g>''', ground=False)

add('respectful', '相手に向かってていねいに頭を下げる', f'''
{table(380)}
{person(440, 380, 1.1, -1, 'violet', 'blue', 'stand', 'bun', 'smile')}
<g transform="translate(200 380)">
  <path d="M-14-8l-10 8M14-8l10 8" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-28-76q28-16 56 0l-8 68h-40z" class="teal o"/>
  <g transform="translate(30 -80) rotate(38)">
    <circle cy="-30" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="{HAIRS['short']}" transform="translate(0 78) scale(1.06)" fill="{HAIR}"/>
    <circle cx="-8" cy="-26" r="2.4" fill="{INK}"/><circle cx="8" cy="-26" r="2.4" fill="{INK}"/>
    <path d="M-8-14q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
  </g>
  <path d="M-24-70l-12 46M24-72l16 44" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)" stroke="{TONES['green'][0]}"><path d="M270 210q60-40 110-10"/></g>''', ground=False)

print(sheet(W, '/tmp/vocab-sheet.html', 5)); print(len(W))
