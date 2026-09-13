"""第66回: 刑務所・進歩・範囲・関係など46語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('princess', '王冠をかぶった王女のイラスト。', f"""
{person(300,346,1.35,1,'violet','violet','stand','bob','smile')}
<g transform="translate(300 186)"><path d="M-40 16l-8-44 24 18 24-30 24 30 24-18-8 44z" class="gold o"/></g>
<g class="golds" style="stroke-width:5"><path d="M400 200l24-18M180 200l-24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('principal', '学校で先頭に立つ長のイラスト。', f"""
{person(170,346,1.35,1,'blue','blue','stand','short','neutral')}
<g transform="translate(170 226)"><path d="M-16-16l6 14 16 2-12 11 3 16-13-8-13 8 3-16-12-11 16-2z" class="gold o"/></g>
<g transform="translate(420 280)">
  <path d="M-110 60h220v-120h-220z" fill="#f4ead2" class="o"/>
  <path d="M-130-60l130-70 130 70z" class="teal o"/>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="2"><rect x="-80" y="-20" width="50" height="40"/><rect x="30" y="-20" width="50" height="40"/></g>
</g>
<path d="M250 240h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('printing', '版から紙へ文字を刷るイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-150-60h300v120h-300z" fill="#dfe6ea" class="o"/>
  <path d="M-100-110h200v50h-200z" fill="#c9d3dc" class="o"/>
  <path d="M-90 60h180v14h-180z" class="ink"/>
</g>
<g transform="translate(300 350)">
  <path d="M-90-30h180v60h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-10" width="120" height="10"/><rect x="-60" y="8" width="90" height="10"/></g>
</g>
<path d="M470 240v60" class="a" marker-end="url(#ar)"/>
<path d="M60 396h480" class="a"/>
""", ground=True, arrow=True)

add('prior', '本番の前に置かれた段を示すイラスト。', f"""
<g class="coral o"><rect x="120" y="200" width="110" height="130"/></g>
<g class="tealp o"><rect x="330" y="200" width="110" height="130"/></g>
<path d="M175 150v30" class="a" marker-end="url(#ar)"/>
<g class="a" marker-end="url(#ar)"><path d="M110 370h340"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('prison', '鉄格子で囲われた刑務所のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#c9c6b8" class="o"/>
  <path d="M-160-100h320v220h-320z" fill="#e4e9ee" class="o"/>
  <g fill="{INK}">{''.join(f'<rect x="{-150+i*44}" y="-100" width="14" height="220"/>' for i in range(8))}</g>
  <path d="M-160-100h320v14h-320z" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('prisoner', '格子の内側に入れられた人のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-140h320v280h-320z" fill="#e4e9ee" class="o"/>
  <g fill="{INK}">{''.join(f'<rect x="{-140+i*46}" y="-120" width="14" height="250"/>' for i in range(7))}</g>
</g>
<g transform="translate(300 250) scale(0.8)">{person(0,60,1.0,1,'violet','violet','stand','cap','sad')}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('probable', '起こりそうな方に、太い道がついているイラスト。', f"""
<circle cx="100" cy="230" r="22" class="teal o"/>
<path d="M130 210q120-70 220-50t140 20" fill="none" stroke="{TONES['teal'][0]}" stroke-width="16" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M130 250q120 70 220 50t140-20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 120l18 18 30-36"/></g>
""", ground=False, arrow=True)

add('problematic', '仕組みに引っかかりがあって、うまく回らないイラスト。', f"""
<g transform="translate(300 240)">
  <g fill="none" stroke="{INK}" stroke-width="12"><circle cx="-70" r="60"/><circle cx="70" cy="40" r="42"/></g>
  <g fill="{INK}">{''.join(f'<rect x="-78" y="-78" width="16" height="20" transform="rotate({i*60} -70 0)"/>' for i in range(6))}</g>
  <g transform="translate(10 -10) rotate(20)"><path d="M-40-10h80v20h-80z" class="coral o"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 140l34 34M504 140l-34 34"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('proceed', 'いったん止まったあと、また先へ進むイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','walk','short','neutral')}
<g transform="translate(330 250)">
  <circle r="40" class="greenp o"/>
  <path d="M-14-20l34 20-34 20z" class="green"/>
</g>
<path d="M400 250h130" class="a" marker-end="url(#ar)"/>
<g opacity=".35">{person(120,346,1.0,1,'teal','blue','stand','short','neutral')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('producer', '材料から品を作り出す生産者のイラスト。', f"""
{person(150,346,1.15,1,'teal','blue','reach','cap','neutral')}
<g transform="translate(320 250)">
  <path d="M-90-90h180v180h-180z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="-30" cy="-20" r="34"/><circle cx="40" cy="30" r="24"/></g>
</g>
{box(490,290,100,80,0,'gold')}
<path d="M420 200h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('production', '工場で次々に品ができていくイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-240-20h480v40h-480z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M{-180+i*80}-20v40"/>' for i in range(5))}</g>
</g>
<g transform="translate(160 250)"><path d="M-30-30h60v60h-60z" class="tealp o"/></g>
<g transform="translate(300 250)"><path d="M-30-30h60v60h-60z" class="teal o"/></g>
{box(450,250,80,60,0,'gold')}
<path d="M120 160h360" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('profound', '底の深い井戸をのぞきこむイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-110 100h220v-40h-220z" fill="#b09274" stroke="{INK}" stroke-width="3"/>
  <path d="M-90 60h180l-20-160h-140z" fill="#41506a"/>
  <path d="M-60 20h120l-10-100h-100z" fill="#2f4055"/>
  <g class="muted"><path d="M-30-40h60"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 180v140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('progress', '段を一つずつ上がって前へ進むイラスト。', f"""
<g class="goldd o">{''.join(f'<rect x="{100+i*80}" y="{320-i*50}" width="80" height="{50+i*50}"/>' for i in range(5))}</g>
<g opacity=".4">{person(140,320,0.7,1,'teal','blue','walk','short','neutral')}</g>
{person(460,120,0.7,1,'teal','blue','walk','short','smile')}
<path d="M120 240l340-160" class="a" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('progressive', '古い形から新しい形へ、進んで変えるイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-70-60h140v120h-140z" fill="#cfc9b8" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-40-20h80M-40 10h60"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-80-80h160v160h-160z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-50" y="-40" width="100" height="20"/><rect x="-50" y="0" width="70" height="20"/></g>
  <g class="golds" style="stroke-width:5"><path d="M-100-100l-22-18M100-100l22-18"/></g>
</g>
<path d="M280 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('promising', '芽が勢いよく伸びて、有望に見えるイラスト。', f"""
<g transform="translate(220 320)">
  <path d="M0 20v-90" fill="none" stroke="{TONES['green'][2]}" stroke-width="8"/>
  <g class="green o"><ellipse cx="-30" cy="-60" rx="30" ry="16" transform="rotate(-24 -30 -60)"/><ellipse cx="30" cy="-84" rx="30" ry="16" transform="rotate(24 30 -84)"/></g>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M300 220q80-40 160-90"/></g>
<g transform="translate(500 100)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
{sun(120,110,26)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('prompt', '呼ばれてすぐに応じるイラスト。', f"""
{person(180,346,1.15,1,'blue','blue','point','short','neutral')}
<g transform="translate(320 200)">
  <circle r="40" fill="#fffdf6" class="o"/>
  <path d="M-20 0h30M4-16l16 16-16 16" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
{person(470,346,1.15,1,'teal','gold','walk','bob','smile')}
<g class="a" marker-end="url(#ar)"><path d="M380 200h50"/></g>
<g transform="translate(500 140)">
  <circle r="30" fill="#fffdf6" class="o"/>
  <path d="M0-20v20l14 8" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pronounced', '線がはっきり濃く出ているイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-90-70h180v140h-180z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="#cfd8e0" stroke-width="4"><path d="M-60-20h120M-60 20h120"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-90-70h180v140h-180z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="12"><path d="M-60-20h120M-60 20h120"/></g>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('prospective', 'これから客になりそうな人を見込むイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','point','short','smile')}
{person(430,346,1.1,-1,'coral','gold','walk','bob','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"><circle cx="430" cy="250" r="100"/></g>
<path d="M240 220h100" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('protection', '傘やヘルメットで身を守るイラスト。', f"""
{person(300,346,1.2,1,'teal','blue','stand','cap','smile')}
<g transform="translate(300 220)">
  <path d="M-40-16h80v10h-80z" class="coral o"/>
</g>
<g transform="translate(300 150)">
  <path d="M-140 0q0-80 140-80t140 80z" class="violetp o"/>
</g>
<g class="muted" opacity=".9">{''.join(f'<path d="M{120+i*70} 60l-14 40"/>' for i in range(7))}</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 300l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('protective', '前に立って相手をかばうイラスト。', f"""
{person(250,346,1.25,1,'blue','blue','carry','short','flat')}
<g transform="translate(330 250)">
  <path d="M0-80q56 22 56 66 0 56-56 78-56-22-56-78 0-44 56-66z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
</g>
{person(430,346,0.85,1,'coral','gold','stand','cap','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M180 200h60M180 300h60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('provincial', '都から離れた地方の町を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-200 0h400"/></g>
  <g class="tealp o"><circle cx="-120" cy="-70" r="30"/></g>
  <g fill="{INK}"><circle cx="-120" cy="-70" r="8"/></g>
  <g class="greenp o"><rect x="40" y="40" width="120" height="70"/></g>
</g>
<path d="M500 340l-90-60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('psychological', '心の内側のはたらきを示したイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(430 210)">
  <path d="M0-110q100 0 100 90 0 78-100 78t-100-78q0-90 100-90z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"><path d="M0-104v140M-50-84q34 30 0 60t24 60M50-84q-34 30 0 60t-24 60"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="300" r="12"/><circle cx="266" cy="324" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('punctual', '約束の時刻ぴったりに現れるイラスト。', f"""
<g transform="translate(430 210)">
  <circle r="80" fill="#fffdf6" class="o"/>
  <path d="M0-50v50l30 16" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
{person(180,346,1.2,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M280 190l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('punishment', '悪いことをした人に罰が与えられるイラスト。', f"""
{person(180,346,1.15,1,'violet','violet','stand','cap','sad')}
<g transform="translate(400 220)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-60h140M-70-20h140"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-40 20l70 60M30 20l-70 60"/></g>
</g>
<path d="M290 250h-50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('quantity', '同じ品の数量を数えるイラスト。', f"""
<g class="teal o">{''.join(f'<rect x="{110+c*70}" y="{180+r*80}" width="52" height="60"/>' for r in range(2) for c in range(6))}</g>
<g class="a" marker-end="url(#ar)"><path d="M100 350h420"/></g>
<g fill="{INK}"><rect x="480" y="130" width="60" height="12"/></g>
""", ground=False, arrow=True)

add('quietly', '足音を立てず、静かに歩くイラスト。', f"""
{person(250,346,1.2,1,'teal','blue','walk','short','smile')}
<g transform="translate(320 220)">
  <path d="M-10 0h20v-70h-20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(450 250)">
  <path d="M-50-50h60l50-40v180l-50-40h-60z" class="ink"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M40-40l50 50M90-40l-50 50"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('quotation', '見積もりの金額が書かれた紙のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="{INK}"><rect x="-130" y="-110" width="130" height="18"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-130-50h260M-130-10h260M-130 30h260"/></g>
  <g fill="{INK}"><rect x="40" y="70" width="90" height="18"/></g>
  <g class="goldd o"><circle cx="-100" cy="80" r="20"/></g>
</g>
""", ground=True)

add('racing', '横一線で速さを競うレースのイラスト。', f"""
{person(150,346,1.1,1,'coral','blue','walk','cap','neutral')}
{person(260,346,1.1,1,'teal','gold','walk','short','neutral')}
{person(370,346,1.1,1,'gold','blue','walk','bob','neutral')}
<g class="muted"><path d="M110 210h-40M220 210h-40M330 210h-40"/></g>
<g transform="translate(510 250)"><path d="M-6-100h12v200h-12z" class="ink"/>
<g fill="{INK}"><rect x="-60" y="-100" width="18" height="18"/><rect x="-24" y="-100" width="18" height="18"/><rect x="-42" y="-82" width="18" height="18"/><rect x="-6" y="-82" width="18" height="18"/></g></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('radical', '根もとから丸ごと入れ替えるイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
  <path d="M-40 60v40h80V60" fill="none" stroke="{TONES['teal'][2]}" stroke-width="6"/>
</g>
<g transform="translate(430 250)">
  <path d="M0-70l70 130h-140z" class="coral o"/>
  <path d="M-30 60v40h60V60" fill="none" stroke="{TONES['coral'][2]}" stroke-width="6"/>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('rapid', '短い時間で一気に上がるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100h340M-170-110v210" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-150 90q60 0 90-180" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" marker-end="url(#ar)"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M220 140l-24-18M230 180h-28"/></g>
""", ground=True, arrow=True)

add('raw', '生のままの魚と、火を通した魚を比べたイラスト。', f"""
<g transform="translate(170 250)">
  <ellipse rx="80" ry="46" class="coralp o"/>
  <path d="M-80 0l-50-34v68z" class="coralp o"/>
  <circle cx="46" cy="-10" r="6" class="ink"/>
</g>
<g transform="translate(430 250)">
  <ellipse rx="80" ry="46" fill="#c98a5e" stroke="{INK}" stroke-width="3"/>
  <path d="M-80 0l-50-34v68z" fill="#c98a5e" stroke="{INK}" stroke-width="3"/>
  <circle cx="46" cy="-10" r="6" class="ink"/>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
{flame(300,340,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('reaction', 'たたかれて、すぐ跳ね返るイラスト。', f"""
{hand(160,200,1)}
<g transform="translate(300 250)"><circle r="50" class="teal o"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M230 250h30M370 250h60"/></g>
<g class="corals" style="stroke-width:5"><path d="M300 180v-26M250 200l-20-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('receipt', '買い物のあとに渡される細長い領収書のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-100-150h200v300l-24-20-26 20-26-20-26 20-26-20-24 20z" class="paper"/>
  <g fill="{INK}"><rect x="-70" y="-120" width="100" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-70 {-80+i*34}h140"/>' for i in range(5))}</g>
  <g fill="{INK}"><rect x="0" y="100" width="70" height="14"/></g>
</g>
{hand(140,300,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('recommendation', '推薦の書面を差し出すイラスト。', f"""
{person(150,346,1.1,1,'blue','blue','give','short','smile')}
<g transform="translate(320 240)">
  <path d="M-90-80h180v160h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-50" width="90" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-10h120M-60 20h100"/></g>
  <g transform="translate(50 50)"><path d="M0-20l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="gold o"/></g>
</g>
{person(490,346,1.1,-1,'teal','gold','reach','bob','smile')}
<path d="M420 300h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('reduction', '量が削られて少なくなるイラスト。', f"""
<path d="M60 340h480" class="a"/>
<rect x="140" y="120" width="120" height="220" class="tealp o"/>
<rect x="360" y="240" width="120" height="100" class="coral o"/>
<path d="M300 160l60 60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M120 120h380"/></g>
""", ground=False, arrow=True)

add('region', '地図の一帯を囲って地域を示すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-200 20q120-50 200 0t200-30" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <path d="M-140-100q120-30 180 40t-40 140-160-20-20-160z" class="tealp o" opacity=".85"/>
  <path d="M-140-100q120-30 180 40t-40 140-160-20-20-160z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 9"/>
</g>
""", ground=True)

add('regulatory', '規則にもとづいて検査し、印をつけるイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','reach','short','neutral')}
<g transform="translate(400 230)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-60h140M-70-20h140M-70 20h140"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
    <path d="M-92-66l14 14 22-26"/><path d="M-92-26l14 14 22-26"/><path d="M-92 14l14 14 22-26"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><rect x="-120" y="-120" width="240" height="240"/></g>
</g>
<path d="M250 220h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('relation', '二つの間に線が引かれ、つながりを示すイラスト。', f"""
<g transform="translate(160 230)"><circle r="60" class="tealp o"/></g>
<g transform="translate(440 230)"><circle r="60" class="coralp o"/></g>
<path d="M225 230h150" fill="none" stroke="{INK}" stroke-width="10"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M300 300v50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('relative', '家族の輪の中にいる親戚のイラスト。', f"""
{person(150,346,1.1,1,'blue','blue','stand','short','smile')}
{person(260,346,1.1,1,'coral','gold','stand','bob','smile')}
{person(370,346,0.8,1,'teal','blue','stand','cap','smile')}
{person(480,346,1.1,1,'gold','violet','stand','short','smile')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="100" y="180" width="440" height="180" rx="18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('release', '閉じていた戸を開けて、外へ放つイラスト。', f"""
<g transform="translate(200 240)">
  <path d="M-110-140h220v280h-220z" fill="#e4e9ee" class="o"/>
  <g fill="{INK}">{''.join(f'<rect x="{-90+i*44}" y="-120" width="12" height="200"/>' for i in range(4))}</g>
  <path d="M90-120h20v200H90z" fill="none"/>
</g>
<g transform="translate(430 250)">
  <ellipse rx="60" ry="40" fill="#fffdf6" class="o"/>
  <circle cx="50" cy="-24" r="24" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M-60 0l-40-24v48z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M320 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('relevant', '問いに関わる資料だけを選び出すイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-100-90h200v180h-200z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="teal o"><rect x="-70" y="-60" width="60" height="40"/><rect x="10" y="0" width="60" height="40"/></g>
  <g class="mutedfill" fill="#cfd8e0"><rect x="-70" y="20" width="60" height="40"/><rect x="10" y="-60" width="60" height="40"/></g>
</g>
<g transform="translate(440 230)">
  <path d="M-70-70h140v140h-140z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
  <g class="teal o"><rect x="-50" y="-40" width="60" height="40"/><rect x="-10" y="10" width="60" height="40"/></g>
</g>
<path d="M300 230h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('reliable', '何度使っても同じ結果が出るイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-80h280v160h-280z" fill="#dfe6ea" class="o"/>
  <g class="green o"><circle cx="90" cy="-50" r="14"/></g>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="-40" cy="0" r="40"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M120 130l14 14 24-30"/><path d="M180 130l14 14 24-30"/><path d="M240 130l14 14 24-30"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('relieved', '重荷が下りて、ほっと息をつくイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','stand','short','smile')}
<g opacity=".35" transform="translate(200 190)"><path d="M-60-30h120v50h-120z" class="muted"/></g>
<path d="M300 180q60-40 110 20" class="a" marker-end="url(#ar)"/>
<g transform="translate(450 250)"><path d="M-60-30h120v60h-120z" class="goldd o"/></g>
<g class="muted"><path d="M280 250q40-16 60 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('religion', '寺院と祈りで、宗教を示したイラスト。', f"""
<g transform="translate(400 240)">
  <path d="M-110 100h220v-150h-220z" fill="#f4ead2" class="o"/>
  <path d="M-130-50l130-90 130 90z" class="tealp o"/>
  <g fill="{TONES['gold'][2]}"><rect x="-8" y="-190" width="16" height="56"/><rect x="-34" y="-172" width="68" height="16"/></g>
  <path d="M-40 100V30h80v70z" class="goldd o"/>
</g>
{person(160,346,1.15,1,'violet','blue','stand','short','neutral')}
<g transform="translate(160 226)"><path d="M-20 26q-4-38 20-50 24 12 20 50z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('reluctant', '気が進まず、足が前に出ないイラスト。', f"""
<g transform="translate(230 346) rotate(-14)">{person(0,0,1.2,1,'teal','blue','stand','short','flat')}</g>
<g transform="translate(450 250)">
  <path d="M-70-70h140v140h-140z" class="coralp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M310 250h60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M270 320h-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
