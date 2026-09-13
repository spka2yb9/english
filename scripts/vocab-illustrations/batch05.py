"""第5回: 状態変化・出入り・形状・自然物の30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('boil', 'なべの水がぶくぶくと泡立ち、湯気が上がって沸騰しているイラスト。', f"""
<g class="muted" opacity=".9"><path d="M250 130q-16-40 6-70M300 120q-16-46 8-78M352 132q-16-40 6-70"/></g>
<g transform="translate(300 250)">
  <path d="M-130-56h260l-16 116h-228z" fill="#dfe6ea" class="o"/>
  <path d="M-130-56h260" class="a"/>
  <path d="M130-40q42 0 42 22t-42 22" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-116-30h232l-14 88h-204z" class="bluep o"/>
  <g class="blue o"><circle cx="-70" cy="4" r="13"/><circle cx="-24" cy="18" r="10"/><circle cx="20" cy="0" r="15"/><circle cx="64" cy="16" r="11"/><circle cx="-46" cy="-16" r="8"/><circle cx="44" cy="-18" r="9"/></g>
</g>
{flame(268,352,0.9)}
{flame(330,352,0.7)}
""", ground=True)

add('stream', '林の間を細く流れていく小川のイラスト。水の流れる向きを矢印が示す。', f"""
{tree(90,180,0.9)}{tree(510,170,0.8)}
<path d="M0 300q100-40 190 0t210 10 200-30v120H0z" class="bluep o"/>
<path d="M0 300q100-40 190 0t210 10 200-30" class="a"/>
<g class="blues" opacity=".8" marker-end="url(#ar)">
  <path d="M80 340q110-32 210 6t230-16"/>
  <path d="M60 376q110-30 220 8t250-14"/>
</g>
<g fill="#cfc3ab" stroke="{INK}" stroke-width="2"><ellipse cx="180" cy="326" rx="22" ry="12"/><ellipse cx="420" cy="348" rx="18" ry="10"/></g>
""", ground=False, arrow=True)

add('pump', 'ポンプのハンドルを押し下げると、管の中の水が上へくみ上げられるイラスト。', f"""
<path d="M0 300h600v100H0z" fill="#e7d9c4"/>
<path d="M0 300h600" class="a"/>
<path d="M290 300v90h30v-90z" fill="#cfd8de" stroke="{INK}" stroke-width="3"/>
<path d="M296 380h18" class="blue"/>
<g transform="translate(300 240)">
  <path d="M-40 60h80V-40h-80z" fill="#dfe6ea" class="o"/>
  <path d="M-40-40h80l-14-26h-52z" class="tealp o"/>
  <path d="M30-20h110l-8 46H30z" fill="#dfe6ea" class="o"/>
  <path d="M-30-66v-30h-70" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M306 340V262" class="blues" marker-end="url(#ar)" style="stroke-width:6"/>
<path d="M420 236q40 6 60 34" class="blues" marker-end="url(#ar)"/>
<path d="M200 130v40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('tie', 'ひもの両端を交差させて結び目をつくり、しっかり結んでいるイラスト。', f"""
<circle cx="470" cy="110" r="60" class="violetp"/>
<path d="M60 200q120-60 180 20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round"/>
<path d="M540 200q-120-60-180 20" fill="none" stroke="{TONES['teal'][0]}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(300 236)">
  <path d="M-60-16q60-40 120 0-60 40-120 0z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-40 24q40-50 80 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="16" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 320q40-24 70-30"/><path d="M420 320q-40-24-70-30"/></g>
""", ground=False, arrow=True)

add('enter', '建物の開いた入口へ、外から中へ入っていく人のイラスト。', f"""
{building(400,300,1.15,'teal')}
<path d="M382 300v-46h36v46z" fill="#3d4c5c"/>
{person(170,336,1.0,1,'coral','blue','walk','short','neutral')}
<path d="M230 250h130" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('exit', '建物の出口の扉から、外へ出ていく人のイラスト。', f"""
{building(180,300,1.15,'teal')}
<path d="M162 300v-46h36v46z" fill="#3d4c5c"/>
{person(420,336,1.0,1,'coral','blue','walk','short','neutral')}
<path d="M240 250h130" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('cross', '横断歩道で道路の反対側へ渡っていく人のイラスト。', f"""
<path d="M0 190h600v150H0z" fill="#d8d3ca"/>
<path d="M0 190h600M0 340h600" class="a"/>
<g fill="#fffdf6"><rect x="240" y="196" width="46" height="26"/><rect x="240" y="234" width="46" height="26"/><rect x="240" y="272" width="46" height="26"/><rect x="240" y="310" width="46" height="26"/></g>
{person(180,376,0.95,1,'teal','blue','walk','short','smile')}
<path d="M240 130h130" class="a" marker-end="url(#ar)"/>
<path d="M0 376h600" class="a" opacity=".3"/>
""", ground=False, arrow=True)

add('block', '道の途中に置かれた大きな石が通り道をふさいでいるイラスト。', f"""
<path d="M40 320h520" fill="none" stroke="#e6dcc9" stroke-width="54" stroke-linecap="round"/>
<g transform="translate(340 280)">
  <path d="M-80 40q-24-58 10-86 36-30 84-14 44 16 40 62 0 26-18 38z" fill="#b9b1a3" class="o"/>
  <path d="M-40-30q30-16 60 4" fill="none" stroke="#9a9284" stroke-width="3"/>
</g>
<path d="M120 250h100" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:8"><path d="M232 220l52 52M284 220l-52 52"/></g>
""", ground=True, arrow=True)

add('lock', '南京錠のつるが閉じてかかり、開かないように締められているイラスト。', f"""
<circle cx="470" cy="110" r="58" class="tealp"/>
<g transform="translate(280 230)">
  <path d="M-46-40v-30a46 46 0 0 1 92 0v30" fill="none" stroke="{INK}" stroke-width="16"/>
  <path d="M-70-40h140q12 0 12 12v96q0 12-12 12h-140q-12 0-12-12v-96q0-12 12-12z" class="goldp o"/>
  <circle cx="0" cy="14" r="16" class="ink"/>
  <path d="M0 30v26" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M150 176q30-20 56-22"/><path d="M410 176q-30-20-56-22"/></g>
""", ground=True, arrow=True)

add('knock', '閉じた扉を握りこぶしで叩き、音が広がっているイラスト。', f"""
<path d="M180 40h240v340H180z" fill="#e7dcc9" stroke="{INK}" stroke-width="3"/>
<circle cx="392" cy="220" r="12" class="goldd"/>
<g transform="translate(150 200)">
  <path d="M-40 30h30v-52a26 26 0 0 1 52 0v52h-30z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-40 30h-60" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:5">
  <path d="M196 150q26 30 26 70t-26 70"/>
  <path d="M226 128q34 36 34 92t-34 92"/>
</g>
""", ground=True)

add('press', '指がボタンを押し下げて、ボタンが沈んでいるイラスト。', f"""
<circle cx="120" cy="110" r="58" class="coralp"/>
<g transform="translate(300 300)">
  <path d="M-110 30h220v40h-220z" fill="#dfe6ea" class="o"/>
  <circle cx="0" cy="18" r="56" class="coralp o"/>
  <circle cx="0" cy="24" r="42" class="coral o"/>
  <path d="M-42 6a42 42 0 0 1 84 0" fill="none" stroke="#fde9e3" stroke-width="4"/>
</g>
<path d="M300 150v70" class="a" marker-end="url(#ar)"/>
<path d="M300 120q-40-40-90-24" fill="none" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>
<circle cx="300" cy="120" r="18" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
""", ground=True, arrow=True)

add('burn', 'たき木が炎を上げて燃え、煙が立ちのぼっているイラスト。', f"""
<g class="muted" opacity=".8"><path d="M270 130q-20-46 4-80M330 120q-20-50 6-84"/></g>
{flame(300,270,1.7)}
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round">
  <path d="M210 330l180-40M390 330L210 290"/>
</g>
<g class="golds" opacity=".8"><path d="M180 250l-24-16M420 250l24-16M170 300h-30M430 300h30"/></g>
""", ground=True)

add('cool', 'あつい飲み物が湯気を止め、温度計の目盛りが下がって冷めていくイラスト。', f"""
{thermometer(430,300,0.28,1.0)}
<g transform="translate(240 250)">
  <path d="M-74-60h148l-18 110h-112z" fill="#fffdf6" class="o"/>
  <path d="M-74-60h148" class="a"/>
  <path d="M74-40q40 0 40 26t-40 26" fill="none" stroke="{INK}" stroke-width="8"/>
  <path d="M-62-40h124l-14 84h-96z" class="bluep o"/>
</g>
<g class="blues" marker-end="url(#ar)"><path d="M240 130v46"/></g>
<path d="M360 200v70" class="blues" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('dry', '日ざしの下で洗濯物から水分が抜け、乾いていくイラスト。', f"""
{sun(500,96,46)}
<path d="M40 130h520" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g transform="translate(240 140)">
  <path d="M-70 0l-30 16 12 28 16-8v96h144V36l16 8 12-28-30-16h-38q-14 12-28 0z" class="tealp o"/>
</g>
<g class="blues" opacity=".85" marker-end="url(#ar)">
  <path d="M180 300v-40"/><path d="M260 320v-40"/><path d="M340 300v-40"/>
</g>
{drop(176,300,0.9)}{drop(256,320,0.9)}{drop(336,300,0.9)}
""", ground=True, arrow=True)

add('wet', '雨に降られたシャツから水がしたたり、表面がぬれているイラスト。', f"""
<g class="blues" opacity=".9"><path d="M120 40l-10 30M200 70l-10 30M300 40l-10 30M400 70l-10 30M480 40l-10 30"/></g>
<g transform="translate(290 220)">
  <path d="M-70 0l-30 16 12 28 16-8v96h144V36l16 8 12-28-30-16h-38q-14 12-28 0z" class="blue o"/>
  <path d="M-40 40q40 20 80 0" fill="none" stroke="#e1edfb" stroke-width="6" stroke-linecap="round"/>
</g>
{drop(230,346,1.1)}{drop(300,356,1.1)}{drop(370,346,1.1)}
<ellipse cx="300" cy="390" rx="120" ry="12" class="bluep"/>
""", ground=True)

add('thick', '厚みのある本と、その厚さを示す矢印のイラスト。', f"""
<circle cx="470" cy="110" r="58" class="goldp"/>
<g transform="translate(280 250)">
  <path d="M-120-90h150l60 30v150l-60 30h-150z" class="coralp o"/>
  <path d="M-120-90l60-30h150l-60 30z" class="coral o"/>
  <path d="M30-60v150" class="a"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="2.5"><path d="M-110-76h130M-110-56h130M-110-36h130"/></g>
</g>
<path d="M160 190v120" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('thin', '薄い一冊の本と、その薄さを示す短い矢印のイラスト。', f"""
<circle cx="470" cy="110" r="58" class="bluep"/>
<g transform="translate(280 280)">
  <path d="M-120-24h150l60 30v30l-60 30h-150z" class="bluep o"/>
  <path d="M-120-24l60-30h150l-60 30z" class="blue o"/>
  <path d="M30 6v30" class="a"/>
</g>
<path d="M160 256v50" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('flat', 'でこぼこのない平らな板の上に、水平な線が引かれているイラスト。', f"""
<circle cx="470" cy="110" r="58" class="tealp"/>
<path d="M80 250h440l-40 40H120z" class="tealp o"/>
<path d="M80 250h440" class="a"/>
<path d="M110 210h380" class="muted"/>
<circle cx="300" cy="226" r="16" class="gold o"/>
<path d="M120 320h360" class="a" opacity=".3"/>
""", ground=True)

add('curved', 'まっすぐな点線に対して、なめらかに湾曲した線を描いたイラスト。', f"""
<path d="M70 200h460" class="muted"/>
<path d="M70 260q230-180 460 0" fill="none" stroke="{TONES['violet'][0]}" stroke-width="16" stroke-linecap="round"/>
<circle cx="70" cy="260" r="14" class="violetd"/>
<circle cx="530" cy="260" r="14" class="violetd"/>
<g class="a" marker-end="url(#ar)"><path d="M300 200v-40"/></g>
""", ground=False, arrow=True)

add('mirror', '鏡の前に立つ人の姿が、鏡の中に左右反対に映っているイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-18-150h36v300h-36z" class="goldd"/>
</g>
<g transform="translate(430 200)">
  <path d="M-100-146h200v292h-200z" class="bluep o"/>
  <path d="M-84-130l60 40M-84-70l60 40" fill="none" stroke="#ffffff" stroke-width="5" opacity=".8"/>
</g>
{person(180,336,1.0,1,'coral','blue','wave' if 'wave' in POSES else 'point','short','smile')}
{person(440,336,1.0,-1,'coral','blue','point','short','smile')}
<path d="M270 130h60" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('gate', '塀の途中に取り付けられた門が開き、その先へ道が続いているイラスト。', f"""
<path d="M0 200h180v130H0zM420 200h180v130H420z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
<g fill="none" stroke="#c9bda6" stroke-width="4"><path d="M0 240h180M0 280h180M420 240h180M420 280h180"/></g>
<path d="M180 180h20v150h-20zM400 180h20v150h-20z" class="goldd"/>
<g transform="translate(240 250) rotate(-24 -40 0)">
  <path d="M-40-70h80v140h-80z" class="goldp o"/>
  <path d="M-40-30h80M-40 20h80M0-70v140" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
</g>
<path d="M300 330q0-60 40-90" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('rope', '太いロープが束ねられ、両端が結ばれているイラスト。', f"""
<circle cx="470" cy="110" r="58" class="goldp"/>
<path d="M80 220q60-70 130 0t130 0 130 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="24" stroke-linecap="round"/>
<path d="M80 220q60-70 130 0t130 0 130 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4" stroke-dasharray="14 14"/>
<path d="M110 300q80 60 190 0t190 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="24" stroke-linecap="round"/>
<path d="M110 300q80 60 190 0t190 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4" stroke-dasharray="14 14"/>
""", ground=True)

add('wheel', '車軸を中心に回る車輪と、回転の向きを示す矢印のイラスト。', f"""
<circle cx="300" cy="220" r="120" fill="none" stroke="{INK}" stroke-width="18"/>
<circle cx="300" cy="220" r="120" fill="none" stroke="{MUTED}" stroke-width="3"/>
<circle cx="300" cy="220" r="26" class="goldd"/>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="8">
  <path d="M300 196V112M300 244v84M276 220h-84M324 220h84M258 178l-58-58M342 262l58 58M342 178l58-58M258 262l-58 58"/>
</g>
<path d="M300 60a160 160 0 0 1 140 84" class="muted" marker-end="url(#ar)"/>
<path d="M120 360h360" class="a"/>
""", ground=True, arrow=True)

add('spring', 'ばねが押し縮められ、離すと元の長さへ跳ね返るイラスト。', f"""
<path d="M60 100h140v260H60z" fill="none" stroke="none"/>
<path d="M110 120h180" class="a"/>
<path d="M110 340h180" class="a"/>
<path d="M200 130q60-14 0-28-60-14 0-28" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10"/>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round">
  <path d="M130 140q140-24 0-48q-140-24 0-48"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round">
  <path d="M130 330q140-40 0-80q-140-40 0-80"/>
</g>
<path d="M380 160v60" class="a" marker-end="url(#ar)"/>
<path d="M440 300v-60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('filter', 'ろうとに入れた濁った水が、フィルターを通って澄んだ水になるイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-110-70h220L20 40h-40z" fill="#eef4f8" class="o"/>
  <path d="M-96-56h192L14 26h-28z" fill="#c9b79a" opacity=".55"/>
  <path d="M-110-70h220" class="a"/>
  <path d="M-70-10h140" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="8 8"/>
</g>
<path d="M300 190v54" class="blues" marker-end="url(#ar)" style="stroke-width:6"/>
<g transform="translate(300 320)">
  <path d="M-80-60h160l-12 116H-68z" fill="#f7fbfe" class="o"/>
  <path d="M-72 0h144l-8 56H-64z" class="bluep o"/>
  <path d="M-72 0h144" class="a"/>
</g>
""", ground=True, arrow=True)

add('seed', '一粒の種が土の中で芽を出し、上へ伸びはじめるイラスト。', f"""
<path d="M0 200h600v200H0z" fill="#e7d9c4"/>
<path d="M0 200h600" class="a"/>
{sun(500,96,44)}
<g transform="translate(300 280)">
  <ellipse rx="34" ry="44" class="goldd o"/>
  <path d="M-14-18q14 20 28 0" fill="none" stroke="{TONES['gold'][1]}" stroke-width="3"/>
  <path d="M0-44v-60" fill="none" stroke="{TONES['green'][2]}" stroke-width="7" stroke-linecap="round"/>
  <path d="M0-80c-32-8-42-30-42-30 30-8 42 30 42 30z" class="green o"/>
  <path d="M0-96c32-8 42-30 42-30-30-8-42 30-42 30z" class="green o"/>
  <g fill="none" stroke="#c9a97c" stroke-width="5" stroke-linecap="round"><path d="M0 44v34M0 60l-26 22M0 66l28 20"/></g>
</g>
""", ground=False)

add('root', '土の中に広がった根が、木の幹を支えているイラスト。', f"""
<path d="M0 230h600v170H0z" fill="#e7d9c4"/>
<path d="M0 230h600" class="a"/>
<path d="M292 230V120" fill="none" stroke="{TONES['gold'][2]}" stroke-width="20" stroke-linecap="round"/>
<circle cx="250" cy="100" r="44" class="greenp o"/><circle cx="330" cy="90" r="50" class="greenp o"/><circle cx="292" cy="52" r="40" class="greenp o"/>
<g fill="none" stroke="#c9a97c" stroke-width="9" stroke-linecap="round">
  <path d="M292 230v130"/><path d="M292 262l-90 74"/><path d="M292 276l96 66"/><path d="M292 320l-56 60"/><path d="M292 330l64 54"/>
</g>
<g fill="none" stroke="#c9a97c" stroke-width="5" stroke-linecap="round">
  <path d="M240 300l-40 20M340 306l40 18M270 350l-30 26M320 356l34 22"/>
</g>
""", ground=False)

add('branch', '木の幹から分かれて伸びた枝の先に、小さな店の看板が下がっているイラスト。', f"""
{sun(90,90,42)}
<path d="M300 400V180" fill="none" stroke="{TONES['gold'][2]}" stroke-width="26" stroke-linecap="round"/>
<path d="M300 240q80-20 150-80" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
<path d="M300 300q-80-16-140-70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
<circle cx="300" cy="140" r="54" class="greenp o"/>
<circle cx="180" cy="212" r="34" class="greenp o"/>
<g transform="translate(452 176)">
  <path d="M0-16v20" class="a"/>
  <path d="M-46 4h92v56h-92z" class="tealp o"/>
  <path d="M-30 24h60M-30 40h40" fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"/>
</g>
""", ground=True)

add('leaf', '一枚の葉が、葉脈まで見える形で描かれたイラスト。', f"""
<circle cx="470" cy="110" r="58" class="greenp"/>
<g transform="translate(280 220) rotate(-16)">
  <path d="M0-130C110-100 120 30 0 130-120 30-110-100 0-130z" class="green o"/>
  <path d="M0-130V130" fill="none" stroke="#e1f3e5" stroke-width="6"/>
  <g fill="none" stroke="#e1f3e5" stroke-width="4">
    <path d="M0-80q46 10 62 46M0-80q-46 10-62 46M0-20q52 10 68 50M0-20q-52 10-68 50M0 40q40 10 52 44M0 40q-40 10-52 44"/>
  </g>
</g>
<path d="M280 350v40" fill="none" stroke="{TONES['green'][2]}" stroke-width="8" stroke-linecap="round"/>
""", ground=True)

add('path', '庭の芝生の間を、飛び石が続いて奥へ延びていくイラスト。', f"""
<path d="M0 220h600v180H0z" fill="#e4efe2"/>
<path d="M0 220h600" class="a" opacity=".4"/>
{tree(90,230,0.8)}{tree(520,226,0.7)}
<g fill="#d8d3ca" stroke="{INK}" stroke-width="2.5">
  <ellipse cx="300" cy="380" rx="86" ry="24"/>
  <ellipse cx="300" cy="330" rx="66" ry="19"/>
  <ellipse cx="300" cy="292" rx="50" ry="15"/>
  <ellipse cx="300" cy="264" rx="36" ry="11"/>
  <ellipse cx="300" cy="242" rx="26" ry="8"/>
</g>
<path d="M420 300q-40-50-70-70" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(' '.join(W)); print(sheet(W))
