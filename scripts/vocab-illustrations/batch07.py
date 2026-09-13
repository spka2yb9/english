"""第7回: 見る・つかむ・空と天気・家具などの30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('sink', '蛇口の下に水を受ける流し台があり、水がたまっているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-170 0h340v20h-340z" fill="#dfe6ea" class="o"/>
  <path d="M-130 20h260l-24 120h-212z" fill="#eef4f8" class="o"/>
  <path d="M-104 70h208l-16 60h-176z" class="bluep o"/>
  <path d="M-104 70h208" class="a"/>
  <ellipse cy="132" rx="26" ry="8" class="ink"/>
</g>
<path d="M300 100v-40h-90" fill="none" stroke="#cfd8de" stroke-width="16" stroke-linecap="round"/>
<path d="M300 100v20" fill="none" stroke="#cfd8de" stroke-width="22"/>
<path d="M210 60v-24" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M300 130v130" fill="none" stroke="{TONES['blue'][0]}" stroke-width="12" stroke-linecap="round"/>
<path d="M300 130v130" fill="none" stroke="#9dc6ea" stroke-width="4" stroke-linecap="round"/>
""", ground=True)

add('strange', '同じ形の器が並ぶ中に、一つだけ形の違う器がまざっているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
<g class="tealp o">
  <path d="M100 300h80l-8-90h-64z"/><path d="M200 300h80l-8-90h-64z"/><path d="M400 300h80l-8-90h-64z"/>
</g>
<g transform="translate(340 250)">
  <path d="M-40 50q-30-60 10-90 30-22 60 4 26 22 4 56-16 26-34 30z" class="violet o"/>
  <path d="M-10-30q24-10 40 8" fill="none" stroke="{TONES['violet'][1]}" stroke-width="3"/>
</g>
<path d="M340 130v46" class="a" marker-end="url(#ar)"/>
<path d="M60 300h480" class="a"/>
""", ground=True, arrow=True)

add('trick', '手品師の帽子から、うさぎが飛び出してくるイラスト。', f"""
<circle cx="470" cy="100" r="56" class="violetp"/>
<g transform="translate(280 300)">
  <ellipse cy="0" rx="130" ry="26" class="violetd o"/>
  <path d="M-80 0v-110h160V0z" class="violet o"/>
  <path d="M-80-30h160" fill="none" stroke="{TONES['violet'][1]}" stroke-width="10"/>
</g>
<g transform="translate(300 150)">
  <ellipse rx="40" ry="34" fill="#fffdf6" class="o"/>
  <path d="M-22-26q-14-50 4-52 16-2 16 40z" fill="#fffdf6" class="o"/>
  <path d="M18-30q10-48 26-44 14 4-6 44z" fill="#fffdf6" class="o"/>
  <circle cx="-12" cy="-4" r="3.4" class="ink"/><circle cx="14" cy="-4" r="3.4" class="ink"/>
  <path d="M-6 12q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <ellipse cx="1" cy="6" rx="6" ry="4" class="coral"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M200 130l-26-22M400 130l26-22M180 200h-30M420 200h30"/></g>
""", ground=True)

add('airline', '航空会社の旅客機が、雲の上を飛んでいるイラスト。', f"""
{cloud(120,120,1.2)}{cloud(470,180,1.0)}{cloud(240,320,1.4)}
{plane(300,220,1.1,-8,'teal')}
<path d="M60 260q90-30 170-40" class="muted"/>
""", ground=False)

add('align', 'ばらばらに置かれた棒を、一直線にそろえて並べ直しているイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 8"><path d="M60 120h480"/></g>
<g class="tealp o">
  <rect x="80" y="90" width="90" height="26" transform="rotate(-14 125 103)"/>
  <rect x="220" y="98" width="90" height="26" transform="rotate(9 265 111)"/>
  <rect x="370" y="86" width="90" height="26" transform="rotate(-6 415 99)"/>
</g>
<g class="teal o">
  <rect x="80" y="250" width="90" height="26"/><rect x="180" y="250" width="90" height="26"/>
  <rect x="280" y="250" width="90" height="26"/><rect x="380" y="250" width="90" height="26"/>
</g>
<path d="M60 250h480" class="a"/>
<path d="M300 170v50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('architect', '図面を広げて建物の設計を描いている人と、完成予想の建物のイラスト。', f"""
{building(460,260,1.0,'teal')}
<g transform="translate(200 260)">
  <path d="M-130-60h260v120h-260z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3">
    <path d="M-90-30h80v70h-80zM-50-30v70M10-10h70v50h-70z"/>
    <path d="M-100-40h180" stroke-dasharray="6 6"/>
  </g>
</g>
{person(200,376,0.9,1,'coral','blue','point','cap','neutral')}
<path d="M300 200q60-30 100-20" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('athlete', 'ゼッケンをつけた選手が、トラックを全力で走っているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="goldp"/>
<path d="M0 330h600v70H0z" fill="#e2b7a2"/>
<g fill="none" stroke="#fffdf6" stroke-width="4"><path d="M0 350h600M0 380h600"/></g>
{person(280,330,1.3,1,'coral','blue','walk','short','neutral')}
<rect x="256" y="240" width="48" height="34" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
<g class="muted"><path d="M180 250q-40 10-50 30M170 300q-40 6-54 22"/></g>
<path d="M400 260h80" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('blank', '何も書かれていない一枚の白い紙のイラスト。線だけが引かれている。', f"""
<circle cx="470" cy="96" r="54" class="bluep"/>
<g transform="translate(280 220)">
  <path d="M-120-140h240v280h-240z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="8 8">
    <path d="M-90-80h180M-90-30h180M-90 20h180M-90 70h180"/>
  </g>
</g>
<path d="M420 200q-40 10-60 14" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('blast', '爆発の衝撃で、周りの物が外へ吹き飛ばされているイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-140 0l60-30-30-60 70 20 20-70 30 68 66-30-24 62 74 10-60 40 50 50-72-8-10 66-46-56-56 44 10-66z" class="coral o"/>
  <path d="M-70 0l40-16-16-34 40 12 12-40 18 40 36-18-14 36 42 6-34 22 28 28-40-4-6 38-26-32-32 26 6-38z" class="goldp o"/>
</g>
<g class="corals" marker-end="url(#ar)" style="stroke-width:5">
  <path d="M120 130L60 80"/><path d="M480 130l60-50"/><path d="M120 290L60 340"/><path d="M480 290l60 50"/>
</g>
{box(90,330,60,44,0,'gold')}
{box(520,330,60,44,0,'gold')}
""", ground=True, arrow=True)

add('blend', '二色の液体をミキサーで混ぜ合わせて、一つの色にしているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
<g transform="translate(280 220)">
  <path d="M-80-120h160l-14 200h-132z" fill="#f4fbff" class="o"/>
  <path d="M-80-120h160" class="a"/>
  <path d="M-72-40h144l-10 116h-124z" class="violetp o"/>
  <path d="M-60-40q40 26 72 0t60 6" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M-66 20q46 24 76 0t62 4" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
  <path d="M-100 80h200v40h-200z" fill="#dfe6ea" class="o"/>
  <circle cx="60" cy="100" r="10" class="coral o"/>
</g>
<path d="M150 160a130 60 0 0 0 250 0" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('cartoon', '四角い枠の中に、吹き出し付きの簡単な絵が描かれた漫画のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-170-110h160v100h-160zM10-110h160v100H10zM-170 10h160v100h-160zM10 10h160v100H10z" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
  {face(-90,-64,30,'smile')}
  <path d="M-30-96h60q10 0 10 10v20q0 10-10 10h-40l-14 12 4-12q-10 0-10-10v-20q0-10 10-10z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
  {face(90,-64,30,'grin')}
  {face(-90,56,30,'sad')}
  {face(90,56,30,'flat')}
</g>
""", ground=True)

add('carve', 'のみと木づちで木を削り、模様を彫り出しているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(280 290)">
  <path d="M-160-40h320v80h-320z" class="goldp o"/>
  <path d="M-160-40h320" class="a"/>
  <path d="M-90-10q30-30 60 0t60 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
  <path d="M-60 20q30-26 60 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
</g>
<g transform="translate(300 190) rotate(20)">
  <path d="M-9-90h18v70h-18z" class="goldd o"/>
  <path d="M-9-20h18l-9 34z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(410 150) rotate(-30)">
  <path d="M-40-24h80v48h-80z" class="goldd o"/>
  <path d="M0 24v70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
</g>
<g fill="#e0cba8"><circle cx="230" cy="230" r="6"/><circle cx="212" cy="252" r="5"/><circle cx="250" cy="256" r="4"/></g>
""", ground=True)

add('check', 'リストの項目を一つずつ確かめて、チェック印を付けているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
<g transform="translate(280 220)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-90h170M-60-30h170M-60 30h170M-60 90h170"/></g>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><rect x="-116" y="-108" width="36" height="36"/><rect x="-116" y="-48" width="36" height="36"/><rect x="-116" y="12" width="36" height="36"/><rect x="-116" y="72" width="36" height="36"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
    <path d="M-110-92l14 14 22-26M-110-32l14 14 22-26M-110 28l14 14 22-26"/>
  </g>
</g>
<path d="M430 240q-40 26-58 44" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('cloud', '空にうかぶ白い雲を描いたイラスト。', f"""
{sun(500,90,44)}
{cloud(240,180,2.2)}
{cloud(440,280,1.2)}
{cloud(110,300,1.0)}
""", ground=False)

add('coast', '海と陸が接する海岸線を、上から見たイラスト。', f"""
<path d="M0 0h600v400H0z" class="bluep"/>
<path d="M0 400h600V150q-90 30-170 10T290 130 150 200 0 190z" fill="#e4efe2" stroke="{INK}" stroke-width="3"/>
<path d="M0 190q150 10 150-10t140 20 140 40 170-10" fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
{tree(120,330,0.7)}{tree(460,340,0.6)}
<g class="blues" opacity=".7"><path d="M40 90q50-14 100 0t100 0M340 60q50-14 100 0t100 0M60 130q40-10 80 0"/></g>
""", ground=False)

add('collapse', '積み上げた箱の山が支えを失い、崩れ落ちていくイラスト。', f"""
{box(160,300,90,66,0,'gold')}
{box(160,232,90,66,0,'gold')}
<g transform="rotate(28 380 300)">{box(380,300,90,66,0,'gold')}</g>
<g transform="rotate(-46 470 330)">{box(470,330,90,66,0,'gold')}</g>
<g transform="rotate(64 300 350)">{box(300,350,90,66,0,'gold')}</g>
<g class="corals" marker-end="url(#ar)" style="stroke-width:5"><path d="M240 200l60 60"/><path d="M300 170q90 20 120 80"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('dark', '明かりが消えて、部屋の中が暗くなっているイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a4a"/>
<path d="M60 60h200v180H60z" fill="#1e2a36" stroke="#4a5c6e" stroke-width="3"/>
<path d="M160 60v180M60 150h200" fill="none" stroke="#4a5c6e" stroke-width="3"/>
<circle cx="440" cy="120" r="46" fill="#3a4a5c" stroke="#556777" stroke-width="3"/>
<path d="M440 74V40" fill="none" stroke="#556777" stroke-width="4"/>
<path d="M0 330h600v70H0z" fill="#22303e"/>
<g fill="#f7e6a8"><circle cx="120" cy="110" r="4"/><circle cx="200" cy="180" r="3"/></g>
""", ground=False)

add('dip', 'クッキーをカップの中の飲み物に、少しだけ浸しているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(280 260)">
  <path d="M-90-70h180l-18 130h-144z" fill="#fffdf6" class="o"/>
  <path d="M-90-70h180" class="a"/>
  <path d="M-80-36h160l-14 96h-132z" class="goldp o"/>
  <path d="M-80-36h160" class="a"/>
  <path d="M90-50q40 0 40 28t-40 28" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
<g transform="translate(300 170) rotate(16)">
  <circle r="42" class="goldd o"/>
  <g fill="{INK}"><circle cx="-14" cy="-10" r="5"/><circle cx="12" cy="4" r="5"/><circle cx="-4" cy="20" r="5"/><circle cx="18" cy="-18" r="5"/></g>
</g>
<path d="M380 150v70" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('drive', 'ハンドルを握って車を運転しているイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200 40h400l-20-60h-60l-40-60h-140l-40 60h-80z" class="coral o"/>
  <path d="M-140-20h100v-46h-70zM-20-66h90l30 46H-20z" class="bluep o"/>
  <circle cx="-110" cy="50" r="34" class="ink"/><circle cx="110" cy="50" r="34" class="ink"/>
  <circle cx="-110" cy="50" r="14" fill="#dfe6ea"/><circle cx="110" cy="50" r="14" fill="#dfe6ea"/>
</g>
<g transform="translate(200 216)">
  <circle r="26" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-26 0h52M0 0v26" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<circle cx="200" cy="180" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M420 190h80" class="a" marker-end="url(#ar)"/>
<path d="M40 320h520" class="a"/>
""", ground=True, arrow=True)

add('drop', '手からコップがすべり落ちて、床へ向かっているイラスト。', f"""
<path d="M120 120h140" fill="none" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>
<circle cx="270" cy="120" r="20" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<g transform="translate(320 260) rotate(18)">
  <path d="M-46-56h92l-12 100h-68z" fill="#f4fbff" class="o"/>
  <path d="M-46-56h92" class="a"/>
  <path d="M-38-16h76l-8 60h-60z" class="bluep o"/>
</g>
{drop(392,180,1.0)}{drop(250,210,0.8)}
<path d="M320 140v70" class="a" marker-end="url(#ar)"/>
<path d="M80 350h440" class="a"/>
""", ground=True, arrow=True)

add('erupt', '火山の火口から溶岩と煙が噴き上がっているイラスト。', f"""
<path d="M60 340L300 90l240 250z" class="tealp o"/>
<path d="M300 90l50 52h-100z" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
<g class="muted" opacity=".9"><path d="M270 60q-20-40 6-60M330 60q20-40-6-60M300 30q0-30 0-30"/></g>
<g class="corals" marker-end="url(#ar)" style="stroke-width:6">
  <path d="M280 90L230 20"/><path d="M320 90l50-70"/><path d="M300 84V10"/>
</g>
<path d="M290 130q-30 80-70 130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" stroke-linecap="round"/>
<path d="M320 130q30 70 80 120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" stroke-linecap="round"/>
<g class="coral o"><circle cx="200" cy="60" r="12"/><circle cx="410" cy="70" r="10"/><circle cx="150" cy="130" r="9"/></g>
""", ground=True, arrow=True)

add('fan', '羽根が回る扇風機から、風が前へ送り出されているイラスト。', f"""
<g transform="translate(230 220)">
  <circle r="100" fill="none" stroke="{INK}" stroke-width="6"/>
  <g class="tealp o">
    <path d="M0 0q60-40 76 20-46 30-76-20z"/>
    <path d="M0 0q-10 72-70 40 12-52 70-40z" transform="rotate(120)"/>
    <path d="M0 0q-66-32-36-86 46 22 36 86z" transform="rotate(240)"/>
  </g>
  <circle r="18" class="teald o"/>
  <path d="M0 100v70" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-56 176h112" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
<g class="muted" marker-end="url(#ar)">
  <path d="M350 160q80-20 180 0"/><path d="M350 220q80-20 180 0"/><path d="M350 280q80-20 180 0"/>
</g>
""", ground=True, arrow=True)

add('fly', '鳥が翼を広げて空を飛んでいるイラスト。', f"""
{cloud(120,110,1.2)}{cloud(470,250,1.0)}
<g transform="translate(290 190)">
  <path d="M0 0c-40-16-40-52 10-52 34 0 54 20 54 44 0 22-26 34-64 8z" class="teal o"/>
  <path d="M4-34c-24-40 30-64 56-30 20 26-14 46-56 30z" class="tealp o"/>
  <path d="M2-30c26-44 80-20 74 16-6 30-52 20-74-16z" class="tealp o" transform="translate(-40 40)"/>
  <path d="M62-26l30-12-20 26z" class="gold o"/>
  <circle cx="46" cy="-34" r="3.6" class="ink"/>
</g>
<path d="M120 260q90-40 150-50" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('furniture', 'いす・机・たなが並んだ室内の家具のイラスト。', f"""
<g transform="translate(150 280)">
  <path d="M-60-40h20v90h-20zM40-40h20v90H40z" class="goldd o"/>
  <path d="M-60-60h120v22h-120z" class="goldp o"/>
  <path d="M-60-120h20v60h-20z" class="goldd o"/>
</g>
<g transform="translate(320 290)">
  <path d="M-90-20h180v18h-180z" class="goldp o"/>
  <path d="M-80-2v62M70-2v62" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(490 250)">
  <path d="M-70-100h140v200h-140z" class="goldp o"/>
  <path d="M-70-40h140M-70 30h140" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
  <g class="coral o"><rect x="-56" y="-84" width="20" height="40"/><rect x="-30" y="-84" width="20" height="40"/></g>
  <g class="tealp o"><rect x="-56" y="-14" width="60" height="40"/></g>
</g>
<path d="M40 350h520" class="a"/>
""", ground=True)

add('gaze', '一点をじっと見つめ続けている人と、視線を示す長い線のイラスト。', f"""
{person(160,336,1.1,1,'teal','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">
  <path d="M200 216h300" marker-end="url(#ar)"/>
  <path d="M200 226h300" marker-end="url(#ar)"/>
</g>
<circle cx="520" cy="220" r="34" class="goldp o"/>
<circle cx="520" cy="220" r="12" class="gold o"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('glance', '横を向いて一瞬だけ目を向けている人と、短い視線のイラスト。', f"""
{person(220,336,1.1,1,'coral','blue','stand','bob','neutral')}
<path d="M262 216l80-6" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)" stroke-dasharray="10 8"/>
<circle cx="410" cy="206" r="30" class="goldp o"/>
<circle cx="410" cy="206" r="10" class="gold o"/>
<path d="M470 130q30 20 30 44" class="muted"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('goal', 'ゴールの旗に向かって進み、最後の一歩でたどり着くイラスト。', f"""
<path d="M480 340V90" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
<path d="M488 96l90 26-90 26z" class="coral o"/>
<circle cx="480" cy="340" r="16" class="goldp o"/>
<path d="M60 340h420" fill="none" stroke="#e6dcc9" stroke-width="34" stroke-linecap="round"/>
{person(360,340,1.0,1,'teal','gold','walk','short','smile')}
<path d="M120 250q140-40 300-20" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('grab', '差し出されたかばんの取っ手を、手ですばやくつかみ取るイラスト。', f"""
<circle cx="120" cy="100" r="56" class="coralp"/>
<g transform="translate(330 290)">
  <path d="M-90-40h180v100h-180z" class="tealp o"/>
  <path d="M-40-40q0-40 40-40t40 40" fill="none" stroke="{INK}" stroke-width="8"/>
  <path d="M-90 0h180" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
</g>
{hand(330,206,1)}
<g class="corals" style="stroke-width:4"><path d="M400 150l24-24M420 190l30-14M380 130l6-30"/></g>
<path d="M200 190q60-30 96-12" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('grin', '歯を見せて大きくにっと笑っている顔のイラスト。', f"""
{face(300,200,140,'grin')}
<circle cx="180" cy="240" r="20" class="coralp"/><circle cx="420" cy="240" r="20" class="coralp"/>
<g class="golds" style="stroke-width:4"><path d="M120 120l-30-24M480 120l30-24M110 200H74M490 200h36"/></g>
""", ground=False)

add('headache', '頭を手で押さえ、頭の中で痛みが響いている人のイラスト。', f"""
{person(300,346,1.2,1,'teal','blue','up','short','sad')}
<g class="corals" opacity=".95" style="stroke-width:5">
  <path d="M240 190q-30-20-30-50M360 190q30-20 30-50M300 160v-40"/>
  <path d="M214 150l-30-14M386 150l30-14"/>
</g>
<g transform="translate(300 216)"><path d="M-40-30l16 20-20 16 22 20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)
print(' '.join(W)); print(sheet(W))
