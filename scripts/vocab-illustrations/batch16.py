"""第16回: 針・積み重ね・写真・祈りなど30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('mixture', '白と赤の粒がまざり合って、一つの混合物になっているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(270 260)">
  <path d="M-120-70h240q-16 150-120 150T-120-70z" fill="#fffdf6" class="o"/>
  <path d="M-120-70h240" class="a"/>
  <g class="coral o"><circle cx="-60" cy="0" r="16"/><circle cx="10" cy="14" r="16"/><circle cx="66" cy="-6" r="16"/><circle cx="-20" cy="-32" r="16"/></g>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="-30" cy="10" r="16"/><circle cx="40" cy="16" r="16"/><circle cx="30" cy="-30" r="16"/><circle cx="-70" cy="-34" r="16"/></g>
</g>
<path d="M150 180a120 50 0 0 0 240 0" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('needle', '細く先のとがった針に、糸が通っているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="bluep"/>
<g transform="translate(300 220) rotate(-16)">
  <path d="M-200 0h360l40 0" fill="none" stroke="#dfe6ea" stroke-width="10" stroke-linecap="butt"/>
  <path d="M160-5l50 5-50 5z" fill="#cfd8de" stroke="{INK}" stroke-width="2"/>
  <path d="M-200 0h360" fill="none" stroke="{INK}" stroke-width="2"/>
  <ellipse cx="-180" cy="0" rx="14" ry="7" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M120 240q60 40 130 0t120 20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
""", ground=True)

add('notice', '壁に貼られた知らせに気づいて、目を向けるイラスト。', f"""
<g transform="translate(400 220)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-60h140M-70-30h140M-70 0h110M-70 30h120"/></g>
  <circle cy="-100" r="8" class="coral o"/>
</g>
{person(160,346,1.15,1,'teal','blue','point','short','surprised')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M220 220h70" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('offer', '飲み物を差し出して、相手にすすめているイラスト。', f"""
<circle cx="300" cy="130" r="70" class="tealp"/>
{person(160,346,1.15,1,'teal','blue','give','bob','smile')}
{person(450,346,1.15,-1,'coral','gold','stand','short','smile')}
<g transform="translate(300 250)">
  <path d="M-46-40h92l-10 74h-72z" fill="#fffdf6" class="o"/>
  <path d="M-46-40h92" class="a"/>
  <path d="M-40-16h80l-8 50h-64z" class="goldp o"/>
  <path d="M46-26q34 0 34 22t-34 22" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<path d="M360 200h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('operation', '手術台の上で、器具を使って処置を行っているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-200-30h400v26h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-160-4v70M160-4v70" fill="none" stroke="{MUTED}" stroke-width="10"/>
  <path d="M-130-56h260v26h-260z" class="bluep o"/>
</g>
{person(200,240,0.85,1,'teal','teal','point','cap','neutral')}
{person(400,240,0.85,-1,'teal','teal','point','cap','neutral')}
<g transform="translate(300 130)">
  <circle r="40" class="goldp o"/>
  <path d="M0 40v20" fill="none" stroke="{INK}" stroke-width="8"/>
  <g class="golds" style="stroke-width:4"><path d="M-60 20l-20 14M60 20l20 14"/></g>
</g>
""", ground=True)

add('organize', 'ばらばらの書類を、種類ごとにファイルへ分けて整えるイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(160 180)">
  <g transform="rotate(-12)"><path d="M-60-50h120v100h-120z" class="paper"/></g>
  <g transform="rotate(8) translate(10 20)"><path d="M-60-50h120v100h-120z" class="paper"/></g>
</g>
<g transform="translate(400 300)">
  <g class="tealp o"><rect x="-140" y="-60" width="80" height="110"/><rect x="-40" y="-60" width="80" height="110"/><rect x="60" y="-60" width="80" height="110"/></g>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-120-30h40M-20-30h40M80-30h40"/></g>
</g>
<path d="M250 220h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('overseas', '海をこえた向こう側の国と、荷物のやりとりをするイラスト。', f"""
<path d="M0 240h600v160H0z" class="bluep"/>
<path d="M0 240h150v160H0zM450 240h150v160H450z" class="ground"/>
<path d="M0 240h150M450 240h150" class="a"/>
{building(70,240,0.5,'teal')}
{building(530,240,0.5,'gold')}
<g transform="translate(300 260)">
  <path d="M-90 0h180l-20 34h-140z" class="teal o"/>
  <path d="M-90 0h180" class="a"/>
  <path d="M-40 0v-40h70v40z" class="paper"/>
</g>
<path d="M150 190q140-70 300-10" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('own', '自分の名札のついた品物を、自分の手元に持っているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
{person(200,346,1.15,1,'teal','blue','carry','short','smile')}
{box(200,266,120,80,0,'gold')}
<g transform="translate(320 200) rotate(-10)">
  <path d="M-40-22h80v44h-80z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-24-6h48M-24 8h30"/></g>
  <path d="M-40 0l-22-12v24z" class="paper"/>
</g>
<path d="M280 250l30-30" class="muted" marker-end="url(#ar)" transform="rotate(180 295 235)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pack', 'かばんに荷物を詰め込んで、旅の支度をしているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
<g transform="translate(300 300)">
  <path d="M-120-50h240v100h-240z" class="violetp o"/>
  <path d="M-60-50q0-40 60-40t60 40" fill="none" stroke="{INK}" stroke-width="8"/>
  <g class="tealp o"><rect x="-100" y="-30" width="70" height="50"/><rect x="-20" y="-30" width="60" height="50"/></g>
  <path d="M-120 0h240" fill="none" stroke="{TONES['violet'][2]}" stroke-width="5"/>
</g>
<g transform="translate(300 160)">
  <path d="M-40-30h80v50h-80z" class="coralp o"/>
</g>
<path d="M300 200v40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('pass', '試験の答案に合格の印がついているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
<g transform="translate(270 230)">
  <path d="M-130-140h260v280h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-90h200M-100-40h200M-100 10h160"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="12" stroke-linecap="round"><path d="M-40 70l30 30 60-70"/></g>
</g>
<path d="M440 200q-40 20-60 24" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('perform', '舞台の上で楽器を演奏し、観客に見せているイラスト。', f"""
<g transform="translate(300 340)">
  <path d="M-260-20h520v40h-520z" class="goldd o"/>
  <path d="M-260-20h520" class="a"/>
</g>
<g transform="translate(300 200)">
  <path d="M-280-140h560v40h-560z" class="coralp o"/>
  <path d="M-240-100v40M-160-100v30M240-100v40M160-100v30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{person(300,320,1.15,1,'violet','blue','up','bun','smile')}
<g fill="{INK}">
  <g transform="translate(420 230) scale(0.8)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g>
  <g transform="translate(180 240) scale(0.7)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g>
</g>
""", ground=False)

add('photograph', 'カメラを構えて、目の前の景色を写しているイラスト。', f"""
{tree(480,320,0.8)}
{person(200,346,1.15,1,'teal','blue','hold','short','neutral')}
<g transform="translate(250 236)">
  <path d="M-50-30h100v60h-100z" class="ink"/>
  <circle r="18" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-30-30h20v-10h-20z" class="ink"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M300 220l140-40M300 250l140 60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('photographer', 'カメラを持って撮影を仕事にしている人のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
{person(280,346,1.25,1,'violet','blue','hold','cap','smile')}
<g transform="translate(340 240) rotate(-6)">
  <path d="M-60-34h120v68h-120z" class="ink"/>
  <circle r="22" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <circle r="10" class="bluep o"/>
  <path d="M-36-34h26v-12h-26z" class="ink"/>
</g>
<path d="M280 288v40" fill="none" stroke="{MUTED}" stroke-width="6"/>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('pile', '同じ本を高く積み重ねた山のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(260 0)">
  {''.join(f'<g transform="translate({(i%2)*10-5} {330 - i*32})"><path d="M-90-14h180v28h-180z" class="{"tealp" if i%2 else "coralp"} o"/></g>' for i in range(7))}
</g>
<path d="M420 200v130" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('pointed', '先が鋭くとがった鉛筆の先端を、拡大して示したイラスト。', f"""
<circle cx="120" cy="100" r="56" class="goldp"/>
<g transform="translate(300 240) rotate(-14)">
  <path d="M-220-18h300v36h-300z" class="gold o"/>
  <path d="M80-18h60l60 18-60 18H80z" fill="#f0dfc2" stroke="{INK}" stroke-width="3"/>
  <path d="M140-6l60 6-60 6z" class="ink"/>
</g>
<circle cx="430" cy="180" r="60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
""", ground=True)

add('population', 'たくさんの人が並び、その総数を示しているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<g transform="translate({70+ (i%8)*70} {170 + (i//8)*80})"><circle cy="-26" r="16"/><path d="M-20 30q0-32 20-32t20 32z"/></g>' for i in range(24))}
</g>
<path d="M60 380h480" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('pot', '取っ手のついた深い容器を、横から見たイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(280 250)">
  <path d="M-110-50h220l-16 130h-188z" fill="#dfe6ea" class="o"/>
  <path d="M-124-50h248" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M-124-40q-44 0-44 24t44 24M124-40q44 0 44 24t-44 24" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('prayer', '手を組んで目を閉じ、静かに祈っている人のイラスト。', f"""
<circle cx="300" cy="140" r="86" class="goldp" opacity=".6"/>
{person(300,346,1.3,1,'violet','blue','hold','bob','neutral')}
<g transform="translate(300 250)">
  <path d="M-26-20h52q10 0 10 20t-10 20h-52q-10 0-10-20t10-20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M0-20v40" fill="none" stroke="{SKINL}" stroke-width="2"/>
</g>
<path d="M254 218h14M332 218h14" class="a"/>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('print', '印刷機から、文字の入った紙が出てくるイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-150-50h300v100h-300z" fill="#dfe6ea" class="o"/>
  <path d="M-100-50h200v-16h-200z" class="ink"/>
  <g class="green o"><circle cx="-120" cy="20" r="12"/></g>
</g>
<g transform="translate(300 170)">
  <path d="M-90-70h180v70h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-48h120M-60-28h100"/></g>
</g>
<path d="M300 120v-30" class="a" marker-end="url(#ar)" transform="rotate(180 300 105)"/>
""", ground=True, arrow=True)

add('productive', '同じ時間で、たくさんの成果物ができているイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-220-20h440v20h-440z" class="goldp o"/>
</g>
<g class="tealp o">
  {''.join(f'<rect x="{110+i*60}" y="220" width="46" height="80"/>' for i in range(6))}
</g>
<g transform="translate(300 130)">
  <circle r="46" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-30M0 0l22 14" class="a"/>
</g>
<path d="M420 130h100" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('program', 'テレビの画面に、番組が映っているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-180-130h360v240h-360z" fill="#dfe6ea" class="o"/>
  <path d="M-150-100h300v180h-300z" class="bluep o"/>
  <g transform="translate(0 -10) scale(0.6)">{person(0,60,1.0,1,'coral','gold','up','bob','smile')}</g>
  <path d="M-60 110h120v14h-120z" class="ink"/>
  <g class="coral o"><circle cx="160" cy="60" r="10"/></g>
</g>
<path d="M300 390v-40" class="a"/>
""", ground=True)

add('promise', '小指を結び、約束を交わしている二人のイラスト。', f"""
<circle cx="300" cy="130" r="70" class="violetp"/>
{person(190,346,1.15,1,'teal','blue','give','short','smile')}
{person(410,346,1.15,-1,'coral','gold','give','bob','smile')}
<g transform="translate(300 258)">
  <path d="M-30-14q30-14 60 0" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-30 14q30 14 60 0" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('pronounce', '口の形を見せて、音を声に出しているイラスト。', f"""
<g transform="translate(230 200)">
  <circle r="120" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-44" cy="-30" r="8" class="ink"/><circle cx="44" cy="-30" r="8" class="ink"/>
  <ellipse cy="46" rx="40" ry="30" fill="#b7574c" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="56" rx="24" ry="14" class="coralp"/>
</g>
<g class="teals" opacity=".9" style="stroke-width:5">
  <path d="M380 200q26 26 26 46t-26 46"/><path d="M430 180q34 34 34 66t-34 66"/>
</g>
""", ground=False)

add('prominent', '横に並んだ建物の中で、一つだけ高く目立っているイラスト。', f"""
{building(120,340,0.6,'gold')}
{building(230,340,0.6,'gold')}
<g transform="translate(360 0)">
  <path d="M-60 340V120h120v220z" class="teal o"/>
  <path d="M-76 120L0 50l76 70z" class="teald o"/>
  <g class="bluep o"><rect x="-26" y="160" width="52" height="44"/><rect x="-26" y="230" width="52" height="44"/></g>
</g>
{building(500,340,0.6,'gold')}
<path d="M180 200q80-60 120-80" class="muted" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('noble', '王冠をいただいた、位の高い人物のイラスト。', f"""
<circle cx="470" cy="100" r="56" class="violetp"/>
{person(280,346,1.3,1,'violet','violet','stand','short','neutral')}
<g transform="translate(280 192)">
  <path d="M-40 0l-6-40 20 16 12-26 12 26 20-16-6 40z" class="gold o"/>
  <path d="M-40 0h80v12h-80z" class="goldd o"/>
</g>
<g transform="translate(280 300)">
  <path d="M-56-40q56-20 112 0l24 100h-160z" class="violetd o"/>
</g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('notable', '並んだ点の中で、一つだけ大きく目を引くしるしのイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{90+ (i%7)*70} cy="220" r="18"/>'.replace('cx=','cx=') for i in [])}
</g>
<g class="tealp o">
  {''.join(f'<circle cx="{90+ i*70}" cy="220" r="18"/>' for i in range(7))}
</g>
<circle cx="300" cy="220" r="48" class="coral o"/>
<g class="golds" style="stroke-width:4"><path d="M300 150v-24M240 170l-18-18M360 170l18-18"/></g>
<path d="M300 300v40" class="a"/>
""", ground=False)

add('notorious', '悪い評判が、うわさとなって広く伝わっていくイラスト。', f"""
{person(140,346,1.05,1,'gold','blue','stand','cap','sad')}
<g class="corals" opacity=".9" style="stroke-width:5">
  <path d="M220 200q26 26 26 46t-26 46"/><path d="M266 180q34 34 34 66t-34 66"/>
</g>
<g opacity=".8">
  {person(400,346,0.9,-1,'violet','teal','stand','bob','neutral')}
  {person(490,346,0.9,-1,'blue','gold','stand','short','neutral')}
</g>
<g transform="translate(360 180)">
  <path d="M-60-34h120q14 0 14 14v34q0 14-14 14h-90l-20 18 4-18h-14q-14 0-14-14v-34q0-14 14-14z" class="paper"/>
  <path d="M-8-18h16v28h-16zM-8 16h16v10h-16z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('municipal', '市の建物と、その区域を示した地図のイラスト。', f"""
{building(200,300,1.1,'teal')}
<g transform="translate(200 210)">
  <path d="M-30-30h60v20h-60z" class="paper"/>
</g>
<g transform="translate(450 250)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <path d="M-60-40h120v80h-120z" class="tealp o"/>
  <path d="M-90-80h180v160h-180z" fill="none" class="a"/>
  <circle r="10" class="coral o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('naval', '海の上に並んだ軍艦のイラスト。', f"""
<path d="M0 260h600v140H0z" class="bluep"/>
<path d="M0 260q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(230 240)">
  <path d="M-150 0h300l-30 40h-240z" fill="#7a8794" stroke="{INK}" stroke-width="3"/>
  <path d="M-60 0v-40h100v40z" fill="#95a2af" stroke="{INK}" stroke-width="3"/>
  <path d="M-10-40v-40" class="a"/>
  <path d="M60-10h60v-16H60z" class="ink"/>
</g>
<g transform="translate(470 300) scale(0.6)">
  <path d="M-150 0h300l-30 40h-240z" fill="#7a8794" stroke="{INK}" stroke-width="3"/>
  <path d="M-60 0v-40h100v40z" fill="#95a2af" stroke="{INK}" stroke-width="3"/>
</g>
""", ground=False)

add('oral', '口の形を大きく示し、声で伝えていることを表したイラスト。', f"""
{face(240,200,120,'grin')}
<g transform="translate(430 200)">
  <path d="M-60-50h120q16 0 16 16v68q0 16-16 16h-90l-24 20 6-20h-12q-16 0-16-16v-68q0-16 16-16z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-24" cy="0" r="5"/><circle cx="0" cy="0" r="5"/><circle cx="24" cy="0" r="5"/></g>
</g>
<path d="M350 200h30" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('mind', '頭の中で考えが動いていることを、歯車で示したイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(400 190)">
  <circle r="100" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(-20 -10)">
    <circle r="46" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14"/>
    <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="9">{''.join(f'<path d="M0 -46v-14" transform="rotate({i*60})"/>' for i in range(6))}</g>
  </g>
  <g transform="translate(44 40)">
    <circle r="28" fill="none" stroke="{TONES['coral'][0]}" stroke-width="11"/>
    <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8">{''.join(f'<path d="M0 -28v-10" transform="rotate({i*72})"/>' for i in range(5))}</g>
  </g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="260" r="12"/><circle cx="264" cy="286" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(' '.join(W)); print(sheet(W))
