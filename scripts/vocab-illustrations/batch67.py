"""第67回: 範囲・責任・危険・場面など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('range', '下限から上限までの幅を示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-220-30h440v60h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-120-30h240v60h-240z" class="teal o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M-120-70v140M120-70v140"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 150h240M420 150H180"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('remote', '町からずっと離れた一軒家のイラスト。', f"""
<g class="green o" opacity=".8"><path d="M0 320q150-50 300-20t300-10v110H0z"/></g>
<g opacity=".5">{building(110,320,0.55,'teal')}</g>
<g transform="translate(470 280)">
  <path d="M-60 50h120V-20h-120z" fill="#f4ead2" class="o"/>
  <path d="M-76-20l76-52 76 52z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 200h230M410 200H180"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('request', '書面で頼みごとを差し出すイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(320 240)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-40" width="90" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60 0h120M-60 30h90"/></g>
</g>
{person(490,346,1.1,-1,'blue','blue','reach','bob','neutral')}
<path d="M420 300h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('research', '資料と実験でくり返し調べるイラスト。', f"""
<g transform="translate(400 250)">
  <path d="M-16-90h32v40l46 100h-124l46-100z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-52 20h104l22 30h-148z" class="tealp o"/>
</g>
{person(150,340,1.05,1,'blue','blue','think','bob','neutral')}
<g transform="translate(250 230)">
  <path d="M-50-50h100v90h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-24h60M-30 0h60M-30 24h40"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('reservation', '席を予約して、名札を置いておくイラスト。', f"""
<g transform="translate(300 310)">
  <g class="goldd o"><rect x="-230" y="-20" width="130" height="20"/><rect x="-65" y="-20" width="130" height="20"/><rect x="100" y="-20" width="130" height="20"/></g>
  <g class="goldd o"><rect x="-230" y="-90" width="20" height="70"/><rect x="-65" y="-90" width="20" height="70"/><rect x="100" y="-90" width="20" height="70"/></g>
</g>
<g transform="translate(300 240)">
  <path d="M-6 30h12v-40h-12z" class="ink"/>
  <path d="M-60-40h120v40h-120z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-40" y="-28" width="80" height="10"/></g>
</g>
<circle cx="300" cy="280" r="76" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('residential', '住宅ばかりが並ぶ地区のイラスト。', f"""
<g transform="translate(300 300)"><path d="M-250-10h500v14h-500z" fill="#e6dcc9"/></g>
<g transform="translate(140 270)"><path d="M-56 40h112V-16h-112z" fill="#f4ead2" class="o"/><path d="M-70-16l70-46 70 46z" class="coral o"/></g>
<g transform="translate(300 270)"><path d="M-56 40h112V-16h-112z" fill="#f4ead2" class="o"/><path d="M-70-16l70-46 70 46z" class="teal o"/></g>
<g transform="translate(460 270)"><path d="M-56 40h112V-16h-112z" fill="#f4ead2" class="o"/><path d="M-70-16l70-46 70 46z" class="gold o"/></g>
{tree(220,320,0.5)}{tree(380,320,0.5)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('respective', 'それぞれの持ち主に、それぞれの品が対応するイラスト。', f"""
{person(160,340,0.95,1,'teal','blue','stand','short','smile')}
{person(300,340,0.95,1,'coral','gold','stand','bob','smile')}
{person(440,340,0.95,1,'gold','blue','stand','cap','smile')}
<g class="tealp o"><rect x="130" y="150" width="60" height="50"/></g>
<g class="coralp o"><rect x="270" y="150" width="60" height="50"/></g>
<g class="goldp o"><rect x="410" y="150" width="60" height="50"/></g>
<g class="a" marker-end="url(#ar)"><path d="M160 240v-30M300 240v-30M440 240v-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('response', '問いかけに返事が返ってくるイラスト。', f"""
{person(150,346,1.15,1,'teal','blue','stand','short','neutral')}
{person(450,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="3">
  <path d="M210 130h130v60H210z"/><path d="M255 190l-14 26 34-26z"/>
  <path d="M260 220h130v60H260z"/><path d="M330 280l14 26-34-26z"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M250 250h-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('responsibility', '重い荷を自分の肩に担うイラスト。', f"""
{person(300,346,1.35,1,'blue','blue','carry','short','neutral')}
{box(300,200,180,90,0,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M470 200v60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('responsible', '自分の担当だと札を持って引き受けるイラスト。', f"""
{person(200,346,1.25,1,'blue','blue','carry','short','neutral')}
<g transform="translate(200 240)">
  <path d="M-60-30h120v60h-120z" class="paper"/>
  <g fill="{INK}"><rect x="-40" y="-10" width="80" height="12"/></g>
</g>
<g transform="translate(440 250)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
</g>
<path d="M290 250h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 180l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('revolutionary', 'それまでの形をひっくり返す新しさのイラスト。', f"""
<g transform="translate(160 250)" opacity=".5">
  <path d="M-70-60h140v120h-140z" fill="#cfc9b8" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 160l80 80M200 160l-80 80"/></g>
<g transform="translate(430 240)">
  <path d="M0-90l70 130h-140z" class="coral o"/>
  <g class="golds" style="stroke-width:6"><path d="M-100-70l-24-20M100-70l24-20M0-110v-26"/></g>
</g>
<path d="M280 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('ridiculous', '長靴を手にはめるような、ばかばかしいイラスト。', f"""
{person(250,346,1.3,1,'gold','blue','up','short','smile')}
<g transform="translate(180 190) rotate(-20)">
  <path d="M-24-50h48v70h-48z" class="coralp o"/>
  <path d="M-24 20h70v30h-70z" class="coralp o"/>
</g>
<g fill="{INK}" transform="translate(430 180)">
  <path d="M0 0q0-30 22-30t22 30q0 16-16 20v14h-12v-22q16-4 16-16t-9-10-11 14z"/><rect x="14" y="48" width="12" height="12"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 260l28 28M528 260l-28 28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('risk', '崖のふちに近づく危険を示したイラスト。', f"""
<path d="M60 340h240v60H60z" class="green o"/>
<path d="M300 340v60" fill="none" stroke="{INK}" stroke-width="4"/>
{person(230,340,1.1,1,'teal','blue','walk','short','flat')}
<g transform="translate(400 200)">
  <path d="M0-70l70 130h-140z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-6" y="-18" width="12" height="44"/><rect x="-6" y="34" width="12" height="12"/></g>
</g>
<path d="M310 260h60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('risky', 'ぐらつく板の上を渡る、危ういイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-240 40h100v60h-100zM140 40h100v60h-100z" fill="#c9d3dc" class="o"/>
  <path d="M-140 30h280v16h-280z" class="goldd o" transform="rotate(-3)"/>
</g>
<g transform="translate(300 300) rotate(-4)">{person(0,0,1.0,1,'coral','blue','walk','short','flat')}</g>
{drop(360,240,0.7)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 150l30 30M500 150l-30 30"/></g>
""", ground=False)

add('robot', '腕と車輪をもつロボットのイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-80-60h160v140h-160z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-60-140h120v70h-120z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><circle cx="-24" cy="-104" r="10"/><circle cx="24" cy="-104" r="10"/></g>
  <path d="M-6-170h12v30h-12z" class="ink"/><circle cy="-176" r="10" class="coral o"/>
  <path d="M-80-40h-40v70h40zM80-40h40v70H80z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <g class="teal o"><rect x="-40" y="-20" width="80" height="30"/></g>
  <circle cx="-40" cy="100" r="26" class="ink"/><circle cx="40" cy="100" r="26" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('robust', '太い柱で重さを支える、頑丈なイラスト。', f"""
{box(300,170,240,80,0,'gold')}
<g transform="translate(300 300)">
  <path d="M-140-50h280v40h-280z" class="teal o"/>
  <path d="M-120-10h60v70h-60zM60-10h60v70H60z" class="teald o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 100v40"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 200l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('role', '役の札を胸につけて舞台に立つイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-200-50h400v30h-400z" class="coral o"/>
  <path d="M-200-20h50q10 90 0 150h-50z" class="coralp o"/>
  <path d="M150-20h50v150h-50q-10-60 0-150z" class="coralp o"/>
</g>
<g transform="translate(300 250) scale(0.95)">{person(0,60,1.0,1,'violet','blue','stand','bob','smile')}</g>
<g transform="translate(300 250)">
  <path d="M-40-16h80v32h-80z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-26" y="-6" width="52" height="12"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('rough', 'ざらざらした面と、なめらかな面を比べたイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-90 60V-10q20-20 30 0t30-16 30 16 30-10v70z" class="goldd o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-90 60V-10h180v70z" class="tealp o"/>
  <path d="M-90-10h180" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
</g>
{hand(170,140,1)}
<g class="a" marker-end="url(#ar)"><path d="M290 250h50"/></g>
""", ground=True, arrow=True)

add('row', 'いくつも横一列に並ぶ列のイラスト。', f"""
<g class="teal o">{''.join(f'<rect x="{90+i*70}" y="200" width="52" height="70"/>' for i in range(7))}</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 9"><path d="M80 235h470"/></g>
<path d="M60 330h480" class="a"/>
""", ground=True)

add('rugby', '楕円のボールを抱えて走るラグビーのイラスト。', f"""
{person(250,346,1.3,1,'coral','blue','carry','short','flat')}
<g transform="translate(250 250) rotate(-20)">
  <ellipse rx="56" ry="34" fill="#8b5e3c" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#fffdf6" stroke-width="3"><path d="M-20-8h40M-20 8h40"/></g>
</g>
<g transform="translate(470 240)">
  <path d="M-50-100h10v200h-10zM40-100h10v200h-10z" class="ink"/>
  <path d="M-50-70h100v14h-100z" class="ink"/>
</g>
<path d="M340 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('rural', '畑と農家が広がる田舎のイラスト。', f"""
{sun(500,90,28)}
<g class="green o" opacity=".85"><path d="M0 320q150-60 300-30t300-20v130H0z"/></g>
<g transform="translate(180 280)">
  <path d="M-60 50h120V-10h-120z" fill="#f4ead2" class="o"/>
  <path d="M-76-10l76-50 76 50z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['green'][2]}" stroke-width="4" opacity=".8"><path d="M300 350q60-20 120 0M320 380q60-20 120 0"/></g>
{tree(470,330,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('sacred', '光に包まれた神聖な場のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#f6f0dc"/>
<g fill="#f7e6bd" opacity=".7"><circle cx="300" cy="210" r="160"/></g>
<g transform="translate(300 250)">
  <path d="M-90 90h180v-40h-180z" class="goldd o"/>
  <path d="M-60 50V-30h120v80z" class="goldp o"/>
  <g fill="{TONES['gold'][2]}"><rect x="-8" y="-110" width="16" height="80"/><rect x="-40" y="-84" width="80" height="16"/></g>
</g>
""", ground=False)

add('sadly', '肩を落として、悲しそうにするイラスト。', f"""
{person(280,346,1.35,1,'blue','blue','stand','short','sad')}
{drop(340,230,0.8)}
<g class="muted"><path d="M170 200q-16 20-16 44M390 200q16 20 16 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('safety', 'ヘルメットと囲いで安全を守るイラスト。', f"""
{person(300,346,1.25,1,'teal','blue','stand','cap','smile')}
<g transform="translate(300 224)"><path d="M-44-16h88v10h-88z" class="coral o"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-dasharray="14 10"><rect x="180" y="200" width="240" height="170" rx="16"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 180l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('sample', 'たくさんの中から一つ取り出した見本のイラスト。', f"""
<g transform="translate(220 250)">
  <path d="M-120-90h240v180h-240z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o">{''.join(f'<rect x="{-100+c*60}" y="{-70+r*60}" width="44" height="44"/>' for r in range(3) for c in range(4))}</g>
</g>
<g transform="translate(470 250)"><path d="M-30-30h60v60h-60z" class="teal o"/></g>
<path d="M360 250h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="440" y="220" width="60" height="60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sand', 'さらさらした砂と、砂浜のイラスト。', f"""
<path d="M0 260h600v140H0z" fill="#f3e3ae"/>
<g fill="#e0cd94"><ellipse cx="200" cy="320" rx="120" ry="30"/><ellipse cx="430" cy="350" rx="110" ry="26"/></g>
<g transform="translate(300 170) rotate(20)">
  <path d="M-40-40h80l-8 70h-64z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="#e0cd94"><circle cx="330" cy="230" r="6"/><circle cx="350" cy="250" r="5"/><circle cx="316" cy="252" r="4"/></g>
""", ground=False)

add('satellite', '地球のまわりを回る人工衛星のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a52"/>
<g transform="translate(300 260)"><circle r="120" class="bluep o"/><g class="green o"><path d="M-90-20q60-30 100 0t80-10v30q-60 30-100 0t-80 10z"/></g></g>
<g fill="none" stroke="#8b98a6" stroke-width="3" stroke-dasharray="12 10"><ellipse cx="300" cy="250" rx="230" ry="120"/></g>
<g transform="translate(480 150)">
  <path d="M-30-20h60v40h-60z" fill="#c9d3dc" stroke="{INK}" stroke-width="2"/>
  <path d="M-100-16h60v32h-60zM40-16h60v32H40z" class="bluep o"/>
  <path d="M0-20v-26" fill="none" stroke="#c9d3dc" stroke-width="4"/>
</g>
""", ground=False)

add('scattered', '物があちこちに散らばっているイラスト。', f"""
<g class="tealp o" ><circle cx="120" cy="150" r="22"/><circle cx="290" cy="120" r="20"/><circle cx="470" cy="170" r="24"/><circle cx="180" cy="290" r="20"/><circle cx="360" cy="260" r="22"/><circle cx="520" cy="300" r="18"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="80" y="90" width="470" height="240" rx="16"/></g>
""", ground=False)

add('scene', '映画の一場面が映るイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" fill="#41506a"/>
  <path d="M-170-110h340v220h-340z" class="bluep"/>
  <g transform="translate(-60 60) scale(0.6)">{person(0,0,1.0,1,'coral','gold','walk','bob','smile')}</g>
  {tree(90,50,0.6)}
  <g fill="#2f4055"><rect x="-170" y="-110" width="340" height="26"/><rect x="-170" y="84" width="340" height="26"/></g>
</g>
""", ground=False)

add('sceptical', '示された話を、ほんとかと疑うイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(300 220)">
  <path d="M-60-40h120v70h-120z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-16h72M-36 4h50"/></g>
</g>
{person(470,346,1.2,-1,'violet','blue','think','bob','flat')}
<g fill="{INK}" transform="translate(430 150)">
  <path d="M0 0q0-26 20-26t20 26q0 14-14 18v12h-10v-20q14-4 14-14t-8-8-8 12z"/><rect x="12" y="42" width="10" height="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('schedule', '時刻ごとの予定を書き込んだ表のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="{MUTED}">{''.join(f'<rect x="-160" y="{-100+i*45}" width="34" height="12"/>' for i in range(5))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-110 {-70+i*45}h270"/>' for i in range(5))}</g>
  <g class="tealp o"><rect x="-110" y="-104" width="180" height="34"/></g>
  <g class="coralp o"><rect x="-110" y="-14" width="240" height="34"/></g>
</g>
""", ground=True)

add('score', '得点の数字が上がるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-120h360v200h-360z" fill="#41506a"/>
  <g fill="#f3c94f"><rect x="-120" y="-70" width="34" height="100"/><rect x="-70" y="-70" width="34" height="100"/><rect x="30" y="-70" width="34" height="100"/><rect x="80" y="-70" width="34" height="100"/></g>
  <g fill="#f3c94f"><circle cx="-10" cy="-40" r="7"/><circle cx="-10" cy="0" r="7"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 320v-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('scratch', 'つめで表面を引っかいて傷をつけるイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-180-90h360v180h-360z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="5"><path d="M-100-40l120 100M-40-60l120 100M20-70l120 100"/></g>
</g>
{hand(200,140,1)}
<g class="a" marker-end="url(#ar)"><path d="M250 180l80 60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('screen', '映像を映す画面のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v260h-400z" fill="#41506a"/>
  <path d="M-170-110h340v200h-340z" class="bluep"/>
  <path d="M-140 60l90-100 60 60 70-80 90 120z" class="green o"/>
  <path d="M-30 120h60v40h-60z" fill="#41506a"/>
  <path d="M-90 160h180v16h-180z" class="ink"/>
</g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('sculpture', '台にのった彫刻のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-90-20h180v40h-180z" fill="#c9d3dc" class="o"/>
</g>
<g transform="translate(300 220)">
  <circle cy="-40" r="40" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-50 80q0-80 50-80t50 80z" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-50 20q-30 20-30 60" fill="none" stroke="#dbe3ea" stroke-width="18" stroke-linecap="round"/>
</g>
{person(120,346,0.7,1,'teal','blue','think','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('seal', '封筒に封をして、印を押すイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-140-90h280v180h-280z" class="paper"/>
  <path d="M-140-90l140 110 140-110" fill="none" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 40)"><circle r="34" class="coral o"/><g fill="#fffdf6"><rect x="-18" y="-6" width="36" height="12"/></g></g>
</g>
<g transform="translate(480 160)"><path d="M-40-30h80v40h-80z" class="ink"/><path d="M-16-80h32v50h-32z" class="ink"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('second', '順番の二番目を示したイラスト。', f"""
<g class="tealp o"><rect x="120" y="200" width="100" height="120"/><rect x="380" y="200" width="100" height="120"/></g>
<rect x="250" y="190" width="100" height="130" class="coral o"/>
<g fill="#fffdf6"><rect x="285" y="230" width="30" height="8"/><rect x="285" y="250" width="30" height="8"/></g>
<path d="M300 130v40" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('secondly', '手順の二番目を指し示すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-80h240M-100-20h240M-100 40h240M-100 100h200"/></g>
  <g class="tealp o"><circle cx="-140" cy="-80" r="20"/><circle cx="-140" cy="40" r="20"/><circle cx="-140" cy="100" r="20"/></g>
  <g class="coral o"><circle cx="-140" cy="-20" r="24"/></g>
  <g fill="#fffdf6"><rect x="-150" y="-32" width="20" height="7"/><rect x="-150" y="-16" width="20" height="7"/></g>
</g>
<path d="M500 200h-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('section', '全体をいくつかの区画に切り分けたイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-130h400v260h-400z" fill="none" stroke="{INK}" stroke-width="5"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-60-130v260M80-130v260"/></g>
  <g class="tealp o"><rect x="-60" y="-130" width="140" height="260"/></g>
</g>
<path d="M300 380v-30" class="a" marker-end="url(#ar)" transform="rotate(180 300 365)"/>
""", ground=False, arrow=True)

add('secular', '宗教から切り離された、世俗の場を示すイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-70 60V-40h140v100z" fill="#f4ead2" class="o"/>
  <path d="M-84-40l84-60 84 60z" class="tealp o"/>
  <g fill="{TONES['gold'][2]}"><rect x="-8" y="-140" width="16" height="46"/><rect x="-30" y="-124" width="60" height="14"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80 60V-60h160v120z" fill="#dfe6ea" class="o"/>
  <g fill="#cfe6f5" stroke="{INK}" stroke-width="2">{''.join(f'<rect x="{-60+c*50}" y="{-40+r*44}" width="40" height="32"/>' for r in range(2) for c in range(3))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M300 140v220"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('security', '錠と見張りで守りを固めるイラスト。', f"""
<g transform="translate(400 240)">
  <path d="M-100-120h200v240h-200z" class="goldd o"/>
  <g transform="translate(60 0)"><circle r="14" class="ink"/></g>
</g>
<g transform="translate(240 240)">
  <path d="M-50 0h100v80h-100z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-30 0v-30a30 30 0 0 1 60 0v30" fill="none" stroke="{INK}" stroke-width="10"/>
</g>
{person(120,346,0.9,1,'blue','blue','stand','cap','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('selective', 'たくさんの中から、えらんで少しだけ取るイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-120-90h240v180h-240z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o">{''.join(f'<circle cx="{-90+c*60}" cy="{-60+r*60}" r="22"/>' for r in range(3) for c in range(4))}</g>
</g>
<g transform="translate(460 250)">
  <g class="teal o"><circle cx="-30" cy="-20" r="22"/><circle cx="30" cy="20" r="22"/></g>
</g>
<path d="M340 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="170" cy="230" r="30"/><circle cx="230" cy="290" r="30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('senior', '年上で上位に立つ人を示したイラスト。', f"""
{person(200,346,1.3,1,'violet','blue','stand','short','smile')}
<g transform="translate(200 226)"><path d="M-16-16l6 14 16 2-12 11 3 16-13-8-13 8 3-16-12-11 16-2z" class="gold o"/></g>
{person(400,346,0.95,1,'teal','gold','stand','bob','smile')}
<g class="a" marker-end="url(#ar)"><path d="M200 150v-30"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M150 190h300"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sensible', 'よく考えて、無理のない道を選ぶイラスト。', f"""
{person(150,346,1.15,1,'teal','blue','think','short','smile')}
<path d="M230 250q100 0 140-50h130" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" marker-end="url(#ar)"/>
<path d="M230 290q100 0 140 60h130" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 140l18 18 30-36"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 330l28 28M498 330l-28 28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sentence', 'ひと続きの文が書かれたイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-120h380v240h-380z" class="paper"/>
  <g fill="{INK}"><rect x="-150" y="-40" width="60" height="14"/><rect x="-80" y="-40" width="90" height="14"/><rect x="20" y="-40" width="70" height="14"/><rect x="100" y="-40" width="40" height="14"/></g>
  <circle cx="150" cy="-20" r="7" class="ink"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="-160" y="-54" width="320" height="46"/></g>
</g>
""", ground=True)

add('serial', '同じ形が番号順に続くイラスト。', f"""
<g class="tealp o">{''.join(f'<rect x="{90+i*90}" y="200" width="70" height="90"/>' for i in range(5))}</g>
<g fill="{INK}">{''.join(f'<rect x="{110+i*90}" y="310" width="{10+i*8}" height="10"/>' for i in range(5))}</g>
<path d="M100 150h400" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
