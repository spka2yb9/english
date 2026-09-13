"""第53回: 2周目のB1/B2語。承認・調整・記念日など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('written', '手で書き記された文書のイラスト。', f"""
<g transform="translate(270 220)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="4">
    <path d="M-120-90q30-20 60 0t60 0t60 0"/><path d="M-120-40q30-20 60 0t60 0t60 0"/>
    <path d="M-120 10q30-20 60 0t60 0t60 0"/><path d="M-120 60q30-20 60 0t40 0"/>
  </g>
</g>
<g transform="translate(490 300) rotate(28)"><path d="M-10-90h20v120h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('yell', '遠くの相手に向かって大声でどなるイラスト。', f"""
{person(170,346,1.25,1,'coral','blue','up','short','flat')}
<g transform="translate(220 200)"><ellipse rx="20" ry="16" fill="#8b4a3e"/></g>
<g class="corals" opacity=".9" style="stroke-width:6"><path d="M270 160q30 40 30 70t-30 70M330 130q46 56 46 100t-46 100"/></g>
{person(510,346,0.85,-1,'teal','gold','stand','bob','surprised')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('yield', '道をゆずって、相手を先に通すイラスト。', f"""
<g transform="translate(150 160)">
  <path d="M0 60l-60-104h120z" fill="#fffdf6" stroke="{TONES['coral'][0]}" stroke-width="10"/>
</g>
<path d="M240 300h300" class="a" marker-end="url(#ar)"/>
<g transform="translate(300 250)">
  <path d="M-100 40h200v-40l-40-30h-120l-40 30z" class="tealp o"/>
  <circle cx="-50" cy="44" r="20" class="ink"/><circle cx="50" cy="44" r="20" class="ink"/>
</g>
<g transform="translate(180 250)" opacity=".5">
  <path d="M-60 20h120v-30h-120z" class="coralp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M120 300h60"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('zero', '中に何も入っていない、数がゼロのイラスト。', f"""
<g transform="translate(210 220)">
  <path d="M-120-110h240v220h-240z" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g transform="translate(450 220)">
  <ellipse rx="70" ry="100" fill="none" stroke="{TONES['coral'][0]}" stroke-width="22"/>
</g>
<g class="muted"><path d="M340 220h40"/></g>
""", ground=False)

add('absolute', '目盛りがいっぱいまで振り切れているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160 40a160 160 0 0 1 320 0z" fill="#f7fbfe" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M0 40l{int(-140*__import__("math").cos(i*3.14159/8))} {int(40-140*__import__("math").sin(i*3.14159/8))}" opacity=".5"/>' for i in range(9))}</g>
  <path d="M0 40L140 30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="40" r="12" class="ink"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M480 190l24-20M490 230h30"/></g>
<path d="M60 320h480" class="a"/>
""", ground=True)

add('abstract', '見たままの形から、線と色だけに抜き出すイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-90-100h180v200h-180z" fill="#fffdf6" class="o"/>
  {tree(0,70,0.75)}
</g>
<g transform="translate(430 240)">
  <path d="M-90-100h180v200h-180z" fill="#fffdf6" class="o"/>
  <path d="M-10 60h20v-60h-20z" class="goldd o"/>
  <path d="M0-70l60 70h-120z" class="green o"/>
</g>
<path d="M280 240h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('absurd', '四角い車輪の荷車という、ばかげたイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-140-60h280v70h-280z" class="goldd o"/>
  <path d="M-110 10h100v100h-100zM10 10h100v100H10z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="{INK}" transform="translate(470 130)">
  <path d="M0 0q0-32 24-32t24 32q0 18-20 22v16h-12v-26q18-4 18-18t-10-12-12 18z"/>
  <rect x="14" y="52" width="12" height="12"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M130 150l34 34M164 150l-34 34"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('acceptable', '許せる範囲の中に収まっているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-220-20h440v40h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-100-20h200v40h-200z" class="greenp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M-100-60v100M100-60v100"/></g>
  <circle cx="50" r="22" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M420 150l20 20 34-40"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('accessible', 'なだらかな坂で、だれでも入れる入口のイラスト。', f"""
<g transform="translate(400 260)">
  <path d="M-120 80h240v-160h-240z" fill="#f4ead2" class="o"/>
  <path d="M-40 80V0h80v80z" class="goldd o"/>
</g>
<path d="M120 340L280 260h60" fill="none" stroke="#c9d3dc" stroke-width="18" stroke-linejoin="round"/>
{person(180,320,0.9,1,'teal','blue','walk','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 180l20 20 34-40"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('accommodation', 'ベッドのある宿のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200 90h400v-160h-400z" fill="#f4ead2" class="o"/>
  <path d="M-220-70l220-70 220 70z" class="coral o"/>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="3"><rect x="-160" y="-30" width="80" height="60"/><rect x="80" y="-30" width="80" height="60"/></g>
  <g transform="translate(0 40)">
    <path d="M-70-10h140v30h-140z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
    <path d="M-70-10h40v-24h-40z" class="tealp o"/>
    <path d="M-70 20h10v30h-10zM60 20h10v30H60z" fill="#c9d3dc"/>
  </g>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('accompany', '並んで一緒に歩いていくイラスト。', f"""
{person(230,346,1.2,1,'teal','blue','walk','short','smile')}
{person(340,346,1.2,1,'coral','gold','walk','bob','smile')}
<path d="M430 250h90" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M230 180q55-30 110 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('accuse', '証拠の紙を突きつけて、相手を責めるイラスト。', f"""
{person(150,346,1.2,1,'blue','blue','point','short','flat')}
<g transform="translate(310 230)">
  <path d="M-70-60h140v120h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-30h92M-46 0h92"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-40 34h80"/></g>
</g>
{person(470,346,1.15,-1,'coral','gold','up','bob','sad')}
<path d="M390 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('acknowledge', 'たしかにそうだと、うなずいて認めるイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','stand','short','smile')}
<g transform="translate(430 220)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-50h140M-70-10h140M-70 30h100"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M270 200l20 20 34-40"/></g>
<path d="M270 280h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('acute', '症状の線が急に跳ね上がる、深刻なイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100h340" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-170 100q80-10 140-20t60-180" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M30-100q60 0 140 20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M300 90v-30"/></g>
""", ground=True)

add('ad', '通りに立つ広告の看板のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-180-140h360v220h-360z" fill="#fffdf6" class="o"/>
  <path d="M-150-110h300v100h-300z" class="coralp o"/>
  <circle cy="-60" r="34" class="coral o"/>
  <g fill="{INK}"><rect x="-120" y="10" width="240" height="22"/><rect x="-70" y="46" width="140" height="14"/></g>
  <path d="M-20 80h40v90h-40z" class="ink"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M500 130l26-20M510 170h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('adequate', '必要な線まで、ちょうど足りているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-90-130h180v260h-180z" fill="#f7fbfe" class="o"/>
  <path d="M-90-20h180v150h-180z" class="teal o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 8"><path d="M-130-20h260"/></g>
  <path d="M-90-130h180v260h-180z" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M450 200l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('adjacent', 'すぐ隣どうしで接している二つの区画のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-120h220v240h-220z" class="tealp o"/>
  <path d="M0-120h220v240H0z" class="goldp o"/>
  <path d="M0-120v240" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<path d="M300 380v-30" class="a" marker-end="url(#ar)" transform="rotate(180 300 365)"/>
""", ground=False, arrow=True)

add('adjust', 'つまみを回して、ちょうどよく合わせるイラスト。', f"""
<g transform="translate(200 250)">
  <circle r="80" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-60" fill="none" stroke="{INK}" stroke-width="10"/>
  <circle r="12" class="ink"/>
  <g fill="{MUTED}"><circle cx="-70" cy="-30" r="5"/><circle cx="0" cy="-76" r="5"/><circle cx="70" cy="-30" r="5"/></g>
</g>
<g transform="translate(440 250)">
  <path d="M-70-110h140v220h-140z" fill="#f7fbfe" class="o"/>
  <path d="M-70 10h140v100h-140z" class="teal o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"><path d="M-100 10h200"/></g>
</g>
<path d="M300 200a90 90 0 0 1 30-40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('advanced', '三段の目盛りが最上段までいっている上級のイラスト。', f"""
<g transform="translate(300 260)">
  <g class="tealp o"><rect x="-180" y="20" width="100" height="60"/></g>
  <g class="teal o"><rect x="-50" y="-40" width="100" height="120"/></g>
  <g class="teald o"><rect x="80" y="-120" width="100" height="200"/></g>
  <g transform="translate(130 -150)"><path d="M0-24l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="gold o"/></g>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('adverse', '向かい風に逆らって進みにくいイラスト。', f"""
<g transform="translate(300 346) rotate(-14)">{person(0,0,1.25,1,'teal','blue','walk','short','flat')}</g>
<g class="muted" opacity=".9"><path d="M540 180q-80-20-140 0M540 240q-80-20-140 0M540 300q-80-20-140 0"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M520 210h-90"/></g>
<path d="M180 210h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('aesthetic', '形の美しさを見て味わうイラスト。', f"""
<g transform="translate(360 240)">
  <path d="M-140-140h280v280h-280z" class="goldd o"/>
  <path d="M-110-110h220v220h-220z" fill="#fffdf6" class="o"/>
  <g transform="translate(0 30)">
    <path d="M-40 60q-30-60 0-90t80 0q30 30 0 90z" class="tealp o"/>
    <path d="M-16-30h32v-40h-32z" class="teal o"/>
    <g class="coral o"><circle cx="0" cy="-84" r="20"/></g>
  </g>
</g>
{person(130,346,0.95,1,'violet','blue','think','bob','smile')}
<g class="golds" style="stroke-width:5"><path d="M210 160l26-20M220 200h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('against', '壁を手で押して、逆らって力をかけるイラスト。', f"""
<g transform="translate(450 250)"><path d="M-40-160h80v320h-80z" fill="#c9d3dc" class="o"/></g>
{person(280,346,1.25,1,'coral','blue','point','short','flat')}
<path d="M360 220h40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)"/>
<path d="M400 280h-40" fill="none" stroke="{MUTED}" stroke-width="8" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('agent', '本人の代わりに、書類を扱って動く代理人のイラスト。', f"""
{person(140,346,1.0,1,'teal','gold','give','bob','smile')}
{person(300,346,1.2,1,'blue','blue','carry','short','neutral')}
<g transform="translate(300 250)">
  <path d="M-50-30h100v60h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-30-10h60M-30 10h40"/></g>
</g>
{person(490,346,1.0,-1,'coral','blue','reach','cap','neutral')}
<path d="M210 300h50M390 300h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('aggressive', '前へ強く出て、相手にせまるイラスト。', f"""
<g transform="translate(200 346) rotate(12)">{person(0,0,1.3,1,'coral','blue','point','short','flat')}</g>
{person(470,346,1.1,-1,'teal','gold','stand','bob','surprised')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)"><path d="M280 200h100M290 260h90"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('agreement', '握手をして、二人の署名がそろうイラスト。', f"""
{person(150,340,1.05,1,'blue','blue','reach','short','smile')}
{person(450,340,1.05,-1,'coral','gold','reach','bob','smile')}
<path d="M240 250h120" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
<g transform="translate(300 150)">
  <path d="M-90-60h180v100h-180z" class="paper"/>
  <path d="M-60 10q30-20 60 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
  <path d="M10 10q30-20 60 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
  <g fill="{INK}"><rect x="-60" y="-40" width="120" height="12"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('album', '写真を並べてとじたアルバムのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-190-140h380v280h-380z" class="violet o"/>
  <path d="M-170-120h340v240h-340z" fill="#fffdf6" class="o"/>
  <g class="tealp o"><rect x="-140" y="-90" width="130" height="90"/><rect x="10" y="-90" width="130" height="90"/><rect x="-140" y="20" width="130" height="90"/><rect x="10" y="20" width="130" height="90"/></g>
  <g fill="{TONES['teal'][2]}"><circle cx="-100" cy="-60" r="14"/><path d="M-40-10l-30-40-30 40z"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('alcohol', 'びんとグラスに入った酒のイラスト。', f"""
<g transform="translate(210 250)">
  <path d="M-50-60h100v160h-100z" fill="#5b7f5b" stroke="{INK}" stroke-width="3"/>
  <path d="M-18-60h36v-80h-36z" fill="#5b7f5b" stroke="{INK}" stroke-width="3"/>
  <path d="M-18-150h36v20h-36z" class="ink"/>
  <path d="M-40-30h80v50h-80z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(420 250)">
  <path d="M-50-60h100l-40 60v70h-20v-70z" fill="#f7fbfe" stroke="{INK}" stroke-width="3"/>
  <path d="M-34-40h68l-24 34h-20z" class="violetp o"/>
  <path d="M-40 90h80v14h-80z" fill="#f7fbfe" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('alike', 'ほとんど同じ形が二つ並ぶイラスト。', f"""
<g transform="translate(180 230)"><path d="M0-90l80 90-80 90-80-90z" class="teal o"/></g>
<g transform="translate(430 230)"><path d="M0-86l78 86-78 86-78-86z" class="teal o"/></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M280 210q20-14 40 0M280 250q20-14 40 0"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('allergic', '花粉にくしゃみが出て、赤くなるイラスト。', f"""
{face(230,200,88,'flat')}
<g class="coralp"><circle cx="180" cy="230" r="22"/><circle cx="280" cy="230" r="22"/></g>
<g transform="translate(230 250)"><ellipse rx="18" ry="14" fill="#8b4a3e"/></g>
{drop(300,250,0.7)}{drop(320,290,0.6)}
<g transform="translate(450 300)">
  <path d="M0 40v-60" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <g class="gold o"><circle r="24"/></g>
  <g class="goldp o"><circle cx="-30" cy="-24" r="18"/><circle cx="30" cy="-24" r="18"/><circle cx="0" cy="-46" r="18"/></g>
</g>
<g fill="{TONES['gold'][0]}" opacity=".8"><circle cx="380" cy="200" r="6"/><circle cx="350" cy="240" r="5"/><circle cx="400" cy="260" r="5"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('almost', 'あと少しで満杯になる、ほとんど届いた状態のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-220-40h440v80h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-220-40h390v80h-390z" class="teal o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="9 8"><path d="M220-70v140"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 150h50"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('already', '約束の時刻より前に、もう終わっているイラスト。', f"""
<g transform="translate(180 210)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <path d="M0 0v-56M0 0l40 26" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
<g transform="translate(430 220)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-40h140M-70 0h140M-70 40h100"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-30 0l24 24 46-56"/></g>
</g>
<path d="M290 210h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('ambition', 'はるか高い星を目ざして、はしごを上るイラスト。', f"""
<g transform="translate(470 120)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
<g transform="translate(260 280) rotate(-24)">
  <path d="M-40-160h16v320h-16zM24-160h16v320H24z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <g fill="#c9a06b" stroke="{INK}" stroke-width="2">{''.join(f'<rect x="-24" y="{-140+i*60}" width="48" height="12"/>' for i in range(5))}</g>
</g>
{person(160,346,0.95,1,'teal','blue','up','short','neutral')}
<path d="M330 240l90-70" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ambitious', '大きな塔の図面を広げて意気込むイラスト。', f"""
<g transform="translate(400 230)">
  <path d="M-140-140h280v280h-280z" fill="#e8f2fb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M-40 120h80v-220l-40-40-40 40z"/><path d="M-40 40h80M-40-20h80M-40-80h80"/></g>
</g>
{person(150,346,1.15,1,'coral','blue','up','bob','smile')}
<g class="golds" style="stroke-width:5"><path d="M230 190l26-20M240 230h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('among', '大勢の中にまじって一人いるイラスト。', f"""
{person(120,340,0.85,1,'teal','blue','stand','short','neutral')}
{person(210,340,0.85,1,'gold','blue','stand','bob','neutral')}
{person(300,340,0.95,1,'coral','gold','stand','cap','smile')}
{person(390,340,0.85,1,'teal','gold','stand','short','neutral')}
{person(480,340,0.85,1,'gold','blue','stand','bob','neutral')}
<circle cx="300" cy="300" r="80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M300 160v40" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('amusing', '見ておかしくて、笑ってしまうイラスト。', f"""
{face(200,200,90,'smile')}
<g fill="none" stroke="{INK}" stroke-width="5"><path d="M160 180q16-14 32 0M208 180q16-14 32 0"/></g>
<g class="golds" style="stroke-width:5"><path d="M300 150l26-20M310 190h30"/></g>
<g transform="translate(450 250)">
  <path d="M-90-70h180v140h-180z" fill="#fffdf6" class="o"/>
  <g class="coralp o"><circle cx="-30" cy="-20" r="24"/></g>
  <path d="M20 40l40-60 30 60z" class="tealp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('anniversary', '毎年めぐってくる記念の日を祝うイラスト。', f"""
<g transform="translate(190 210)">
  <path d="M-130-120h260v240h-260z" class="paper"/>
  <path d="M-130-120h260v50h-260z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-130+c*65}-70v190"/>' for c in range(1,4))}{''.join(f'<path d="M-130 {-10+r*65}h260"/>' for r in range(2))}</g>
  <circle cx="0" cy="30" r="28" class="coral o"/>
</g>
<g transform="translate(430 280)">
  <path d="M-90 60h180V-30h-180z" class="coralp o"/>
  <path d="M-90-30h180v-20h-180z" class="coral o"/>
  <g class="gold o"><rect x="-6" y="-90" width="12" height="40"/></g>
  {flame(430,180,0.6)}
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('announcement', '掲示板に知らせが貼り出されるイラスト。', f"""
<g transform="translate(360 220)">
  <path d="M-160-130h320v240h-320z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <path d="M-120-100h140v100h-140z" class="paper"/>
  <path d="M20-60h100v130H20z" class="paper"/>
  <g fill="{INK}"><rect x="-100" y="-80" width="100" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-50h100M-100-30h80M40-40h60M40-20h60M40 0h40"/></g>
</g>
{person(140,346,1.0,1,'teal','blue','stand','short','neutral')}
<path d="M200 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('anonymous', '名前の欄が空のままで、誰だかわからないイラスト。', f"""
<g transform="translate(400 220)">
  <path d="M-130-120h260v240h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-90-60h180M-90 0h180M-90 60h140"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="-100" y="-96" width="200" height="46"/></g>
</g>
<g transform="translate(160 250)">
  <circle cy="-60" r="46" fill="#7f8ea6"/>
  <path d="M-70 90q0-90 70-90t70 90z" fill="#7f8ea6"/>
  <g fill="#fffdf6"><path d="M-14-80q0-24 20-24t20 24q0 14-14 18v12h-12v-20q12-4 12-14t-8-8-8 12z"/><rect x="-2" y="-32" width="10" height="10"/></g>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('apparent', '遠くからでもはっきり見える大きな標示のイラスト。', f"""
<g transform="translate(370 210)">
  <path d="M-140-120h280v170h-280z" class="coral o"/>
  <g fill="#fffdf6"><rect x="-100" y="-80" width="200" height="30"/><rect x="-100" y="-20" width="140" height="24"/></g>
  <path d="M-14 50h28v120h-28z" class="ink"/>
</g>
{person(130,346,0.95,1,'teal','blue','point','short','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"><path d="M190 220h40"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M110 150l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('application', '申込書に記入して差し出すイラスト。', f"""
<g transform="translate(320 240)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <g fill="{INK}"><rect x="-100" y="-110" width="120" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-60h200M-100-20h200M-100 20h200M-100 60h160"/></g>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-100-66q30-20 60 0t50 0"/></g>
</g>
{hand(140,180,1)}
<path d="M240 350h100" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('appointment', '手帳の時刻に予約を書き入れるイラスト。', f"""
<g transform="translate(250 220)">
  <path d="M-150-130h300v260h-300z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-110 {-90+i*45}h220"/>' for i in range(5))}</g>
  <g fill="{MUTED}"><rect x="-140" y="-100" width="24" height="10"/><rect x="-140" y="-55" width="24" height="10"/><rect x="-140" y="-10" width="24" height="10"/></g>
  <path d="M-110-30h180v40h-180z" class="coralp o"/>
</g>
<g transform="translate(480 150)">
  <circle r="54" fill="#fffdf6" class="o"/>
  <path d="M0-34v34l26 14" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<path d="M420 210h-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
