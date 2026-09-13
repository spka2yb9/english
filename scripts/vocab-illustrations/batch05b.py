"""第5回の描き直し分。batch05.py のあとに実行する（こちらが最終版）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('boil', 'なべの水がぶくぶくと泡立ち、湯気が上がって沸騰しているイラスト。', f"""
<g class="muted" opacity=".9"><path d="M236 120q-18-44 6-76M300 106q-18-50 8-84M366 122q-18-44 6-76"/></g>
<g transform="translate(300 250)">
  <path d="M-150-46h300l-20 106q-4 20-26 20h-208q-22 0-26-20z" fill="#dfe6ea" class="o"/>
  <path d="M-164-46h328" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-164-38q-40 0-40 22t40 22M164-38q40 0 40 22t-40 22" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-132-28h264l-16 84q-2 12-16 12h-200q-14 0-16-12z" class="bluep o"/>
  <g class="blue o"><circle cx="-84" cy="10" r="15"/><circle cx="-28" cy="26" r="11"/><circle cx="26" cy="6" r="17"/><circle cx="82" cy="24" r="12"/><circle cx="-52" cy="-10" r="9"/><circle cx="58" cy="-12" r="10"/></g>
</g>
{flame(258,368,1.25)}
{flame(342,368,1.05)}
""", ground=True)

add('pump', 'ポンプのハンドルを押し下げると、地下の水が管を通ってくみ上げられるイラスト。', f"""
<path d="M0 270h600v130H0z" fill="#e7d9c4"/>
<path d="M0 270h600" class="a"/>
<path d="M0 350h600v50H0z" class="bluep"/>
<path d="M0 350h600" class="blues"/>
<path d="M284 380V262h34v118z" fill="#cfd8de" stroke="{INK}" stroke-width="3"/>
<g transform="translate(300 200)">
  <path d="M-44 70h88V-30h-88z" fill="#dfe6ea" class="o"/>
  <path d="M-44-30h88l-16-28h-56z" class="tealp o"/>
  <path d="M34-4h96l-10 44H34z" fill="#dfe6ea" class="o"/>
  <path d="M-26-58v-34h-84" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="-114" cy="-92" r="12" class="ink"/>
</g>
<path d="M186 90v46" class="a" marker-end="url(#ar)"/>
<path d="M300 344V236" class="blues" marker-end="url(#ar)" style="stroke-width:6"/>
<path d="M420 240q34 16 44 50" fill="none" stroke="{TONES['blue'][0]}" stroke-width="12" stroke-linecap="round"/>
<path d="M420 240q34 16 44 50" fill="none" stroke="#9dc6ea" stroke-width="4" stroke-linecap="round"/>
""", ground=False, arrow=True)

add('tie', 'ひもの両端で輪をつくり、中央を結んでちょう結びにしているイラスト。', f"""
<circle cx="470" cy="100" r="54" class="violetp"/>
<g fill="none" stroke-linecap="round">
  <path d="M300 236C180 130 60 190 108 258c34 48 130 24 192-22" stroke="{TONES['coral'][0]}" stroke-width="18"/>
  <path d="M300 236c120-106 240-46 192 22-34 48-130 24-192-22" stroke="{TONES['teal'][0]}" stroke-width="18"/>
  <path d="M286 250q-70 70-96 130" stroke="{TONES['coral'][0]}" stroke-width="18"/>
  <path d="M314 250q70 70 96 130" stroke="{TONES['teal'][0]}" stroke-width="18"/>
  <path d="M262 216q40 44 78 0" stroke="{TONES['coral'][0]}" stroke-width="20"/>
  <path d="M266 250q34-34 68 0" stroke="{TONES['teal'][0]}" stroke-width="20"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M150 350q34-14 56-18"/><path d="M450 350q-34-14-56-18"/></g>
""", ground=False, arrow=True)

add('cross', '横断歩道の上を歩いて、道路の反対側へ渡っていく人のイラスト。', f"""
<path d="M0 170h600v160H0z" fill="#d8d3ca"/>
<path d="M0 156h600v14H0zM0 330h600v14H0z" class="ground"/>
<path d="M0 170h600M0 330h600" class="a"/>
<g fill="#fffdf6" stroke="{MUTED}" stroke-width="1.5">
  <rect x="180" y="176" width="34" height="148"/><rect x="232" y="176" width="34" height="148"/>
  <rect x="284" y="176" width="34" height="148"/><rect x="336" y="176" width="34" height="148"/>
  <rect x="388" y="176" width="34" height="148"/>
</g>
{person(300,320,0.92,1,'teal','blue','walk','short','smile')}
<path d="M360 130h120" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('block', '道の真ん中に転がった大きな岩が、通り道をふさいでいるイラスト。', f"""
<path d="M30 330h540" fill="none" stroke="#e6dcc9" stroke-width="76" stroke-linecap="round"/>
<g transform="translate(360 268)">
  <path d="M-104 62q-34-80 14-118 50-42 116-20 60 22 54 86 0 36-24 52z" fill="#b9b1a3" class="o"/>
  <path d="M-52-40q40-22 82 6" fill="none" stroke="#9a9284" stroke-width="3"/>
  <path d="M-30 20q50-16 90 8" fill="none" stroke="#9a9284" stroke-width="3"/>
</g>
<path d="M110 250h96" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:9"><path d="M212 218l56 56M268 218l-56 56"/></g>
""", ground=True, arrow=True)

add('press', '指がボタンを真上から押し下げて、ボタンが沈んでいるイラスト。', f"""
<circle cx="116" cy="104" r="52" class="coralp"/>
<g transform="translate(300 316)">
  <path d="M-116 20h232v46h-232z" fill="#dfe6ea" class="o"/>
  <ellipse cx="0" cy="14" rx="70" ry="26" class="coralp o"/>
  <ellipse cx="0" cy="24" rx="50" ry="17" class="coral o"/>
</g>
<g transform="translate(300 150)">
  <path d="M-24-30h48v128a24 24 0 0 1-48 0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-24-30q-60 0-60-26h108v26z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-84-56q-40 0-40 26h40" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-14 78q14 12 28 0" fill="none" stroke="{SKINL}" stroke-width="2"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M190 230v70"/><path d="M410 230v70"/></g>
""", ground=True, arrow=True)

add('mirror', '鏡の前に立つ人の姿が、鏡の中にそのまま映っているイラスト。', f"""
<g transform="translate(400 210)">
  <path d="M-108-160h216v320h-216z" class="goldd o"/>
  <path d="M-92-144h184v288h-184z" class="bluep o"/>
  <path d="M-80-128l52 36M-80-72l52 36" fill="none" stroke="#ffffff" stroke-width="5" opacity=".75"/>
</g>
<g opacity=".72">{person(414,330,0.92,-1,'coral','blue','point','short','smile')}</g>
{person(160,336,1.0,1,'coral','blue','point','short','smile')}
<path d="M246 200h60" class="muted" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('gate', '塀の途中の両開きの門が開き、その先へ道が続いているイラスト。', f"""
<path d="M300 400V210" fill="none" stroke="#e6dcc9" stroke-width="56" stroke-linecap="round"/>
<path d="M0 196h150v140H0zM450 196h150v140H450z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
<g fill="none" stroke="#c9bda6" stroke-width="4"><path d="M0 234h150M0 272h150M450 234h150M450 272h150"/></g>
<rect x="142" y="170" width="20" height="172" class="goldd o"/>
<rect x="438" y="170" width="20" height="172" class="goldd o"/>
<path d="M162 176v160l86-30V204z" class="goldp o"/>
<path d="M162 216l86-8M162 262l86-6" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
<path d="M438 176v160l-86-30V204z" class="goldp o"/>
<path d="M438 216l-86-8M438 262l-86-6" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
<path d="M300 380V232" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('spring', '押し縮められたばねが、手を離すと元の長さへ伸びて跳ね返るイラスト。', f"""
<g transform="translate(160 0)">
  <path d="M-74 196h148M-74 300h148" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-56 292q112-14 0-28-112-14 0-28-112-14 0-28-112-14 0-28" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round"/>
  <g class="a" marker-end="url(#ar)"><path d="M0 130v52"/></g>
</g>
<g transform="translate(430 0)">
  <path d="M-74 60h148M-74 340h148" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-56 330q112-46 0-92-112-46 0-92-112-46 0-92" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round"/>
  <g class="teals" marker-end="url(#ar)" style="stroke-width:6"><path d="M0 40V6"/></g>
</g>
<path d="M250 200h110" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(' '.join(W)); print(sheet(W))
