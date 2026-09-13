"""第38回: 浮く・流れる・折る・怖がるなど42語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('familiar', '見慣れた道を、迷わず歩いていくイラスト。', f"""
{building(140,300,0.6,'teal')}{tree(500,320,0.6)}
<path d="M120 340q120-40 240-20t200-40" fill="none" stroke="#e6dcc9" stroke-width="26" stroke-linecap="round"/>
{person(280,330,1.0,1,'teal','blue','walk','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M380 200l18 18 30-36"/></g>
""", ground=True)

add('far', '手前の点から遠くの点までを、長い矢印で示したイラスト。', f"""
<circle cx="90" cy="250" r="22" class="teal o"/>
<circle cx="520" cy="200" r="16" class="coral o"/>
<path d="M120 240h370" class="a" marker-end="url(#ar)" style="stroke-width:6"/>
{tree(220,340,0.5)}{tree(400,320,0.35)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('fascinating', '珍しい仕掛けに引き込まれて、目を離せないイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','bob','smile')}
<g transform="translate(410 230)">
  <circle r="90" class="violetp o"/>
  <g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4"><circle r="60"/><circle r="30"/></g>
  <circle r="12" class="violet o"/>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="5"><path d="M240 230h70" marker-end="url(#ar)"/></g>
<g class="golds" style="stroke-width:4"><path d="M500 140l24-24M340 140l-24-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('fashion', '流行の服を着た人が、通りを歩くイラスト。', f"""
{person(280,346,1.3,1,'violet','violet','walk','bun','smile')}
<g transform="translate(280 262)">
  <path d="M-46-30q46-16 92 0l-8 60h-76z" class="violetd o"/>
  <path d="M-40 0q40 14 80 0" fill="none" stroke="{TONES['violet'][1]}" stroke-width="3"/>
</g>
<g transform="translate(430 220)"><path d="M-40 0a40 30 0 0 1 80 0z" class="coral o"/><ellipse cy="2" rx="56" ry="12" class="coralp o"/></g>
<g class="golds" style="stroke-width:4"><path d="M170 200l-24-24"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('fashionable', '流行の形の服と、古い形の服を比べたイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-60-50h120v30l-16 110h-88l-16-110z" class="violetp o"/>
  <g class="golds" style="stroke-width:4"><path d="M60-70l24-24"/></g>
</g>
<g transform="translate(430 240)" opacity=".55">
  <path d="M-70-40h140v20l-14 110h-112l-14-110z" class="muted"/>
</g>
<path d="M300 130v220" class="muted"/>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('fasten', 'ベルトの金具をはめて、しっかり留めるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220-22h180v44h-220z" class="goldd o"/>
  <path d="M40-22h180v44H40z" class="goldd o"/>
  <g transform="translate(0 0)">
    <path d="M-44-30h40v60h-40z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
    <path d="M4-30h40v60H4z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  </g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 330h60"/><path d="M420 330h-60"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 150l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('fat', '肉の白い脂肪の部分を示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-80h280v160h-280z" class="coralp o"/>
  <path d="M-140-40h280v40h-280z" fill="#fff8e6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-140 40h280v20h-280z" fill="#fff8e6" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M470 160q-40 30-60 46" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('fiction', '想像で書かれた物語の本のイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-100-120h200v240h-200z" class="violetp o"/>
  <path d="M-80-120h20v240h-20z" class="violet o"/>
  <g transform="translate(20 -30) scale(0.5)">
    <path d="M-60 40L-10-40l40 46 40-56 30 90z" class="tealp o"/>
    <circle cx="40" cy="-50" r="20" class="goldp o"/>
  </g>
</g>
<g transform="translate(450 200)">
  <path d="M-70-40q-10-34 30-40 12-28 56-20 26 4 32 28 42-4 44 32 2 30-36 32h-100q-24-2-26-32z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('field', '専門の分野を、区画で分けて示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M0-140v280M-200 0h400" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <g class="tealp o"><rect x="-180" y="-120" width="160" height="100"/></g>
  <g class="coralp o"><rect x="20" y="-120" width="160" height="100"/></g>
  <g class="goldp o"><rect x="-180" y="20" width="160" height="100"/></g>
  <g class="violetp o"><rect x="20" y="20" width="160" height="100"/></g>
</g>
""", ground=True)

add('final', '一連の段のうち、最後の段に印があるイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{110+i*90}" cy="230" r="38"/>' for i in range(5))}
</g>
<circle cx="470" cy="230" r="38" class="coral o"/>
<g class="a" marker-end="url(#ar)">{''.join(f'<path d="M{152+i*90} 230h34"/>' for i in range(4))}</g>
<path d="M470 320v30" class="a"/>
""", ground=False, arrow=True)

add('financial', 'グラフと硬貨で、お金の動きを示したイラスト。', f"""
<g transform="translate(240 250)">
  <path d="M-120-100h240v200h-240z" class="paper"/>
  <path d="M-90 60h180M-90 60V-60" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-80 30l60-40 60 20 60-50" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
</g>
<g class="goldp o"><circle cx="450" cy="290" r="30"/><circle cx="500" cy="300" r="30"/><circle cx="475" cy="240" r="30"/></g>
""", ground=True)

add('fine', '違反の紙が渡され、罰金を払わされるイラスト。', f"""
{person(430,346,1.15,-1,'blue','violet','give','cap','neutral')}
{person(170,346,1.1,1,'coral','blue','give','short','sad')}
<g transform="translate(300 230)">
  <path d="M-56-40h112v80h-112z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-34-14h68M-34 8h44"/></g>
</g>
<g transform="translate(300 320)">
  <circle r="22" class="goldp o"/>
  <path d="M-7-10h14v20h-14z" class="goldd"/>
</g>
<path d="M240 320h-40" class="a" marker-end="url(#ar)" transform="rotate(180 220 320)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('finger', '手の一本の指を示したイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-70 90q-30-90 0-130 10-50 30-50t18 44v26q6-38 24-38t18 44v14q8-30 24-28t12 34q8-20 20-14t8 30q0 54-34 64z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<circle cx="245" cy="130" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M400 140q-60 0-110 0" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('finish', '最後の一筆を入れて、作品を仕上げるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-110h280v220h-280z" class="paper"/>
  <path d="M-100 60l60-90 50 56 50-66 30 100z" class="tealp o"/>
  <circle cx="60" cy="-50" r="24" class="goldp o"/>
</g>
<g transform="translate(440 150) rotate(40)">
  <path d="M-60-8h100v16H-60z" class="goldd o"/>
  <path d="M40-12h26v24H40z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 360l18 18 30-36"/></g>
""", ground=True)

add('first', '列の先頭に、一番の印がついているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{130+i*90}" cy="230" r="38"/>' for i in range(5))}
</g>
<circle cx="130" cy="230" r="38" class="coral o"/>
<g fill="{INK}"><rect x="126" y="310" width="10" height="30"/></g>
<g class="a" marker-end="url(#ar)">{''.join(f'<path d="M{172+i*90} 230h34"/>' for i in range(4))}</g>
""", ground=False, arrow=True)

add('fixed', 'ねじで固定されて、動かなくなっているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-40h280v80h-280z" class="tealp o"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><circle cx="-100" r="14"/><circle cx="100" r="14"/><path d="M-108-8l16 16M-108 8l16-16M92-8l16 16M92 8l16-16"/></g>
</g>
<g class="corals" style="stroke-width:6"><path d="M300 150v-30M300 350v30"/></g>
<g class="corals" style="stroke-width:8"><path d="M440 130l30 30M470 130l-30 30"/></g>
""", ground=True)

add('flash', '一瞬だけ強い光がひらめくイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a4a"/>
<g transform="translate(300 210)">
  <circle r="60" fill="#fff8e6"/>
  <g fill="none" stroke="#f7e6a8" stroke-width="7" stroke-linecap="round">
    {''.join(f'<path d="M0 -80v-40" transform="rotate({i*45})"/>' for i in range(8))}
  </g>
</g>
""", ground=False)

add('flee', '危険な場所から、走って逃げていくイラスト。', f"""
{flame(480,320,1.2)}
{person(200,346,1.15,1,'coral','blue','walk','short','surprised')}
<g class="muted"><path d="M280 280h50M270 320h60"/></g>
<path d="M140 240h-70" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('float', '水面に葉が浮かんで、沈まずに漂うイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(300 240) rotate(-10)">
  <path d="M-70 0C-30-40 30-40 70 0-30 40-30 40-70 0z" class="green o"/>
</g>
<path d="M420 200v40" class="a" marker-end="url(#ar)" transform="rotate(180 420 220)"/>
<g class="blues" opacity=".7"><path d="M80 300q50-14 100 0t100 0"/></g>
""", ground=False, arrow=True)

add('flourish', '植物が勢いよく茂って、栄えているイラスト。', f"""
{sun(480,90,44)}
<path d="M0 300h600v100H0z" fill="#e7d9c4"/>
<path d="M0 300h600" class="a"/>
<g transform="translate(270 300)">
  <path d="M0 0v-160" fill="none" stroke="{TONES['green'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M0-50c-50-12-66-42-66-42 46-12 66 42 66 42z" class="green o"/>
  <path d="M0-90c50-12 66-42 66-42-46-12-66 42-66 42z" class="green o"/>
  <path d="M0-130c-40-16-40-56-40-56 40 8 40 56 40 56z" class="green o"/>
  <g class="coral o"><circle cx="-40" cy="-120" r="12"/><circle cx="46" cy="-140" r="12"/></g>
</g>
<path d="M120 170h60" class="a" marker-end="url(#ar)" transform="rotate(-90 150 200)"/>
""", ground=False, arrow=True)

add('flow', '水が管を通って、一定の向きに流れるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-240-40h480v80h-480z" fill="#e3e9ee" stroke="{INK}" stroke-width="3"/>
  <path d="M-240-14h480" fill="none" stroke="#ffffff" stroke-width="8"/>
</g>
<g class="blues" marker-end="url(#ar)" style="stroke-width:8">
  <path d="M100 230h140"/><path d="M280 230h140"/>
</g>
<path d="M120 330h360" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('flu', '熱を出して寝込み、鼻をかんでいるイラスト。', f"""
<g transform="translate(260 300)">
  <path d="M-160-20h320v50h-320z" class="tealp o"/>
  <path d="M-170 30h340v20h-340z" class="goldd o"/>
  <ellipse cx="-100" cy="-40" rx="50" ry="26" fill="#fffdf6" class="o"/>
  <g transform="translate(-100 -60)">
    <circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-26-4q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
    <path d="M-10 2h6M6 2h6" class="a"/>
    <circle cx="0" cy="14" r="7" class="coralp"/>
  </g>
</g>
{thermometer(470,280,0.9,1.0)}
<g class="corals" style="stroke-width:4"><path d="M180 190q20-24 16-44"/></g>
<path d="M60 370h480" class="a"/>
""", ground=True)

add('flying', '飛行機が空を飛んでいるイラスト。', f"""
{cloud(120,110,1.2)}{cloud(470,260,1.0)}
{plane(310,200,1.1,-6,'teal')}
<path d="M120 270q90-40 150-56" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('focus', '光が一点に集まって、焦点を結ぶイラスト。', f"""
<g class="golds" style="stroke-width:5">
  <path d="M60 140h180M60 200h180M60 260h180M60 320h180"/>
</g>
<g transform="translate(300 230)">
  <path d="M-40-120q60 120 0 240-60-120 0-240z" class="bluep o"/>
</g>
<g class="golds" style="stroke-width:5" marker-end="url(#ar)">
  <path d="M330 160l120 60"/><path d="M330 200l120 25"/><path d="M330 260l120-25"/><path d="M330 300l120-60"/>
</g>
<circle cx="470" cy="230" r="14" class="coral o"/>
""", ground=False, arrow=True)

add('fold', '紙を半分に折りたたむイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-90-100h180v200h-180z" class="paper"/>
  <path d="M0-100v200" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g transform="translate(430 240)">
  <path d="M-50-100h100v200h-100z" class="paper"/>
  <path d="M-50-100h100v200h-100z" fill="none" class="a"/>
  <path d="M-50-100l-30 12v176l30 12z" class="goldp o"/>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('folk', '素朴な民族衣装を着た人たちが並ぶイラスト。', f"""
{person(160,346,1.05,1,'gold','coral','stand','bob','smile')}
{person(300,346,1.05,1,'coral','gold','stand','short','smile')}
{person(440,346,1.05,1,'violet','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><path d="M136 280h48M276 280h48M416 280h48"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('following', 'ある一つの次に来るものを、印で示したイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{110+i*90}" y="200" width="70" height="90"/>' for i in range(5))}
</g>
<rect x="290" y="200" width="70" height="90" class="coral o"/>
<path d="M220 340h120" class="a" marker-end="url(#ar)"/>
<path d="M60 300h480" class="a" opacity=".3"/>
""", ground=False, arrow=True)

add('forbid', '進入を禁じる印が、道をふさいでいるイラスト。', f"""
<path d="M60 320h480" fill="none" stroke="#e6dcc9" stroke-width="50" stroke-linecap="round"/>
<g transform="translate(330 230)">
  <circle r="70" fill="#fffdf6" stroke="{TONES['coral'][0]}" stroke-width="14"/>
  <path d="M-46 0h92" fill="none" stroke="{TONES['coral'][0]}" stroke-width="14"/>
  <path d="M0 70v70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9"/>
</g>
{person(130,320,0.85,1,'teal','blue','stand','short','neutral')}
<path d="M200 260h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('forest', '木が密に立ち並んだ森のイラスト。', f"""
{tree(100,340,0.9)}{tree(200,350,1.1)}{tree(300,340,0.85)}{tree(400,352,1.15)}{tree(500,340,0.95)}
<g opacity=".55">{tree(150,300,0.6)}{tree(350,300,0.6)}{tree(460,296,0.55)}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('forge', '熱した鉄を打って、形を作るイラスト。', f"""
{flame(150,330,1.0)}
<g transform="translate(320 300)">
  <path d="M-110-20h220v20h-220z" class="ink"/>
  <path d="M-60-40h120v20h-120z" class="coral o"/>
</g>
<g transform="translate(320 190) rotate(-24)">
  <path d="M-44-24h88v34h-88z" class="goldd o"/>
  <path d="M0 10v70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M240 250l-24-16M400 250l24-16"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('forgive', '謝る相手を受け入れて、握手するイラスト。', f"""
<circle cx="300" cy="140" r="76" class="greenp"/>
{person(190,346,1.15,1,'coral','blue','give','short','sad')}
{person(410,346,1.15,-1,'teal','gold','give','bob','smile')}
<g transform="translate(300 256)">
  <path d="M-40-16h80q14 0 14 16t-14 16h-80q-14 0-14-16t14-16z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M270 170l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('forest' if False else 'fork', '四本の先が分かれたフォークのイラスト。', f"""
<g transform="translate(300 230) rotate(6)">
  <path d="M-40-140v70q0 24 14 30v190h52V-40q14-6 14-30v-70h-12v58h-10v-58h-10v58h-10v-58h-10v58h-10v-58z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('formulate', '断片の考えを組み立てて、一つの案にまとめるイラスト。', f"""
<g transform="translate(160 220)">
  <g class="tealp o"><rect x="-60" y="-50" width="46" height="34" transform="rotate(-12 -37 -33)"/><rect x="0" y="-30" width="46" height="34" transform="rotate(10 23 -13)"/><rect x="-40" y="20" width="46" height="34" transform="rotate(6 -17 37)"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-60-40h120M-60-10h120M-60 20h90"/></g>
</g>
<path d="M270 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('foster', '苗に水をやって、育てているイラスト。', f"""
{hand(160,190,1)}
<g transform="translate(280 210) rotate(28)">
  <path d="M-40-30h80l-8 60h-64z" class="tealp o"/>
  <path d="M40-24h40l20-14-60-6z" class="teal o"/>
</g>
<g stroke-linecap="round" fill="none"><path d="M340 236q20 30 22 60" stroke="{TONES['blue'][0]}" stroke-width="8"/></g>
<g transform="translate(380 330)">
  <path d="M-50-30h100l-14 60h-72z" class="coralp o"/>
  <path d="M0-30v-50" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
  <path d="M0-56c-30-8-40-26-40-26 26-8 40 26 40 26z" class="green o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('free', '鎖が外れて、自由になっているイラスト。', f"""
{person(300,346,1.25,1,'teal','blue','up','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="10">
  <ellipse cx="150" cy="300" rx="30" ry="18"/><ellipse cx="200" cy="310" rx="30" ry="18" transform="rotate(30 200 310)"/>
  <ellipse cx="450" cy="300" rx="30" ry="18"/><ellipse cx="400" cy="312" rx="30" ry="18" transform="rotate(-30 400 312)"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 220h-60"/><path d="M370 220h60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('fridge', '扉を開けると中が冷えている冷蔵庫のイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-100-150h200v300h-200z" fill="#dfe6ea" class="o"/>
  <path d="M-100-30h200" class="a"/>
  <path d="M76-110v60h-10v-60z" class="ink"/>
  <path d="M76 10v60h-10V10z" class="ink"/>
</g>
<g transform="translate(450 230)">
  <path d="M-60-150h120v300h-120z" fill="#eef4f8" class="o"/>
  <g class="tealp o"><rect x="-40" y="-120" width="80" height="40"/><rect x="-40" y="-60" width="80" height="40"/></g>
  <g class="blues" style="stroke-width:4"><path d="M-20 20l40 30M20 20l-40 30"/></g>
</g>
<path d="M120 390h380" class="a"/>
""", ground=True)

add('frighten', '大きな音で相手を驚かせて、怖がらせるイラスト。', f"""
{person(180,346,1.15,1,'violet','blue','up','cap','neutral')}
{person(430,346,1.15,-1,'coral','gold','up','bob','sad')}
<g class="corals" opacity=".9" style="stroke-width:6"><path d="M270 200q30 30 30 50t-30 50"/><path d="M310 180q38 38 38 70t-38 70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('frightened', '身をすくめて、おびえている人のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#3a4a5c"/>
{person(240,350,1.2,1,'coral','blue','up','short','sad')}
<g fill="#22303e" stroke="#556777" stroke-width="3"><path d="M430 350q-30-90 40-124 56-26 92 16 38 48-24 108z"/></g>
<g fill="#f7e6a8"><circle cx="470" cy="250" r="9"/><circle cx="516" cy="250" r="9"/></g>
""", ground=False)

add('frightening', '暗い森の影が、恐ろしく見えるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#22303e"/>
<g fill="#16202b" stroke="#3a4a5c" stroke-width="3">
  <path d="M60 400V200h40v200zM120 400V160h40v200zM440 400V180h40v200zM500 400V220h40v200z"/>
</g>
<g fill="#f7e6a8"><circle cx="300" cy="200" r="8"/><circle cx="340" cy="200" r="8"/></g>
<g fill="none" stroke="#3a4a5c" stroke-width="4"><path d="M240 260q60 30 160 0"/></g>
""", ground=False)

add('frog', '水辺にいるカエルのイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep o"/>
<path d="M0 300q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(300 270)">
  <ellipse cy="0" rx="90" ry="56" class="green o"/>
  <circle cx="-40" cy="-44" r="22" class="green o"/><circle cx="40" cy="-44" r="22" class="green o"/>
  <circle cx="-40" cy="-46" r="9" fill="#fffdf6" stroke="{INK}" stroke-width="2"/><circle cx="40" cy="-46" r="9" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
  <circle cx="-40" cy="-46" r="4" class="ink"/><circle cx="40" cy="-46" r="4" class="ink"/>
  <path d="M-30 16q30 20 60 0" fill="none" stroke="{TONES['green'][2]}" stroke-width="3"/>
  <path d="M-86 30q-30 20-24 40 20 6 34-20M86 30q30 20 24 40-20 6-34-20" fill="{TONES['green'][0]}" stroke="{INK}" stroke-width="2.5"/>
</g>
""", ground=False)
print(len(W), ' '.join(W)); print(sheet(W))
