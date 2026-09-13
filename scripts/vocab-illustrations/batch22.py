"""第22回: 消える・稼ぐ・交換・爆発など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('disagree', '二人が別の方向を指して、意見が合っていないイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','point','short','sad')}
{person(430,346,1.15,-1,'coral','gold','point','bob','sad')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"><path d="M250 230h60" marker-end="url(#ar)"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M360 260h-60" marker-end="url(#ar)"/></g>
<g class="corals" style="stroke-width:8"><path d="M280 150l40 40M320 150l-40 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('disappear', 'そこにあったものが薄れて、見えなくなるイラスト。', f"""
{box(140,260,110,80,0,'gold')}
<g opacity=".5">{box(300,260,110,80,0,'gold')}</g>
<g opacity=".15">{box(460,260,110,80,0,'gold')}</g>
<path d="M110 350h420" class="a"/>
<path d="M140 160h380" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('dislike', '差し出された皿を手で押し返して、嫌がっているイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','point','short','sad')}
<g transform="translate(420 280)">
  <ellipse rx="76" ry="26" fill="#fffdf6" class="o"/>
  <g class="greenp o"><circle cx="-20" cy="-12" r="20"/><circle cx="18" cy="-8" r="20"/></g>
</g>
<path d="M330 240h-40" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:7"><path d="M320 170l30 30M350 170l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('divorced', '一つだった指輪が二つに離れ、別々になったイラスト。', f"""
<g transform="translate(200 220)">
  <circle r="56" fill="none" stroke="{TONES['gold'][0]}" stroke-width="12"/>
</g>
<g transform="translate(400 220)">
  <circle r="56" fill="none" stroke="{TONES['gold'][0]}" stroke-width="12"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 320h-60"/><path d="M330 320h60"/></g>
<g class="corals" style="stroke-width:7"><path d="M280 200l40 40M320 200l-40 40"/></g>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('dose', '一回分の薬をスプーンに量り取っているイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-50-100h100l-10 200h-80z" fill="#f4fbff" class="o"/>
  <path d="M-44-30h88l-8 130h-72z" class="coralp o"/>
  <path d="M-24-110h48v14h-48z" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5"><path d="M50-60h16M50-20h16M50 20h16"/></g>
</g>
<g transform="translate(400 240) rotate(-16)">
  <ellipse rx="40" ry="22" fill="#f0dfc2" stroke="{INK}" stroke-width="2.5"/>
  <ellipse rx="28" ry="13" class="coralp o"/>
  <path d="M36 0h90" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('downstairs', '階段を下って、下の階へ降りていくイラスト。', f"""
<g class="goldp o">
  <rect x="80" y="120" width="90" height="240"/><rect x="170" y="180" width="90" height="180"/>
  <rect x="260" y="240" width="90" height="120"/><rect x="350" y="300" width="90" height="60"/>
</g>
{person(140,120,0.7,1,'teal','blue','walk','short','neutral')}
<path d="M220 160L420 290" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('earn', '働いた分の給料を受け取っているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','carry','short','smile')}
{box(180,266,90,64,0,'gold')}
<path d="M290 250h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(440 260)">
  <path d="M-70-40h140v80h-140z" class="greenp o"/>
  <circle r="20" class="green o"/>
  <path d="M-70-10h140" fill="none" stroke="{TONES['green'][2]}" stroke-width="4"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('educate', '黒板の前で、子どもたちに教えているイラスト。', f"""
<g transform="translate(400 210)">
  <path d="M-140-100h280v200h-280z" fill="#3d4c5c" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#c9d4dd" stroke-width="4"><path d="M-100-50h200M-100-10h160M-100 30h180"/></g>
</g>
{person(140,346,1.15,1,'teal','blue','point','bun','neutral')}
<g opacity=".85">{person(300,366,0.7,-1,'coral','gold','stand','short','smile')}{person(380,366,0.7,-1,'violet','teal','stand','bob','smile')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('electric', 'コードでつながった機器に、電気が流れているイラスト。', f"""
<g transform="translate(400 250)">
  <path d="M-90-80h180v160h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-60-50h120v80h-120z" class="bluep o"/>
  <g class="green o"><circle cx="-60" cy="54" r="12"/></g>
</g>
<path d="M120 300h190" fill="none" stroke="{INK}" stroke-width="8"/>
<g transform="translate(110 300)"><path d="M-30-20h30v40h-30z" class="ink"/><path d="M-46-10h16v8h-16zM-46 4h16v8h-16z" class="ink"/></g>
<g transform="translate(250 200)">
  <path d="M-14-40l-16 46h20l-10 34 30-50h-20l16-30z" class="gold o"/>
</g>
""", ground=True)

add('electronics', '基板と小さな部品が並んだ電子機器の中身のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-180-110h360v220h-360z" class="greenp o"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="3">
    <path d="M-140-60h120v60h-120M20-60h120v120"/>
    <path d="M-140 40h100M40 20h100"/>
  </g>
  <g class="ink"><rect x="-100" y="-30" width="70" height="40"/><rect x="40" y="30" width="80" height="40"/></g>
  <g class="coral o"><circle cx="-140" cy="-80" r="10"/><circle cx="140" cy="80" r="10"/></g>
</g>
""", ground=True)

add('emergence', '水面から新しい芽が現れ出るイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(300 250)">
  <path d="M0 0v-90" fill="none" stroke="{TONES['green'][2]}" stroke-width="9" stroke-linecap="round"/>
  <path d="M0-50c-40-10-52-34-52-34 36-10 52 34 52 34z" class="green o"/>
  <path d="M0-90c-30-16-30-48-30-48 30 6 30 48 30 48z" class="green o"/>
</g>
<path d="M420 200v-60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('employ', '面接に合格した人を、職場に迎え入れているイラスト。', f"""
{building(450,300,0.95,'teal')}
{person(160,346,1.1,1,'coral','blue','walk','short','smile')}
<g transform="translate(280 250)">
  <path d="M-50-60h100v120h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-34h60M-30-10h60"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-20 26l12 12 22-24"/></g>
</g>
<path d="M340 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('encourage', '背中を押して、相手を励ましているイラスト。', f"""
{person(360,346,1.15,1,'coral','blue','walk','short','smile')}
{person(180,346,1.15,1,'teal','gold','point','bob','smile')}
<path d="M250 250h50" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M420 240h80" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:4"><path d="M420 190l24-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('entertain', '舞台の演し物で、客を楽しませているイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-280-140h560v40h-560z" class="coralp o"/>
  <path d="M-240-100v40M240-100v40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{person(300,300,1.1,1,'violet','blue','up','bun','smile')}
<g transform="translate(300 330)"><path d="M-260-20h520v40h-520z" class="goldd o"/></g>
<g opacity=".8">{person(140,380,0.7,1,'coral','gold','up','short','smile')}{person(470,380,0.7,-1,'teal','violet','up','bob','smile')}</g>
""", ground=False)

add('enthusiast', '好きな模型を並べて、夢中になっている人のイラスト。', f"""
{person(160,346,1.15,1,'coral','blue','point','bun','smile')}
<g transform="translate(400 280)">
  <path d="M-140-20h280v20h-280z" class="goldp o"/>
  <g transform="translate(-80 -40) scale(0.4)">{plane(0,0,1.0,-8,'teal')}</g>
  <g transform="translate(30 -40) scale(0.35)">{plane(0,0,1.0,6,'coral')}</g>
</g>
<g class="golds" style="stroke-width:4"><path d="M250 200l24-24M240 250h-26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('equipment', '作業に使う道具や機器がひとそろい並んだイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-220-20h440v20h-440z" class="goldp o"/>
</g>
<g transform="translate(150 250) rotate(-8)">
  <path d="M-40-20h80v26h-80z" class="goldd o"/>
  <path d="M0 6v40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(300 240)">
  <path d="M-60-60h120v120h-120z" fill="#dfe6ea" class="o"/>
  <circle r="26" class="tealp o"/>
</g>
<g transform="translate(450 250)">
  <path d="M-12-60h24v50h-24z" class="coral o"/>
  <path d="M-5-10h10v60h-5z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
""", ground=True)

add('establishment', '新しい施設が完成して、看板が掛けられるイラスト。', f"""
{building(300,300,1.1,'teal')}
<g transform="translate(300 200)">
  <path d="M-70-24h140v48h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46 0h92"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 200l18 18 30-36"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('estate', '広い土地が区画に分けられ、境界が示されたイラスト。', f"""
<path d="M0 200h600v200H0z" fill="#e4efe2"/>
<path d="M0 200h600" class="a" opacity=".4"/>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="5" stroke-dasharray="14 10">
  <path d="M200 200v200M400 200v200M0 300h600"/>
</g>
{building(100,290,0.45,'teal')}
{building(300,290,0.45,'gold')}
{tree(500,290,0.5)}
""", ground=False)

add('everyday', '毎日くり返す身支度の場面を並べたイラスト。', f"""
<g transform="translate(140 250)">
  <circle r="60" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-36M0 0l24 14" class="a"/>
</g>
<g transform="translate(300 250)">
  <path d="M-50-50h100l-8 100h-84z" fill="#fffdf6" class="o"/>
  <path d="M-44-20h88l-6 70h-76z" class="goldp o"/>
</g>
<g transform="translate(460 250)">
  <path d="M-50-60l-24 14 10 26 14-8v78h100V-28l14 8 10-26-24-14h-34q-12 10-24 0z" class="tealp o"/>
</g>
<path d="M60 350h480" class="muted"/>
""", ground=True)

add('examine', '虫めがねで細かい部分を、詳しく調べているイラスト。', f"""
<g transform="translate(340 280)">
  <path d="M-140-40h280v100h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-110-14h220M-110 14h180"/></g>
</g>
<g transform="translate(320 200)">
  <circle r="80" fill="#e8f4fb" opacity=".4" stroke="{INK}" stroke-width="7"/>
  <path d="M56 56l60 60" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
</g>
{person(130,346,0.95,1,'teal','blue','point','short','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('exchange', '二人が持ち物を互いにわたし合っているイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','give','short','smile')}
{person(440,346,1.1,-1,'coral','gold','give','bob','smile')}
<g transform="translate(250 220)">{box(0,0,60,44,0,'gold')}</g>
<g transform="translate(360 280)">{box(0,0,60,44,0,'teal')}</g>
<g fill="none" stroke="{INK}" stroke-width="4">
  <path d="M290 200q60-30 100 40" marker-end="url(#ar)"/>
  <path d="M320 300q-60 30-100-40" marker-end="url(#ar)"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('execution', '手順表のとおりに作業を進めて、完了印がつくイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50-70h120M-50-30h120M-50 10h120M-50 50h90"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">
    <path d="M-86-74l10 10 16-18M-86-34l10 10 16-18M-86 6l10 10 16-18"/>
  </g>
</g>
<g transform="translate(430 260)">{box(0,0,150,110,32,'gold')}</g>
<path d="M300 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('exist', 'そこに確かにあるものと、何もない空間を比べたイラスト。', f"""
<g transform="translate(180 250)">{box(0,0,140,110,32,'gold')}</g>
<g transform="translate(430 250)">
  <path d="M-70-55h140v110h-140z" class="muted"/>
</g>
<path d="M120 350h360" class="a"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M150 130l18 18 30-36"/></g>
<g class="corals" style="stroke-width:7"><path d="M410 140l40 40M450 140l-40 40"/></g>
""", ground=True)

add('expertise', '専門の道具を的確に使い分けている手元のイラスト。', f"""
<circle cx="120" cy="100" r="56" class="goldp"/>
{hand(200,220,1)}
<g transform="translate(340 230) rotate(-10)">
  <path d="M-50-16h100v32h-100z" class="goldd o"/>
  <path d="M50-24h34v48H50z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(430 320)">
  <path d="M-90-20h180v20h-180z" class="goldp o"/>
  <g class="tealp o"><rect x="-70" y="-60" width="30" height="40"/><rect x="-20" y="-60" width="30" height="40"/><rect x="30" y="-60" width="30" height="40"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M250 140l18 18 30-36"/></g>
""", ground=True)

add('explode', '中の圧力で、勢いよく破裂して飛び散るイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-160 0l70-36-36-64 80 28 26-80 34 78 72-36-24 70 84 12-70 46 50 54-80-10-12 74-50-60-60 50 12-74z" class="coral o"/>
  <path d="M-80 0l36-18-18-32 40 14 14-40 18 40 36-18-12 34 42 8-36 22 26 28-40-6-6 38-26-30-30 26 6-38z" class="goldp o"/>
</g>
<g class="corals" marker-end="url(#ar)" style="stroke-width:5">
  <path d="M110 90L50 40"/><path d="M490 90l60-50"/><path d="M110 330L50 380"/><path d="M490 330l60 50"/>
</g>
""", ground=False, arrow=True)

add('export', '国内で作った品を、船で外国へ送り出すイラスト。', f"""
<path d="M0 260h600v140H0z" class="bluep"/>
<path d="M0 260h180v140H0z" class="ground"/>
<path d="M0 260h180" class="a"/>
{building(80,260,0.5,'teal')}
<g transform="translate(380 250)">
  <path d="M-110 0h220l-24 34h-172z" class="teal o"/>
  <path d="M-110 0h220" class="a"/>
  <g class="goldp o"><rect x="-70" y="-40" width="50" height="40"/><rect x="-10" y="-40" width="50" height="40"/></g>
</g>
<path d="M200 200h300" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('express', '思っていることを、言葉と表情で外に出しているイラスト。', f"""
{person(190,346,1.2,1,'teal','blue','point','short','smile')}
<g transform="translate(400 200)">
  <path d="M-90-50h180q16 0 16 16v56q0 16-16 16h-120l-26 22 6-22h-40q-16 0-16-16v-56q0-16 16-16z" class="paper"/>
  <path d="M0 10l-24-28 12-14 12 12 12-12 12 14z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('face', '目の前の壁に正面から向き合っているイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','stand','short','neutral')}
<g transform="translate(430 240)">
  <path d="M-80-140h160v280h-160z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><path d="M-80-70h160M-80 0h160M-80 70h160"/></g>
</g>
<path d="M270 240h70" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('fair', '天びんが左右等しく釣り合い、公平さを示すイラスト。', f"""
<path d="M300 340V140" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M250 356h100" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>
<path d="M150 150h300" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="300" cy="150" r="13" class="teal o"/>
<path d="M150 150v34M450 150v34" class="a"/>
<path d="M96 184h108l-14 30H110z" class="goldp o"/>
<path d="M396 184h108l-14 30H410z" class="goldp o"/>
<circle cx="150" cy="164" r="18" class="coral o"/>
<circle cx="450" cy="164" r="18" class="coral o"/>
<path d="M120 132h360" class="muted"/>
""", ground=True)

add('fancy', '装飾の多い高級な器と、簡素な器を比べたイラスト。', f"""
<g transform="translate(180 260)">
  <path d="M-60-70h120l-10 130h-100z" fill="#fffdf6" class="o"/>
  <path d="M-60-70h120" class="a"/>
</g>
<g transform="translate(420 260)">
  <path d="M-70-80h140l-12 150h-116z" fill="#fffdf6" class="o"/>
  <path d="M-70-80h140" class="a"/>
  <g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"><path d="M-62-40h124M-58 0h116M-54 40h108"/></g>
  <g class="gold o"><circle cx="0" cy="-20" r="12"/><circle cx="-30" cy="20" r="9"/><circle cx="30" cy="20" r="9"/></g>
</g>
<path d="M300 130v230" class="muted"/>
<path d="M100 360h400" class="a"/>
""", ground=True)

add('fantasy', '空想の世界が、雲の中に思い浮かぶイラスト。', f"""
{person(150,346,1.1,1,'violet','blue','think','bun','smile')}
<g transform="translate(400 180)">
  <path d="M-160 50q-16-76 52-90 20-52 100-36 46 8 60 56 76-8 84 62 4 56-64 60h-190q-46-4-42-52z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 16)">
    <path d="M-70 40L-20-40l40 46 40-60 50 94z" class="violetp o"/>
    <circle cx="60" cy="-40" r="20" class="goldp o"/>
    <path d="M-30-10l10 16 18 4-14 12 4 18-18-10-18 10 4-18-14-12 18-4z" class="gold o" transform="translate(-10 -20) scale(0.8)"/>
  </g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="240" cy="270" r="12"/><circle cx="214" cy="296" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('favour', 'ちょっとしたお願いを聞いて、荷物を持ってあげるイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
{person(200,346,1.1,1,'coral','blue','stand','bob','smile')}
{person(400,346,1.1,-1,'teal','violet','carry','short','smile')}
{box(400,266,90,64,0,'gold')}
<path d="M320 230q-40-20-70-14" class="a" marker-end="url(#ar)"/>
<g transform="translate(270 190)"><path d="M0 16l-20-24 10-12 10 10 10-10 10 12z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('feature', '製品の一部だけを丸で囲んで、特徴を示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-110h320v220h-320z" fill="#dfe6ea" class="o"/>
  <path d="M-130-80h260v130h-260z" class="bluep o"/>
  <g class="ink"><rect x="-60" y="70" width="120" height="20" rx="6"/></g>
</g>
<circle cx="380" cy="200" r="60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M470 130q-40 30-60 40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('fee', '窓口で決まった料金を払っているイラスト。', f"""
<g transform="translate(430 260)">
  <path d="M-110-120h220v240h-220z" fill="#dfe6ea" class="o"/>
  <path d="M-80-90h160v70h-160z" class="bluep o"/>
  <path d="M-60 20h120v20h-120z" class="ink"/>
  <g transform="translate(0 -55)"><path d="M-40-14h80v28h-40z" class="paper"/></g>
</g>
{person(160,346,1.1,1,'coral','blue','give','short','neutral')}
<g transform="translate(270 260)">
  <circle r="22" class="goldp o"/>
  <path d="M-7-10h14v20h-14z" class="goldd"/>
</g>
<path d="M310 210h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
