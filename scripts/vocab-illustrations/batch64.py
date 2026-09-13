"""第64回: 気分・筋肉・近所・全般など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('monthly', '毎月おなじ日に印がつくイラスト。', f"""
<g transform="translate(180 220)">
  <path d="M-120-120h240v240h-240z" class="paper"/>
  <path d="M-120-120h240v46h-240z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-120+c*60}-74v194"/>' for c in range(1,4))}{''.join(f'<path d="M-120 {-14+r*60}h240"/>' for r in range(2))}</g>
  <circle cx="-30" cy="16" r="22" class="coral o"/>
</g>
<g transform="translate(420 220)" opacity=".55">
  <path d="M-120-120h240v240h-240z" class="paper"/>
  <path d="M-120-120h240v46h-240z" class="teal o"/>
  <circle cx="-30" cy="16" r="22" class="coral o"/>
</g>
<path d="M310 360h120" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('mood', 'そのときの気分が顔つきに出るイラスト。', f"""
{face(150,210,66,'smile')}
{face(300,210,66,'flat')}
{face(450,210,66,'sad')}
{cloud(300,90,0.8)}
<path d="M120 330h360" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('mostly', '大部分が同じ色で、少しだけ別の色があるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-120h400v240h-400z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="teal o">{''.join(f'<rect x="{-190+c*67}" y="{-110+r*78}" width="60" height="70"/>' for r in range(3) for c in range(6))}</g>
  <g class="coralp o"><rect x="134" y="46" width="60" height="70"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 380h250"/></g>
""", ground=False, arrow=True)

add('move', '家具を運んで引っ越すイラスト。', f"""
<g transform="translate(170 280)">
  <path d="M-90 50h80v-90h-80z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 50h120v-70H-10z" class="tealp o"/>
  <circle cx="-50" cy="60" r="24" class="ink"/><circle cx="60" cy="60" r="24" class="ink"/>
</g>
{person(330,340,0.95,1,'coral','blue','carry','cap','neutral')}
{box(330,260,80,60,0,'gold')}
<g transform="translate(490 290)">
  <path d="M-70 50h140V-20h-140z" fill="#f4ead2" class="o"/>
  <path d="M-90-20l90-60 90 60z" class="coral o"/>
</g>
<path d="M250 200h140" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('moving', '物語に心を動かされて涙するイラスト。', f"""
{face(220,200,88,'sad')}
{drop(272,240,0.8)}{drop(168,244,0.7)}
<g transform="translate(440 230)">
  <path d="M-90-70h180v140h-180z" class="violet o"/>
  <path d="M-70-50h140v100h-140z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-20h80M-40 10h60"/></g>
</g>
<path d="M330 220h-30" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('mud', '足あとの残るぬかるんだ泥のイラスト。', f"""
<g fill="#8b6f4e" stroke="{INK}" stroke-width="3"><path d="M60 300q120-40 240 0t240-20v80H60z"/></g>
<g fill="#6f5739"><ellipse cx="200" cy="320" rx="26" ry="14"/><ellipse cx="280" cy="336" rx="26" ry="14"/></g>
{person(400,300,1.0,1,'teal','blue','walk','short','flat')}
<g fill="#8b6f4e"><circle cx="470" cy="270" r="8"/><circle cx="500" cy="290" r="6"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('multiple', 'いくつもの部分が集まって一つになるイラスト。', f"""
<g transform="translate(300 230)">
  <g class="tealp o">{''.join(f'<circle cx="{int(120*__import__("math").cos(i*3.14159/3))}" cy="{int(120*__import__("math").sin(i*3.14159/3))}" r="40"/>' for i in range(6))}</g>
  <circle r="46" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M480 120h50"/></g>
""", ground=False, arrow=True)

add('muscle', '腕を曲げて力こぶを見せるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-120 60q-20-60 20-90t60 10" fill="none" stroke="{SKIN}" stroke-width="46" stroke-linecap="round"/>
  <path d="M-40-20q60-30 90 20t-10 70-90-10z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="3"><path d="M0-10q26 20 20 50"/></g>
  <path d="M50 70q40 20 60 0" fill="none" stroke="{SKIN}" stroke-width="40" stroke-linecap="round"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M330 150l24-18M340 190h28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('mutual', '互いに同じものを渡し合うイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','give','short','smile')}
{person(440,346,1.15,-1,'coral','gold','give','bob','smile')}
<g class="a" marker-end="url(#ar)"><path d="M240 200h120M360 260H240"/></g>
<g class="teal o"><circle cx="300" cy="200" r="16"/></g>
<g class="coral o"><circle cx="300" cy="260" r="16"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('mystery', '正体のわからない、謎の影のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#33445c"/>
<g fill="#4c5f7c"><path d="M300 340q-90-10-90-110 0-90 90-90t90 90q0 100-90 110z"/></g>
<g fill="#f3e3ae"><path d="M280 170q0-40 30-40t30 40q0 22-22 28v20h-16v-32q20-6 20-20t-12-12-14 18z"/><rect x="292" y="240" width="16" height="16"/></g>
<g fill="#fdf6e0"><circle cx="90" cy="90" r="4"/><circle cx="510" cy="120" r="4"/></g>
""", ground=False)

add('nail', 'かなづちで打ち込むくぎのイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160-20h320v70h-320z" class="goldd o"/>
  <path d="M-10-90h20v90h-20z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-30-100h60v14h-60z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(300 130) rotate(-16)">
  <path d="M-70-30h140v50h-140z" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 20h20v70h-20z" class="goldd o"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M380 260l24-18M170 260l-24-18"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('naked', '道具を使わず、裸の目で見ることを示したイラスト。', f"""
<g transform="translate(200 230)">
  <ellipse rx="70" ry="46" fill="#fffdf6" class="o"/>
  <circle r="22" class="ink"/>
  <circle cx="8" cy="-8" r="6" fill="#fffdf6"/>
</g>
<g transform="translate(430 230)" opacity=".45">
  <circle r="60" fill="none" stroke="{INK}" stroke-width="8"/>
  <path d="M42 42l40 40" fill="none" stroke="{INK}" stroke-width="12"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M400 120l60 60M460 120l-60 60"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M160 330l20 20 34-40"/></g>
""", ground=False)

add('narrative', '出来事を順に語る物語のイラスト。', f"""
<g transform="translate(300 220)">
  <g class="paper"><path d="M-200-90h120v90h-120z"/><path d="M-60-90h120v90h-120z"/><path d="M80-90h120v90H80z"/></g>
  <g class="tealp o"><circle cx="-140" cy="-46" r="24"/></g>
  <g class="coralp o"><rect x="-30" y="-70" width="60" height="50"/></g>
  <path d="M110-20l30-40 30 40z" class="goldp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-200 30h400M-200 66h400M-200 102h320"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 380h400"/></g>
""", ground=True, arrow=True)

add('nasty', 'いやなにおいのする、汚れたもののイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-70 60h140l-16-110h-108z" fill="#8b8161" stroke="{INK}" stroke-width="3"/>
  <g class="muted" opacity=".9"><path d="M-30-60q20-40 0-70M30-60q20-40 0-70"/></g>
  <g fill="#6f6a4a"><circle cx="-20" cy="20" r="10"/><circle cx="24" cy="34" r="8"/></g>
</g>
{person(140,346,1.05,1,'teal','blue','stand','short','sad')}
<g fill="none" stroke="{INK}" stroke-width="5"><path d="M120 200l30 10M180 200l-30 10"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('nation', '国旗のもと、ひとつの国としてまとまるイラスト。', f"""
<g transform="translate(300 140)">
  <path d="M-4-70h8v100h-8z" class="ink"/>
  <path d="M4-66h110v60H4z" class="tealp o"/>
</g>
<g transform="translate(300 300)">
  <path d="M-220-40h440v80h-440z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="green o"><path d="M-200-20q100-30 200 0t190-10v40h-390z"/></g>
</g>
{person(170,300,0.7,1,'coral','blue','stand','bob','smile')}
{person(430,300,0.7,1,'gold','blue','stand','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('nationwide', '国じゅうの各地に同じ印が広がるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-180 30q120-50 200 0t160-30" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <g class="coral o">{''.join(f'<circle cx="{-150+c*100}" cy="{-90+r*90}" r="18"/>' for r in range(3) for c in range(4))}</g>
</g>
""", ground=True)

add('native', '生まれた土地の言葉を自然に話すイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','stand','short','smile')}
<g transform="translate(380 180)">
  <path d="M-90-50h180v80h-180z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-60" y="-26" width="120" height="14"/><rect x="-60" y="0" width="80" height="14"/></g>
</g>
<g transform="translate(500 320)">
  <path d="M-50 40h100V-20h-100z" fill="#f4ead2" class="o"/>
  <path d="M-64-20l64-46 64 46z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 190l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('nearby', 'すぐ近くに建物があるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','stand','short','smile')}
<g transform="translate(400 290)">
  <path d="M-80 50h160V-30h-160z" fill="#f4ead2" class="o"/>
  <path d="M-100-30l100-70 100 70z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 260h60M300 260h-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('nearly', 'あと一歩で線に届きそうなイラスト。', f"""
{person(300,346,1.2,1,'coral','blue','walk','short','neutral')}
<g transform="translate(450 240)"><path d="M-6-110h12v220h-12z" class="ink"/></g>
<g class="a" marker-end="url(#ar)"><path d="M370 250h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M400 150v200"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('neat', '散らかった机が、きちんと整うイラスト。', f"""
<g transform="translate(160 260)">
  <path d="M-100-20h200v26h-200z" class="goldd o"/>
  <g class="tealp o" transform="rotate(20)"><rect x="-60" y="-60" width="60" height="30"/></g>
  <g class="coralp o" transform="rotate(-14)"><rect x="10" y="-56" width="60" height="26"/></g>
</g>
<g transform="translate(430 260)">
  <path d="M-100-20h200v26h-200z" class="goldd o"/>
  <g class="tealp o"><rect x="-70" y="-56" width="60" height="36"/></g>
  <g class="coralp o"><rect x="10" y="-56" width="60" height="36"/></g>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 350l20 20 34-40"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('neighbourhood', '家が寄り集まった近所のイラスト。', f"""
<g transform="translate(300 300)"><path d="M-250-10h500v14h-500z" fill="#e6dcc9"/></g>
<g transform="translate(150 270)">
  <path d="M-60 40h120V-20h-120z" fill="#f4ead2" class="o"/>
  <path d="M-74-20l74-50 74 50z" class="coral o"/>
</g>
<g transform="translate(300 270)">
  <path d="M-60 40h120V-20h-120z" fill="#f4ead2" class="o"/>
  <path d="M-74-20l74-50 74 50z" class="teal o"/>
</g>
<g transform="translate(450 270)">
  <path d="M-60 40h120V-20h-120z" fill="#f4ead2" class="o"/>
  <path d="M-74-20l74-50 74 50z" class="gold o"/>
</g>
{person(230,330,0.6,1,'coral','blue','walk','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('neighbouring', '境をはさんで隣り合う二つの土地のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-130h220v260h-220z" class="tealp o"/>
  <path d="M0-130h220v260H0z" class="goldp o"/>
  <path d="M0-130v260" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="16 12"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M200 380h60M400 380h-60"/></g>
""", ground=False, arrow=True)

add('nervousness', '出番の前に、緊張して汗をかくイラスト。', f"""
{person(220,346,1.25,1,'teal','blue','stand','short','flat')}
{drop(290,220,0.8)}{drop(160,230,0.7)}
<g class="muted"><path d="M300 300q30 20 0 40"/></g>
<g transform="translate(440 250)">
  <path d="M-70-60h140v120h-140z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-40" y="-30" width="80" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40 0h80M-40 24h60"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('net', '目の細かい網のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-120h400v240h-400z" fill="none" stroke="{INK}" stroke-width="5"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M{-200+i*40}-120v240"/>' for i in range(1,10))}
    {''.join(f'<path d="M-200 {-120+i*40}h400"/>' for i in range(1,6))}
  </g>
</g>
""", ground=False)

add('neutral', 'どちらにも寄らず、真ん中に立つイラスト。', f"""
<g transform="translate(150 240)"><path d="M-60-60h120v120h-120z" class="tealp o"/></g>
<g transform="translate(450 240)"><path d="M-60-60h120v120h-120z" class="coralp o"/></g>
{person(300,346,1.15,1,'gold','blue','stand','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 120v100"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 200h-40M330 200h40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('next', '列の中で、すぐ次に来るものを示したイラスト。', f"""
<g class="tealp o"><rect x="90" y="220" width="90" height="110"/><rect x="380" y="220" width="90" height="110"/><rect x="480" y="220" width="90" height="110"/></g>
<rect x="230" y="210" width="100" height="120" class="coral o"/>
<path d="M280 150v40" class="a" marker-end="url(#ar)"/>
<g class="a" marker-end="url(#ar)"><path d="M100 370h420"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('nor', 'どちらの箱にも入っていないイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-80-70h160v140h-160z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-40-30l80 60M40-30l-80 60"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-80-70h160v140h-160z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-40-30l80 60M40-30l-80 60"/></g>
</g>
<g transform="translate(300 120)"><circle r="24" class="teal o"/></g>
""", ground=False)

add('normally', 'いつもと同じ、正常な目盛りのイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-170 40a170 170 0 0 1 340 0z" fill="#f7fbfe" class="o"/>
  <path d="M-40-120h80v30h-80z" class="greenp o"/>
  <path d="M0 40V-100" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle cy="40" r="12" class="ink"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M460 200l20 20 34-40"/></g>
<path d="M60 320h480" class="a"/>
""", ground=True)

add('nowhere', 'どこを探しても見つからないイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-200-40h400M-200 50h400M-70-140v280M70-140v280"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
    <path d="M-160-100l60 60M-100-100l-60 60"/><path d="M-30-10l60 60M30-10l-60 60"/><path d="M110 70l60 60M170 70l-60 60"/>
  </g>
</g>
""", ground=True)

add('numerous', '数えきれないほど多くの点があるイラスト。', f"""
<g class="teal o">
  {''.join(f'<circle cx="{90+((i*53)%460)}" cy="{110+((i*97)%230)}" r="11"/>' for i in range(70))}
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 370h400"/></g>
""", ground=False, arrow=True)

add('obedient', '言われたとおりに素直に従うイラスト。', f"""
{person(150,346,1.15,1,'blue','blue','point','short','neutral')}
<g transform="translate(300 200)">
  <circle r="44" fill="#fffdf6" class="o"/>
  <path d="M-20 0h34M8-16l16 16-16 16" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
{person(460,346,1.15,1,'teal','gold','walk','bob','smile')}
<path d="M360 200h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 150l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('occasion', 'その日だけの特別な場を示したイラスト。', f"""
<g transform="translate(240 220)">
  <path d="M-160-130h320v260h-320z" class="paper"/>
  <path d="M-160-130h320v46h-320z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-160+c*80}-84v214"/>' for c in range(1,4))}{''.join(f'<path d="M-160 {-14+r*70}h320"/>' for r in range(2))}</g>
  <circle cx="40" cy="20" r="28" class="coral o"/>
</g>
<g transform="translate(480 250)">
  <path d="M-50 40h100V-10h-100z" class="coralp o"/>
  <path d="M-50-10h100v-16h-100z" class="coral o"/>
  <g class="gold o"><rect x="-6" y="-60" width="12" height="34"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('occasional', 'ときどきだけ印がつくイラスト。', f"""
<path d="M60 250h480" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g class="coral o"><circle cx="130" cy="250" r="18"/><circle cx="300" cy="250" r="18"/><circle cx="480" cy="250" r="18"/></g>
<g class="a" marker-end="url(#ar)"><path d="M130 330h170M300 330H130"/></g>
""", ground=False, arrow=True)

add('offensive', '前へ出て攻めかかるイラスト。', f"""
{person(190,346,1.25,1,'coral','blue','point','short','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)"><path d="M270 200h110M280 260h100"/></g>
{person(470,346,1.15,-1,'teal','gold','carry','bob','neutral')}
<g transform="translate(420 250)"><path d="M0-60q40 16 40 46 0 40-40 54-40-14-40-54 0-30 40-46z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('official', '公の印が押された正式な書面のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="{INK}"><rect x="-120" y="-110" width="140" height="18"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-120-60h240M-120-20h240M-120 20h180"/></g>
  <g transform="translate(70 80) rotate(-10)">
    <circle r="50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
    <g fill="{TONES['coral'][0]}"><rect x="-26" y="-8" width="52" height="16"/></g>
  </g>
</g>
""", ground=True)

add('ongoing', '作業がまだ途中で、続いているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200-30h400v60h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-200-30h230v60h-230z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M130 160h340"/></g>
<g transform="translate(300 340)">
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><path d="M-60 0h120"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('operational', '機械が実際に稼働しているイラスト。', f"""
<g transform="translate(320 240)">
  <path d="M-160-120h320v240h-320z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="12"><circle cx="-60" cy="-30" r="50"/><circle cx="50" cy="40" r="34"/></g>
  <g class="green o"><circle cx="110" cy="-80" r="16"/></g>
</g>
<g class="corals" style="stroke-width:5"><path d="M120 150q26-14 50 4M500 190q20 20 12 44"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 320l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('opposed', '案に向かって、はっきり反対するイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-70-60h140v120h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-30h92M-46 0h92"/></g>
</g>
{person(150,346,1.2,1,'coral','blue','up','short','flat')}
{person(450,346,1.2,-1,'teal','gold','up','bob','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M270 130l60 60M330 130l-60 60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('optical', 'レンズで光の道が曲がるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M0-110q60 110 0 220-60-110 0-220z" fill="#e7f6fb" opacity=".9" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5">
  <path d="M60 150h230M60 220h230M60 290h230"/>
  <path d="M310 150l160 60M310 220h160M310 290l160-60"/>
</g>
<g class="gold o"><circle cx="480" cy="220" r="14"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('organic', '化学肥料を使わず、土と堆肥で育てるイラスト。', f"""
<g fill="#8b6f4e"><path d="M60 320h480v40H60z"/></g>
<g transform="translate(230 300)">
  <path d="M0 20V-40" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <g class="green o"><ellipse cx="-24" cy="-40" rx="26" ry="14" transform="rotate(-20 -24 -40)"/><ellipse cx="24" cy="-56" rx="26" ry="14" transform="rotate(20 24 -56)"/></g>
</g>
<g transform="translate(400 300)">
  <path d="M0 20V-40" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <g class="green o"><ellipse cx="-24" cy="-40" rx="26" ry="14" transform="rotate(-20 -24 -40)"/><ellipse cx="24" cy="-56" rx="26" ry="14" transform="rotate(20 24 -56)"/></g>
</g>
<g transform="translate(130 260)">
  <path d="M-50-40h100l-10 90h-80z" fill="#e2eee2" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-30-70l60 60M30-70l-60 60"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('organizer', '進行表を手に、催しを取りしきる人のイラスト。', f"""
{person(160,346,1.25,1,'blue','blue','point','short','neutral')}
<g transform="translate(112 250) rotate(-10)">
  <path d="M-30-40h60v80h-60z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-18-20h36M-18 0h36M-18 20h24"/></g>
</g>
<g transform="translate(410 230)">
  <path d="M-120-100h240v200h-240z" fill="#fffdf6" class="o"/>
  <path d="M-90-70h180v60h-180z" class="coralp o"/>
  <g fill="{INK}"><rect x="-90" y="10" width="180" height="16"/></g>
</g>
<path d="M250 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ours', '私たちのものだと、囲って示すイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','point','short','smile')}
{person(320,346,1.15,1,'coral','gold','point','bob','smile')}
<g transform="translate(470 250)">{box(470,250,110,90,0,'gold')}</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="110" y="170" width="420" height="190" rx="18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('outer', '二重の輪の、外側の部分を示したイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="140" class="tealp o"/>
  <circle r="80" fill="#fffaf1" stroke="{INK}" stroke-width="4"/>
</g>
<path d="M520 100l-120 50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('outgoing', '自分から声をかけて、輪に入っていくイラスト。', f"""
{person(160,346,1.2,1,'coral','gold','up','bob','smile')}
{person(390,346,1.05,-1,'teal','blue','stand','short','smile')}
{person(490,346,1.05,-1,'gold','blue','stand','cap','smile')}
<g transform="translate(280 170)">
  <path d="M-60-40h120v56h-120z" fill="#fffdf6" class="o"/>
  <path d="M-20 16l-12 26 34-26z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-40" y="-16" width="80" height="12"/></g>
</g>
<path d="M240 280h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('outstanding', '並んだ中から一つだけ突き出ているイラスト。', f"""
<path d="M60 346h480" class="a"/>
<g class="tealp o">{''.join(f'<rect x="{90+i*70}" y="250" width="52" height="96"/>' for i in range(6))}</g>
<rect x="440" y="110" width="90" height="236" class="coral o"/>
<g class="golds" style="stroke-width:6"><path d="M420 90l-26-20M550 90l26-20"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M80 250h460"/></g>
""", ground=False)

add('overall', '部分ではなく、全体をひとまとめに見るイラスト。', f"""
<g transform="translate(300 230)">
  <g class="tealp o">{''.join(f'<rect x="{-190+c*100}" y="{-110+r*90}" width="80" height="70"/>' for r in range(3) for c in range(4))}</g>
  <path d="M-210-130h420v260h-420z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<path d="M520 90l-40 30" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
