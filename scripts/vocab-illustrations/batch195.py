# -*- coding: utf-8 -*-
"""第43回: plus43(k〜m)の100語。"""
from kit import *


# --- この回で使う小物 --------------------------------------------------------

def bubble(x, y, s=1, cls='blue', f=1, style='lines'):
    """せりふの吹き出し。style で中の模様を変える(言語の違いを表すのに使う)。"""
    g = [f'<g transform="translate({x} {y}) scale({s*f} {s})">',
         f'<path d="M-56-50h112a14 14 0 0 1 14 14v50a14 14 0 0 1-14 14H-14l-30 32 6-32h-18'
         f'a14 14 0 0 1-14-14v-50a14 14 0 0 1 14-14z" class="{cls}p o"/>']
    if style == 'dots':
        g.append(''.join(f'<circle cx="{-34+c*26}" cy="{-20+r*28}" r="7" class="{cls}"/>'
                         for r in range(2) for c in range(4)))
    elif style == 'wave':
        g.append(f'<g fill="none" stroke="{TONES[cls][0]}" stroke-width="5" stroke-linecap="round">'
                 f'<path d="M-38-18q16-16 32 0t32 0M-38 14h64"/></g>')
    else:
        g.append(''.join(f'<rect x="-38" y="{-26+i*24}" width="{76-(i%3)*18}" height="10" rx="5" '
                         f'fill="{TONES[cls][0]}"/>' for i in range(3)))
    g.append('</g>')
    return ''.join(g)


def note(x, y, s=1, cls='violet'):
    """音符。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse cx="0" cy="0" rx="13" ry="10" transform="rotate(-18 0 0)" class="{cls} o"/>'
            f'<path d="M10-2v-38h5v38z" class="{cls}"/>'
            f'<path d="M15-40q24 6 26 26" fill="none" stroke="{TONES[cls][0]}" '
            f'stroke-width="6" stroke-linecap="round"/></g>')


def heart(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0C-38-26-46-52-26-62-8-70 0-56 0-44 0-56 8-70 26-62 46-52 38-26 0 0Z" '
            f'class="{cls} o"/></g>')


def moon(x, y, r=40, cls='gold'):
    return (f'<path d="M{x} {y-r}A{r} {r} 0 0 0 {x} {y+r}A{r*1.5} {r*1.5} 0 0 1 {x} {y-r}Z" '
            f'class="{cls} o"/>')


def key(x, y, s=1, cls='gold'):
    c = TONES[cls][0]
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cx="-46" cy="0" r="24" fill="none" stroke="{c}" stroke-width="12"/>'
            f'<path d="M-22 0h92" fill="none" stroke="{c}" stroke-width="14" stroke-linecap="round"/>'
            f'<path d="M38 0v24M62 0v32" fill="none" stroke="{c}" stroke-width="12" stroke-linecap="round"/></g>')


def gear(x, y, r=50, cls='gold', teeth=9):
    g = [f'<g transform="translate({x} {y})">']
    for i in range(teeth):
        g.append(f'<rect x="{-r*0.16}" y="{-r-8}" width="{r*0.32}" height="18" rx="5" '
                 f'class="{cls} o" transform="rotate({i*360.0/teeth})"/>')
    g.append(f'<circle r="{r}" class="{cls}p o"/><circle r="{r*0.4}" fill="#fffefd" class="o"/></g>')
    return ''.join(g)


def wink(x, y, s=1, cls='blue'):
    """波線(湯気・音・振動など)。"""
    g = ''.join(f'<path d="M{x+i*26*s} {y}q{-14*s} {-22*s} 0 {-44*s}t0 {-44*s}"/>' for i in range(2))
    return f'<g fill="none" stroke="{TONES[cls][0]}" stroke-width="{5*s}" stroke-linecap="round">{g}</g>'


# --- h ----------------------------------------------------------------------

add('fertiliser', '肥料の袋を傾けて芽に粒をふりまくイラスト。', '土にまいて植物の育ちをよくする肥料。', f"""
<g transform="translate(150 140) rotate(32)">
  <path d="M-62-64h124v128h-124z" class="gold o"/>
  <path d="M-62-64h124l-24-30h-76z" class="goldp o"/>
  <path d="M-18 64h36v16h-36z" fill="{MUTED}"/>
</g>
<g class="gold">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>'
                        for x, y, r in [(238,182,8),(266,216,7),(288,252,7),(268,158,6),(300,286,7)])}</g>
<g transform="translate(330 348)">
  <path d="M-74-4h148v44h-148z" class="corald o"/>
  <path d="M-88-14h176v14h-176z" class="coral o"/>
  <path d="M0-14v-84" class="greens"/>
  <path d="M0-56q-44-8-50-46 40-8 50 46z" class="greenp o"/>
  <path d="M0-80q44-8 50-46-40-8-50 46z" class="greenp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('haircut', 'いすに座った人の髪をはさみで切っているイラスト。', '髪を切って整えてもらうこと。', f"""
{sit(230,352,1.2,1,'blue','blue','short','smile','down')}
{person(430,352,1.15,-1,'violet','blue','reach','short','smile')}
<g transform="translate(288 200) rotate(-14)">
  <path d="M40-16L-40-32M40 16L-40 32" fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>
  <circle cx="54" cy="-18" r="13" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <circle cx="54" cy="18" r="13" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
<g fill="none" stroke="{HAIR}" stroke-width="4" stroke-linecap="round">
  <path d="M258 268q-10 14-22 20M276 276q-6 16-16 26M244 254q-8 12-20 16"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hamster', '回し車のそばで丸くなっているハムスターのイラスト。', 'ほお袋に餌をためる小さなげっ歯類、ハムスター。', f"""
<g transform="translate(440 250)">
  <circle r="78" fill="none" stroke="{MUTED}" stroke-width="6"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    <path d="M0-78V78M-78 0h156M-55-55l110 110M55-55l-110 110"/>
  </g>
</g>
<g transform="translate(230 300)">
  <ellipse rx="78" ry="58" class="goldp o"/>
  <circle cx="-58" cy="-44" r="22" class="goldp o"/>
  <circle cx="44" cy="-48" r="20" class="goldp o"/>
  <circle cx="-52" cy="-44" r="10" class="gold"/>
  <circle cx="40" cy="-48" r="9" class="gold"/>
  <ellipse cy="8" rx="32" ry="24" fill="#fffdf6" class="o"/>
  <circle cx="-22" cy="-14" r="6" class="ink"/><circle cx="22" cy="-14" r="6" class="ink"/>
  <ellipse cy="2" rx="9" ry="7" fill="{TONES['coral'][0]}"/>
  <path d="M-26 16q26 18 52 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('happen', 'コップが棚から落ちて床で割れる、思いがけない出来事のイラスト。', '予期しないことが起こる。', f"""
<g transform="translate(400 130)">
  <path d="M-150 0h300v16h-300z" class="goldd o"/>
</g>
<g transform="translate(430 96) rotate(52)">
  <path d="M-26-30h52l-8 60h-36z" class="bluep o"/>
</g>
<path d="M430 150q34 60 4 108" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"/>
<g transform="translate(428 296)">
  <path d="M-52 0l22-28 12 24 18-32 14 32 20-22 14 26z" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
    <path d="M-64-32l-20-18M64-32l20-18M0-42v-28"/>
  </g>
</g>
{person(160,352,1.2,1,'teal','blue','up','short','surprised')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('happy', '笑顔で小さなハートを両手に抱えているイラスト。', 'うれしくて幸せな気持ち。', f"""
{person(300,352,1.35,1,'coral','blue','hold','bob','smile')}
{heart(300,300,0.9,'coral')}
{spark(196,180,1.1)}{spark(404,190,0.9)}{spark(300,116,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hard', '硬い岩にハンマーがはね返されるイラスト。', '固くて壊れない、または難しい。', f"""
<g transform="translate(300 305)">
  <path d="M-150 20q0-66 78-80 104-18 168 20 50 30 28 66-32 50-146 44-128-8-128-50z"
        fill="#b9c2c9" class="o"/>
  <path d="M-84-26q70-26 176-4" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-40 30q66-20 148 6" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g transform="translate(300 172) rotate(-34)">
  <path d="M-106-16h150v32h-150z" fill="{MUTED}" class="o"/>
  <path d="M44-36h46v72h-46z" fill="#8f9aa3" class="o"/>
  <path d="M90-10h96l16 10-16 10H90z" class="goldd o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M214 222q-70-46-30-104"/></g>
{spark(330,214,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('harmonica', 'ハーモニカを口にあてて吹いているイラスト。', '口で吹いて音を出す小さな楽器、ハーモニカ。', f"""
{person(230,352,1.2,1,'violet','blue','hold','short','smile')}
<g transform="translate(292 240)">
  <path d="M-72-25h154v50h-154z" class="gold o"/>
  <g fill="{INK}">{''.join(f'<rect x="{-60+i*22}" y="-14" width="12" height="28" rx="3"/>' for i in range(7))}</g>
</g>
{note(430,190,1.2,'violet')}{note(486,232,0.9,'violet')}{note(410,110,1.0,'teal')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('has', '箱をしっかり抱えて持っているイラスト。', '「持っている」を表す have の三人称単数形。', f"""
{person(300,352,1.3,1,'teal','blue','hold','short','smile')}
{box(300,268,124,92,26,'gold')}
{tick(190,180,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hat', 'つばの広い帽子をかぶっている人のイラスト。', '頭にかぶる帽子。', f"""
{person(300,352,1.35,1,'violet','blue','stand','short','smile')}
<g transform="translate(300 176)">
  <ellipse rx="94" ry="19" class="coralp o"/>
  <path d="M-46-8q-4-58 46-58t46 58z" class="coral o"/>
  <path d="M-46-8q46-16 92 0" fill="none" stroke="{CRLD}" stroke-width="10"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('having', '手に持ったカップを口に運んで飲んでいるイラスト。', '「持っている・している」を表す have の進行形。', f"""
{person(300,352,1.3,1,'teal','blue','hold','bob','smile')}
<g transform="translate(316 266)">
  <path d="M-34-38h68v68a10 10 0 0 1-10 10h-48a10 10 0 0 1-10-10z" class="goldp o"/>
  <path d="M34-16h20a19 19 0 0 1 0 38H34" fill="none" stroke="{GLDD}" stroke-width="7"/>
  <path d="M-34-38h68" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M298 216q-14-16 0-32t0-30M334 216q-14-16 0-32t0-30"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('he', '輪でかこんで男性ひとりを指し示すイラスト。', '男性を指す代名詞「彼は・彼が」。', f"""
{person(300,352,1.25,1,'blue','blue','point','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10">
  <circle cx="300" cy="248" r="122"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('health', 'ハートと脈の線、りんごで表す健康のイラスト。', '体の調子がよく元気なこと、健康。', f"""
{heart(180,266,1.6,'coral')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">
  <path d="M320 246h46l26-56 32 104 28-70 22 22h76"/>
</g>
<g transform="translate(492 322)">
  <circle r="44" class="coralp o"/>
  <path d="M-14-34q14-16 30-6" fill="none" stroke="#fffdf6" stroke-width="6" stroke-linecap="round"/>
  <path d="M0-44v-18" fill="none" stroke="{GRND}" stroke-width="7" stroke-linecap="round"/>
  <path d="M2-60q30-14 44 4-24 20-44-4z" class="greenp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('healthy', '走って体を動かし、りんごを食べている健康な人のイラスト。', '体に良く、健康なようす。', f"""
{person(230,352,1.25,1,'teal','blue','walk','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M40 240h58M28 288h48"/>
</g>
<g transform="translate(452 320)">
  <circle r="44" class="coralp o"/>
  <path d="M0-44v-18" fill="none" stroke="{GRND}" stroke-width="7" stroke-linecap="round"/>
  <path d="M2-60q30-14 44 4-24 20-44-4z" class="greenp o"/>
</g>
{heart(320,180,0.75,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hear', 'リンを鳴らして音が耳にとどくようすのイラスト。', '音が自然に耳に入ってくる、聞こえる。', f"""
{person(170,352,1.2,1,'violet','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M382 232a50 50 0 0 0 0 76"/>
  <path d="M352 208a78 78 0 0 0 0 124"/>
  <path d="M322 184a106 106 0 0 0 0 172"/>
</g>
<g transform="translate(452 250)">
  <path d="M-46 12q0-82 46-82t46 82q0 14 22 20H-68q22-6 22-20z" class="gold o"/>
  <circle cy="42" r="14" class="goldd o"/>
  <path d="M0-70v-24" fill="none" stroke="{BRN}" stroke-width="8" stroke-linecap="round"/>
  <circle cy="-102" r="12" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hello', '電話を耳にあてて挨拶しているイラスト。', '電話や対面でのあいさつ「もしもし・こんにちは」。', f"""
{person(250,352,1.25,1,'coral','blue','think','bob','smile')}
<g transform="translate(292 206) rotate(-12)">
  <rect x="-17" y="-48" width="34" height="96" rx="10" class="ink"/>
  <rect x="-11" y="-32" width="22" height="64" rx="5" class="bluep"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M368 168a44 44 0 0 1 34 30M384 132a76 76 0 0 1 58 52"/>
</g>
{spark(430,240,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('help', '穴に落ちた人に手を差し伸べて引き上げるイラスト。', '困っている人の力になる、助ける。', f"""
{person(180,352,1.25,1,'teal','blue','reach','short','smile')}
{person(440,420,1.2,-1,'coral','blue','up','bob','neutral')}
<path d="M290 300h310v100H290z" fill="#ded3c2" class="o"/>
<path d="M290 300h310" fill="none" stroke="{BRN}" stroke-width="7"/>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M300 240q60-56 120-64"/></g>
<path d="M60 386h80" class="a"/>
""", ground=True, arrow=True)

add('her', '花を手渡された女性を輪で示すイラスト。', '女性を目的語・所有格で指す「彼女を・彼女の」。', f"""
{person(180,352,1.15,1,'violet','blue','give','short','smile')}
{person(430,352,1.15,-1,'coral','gold','reach','bob','smile')}
{flower(306,254,0.95,'coral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10">
  <circle cx="430" cy="248" r="120"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('here', '矢印が足もとの場所を指しているイラスト。', '話し手のいる場所「ここに・ここへ」。', f"""
{person(250,352,1.25,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="14 10">
  <ellipse cx="250" cy="368" rx="88" ry="24"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M480 76q70 140-150 262"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('hey', '手を上げて大声で人を呼びとめるイラスト。', '人を呼びとめるときの「おい・やあ」。', f"""
{person(270,352,1.3,1,'coral','blue','up','short','surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M420 156l46-30M404 216h58M424 262l40 26"/>
</g>
{spark(470,110,1,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hi', '手をふって気軽にあいさつしているイラスト。', '気軽なあいさつ「やあ・こんにちは」。', f"""
{person(250,352,1.3,1,'teal','blue','up','bob','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M352 158q26-10 44 10M362 206q28 2 40 22"/>
</g>
{spark(444,140,0.85,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('highchair', '赤ちゃんが高い食事椅子に座っているイラスト。', '小さな子を高い位置に座らせる食事用の椅子。', f"""
<g transform="translate(300 356)">
  <path d="M-90 0l-16-70M90 0l18-70" fill="none" stroke="{BRN}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-100-34h196" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-118-70h236v18h-236z" class="goldd o"/>
  <path d="M64-186h26v116H64z" class="gold o"/>
</g>
<g transform="translate(268 212)">
  <circle r="36" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-26-18q8-16 26-16t26 16" fill="none" stroke="{HAIR}" stroke-width="7" stroke-linecap="round"/>
  <circle cx="-12" cy="-4" r="3.4" class="ink"/><circle cx="12" cy="-4" r="3.4" class="ink"/>
  <path d="M-12 14q12 12 24 0" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>
  <path d="M-30 44q30 18 60 0v36h-60z" class="teal o"/>
  <path d="M-32 36l-26-40M32 36l26-44" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
</g>
<g transform="translate(300 278)">
  <path d="M-150 0h300v16h-300z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('highlighter', '文書の一行を蛍光ペンでなぞって目立たせるイラスト。', '文字の上をなぞって目立たせる蛍光ペン。', f"""
<g transform="translate(268 208)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="{MUTED}">{''.join(f'<rect x="-112" y="{-112+i*44}" width="{224-(i%3)*40}" height="11" rx="5"/>'
                            for i in range(6))}</g>
  <rect x="-116" y="-30" width="232" height="26" rx="6" class="gold" opacity="0.8"/>
</g>
<g transform="translate(400 240) rotate(150)">
  <path d="M-26-92h52v124l-26 40-26-40z" class="gold o"/>
  <path d="M-26-92h52v-26h-52z" class="goldd o"/>
  <path d="M-26 32l26 40 26-40z" fill="#fffdf6" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('him', '手紙を手渡された男性を輪で示すイラスト。', '男性を目的語として指す「彼を・彼に」。', f"""
{person(170,352,1.1,1,'coral','blue','give','bob','smile')}
{person(430,352,1.1,-1,'blue','blue','reach','short','smile')}
<g transform="translate(300 252)">
  <path d="M-46-30h92v60h-92z" class="paper"/>
  <path d="M-46-30l46 30 46-30" fill="none" stroke="{MUTED}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10">
  <circle cx="430" cy="248" r="120"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('history', '古い石の柱の神殿と時の流れを示す矢印のイラスト。', '昔から積み重ねられてきた出来事の流れ、歴史。', f"""
<g transform="translate(180 300)">
  <path d="M-124-18h248v18h-248z" fill="#e6ded2" class="o"/>
  <g fill="#e6ded2" stroke="{INK}" stroke-width="2.5">
    {''.join(f'<rect x="{-100+i*54}" y="-138" width="30" height="120"/>' for i in range(4))}
  </g>
  <path d="M-140-138L0-210l140 72z" fill="#e6ded2" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M60 356h480"/>
</g>
<g class="gold o">{''.join(f'<circle cx="{x}" cy="356" r="13"/>' for x in [140,300,460])}</g>
""", ground=False, arrow=True)

add('hitchhike', '道ばたで親指を上げて車を止めようとするイラスト。', '通りがかりの車に乗せてもらうヒッチハイク。', f"""
<path d="M0 340h600v60H0z" fill="#dfe6ea"/>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="22 18"><path d="M0 372h600"/></g>
{person(190,340,1.2,-1,'coral','blue','up','short','smile')}
<g transform="translate(450 288)">
  <path d="M-120-30h240v56h-240z" class="teal o"/>
  <path d="M-72-30q12-42 62-42t62 42z" class="tealp o"/>
  <circle cx="-64" cy="30" r="25" class="ink"/><circle cx="64" cy="30" r="25" class="ink"/>
  <circle cx="-64" cy="30" r="9" fill="#c3cbd1"/><circle cx="64" cy="30" r="9" fill="#c3cbd1"/>
</g>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="5" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M478 194H352"/></g>
""", ground=False, arrow=True)

add('hobby', 'イーゼルに向かって絵を描いて楽しむイラスト。', '好きで続けている楽しみごと、趣味。', f"""
<g fill="none" stroke="{BRN}" stroke-width="11" stroke-linecap="round">
  <path d="M322 320l-26 62M518 320l26 62M420 320v62"/>
</g>
<g transform="translate(420 210)">
  <path d="M-110-100h220v210h-220z" class="paper"/>
  <circle cx="-40" cy="-40" r="28" class="goldp o"/>
  <path d="M-110 40q60-70 110-20t110-30v110h-220z" class="greenp"/>
  <path d="M-110-100h220v210h-220z" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
{person(190,352,1.15,1,'violet','blue','reach','bob','smile')}
<g transform="translate(258 232) rotate(-24)">
  <path d="M0 0h56" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
  <path d="M56 0l18-11v22z" class="coral o"/>
</g>
<g transform="translate(140 300) rotate(-14)">
  <ellipse rx="48" ry="33" class="paper"/>
  <circle cx="-18" cy="-6" r="9" class="coral o"/><circle cx="10" cy="-12" r="9" class="teal o"/>
  <circle cx="8" cy="10" r="9" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hoodie', 'フードと大きなポケットのついたパーカーのイラスト。', 'フードのついた上着、パーカー。', f"""
<g transform="translate(300 200)">
  <path d="M-74-40q-42 24-52 96l-6 44 40 12 24-72z" class="teal o"/>
  <path d="M74-40q42 24 52 96l6 44-40 12-24-72z" class="teal o"/>
  <path d="M-74-46h148l16 186H-90z" class="teal o"/>
  <path d="M-56-46q4-58 56-58t56 58q-26 22-56 22t-56-22z" class="tealp o"/>
  <path d="M-30-24v46M30-24v46" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="-30" cy="26" r="7" class="gold o"/><circle cx="30" cy="26" r="7" class="gold o"/>
  <path d="M-52 62h104v56h-104z" class="tealp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('horse', 'たてがみと長い尾のある馬の横姿のイラスト。', '人を乗せたり荷を運んだりする家畜、馬。', f"""
<g transform="translate(250 300) scale(0.9)">
  <path d="M-96 0l-10 46M-56 0l-6 44M56 0l8 44M92 0l12 46" fill="none" stroke="#8b6437" stroke-width="16" stroke-linecap="round"/>
  <path d="M-124-26q-6-52 62-58 96-10 168 6 56 14 56 50 0 34-58 42-120 14-198-2-36-8-30-38z" fill="#8b6437" stroke="{INK}" stroke-width="2.5"/>
  <path d="M96-72q16-70 42-92l58 24q-32 40-40 92z" fill="#8b6437" stroke="{INK}" stroke-width="2.5"/>
  <path d="M138-164q30-34 62-22 26 10 22 36-4 22-30 24l-54 6z" fill="#8b6437" stroke="{INK}" stroke-width="2.5"/>
  <path d="M150-176l-8-32 26 20zM180-184l8-32 16 28z" fill="#8b6437" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="176" cy="-146" r="6" fill="#fffdf6"/>
  <path d="M104-76q12-58 38-84" fill="none" stroke="#5b4a3a" stroke-width="18" stroke-linecap="round"/>
  <path d="M-124-46q-46 12-56 70-6 34 4 50 8-44 28-70 14-20 30-26z" fill="#5b4a3a" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hot', '湯気の立つカップと太陽で表す暑さのイラスト。', '熱くて湯気が立つ、または暑い。', f"""
<g transform="translate(220 300)">
  <path d="M-70-70h140v92a32 32 0 0 1-32 32h-76a32 32 0 0 1-32-32z" fill="#fffdf6" class="o"/>
  <path d="M-70-70h140v16H-70z" class="coral o"/>
  <path d="M70-46h24a30 30 0 0 1 0 60H70" fill="none" stroke="{INK}" stroke-width="7"/>
  <ellipse cy="58" rx="52" ry="12" fill="{MUTED}" opacity="0.3"/>
</g>
{wink(190,244,1.2,'coral')}
{sun(452,132,46)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M470 226v42M522 204l-18 38M424 204l18 38"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hotel', '窓のならぶ宿の入口に荷物を運ぶ人のいるイラスト。', '旅行者が泊まる宿、ホテル。', f"""
{tower(400,340,1,'teal',5)}
<g transform="translate(400 296)">
  <path d="M-74-16h148v16h-148z" class="coral o"/>
  <path d="M-60-16v-22h120v22z" class="coralp o"/>
</g>
{person(170,352,1.15,1,'violet','blue','carry','cap','smile')}
<g transform="translate(200 318)">
  <path d="M-36-48h72v72h-72z" class="goldd o"/>
  <path d="M-18-48v-16h36v16" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-36-12h72" fill="none" stroke="{GLDD}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hour', '時計の針が一周するあいだの時間を示すイラスト。', '60分の長さ、1時間。', f"""
{clock(280,196,104,4,12)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M420 90A140 140 0 0 1 420 302"/></g>
""", ground=False, arrow=True)

add('how', '地図の上で道順をたどって行き方を示すイラスト。', '方法や手段をたずねる「どうやって」。', f"""
<g transform="translate(220 236) rotate(-8)">
  <path d="M-120-120h240v240h-240z" class="paper"/>
  <path d="M-120 46q60 40 120 10t120 20v50h-240z" class="greenp"/>
  <path d="M-104-120q40 80 20 120t30 120" fill="none" stroke="{TONES['blue'][0]}" stroke-width="9"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="7" stroke-linecap="round"
     stroke-dasharray="14 10" marker-end="url(#ar)"><path d="M-84 84q80-16 58-74t56-72"/></g>
  <circle cx="-84" cy="84" r="14" class="teal o"/>
  <circle cx="30" cy="-62" r="14" class="coral o"/>
</g>
{person(450,352,1.15,-1,'teal','blue','point','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('humidifier', '白い霧を上に吹き出す加湿器のイラスト。', '部屋をうるおす家電、加湿器。', f"""
<g transform="translate(260 306)">
  <path d="M-66-100h132v122a20 20 0 0 1-20 20h-92a20 20 0 0 1-20-20z" fill="#fffdf6" class="o"/>
  <path d="M-66-100h132v30H-66z" class="bluep o"/>
  <path d="M-34-132h68v32h-68z" class="bluep o"/>
  <circle cy="-8" r="24" class="bluep o"/>
  <path d="M-12-8h24M0-20v24" fill="none" stroke="{BLUD}" stroke-width="4"/>
</g>
{wink(242,168,1.05,'blue')}
<g class="bluep o">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(214,124,9),(288,118,10),(252,84,13),(300,70,9),(232,46,15)])}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('hundred', '10×10にきちんと並んだ点で100を表すイラスト。', '100、また非常に多い数。', f"""
<g class="goldp o">{''.join(f'<circle cx="{112+c*42}" cy="{62+r*30}" r="13"/>' for r in range(10) for c in range(10))}</g>
<rect x="88" y="40" width="424" height="312" rx="20" fill="none" stroke="{CRL}" stroke-width="5" stroke-dasharray="14 10"/>
""", ground=False)

add('hungry', 'おなかを押さえて空腹をこらえているイラスト。', 'おなかがすいた状態。', f"""
{person(230,352,1.25,1,'teal','blue','hold','short','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M144 286q-22-20-4-42M152 314q-22-20-4-42"/>
</g>
<g transform="translate(450 322)">
  <ellipse rx="78" ry="26" class="paper"/>
  <ellipse rx="50" ry="15" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('husband', '指輪をかわした夫婦が並んで立っているイラスト。', '結婚している男性、夫。', f"""
{person(250,352,1.25,-1,'blue','blue','stand','short','smile')}
{person(370,352,1.2,1,'coral','gold','stand','bob','smile')}
<path d="M296 320h34" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
{ring(313,320,18,False,'gold')}
{heart(310,196,0.7,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('i', '自分の胸に両手をあてて名乗るイラスト。', '話し手自身を表す「私は・私が」。', f"""
{person(300,352,1.25,1,'teal','blue','hold','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10">
  <circle cx="300" cy="248" r="120"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M150 160q80 60 132 120"/></g>
""", ground=True, arrow=True)

add('ice', 'グラスに入った角氷と冷気のイラスト。', '水が凍って固まったもの、氷。', f"""
<g transform="translate(280 300)">
  <path d="M-72-104h144l-14 148h-116z" fill="#e1edfb" class="o"/>
  <path d="M-46-76h54v42h-54z" class="bluep o" transform="rotate(12 -19 -55)"/>
  <path d="M6-30h50v40H6z" class="bluep o" transform="rotate(-14 31 -10)"/>
  <path d="M-44 22h48v36h-48z" class="bluep o" transform="rotate(8 -20 40)"/>
  <path d="M-72-104h144" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g fill="none" stroke="{TONES['blue'][2]}" stroke-width="5" stroke-linecap="round">
  <path d="M420 150v-34M456 184l24-24M400 206h-34"/>
</g>
{drop(452,286,1.4,'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('idea', '頭の上に電球が光る、ひらめきのイラスト。', 'ふと浮かんだ考え、思いつき。', f"""
{person(300,352,1.25,1,'violet','blue','think','short','smile')}
<g transform="translate(300 132)">
  <circle cy="-14" r="42" class="goldp o"/>
  <path d="M-16 30h32v14h-32zM-11 48h22v12h-22z" class="goldd o"/>
  <path d="M-24-24a24 24 0 0 1 48 0" fill="none" stroke="{GLDD}" stroke-width="4"/>
</g>
{spark(188,116,1.1)}{spark(414,124,0.95)}{spark(300,52,1.2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('if', '道が二つに分かれる分かれ道のイラスト。', '「もし…なら」と条件を示す接続詞。', f"""
<g fill="none" stroke="#dfe6ea" stroke-width="54" stroke-linecap="round">
  <path d="M300 380V252M300 252L180 92M300 252l120-160"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="16 14" stroke-linecap="round">
  <path d="M300 372V254M296 246L182 96M304 246l114-152"/>
</g>
<g transform="translate(300 252)">
  <path d="M0-52L40 0 0 52-40 0z" class="goldp o"/>
  <path d="M-14 0h28" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('important', '両手で大切にかかえた箱と輝きのイラスト。', 'とても大切で、重要である。', f"""
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-dasharray="12 10">
  <circle cx="300" cy="222" r="112"/>
</g>
{box(300,222,144,100,32,'gold')}
{hand(160,296,1)}
{hand(440,296,-1)}
{spark(300,72,1.5,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('in', '透明な箱の中にボールが入っているイラスト。', 'ある物の中にあることを示す「…の中に」。', f"""
<g transform="translate(300 236)">
  <circle r="56" class="coral o"/>
  <circle cx="-20" cy="-20" r="15" fill="#fffdf6" opacity="0.7"/>
  <path d="M-112-112h224v224h-224z" fill="#e1edfb" opacity="0.5" class="o"/>
</g>
""", ground=False)

add('insomnia', '夜中、目を見開いたまま寝床で眠れずにいるイラスト。', '眠りたいのに眠れない不眠症。', f"""
{moon(108,90,46,'gold')}
{clock(496,108,50,4,0)}
<g transform="translate(300 320)">
  <path d="M-200-8h400v44h-400z" class="violetd o"/>
  <path d="M-200-28h400v20h-400z" class="violet o"/>
  <path d="M-200-28v-100" fill="none" stroke="{VIOD}" stroke-width="24" stroke-linecap="round"/>
</g>
<path d="M124 296h88a26 26 0 0 1 26 26v40H124z" fill="#fffefd" class="o"/>
{face(186,262,40,'flat')}
<g fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" opacity="0.55">
  <path d="M162 280q10-8 20 0M196 280q10-8 20 0"/>
</g>
{drop(244,300,1.2,'blue')}
<g transform="translate(300 308)">
  <path d="M-60-16h300v20h-300z" class="violet o"/>
  <path d="M0-24q40-40 96-24t110 6" fill="none" stroke="{VIOD}" stroke-width="7"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('interested', '身を乗り出して本に見入っているイラスト。', '興味や関心を持っている状態。', f"""
{person(190,352,1.2,1,'teal','blue','reach','short','smile')}
{book(430,254,0.95,'violet')}
{spark(378,166,0.9)}{spark(492,156,1)}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M300 216q50-30 96-16M304 248q48-26 92-14"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('interesting', '本を読んで思わず笑顔になっているイラスト。', '興味をひかれて面白い。', f"""
{person(230,352,1.25,1,'gold','blue','hold','bob','smile')}
{book(248,270,0.62,'teal')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M320 122l-14-30M360 152l26-24M316 178h-34"/>
</g>
{spark(452,116,1.1)}{spark(376,86,0.85)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('internet', 'ノートパソコンと地球を線でつないだイラスト。', '世界のコンピュータをつなぐ網、インターネット。', f"""
<g transform="translate(190 208)">
  <circle r="86" class="bluep o"/>
  <ellipse rx="34" ry="86" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-86-32h172M-86 32h172" fill="none" stroke="{INK}" stroke-width="3"/>
  <g class="coral o"><circle cx="-86" cy="0" r="13"/><circle cx="86" cy="0" r="13"/>
    <circle cx="0" cy="-86" r="13"/><circle cx="0" cy="86" r="13"/></g>
</g>
<g transform="translate(440 302)">
  <path d="M-108-92h216v122h-216z" fill="#fffdf6" class="o"/>
  <path d="M-94-78h188v94h-188z" class="bluep"/>
  <path d="M-136 30h272l22 30H-158z" fill="#c3cbd1" class="o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M388 168a72 72 0 0 1 104 0M410 200a42 42 0 0 1 60 0"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
  <path d="M278 232q60 30 80 60M278 168q60-20 80-40"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('interpreter', '二人の間に立って言葉を行き来させているイラスト。', '異なる言語の間で言葉を伝える人、通訳者。', f"""
{person(110,352,1,1,'teal','blue','stand','short','smile')}
{person(490,352,1,-1,'coral','blue','stand','bob','smile')}
{person(300,352,1.15,1,'violet','blue','give','bun','smile')}
{bubble(120,140,0.72,'teal',1,'lines')}
{bubble(480,140,0.72,'coral',-1,'dots')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
  <path d="M216 96q84-46 168 0M384 224q-84 46-168 0"/>
</g>
""", ground=True)

add('into', '箱の中へボールが入っていくイラスト。', '外から中へ入る動きを表す「…の中へ」。', f"""
<g transform="translate(390 240)">
  <path d="M-110-110h220v220h-220z" fill="#e1edfb" opacity="0.5" class="o"/>
</g>
<circle cx="140" cy="240" r="54" class="coral o"/>
<circle cx="284" cy="240" r="54" class="coral o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M212 240h40"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
  <circle cx="140" cy="240" r="72"/>
</g>
""", ground=False, arrow=True)

add('ironing board', 'アイロン台に布をのせてアイロンをあてるイラスト。', 'アイロンをかけるための台。', f"""
<g transform="translate(300 220)">
  <path d="M-190-16q0-18 24-18h332q24 0 24 18t-24 18h-332q-24 0-24-18z" class="tealp o"/>
  <path d="M-140 20l-24 140M110 20l40 140M-70 20l-6 140" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-150-34h300l-16-14h-268z" fill="#fffefd" class="o"/>
</g>
<g transform="translate(392 166)">
  <path d="M-76 22q-22-2-22-19t24-17h96q32 0 32 19t-32 17z" class="violetp o"/>
  <path d="M-40-16v-36h72v36" fill="none" stroke="{VIOD}" stroke-width="17" stroke-linecap="round"/>
</g>
{wink(438,112,0.9,'violet')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('is', '二つの同じ形を等号で結ぶイラスト。', '「AはBです」と主語と説明をつなぐ語。', f"""
<g transform="translate(160 240)">
  <circle r="76" class="tealp o"/>
  <circle r="36" class="teal o"/>
</g>
<g transform="translate(440 240)">
  <circle r="76" class="tealp o"/>
  <circle r="36" class="teal o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round">
  <path d="M266 210h68M266 270h68"/>
</g>
""", ground=False)

add('island', '海に浮かぶ島とヤシの木のイラスト。', '海に囲まれた陸地、島。', f"""
<path d="M0 318h600v82H0z" class="bluep"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M40 348q30-14 60 0t60 0M420 360q30-14 60 0t60 0M120 382q30-14 60 0"/>
</g>
<g transform="translate(300 318)">
  <path d="M-176 0q44-54 176-54t176 54z" class="goldp o"/>
  <path d="M0-54q-16-70-44-98" fill="none" stroke="{BRN}" stroke-width="13" stroke-linecap="round"/>
  <g class="greenp o">
    <path d="M-44-152q-62-26-98 6 52 22 98-6zM-44-152q-32-62-82-60 12 54 82 60z
             M-44-152q42-58 92-42-22 52-92 42zM-44-152q62-22 82 26-54 14-82-26z"/>
  </g>
</g>
""", ground=False)

add('its', '犬のそばの茶わんを輪で指し示すイラスト。', 'ものや動物の所有を表す「その・それの」。', f"""
{beast(200,330,0.8,'#8b6437',1)}
<g transform="translate(470 336)">
  <path d="M-84-8q0 42 84 42t84-42z" class="blue o"/>
  <ellipse cy="-8" rx="84" ry="24" class="bluep o"/>
  <ellipse cy="-8" rx="58" ry="15" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10">
  <circle cx="470" cy="310" r="78"/>
</g>
""", ground=True)

add('mortar', '乳鉢と乳棒ですりつぶして粉にするイラスト。', '薬や香辛料をすりつぶす道具、乳鉢。', f"""
<g transform="translate(300 330)">
  <path d="M-92-76q0 84 92 84t92-84z" fill="#e6ded2" class="o"/>
  <ellipse cy="-76" rx="92" ry="26" fill="#f4efe6" class="o"/>
  <ellipse cy="-76" rx="70" ry="18" class="gold"/>
</g>
<g transform="translate(300 330) rotate(16)">
  <path d="M0-46v-110" fill="none" stroke="#c3cbd1" stroke-width="26" stroke-linecap="round"/>
  <circle cy="-168" r="24" fill="#c3cbd1" class="o"/>
</g>
<g class="gold o">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(180,340,7),(156,362,6),(432,346,7),(454,330,6)])}</g>
""", ground=True)

add('job', 'かばんを持って職場へ向かう人のイラスト。', '働いて収入を得る仕事、職。', f"""
{building(470,340,0.85,'teal')}
{person(190,352,1.2,1,'blue','blue','carry','short','smile')}
<g transform="translate(250 316)">
  <path d="M-46-52h92v74h-92z" class="corald o"/>
  <path d="M-16-52v-16h32v16" fill="none" stroke="#5f4d91" stroke-width="7"/>
  <path d="M-46-14h92" fill="none" stroke="{CRLD}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('join', 'つながって並ぶ仲間の列に加わっていくイラスト。', '仲間や集まりに加わる、つながる。', f"""
{person(300,352,0.95,1,'teal','blue','stand','short','smile')}
{person(370,352,0.95,1,'coral','blue','stand','bob','smile')}
{person(440,352,0.95,1,'gold','blue','stand','cap','smile')}
{person(120,352,1.15,1,'violet','blue','walk','short','smile')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="6" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M194 296q50-24 88-12"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('judo', '置の上で組み合って投げ技をかけるイラスト。', '日本の武道、柔道。', f"""
<path d="M60 336h480v50H60z" class="goldp o"/>
<g fill="none" stroke="{GLDD}" stroke-width="3"><path d="M60 361h480M220 336v50M380 336v50"/></g>
{person(230,336,1.05,1,'blue','blue','give','short','neutral')}
{person(360,336,1.05,-1,'violet','violet','up','bun','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M436 232q56-40 74 8"/></g>
""", ground=True, arrow=True)

add('juice', 'ストローをさしたジュースのグラスと果物のイラスト。', '果物をしぼった飲みもの、ジュース。', f"""
<g transform="translate(240 300)">
  <path d="M-62-116h124l-14 148h-96z" fill="#fffdf6" class="o"/>
  <path d="M-54-62h108l-9 84h-90z" class="gold"/>
  <path d="M-62-116h124" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M36-152l-44 130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="13" stroke-linecap="round"/>
</g>
<g transform="translate(468 320)">
  <circle r="58" class="goldp o"/>
  <path d="M-58 0h116M0-58v116" fill="none" stroke="{GLDD}" stroke-width="3"/>
  <path d="M0-58v-20" fill="none" stroke="{GRND}" stroke-width="8" stroke-linecap="round"/>
  <path d="M2-78q32-16 46 4-26 22-46-4z" class="greenp o"/>
</g>
""", ground=True)

add('nectar', '花の蜜をハチが吸いに来るイラスト。', '花の中にある甘い蜜。', f"""
{flower(200,300,1.6,'coral')}
{flower(86,330,0.9,'violet')}
{drop(212,268,1.5,'gold')}
<g transform="translate(412 206) rotate(-14)">
  <ellipse rx="44" ry="30" class="gold o"/>
  <path d="M-16-28v56M16-28v56" fill="none" stroke="{INK}" stroke-width="7"/>
  <circle cx="-52" cy="-6" r="18" class="ink"/>
  <path d="M-8-26q-22-44-54-32 16 28 54 32z" fill="#fffdf6" opacity="0.85" class="o"/>
  <path d="M14-26q22-44 54-32-16 28-54 32z" fill="#fffdf6" opacity="0.85" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10">
  <path d="M366 204q-84-30-142 48"/>
</g>
""", ground=True)

add('jungle', '木が何本も茂り、つるが垂れる密林のイラスト。', '熱帯のこんもりと茂った森、ジャングル。', f"""
<g fill="none" stroke="{GRND}" stroke-width="17" stroke-linecap="round">
  <path d="M60 340V250M180 340V190M310 340V120M450 340V200M540 340V260"/>
</g>
<g class="green o">{''.join(f'<circle cx="{66+c*118}" cy="{190+(c%3)*40}" r="{56+(c%2)*12}" opacity="0.85"/>' for c in range(5))}</g>
<g class="greenp o">{''.join(f'<circle cx="{124+c*126}" cy="{236+(c%2)*36}" r="{46+(c%3)*10}"/>' for c in range(4))}</g>
<g fill="none" stroke="{GRND}" stroke-width="5" stroke-linecap="round">
  <path d="M96 210q-10 60 8 92M392 214q12 62-4 96M244 190q-8 76 10 116"/>
</g>
""", ground=True)

add('kangaroo', 'おなかの袋から赤ちゃんが顔を出すカンガルーのイラスト。', 'おなかの袋で子を育てる動物、カンガルー。', f"""
<g transform="translate(300 215) scale(0.85)">
  <path d="M-40 0q-70 30-110 96-10 22 14 20 40-40 76-58z" fill="#8b6437" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-60-96q30-56 96-52 56 4 60 56 4 46-40 66-60 26-104-10-22-30-12-60z" fill="#a2764a" stroke="{INK}" stroke-width="2.5"/>
  <path d="M22-110q6-80 24-108l46 16q-18 50-18 96z" fill="#a2764a" stroke="{INK}" stroke-width="2.5"/>
  <path d="M42-200q22-34 52-26 26 8 24 32-2 22-26 26l-38 6z" fill="#a2764a" stroke="{INK}" stroke-width="2.5"/>
  <path d="M46-212l-8-32 24 20zM84-216l12-30 10 28z" fill="#a2764a" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="76" cy="-186" r="5" fill="#fffdf6"/>
  <path d="M-48 40l-18 96h52l16-72zM28 40l10 96h54l-26-96z" fill="#a2764a" stroke="{INK}" stroke-width="2.5"/>
  <ellipse cx="-20" cy="-38" rx="44" ry="36" class="goldp o"/>
  <circle cx="-22" cy="-72" r="21" class="goldp o"/>
  <circle cx="-30" cy="-76" r="4" class="ink"/><circle cx="-14" cy="-76" r="4" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('karate', '空手の突きで板を割るイラスト。', '日本の武道、空手。', f"""
{person(190,352,1.25,1,'blue','blue','point','short','neutral')}
<g transform="translate(400 240)">
  <path d="M-130-76h124v152h-124z" fill="#e6ded2" class="o" transform="rotate(-7 -124 0)"/>
  <path d="M-4-76h134v152H-4z" fill="#e6ded2" class="o" transform="rotate(5 130 0)"/>
</g>
{spark(286,268,1.2)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M236 216l-32-22M240 320l-30 24"/>
</g>
""", ground=True)

add('kayak', 'パドルでこぐカヤックが水面を進むイラスト。', '一人乗りの細長い小舟、カヤック。', f"""
<path d="M0 306h600v94H0z" class="bluep"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M40 340q30-14 60 0t60 0M420 352q30-14 60 0t60 0M160 380q30-14 60 0"/>
</g>
{sit(300,392,0.95,1,'teal','blue','cap','smile','up')}
<g transform="translate(300 330)">
  <path d="M-250 0q60 36 250 36t250-36q-60-28-250-28t-250 28z" class="coral o"/>
  <path d="M-214-4q120 18 428 0" fill="none" stroke="{CRLD}" stroke-width="5"/>
</g>
<g transform="translate(300 274) rotate(-13)">
  <path d="M-170 0h340" fill="none" stroke="{BRN}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-176-10h-42v20h42zM176-10h42v20h-42z" fill="{BRN}" class="o"/>
</g>
""", ground=False)

add('keep', '錠のついた箱を両腕でかかえて手ばなさないイラスト。', '手もとにおいて、なくさずとっておく。', f"""
{person(300,352,1.3,1,'violet','blue','hold','short','smile')}
<g transform="translate(300 262)">
  <path d="M-72-58h144v116h-144z" class="gold o"/>
  <path d="M-72-58h144" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-14-10v-12a14 14 0 0 1 28 0v12" fill="none" stroke="{GLDD}" stroke-width="7"/>
  <path d="M-24-10h48v40h-48z" class="goldd o"/>
  <circle cy="8" r="6" fill="#fffefd"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('kilometer', '道に距離の目印が置かれた長い一本道のイラスト。', '1000メートルを表す距離の単位。', f"""
<path d="M20 400q140-150 560-170" fill="none" stroke="#dfe6ea" stroke-width="62" stroke-linecap="round"/>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="20 18">
  <path d="M20 400q140-150 560-170"/>
</g>
<g transform="translate(142 328)">
  <path d="M0 0v-76" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0-76h66v34H0z" class="goldp o"/>
</g>
<g transform="translate(424 274)">
  <path d="M0 0v-76" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0-76h66v34H0z" class="goldp o"/>
</g>
{person(296,296,0.8,1,'teal','blue','walk','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('kindness', '困っている人に食べものを差し出して助けるイラスト。', '相手を思いやるやさしさ、親切。', f"""
{person(160,352,1.15,1,'coral','blue','give','bob','smile')}
{person(410,352,1.05,-1,'teal','blue','reach','short','sad')}
<g transform="translate(286 236)">
  <path d="M-48-34h96v44a22 22 0 0 1-22 22h-52a22 22 0 0 1-22-22z" class="goldp o"/>
  <path d="M-48-34h96" fill="none" stroke="{INK}" stroke-width="5"/>
  <g class="gold o"><circle cx="-20" cy="-14" r="10"/><circle cx="8" cy="-12" r="9"/><circle cx="-6" cy="8" r="8"/></g>
</g>
{heart(300,128,0.8,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('kneel', '片ひざを床について低くかがむイラスト。', 'ひざを床について体を低くする、ひざまずく。', f"""
<g transform="translate(300 352) scale(1.25)">
  <path d="M-4-14l-26 14h-46" fill="none" stroke="{BLUD}" stroke-width="20" stroke-linecap="round"/>
  <path d="M-4-14l30-28 6 42" fill="none" stroke="{BLUD}" stroke-width="20" stroke-linecap="round"/>
  <path d="M-25-78q25-13 50 0l-8 66h-34z" fill="{TONES['teal'][0]}" class="o"/>
  <path d="M-22-70l-16 45M22-70l16 45" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="-108" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="{HAIRS['short']}" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <circle cx="-8" cy="-104" r="2.2" class="ink"/><circle cx="8" cy="-104" r="2.2" class="ink"/>
  <path d="M-7-92h14" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('know', '頭の中に電球がともっているイラスト。', '知っている、分かっている。', f"""
<g transform="translate(300 230)">
  <path d="M0-132q92 0 92 96 0 60-40 92v20h-104v-20q-40-32-40-92 0-96 92-96z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cy="-6" r="46" class="goldp o"/>
  <path d="M-18 34h36v14h-36zM-12 52h24v12h-24z" class="goldd o"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-62-10l-30-18M62-10l30-18M-56 30l-32 8M56 30l32 8"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('koala', '木の枝にだきつくようにして座るコアラのイラスト。', '木の上で暮らすオーストラリアの動物、コアラ。', f"""
<g fill="none" stroke="{BRN}" stroke-width="22" stroke-linecap="round"><path d="M20 186h560"/></g>
<g class="greenp o">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="30" ry="14" transform="rotate({r} {x} {y})"/>' for x, y, r in [(90,146,-24),(150,124,16),(470,132,-18),(546,158,20)])}</g>
<g transform="translate(300 186)">
  <path d="M-52-4q-6 44 34 48t34-48z" fill="#c3cbd1" class="o"/>
  <path d="M-58-40q0-56 58-56t58 56v6q0 42-58 42t-58-42z" fill="#c3cbd1" class="o"/>
  <circle cx="-70" cy="-96" r="38" fill="#c3cbd1" class="o"/>
  <circle cx="70" cy="-96" r="38" fill="#c3cbd1" class="o"/>
  <circle cx="-70" cy="-96" r="20" fill="#e6ded2"/>
  <circle cx="70" cy="-96" r="20" fill="#e6ded2"/>
  <circle cx="-32" cy="-72" r="9" class="ink"/><circle cx="32" cy="-72" r="9" class="ink"/>
  <ellipse cy="-36" rx="30" ry="21" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('lamp shade', '電灯のかさから光が広がるイラスト。', '電灯の光をやわらげる、ランプのかさ。', f"""
<g transform="translate(300 120)">
  <path d="M0-120V0" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-44 0h88l72 84H-116z" class="goldp o"/>
  <path d="M-116 84h232" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle cy="104" r="18" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M186 254l-40 34M300 300v44M414 254l40 34M198 190l-52-14M402 190l52-14"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('landslide', '山の斜面がくずれ、岩や土が下へ流れ落ちるイラスト。', '地面が崩れて土砂が落ちる、地すべり。', f"""
<path d="M0 340L136 30l176 310z" fill="#7f8f72" class="o"/>
<path d="M136 30q44 96 112 168-84-14-112-168z" fill="#5f6d55"/>
<path d="M0 340h600v60H0z" fill="#dfe6ea"/>
<g class="goldd o">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(214,148,26),(252,198,22),(280,250,30),(300,300,24)])}</g>
<g class="gold" opacity="0.55">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(190,120,14),(232,180,12),(262,232,16),(290,282,13),(318,322,12)])}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M118 92q112 96 178 224"/></g>
""", ground=False, arrow=True)

add('language', '違う模様の吹き出しで言葉を交わす二人のイラスト。', '人々が使う言葉そのもの、言語。', f"""
{person(160,352,1.15,1,'teal','blue','give','short','smile')}
{person(450,352,1.15,-1,'coral','blue','give','bob','smile')}
{bubble(130,140,0.8,'teal',1,'lines')}
{bubble(480,140,0.8,'coral',-1,'dots')}
""", ground=True)

add('large', '大きな木と小さな木を並べて大きさを示すイラスト。', '大きい、広い。', f"""
{tree(400,330,2.4)}
{tree(140,330,0.6)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"
   marker-start="url(#ar)" marker-end="url(#ar)"><path d="M300 330V186"/></g>
""", ground=True, arrow=True)

add('late', '時計を見ながら走って急いでいるイラスト。', '決めた時刻を過ぎている、遅れて。', f"""
{person(180,352,1.2,1,'coral','blue','walk','short','surprised')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"><path d="M40 250h56M28 296h48"/></g>
<g class="bluep o">{drop(270,178,1.2,'blue')}{drop(240,150,0.9,'blue')}</g>
{clock(452,140,64,7,25)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M396 66l-14-30M508 66l14-30M452 44v-30"/>
</g>
""", ground=True)

add('laugh', '口を大きく開け、涙をためて笑う顔のイラスト。', '声を出して笑う。', f"""
<g transform="translate(296 200)">
  <circle r="116" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="{HAIRS['short']}" transform="translate(0 522) scale(4.83)" fill="{HAIR}"/>
  <g fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round">
    <path d="M-74-28q22-26 44 0M30-28q22-26 44 0"/>
    <path d="M-30 48q30 26 60 0" stroke="{TONES['coral'][0]}" stroke-width="11"/>
  </g>
  <path d="M-58 32q58 72 116 0z" fill="{INK}"/>
  <g class="bluep o">
    <path d="M-98-12q-26 14-12 42 20 6 26-16z"/>
    <path d="M98-12q26 14 12 42-20 6-26-16z"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('laundrette', '洗濯機が並ぶコインランドリーの店内のイラスト。', 'コインを入れて使う共用の洗濯場。', f"""
<g transform="translate(300 250)">
  <path d="M-260-160h520v220h-520z" fill="#fffdf6" class="o"/>
  {''.join(f'<g transform="translate({-176+c*176} 0)"><path d="M-72-90h144v180h-144z" class="tealp o"/><circle cy="4" r="52" fill="#e1edfb" class="o"/><circle cy="4" r="32" fill="none" stroke="{INK}" stroke-width="4"/><circle cx="-44" cy="-62" r="11" class="gold o"/></g>' for c in range(3))}
</g>
{person(470,352,1.1,-1,'coral','blue','hold','bob','smile')}
{coin(548,332,22)}{coin(504,340,18)}
""", ground=True)

add('learn', '本を読みながら学んだことが積み上がっていくイラスト。', '知識や技術を身につける、学ぶ。', f"""
{person(170,352,1.15,1,'teal','blue','hold','short','smile')}
{book(258,282,0.7,'teal')}
<g transform="translate(470 356)">
  <path d="M-84 0h62v-52h-62zM-22-52h62v-52h-62zM40-104h62v-52h-62z" class="goldp o"/>
</g>
{spark(470,128,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('leg', 'ひざを丸で示した脚のイラスト。', '体を支えて歩くための脚。', f"""
<g transform="translate(300 30)">
  <path d="M-46 0h92v146h-92z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-38 126h76v176h-76z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cy="146" r="46" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-44 296h88q40 0 40 34t-40 34h-88z" fill="#fffdf6" class="o"/>
  <path d="M-44 330h168" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10">
  <circle cx="300" cy="176" r="82"/>
</g>
""", ground=False)

add('leggings', '脚にぴったりした細身のズボンをはいているイラスト。', '脚に沿うぴったりしたズボン、レギンス。', f"""
<g transform="translate(300 40)">
  <path d="M-84-24h168v58l-28 296h-58l-12-254-10 254h-58z" class="violet o"/>
  <path d="M-84-24h168v18h-168z" class="violetd o"/>
  <g fill="none" stroke="#5f4d91" stroke-width="4">
    <path d="M-74 6h148M-70 62h140"/>
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M204 100h-44M204 200h-44"/>
</g>
""", ground=False)

add('lesson', '黒板の前に立つ先生と席についた生徒のイラスト。', '先生が教えるひと区切りの授業。', f"""
<g transform="translate(330 160)">
  <path d="M-170-130h340v230h-340z" class="green o"/>
  <path d="M-140-100h150v40h-150z" fill="#e1f3e5" opacity="0.7"/>
  <path d="M-140-20h230v16h-230zM-140 26h170v16h-170z" fill="#e1f3e5" opacity="0.7"/>
  <path d="M-190 100l-22 130M190 100l22 130" fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round"/>
</g>
{person(150,352,1.15,1,'violet','blue','point','bun','smile')}
{chair(430,392,0.8,'gold',1)}
{sit(430,392,0.8,1,'teal','blue','short','neutral','lap')}
{chair(534,392,0.8,'gold',1)}
{sit(534,392,0.8,1,'coral','blue','bob','neutral','lap')}
""", ground=True)

add('let', 'さえぎるロープを持ち上げて相手を通してあげるイラスト。', '行かせてあげる、…させてあげる。', f"""
<g fill="none" stroke="{BRN}" stroke-width="12" stroke-linecap="round">
  <path d="M160 336V188M440 336V188"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="7" stroke-linecap="round">
  <path d="M160 194q-26 56 18 62M440 194q-42 12-48 44"/>
</g>
{person(300,352,1.1,1,'teal','blue','walk','short','smile')}
{person(506,352,1.15,-1,'coral','blue','up','bob','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M232 296h140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('letter', '封筒から手紙を取り出しているイラスト。', '人に送る手紙、または文字。', f"""
<g transform="translate(300 268)">
  <path d="M-160-92h320v184h-320z" class="paper"/>
  <path d="M-160-92l160 96 160-96" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-160 92l116-84M160 92l-116-84" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M96-92h58v46H96z" class="coral o"/>
  <g transform="translate(-6 -134)">
    <path d="M-118-72h236v150h-236z" class="paper"/>
    <g fill="none" stroke="{MUTED}" stroke-width="5">
      <path d="M-88-36h176M-88 0h176M-88 36h120"/>
    </g>
  </g>
</g>
{hand(148,332,-1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('library', '本棚に本が並び、人が読書している図書館のイラスト。', '本を集めて貸し出す施設、図書館。', f"""
<g transform="translate(400 300)">
  <path d="M-190-190h380v190h-380z" fill="#8b6437" class="o"/>
  <g>{''.join(f'<rect x="{-170+c*28}" y="{-176+r*62}" width="20" height="48" rx="3" class="{["teal","coral","gold","green","violet","blue"][(r*6+c)%6]}"/>' for r in range(3) for c in range(13))}</g>
  <g fill="none" stroke="#6b4a2a" stroke-width="8"><path d="M-190-126h380M-190-64h380"/></g>
</g>
{chair(160,372,0.85,'gold',1)}
{sit(160,372,0.85,1,'violet','blue','bob','smile','lap')}
{book(242,300,0.6,'coral')}
""", ground=True)

add('lick', '舌を出してアイスクリームをなめているイラスト。', '舌でなめる。', f"""
{face(288,150,90,'grin')}
<g transform="translate(302 300)">
  <circle cy="-50" r="50" class="coral o"/>
  <circle cx="-18" cy="-64" r="20" fill="#fffdf6" opacity="0.35"/>
  <path d="M-50-4h100l-50 94z" class="gold o"/>
  <path d="M-32 4h64l-32 60z" fill="{GLDD}"/>
</g>
<g transform="translate(292 188) rotate(26)">
  <path d="M-22 0q-4 44 22 44t22-44z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('life', '幼い頃から年を重ねて人生の道を歩んでいくイラスト。', '人が生きていること、一生の歩み。', f"""
<path d="M90 356q120-40 200-30t220-160" fill="none" stroke="#e8e2d8" stroke-width="56" stroke-linecap="round"/>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="16 12">
  <path d="M90 356q120-40 200-30t220-160"/>
</g>
<g transform="translate(104 350) scale(0.42)">{person(0,0,1,1,'gold','blue','stand','short','smile')}</g>
<g transform="translate(238 320) scale(0.62)">{person(0,0,1,1,'teal','blue','walk','short','smile')}</g>
<g transform="translate(388 262) scale(0.85)">{person(0,0,1,1,'coral','blue','walk','bob','smile')}</g>
<g transform="translate(506 172) scale(1)">{person(0,0,1,1,'violet','violet','stand','bun','neutral')}</g>
<path d="M548 146v28q0 8-10 8" fill="none" stroke="{BRN}" stroke-width="9" stroke-linecap="round"/>
""", ground=True)

add('light switch', '壁のスイッチを入れて電灯がつくイラスト。', '部屋の電灯を入り切りするスイッチ。', f"""
<g transform="translate(150 210)">
  <path d="M-72-96h144v192h-144z" class="paper"/>
  <path d="M-32-44h64v88h-64z" class="tealp o"/>
  <path d="M-22-32h44v26h-44z" class="teal o"/>
</g>
{hand(250,206,-1)}
<g transform="translate(456 150)">
  <path d="M0-56v-40" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-84 0h168l-28 62h-112z" class="goldp o"/>
  <circle cy="84" r="20" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M330 236l-34 20M456 288v38M566 236l30 18"/>
</g>
""", ground=False)

add('list', '紙に項目が上から順に並んだ一覧のイラスト。', '順に並べた項目、リスト。', f"""
<g transform="translate(300 210)">
  <path d="M-124-160h248v320h-248z" class="paper"/>
  <path d="M-46-178h92v30h-92z" fill="{MUTED}" class="o"/>
  <g class="gold o">{''.join(f'<rect x="-92" y="{-126+i*46}" width="24" height="24" rx="5"/>' for i in range(6))}</g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
    {''.join(f'<path d="M-86 {-114+i*46}l9 11 17-22"/>' for i in range(4))}
  </g>
  <g fill="{MUTED}">{''.join(f'<rect x="-46" y="{-120+i*46}" width="{130-(i%3)*26}" height="12" rx="6"/>' for i in range(6))}</g>
</g>
""", ground=False)

add('listen', '耳をそばだててラジオの音に聞き入るイラスト。', '注意して耳を傾ける。', f"""
{person(230,352,1.2,1,'violet','blue','think','bob','neutral')}
<g transform="translate(448 268)">
  <path d="M-96-62h192v120h-192z" class="goldd o"/>
  <circle cx="-44" cy="16" r="32" fill="#fffdf6" class="o"/>
  <circle cx="-44" cy="16" r="12" fill="{MUTED}"/>
  <g fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"><path d="M20-30h56M20 10h56"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-96-66l-30-58M96-66l30-58"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M336 208a50 50 0 0 0 0 76M308 184a78 78 0 0 0 0 124"/>
</g>
""", ground=True)

add('live on', '毎日お米を主食にして食べているイラスト。', '…を主食にしてそれで暮らす。', f"""
{person(190,352,1.15,1,'teal','blue','hold','short','smile')}
<g transform="translate(420 326)">
  <path d="M-86-30q0 46 86 46t86-46z" class="bluep o"/>
  <ellipse cy="-30" rx="86" ry="24" fill="#fffdf6" class="o"/>
  <g class="goldp o">{''.join(f'<ellipse cx="{-44+c*30}" cy="{-38+(c%3)*8}" rx="13" ry="9"/>' for c in range(4))}</g>
</g>
<g fill="none" stroke="{GLDD}" stroke-width="5" stroke-linecap="round" stroke-dasharray="14 10"
   marker-end="url(#ar)"><path d="M300 186a132 132 0 0 1 106 128"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('loafers', 'ひもなしの革靴が二足並べられているイラスト。', 'ひもを結ばずに履く革靴、ローファー。', f"""
<g transform="translate(190 300)">
  <path d="M-92 0q0-44 34-48h62q42 4 42 32 0 16-26 16h-112z" class="coral o"/>
  <path d="M-90 0h180v20h-180z" fill="#8f6444" class="o"/>
  <path d="M-52-40h56v9h-56z" fill="{INK}"/>
</g>
<g transform="translate(410 300)">
  <path d="M-92 0q0-44 34-48h62q42 4 42 32 0 16-26 16h-112z" class="coral o"/>
  <path d="M-90 0h180v20h-180z" fill="#8f6444" class="o"/>
  <path d="M-52-40h56v9h-56z" fill="{INK}"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('lockers', 'かぎのかかったロッカーが並び、一つが開いているイラスト。', 'かぎをかけて荷物を保管するロッカー。', f"""
<g transform="translate(380 320)">
  <path d="M-190-220h380v220h-380z" class="teald o"/>
  <g fill="none" stroke="{INK}" stroke-width="4">
    <path d="M-114-220v220M-38-220v220M38-220v220M114-220v220"/>
  </g>
  <g>{''.join(f'<circle cx="{-152+c*76}" cy="-172" r="11" class="ink"/>' for c in range(5))}</g>
  <g fill="none" stroke="{INK}" stroke-width="5">
    {''.join(f'<path d="M{-172+c*76} -140h40"/>' for c in range(5))}
  </g>
</g>
<g transform="translate(190 320)">
  <path d="M0-220l-104 26v196l104-24z" class="tealp o"/>
  <path d="M-14-58h40v40h-40z" fill="{MUTED}"/>
</g>
{key(300,352,0.9,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('long', '長くのびたロープと短いロープを並べたイラスト。', '端から端までのへだたりが大きい、長い。', f"""
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" stroke-linecap="round">
  <path d="M60 204q130-26 240 0t240 0"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round">
  <path d="M60 324q50-14 110 0"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round"
   marker-start="url(#ar)" marker-end="url(#ar)"><path d="M60 130h480M60 372h110"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 8">
  <path d="M60 140v60M540 140v60M170 372v-44"/>
</g>
""", ground=True, arrow=True)

add('look for', '虫めがねで荷物の山をのぞいて探すイラスト。', '見つけようとして捜す。', f"""
<g transform="translate(180 300)">
  <path d="M-96-46h192v70H-96z" class="goldd o"/>
  <path d="M-96-46l34-32h192l-34 32z" class="gold o"/>
  <g class="gold o"><circle cx="-32" cy="-14" r="18"/><circle cx="30" cy="-10" r="15"/></g>
</g>
<g transform="translate(430 190)">
  <circle r="74" fill="#e1edfb" opacity="0.65" class="o"/>
  <path d="M54 54l58 58" fill="none" stroke="{BRN}" stroke-width="20" stroke-linecap="round"/>
</g>
{person(300,352,1.05,1,'teal','blue','reach','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 9">
  <path d="M322 240q60-40 116-14"/>
</g>
""", ground=True)

add('lose', '歩いていて小銭を落とし、それに気づかず行ってしまうイラスト。', '持っていたものをなくす、失う。', f"""
{person(400,352,1.2,1,'teal','blue','walk','short','sad')}
<g transform="translate(160 356)">
  <circle r="30" class="gold o"/>
  <circle r="16" fill="none" stroke="{GLDD}" stroke-width="3"/>
</g>
{coin(238,378,16)}{coin(200,386,13)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9">
  <path d="M368 292q-90 42-176 54"/>
</g>
""", ground=True)

add('lost property', '忘れ物の品に札がつけられて並べられているイラスト。', '落とし物や忘れ物を預かる場所とその品。', f"""
<g transform="translate(300 340)">
  <path d="M-240-70h480v70h-480z" class="goldd o"/>
  <path d="M-240-70h480v14h-480z" class="gold o"/>
</g>
<g transform="translate(140 276)">
  <path d="M0 64V-24" fill="none" stroke="{MUTED}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0-24q0-52 46-52t46 52z" class="coral o"/>
</g>
<g transform="translate(292 250)">
  <path d="M-56 26q0-30 56-30t56 30z" class="teal o"/>
  <path d="M-66 26h132v12h-132z" class="teald o"/>
</g>
<g transform="translate(444 262)">
  <path d="M-58 44v-70h116v70z" class="violet o"/>
  <path d="M-26-26v-18h52v18" fill="none" stroke="#5f4d91" stroke-width="8"/>
</g>
{key(500,326,0.6,'gold')}
<g class="paper">{''.join(f'<rect x="{228+c*150}" y="272" width="32" height="22" rx="3"/>' for c in range(3))}</g>
""", ground=True)

add('lot', '果物が山のようにたくさん積み上げられているイラスト。', '数量がとても多いこと、たくさん。', f"""
<g class="coral o">{''.join(f'<circle cx="{300+(c-(7-r)/2)*62}" cy="{344-r*54}" r="31"/>' for r in range(5) for c in range(8-r))}</g>
<g class="gold o">{''.join(f'<circle cx="{300+(c-1.5)*54}" cy="{86-r*42}" r="17"/>' for r in range(2) for c in range(4))}</g>
""", ground=False)

add('lotion', 'ボトルから化粧水を手のひらに出しているイラスト。', '肌につける化粧水、乳液。', f"""
<g transform="translate(190 140) rotate(150)">
  <path d="M-52-46h104v152h-104z" fill="#fffdf6" class="o"/>
  <path d="M-52 36h104v70h-104z" class="coralp"/>
  <path d="M-30-46v-28h60v28z" class="coral o"/>
  <path d="M-14-74h28v-26h-28z" class="coral o"/>
  <path d="M-30 36h60v24h-60z" class="coral"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M244 234v36M244 290v34"/>
</g>
{hand(250,336,-1)}
<g transform="translate(300 340)"><ellipse rx="38" ry="13" class="coralp"/></g>
""", ground=True)

add('love', '二人の間に大きなハートが浮かんでいるイラスト。', '大切に思う気持ち、愛すること。', f"""
{person(140,352,1.1,1,'coral','blue','give','bob','smile')}
{person(460,352,1.1,-1,'violet','blue','give','short','smile')}
{heart(300,232,1.55,'coral')}
{spark(300,88,1.2,'gold')}
""", ground=True)

add('lunchbox', 'ふたを開けた弁当箱におかずとごはんがつまっているイラスト。', '食事を入れて持ち歩く箱、弁当箱。', f"""
<g transform="translate(300 300)">
  <path d="M-200-70h400v120a16 16 0 0 1-16 16h-368a16 16 0 0 1-16-16z" class="bluep o"/>
  <path d="M-200-70h400" fill="none" stroke="{INK}" stroke-width="5"/>
  <g fill="none" stroke="#315f98" stroke-width="4"><path d="M-72-70v120M72-70v120M-136-24h272"/></g>
  <g class="teal o"><circle cx="-136" cy="-34" r="28"/><circle cx="-136" cy="26" r="22"/><circle cx="136" cy="-30" r="24"/></g>
  <g class="gold o">{''.join(f'<rect x="{-58+c*38}" y="{-50+r*42}" width="30" height="26" rx="7"/>' for r in range(2) for c in range(3))}</g>
  <g class="coral o"><circle cx="-6" cy="40" r="20"/><circle cx="60" cy="32" r="15"/></g>
  <path d="M-200-70h400l34-44h-468z" class="bluep o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('machine', '歯車のついた機械が製品を送り出すイラスト。', '動力で動く装置、機械。', f"""
<g transform="translate(300 250)">
  <path d="M-200-130h400v170h-400z" class="teal o"/>
  <g transform="translate(-110 -46)">{gear(0,0,54,'gold',9)}</g>
  <g transform="translate(20 -46)">{gear(0,0,40,'violet',8)}</g>
  <g transform="translate(132 -46)">{gear(0,0,32,'coral',7)}</g>
  <path d="M-200 40h400" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g transform="translate(300 120) rotate(-40)">
  <path d="M0 0h116" fill="none" stroke="{MUTED}" stroke-width="13" stroke-linecap="round"/>
  <circle cx="126" cy="0" r="17" class="coral o"/>
</g>
<g transform="translate(300 320)">
  <path d="M-190 0h380v26h-380z" class="goldd o"/>
  <g class="gold o">{''.join(f'<rect x="{-160+c*66}" y="-34" width="42" height="34" rx="6"/>' for c in range(5))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('magazine', 'カラフルな表紙の雑誌が何冊か重なっているイラスト。', '記事や写真を載せた定期刊行の読みもの、雑誌。', f"""
<g transform="translate(300 320) rotate(-8)"><path d="M-124-156h248v186h-248z" class="violetp o"/></g>
<g transform="translate(300 314) rotate(-3)"><path d="M-124-156h248v186h-248z" class="goldp o"/></g>
<g transform="translate(300 308)">
  <path d="M-124-156h248v186h-248z" class="paper"/>
  <path d="M-106-138h212v104h-212z" class="tealp o"/>
  <circle cx="-40" cy="-92" r="26" class="gold o"/>
  <path d="M-106-40q60-56 212-16v22h-212z" class="greenp"/>
  <g fill="{MUTED}">{''.join(f'<rect x="-106" y="{-14+i*24}" width="{152-(i%3)*44}" height="11" rx="5"/>' for i in range(3))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

finish(__file__)
