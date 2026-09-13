"""第100回: 形容詞・名詞45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def star(x,y,r=30,cls='gold'):
    import math
    pts=[]
    for i in range(10):
        rr = r if i%2==0 else r*0.45
        a = math.radians(-90+i*36)
        pts.append(f'{x+rr*math.cos(a):.0f} {y+rr*math.sin(a):.0f}')
    return f'<path d="M{"L".join(pts)}z" class="{cls} o"/>'
def gear(x,y,r=60,cls='teal',teeth=8):
    t=''.join(f'<rect x="-12" y="{-r-22}" width="24" height="26" transform="rotate({i*360//teeth})"/>' for i in range(teeth))
    return (f'<g transform="translate({x} {y})"><g class="{cls} o">{t}</g>'
            f'<circle r="{r}" class="{cls} o"/><circle r="{r*0.35:.0f}" fill="#fffdf6" stroke="{INK}" stroke-width="3"/></g>')

add('efficient', '少ない元手で大きな結果を出すイラスト。', f"""
<g transform="translate(150 280)">
  <path d="M-40-40h80v80h-80z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 260h60"/></g>
<g transform="translate(430 250)">
  <path d="M-110-110h220v220h-220z" class="teal o"/>
</g>
{ck(200,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('element', '全体を組み立てるひとつの要素のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-210-140h420v280h-420z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"/>
  <g class="tealp o">{''.join(f'<rect x="{-200+c*70}" y="{-130+r*90}" width="60" height="80"/>' for r in range(3) for c in range(6))}</g>
  <rect x="-60" y="-40" width="60" height="80" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M520 350l-220-100"/></g>
""", ground=False, arrow=True)

add('eligible', '条件に達して入れる資格があるイラスト。', f"""
<g transform="translate(340 250)">
  <path d="M-20-160h40v300h-40z" class="ink"/>
  <path d="M-160-80h140v30h-140z" class="coral o"/>
</g>
{person(170,352,1.2,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M120 170h140"/></g>
{ck(470,200,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('employee', '社の名札をつけて働く従業員のイラスト。', f"""
{tower(460,320,0.7,'teal',5)}
{person(190,352,1.3,1,'violet','blue','stand','short','smile')}
<g transform="translate(250 260)">
  <path d="M-40-26h80v52h-80z" class="paper"/>
  <circle cx="-18" cy="-2" r="13" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M2-8h24M2 6h24"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('engine', 'ピストンが動く機関のイラスト。', f"""
<g transform="translate(290 250)">
  <path d="M-160-60h320v140h-320z" class="bluep o"/>
  <g fill="{MUTED}" class="o">{''.join(f'<rect x="{-130+i*80}" y="-130" width="56" height="70"/>' for i in range(3))}</g>
  <g fill="none" stroke="{INK}" stroke-width="5">{''.join(f'<path d="M{-102+i*80} -130v-24"/>' for i in range(3))}</g>
  <path d="M160-20h50v60h-50z" fill="{MUTED}" class="o"/>
</g>
{gear(480,330,40,'gold',8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('essay', '段落をそろえて書いた小論文のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <path d="M-90-110h180v24h-180z" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
    <path d="M-150-50h300M-150-20h300M-150 10h240"/>
    <path d="M-120 50h270M-150 80h300M-150 110h200"/>
  </g>
</g>
""", ground=False)

add('evolutionary', '長い時をかけて少しずつ変わるイラスト。', f"""
<g class="tealp o"><ellipse cx="120" cy="290" rx="34" ry="22"/></g>
<g class="tealp o"><ellipse cx="250" cy="285" rx="38" ry="24"/><circle cx="280" cy="266" r="14"/></g>
<g class="teal o"><ellipse cx="390" cy="278" rx="42" ry="26"/><circle cx="424" cy="254" r="17"/><path d="M368 302v22M404 304v20" fill="none" stroke="{TONES['teal'][2]}" stroke-width="7" stroke-linecap="round"/></g>
<g class="teal o"><ellipse cx="530" cy="270" rx="46" ry="28"/><circle cx="566" cy="242" r="20"/><path d="M506 296v26M546 298v24" fill="none" stroke="{TONES['teal'][2]}" stroke-width="8" stroke-linecap="round"/></g>
<g class="a" marker-end="url(#ar)"><path d="M60 370h480"/></g>
""", ground=False, arrow=True)

add('factor', 'いくつもの要因が結果を作るイラスト。', f"""
<g transform="translate(140 210)">
  <circle cy="-90" r="34" class="tealp o"/>
  <circle cy="0" r="34" class="coralp o"/>
  <circle cy="90" r="34" class="goldp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M190 120l120 90M190 210h120M190 300l120-90"/></g>
<g transform="translate(400 210)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('government', '旗を掲げた政府の庁舎のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-210 0h420v20h-420z" class="teald o"/>
  <path d="M-170-130h340v130h-340z" fill="#fffdf6" class="o"/>
  <g class="tealp o">{''.join(f'<rect x="{-150+i*60}" y="-120" width="40" height="120"/>' for i in range(5))}</g>
  <path d="M-200-130L0-210l200 80z" class="teal o"/>
  <path d="M-200-130h400v20h-400z" class="teald o"/>
</g>
<g transform="translate(300 110)">
  <path d="M-6 0v-90" class="a"/>
  <path d="M-6-90h90v56H-6z" class="coral o"/>
</g>
{person(140,356,0.75,1,'violet','blue','walk','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('importance', 'ほかより重んじられる大切さのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-70-120h140v220h-140z" class="coral o"/>
  <path d="M-230 20h100v80h-100zM130 20h100v80H130z" class="tealp o"/>
</g>
{star(300,110,34,'gold')}
<g fill="{TONES['coral'][0]}"><rect x="490" y="170" width="24" height="70" rx="12"/><circle cx="502" cy="266" r="14"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('inclined', 'かたむいた面に転がり寄るイラスト。', f"""
<path d="M60 340L500 160v180z" class="greenp o"/>
<path d="M60 340L500 160" fill="none" stroke="{INK}" stroke-width="4"/>
<circle cx="330" cy="228" r="34" class="teal o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M300 280l-90 40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M140 340a90 90 0 0 0 40-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('industrial', '煙突と歯車の並ぶ工業地帯のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-220 60v-120h440V60z" class="bluep o"/>
  <g fill="{MUTED}" class="o">{''.join(f'<rect x="{-190+i*130}" y="-190" width="50" height="130"/>' for i in range(3))}</g>
  <g class="tealp o">{''.join(f'<rect x="{-180+i*70}" y="-40" width="50" height="40"/>' for i in range(6))}</g>
</g>
{cloud(150,120,1,'blue')}
{cloud(300,90,0.9,'blue')}
{gear(470,160,44,'gold',8)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('industry', '材料が工場を通って製品になる産業のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-110-110h220v220h-220z" class="bluep o"/>
  <path d="M-60-60h120v100h-120z" class="ink"/>
  <path d="M-40 60h80v50h-80z" class="blued o"/>
</g>
<g class="goldp o"><path d="M90 250l50-20 16 44-50 16z"/></g>
<g class="gold o"><rect x="470" y="220" width="70" height="70" rx="10"/></g>
<g class="a" marker-end="url(#ar)"><path d="M180 250h40M420 250h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('influence', '波が船の進む向きを変えるイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(380 290)">
  <path d="M-90 0h180l-24 40h-132z" class="coral o"/>
  <path d="M-6-70h12v70H-6z" fill="{TONES['gold'][2]}"/>
  <path d="M6-70h70l-20 30 20 30H6z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="6">
  <path d="M60 300q40-24 80 0t80 0M60 340q40-24 80 0t80 0"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M240 270q80-40 150-90"/></g>
""", ground=False, arrow=True)

add('influential', 'ひとりの言葉が大勢を動かすイラスト。', f"""
{person(150,352,1.3,1,'violet','blue','point','bun','neutral')}
<g transform="translate(230 200)">
  <path d="M-60-40h120v70h-120zM-30 30l-12 26 34-26z" fill="#fffdf6" class="o"/>
</g>
{person(370,356,0.85,1,'teal','blue','up','short','smile')}
{person(450,356,0.85,1,'coral','gold','up','bob','smile')}
{person(530,356,0.85,1,'gold','violet','up','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M300 250h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('informative', '役に立つ知らせがつまった掲示のイラスト。', f"""
<g transform="translate(280 200)">
  <path d="M-170-140h340v260h-340z" class="paper"/>
  <circle cx="-110" cy="-60" r="40" class="teal o"/>
  <g fill="#fffdf6"><circle cx="-110" cy="-80" r="7"/><rect x="-117" y="-66" width="14" height="40" rx="7"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-40-90h170M-40-56h170M-40-22h130M-140 20h310M-140 54h250"/></g>
</g>
{person(510,352,1,-1,'teal','blue','stand','short','smile')}
{ck(430,320,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('ingredient', '料理に使う材料を並べたイラスト。', f"""
<g transform="translate(430 290)">
  <path d="M-90-30h180q0 70-90 70t-90-70z" fill="#fffdf6" class="o"/>
  <path d="M-100-40h200v14h-200z" class="teal o"/>
</g>
<g class="coralp o"><circle cx="140" cy="230" r="34"/></g>
<g class="greenp o"><ellipse cx="240" cy="250" rx="40" ry="22"/></g>
<g class="goldp o"><ellipse cx="160" cy="330" rx="30" ry="20"/></g>
<g class="violetp o"><circle cx="260" cy="340" r="26"/></g>
<g class="a" marker-end="url(#ar)"><path d="M310 250h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('institutional', 'そろった造りの大きな施設のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-230 60v-240h460V60z" fill="#fffdf6" class="o"/>
  <g class="tealp o">{''.join(f'<rect x="{-200+c*66}" y="{-160+r*60}" width="46" height="40"/>' for r in range(3) for c in range(7))}</g>
  <path d="M-230-180h460v24h-460z" class="teal o"/>
  <path d="M-40 60v-56h80v56z" class="teald o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('instruction', '手順を示した説明書のイラスト。', f"""
<g transform="translate(260 210)">
  <path d="M-160-150h320v300h-320z" class="paper"/>
  <g class="tealp o">{''.join(f'<circle cx="-120" cy="{-90+i*60}" r="20"/>' for i in range(4))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-84 {-90+i*60}h220"/>' for i in range(4))}</g>
</g>
{hand(510,260,-1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M446 260h-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('integral', 'それを抜くと成り立たない不可欠な部品のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-90-40h180v30h-180z" class="teal o"/>
  <path d="M-70-10h40v70h-40zM30-10h40v70H30z" class="tealp o"/>
  <path d="M-20-10h40v70h-40z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 250h50"/></g>
<g transform="translate(470 300)">
  <path d="M-90-20h180v20h-180z" class="teal o" transform="rotate(14)"/>
  <path d="M-70 10h40v30h-40z" class="tealp o" transform="rotate(-10 -50 25)"/>
  <path d="M30 14h40v26H30z" class="tealp o" transform="rotate(16 50 27)"/>
</g>
{xx(470,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('intellectual', '本を読み考えを深める知的なイラスト。', f"""
{sit(220,352,1.3,1,'violet','violet','short','neutral','lap')}
{chair(230,356,1.25,'gold',1)}
<g transform="translate(290 300)"><path d="M-46-16h92v34h-92z" class="paper"/></g>
<g transform="translate(430 180)">
  <circle r="66" class="bluep o"/>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="5"><circle r="28"/><path d="M0-66v-14M0 66v14M-66 0h-14M66 0h14M-48-48l-10-10M48 48l10 10M48-48l10-10M-48 48l-10 10"/></g>
</g>
<g class="o" fill="#e1edfb"><circle cx="330" cy="230" r="14"/><circle cx="310" cy="256" r="9"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('intriguing', '中身が気になって引き込まれるイラスト。', f"""
<g transform="translate(380 280)">
  <path d="M-100 0h200v90h-200z" class="goldd o"/>
  <path d="M-110-20h220v20h-220z" class="gold o"/>
  <path d="M-110-20l-14-50h248l-14 50z" class="goldp o" transform="rotate(-14 -110 -20)"/>
</g>
<g transform="translate(380 130)">
  <path d="M-26-26q0-28 28-28t28 26q0 22-28 28v12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="36" r="7" class="coral"/>
</g>
{person(150,352,1.15,1,'teal','blue','reach','short','surprised')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M230 250h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('irrelevant', '話の輪の外にあって関係がないイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 12"><circle cx="250" cy="220" r="150"/></g>
<g class="tealp o"><circle cx="200" cy="180" r="34"/><circle cx="300" cy="240" r="34"/><circle cx="210" cy="290" r="30"/></g>
<g class="coralp o"><circle cx="520" cy="300" r="40"/></g>
{xx(520,190,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('judicial', '法のつちとてんびんで表す司法のイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-8-80h16v190h-16z" class="ink"/>
  <path d="M-70 110h140v20H-70z" class="ink"/>
  <path d="M-110-76h220v12h-220z" class="ink"/>
  <path d="M-110-64v40M110-64v40" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-160-24h100q0 40-50 40t-50-40z" class="goldp o"/>
  <path d="M60-24h100q0 40-50 40t-50-40z" class="goldp o"/>
</g>
<g transform="translate(450 300) rotate(-24)">
  <path d="M-60-16h50v32h-50z" class="goldd o"/>
  <path d="M-10-9h110v18H-10z" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('launch', '新しいものを世に打ち出すイラスト。', f"""
<g transform="translate(220 220)">
  <path d="M-40 80V-40q0-60 40-100 40 40 40 100V80z" fill="#fffdf6" class="o"/>
  <circle cx="0" cy="-30" r="20" class="bluep o"/>
  <path d="M-40 40l-46 60h46zM40 40l46 60H40z" class="coral o"/>
</g>
{flame(220,330,0.85)}
<g fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"><path d="M400 340V120"/></g>
{star(500,140,28,'gold')}
""", ground=False, arrow=True)

add('legislative', '議場で法案を通す立法のイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-110-70h220v110h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-76-40h152M-76-10h110"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="8"><path d="M-60 16l12 14 26-30"/></g>
</g>
{sit(140,376,0.8,1,'violet','violet','short','neutral','up')}
{sit(260,376,0.8,1,'teal','blue','bob','neutral','up')}
{sit(380,376,0.8,-1,'coral','gold','short','neutral','up')}
{sit(500,376,0.8,-1,'green','blue','bun','neutral','up')}
<path d="M60 390h480" class="a"/>
""", ground=True)

add('legitimate', '正式な判を受けて認められるイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-160-150h320v300h-320z" class="paper"/>
  <path d="M-120-110h240v40h-240z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-120 {-30+i*44}h240"/>' for i in range(3))}</g>
  <circle cx="80" cy="100" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
  <path d="M54 100h52M80 74v52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
{ck(500,180,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('logical', '頭の中で筋道を立てて考えるイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(400 200)">
  <path d="M-160-110q-8-52 40-58 20-40 62-26 34-6 42 32 40 6 34 44-6 36-42 36h-100q-38-2-36-28z" class="bluep o"/>
  <g class="teal o"><rect x="-110" y="-70" width="50" height="40"/><rect x="-30" y="-70" width="50" height="40"/><rect x="50" y="-70" width="50" height="40"/></g>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="4" marker-end="url(#ar)"><path d="M-56-50h20M24-50h20"/></g>
</g>
<g class="o" fill="#e1edfb"><circle cx="250" cy="270" r="14"/><circle cx="228" cy="296" r="9"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('magical', '杖のひと振りで姿が変わる魔法のようなイラスト。', f"""
<g transform="translate(150 280)">
  <path d="M-40-40h80v80h-80z" fill="#dfe6ea" class="o"/>
</g>
<g transform="translate(300 200) rotate(30)">
  <path d="M-10-80h20v160h-20z" fill="{TONES['gold'][2]}"/>
  <circle cx="0" cy="-90" r="14" class="gold o"/>
</g>
<g transform="translate(460 260)">
  <circle r="60" class="violetp o"/>
  <circle r="26" class="violet o"/>
</g>
<g class="golds"><path d="M380 150l-20-20M460 150v-24M540 170l20-20"/></g>
{star(380,300,22,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('meaningful', '中に思いのこもった贈り物のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-110-60h220v140h-220z" class="teal o"/>
  <path d="M-110-60h220v26h-220zM-10-60v140" class="a"/>
  <path d="M0-60q-40-40-54-10 26 16 54 10zM0-60q40-40 54-10-26 16-54 10z" class="tealp o"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2.5">
  <path d="M300 170q-30-38 0-54 30-16 30 22 0-38 30-22 30 16 0 54l-30 30z"/>
</g>
{ck(500,300,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('mysterious', '霧の中に人影がぼんやり見える不思議なイラスト。', f"""
<path d="M0 0h600v400H0z" fill="#dfe6ea"/>
<g opacity="0.45">{person(300,352,1.4,1,'blue','blue','stand','short','neutral')}</g>
<g fill="#dfe6ea" opacity="0.8">
  <ellipse cx="180" cy="250" rx="150" ry="40"/><ellipse cx="420" cy="300" rx="160" ry="44"/>
  <ellipse cx="300" cy="180" rx="140" ry="36"/>
</g>
<g transform="translate(470 150)">
  <path d="M-26-26q0-28 28-28t28 26q0 22-28 28v12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="36" r="7" class="coral"/>
</g>
""", ground=False)

add('optimistic', '同じ半分を「まだある」と見る前向きなイラスト。', f"""
<g transform="translate(230 250)">
  <path d="M-70-120h140l-16 220h-108z" fill="#fffdf6" class="o"/>
  <path d="M-62-10h124l-10 110h-104z" class="bluep o"/>
</g>
{face(450,200,80,'smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M360 220h-40"/></g>
{ck(230,150,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('organizational', '会社の組み立てを示す組織図のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-50-150h100v50h-100z" class="teal o"/>
  <path d="M-180-50h100v50h-100zM-50-50h100v50h-100zM80-50h100v50H80z" class="tealp o"/>
  <path d="M-230 60h80v46h-80zM-130 60h80v46h-80zM-10 60h80v46h-80zM110 60h80v46h-80z" class="bluep o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
    <path d="M0-100v20M-130-80h260M-130-80v30M0-80v30M130-80v30"/>
    <path d="M-130 0v20M-190 20h120M-190 20v40M-70 20v40M130 0v20M70 20h120M70 20v40M190 20v40"/>
  </g>
</g>
""", ground=False)

add('overtime', '終業の時をすぎても働く残業のイラスト。', f"""
<g transform="translate(180 200)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <path d="M0 0v-60" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M0 0l50 30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
  <circle r="8" class="ink"/>
  <path d="M0-90A90 90 0 0 1 64 26L0 0z" class="coralp" opacity="0.6"/>
</g>
{sit(420,352,1.2,1,'violet','blue','short','sad','lap')}
{chair(430,356,1.15,'gold',1)}
<g transform="translate(490 300)"><path d="M-40-16h80v34h-40z" class="paper"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M280 200h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('parliamentary', '半円の議場に並ぶ議席のイラスト。', f"""
<g transform="translate(300 340)">
  <path d="M-260 0a260 100 0 0 1 520 0z" fill="#fffdf6" class="o"/>
  <path d="M-190 0a190 74 0 0 1 380 0z" class="goldd o"/>
  <path d="M-120 0a120 46 0 0 1 240 0z" class="gold o"/>
</g>
{person(300,240,0.9,1,'violet','violet','point','bun','neutral')}
{sit(170,330,0.6,1,'teal','blue','short','neutral','lap')}
{sit(430,330,0.6,-1,'coral','gold','bob','neutral','lap')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('personality', 'その人らしさが表れる性格のイラスト。', f"""
{person(300,352,1.3,1,'coral','blue','up','short','smile')}
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M150 180q-18-24 0-34 18-10 18 14 0-24 18-14 18 10 0 34l-18 18z"/>
</g>
{star(450,180,26,'gold')}
<g transform="translate(150 300)">
  <path d="M-30-24h60v48h-60z" class="tealp o"/>
</g>
<g transform="translate(460 300)">
  <circle r="26" class="violetp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="240" r="200"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('policy', '進む向きを定めた方針のイラスト。', f"""
<g transform="translate(230 220)">
  <path d="M-150-150h300v300h-300z" class="paper"/>
  <path d="M-110-110h220v40h-220z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-110 {-30+i*44}h220"/>' for i in range(3))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" marker-end="url(#ar)"><path d="M410 220h130"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('politics', '壇上で意見を競い合う政治のイラスト。', f"""
{person(160,352,1.15,1,'teal','blue','point','short','neutral')}
{person(440,352,1.15,-1,'coral','gold','point','bob','neutral')}
<g transform="translate(160 330)"><path d="M-50-30h100l14 50h-128z" class="goldd o"/></g>
<g transform="translate(440 330)"><path d="M-50-30h100l14 50h-128z" class="goldd o"/></g>
<g transform="translate(300 160)">
  <path d="M-6 0v-70" class="a"/>
  <path d="M-6-70h80v50H-6z" class="violet o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"><path d="M300 200v180"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('position', '盤の上の決まった位置を示すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M{-200+i*50} -140v280"/>' for i in range(1,8))}
    {''.join(f'<path d="M-200 {-140+i*47}h400"/>' for i in range(1,6))}
  </g>
  <circle cx="-50" cy="-46" r="24" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M250 174V80M250 174H100"/></g>
""", ground=False)

add('possibility', 'いくつもの起こりうる先があるイラスト。', f"""
{person(140,352,1.1,1,'teal','blue','stand','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)">
  <path d="M210 300q120-90 240-160M210 300h240M210 320q120 40 240 60"/>
</g>
<g opacity="0.5"><circle cx="500" cy="130" r="34" class="tealp o"/></g>
<g opacity="0.5"><path d="M470 270h60v60h-60z" class="coralp o"/></g>
<g opacity="0.5"><circle cx="500" cy="380" r="28" class="goldp o"/></g>
<g transform="translate(300 150)">
  <path d="M-22-24q0-24 22-24t22 22q0 18-22 24v10" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle cy="30" r="6" class="coral"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('potential', '小さな種に秘められた大きさのイラスト。', f"""
<g opacity="0.4">{tree(300,340,2)}</g>
<g transform="translate(300 330)">
  <ellipse rx="26" ry="20" class="goldd o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M300 300V140"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('presidential', '大統領の印をつけた演壇のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-110-60h220l24 90h-268z" class="goldd o"/>
  <circle cx="0" cy="-20" r="40" class="gold o"/>
  <path d="M0-44l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="goldp"/>
</g>
<g transform="translate(470 240)">
  <path d="M-6 110V-110" class="a"/>
  <path d="M-6-110h100v70H-6z" class="coral o"/>
</g>
{person(300,240,0.95,1,'violet','blue','point','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('pressure', '上から押しつけられる圧力のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-140-40h280v40h-280z" fill="#b9c2c9" class="o"/>
  <path d="M-100 0h200v60h-200z" class="tealp o" transform="scale(1 0.8)"/>
</g>
{box(300,170,220,80,0,'gold')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)">
  <path d="M180 90v40M300 70v50M420 90v40"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('prestigious', '名の通った格式ある印のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-90-120h180v160q0 80-90 110-90-30-90-110z" class="goldp o"/>
  <path d="M0-80l16 34 38 6-28 26 8 38-34-20-34 20 8-38-28-26 38-6z" class="gold o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"><path d="M-50 60h100"/></g>
</g>
{star(140,140,26,'gold')}
{star(470,140,26,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('process', '手を経て形が変わっていく工程のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-230-60h100v120h-100z" class="tealp o"/>
  <path d="M-60-60h120v120H-60z" class="tealp o"/>
  <path d="M130-60h100v120h-100z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 230h40M370 230h40"/></g>
<g class="goldp o"><circle cx="120" cy="230" r="22"/></g>
<g class="gold o"><rect x="490" y="200" width="60" height="60" rx="10"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W))
