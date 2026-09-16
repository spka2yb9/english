# -*- coding: utf-8 -*-
"""第198回: plus46(s〜t)の100語。"""
from kit import *


# --- この回で使う小物 --------------------------------------------------------

def bundle(x, y, s=1, cls='gold'):
    """10本を帯でたばねたもの。数を表すのに使う。"""
    st = ''.join(f'<path d="M{-36+i*8} 36l8 -70" fill="none" stroke="{TONES[cls][2]}" '
                 f'stroke-width="7" stroke-linecap="round"/>' for i in range(10))
    return (f'<g transform="translate({x} {y}) scale({s})">{st}'
            f'<path d="M-52-12h104v12H-52zM-52 12h104v12H-52z" class="coral o"/></g>')


def ball(x, y, r=40, cls='gold'):
    return f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls} o"/>'


def heart(x, y, s=1, cls='coral'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0C-38-26-46-52-26-62-8-70 0-56 0-44 0-56 8-70 26-62 46-52 38-26 0 0Z" '
            f'class="{cls} o"/></g>')


def note(x, y, s=1, cls='violet'):
    """音符。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse rx="13" ry="10" transform="rotate(-18)" class="{cls} o"/>'
            f'<path d="M10-2v-38h5v38z" class="{cls}"/>'
            f'<path d="M15-40q24 6 26 26" fill="none" stroke="{TONES[cls][0]}" '
            f'stroke-width="6" stroke-linecap="round"/></g>')


def bubble(x, y, s=1, cls='blue', lines=3):
    """せりふの吹き出し。"""
    g = [f'<g transform="translate({x} {y}) scale({s})">',
         f'<path d="M-56-52h112a14 14 0 0 1 14 14v54a14 14 0 0 1-14 14H-12l-32 34 6-34H-56'
         f'a14 14 0 0 1-14-14v-54a14 14 0 0 1 14-14z" class="{cls}p o"/>']
    g.append(''.join(f'<rect x="-38" y="{-28+i*24}" width="{76-(i%3)*20}" height="11" rx="5" '
                     f'fill="{TONES[cls][0]}"/>' for i in range(lines)))
    g.append('</g>')
    return ''.join(g)


def cup(x, y, s=1, cls='teal', steam=True):
    """カップと受け皿。(x,y)は受け皿の中心。"""
    g = [f'<g transform="translate({x} {y}) scale({s})">',
         f'<ellipse cy="28" rx="54" ry="10" fill="#fffefd" class="o"/>',
         f'<path d="M-40-36h80l-11 58a10 10 0 0 1-10 8h-38a10 10 0 0 1-10-8z" class="{cls}p o"/>',
         f'<path d="M40-22h14a20 20 0 0 1 0 36H32" fill="none" stroke="{TONES[cls][0]}" stroke-width="7"/>',
         f'<path d="M-46-36h92v10h-92z" class="{cls}d o"/>']
    if steam:
        g.append(f'<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">'
                 f'<path d="M-16-64q-14-18 0-34t0-34M18-64q-14-18 0-34t0-34"/></g>')
    g.append('</g>')
    return ''.join(g)


def sneaker(x, y, s=1, cls='blue', f=1):
    """横から見たスニーカー。(x,y)は靴底。"""
    return (f'<g transform="translate({x} {y}) scale({s*f} {s})">'
            f'<path d="M-74 6q-2-20 20-22l114-2q28-4 28 24z" fill="#fffefd" class="o"/>'
            f'<path d="M-54-16q-6-46 20-48 22-2 30 14l56 32z" class="{cls} o"/>'
            f'<path d="M-56-16h-16v-26h16z" class="{cls}d o"/>'
            f'<g fill="none" stroke="{INK}" stroke-width="3">'
            f'<path d="M-32-42l30 12M-34-30l32 14M-36-18l34 16"/></g>'
            f'<circle cx="-20" cy="-34" r="3" class="ink"/>'
            f'<circle cx="-22" cy="-24" r="3" class="ink"/></g>')


def sled(x, y, s=1, cls='gold'):
    """木のそり。(x,y)は滑走面。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-104 22h72q18 0 18-18v-32" fill="none" stroke="{STONE}" '
            f'stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-104 22q-22-4-14-24" fill="none" stroke="{STONE}" '
            f'stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-116-18h236v14h-236z" class="{cls} o"/>'
            f'<path d="M-84-4v24M84-4v24" fill="none" stroke="{TONES[cls][2]}" stroke-width="8"/>'
            f'</g>')


def phone(x, y, s=1, cls='blue'):
    """台の上に置いた電話機。"""
    keys = ''.join(f'<rect x="{-58+c*36}" y="{-6+r*20}" width="22" height="14" rx="4"/>'
                   for r in range(3) for c in range(4))
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-116-16h232v72a12 12 0 0 1-12 12h-208a12 12 0 0 1-12-12z" class="{cls} o"/>'
            f'<g class="{cls}p o">{keys}</g>'
            f'<ellipse cx="-118" cy="-46" rx="24" ry="28" class="ink"/>'
            f'<ellipse cx="118" cy="-46" rx="24" ry="28" class="ink"/>'
            f'<path d="M-118-58h236v14a14 14 0 0 1-14 14h-208a14 14 0 0 1-14-14z" class="ink"/>'
            f'<g fill="none" stroke="{TONES[cls][0]}" stroke-width="5" stroke-linecap="round">'
            f'<path d="M-150 24q-18 14 0 28t0 28"/><path d="M-150 80q-18 14 0 28t0 24"/></g></g>')


def tv(x, y, s=1):
    """アンテナのついたテレビ。画面には山と太陽。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-36-116l-46-60M36-116l46-60" fill="none" stroke="{STONE}" '
            f'stroke-width="8" stroke-linecap="round"/>'
            f'<circle cx="-86" cy="-182" r="9" class="coral"/>'
            f'<circle cx="86" cy="-182" r="9" class="coral"/>'
            f'<path d="M-196-116h392v236h-392z" class="ink"/>'
            f'<rect x="-172" y="-94" width="344" height="192" fill="#dff4ef"/>'
            f'<circle cx="-64" cy="-42" r="26" class="gold"/>'
            f'<path d="M-172 98l96-96 68 72 62-54 118 78z" class="greenp"/>'
            f'<path d="M-40 120v26M40 120v26M-124 146h248" fill="none" stroke="{INK}" '
            f'stroke-width="9" stroke-linecap="round"/></g>')


def compass(x, y, r=104):
    """方位磁針。針は南(下)を指す。"""
    ticks = ''.join(f'<path d="M0 {-r}v-14" transform="rotate({a})" fill="none" '
                    f'stroke="{MUTED}" stroke-width="4"/>' for a in range(0, 360, 45))
    return (f'<g transform="translate({x} {y})">'
            f'<circle r="{r}" fill="#fffefd" class="o"/>'
            f'<circle r="{r*0.82:.0f}" fill="none" stroke="{MUTED}" stroke-width="2"/>'
            f'{ticks}'
            f'<path d="M0 {r*0.8:.0f}L{r*0.2:.0f} 0 0 -{r*0.6:.0f}L-{r*0.2:.0f} 0z" class="coral o"/>'
            f'<circle r="9" class="ink"/></g>')


def ticket(x, y, s=1, cls='gold'):
    """切り取り線のあるチケット。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-150-70h300v140h-300z" class="{cls}p o"/>'
            f'<circle cx="-150" cy="0" r="14" fill="#fffaf1" class="o"/>'
            f'<circle cx="150" cy="0" r="14" fill="#fffaf1" class="o"/>'
            f'<path d="M60-70v140" fill="none" stroke="{MUTED}" stroke-width="4" '
            f'stroke-dasharray="10 9"/>'
            f'<path d="M-118-32h140M-118 2h112M-118 36h130" fill="none" '
            f'stroke="{TONES[cls][2]}" stroke-width="8" stroke-linecap="round"/>'
            f'{spark(110,0,1.1)}</g>')


def can(x, y, s=1, cls='blue'):
    """ラベルのついた缶。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-74-96h148v170h-148z" class="{cls}p o"/>'
            f'<ellipse cy="74" rx="74" ry="24" class="{cls}p o"/>'
            f'<path d="M-74-54h148v58h-148z" class="coral"/>'
            f'<ellipse cy="-96" rx="74" ry="24" fill="#fffefd" class="o"/></g>')


def car(x, y, s=1, cls='gold', roof=False):
    """横から見た車。roof=True で屋根に標識がつく。"""
    g = [f'<g transform="translate({x} {y}) scale({s})">',
         f'<path d="M-180 0v-56q0-16 16-16h34l34-52h120l30 52h30q16 0 16 16v56z" class="{cls} o"/>',
         f'<path d="M-104-72l24-38h54v38z" fill="#fffdf6" class="o"/>',
         f'<path d="M-14-72v-38h52l24 38z" fill="#fffdf6" class="o"/>']
    if roof:
        g.append('<path d="M-36-136h72v26h-72z" class="coral o"/>')
    g.append(f'<circle cx="-108" cy="4" r="30" fill="#3a3f45" class="o"/>'
             f'<circle cx="108" cy="4" r="30" fill="#3a3f45" class="o"/>'
             f'<circle cx="-108" cy="4" r="11" fill="#8f9aa3"/>'
             f'<circle cx="108" cy="4" r="11" fill="#8f9aa3"/></g>')
    return ''.join(g)


def pbox(x, y, w=84, h=66, d=22):
    """白い箱。lib.box() に paper 系のクラスがないので自前で描く。"""
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M{-w/2} {-h/2}h{w}v{h}h{-w}z" fill="#f7f4ed" class="o"/>'
            f'<path d="M{-w/2} {-h/2}l{d} {-d}h{w}l{-d} {d}z" fill="#fdfcf8" class="o"/>'
            f'<path d="M{w/2} {-h/2}l{d} {-d}v{h}l{-d} {d}z" fill="#e7e1d5" class="o"/></g>')


def star6(x, y, r=34, cls='blue'):
    """ダビデの星(六芒星)。"""
    return (f'<g transform="translate({x} {y})">'
            f'<path d="M0-{r}L{r*0.87:.0f} {r*0.5:.0f}H-{r*0.87:.0f}z" class="{cls} o"/>'
            f'<path d="M0 {r}L-{r*0.87:.0f}-{r*0.5:.0f}H{r*0.87:.0f}z" class="{cls}d o"/></g>')


def bulb(x, y, s=1):
    """電球。ひらめき・考えを表す。"""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<circle cy="-26" r="34" class="goldp o"/>'
            f'<path d="M-14 6h28v16h-28z" class="goldd o"/>'
            f'<path d="M-10 22h20v10h-20z" class="ink"/>'
            f'<g fill="none" stroke="{GLDD}" stroke-width="4">'
            f'<path d="M-12-32q14 12 0 24M12-32q-14 12 0 24M0-10v-40"/></g>'
            f'<g fill="none" stroke="{GLD}" stroke-width="5" stroke-linecap="round">'
            f'<path d="M-52-52l-16-16M52-52l16-16M0-72v-20"/></g></g>')


# --- s ----------------------------------------------------------------------

add('show', '写真の入った大きな紙を相手に向けて差し出しているイラスト。', '見せる、示す。番組やショーの意味もある。', f"""
{person(150,352,1.2,1,'teal','blue','give','short','smile')}
{person(478,352,1.15,-1,'violet','blue','reach','bob','smile')}
<g transform="translate(322 216) rotate(-6)">
  <path d="M-96-70h192v140h-192z" class="paper"/>
  <path d="M-78-52h156v104h-156z" class="tealp o"/>
  <circle cx="-20" cy="-18" r="22" class="goldp o"/>
  <path d="M-78 52l52-42 44 34 60-46v54z" class="greenp"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('shower', '頭の上のシャワーから湯が降りそそぎ、湯気が立っているイラスト。', 'シャワー、にわか雨。take a shower で「シャワーを浴びる」。', f"""
{person(300,352,1.15,1,'gold','blue','stand','bob','smile')}
<path d="M60 56h150q22 0 22 22v36" fill="none" stroke="{STONE}" stroke-width="11"
      stroke-linecap="round"/>
<g transform="translate(232 118)">
  <path d="M-54-8h108l-18 28h-72z" class="blue o"/>
  <g fill="{TONES['blue'][2]}">{''.join(f'<circle cx="{-30+i*20}" cy="26" r="4"/>' for i in range(4))}</g>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round"
   stroke-dasharray="16 12">
  <path d="M206 150v76M246 154v88M286 156v92M326 154v88M366 148v74"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M150 254q-14-16 0-32t0-30M452 254q14-16 0-32t0-30"/>
</g>
<ellipse cx="300" cy="376" rx="120" ry="14" class="bluep o"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sick', 'いすに座って体温計をくわえ、具合が悪そうなイラスト。', '病気の、気分が悪い。', f"""
{chair(210,352,1.25,'gold')}
{sit(210,352,1.2,1,'violet','blue','short','sad','down')}
<g transform="translate(238 246) rotate(-52) scale(0.55)">{thermometer(0,0,0.95,1)}</g>
<path d="M186 300h150l-14 52h-122z" class="bluep o"/>
<g transform="translate(452 344)">
  <path d="M-46-42h92v42h-92z" class="bluep o"/>
  <path d="M-14-42q14-28 28 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sightsee', 'カメラを構えて、遠くの塔を写真に撮っているイラスト。', '観光する、見物して回る。', f"""
{person(180,352,1.25,1,'coral','blue','hold','bob','smile')}
<g transform="translate(262 236)">
  <path d="M-42-26h84v52h-84z" class="ink"/>
  <circle cx="0" cy="0" r="17" class="bluep o"/>
  <path d="M-16-26v-10h32v10z" class="ink"/>
</g>
<path d="M300 214q60-30 120-26" fill="none" stroke="{MUTED}" stroke-width="4"
      stroke-dasharray="10 9"/>
{tower(470,352,1.0,'teal',5)}
{spark(400,140,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sing', '口を大きく開けて歌い、音符が浮かんでいるイラスト。', '歌う。', f"""
{person(250,352,1.25,1,'violet','blue','hold','bob','surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M336 236a44 44 0 0 1 0 60M366 210a80 80 0 0 1 0 112"/>
</g>
{note(452,180,1.2,'teal')}{note(510,246,0.9,'gold')}{note(430,110,1.0,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sister', '背の違う二人の女の子が並んで立っているイラスト。', '姉、妹。', f"""
{person(222,352,1.30,1,'coral','blue','stand','bob','smile')}
{person(400,352,1.02,1,'violet','gold','stand','bob','smile')}
<path d="M330 120v244" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"/>
<path d="M300 122h60M300 154h60" fill="none" stroke="{MUTED}" stroke-width="3"/>
{heart(320,190,0.78,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sit', 'いすに腰かけて足もとに手を置いているイラスト。', '座る、位置する。', f"""
{chair(300,352,1.4,'gold')}
{sit(300,352,1.35,1,'teal','blue','short','smile','lap')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sit down', 'いすの真上から下向きの矢印で、腰を下ろす動きを示すイラスト。', '座る、腰を下ろす(sit down)。', f"""
{chair(300,352,1.35,'gold')}
{sit(300,352,1.3,1,'coral','blue','short','smile','lap')}
{arrowline([(300,120),(300,222)], MUTED, 6, True)}
<path d="M180 296h240" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"
      stroke-dasharray="10 9"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('six', '金のボールが2列に3つずつ、6つ並んでいるイラスト。', '6、六。', f"""
{''.join(ball(195 + c*105, 200 + r*84, 40) for r in range(2) for c in range(3))}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sixteen', '10本をたばねた束と、ボール6つを並べて示したイラスト。', '16、十六。10と6を合わせた数。', f"""
{bundle(160,224,1.05,'gold')}
{''.join(ball(330 + c*86, 190 + r*76, 32) for r in range(2) for c in range(3))}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sixth', '6つ並んだボールのうち、6番目だけが輪で示されているイラスト。', '6番目の。', f"""
{''.join(ball(150 + i*60, 258, 24) for i in range(6))}
{ring(450,258,46,False,'coral')}
{spark(450,180,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sixty', '10本の束が6つ、2列に並んでいるイラスト。', '60、六十。', f"""
{''.join(bundle(140 + c*160, 180 + r*124, 0.85, 'gold') for r in range(2) for c in range(3))}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sketchbook', '開いたスケッチブックに木の下絵が描かれ、そばに鉛筆が置かれているイラスト。', 'スケッチブック、写生帳。', f"""
<g transform="translate(280 236) rotate(-4)">
  <path d="M-140-100h280v200h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
    <path d="M-40 60v-66"/>
    <path d="M-40-6q-42 0-42-40t42-40 42 40-42 40z"/>
    <path d="M-104-64q50-22 96 4"/>
  </g>
  <g fill="{STONE}">{''.join(f'<rect x="-152" y="{-88+i*24}" width="18" height="10" rx="5"/>' for i in range(8))}</g>
</g>
<g transform="translate(430 340) rotate(-18)">
  <path d="M-84-11h140v22h-140z" class="gold o"/>
  <path d="M56-11l30 11-30 11z" class="goldp o"/>
  <path d="M78-4l10 4-10 4z" class="ink"/>
  <path d="M-84-11h-18v22h18z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('skirt', 'スカートをはいた人が立っているイラスト。', 'スカート。', f"""
{person(300,352,1.3,1,'teal','blue','stand','bob','smile')}
<path d="M262 296h76l40 56h-156z" class="violet o"/>
<path d="M262 296h76v10h-76z" class="violetd o"/>
{ring(300,320,96,True)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sled', '雪の坂を木のそりで滑り降りるイラスト。', 'そり。', f"""
<path d="M0 160L600 320v80H0z" fill="#f6fafd"/>
<path d="M0 160L600 320" fill="none" stroke="{BLUD}" stroke-width="5"/>
<g transform="translate(340 262) rotate(15)">
  {sled(0,0,0.9,'gold')}
  {sit(0,-12,0.8,1,'coral','blue','short','smile','lap')}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" stroke-dasharray="10 9">
  <path d="M120 172q40 26 70 62"/>
</g>
<g fill="#fffefd" class="o">
  <circle cx="180" cy="230" r="9"/><circle cx="210" cy="256" r="7"/><circle cx="228" cy="288" r="8"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('small', '大きな家のとなりに小さな家が並び、小さい方が輪で囲まれているイラスト。', '小さい、少ない。', f"""
{house(430,352,1.05,'coral')}
{house(160,352,0.45,'blue')}
<ellipse cx="160" cy="316" rx="76" ry="58" fill="none" stroke="{TONES['coral'][0]}"
         stroke-width="4" stroke-dasharray="12 10"/>
{spark(92,262,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sneakers', 'スニーカーが一足、床に並べて置かれているイラスト。', 'スニーカー、運動靴。', f"""
{sneaker(240,344,1.0,'blue',1)}
{sneaker(430,334,0.92,'coral',1)}
{spark(330,180,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('snow', '雪が降りつづけ、家と木の上に積もっているイラスト。', '雪、雪が降る。', f"""
{house(210,352,0.85,'teal')}
{tree(450,352,1.0)}
<path d="M110 292q40-34 90-6 46-26 96 6z" fill="#fffefd"/>
<g fill="#fffefd" class="o">
  <circle cx="90" cy="90" r="8"/><circle cx="190" cy="60" r="7"/><circle cx="300" cy="96" r="9"/>
  <circle cx="410" cy="66" r="7"/><circle cx="510" cy="110" r="8"/><circle cx="240" cy="170" r="7"/>
  <circle cx="360" cy="180" r="8"/><circle cx="120" cy="210" r="7"/><circle cx="470" cy="220" r="7"/>
</g>
<path d="M40 340q120-24 240 0t280 0" fill="none" stroke="#dfeaf4" stroke-width="8"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('snowboarding', 'スノーボードの板に乗って雪の斜面を滑っているイラスト。', 'スノーボード。', f"""
<path d="M0 170L600 330v70H0z" fill="#f6fafd"/>
<path d="M0 170L600 330" fill="none" stroke="{BLUD}" stroke-width="5"/>
<g transform="translate(330 250) rotate(15)">
  <path d="M-140 26h280a14 14 0 0 1-14 22H-126a14 14 0 0 1-14-22z" class="violet o"/>
  {person(0,26,0.95,1,'gold','blue','stand','cap','smile')}
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round" stroke-dasharray="10 9">
  <path d="M100 190q44 30 74 64"/>
</g>
<g fill="#fffefd" class="o">
  <circle cx="160" cy="240" r="9"/><circle cx="192" cy="270" r="7"/><circle cx="214" cy="302" r="8"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('so', '燃えるように暑い太陽の下で、うちわで扇いで汗をぬぐうイラスト。', 'とても、そんなに。程度を強める語。「だから」と結果を導く用法もある。', f"""
{sun(470,110,56)}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M96 300q-16-18 0-34t0-32M154 306q-16-18 0-34t0-32"/>
</g>
{person(250,352,1.3,1,'teal','blue','up','short','surprised')}
<g transform="translate(376 220) rotate(-28)">
  <path d="M0 0v86" fill="none" stroke="{BRN}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="-52" r="52" class="goldp o"/>
  <path d="M-52-52h104M-36-88v72M-20-100v96" fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"/>
</g>
<g class="blue">{drop(180,222,0.9)}{drop(140,270,0.7)}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('some', 'かごの中のクッキーをいくつか手に取っているイラスト。', 'いくつかの、少しの。全部ではなく一部を指す。', f"""
<g transform="translate(280 320)">
  <path d="M-120-30h240l-30 76h-180z" class="gold o"/>
  <path d="M-140-40h280v16h-280z" class="goldd o"/>
</g>
<g class="gold o">
  {''.join(f'<circle cx="{-84+i*56}" cy="286" r="22"/>' for i in range(4))}
</g>
{hand(452,232,-1)}
<g class="gold o">
  <circle cx="386" cy="184" r="24"/><circle cx="434" cy="172" r="24"/><circle cx="392" cy="138" r="24"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('somebody', 'ドアの前に立ってノックしている、正体の分からない人の影のイラスト。', 'だれか。正体が分からない一人を指す語。', f"""
<g fill="{MUTED}">
  <circle cx="244" cy="168" r="42"/>
  <path d="M244 214q-76 12-80 138h160q-4-126-80-138z"/>
</g>
<ellipse cx="244" cy="252" rx="104" ry="132" fill="none" stroke="{CRL}" stroke-width="4"
         stroke-dasharray="14 11"/>
<g transform="translate(436 236)">
  <path d="M-96-116h192v232h-192z" class="gold o"/>
  <path d="M-96-116h192v22h-192z" class="goldd o"/>
  <circle cx="66" cy="6" r="12" class="ink"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M310 180l30-14M310 216h34M310 252l30 14"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('someone', '遠くの道から手をふっている小さな人を、手前の人が指さしているイラスト。', 'だれか。somebody とほぼ同じで、少し改まった言い方。', f"""
<path d="M300 306l150 94H150z" fill="#ded3c2"/>
<path d="M300 306v94" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
{person(158,352,1.15,1,'teal','blue','point','short','smile')}
<g transform="translate(420 316) scale(0.62)">
  {person(0,0,1,1,'coral','blue','up','bob','smile')}
</g>
<ellipse cx="420" cy="278" rx="62" ry="74" fill="none" stroke="{CRL}" stroke-width="4"
         stroke-dasharray="12 10"/>
<path d="M352 236a34 34 0 0 1 26 22" fill="none" stroke="{TONES['teal'][0]}"
      stroke-width="5" stroke-linecap="round"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('something', '箱から出ている正体不明の物を、首をかしげてのぞきこむイラスト。', '何か、ある物。中身が分からない物を指す。', f"""
{person(150,352,1.25,1,'teal','blue','think','short','surprised')}
{box(370,330,170,120,36,'blue')}
<ellipse cx="370" cy="252" rx="66" ry="40" class="goldp o"/>
<ellipse cx="370" cy="252" rx="96" ry="62" fill="none" stroke="{CRL}" stroke-width="4"
         stroke-dasharray="12 10"/>
{spark(370,170,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

_days = ''.join(f'<rect x="{90+i*70-26}" y="214" width="52" height="52" rx="8" class="{c} o"/>'
               for i, c in enumerate(['paper', 'paper', 'paper', 'gold', 'paper', 'paper', 'paper']))
add('sometimes', '7つ並んだ四角のうち、1つだけが金色で印がついているイラスト。', 'ときどき。いつもではない頻度を表す。', f"""
{_days}
{tick(300,240,0.55)}
{spark(300,150,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('son', '大人と男の子が手をつないで並び、そばにボールが転がっているイラスト。', '息子。親から見た男の子。', f"""
{person(196,352,1.35,1,'blue','blue','stand','short','smile')}
{person(392,352,0.86,1,'teal','blue','stand','short','smile')}
<path d="M247 318q56 24 112 12" fill="none" stroke="{SKIN}" stroke-width="10"
      stroke-linecap="round"/>
{ball(500,336,26,'gold')}
{heart(300,168,0.7,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('song', '音符の書かれた本が開かれ、まわりに音符が浮かんでいるイラスト。', '歌。歌われる曲そのもの。', f"""
{book(300,250,1.05,'violet')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="3">
  <path d="M-86 214h72M-86 238h72M-86 262h72M14 214h72M14 238h72M14 262h72"/>
</g>
<g class="ink">
  {''.join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="7" transform="rotate(-18 {x} {y})"/>' for x, y in [(-70,210),(-30,234),(30,258),(70,234)])}
</g>
{note(150,140,1.1,'teal')}{note(470,150,1.0,'coral')}{note(520,232,0.85,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('soon', '時計と、まもなく到着するバスを点線の矢印で結んだイラスト。', 'まもなく、すぐに。', f"""
{clock(180,170,64,11,4)}
{person(300,352,1.15,1,'gold','blue','stand','short','smile')}
<g transform="translate(480 316) scale(0.62)">
  <rect x="-120" y="-100" width="240" height="100" rx="18" class="blue o"/>
  <g class="bluep o">
    <rect x="-104" y="-86" width="70" height="42" rx="6"/>
    <rect x="-24" y="-86" width="70" height="42" rx="6"/>
    <rect x="56" y="-86" width="52" height="42" rx="6"/>
  </g>
  <circle cx="-70" cy="0" r="24" fill="#3a3f45" class="o"/>
  <circle cx="70" cy="0" r="24" fill="#3a3f45" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"
   marker-end="url(#ar)"><path d="M256 150q92-30 152 82"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('sorry', '割れたカップのそばで、頭を下げて謝っているイラスト。', 'すまなく思って、残念で。', f"""
<g transform="translate(250 352) rotate(18)">
  {person(0,0,1.2,1,'blue','blue','hold','short','sad')}
</g>
<g transform="translate(444 368)">
  <path d="M-70 0l24-30 14 26 18-32 16 32 20-24 16 28z" class="coral o"/>
  <path d="M-40 8h84a10 10 0 0 1-10 14h-64a10 10 0 0 1-10-14z" class="corald o"/>
</g>
<ellipse cx="444" cy="376" rx="96" ry="14" class="bluep o"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M304 190l-16-22M348 182l8-26"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('soup', '湯気の立つスープの皿に、スプーンが添えられているイラスト。', 'スープ。', f"""
<g transform="translate(300 300)">
  <ellipse rx="152" ry="38" fill="#fffefd" class="o"/>
  <path d="M-130 0h260a130 96 0 0 1-260 0z" class="blue o"/>
  <ellipse rx="124" ry="28" class="goldp o"/>
  <g class="coralp o">
    <circle cx="-52" cy="-4" r="18"/><circle cx="20" cy="6" r="16"/><circle cx="72" cy="-8" r="14"/>
  </g>
</g>
<g transform="translate(392 196) rotate(-32)">
  <path d="M-6 0h-104" fill="none" stroke="{STONE}" stroke-width="12" stroke-linecap="round"/>
  <ellipse cx="16" cy="0" rx="38" ry="25" class="paper"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M232 226q-16-18 0-36t0-34M300 210q-16-18 0-36t0-34M368 224q-16-18 0-36t0-34"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('south', '方位磁針の針が下を指し、下の方に太陽が描かれているイラスト。', '南、南の・南へ。', f"""
{compass(300,168,104)}
{sun(500,330,30)}
<path d="M300 300v44" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"
      stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('space', 'ロケットが惑星と星の間を飛んでいるイラスト。', '空間、場所。宇宙の意味でも使われる。', f"""
<g transform="translate(240 200) rotate(-30)">
  <path d="M0-96q30 34 30 96v40h-60v-40q0-62 30-96z" fill="#fffefd" class="o"/>
  <circle cy="-30" r="17" class="bluep o"/>
  <path d="M-30 24l-32 48h32zM30 24l32 48h-32z" class="coral o"/>
  <path d="M-20 40h40l-20 42z" class="gold o"/>
</g>
<circle cx="470" cy="140" r="46" class="violetp o"/>
<ellipse cx="470" cy="140" rx="88" ry="20" fill="none" stroke="{VIOD}" stroke-width="7"
         transform="rotate(-18 470 140)"/>
<circle cx="150" cy="330" r="34" class="greenp o"/>
<circle cx="182" cy="312" r="9" class="greend"/>
{spark(420,300,1.0)}{spark(120,120,0.9)}{spark(540,280,0.8)}{spark(330,80,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('speak', '吹き出しを出して話しかけ、いすの相手が聞いているイラスト。', '話す、話をする。', f"""
{person(180,352,1.25,1,'teal','blue','point','short','smile')}
{bubble(398,166,1.15,'teal')}
{chair(470,352,1.05,'gold')}
{sit(470,352,1.0,-1,'violet','blue','short','smile','lap')}
<path d="M300 214a46 46 0 0 1 0 62" fill="none" stroke="{TONES['teal'][0]}"
      stroke-width="5" stroke-linecap="round"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

_cakes = ''.join(
    f'<g transform="translate({x} 340)">'
    f'<path d="M-44 0h88l-10-58h-68z" class="{c} o"/>'
    f'<path d="M-48-58h96v12h-96z" class="{p} o"/>'
    f'<path d="M0-58v-28" fill="none" stroke="{INK}" stroke-width="6"/>'
    f'<circle cy="-94" r="10" class="coral o"/></g>'
    for x, c, p in ((140, 'paper', 'muted'), (300, 'gold', 'goldp'), (460, 'paper', 'muted')))
add('special', '3つのケーキのうち真ん中の1つだけが金色で、輪に囲まれているイラスト。', '特別な、特別の。', f"""
{_cakes}
{ring(300,290,112,True)}
{spark(410,150,1.0)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('spoonful', '粉を山もりにすくったスプーンから、カップへ粉が落ちるイラスト。', 'スプーン1杯の量。', f"""
{cup(300,332,1.2,'teal')}
<g transform="translate(322 168) rotate(-28)">
  <path d="M-8 0h-104" fill="none" stroke="{STONE}" stroke-width="13" stroke-linecap="round"/>
  <ellipse cx="16" cy="0" rx="38" ry="25" class="paper"/>
  <path d="M-10-16q26-36 52 0z" class="goldp o"/>
</g>
<g class="gold">
  {''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(306,238,6),(298,268,5),(310,296,6),(296,318,5)])}
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sport', 'ボールを蹴ってゴールをねらっているイラスト。', 'スポーツ、運動競技。', f"""
{person(180,352,1.25,1,'gold','blue','walk','short','smile')}
<circle cx="276" cy="340" r="26" class="paper"/>
<path d="M256 326q20 12 40 0" fill="none" stroke="{INK}" stroke-width="3"/>
<g transform="translate(470 352)">
  <path d="M-88 0v-124M88 0v-124M-88-124h176" fill="none" stroke="{STONE}"
        stroke-width="11" stroke-linecap="round"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8">
    <path d="M-44-124v124M0-124v124M44-124v124M-88-84h176M-88-44h176"/>
  </g>
</g>
<path d="M310 336q64-24 108-16" fill="none" stroke="{MUTED}" stroke-width="4"
      stroke-dasharray="10 9"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stairs', '積み上がった階段を、一段ずつ上っているイラスト。', '階段。', f"""
{''.join(f'<rect x="{160+i*76}" y="{352-(i+1)*46}" width="76" height="{(i+1)*46}" class="bluep o"/>' for i in range(4))}
{person(276,260,1.05,1,'gold','blue','walk','short','smile')}
<path d="M480 300q56-72 84-158" fill="none" stroke="{MUTED}" stroke-width="4"
      stroke-dasharray="10 9" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('stand up', 'いすのそばに立ち、上向きの矢印と、空いた座面が示されているイラスト。', '立ち上がる、立っている。', f"""
{chair(420,352,1.3,'gold')}
<ellipse cx="420" cy="300" rx="72" ry="54" fill="none" stroke="{MUTED}" stroke-width="4"
         stroke-dasharray="10 9"/>
{person(200,352,1.25,1,'teal','blue','stand','short','smile')}
{arrowline([(310,296),(310,150)], None, 6, False)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('station', '屋根つきのホームに電車がとまり、時計が下がっているイラスト。', '駅。署、局の意味もある。', f"""
<g transform="translate(300 330)">
  <rect x="-250" y="-104" width="440" height="104" rx="16" class="teal o"/>
  <g class="tealp o">
    <rect x="-230" y="-88" width="70" height="44" rx="7"/>
    <rect x="-144" y="-88" width="70" height="44" rx="7"/>
    <rect x="-58" y="-88" width="70" height="44" rx="7"/>
  </g>
  <path d="M190-104h30a26 26 0 0 1 26 26v52a26 26 0 0 1-26 26h-30z" class="teal o"/>
  <circle cx="-160" cy="0" r="24" fill="#3a3f45" class="o"/>
  <circle cx="60" cy="0" r="24" fill="#3a3f45" class="o"/>
</g>
<path d="M0 342h600v12H0z" fill="#ded3c2" class="o"/>
<path d="M340 152h240v16H340z" class="green o"/>
<path d="M364 168v174" fill="none" stroke="{STONE}" stroke-width="9"/>
{clock(452,210,44,3,10)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stethoscope', '聴診器が、心臓の鼓動を表す線の上に置かれているイラスト。', '聴診器。', f"""
<g fill="none" stroke="{STONE}" stroke-width="10" stroke-linecap="round">
  <path d="M150 62v70q0 90 100 96M250 62v70q0 90-100 96"/>
</g>
<circle cx="150" cy="54" r="12" class="ink"/>
<circle cx="250" cy="54" r="12" class="ink"/>
<path d="M200 228q46 40 118 32" fill="none" stroke="{STONE}" stroke-width="12"
      stroke-linecap="round"/>
<circle cx="350" cy="262" r="42" fill="#fffefd" class="o"/>
<circle cx="350" cy="262" r="22" fill="{STONE}" class="o"/>
<path d="M60 356h84l26-50 30 96 24-70 18 24h56" fill="none" stroke="{TONES['teal'][0]}"
      stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stickers', '台紙に星やハートのシールが並び、1枚がめくれかかっているイラスト。', 'ステッカー、シール。', f"""
<g transform="translate(276 236) rotate(-5)">
  <path d="M-160-130h320v260h-320z" class="paper"/>
  <circle cx="-90" cy="-70" r="34" class="goldp o"/>
  <circle cx="0" cy="-70" r="34" class="tealp o"/>
  <circle cx="90" cy="-70" r="34" class="bluep o"/>
  {spark(-90,26,1.2)}{spark(0,26,1.2)}{spark(90,26,1.2)}
  <g transform="translate(-90 96)">{heart(0,0,0.6,'coral')}</g>
  <g transform="translate(0 96)">{heart(0,0,0.6,'violet')}</g>
  <g transform="translate(90 96)">{heart(0,0,0.6,'green')}</g>
</g>
<g transform="translate(474 138) rotate(22)">
  <circle r="42" class="coralp o"/>
  <path d="M-42 14q42 26 84 0" fill="none" stroke="{CRLD}" stroke-width="6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sticky note', 'ボードに貼られた付箋が1枚めくれて、角が丸まっているイラスト。', '付箋。はがして貼り直せる小さな紙。', f"""
<g transform="translate(300 220)">
  <path d="M-240-150h480v300h-480z" class="paper"/>
  <g transform="translate(-140 -60)">
    <path d="M-70-70h140v140h-140z" class="gold o"/>
    <g fill="{TONES['gold'][2]}">{''.join(f'<rect x="-46" y="{-40+i*26}" width="{92-(i%3)*24}" height="10" rx="5"/>' for i in range(3))}</g>
  </g>
  <g transform="translate(30 -40) rotate(-3)">
    <path d="M-70-70h140v140h-140z" class="teal o"/>
    <g fill="{TONES['teal'][2]}">{''.join(f'<rect x="-46" y="{-40+i*26}" width="{92-(i%3)*24}" height="10" rx="5"/>' for i in range(3))}</g>
  </g>
  <g transform="translate(80 60)">
    <path d="M-70-60h128l28 28v92h-156z" class="coral o"/>
    <path d="M58-60l28 28h-28z" class="coralp o"/>
    <g fill="{CRLD}">{''.join(f'<rect x="-46" y="{-24+i*26}" width="{92-(i%3)*24}" height="10" rx="5"/>' for i in range(3))}</g>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stop', '手のひらを前に出して止め、そばに八角形の標識が立っているイラスト。', '止まる、止める。停留所の意味もある。', f"""
<path d="M180 200v86" fill="none" stroke="{STONE}" stroke-width="14" stroke-linecap="round"/>
<g transform="translate(180 200)">
  <path d="M70 29L29 70H-29L-70 29V-29L-29-70H29L70-29z" class="coral o"/>
  <path d="M-44 0h88v18h-88z" fill="#fffefd"/>
</g>
{hand(424,190,1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M340 116l-34-24M340 200h-46M340 280l-34 24"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('story', 'いすに座って絵本を開き、読み聞かせているイラスト。', '話、物語。記事の意味もある。', f"""
{chair(240,352,1.25,'gold')}
{sit(240,352,1.2,1,'violet','blue','bob','smile','down')}
<g transform="translate(360 312) rotate(-8)">
  <path d="M-96-64h88v128h-88zM0-64h88v128H0z" class="paper"/>
  <path d="M-8-70h16v140h-16z" class="violetd o"/>
  <circle cx="-52" cy="-16" r="26" class="goldp o"/>
  <path d="M-92 40l30-30 30 26z" class="greenp"/>
  <g fill="{MUTED}">
    <rect x="20" y="-30" width="56" height="9" rx="4"/>
    <rect x="20" y="-4" width="48" height="9" rx="4"/>
    <rect x="20" y="22" width="52" height="9" rx="4"/>
  </g>
</g>
{heart(330,168,0.7,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('street', '建物が並ぶ通りに、街灯とセンターラインのある道が続くイラスト。', '通り、街路。', f"""
{building(110,310,0.7,'teal')}
{building(290,310,0.88,'coral')}
{building(490,310,0.7,'blue')}
<path d="M20 344h560v46H20z" fill="#e6e2da" class="o"/>
<path d="M60 370h480" fill="none" stroke="#fffefd" stroke-width="7" stroke-dasharray="30 24"/>
<g transform="translate(60 344)">
  <path d="M0 0v-150" fill="none" stroke="{STONE}" stroke-width="11" stroke-linecap="round"/>
  <path d="M0-150q40 0 40 30" fill="none" stroke="{STONE}" stroke-width="11"
        stroke-linecap="round"/>
  <circle cx="44" cy="-108" r="15" class="goldp o"/>
</g>
{spark(96,140,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stressful', '書類と時計に囲まれ、頭をかかえて緊張しているイラスト。', 'ストレスの多い、緊張する。', f"""
{doc(110,158,78,100,3,MUTED)}
{doc(492,150,78,100,3,MUTED)}
{doc(176,80,70,88,3,MUTED)}
{doc(430,76,70,88,3,MUTED)}
{clock(300,110,46,10,2)}
{person(300,352,1.28,1,'coral','blue','up','short','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M234 200q-18-14-6-30M366 200q18-14 6-30"/>
</g>
<g class="blue">{drop(252,206,0.8)}{drop(352,214,0.8)}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('strong', 'バーベルを頭上に持ち上げて立っているイラスト。', '強い、丈夫な、味が濃い。', f"""
{person(300,352,1.4,1,'coral','blue','up','short','smile')}
<path d="M150 176h300" fill="none" stroke="{STONE}" stroke-width="13" stroke-linecap="round"/>
<circle cx="150" cy="176" r="48" class="ink"/>
<circle cx="450" cy="176" r="48" class="ink"/>
<g fill="none" stroke="{MUTED}" stroke-width="6">
  <circle cx="150" cy="176" r="30"/><circle cx="450" cy="176" r="30"/>
</g>
<g fill="{BRN}">
  <rect x="118" y="140" width="14" height="72" rx="6"/>
  <rect x="168" y="140" width="14" height="72" rx="6"/>
  <rect x="418" y="140" width="14" height="72" rx="6"/>
  <rect x="468" y="140" width="14" height="72" rx="6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('student', 'かばんを背負い、本を抱えて歩いていくイラスト。', '学生、生徒。', f"""
<g transform="translate(196 292)">
  <path d="M-42-58q42-26 84 0v100h-84z" class="coral o"/>
  <path d="M-24-58v-18h48v18z" class="corald o"/>
  <path d="M-30 42h60v10h-60z" class="corald"/>
</g>
{person(250,352,1.25,1,'teal','blue','walk','short','smile')}
{book(302,300,0.46,'teal')}
{building(510,352,0.6,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('study', '机に向かい、ランプの明かりで本を読んでいるイラスト。', '勉強する。研究・勉強という名詞の意味もある。', f"""
{sit(200,352,1.2,1,'teal','blue','short','smile','down')}
{chair(200,352,1.15,'gold')}
<g transform="translate(340 320)">
  <path d="M-170-14h340v18h-340z" class="goldd o"/>
  <path d="M-156 4v68M156 4v68M-40 4v68M40 4v68" fill="none" stroke="{BRN}"
        stroke-width="11" stroke-linecap="round"/>
</g>
<g transform="translate(300 286)">
  <path d="M-84-34h84v68h-84zM0-34h84v68H0z" class="paper"/>
  <path d="M-6-40h12v76h-12z" class="teald o"/>
  <g fill="{MUTED}">
    <rect x="-70" y="-18" width="56" height="8" rx="4"/>
    <rect x="-70" y="6" width="48" height="8" rx="4"/>
    <rect x="14" y="-18" width="56" height="8" rx="4"/>
    <rect x="14" y="6" width="48" height="8" rx="4"/>
  </g>
</g>
<path d="M486 240l-72 76h128z" fill="#fff6d9"/>
<g transform="translate(486 270)">
  <path d="M0 36v-42" fill="none" stroke="{STONE}" stroke-width="9" stroke-linecap="round"/>
  <path d="M-52-4h104l-26-46h-52z" class="coral o"/>
</g>
{clock(120,150,40,10,2)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('summer', '強い日ざしと波の立つ海、砂浜にビーチボールが転がっているイラスト。', '夏。', f"""
{sun(470,110,52)}
<path d="M0 306h600v94H0z" fill="#e8eef6"/>
<path d="M0 306q60-26 120 0t120 0 120 0 120 0 120 0v92H0z" class="bluep"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M40 336q50-22 100 0t100 0 100 0 100 0 100 0"/>
  <path d="M60 372q50-22 100 0t100 0 100 0 100 0"/>
</g>
<g transform="translate(170 292)">
  <circle r="50" class="paper"/>
  <path d="M0-50q36 50 0 100" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9"/>
  <path d="M0-50q-36 50 0 100" fill="none" stroke="{TONES['teal'][0]}" stroke-width="9"/>
  <circle r="10" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=False)

add('sun', '家の上に大きく輝いている太陽のイラスト。', '太陽、日光。', f"""
{sun(300,140,76)}
{house(300,352,0.78,'teal')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sunbathe', 'タオルの上に寝そべり、太陽の下で日光浴をしているイラスト。', '日光浴をする、日なたぼっこをする。', f"""
{sun(480,104,44)}
<path d="M110 348h360l-26 40H136z" class="goldp o"/>
<g transform="translate(312 344) rotate(-74)">
  {person(0,0,1.05,1,'coral','blue','stand','bob','smile')}
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sunburn', '赤くなった背中と肩に、太陽の光と熱の波線が当たっているイラスト。', '日焼け。赤くなってひりひりする肌。', f"""
{sun(486,104,44)}
<circle cx="300" cy="168" r="48" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
<path d="M300 352q-124-12-140-100-8-64 62-80 78-18 156 0 70 16 62 80-16 88-140 100z" class="coral o"/>
<path d="M256 262l44 96 44-96" fill="none" stroke="{VIOD}" stroke-width="13"/>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M208 244q-18-18 0-36t0-34M392 244q18-18 0-36t0-34"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('punctuality', '時計の針がちょうど時刻を指し、時間どおりに着いた人にチェックがついているイラスト。', '時間を守ること、正確さ。', f"""
{clock(220,180,76,12,0)}
{tick(306,182,1.15)}
{person(468,352,1.2,1,'teal','blue','walk','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sunglasses', '大きな顔に黒いサングラスがかかっているイラスト。', 'サングラス。', f"""
{face(300,220,112,'smile')}
<g transform="translate(300 200)">
  <rect x="-104" y="-32" width="88" height="64" rx="24" class="ink"/>
  <rect x="16" y="-32" width="88" height="64" rx="24" class="ink"/>
  <path d="M-16-10h32" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M-104-16h-30M104-16h30" fill="none" stroke="{INK}" stroke-width="10"
        stroke-linecap="round"/>
  <path d="M-96-26q30-14 72 0" fill="none" stroke="#8f9aa3" stroke-width="5"/>
  <path d="M24-26q30-14 72 0" fill="none" stroke="#8f9aa3" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sunshine', '雲がわきに流れ、明るい日ざしの中で人が手を広げているイラスト。', '日光、晴天。', f"""
{sun(200,140,62)}
<g transform="translate(500 96)">{cloud(0,0,0.6,'blue')}</g>
{person(410,352,1.25,1,'gold','blue','up','bob','smile')}
{spark(306,152,1.0)}{spark(140,236,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('swimsuit', 'ハンガーにかけられた水着と、足もとの波のイラスト。', '水着。', f"""
<path d="M300 70q0-24 24-24t24 24" fill="none" stroke="{MUTED}" stroke-width="7"
      stroke-linecap="round"/>
<path d="M300 70l-96 48h192z" fill="none" stroke="{STONE}" stroke-width="9"
      stroke-linejoin="round"/>
<g transform="translate(300 240)">
  <path d="M-64-104h128q-10 44 0 86 6 30-8 50h-46l-18-58-18 58h-46q-14-20-8-50 10-42 0-86z" class="violet o"/>
  <path d="M-64-104q64 24 128 0" fill="none" stroke="{VIOD}" stroke-width="9"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M60 356q40-20 80 0t80 0 80 0 80 0 80 0"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('synagogue', '六芒星の飾られた建物が立っているイラスト。', 'シナゴーグ、ユダヤ教の礼拝所。', f"""
{building(300,352,1.1,'blue')}
<path d="M300 100v-28" fill="none" stroke="{STONE}" stroke-width="8"/>
{star6(300,140,40,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('table', '4本脚の食卓にカップと皿が載っているイラスト。', 'テーブル、食卓。一覧の「表」の意味もある。', f"""
<g transform="translate(300 250)">
  <path d="M-186-18h372v22h-372z" class="gold o"/>
  <path d="M-168 4l-14 96M168 4l14 96M-62 4l-8 96M62 4l8 96" fill="none" stroke="{BRN}"
        stroke-width="13" stroke-linecap="round"/>
</g>
{cup(190,206,0.95,'teal')}
<ellipse cx="400" cy="232" rx="62" ry="15" class="paper"/>
<ellipse cx="400" cy="226" rx="38" ry="9" fill="#fffefd" class="o"/>
<path d="M470 200v40" fill="none" stroke="{STONE}" stroke-width="9" stroke-linecap="round"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('take', '棚に並んだ箱を1つ、手をのばして取り上げているイラスト。', '取る、持っていく。乗る、時間がかかるの意味もある。', f"""
<path d="M60 250h480v18H60z" class="goldd o"/>
<path d="M120 268v84M480 268v84" fill="none" stroke="{BRN}" stroke-width="12"
      stroke-linecap="round"/>
{box(180,214,96,72,24,'teal')}
{pbox(320,214,96,72,24)}
{box(430,140,112,84,26,'gold')}
{hand(430,206,1)}
<path d="M330 214q60-50 84-64" fill="none" stroke="{MUTED}" stroke-width="4"
      stroke-dasharray="10 9"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('take care of', '具合の悪い人に、そばから水のカップを差し出しているイラスト。', '〜の世話をする、〜に対処する。', f"""
{chair(452,352,1.2,'gold')}
{sit(452,352,1.15,-1,'violet','blue','short','sad','down')}
<path d="M382 300h150l-14 52h-122z" class="bluep o"/>
{person(178,352,1.2,1,'teal','blue','give','short','smile')}
{cup(330,248,0.85,'gold')}
{heart(330,148,0.75,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tall', '背の高い人と低い人が並び、高い方に目印がついているイラスト。', '背が高い、高い。', f"""
{person(210,352,1.5,1,'blue','blue','stand','short','smile')}
{person(430,352,0.95,1,'teal','blue','stand','short','smile')}
<ellipse cx="210" cy="200" rx="92" ry="150" fill="none" stroke="{TONES['coral'][0]}"
         stroke-width="4" stroke-dasharray="12 10"/>
<path d="M112 146h196M112 146v-16M308 146v-16" fill="none" stroke="{MUTED}"
      stroke-width="4" stroke-dasharray="10 9"/>
{spark(330,120,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tambourine', 'タンバリンを手に持って振り、音が広がっているイラスト。', 'タンバリン。', f"""
{person(214,352,1.25,1,'violet','blue','hold','bob','smile')}
<g transform="translate(310 244)">
  <circle r="64" fill="#fffefd" class="o"/>
  <circle r="64" fill="none" stroke="{TONES['gold'][0]}" stroke-width="14"/>
  {''.join(f'<circle cx="{60*math.cos(math.radians(a)):.0f}" cy="{60*math.sin(math.radians(a)):.0f}" r="9" class="gold o"/>' for a in range(0,360,60))}
</g>
{note(432,176,1.0,'teal')}{note(492,250,0.85,'coral')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M384 320q40 20 58 58"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('taxi', '屋根に標識のついた車がとまり、人が手を上げて呼びとめているイラスト。', 'タクシー。', f"""
{person(112,352,1.2,1,'teal','blue','up','short','smile')}
{car(386,336,0.92,'gold',True)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tea', '湯気の立つティーカップと、そばに置かれたティーポットのイラスト。', '茶、紅茶。お茶の時間の意味もある。', f"""
{cup(214,300,1.5,'teal')}
<g transform="translate(452 322)">
  <path d="M-64-6q-6-72 64-72t64 72z" class="gold o"/>
  <path d="M-28-80h56l-8-16h-40z" class="goldd o"/>
  <circle cy="-104" r="10" class="goldd o"/>
  <path d="M58-52q44-14 54-46l-24-10q-16 28-42 34z" class="goldd o"/>
  <path d="M-62-52q-46-10-40 24 6 30 40 26" fill="none" stroke="{TONES['gold'][0]}"
        stroke-width="10"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M182 224q-16-18 0-36t0-34M246 224q-16-18 0-36t0-34"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('teach', '黒板に書いた図を指して説明しているイラスト。', '教える。', f"""
<g transform="translate(400 200)">
  <path d="M-176-124h352v248h-352z" class="greend o"/>
  <g fill="none" stroke="#fffefd" stroke-width="5" stroke-linecap="round">
    <path d="M-120 60l64-104 68 104z"/>
    <circle cx="86" cy="-30" r="42"/>
    <path d="M-120-40h72M-120-96h120"/>
  </g>
</g>
<path d="M320 324v28M480 324v28" fill="none" stroke="{BRN}" stroke-width="12"
      stroke-linecap="round"/>
{person(150,352,1.3,1,'violet','blue','point','short','smile')}
<path d="M240 244q56-40 84-64" fill="none" stroke="{MUTED}" stroke-width="4"
      stroke-dasharray="10 9"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('teacher', '黒板の前に立ち、本を持って生徒の方を向いているイラスト。', '教師、先生。', f"""
<g transform="translate(200 150)">
  <path d="M-160-96h320v192h-320z" class="greend o"/>
  <g fill="none" stroke="#fffefd" stroke-width="5" stroke-linecap="round">
    <path d="M-110-40h84M-110 0h120M-110 40h72"/>
  </g>
</g>
{person(168,352,1.28,1,'violet','blue','hold','short','smile')}
{book(232,288,0.42,'gold')}
{chair(468,352,1.1,'gold')}
{sit(468,352,1.05,-1,'teal','blue','short','smile','lap')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('team', '同じ色のユニフォームを着た3人が並び、前にボールが置かれているイラスト。', 'チーム、組。', f"""
{person(150,352,1.1,1,'teal','blue','hold','short','smile')}
{person(300,352,1.2,1,'teal','blue','hold','short','smile')}
{person(450,352,1.1,1,'teal','blue','hold','short','smile')}
{ball(300,338,30,'paper')}
<circle cx="300" cy="338" r="30" fill="none" stroke="{INK}" stroke-width="3"/>
<path d="M280 322q20 12 40 0" fill="none" stroke="{INK}" stroke-width="3"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('telephone', '台の上に置かれた電話機と、らせん状にのびるコードのイラスト。', '電話、電話をかける。', f"""
<path d="M120 340h360v16H120z" class="goldd o"/>
{phone(300,270,1.0,'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('television', '画面に山と太陽の映像が映っているテレビのイラスト。', 'テレビ、テレビ放送。', f"""
<g transform="translate(300 250)">{tv(0,0,0.8)}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tell', '相手の耳もとに口を寄せて、ひそひそと伝えているイラスト。', '話す、伝える。見分けるの意味もある。', f"""
{person(200,352,1.2,1,'coral','blue','reach','short','smile')}
{person(400,352,1.15,-1,'violet','blue','think','bob','smile')}
{bubble(322,146,0.62,'coral')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M344 268a30 30 0 0 1 22-16"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('ten', '金のボールが2列に5つずつ、10個並んでいるイラスト。', '10、十、10歳。', f"""
{''.join(ball(140 + c*80, 200 + r*84, 32) for r in range(2) for c in range(5))}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tennis', 'ラケットを構えてボールを打ち、コートにネットが張られているイラスト。', 'テニス。', f"""
{person(190,352,1.25,1,'gold','blue','reach','short','smile')}
<g transform="translate(320 230) rotate(-16)">
  <path d="M0 0v-88" fill="none" stroke="{STONE}" stroke-width="12" stroke-linecap="round"/>
  <ellipse cy="-146" rx="52" ry="62" fill="#fffefd" stroke="{TONES['coral'][0]}"
           stroke-width="10"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    <path d="M-52-146h104M-26-200v110M0-206v118M26-200v110"/>
  </g>
</g>
<g transform="translate(500 306)">
  <path d="M-70 0v-104h140v104" fill="none" stroke="{STONE}" stroke-width="10"
        stroke-linecap="round"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 7">
    <path d="M-46-104v104M-22-104v104M0-104v104M22-104v104M46-104v104M-70-78h140M-70-52h140M-70-26h140"/>
  </g>
</g>
{ball(430,180,20,'gold')}
<path d="M340 158q70-30 86-4" fill="none" stroke="{MUTED}" stroke-width="4"
      stroke-dasharray="10 9"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tenth', '10個並んだボールのうち、10番目だけが輪で示されているイラスト。', '10番目の、10分の1。', f"""
{''.join(ball(120 + i*40, 258, 22) for i in range(10))}
{ring(480,258,44,False,'coral')}
{spark(480,178,1.0)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('terrible', '黒い雲から雷が落ち、激しい雨の中を人が身をすくめて歩いているイラスト。', 'ひどい、恐ろしい。とても下手な、の意味もある。', f"""
<g transform="translate(230 120)">{cloud(0,0,1.5,'blue')}</g>
{bolt(300,220,1.3)}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M120 166l-24 60M190 176l-24 60M356 178l-24 60M426 168l-24 60"/>
</g>
{person(300,352,1.25,1,'coral','blue','up','short','surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M234 198q-18-14-6-30M366 198q18-14 6-30"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('test', '答案用紙に書き込み、チェックがついているイラスト。', '試験、テスト。試す、検査するの意味もある。', f"""
{chair(120,352,1.1,'gold')}
{sit(120,352,1.05,1,'teal','blue','short','neutral','down')}
<g transform="translate(340 210) rotate(-3)">
  <path d="M-120-150h240v300h-240z" class="paper"/>
  {''.join(f'<rect x="-92" y="{-104+i*58}" width="{170-(i%3)*40}" height="12" rx="6" fill="{MUTED}"/>' for i in range(5))}
  {tick(52,-112,0.7)}
</g>
<g transform="translate(506 346) rotate(-24)">
  <path d="M-70-10h116v20h-116z" class="gold o"/>
  <path d="M46-10l26 10-26 10z" class="goldp o"/>
  <path d="M66-4l8 4-8 4z" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('than', '天筆に大小の箱が載り、重い左側が下に傾いているイラスト。', '〜より。2つを比べる語。', f"""
{scales(300,300,-14,1)}
{box(175,216,92,72,24,'gold')}
{box(388,176,62,48,16,'teal')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thank', '品物を手渡され、笑顔で受け取っているイラスト。', '感謝する、礼を言う。', f"""
{person(180,352,1.2,1,'teal','blue','give','short','smile')}
{person(430,352,1.2,-1,'coral','blue','reach','bob','smile')}
{box(306,256,86,64,22,'gold')}
{heart(306,148,0.8,'coral')}
{spark(390,186,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('the', '3つの箱のうち真ん中の1つだけが輪で囲まれ、上から矢印が指しているイラスト。', 'その、例の。特定のものを指す語。', f"""
{pbox(150,300,104,80,26)}
{box(300,300,104,80,26,'gold')}
{pbox(450,300,104,80,26)}
<ellipse cx="300" cy="300" rx="86" ry="72" fill="none" stroke="{TONES['coral'][0]}"
         stroke-width="4" stroke-dasharray="12 10"/>
{arrowline([(300,116),(300,204)], MUTED, 6, True)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('theater', '緞帳の下がった舞台と、階段状の客席が並んでいるイラスト。', '劇場、演劇。', f"""
<g transform="translate(300 150)">
  <path d="M-280-76h560v40h-560z" class="corald o"/>
  <path d="M-280-36q40 60 40 186h-40z" class="coral o"/>
  <path d="M280-36q-40 60-40 186h40z" class="coral o"/>
  <path d="M-236 150h472v18h-472z" class="goldd o"/>
</g>
<g class="bluep o">
  {''.join(f'<rect x="{60+c*152}" y="{336+r*36}" width="128" height="28" rx="7"/>' for r in range(2) for c in range(4))}
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('theatre', 'スポットライトの当たった舞台で、2人の役者が向かい合って演じているイラスト。', '劇場、演劇。イギリス式のつづり。', f"""
<path d="M300 60l-150 246h300z" fill="#fff6d9"/>
<path d="M30 110h64v196H30z" class="coral o"/>
<path d="M506 110h64v196h-64z" class="coral o"/>
<path d="M30 306h540v18H30z" class="goldd o"/>
<g transform="translate(232 306) scale(0.9)">{person(0,0,1,1,'violet','blue','give','bob','smile')}</g>
<g transform="translate(388 306) scale(0.9)">{person(0,0,1,-1,'gold','blue','reach','short','smile')}</g>
{heart(310,150,0.7,'coral')}
{spark(190,116,0.9)}{spark(412,116,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('their', '3人の人物から、共通で持っている家へ点線がのびているイラスト。', '彼らの、彼女らの。所有を表す語。', f"""
{person(120,352,1.05,1,'blue','blue','hold','short','smile')}
{person(232,352,1.15,1,'blue','blue','hold','short','smile')}
{person(344,352,1.05,1,'blue','blue','hold','short','smile')}
{house(496,352,0.64,'gold')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9">
  <path d="M150 232q120-44 262-30"/>
  <path d="M262 224q100-32 150-24"/>
  <path d="M374 232q60-24 66-26"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('them', '3人の相手に向かって、品物を手渡しているイラスト。', '彼らを、彼らに。複数の目的格。', f"""
{person(110,352,1.2,1,'teal','blue','give','short','smile')}
{box(214,272,74,56,20,'gold')}
{person(340,352,1.0,-1,'coral','blue','reach','short','smile')}
{person(448,352,1.0,-1,'coral','blue','reach','bob','smile')}
{person(554,352,1.0,-1,'coral','blue','reach','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

_steps = ''.join(
    f'<g transform="translate({x} {y}) rotate({r})">'
    f'<ellipse cy="10" rx="13" ry="19" fill="{MUTED}"/>'
    f'<ellipse cy="-14" rx="9" ry="8" fill="{MUTED}"/></g>'
    for x, y, r in [(100,356,14),(162,338,22),(226,308,30),(284,270,38),(328,226,46),(356,178,52)])
add('then', '道に沿って足あとが続き、順に進んでいくようすを示すイラスト。', 'そのとき、それから。順に起こることをつなぐ語。', f"""
{_steps}
{arrowline([(140,376),(400,150)], MUTED, 6, True)}
{clock(500,140,46,3,0)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('there', '丘の上の木を指さし、矢印と輪でその場所を示すイラスト。', 'そこに、そこへ。〜がある、の意味でも使う。', f"""
{person(140,352,1.2,1,'teal','blue','point','short','smile')}
<path d="M300 306q94-74 200 0z" class="greenp o"/>
{tree(452,268,0.66)}
<ellipse cx="452" cy="224" rx="82" ry="76" fill="none" stroke="{TONES['coral'][0]}"
         stroke-width="4" stroke-dasharray="12 10"/>
<path d="M224 268q80-46 118-50" fill="none" stroke="{MUTED}" stroke-width="5"
      stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('these', '手前に並んだ3つの品物を指さし、輪で囲んでいるイラスト。', 'これらの。近くにある複数を指す語。', f"""
{person(110,352,1.15,1,'gold','blue','point','short','smile')}
{pbox(320,320,92,72,24)}
{ball(432,300,34,'teal')}
{cup(534,294,0.8,'gold')}
<ellipse cx="428" cy="310" rx="172" ry="88" fill="none" stroke="{TONES['coral'][0]}"
         stroke-width="4" stroke-dasharray="12 10"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('those', '遠くの3つの品物を指さし、点線の矢印と輪で示しているイラスト。', 'あれらの、それらの。遠くにある複数を指す語。', f"""
{person(120,352,1.15,1,'gold','blue','point','short','smile')}
<g transform="translate(438 318) scale(0.5)">{pbox(0,0,92,72,24)}</g>
{ball(506,300,18,'teal')}
<g transform="translate(560 320) scale(0.4)">{cup(0,0,1,'gold')}</g>
<ellipse cx="486" cy="300" rx="110" ry="72" fill="none" stroke="{TONES['coral'][0]}"
         stroke-width="4" stroke-dasharray="12 10"/>
<path d="M230 264q110-40 156-24" fill="none" stroke="{MUTED}" stroke-width="5"
      stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('they', '3人が並んで一緒に歩いているイラスト。', '彼らは、彼女らは、それらは。複数の主語。', f"""
{person(160,352,1.15,1,'teal','blue','walk','short','smile')}
{person(300,352,1.25,1,'coral','blue','walk','bob','smile')}
{person(440,352,1.15,1,'violet','blue','walk','short','smile')}
<ellipse cx="300" cy="300" rx="242" ry="94" fill="none" stroke="{MUTED}" stroke-width="4"
         stroke-dasharray="12 12"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thing', '箱やボール、りんごにカップと、いろいろな物が並んでいるイラスト。', '物、こと。まとめて物を指す語。', f"""
{box(150,300,110,84,26,'gold')}
{ball(280,292,38,'teal')}
<g transform="translate(400 300)">
  <circle r="42" class="coral o"/>
  <path d="M-2-42q0-24 18-30" fill="none" stroke="{GRND}" stroke-width="6" stroke-linecap="round"/>
  <path d="M4-62q30-14 44 4-24 20-44-4z" class="greenp o"/>
</g>
{cup(530,294,0.85,'violet')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('think', '頭の上の吹き出しの中に電球が浮かび、考えこんでいるイラスト。', '考える、思う。', f"""
{person(210,352,1.3,1,'teal','blue','think','short','neutral')}
<circle cx="296" cy="186" r="14" class="bluep o"/>
<circle cx="332" cy="152" r="21" class="bluep o"/>
{bubble(430,104,1.0,'blue',0)}
{bulb(430,104,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thirsty', '太陽の下、水の入ったグラスを手に持っているイラスト。', 'のどが渇いて。', f"""
{sun(490,104,42)}
{person(230,352,1.25,1,'gold','blue','hold','short','sad')}
<g transform="translate(296 264)">
  <path d="M-36-54h72l-10 108h-52z" fill="#fffefd" class="o"/>
  <path d="M-33-22h66l-8 76h-50z" class="bluep"/>
</g>
<g class="blue">{drop(376,238,0.8)}{drop(404,266,0.6)}</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M170 234q-14-16 0-32t0-30"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thirteen', '10本をたばねた束と、ボール3つを並べて示したイラスト。', '13、十三。10と3を合わせた数。', f"""
{bundle(160,224,1.05,'gold')}
{''.join(ball(380 + i*80, 252, 32) for i in range(3))}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thirty', '10本の束が3つ並んでいるイラスト。', '30、三十。', f"""
{bundle(150,230,1.1,'gold')}
{bundle(300,230,1.1,'gold')}
{bundle(450,230,1.1,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('thousand', '箱を四段のピラミッド状に積み上げたイラスト。', '1000、千。数が多いことを表す。', f"""
{box(130,340,104,76,26,'gold')}
{box(250,340,104,76,26,'gold')}
{box(370,340,104,76,26,'gold')}
{box(490,340,104,76,26,'gold')}
{box(190,262,104,76,26,'teal')}
{box(310,262,104,76,26,'teal')}
{box(430,262,104,76,26,'teal')}
{box(250,184,104,76,26,'coral')}
{box(370,184,104,76,26,'coral')}
{box(310,106,104,76,26,'violet')}
{spark(150,112,1.0)}{spark(476,124,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('three', '金のボールが3つ並んでいるイラスト。', '3、三、3つ。', f"""
{ball(180,250,52)}{ball(300,250,52)}{ball(420,250,52)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('through', '丘のトンネルの中を列車が通り抜けているイラスト。', '〜を通って、〜を貫いて。〜の間じゅう、の意味もある。', f"""
<path d="M60 306q0-206 240-206t240 206z" class="greenp o"/>
<path d="M240 306v-96a60 60 0 0 1 120 0v96z" fill="#5b5347"/>
<g transform="translate(300 306)">
  <rect x="-56" y="-88" width="112" height="88" rx="14" class="teal o"/>
  <rect x="-40" y="-72" width="34" height="30" rx="6" class="tealp o"/>
  <rect x="4" y="-72" width="34" height="30" rx="6" class="tealp o"/>
  <circle cx="-30" cy="0" r="16" fill="#3a3f45" class="o"/>
  <circle cx="30" cy="0" r="16" fill="#3a3f45" class="o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M116 266h80M92 296h104M478 266h80M500 296h88"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('planner', '開いた手帳にマス目の予定表が広がり、そばにペンが置かれているイラスト。', '予定表、手帳。計画する人の意味もある。', f"""
<g transform="translate(300 240)">
  <path d="M-200-124h400v248h-400z" class="paper"/>
  <path d="M0-124v248" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
  <g class="goldp o">
    {''.join(f'<rect x="{-170+c*40}" y="{-96+r*34}" width="30" height="26" rx="4"/>' for r in range(3) for c in range(4))}
  </g>
  <g class="bluep o">
    {''.join(f'<rect x="{20+c*40}" y="{-96+r*34}" width="30" height="26" rx="4"/>' for r in range(3) for c in range(4))}
  </g>
  {tick(150,-30,0.5)}
  <g fill="{STONE}">{''.join(f'<rect x="-212" y="{-112+i*30}" width="16" height="10" rx="5"/>' for i in range(8))}</g>
</g>
<g transform="translate(492 344) rotate(-22)">
  <path d="M-70-10h116v20h-116z" class="violet o"/>
  <path d="M46-10l26 10-26 10z" class="violetp o"/>
  <path d="M66-4l8 4-8 4z" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('ticket', '切り取り線のついたチケットを手に持っているイラスト。', '切符、チケット。違反切符の意味もある。', f"""
{ticket(300,220,1.25,'gold')}
{hand(170,306,1)}
{spark(300,110,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tidy up', '棚に本をそろえ、散らかった物を箱にまとめているイラスト。', '片づける、整理する。', f"""
<path d="M330 176h244v18H330z" class="goldd o"/>
<path d="M330 322h244v18H330z" class="goldd o"/>
<path d="M550 176v146M336 176v146" fill="none" stroke="{BRN}" stroke-width="12"
      stroke-linecap="round"/>
{''.join(f'<rect x="{352+i*32}" y="84" width="24" height="92" rx="4" class="{c} o"/>' for i, c in enumerate(['teal','teal','coral','coral','gold','gold','violet']))}
{person(230,352,1.2,1,'teal','blue','give','short','smile')}
{book(292,278,0.4,'coral')}
{box(96,346,104,72,26,'blue')}
{tick(120,140,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tin opener', '缶切りで缶のふたを開け、めくれたふたが立っているイラスト。', '缶切り。', f"""
{can(260,300,1.15,'blue')}
<path d="M186 192q-32-42 8-66 28-16 42 12" fill="none" stroke="{STONE}"
      stroke-width="10" stroke-linecap="round"/>
<g transform="translate(330 178) rotate(-16)">
  <path d="M-96 0h150" fill="none" stroke="{STONE}" stroke-width="14" stroke-linecap="round"/>
  <circle cx="62" cy="0" r="20" class="ink"/>
  <path d="M62-20q28 2 26 24" fill="none" stroke="{STONE}" stroke-width="10"
        stroke-linecap="round"/>
</g>
{hand(432,232,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

finish(__file__)
