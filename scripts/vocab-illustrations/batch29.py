"""第29回: 木材・投票・警告・能力など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('timber', '製材された木材が、積み重ねられているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(260 0)">
  {''.join(f'<g transform="translate({(i%2)*16-8} {330 - i*34})"><path d="M-110-16h220v32h-220z" class="goldp o"/><path d="M-110-16h220" class="a"/></g>' for i in range(6))}
</g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('trade', '二つの国が、船で品物をやりとりしているイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h130v150H0zM470 250h130v150H470z" class="ground"/>
<path d="M0 250h130M470 250h130" class="a"/>
{building(60,250,0.45,'teal')}{building(540,250,0.45,'gold')}
<g transform="translate(300 250)">
  <path d="M-110 0h220l-24 34h-172z" class="teal o"/>
  <g class="goldp o"><rect x="-70" y="-40" width="50" height="40"/><rect x="-10" y="-40" width="50" height="40"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 180h100"/><path d="M420 210H320"/></g>
""", ground=False, arrow=True)

add('trailer', '映画の予告編が、画面に短く映されているイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-130h380v260h-380z" fill="#2b3a4a" stroke="{INK}" stroke-width="3"/>
  <path d="M-160-100h320v200h-320z" fill="#1e2a36"/>
  <g fill="#f7e6a8"><path d="M-40-30l90 50-90 50z"/></g>
  <g fill="none" stroke="#4a5c6e" stroke-width="4"><path d="M-160 60h320"/></g>
</g>
<g class="golds" style="stroke-width:4"><path d="M120 120l-24-24M480 120l24-24"/></g>
""", ground=True)

add('translate', '日本語の文が、英語の文に置き換わるイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-50" width="46" height="10"/><rect x="-60" y="-20" width="60" height="10"/><rect x="-60" y="10" width="40" height="10"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M-60-46h120M-60-16h100M-60 14h80"/></g>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('transportation', 'バス・電車・車など、移動の手段を並べたイラスト。', f"""
<g transform="translate(150 220) scale(0.4)">
  <path d="M-200-60h400v100h-400z" class="goldp o"/>
  <g class="bluep o"><rect x="-170" y="-40" width="60" height="40"/><rect x="-90" y="-40" width="60" height="40"/><rect x="-10" y="-40" width="60" height="40"/></g>
  <circle cx="-120" cy="46" r="26" class="ink"/><circle cx="120" cy="46" r="26" class="ink"/>
</g>
<g transform="translate(430 220) scale(0.4)">
  <path d="M-200 40h430v-100q0-34-34-34h-396z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <g class="bluep o"><rect x="-170" y="-62" width="70" height="54"/><rect x="-80" y="-62" width="70" height="54"/><rect x="10" y="-62" width="70" height="54"/></g>
  <circle cx="-120" cy="52" r="26" class="ink"/><circle cx="120" cy="52" r="26" class="ink"/>
</g>
<g transform="translate(290 330) scale(0.4)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
""", ground=True)

add('treat', '傷口に薬を塗って、手当てしているイラスト。', f"""
{person(180,346,1.1,1,'teal','teal','point','cap','neutral')}
<g transform="translate(400 300)">
  <path d="M-100-20h200v20h-200z" class="tealp o"/>
  <path d="M-70-60h140v40h-140z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-20-58h44v36h-44z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(300 250)">
  <path d="M-30-40h60v50h-60z" class="coralp o"/>
  <path d="M-8-50h16v10h-16z" class="ink"/>
</g>
<path d="M300 280v30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('troop', '隊列を組んで行進する軍隊のイラスト。', f"""
{person(140,346,0.95,1,'green','green','walk','cap','neutral')}
{person(240,346,0.95,1,'green','green','walk','cap','neutral')}
{person(340,346,0.95,1,'green','green','walk','cap','neutral')}
{person(440,346,0.95,1,'green','green','walk','cap','neutral')}
<path d="M500 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('type', 'キーボードを打って、文字を入力しているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-180-40h360v60h-360z" fill="#dfe6ea" class="o"/>
  <g class="ink">{''.join(f'<rect x="{-160 + (i%10)*32}" y="{-30 + (i//10)*24}" width="24" height="18" rx="4"/>' for i in range(20))}</g>
</g>
<g transform="translate(300 170)">
  <path d="M-120-70h240v120h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-100-52h200v84h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-26h140M-70 0h100"/></g>
</g>
{hand(160,250,1)}
""", ground=True)

add('typical', '同じ形が並ぶ中で、いかにもその形らしい一つを示したイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{90+i*82}" y="200" width="62" height="80"/>' for i in range(6))}
</g>
<rect x="254" y="200" width="62" height="80" class="teal o"/>
<circle cx="285" cy="240" r="58" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
<path d="M60 300h480" class="a"/>
""", ground=False)

add('underground', '地面の下を通る鉄道のトンネルを示したイラスト。', f"""
<path d="M0 180h600v220H0z" fill="#e7d9c4"/>
<path d="M0 180h600" class="a"/>
{building(150,180,0.45,'teal')}{tree(430,180,0.5)}
<g transform="translate(300 300)">
  <path d="M-220-60h440v120h-440z" fill="#3d4c5c" stroke="{INK}" stroke-width="3"/>
  <g transform="scale(0.6)">
    <path d="M-250-60h430q34 0 34 34v100h-464z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
    <g class="bluep o"><rect x="-220" y="-30" width="70" height="54"/><rect x="-130" y="-30" width="70" height="54"/><rect x="-40" y="-30" width="70" height="54"/></g>
    <circle cx="-170" cy="90" r="20" class="ink"/><circle cx="90" cy="90" r="20" class="ink"/>
  </g>
</g>
""", ground=False)

add('unhappy', '口の端が下がって、うれしくない表情の顔のイラスト。', f"""
{face(280,200,120,'sad')}
<g class="muted"><path d="M440 150v40M480 170v40"/></g>
{drop(400,260,1.0)}
""", ground=False)

add('unusual', '同じ形の中に、まったく違う形が一つだけあるイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{90+i*82}" y="200" width="62" height="80"/>' for i in range(6) if i != 3)}
</g>
<g transform="translate(285 240)">
  <path d="M0-46l14 28 30 4-22 22 6 30-28-16-28 16 6-30-22-22 30-4z" class="coral o"/>
</g>
<path d="M60 300h480" class="a"/>
<circle cx="285" cy="240" r="58" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
""", ground=False)

add('update', '古い表示が、新しい内容に書き換わるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-90h180v180h-180z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-56-40h112M-56-10h90M-56 20h70"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-90-90h180v180h-180z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M-56-40h112M-56-10h112M-56 20h100"/></g>
  <g class="green o"><circle cx="60" cy="60" r="12"/></g>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('upstairs', '階段を上って、上の階へ向かうイラスト。', f"""
<g class="goldp o">
  <rect x="80" y="300" width="90" height="60"/><rect x="170" y="240" width="90" height="120"/>
  <rect x="260" y="180" width="90" height="180"/><rect x="350" y="120" width="90" height="240"/>
</g>
{person(400,120,0.7,1,'teal','blue','walk','short','neutral')}
<path d="M150 260L340 150" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('usual', 'いつも同じ場所に置かれている、決まったカップのイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-200-20h400v20h-400z" class="goldp o"/>
  <path d="M-60-20h120v-16h-120z" class="muted"/>
</g>
<g transform="translate(300 240)">
  <path d="M-50-50h100l-10 90h-80z" fill="#fffdf6" class="o"/>
  <path d="M-50-50h100" class="a"/>
  <path d="M50-34q34 0 34 22t-34 22" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><circle cx="300" cy="240" r="86"/></g>
""", ground=True)

add('vacuum', '空気を抜いて、中に何もない状態を示したイラスト。', f"""
<g transform="translate(300 230)">
  <circle r="130" fill="#f7fbfe" stroke="{INK}" stroke-width="4"/>
  <path d="M-90-90q60 40 180 20" fill="none" stroke="#ffffff" stroke-width="10" opacity=".9"/>
</g>
<g class="a" marker-end="url(#ar)">
  <path d="M120 130l-50-50"/><path d="M480 130l50-50"/><path d="M120 330l-50 50"/><path d="M480 330l50 50"/>
</g>
""", ground=False, arrow=True)

add('value', '天びんが品物と金額を釣り合わせているイラスト。', f"""
<path d="M300 340V140" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M250 356h100" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>
<path d="M150 150h300" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="300" cy="150" r="13" class="teal o"/>
<path d="M150 150v34M450 150v34" class="a"/>
{box(150,220,80,58,0,'gold')}
<g transform="translate(450 210)">
  <circle r="24" class="goldp o"/>
  <path d="M-7-10h14v20h-14z" class="goldd"/>
</g>
<path d="M120 132h360" class="muted"/>
""", ground=True)

add('vessel', '荷を積んだ船と、液体を入れる器を並べたイラスト。', f"""
<path d="M0 280h300v120H0z" class="bluep"/>
<path d="M0 280q40-14 80 0t80 0 80 0 60 0" class="a"/>
<g transform="translate(150 270)">
  <path d="M-90 0h180l-20 30h-140z" class="teal o"/>
  <path d="M-40 0v-40h60v40z" class="paper"/>
</g>
<g transform="translate(440 280)">
  <path d="M-70-80h140l-12 140h-116z" fill="#f4fbff" class="o"/>
  <path d="M-62-20h124l-8 80h-108z" class="bluep o"/>
  <path d="M-70-80h140" class="a"/>
</g>
<path d="M300 130v250" class="muted"/>
""", ground=False)

add('volunteer', '報酬なしで進んで手を挙げて、手伝う人のイラスト。', f"""
{person(180,346,1.15,1,'green','blue','up','bob','smile')}
<g transform="translate(420 280)">
  <path d="M-90-40h180v80h-180z" class="goldp o"/>
  <path d="M-90-40l-20-30h180l-20 30" fill="none" class="a"/>
</g>
<path d="M280 250h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M300 160l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('vote', '投票用紙を箱に入れているイラスト。', f"""
<g transform="translate(360 290)">
  <path d="M-110-60h220v120h-220z" class="tealp o"/>
  <path d="M-50-60h100v-14h-100z" class="ink"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-80 0h160M-80 30h160"/></g>
</g>
<g transform="translate(360 170) rotate(-8)">
  <path d="M-50-34h100v68h-100z" class="paper"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-24 0l14 14 26-30"/></g>
</g>
<path d="M360 210v30" class="a" marker-end="url(#ar)"/>
{hand(180,180,1)}
""", ground=True, arrow=True)

add('warm', '温度計が中ほどを示し、ほどよく暖かいイラスト。', f"""
{thermometer(430,300,0.55,1.0)}
{sun(140,110,44)}
<g transform="translate(250 280)">
  <path d="M-60-50h120l-10 90h-100z" fill="#fffdf6" class="o"/>
  <path d="M-52-20h104l-8 60h-88z" class="goldp o"/>
  <path d="M60-34q34 0 34 22t-34 22" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<g class="muted" opacity=".8"><path d="M230 190q-14-30 4-52M270 186q-14-34 6-56"/></g>
""", ground=True)

add('warn', '危険を示す標識で、注意をうながしているイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M0-120l120 200h-240z" class="goldp o"/>
  <path d="M-8-40h16v70h-16zM-8 44h16v18h-16z" class="ink"/>
</g>
<path d="M300 340v-40" class="a"/>
{person(140,346,0.9,1,'coral','blue','point','cap','neutral')}
<g class="corals" opacity=".85" style="stroke-width:4"><path d="M420 200q26 26 26 40M450 180q34 34 34 56"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('weak', '細い腕では重い物が持ち上がらないイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-120-14h240v28h-240z" class="ink"/>
  <circle cx="-150" cy="0" r="36" class="ink"/><circle cx="150" cy="0" r="36" class="ink"/>
</g>
{person(300,366,1.15,1,'teal','blue','stand','short','sad')}
<g class="a" marker-end="url(#ar)"><path d="M180 210v60"/><path d="M420 210v60"/></g>
<path d="M80 386h440" class="a" opacity=".3"/>
""", ground=True, arrow=True)

add('wild', '柵のない自然の中で、動物が自由に暮らすイラスト。', f"""
{tree(90,330,0.8)}{tree(520,330,0.7)}
<g transform="translate(300 300)">
  <ellipse cy="-20" rx="80" ry="44" class="goldp o"/>
  <path d="M-54 18v26M-16 22v22M20 22v22M54 14v30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
  <g transform="translate(84 -50)">
    <ellipse rx="30" ry="26" class="goldp o"/>
    <path d="M-16-22q-14-30 8-30 18 0 18 22z" class="goldd o"/>
    <path d="M18-24q18-28 34-10 12 14-6 28z" class="goldd o"/>
    <circle cx="8" cy="-4" r="3.4" class="ink"/>
  </g>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('wonder', '答えの分からないことを、頭に浮かべて考えるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(420 190)">
  <path d="M-110-50q-14-54 44-64 18-46 88-32 40 6 52 46 66-6 70 52 4 50-58 54h-160q-40-4-36-56z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}" transform="translate(0 10)">
    <path d="M-26-40q0-26 26-26t26 26q0 18-20 24v12h-12v-20q20-2 20-16 0-12-14-12t-14 12z"/>
    <circle cy="30" r="7"/>
  </g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="270" r="12"/><circle cx="264" cy="296" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('workforce', '職場で働く人が、まとまって並んでいるイラスト。', f"""
{building(300,180,0.5,'teal')}
{person(140,346,0.9,1,'gold','blue','stand','cap','neutral')}
{person(230,346,0.9,1,'gold','blue','stand','short','neutral')}
{person(320,346,0.9,1,'gold','blue','stand','bob','neutral')}
{person(410,346,0.9,1,'gold','blue','stand','cap','neutral')}
{person(500,346,0.9,1,'gold','blue','stand','short','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('working', '道具を使って、実際に作業を進めている人のイラスト。', f"""
{person(200,346,1.15,1,'gold','blue','point','cap','neutral')}
<g transform="translate(300 250) rotate(-14)">
  <path d="M-44-20h88v26h-88z" class="goldd o"/>
  <path d="M0 6v50" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(440 300)">
  <path d="M-80-40h160v80h-160z" class="goldp o"/>
  <path d="M-80 0h160" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('worm', '土の中を進む、細長い虫のイラスト。', f"""
<path d="M0 200h600v200H0z" fill="#e7d9c4"/>
<path d="M0 200h600" class="a"/>
<path d="M120 300q60-60 130 0t130 0 120-30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="26" stroke-linecap="round"/>
<path d="M120 300q60-60 130 0t130 0 120-30" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4" stroke-dasharray="14 16"/>
<circle cx="512" cy="272" r="4" class="ink"/>
<g fill="#c9a97c"><circle cx="180" cy="240" r="6"/><circle cx="420" cy="350" r="5"/></g>
""", ground=False)

add('worried', '眉を寄せて、心配そうな表情の顔のイラスト。', f"""
{face(280,200,120,'flat')}
<g fill="none" stroke="{INK}" stroke-width="5"><path d="M232 148q20-16 36-6M328 148q-20-16-36-6"/></g>
{cloud(460,120,1.2,'violet')}
<g class="muted"><path d="M460 160v26M492 168v22"/></g>
""", ground=False)

add('wrist', '手と腕のつなぎ目にある手首を示したイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-30-120h60v130h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30 10h60v40h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40 50q40-16 80 0 20 60 0 90-40 16-80 0-20-30 0-90z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="0" cy="30" r="42" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
</g>
<path d="M440 250q-60 10-100 10" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('ability', '重い物を軽々と持ち上げられる力を示したイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
<g transform="translate(280 220)">
  <path d="M-110-14h220v28h-220z" class="ink"/>
  <circle cx="-140" cy="0" r="34" class="ink"/><circle cx="140" cy="0" r="34" class="ink"/>
</g>
{person(280,366,1.25,1,'teal','blue','up','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M430 300l20 20 34-40"/></g>
""", ground=True)

add('abuse', '道具を本来と違う使い方で、乱暴に扱っているイラスト。', f"""
<g transform="translate(320 250) rotate(20)">
  <path d="M-100-16h200v32h-200z" class="goldd o"/>
  <path d="M100-24h34v48h-34z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
{hand(160,220,1)}
<g class="corals" style="stroke-width:6"><path d="M420 160l30 30M450 160l-30 30M470 300l-20-20"/></g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('accelerate', '車の速度が上がって、次第に速く走るイラスト。', f"""
<g transform="translate(160 280) scale(0.4)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g transform="translate(420 280) scale(0.55)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g class="muted"><path d="M240 250h60M230 290h80"/></g>
<path d="M120 180h380" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('accident', '車がぶつかって、事故になっている場面のイラスト。', f"""
<g transform="translate(190 290) scale(0.5)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g transform="translate(420 290) scale(-0.5 0.5)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="teal o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g transform="translate(305 260)">
  <path d="M-70 0l30-16-16-28 36 12 12-36 16 36 30-16-10 30 38 6-30 20 22 24-36-4-6 34-22-28-26 22 4-32z" class="goldp o"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('accommodate', '大きな部屋に、多くの人が収まっているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220-120h440v240h-440z" fill="#fffdf6" class="o"/>
  <path d="M-236-120h472l-40-50h-392z" class="teal o"/>
</g>
<g class="tealp o">
  {''.join(f'<g transform="translate({120+ (i%6)*72} {250 + (i//6)*60})"><circle cy="-20" r="15"/><path d="M-18 26q0-30 18-30t18 30z"/></g>' for i in range(12))}
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(' '.join(W)); print(sheet(W))
