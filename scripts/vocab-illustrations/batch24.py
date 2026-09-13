"""第24回: 増える・含む・伝える・けるなど30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('ignore', '呼びかけられても背を向けて、聞き流しているイラスト。', f"""
{person(180,346,1.1,1,'coral','blue','point','short','neutral')}
<g transform="translate(300 200)">
  <path d="M-54-30h108q14 0 14 14v30q0 14-14 14h-70l-20 18 6-18h-24q-14 0-14-14v-30q0-14 14-14z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-20" cy="0" r="4"/><circle cx="0" cy="0" r="4"/><circle cx="20" cy="0" r="4"/></g>
</g>
<g transform="translate(440 346)">
  <path d="M-12-8l-7 35M12-8l7 35" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-30-94q30-16 60 0l-10 86h-40z" class="teal o"/>
  <circle cx="0" cy="-130" r="29" fill="{HAIR}"/>
</g>
<g class="corals" style="stroke-width:7"><path d="M370 220l30 30M400 220l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('ill', 'ベッドで寝込み、体温計をくわえている人のイラスト。', f"""
<g transform="translate(260 300)">
  <path d="M-160-20h320v50h-320z" class="tealp o"/>
  <path d="M-170 30h340v20h-340z" class="goldd o"/>
  <ellipse cx="-100" cy="-40" rx="50" ry="26" fill="#fffdf6" class="o"/>
  <g transform="translate(-100 -60)">
    <circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-26-4q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
    <path d="M-10 2h6M6 2h6" class="a"/>
    <path d="M-8 14h16" class="a"/>
    <path d="M10 10h30" fill="none" stroke="{INK}" stroke-width="4"/>
  </g>
</g>
{thermometer(470,280,0.9,0.7)}
<g class="corals" style="stroke-width:4"><path d="M180 190q20-24 16-44"/></g>
<path d="M60 370h480" class="a"/>
""", ground=True)

add('implementation', '計画書のとおりに、実際の設備が組み上がるイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3" stroke-dasharray="8 7"><path d="M-60-70h120v100h-120z"/><path d="M-60-20h120M0-70v100"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-90-90h180v180h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-60-60h120v60h-120z" class="bluep o"/>
  <g class="green o"><circle cx="-60" cy="50" r="12"/></g>
</g>
<path d="M280 220h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('improve', '低い山から高い山へ、線が上向きに伸びていくイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o">
  <rect x="100" y="280" width="60" height="60"/><rect x="190" y="240" width="60" height="100"/>
  <rect x="280" y="200" width="60" height="140"/><rect x="370" y="150" width="60" height="190"/>
</g>
<path d="M110 270L440 130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('include', '袋の中に品物が入っていることを、点線の囲みで示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-100h280v200h-280z" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="14 10"/>
  <g class="tealp o"><circle cx="-70" cy="-30" r="34"/><circle cx="0" cy="30" r="34"/><circle cx="70" cy="-30" r="34"/></g>
  <circle cx="0" cy="-40" r="30" class="coral o"/>
</g>
<path d="M470 130q-30 30-50 46" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('included', '料金の中に、追加分も入っていることを示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-70h200M-100-30h200M-100 10h200"/></g>
  <path d="M-110 40h220v50h-220z" class="goldp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-90-74l10 10 16-18M-90-34l10 10 16-18M-90 6l10 10 16-18"/>
  </g>
</g>
""", ground=True)

add('increase', '同じ器の中身が、だんだん増えていくイラスト。', f"""
<g transform="translate(140 280)">
  <path d="M-50-90h100l-8 150h-84z" fill="#f7fbfe" class="o"/>
  <path d="M-42 30h84l-4 30h-76z" class="bluep o"/>
</g>
<g transform="translate(300 280)">
  <path d="M-50-90h100l-8 150h-84z" fill="#f7fbfe" class="o"/>
  <path d="M-46-20h92l-6 80h-80z" class="bluep o"/>
</g>
<g transform="translate(460 280)">
  <path d="M-50-90h100l-8 150h-84z" fill="#f7fbfe" class="o"/>
  <path d="M-49-70h98l-7 130h-84z" class="bluep o"/>
</g>
<path d="M100 150h400" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('inform', '知らせの紙をわたして、相手に伝えているイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','give','short','neutral')}
{person(440,346,1.1,-1,'coral','gold','hold','bob','smile')}
<g transform="translate(300 250)">
  <path d="M-60-70h120v140h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-40h72M-36-16h72M-36 8h50"/></g>
  <circle cx="34" cy="40" r="12" class="coral o"/>
</g>
<path d="M250 190h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('informal', 'くだけた普段着と、きちんとした正装を比べたイラスト。', f"""
{person(180,346,1.2,1,'coral','gold','stand','bun','smile')}
{person(430,346,1.2,1,'blue','blue','stand','short','neutral')}
<g transform="translate(430 268)">
  <path d="M-40-24h80v6h-80z" class="paper"/>
  <path d="M-12-20l12 18 12-18z" class="ink"/>
</g>
<path d="M300 130v220" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('injure', 'ひざにけがをして、包帯を巻いているイラスト。', f"""
{person(280,346,1.25,1,'teal','blue','stand','short','sad')}
<g transform="translate(268 310)">
  <path d="M-22-14h44v28h-44z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
  <path d="M-22-6h44M-22 4h44" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M340 300l26-16M330 340l30 10"/></g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('insist', '同じ主張を強く繰り返して、譲らないイラスト。', f"""
{person(200,346,1.2,1,'coral','blue','point','short','neutral')}
<g transform="translate(400 190)">
  <path d="M-80-46h160q16 0 16 16v50q0 16-16 16h-110l-26 22 6-22h-30q-16 0-16-16v-50q0-16 16-16z" class="paper"/>
  <path d="M-8-24h16v34h-16zM-8 18h16v14h-16z" class="coral o"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M300 260h60M300 290h50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('intend', 'これからする予定を、矢印で示して定めているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','point','short','neutral')}
<g transform="translate(430 230)">
  <circle r="80" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle r="52" class="tealp o"/><circle r="18" class="teal o"/>
</g>
<path d="M250 250h100" class="a" marker-end="url(#ar)" style="stroke-width:6"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('intent', '狙う先を、まっすぐ見つめて定めているイラスト。', f"""
{person(170,346,1.15,1,'violet','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4"><path d="M230 216h180" marker-end="url(#ar)"/><path d="M230 228h180" marker-end="url(#ar)"/></g>
<g transform="translate(460 220)">
  <circle r="60" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle r="16" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('interrupt', '話している途中に割り込んで、話をさえぎるイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','stand','short','neutral')}
{person(460,346,1.1,-1,'coral','gold','point','bob','neutral')}
<g transform="translate(270 200)">
  <path d="M-60-34h120q14 0 14 14v34q0 14-14 14h-80l-20 18 6-18h-26q-14 0-14-14v-34q0-14 14-14z" class="paper"/>
</g>
<path d="M370 230h-60" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:8"><path d="M340 170l40 40M380 170l-40 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('introduce', '二人を引き合わせて、互いに紹介しているイラスト。', f"""
{person(300,346,1.15,1,'teal','blue','give','bob','smile')}
{person(140,346,1.05,1,'coral','gold','stand','short','smile')}
{person(470,346,1.05,-1,'violet','teal','stand','cap','smile')}
<g class="a" marker-end="url(#ar)"><path d="M240 230h-60"/><path d="M370 230h60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('involve', 'ある作業の輪の中に、人が引き込まれて加わるイラスト。', f"""
<circle cx="330" cy="220" r="130" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
{person(330,300,0.9,1,'teal','blue','stand','short','smile')}
{person(120,346,0.9,1,'coral','gold','walk','bob','neutral')}
<path d="M180 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('iron', '鉄のかたまりと、そこから作った棒を並べたイラスト。', f"""
<g transform="translate(200 270)">
  <path d="M-70 40q-24-60 12-90 36-30 84-10 40 20 34 66-2 24-18 34z" fill="#8f9aa5" stroke="{INK}" stroke-width="3"/>
  <path d="M-30-30q30-16 60 6" fill="none" stroke="#77828d" stroke-width="3"/>
</g>
<g transform="translate(430 280)">
  <path d="M-80-20h160v40h-160z" fill="#8f9aa5" stroke="{INK}" stroke-width="3"/>
  <path d="M-80-20h160" fill="none" stroke="#c9d4dd" stroke-width="6"/>
</g>
<path d="M300 260h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('jet', '高速で飛ぶジェット機のイラスト。', f"""
{cloud(120,110,1.1)}
{plane(320,200,1.15,-4,'blue')}
<g class="muted"><path d="M120 210h100M110 240h120"/></g>
<path d="M480 260h60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('key', '鍵穴に差し込んで回す鍵のイラスト。', f"""
<g transform="translate(220 240)">
  <circle r="46" fill="none" stroke="{TONES['gold'][0]}" stroke-width="16"/>
  <path d="M46-12h160v24h-30v26h-20v-26h-30v26h-20v-26H46z" class="goldd o"/>
</g>
<g transform="translate(470 240)">
  <path d="M-60-90h120v180h-120z" class="goldp o"/>
  <circle cy="-20" r="14" class="ink"/>
  <path d="M-8-20h16v40h-16z" class="ink"/>
</g>
<path d="M330 300h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('kick', '足でボールをけって、勢いよく飛ばすイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','walk','short','neutral')}
<g transform="translate(300 320)">
  <circle r="30" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><path d="M0-30l14 10-6 16h-16l-6-16z"/></g>
</g>
<path d="M340 290q90-60 190-30" class="muted" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:4"><path d="M250 300l-20-14M256 340l-24 8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('kiss', '二人が顔を寄せて、ほおに口づけしているイラスト。', f"""
<circle cx="300" cy="140" r="76" class="coralp"/>
<g transform="translate(300 176)"><path d="M0 24l-28-34 14-16 14 14 14-14 14 16z" class="coral o"/></g>
{person(210,346,1.15,1,'violet','blue','stand','bob','smile')}
{person(390,346,1.15,-1,'teal','gold','stand','short','smile')}
<path d="M270 240h60" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('labor', '複数の人が力を出して、重い作業をしているイラスト。', f"""
{person(180,346,1.1,1,'gold','blue','carry','cap','neutral')}
{box(180,266,90,64,0,'gold')}
{person(360,346,1.1,1,'gold','blue','carry','short','neutral')}
{box(360,266,90,64,0,'gold')}
<g class="corals" style="stroke-width:4"><path d="M250 200l-20-20M430 200l20-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('landlord', '部屋の鍵を貸し出す、建物の持ち主のイラスト。', f"""
{building(180,300,0.95,'teal')}
{person(430,346,1.15,-1,'gold','violet','give','short','neutral')}
<g transform="translate(320 250)">
  <circle cx="-30" r="16" fill="none" stroke="{TONES['gold'][0]}" stroke-width="7"/>
  <path d="M-14 0h60v10h-14v10h-10v-10h-36z" class="goldd o"/>
</g>
<path d="M270 200h-50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('landmark', '遠くからでも分かる目印の塔を示したイラスト。', f"""
{building(120,340,0.5,'gold')}
{building(220,340,0.5,'gold')}
<g transform="translate(360 0)">
  <path d="M-50 340V120h100v220z" class="teal o"/>
  <path d="M-64 120L0 40l64 80z" class="teald o"/>
  <g class="bluep o"><rect x="-22" y="160" width="44" height="40"/></g>
</g>
{building(500,340,0.5,'gold')}
<circle cx="360" cy="120" r="70" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"/>
<path d="M180 200q80-40 110-56" class="muted" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('lane', '白線で区切られた一本の車線を示したイラスト。', f"""
<path d="M0 170h600v230H0z" fill="#d8d3ca"/>
<path d="M0 170h600" class="a"/>
<g fill="none" stroke="#fffdf6" stroke-width="6" stroke-dasharray="40 30"><path d="M0 250h600M0 320h600"/></g>
<g transform="translate(300 285) scale(0.45)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<path d="M120 250v70" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('later', '時計の針が進んで、あとの時刻になるイラスト。', f"""
<g transform="translate(180 220)">
  <circle r="80" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-50M0 0l30 20" class="a"/>
</g>
<g transform="translate(430 220)">
  <circle r="80" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-50M0 0l-20 34" class="a"/>
</g>
<path d="M290 220h50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('lay', '線路を地面に敷き並べているイラスト。', f"""
<path d="M0 300h600v100H0z" fill="#d8d3ca"/>
<path d="M0 300h600" class="a"/>
<g fill="none" stroke="{INK}" stroke-width="5"><path d="M60 330h480M60 360h480"/></g>
<g fill="{TONES['gold'][2]}">{''.join(f'<rect x="{80+i*70}" y="326" width="16" height="40"/>' for i in range(6))}</g>
{person(200,300,0.8,1,'gold','blue','point','cap','neutral')}
<path d="M300 250h120" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('lazy', 'ソファに寝そべって、何もせず過ごしているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-180-30h360v80h-360z" class="violetp o"/>
  <path d="M-180-30q0-60 60-60h240q60 0 60 60z" class="violetp o"/>
</g>
<g transform="translate(260 240)">
  <ellipse cx="40" cy="20" rx="90" ry="26" class="teal o"/>
  <circle cx="-60" cy="0" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-86-4q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
  <path d="M-70 2h6M-52 2h6" class="a"/>
</g>
<g fill="{INK}" opacity=".7"><path d="M420 180q0-14 14-14t14 14q0 8-14 14h14v10h-30v-8q14-6 14-12 0-6-6-6t-6 6z"/></g>
<path d="M60 360h480" class="a"/>
""", ground=True)

add('lie', '床に体を横たえて、寝ている姿のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-200 20h400v20h-400z" class="goldd o"/>
  <ellipse cx="20" cy="-10" rx="110" ry="30" class="teal o"/>
  <circle cx="-110" cy="-30" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-140-34q4-30 30-30 26 0 30 28-16-10-30-4-12-8-30 6z" fill="{HAIR}"/>
  <path d="M-120-28h8M-100-28h8" class="a"/>
  <path d="M110-6l40 10M110 4l40-10" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('limb', '体から伸びる手足の位置を示したイラスト。', f"""
{person(300,346,1.4,1,'teal','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8">
  <circle cx="215" cy="250" r="40"/><circle cx="385" cy="250" r="40"/>
  <circle cx="272" cy="330" r="34"/><circle cx="328" cy="330" r="34"/>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('load', 'トラックの荷台に、荷物を積み込んでいるイラスト。', f"""
<g transform="translate(380 290)">
  <path d="M-170 40h130v-110h-130z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-40 40h200v-80H-40z" class="coral o"/>
  <circle cx="-120" cy="52" r="28" class="ink"/><circle cx="90" cy="52" r="28" class="ink"/>
</g>
{box(200,300,80,60,0,'gold')}
<path d="M260 250q60-40 100-20" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('loud', '大きな音が、遠くまで強く広がっているイラスト。', f"""
<g transform="translate(200 220)">
  <path d="M-40-30h40l60-50v160l-60-50h-40z" class="ink"/>
</g>
<g class="corals" opacity=".95" style="stroke-width:7">
  <path d="M300 160q34 34 34 60t-34 60"/><path d="M360 130q46 46 46 90t-46 90"/><path d="M420 100q58 58 58 120t-58 120"/>
</g>
""", ground=False)
print(' '.join(W)); print(sheet(W))
