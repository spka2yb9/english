"""第13回: 場所・容器・情報・状態など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('bar', '細長い一本の棒と、それを渡した手すりのイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(300 190) rotate(-8)">
  <path d="M-200-18h400v36h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-200-18h400" fill="none" stroke="#ffffff" stroke-width="6"/>
</g>
<path d="M120 200v160M480 210v150" fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round"/>
<path d="M60 360h480" class="a"/>
""", ground=True)

add('charity', '募金の呼びかけに応じて、困っている人へお金が渡るイラスト。', f"""
<circle cx="300" cy="130" r="70" class="coralp"/>
<g transform="translate(300 176)"><path d="M0 30l-34-42 16-20 18 18 18-18 16 20z" class="coral o"/></g>
{person(150,346,1.05,1,'teal','blue','give','bob','smile')}
{person(450,346,1.05,-1,'gold','violet','give','short','smile')}
<g transform="translate(300 290)">
  <circle r="22" class="goldp o"/>
  <path d="M-7-10h14v20h-14z" class="goldd"/>
</g>
<path d="M234 290h40" class="a" marker-end="url(#ar)"/>
<path d="M366 290h-40" class="a" marker-end="url(#ar)" transform="translate(0 34)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('climate', '同じ地域の一年を通じた天気の傾向を、太陽・雨・雪で並べたイラスト。', f"""
<circle cx="300" cy="200" r="160" class="muted"/>
{sun(160,150,40)}
{cloud(300,140,1.1)}
<g class="blues"><path d="M270 190l-10 26M300 196l-10 26M330 190l-10 26"/></g>
<g fill="#ffffff" stroke="#cfe0ee" stroke-width="2"><circle cx="430" cy="160" r="10"/><circle cx="460" cy="190" r="8"/><circle cx="410" cy="200" r="7"/></g>
<path d="M180 300q120 40 240 0" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('clumsy', '持っていた皿を取り落とし、うまく扱えていない人のイラスト。', f"""
{person(220,346,1.15,1,'coral','blue','up','short','surprised')}
<g transform="translate(360 200) rotate(24)">
  <ellipse rx="54" ry="20" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(420 280) rotate(-40)">
  <ellipse rx="54" ry="20" fill="#fffdf6" class="o"/>
</g>
<path d="M320 170q60 40 80 90" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('coach', '笛を持って選手に指示を出している指導者のイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
{person(200,346,1.2,1,'teal','blue','point','cap','neutral')}
<g transform="translate(240 226)">
  <path d="M-16-10h32v20h-32z" class="goldd o"/>
  <path d="M16-6h20v12H16z" class="gold o"/>
</g>
{person(450,346,0.9,-1,'coral','gold','walk','short','neutral')}
<path d="M300 210h90" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('coal', '黒いかたまりの石炭が積まれ、燃えているイラスト。', f"""
<g transform="translate(280 300)">
  <g fill="#3d4550" stroke="{INK}" stroke-width="2.5">
    <path d="M-100 40q-20-40 10-60 30-20 60-6 30 14 24 46-4 16-14 20z"/>
    <path d="M20 40q-14-30 8-44 22-14 44-4 22 10 18 34-2 10-8 14z"/>
    <path d="M-60 60q-10-20 6-28 16-8 28-2 12 6 10 20z"/>
  </g>
</g>
{flame(250,250,0.9)}
{flame(330,258,0.7)}
<g class="muted" opacity=".8"><path d="M240 160q-14-30 4-52M320 156q-14-34 6-56"/></g>
""", ground=True)

add('community', '同じ町に住む人たちが、家を囲んで集まっているイラスト。', f"""
<circle cx="300" cy="210" r="160" class="tealp" opacity=".45"/>
{building(300,250,0.7,'teal')}
{person(150,336,0.85,1,'coral','blue','stand','short','smile')}
{person(230,346,0.85,1,'gold','violet','stand','bob','smile')}
{person(370,346,0.85,-1,'violet','teal','stand','cap','smile')}
{person(450,336,0.85,-1,'blue','gold','stand','short','smile')}
<path d="M60 356h480" class="a"/>
""", ground=True)

add('competitor', '同じ走路を並んで走り、競い合う二人のイラスト。', f"""
<path d="M0 320h600v80H0z" fill="#e2b7a2"/>
<path d="M0 360h600" fill="none" stroke="#fffdf6" stroke-width="4"/>
{person(220,340,1.1,1,'coral','blue','walk','short','neutral')}
{person(380,360,1.1,1,'teal','gold','walk','cap','neutral')}
<path d="M480 240h70" class="a" marker-end="url(#ar)"/>
<path d="M300 200v40" class="muted"/>
<g class="corals" style="stroke-width:5"><path d="M300 170l-20-20M300 170l20-20"/></g>
""", ground=False, arrow=True)

add('complain', '不満を訴えて、相手に強く言っている人のイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','point','short','sad')}
{person(450,346,1.1,-1,'teal','violet','stand','bob','neutral')}
<g transform="translate(320 190)">
  <path d="M-70-42h140q16 0 16 16v40q0 16-16 16h-96l-24 22 6-22h-26q-16 0-16-16v-40q0-16 16-16z" class="paper"/>
  <path d="M-8-24h16v34h-16zM-8 18h16v14h-16z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('complaint', '窓口に届いた苦情の紙が、束になって積まれているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160-30h320v20h-320z" class="goldp o"/>
  <path d="M-140-10v70M140-10v70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(300 210)">
  <g transform="rotate(-6)"><path d="M-90-70h180v130h-180z" class="paper"/></g>
  <g transform="rotate(4) translate(0 -14)"><path d="M-90-70h180v130h-180z" class="paper"/>
    <path d="M-8-46h16v56h-16zM-8 22h16v14h-16z" class="coral o"/>
  </g>
</g>
<path d="M470 150q-40 30-70 44" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('concrete', '手で触れる具体的な模型と、点線の抽象的な形を比べたイラスト。', f"""
<g transform="translate(170 240)">{box(0,0,150,110,34,'gold')}</g>
<g transform="translate(430 240)">
  <path d="M-70-50h140v100h-140z" class="muted"/>
  <path d="M-70-50l140 100M70-50L-70 50" class="muted"/>
</g>
{hand(170,120,1)}
<path d="M170 170v20" class="a" marker-end="url(#ar)"/>
<path d="M300 130v200" class="muted"/>
""", ground=True, arrow=True)

add('container', 'ふた付きの容器に中身を入れて、保存しているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(280 280)">
  <path d="M-100-60h200l-14 120h-172z" fill="#eef4f8" class="o"/>
  <path d="M-100-60h200" class="a"/>
  <g class="goldp o"><circle cx="-40" cy="10" r="22"/><circle cx="10" cy="20" r="22"/><circle cx="52" cy="6" r="22"/></g>
</g>
<g transform="translate(280 176)">
  <path d="M-110-14h220v22h-220z" class="teal o"/>
  <path d="M-16-14h32v-12h-32z" class="teald o"/>
</g>
<path d="M280 130v20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('continue', 'とぎれずに先へ続いていく線と、まだ先があることを示す矢印のイラスト。', f"""
<path d="M60 200h380" fill="none" stroke="{TONES['teal'][0]}" stroke-width="16" stroke-linecap="round"/>
<path d="M450 200h90" class="teals" style="stroke-width:8" marker-end="url(#ar)" stroke-dasharray="14 12"/>
<g fill="{INK}"><circle cx="60" cy="200" r="10"/></g>
<path d="M200 280h300" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('control', 'つまみとレバーで機械の動きを操作しているイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-180-90h360v180h-360z" fill="#dfe6ea" class="o"/>
  <circle cx="-100" cy="-20" r="40" class="tealp o"/>
  <path d="M-100-20l24-26" class="a"/>
  <circle cx="0" cy="-20" r="40" class="coralp o"/>
  <path d="M0-20l-26-22" class="a"/>
  <path d="M90-70v100" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="90" cy="-74" r="14" class="coral o"/>
  <g class="green o"><circle cx="-140" cy="50" r="12"/><circle cx="-100" cy="50" r="12"/></g>
</g>
{hand(430,150,-1)}
""", ground=True)

add('copy', '原本と同じ内容の紙が、もう一枚できているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="bluep"/>
<g transform="translate(190 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-70h120M-60-40h120M-60-10h100M-60 20h110"/></g>
</g>
<g transform="translate(400 250)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-70h120M-60-40h120M-60-10h100M-60 20h110"/></g>
</g>
<path d="M290 160h30" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('cottage', '屋根の低い小さな家が、庭の中に立っているイラスト。', f"""
{tree(500,340,0.7)}
<g transform="translate(260 340)">
  <path d="M-110 0v-90h220V0z" fill="#fffdf6" class="o"/>
  <path d="M-130-90L0-180l130 90z" class="coral o"/>
  <path d="M-30 0v-60h60V0z" class="goldd o"/>
  <rect x="-86" y="-70" width="40" height="34" class="bluep o"/>
  <rect x="46" y="-70" width="40" height="34" class="bluep o"/>
  <path d="M60-140h20v34h-20z" class="ink"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('cry', '涙をこぼして泣いている顔のイラスト。', f"""
{face(300,190,130,'sad')}
{drop(250,250,1.4)}{drop(348,256,1.4)}
{drop(240,320,1.1)}{drop(356,326,1.1)}
""", ground=False)

add('deal', '二人が握手して、取引の合意ができたイラスト。', f"""
<circle cx="300" cy="130" r="70" class="greenp"/>
{person(170,346,1.1,1,'teal','blue','give','short','smile')}
{person(430,346,1.1,-1,'coral','gold','give','bob','smile')}
<g transform="translate(300 258)">
  <path d="M-40-16h80q14 0 14 16t-14 16h-80q-14 0-14-16t14-16z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M0-16v32" fill="none" stroke="{SKINL}" stroke-width="2"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M270 170l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('desert', '砂の丘とサボテンが並ぶ、雨の少ない砂漠のイラスト。', f"""
{sun(480,90,48)}
<path d="M0 250q120-50 240-10t360-30v190H0z" fill="#efdcb8" stroke="{INK}" stroke-width="3"/>
<g transform="translate(200 300)">
  <path d="M-14 0v-110h28V0z" class="green o"/>
  <path d="M-14-70h-30v40h30M14-84h30v46h-30" fill="none" stroke="{TONES['green'][0]}" stroke-width="20" stroke-linecap="round"/>
</g>
<g fill="none" stroke="#dcc79c" stroke-width="3"><path d="M300 340q60-16 120 0M100 370q60-16 120 0"/></g>
""", ground=False)

add('destination', '道の終わりに立つ旗の場所へ、たどり着くイラスト。', f"""
<path d="M60 340q120-60 240-40t240-60" fill="none" stroke="#e6dcc9" stroke-width="30" stroke-linecap="round"/>
<path d="M500 240V110" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
<path d="M508 116l70 22-70 22z" class="coral o"/>
{person(160,336,0.9,1,'teal','blue','walk','short','smile')}
<path d="M240 240q140-40 240-30" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('device', '小さな画面とボタンが付いた携帯機器のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="bluep"/>
<g transform="translate(280 220)">
  <path d="M-90-130h180q14 0 14 14v232q0 14-14 14h-180q-14 0-14-14v-232q0-14 14-14z" fill="#dfe6ea" class="o"/>
  <path d="M-70-104h140v170h-140z" class="bluep o"/>
  <circle cy="94" r="20" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-40-116h80" class="a"/>
</g>
{hand(430,260,-1)}
""", ground=True)

add('dirt', '手のひらにのせた土と、地面の土を示したイラスト。', f"""
<path d="M0 260h600v140H0z" fill="#e7d9c4"/>
<path d="M0 260h600" class="a"/>
<g fill="#c9a97c"><circle cx="120" cy="300" r="8"/><circle cx="180" cy="330" r="6"/><circle cx="460" cy="310" r="7"/><circle cx="520" cy="340" r="5"/></g>
{hand(300,200,1)}
<g fill="#8e7350" stroke="{INK}" stroke-width="2"><path d="M270 176q30-24 60 0 10 10-30 12t-30-12z"/></g>
<path d="M300 130v30" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('domestic', '家の中の家事と、国境の内側を示したイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-120 90V-40h240V90z" fill="#fffdf6" class="o"/>
  <path d="M-136-40L0-140l136 100z" class="teal o"/>
  <g transform="translate(0 40) scale(0.55)">{person(0,0,1.0,1,'coral','blue','carry','bob','smile')}</g>
</g>
<g transform="translate(470 250)">
  <circle r="90" class="tealp o"/>
  <path d="M-90 0h180M0-90v180" fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"/>
  <circle r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('download', '雲の中のファイルが、下の機器へ矢印に沿って落ちてくるイラスト。', f"""
{cloud(300,110,1.8)}
<g transform="translate(300 220)">
  <path d="M-16-40h32v50h-32z" class="teal o"/>
  <path d="M-34 10h68L0 50z" class="teal o"/>
</g>
<g transform="translate(300 330)">
  <path d="M-110-30h220v50h-220z" fill="#dfe6ea" class="o"/>
  <path d="M-70-30v-14h140v14z" class="ink"/>
</g>
<path d="M440 180v100" class="teals" marker-end="url(#ar)" style="stroke-width:6"/>
""", ground=True, arrow=True)

add('dream', '眠っている人の頭の上に、夢の場面が雲の中で浮かんでいるイラスト。', f"""
<g transform="translate(180 320)">
  <path d="M-110-30h220v40h-220z" class="tealp o"/>
  <ellipse cx="-60" cy="-46" rx="40" ry="24" fill="#fffdf6" class="o"/>
  <g transform="translate(-60 -60)">
    <circle r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-24-2q3-28 25-28 24 0 27 26-13-10-27-4-12-11-25 6z" fill="{HAIR}"/>
    <path d="M-9 2h6M9 2h-6" class="a"/>
  </g>
</g>
<g transform="translate(410 160)">
  <path d="M-150 40q-16-70 50-84 20-56 96-40 46 6 60 54 74-8 82 60 4 60-64 66h-180q-46-4-44-56z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 16)">
    {sun(-60,-6,26)}
    <path d="M20 30L60-20l40 50z" class="tealp o"/>
  </g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="230" cy="250" r="12"/><circle cx="200" cy="276" r="8"/></g>
""", ground=True)

add('dumb', '口が閉じて言葉が出ず、吹き出しが空のままのイラスト。', f"""
{person(240,346,1.2,1,'violet','blue','stand','short','neutral')}
<g transform="translate(410 190)">
  <path d="M-70-46h140q16 0 16 16v50q0 16-16 16h-96l-26 24 6-24h-24q-16 0-16-16v-50q0-16 16-16z" class="paper"/>
</g>
<path d="M240 232h30" fill="none" stroke="{INK}" stroke-width="4"/>
<g class="corals" style="stroke-width:6"><path d="M320 200l-24-24M296 200l24-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('elaborate', '簡単な形に細かい模様を足して、手の込んだ飾りにしているイラスト。', f"""
<g transform="translate(160 230)">
  <circle r="80" class="tealp o"/>
</g>
<g transform="translate(430 230)">
  <circle r="80" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3">
    <circle r="60"/><circle r="40"/><circle r="20"/>
    <path d="M-80 0h160M0-80v160M-56-56l112 112M56-56L-56 56"/>
  </g>
  <g class="goldp o"><circle cx="0" cy="-60" r="10"/><circle cx="60" cy="0" r="10"/><circle cx="0" cy="60" r="10"/><circle cx="-60" cy="0" r="10"/></g>
</g>
<path d="M270 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('employment', '面接に通って職場に迎えられ、働き始めるイラスト。', f"""
{building(430,300,1.0,'teal')}
{person(160,346,1.1,1,'coral','blue','walk','short','smile')}
<g transform="translate(280 250)">
  <path d="M-50-60h100v120h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-34h60M-30-10h60M-30 14h40"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-20 38l12 12 22-24"/></g>
</g>
<path d="M340 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('entrance', '建物の正面にある入口の扉と、そこへ続く階段のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-190 120V-90h380v210z" fill="#fffdf6" class="o"/>
  <path d="M-206-90h412l-40-50h-332z" class="teal o"/>
  <path d="M-60 120V-10h120v130z" class="goldd o"/>
  <path d="M-60-10h120" class="a"/>
  <circle cx="40" cy="60" r="8" class="goldp"/>
</g>
<path d="M180 360h240l-20-20h-200z" class="ground"/>
<path d="M180 360h240" class="a"/>
<path d="M300 400v-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('place', '地図の上のある一点を指し示しているイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-200 40q100-40 200 0t200-20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <path d="M-140-80h100v60h-100z" class="greenp o"/>
  <path d="M40-100h120v70H40z" class="goldp o"/>
</g>
<g transform="translate(340 200)">
  <path d="M0 40c-30-40-40-56-40-72a40 40 0 0 1 80 0c0 16-10 32-40 72z" class="coral o"/>
  <circle cy="-34" r="13" fill="#fffdf6"/>
</g>
""", ground=True)
print(' '.join(W)); print(sheet(W))
