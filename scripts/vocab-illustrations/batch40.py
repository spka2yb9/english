"""第40回: 穴・輸入・示す・受け継ぐなど40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('himself', '鏡に映る自分を、本人が見ているイラスト。', f"""
<g transform="translate(420 210)">
  <path d="M-100-150h200v300h-200z" class="goldd o"/>
  <path d="M-84-134h168v268h-168z" class="bluep o"/>
</g>
<g opacity=".7">{person(430,330,0.92,-1,'teal','blue','point','short','smile')}</g>
{person(170,346,1.1,1,'teal','blue','point','short','smile')}
<path d="M250 210h60" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('hint', '答えの一部だけをそっと示して、手がかりを与えるイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','point','short','smile')}
<g transform="translate(400 240)">
  <path d="M-100-80h200v160h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M-70-40h140M-70 0h140"/></g>
  <g fill="{INK}"><rect x="-70" y="36" width="50" height="10"/></g>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-dasharray="9 8"><path d="M250 240h50" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('his', '二つの持ち物のうち、片方が彼のものと示すイラスト。', f"""
{person(160,346,1.15,1,'blue','violet','point','short','smile')}
{box(360,300,110,80,0,'gold')}
{box(490,300,110,80,0,'teal')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M240 240h80" marker-end="url(#ar)"/></g>
<circle cx="360" cy="300" r="76" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('historic', '歴史に残る出来事を記した石碑のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-100 100V-60a100 90 0 0 1 200 0v160z" fill="#cfc7b8" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-60-30h120M-60 10h120M-60 50h90"/></g>
</g>
<path d="M120 380h360" class="a"/>
{tree(500,380,0.5)}
""", ground=True)

add('hockey', 'スティックでパックを打つ、ホッケーのイラスト。', f"""
<path d="M0 260h600v140H0z" fill="#e8f4fb"/>
<path d="M0 260h600" class="a"/>
<g transform="translate(220 290) rotate(-20)">
  <path d="M-10-130h20v130h-20z" class="goldd o"/>
  <path d="M-10 0h70v20h-70z" class="goldd o"/>
</g>
<ellipse cx="330" cy="320" rx="24" ry="10" class="ink"/>
<path d="M360 310q90-20 160 10" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('hole', '板に開いた丸い穴のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-180-120h360v240h-360z" class="goldp o"/>
  <circle r="70" fill="#3d4550" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M470 130q-40 40-60 60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('homesick', '遠くの家を思って、寂しくなっているイラスト。', f"""
{person(180,346,1.15,1,'violet','blue','think','bob','sad')}
{drop(220,250,0.9)}
<g transform="translate(420 200)">
  <path d="M-110-50q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 6)">{building(0,20,0.4,'teal')}</g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('honest', 'ありのままを話して、正直に伝えているイラスト。', f"""
<circle cx="300" cy="140" r="76" class="greenp"/>
<g transform="translate(300 176)"><path d="M-30 20l30-40 30 40z" class="green o"/><path d="M-30 20h60" class="a"/></g>
{person(200,346,1.2,1,'teal','blue','hold','short','smile')}
<circle cx="200" cy="266" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
{person(440,346,1.1,-1,'coral','gold','stand','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('honour', '功績をたたえて、賞を授けているイラスト。', f"""
{person(180,346,1.15,1,'blue','violet','give','short','neutral')}
{person(430,346,1.15,-1,'coral','gold','hold','bob','smile')}
<g transform="translate(300 250)">
  <circle r="30" class="gold o"/>
  <path d="M-18-30l-16-40h32l10 30zM18-30l16-40h-32l-10 30z" class="coral o"/>
  <circle r="14" class="goldp o"/>
</g>
<path d="M250 190h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('hope', '暗い場所の先に、明かりが見えているイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a4a"/>
<g transform="translate(460 200)">
  <circle r="60" fill="#fff8e6"/>
  <g fill="none" stroke="#f7e6a8" stroke-width="6" stroke-linecap="round">{''.join(f'<path d="M0 -80v-30" transform="rotate({i*45})"/>' for i in range(8))}</g>
</g>
<g transform="translate(180 350)">{person(0,0,1.1,1,'teal','blue','reach','short','smile')}</g>
<g fill="none" stroke="#f7e6a8" stroke-width="4"><path d="M260 260h120" marker-end="url(#ar)"/></g>
""", ground=False, arrow=True)

add('horrible', 'ひどい状態の料理に、顔をしかめるイラスト。', f"""
{person(180,346,1.2,1,'coral','blue','hold','short','sad')}
<g transform="translate(420 300)">
  <ellipse rx="80" ry="28" fill="#fffdf6" class="o"/>
  <g fill="#9aa88f" stroke="{INK}" stroke-width="2.5"><circle cx="-24" cy="-14" r="22"/><circle cx="16" cy="-8" r="22"/></g>
  <g class="muted"><path d="M-20-46q-14-30 4-52M22-42q-14-34 6-56"/></g>
</g>
<g class="corals" style="stroke-width:7"><path d="M280 200l30 30M310 200l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('house', '屋根と壁のある一軒の家のイラスト。', f"""
{building(300,320,1.3,'teal')}
{tree(500,340,0.6)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('huge', '人と比べて、けたはずれに大きな球のイラスト。', f"""
<circle cx="380" cy="230" r="150" class="tealp o"/>
{person(110,346,0.85,1,'coral','blue','up','short','surprised')}
<path d="M170 320h40" class="a" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('human', '人のからだの形を、単純に示したイラスト。', f"""
{person(300,346,1.5,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M180 130h240v240h-240z"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('hurt', 'ひざをぶつけて、痛みを感じているイラスト。', f"""
{person(280,346,1.25,1,'coral','blue','stand','short','sad')}
<g transform="translate(266 310)"><circle r="20" class="coralp o"/></g>
<g class="corals" style="stroke-width:5"><path d="M330 290l26-16M320 340l30 12M330 250l24-18"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('ideal', '思い描いた理想の形と、実際の形を比べたイラスト。', f"""
<g transform="translate(170 230)">
  <circle r="80" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
  <g class="golds" style="stroke-width:4"><path d="M0-100v-20M-80-80l-14-14M80-80l14-14"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-70-60q80-20 140 20-40 80-140 40 20-40 0-60z" class="tealp o"/>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('identify', '複数の中から、その一つだと見分けるイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{110+i*80}" cy="230" r="32"/>' for i in range(6))}
</g>
<circle cx="350" cy="230" r="32" class="coral o"/>
<g transform="translate(350 230)">
  <circle r="60" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M42 42l46 46" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
</g>
<path d="M60 330h480" class="muted"/>
""", ground=False)

add('illness', '熱を出して寝込んでいる、病気のイラスト。', f"""
<g transform="translate(260 300)">
  <path d="M-160-20h320v50h-320z" class="tealp o"/>
  <path d="M-170 30h340v20h-340z" class="goldd o"/>
  <ellipse cx="-100" cy="-40" rx="50" ry="26" fill="#fffdf6" class="o"/>
  <g transform="translate(-100 -60)">
    <circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-26-4q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
    <path d="M-10 2h6M6 2h6" class="a"/>
    <path d="M-8 16h16" class="a"/>
  </g>
</g>
{thermometer(470,280,0.9,1.0)}
<path d="M60 370h480" class="a"/>
""", ground=True)

add('illustrate', '説明に図を添えて、分かりやすく示すイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-140-100h130M-140-70h130M-140-40h110"/></g>
  <g class="tealp o"><rect x="20" y="-110" width="130" height="90"/></g>
  <path d="M40-40l40-50 30 34 30-40 20 56z" class="teal o" transform="translate(0 -30)"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-140 20h290M-140 50h250M-140 80h270"/></g>
</g>
""", ground=True)

add('immediate', '押した直後に、間を置かず反応するイラスト。', f"""
{hand(150,240,1)}
<g transform="translate(300 250)">
  <path d="M-60-50h120v100h-120z" fill="#dfe6ea" class="o"/>
  <circle r="28" class="coral o"/>
</g>
<g transform="translate(460 240)">
  <circle r="40" class="goldp o"/>
  <path d="M-16 40h32v14h-32z" class="ink"/>
</g>
<path d="M220 240h30M370 240h30" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:4"><path d="M300 150v-24"/></g>
""", ground=True, arrow=True)

add('implement', '計画表のとおりに、実際の設備を組み上げるイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3" stroke-dasharray="8 7"><path d="M-60-70h120v100h-120z"/><path d="M-60-20h120M0-70v100"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-90-90h180v180h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-60-60h120v60h-120z" class="bluep o"/>
  <g class="green o"><circle cx="-60" cy="50" r="12"/></g>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('import', '外国から船で品物が運び込まれるイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h130v150H0zM470 250h130v150H470z" class="ground"/>
<path d="M0 250h130M470 250h130" class="a"/>
{building(540,250,0.45,'teal')}
<g transform="translate(300 250)">
  <path d="M-110 0h220l-24 34h-172z" class="teal o"/>
  <g class="goldp o"><rect x="-70" y="-40" width="50" height="40"/><rect x="-10" y="-40" width="50" height="40"/></g>
</g>
<path d="M420 190H180" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('impose', '上から規則を押しつけて、従わせるイラスト。', f"""
{person(300,140,0.8,1,'blue','violet','point','cap','neutral')}
<g transform="translate(300 240)">
  <path d="M-90-30h180v60h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-8h120M-60 12h90"/></g>
</g>
<path d="M300 190v40" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
{person(300,366,1.05,1,'coral','blue','stand','short','sad')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('impress', '見事な出来に、相手が感心しているイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','short','smile')}
<g transform="translate(340 250)">
  <path d="M-80-70h160v140h-160z" class="paper"/>
  <path d="M-56 46l46-80 34 44 34-56 26 92z" class="tealp o"/>
</g>
{person(490,346,1.05,-1,'coral','gold','up','bob','surprised')}
<g class="golds" style="stroke-width:4"><path d="M440 200l24-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('imprison', '鉄格子の中に入れられて、閉じ込められるイラスト。', f"""
<g fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round">
  <path d="M170 130v240M240 130v240M310 130v240M380 130v240M450 130v240M150 150h320M150 350h320"/>
</g>
{person(310,340,0.85,1,'coral','blue','stand','short','sad')}
<g class="corals" style="stroke-width:7"><path d="M500 200l30 30M530 200l-30 30"/></g>
""", ground=True)

add('inconvenience', '道が工事でふさがれ、遠回りが必要になるイラスト。', f"""
<path d="M60 320h480" fill="none" stroke="#e6dcc9" stroke-width="46" stroke-linecap="round"/>
<g transform="translate(330 280)">
  <path d="M-70-40h140v40h-140z" class="goldp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"><path d="M-70-40l140 40M70-40l-140 40"/></g>
  <path d="M-50 0v40M50 0v40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9"/>
</g>
{person(140,320,0.85,1,'teal','blue','stand','short','sad')}
<path d="M200 240q80-60 150-30" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('incorporate', '別の部品を、本体の中に組み入れるイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-140-90h280v180h-280z" class="tealp o"/>
  <path d="M-40-30h80v60h-80z" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(300 130)"><path d="M-38-26h76v46h-76z" class="coral o"/></g>
<path d="M300 170v50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('incredible', '信じがたい高さの記録が出て、驚くイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o"><rect x="110" y="270" width="60" height="70"/><rect x="190" y="250" width="60" height="90"/><rect x="270" y="280" width="60" height="60"/></g>
<rect x="380" y="90" width="70" height="250" class="coral o"/>
{person(530,346,0.8,-1,'teal','blue','up','short','surprised')}
<g class="golds" style="stroke-width:5"><path d="M415 70V44M350 110l-24-24M480 110l24-24"/></g>
""", ground=True)

add('incur', '行動の結果として、損失を背負うイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','carry','short','sad')}
<g transform="translate(200 250)">
  <path d="M-60-36h120v72h-120z" class="coralp o"/>
  <g class="corals" style="stroke-width:6"><path d="M-24-12l48 24M24-12l-48 24"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80-60h160v120h-160z" class="paper"/>
  <path d="M-50 40l50-40 50 30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<path d="M300 210h60" class="a" marker-end="url(#ar)" transform="rotate(180 330 210)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('indeed', '示された事実に、確かにと大きくうなずくイラスト。', f"""
{person(220,346,1.2,1,'teal','blue','stand','short','smile')}
<g transform="translate(420 220)">
  <path d="M-80-60h160v120h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50-30h100M-50 0h80"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M280 200l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('independent', '支えなしで、自分だけで立っているイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','stand','short','smile')}
<g opacity=".35"><path d="M300 250v110" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round" stroke-dasharray="12 10"/></g>
<g class="corals" style="stroke-width:7"><path d="M340 240l30 30M370 240l-30 30"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M460 200l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('indicate', '指し棒で、図のある点を示しているイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','short','neutral')}
<path d="M230 240h120" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
<g transform="translate(440 230)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-60 60l50-70 40 40 40-50 30 80z" class="tealp o"/>
  <circle cx="-10" cy="-10" r="12" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('individual', '集団の中の一人を、丸で囲んで示したイラスト。', f"""
<g class="tealp o">
  {''.join(f'<g transform="translate({120+ (i%5)*80} {220 + (i//5)*90})"><circle cy="-22" r="17"/><path d="M-20 30q0-32 20-32t20 32z"/></g>' for i in range(10))}
</g>
<circle cx="280" cy="230" r="52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('indoor', '屋根と壁に囲まれた、室内の場面のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220-140h440v280h-440z" fill="#fffdf6" class="o"/>
  <path d="M-220-140h440v40h-440z" class="teal o"/>
  <g class="bluep o"><rect x="-180" y="-60" width="100" height="80"/></g>
  <g class="goldp o"><rect x="60" y="20" width="140" height="20"/></g>
</g>
{person(180,340,0.85,1,'coral','blue','stand','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('induce', 'ボタンを押すと、装置が動き出すきっかけになるイラスト。', f"""
{hand(150,240,1)}
<g transform="translate(290 250)">
  <path d="M-60-50h120v100h-120z" fill="#dfe6ea" class="o"/>
  <circle r="28" class="coral o"/>
</g>
<g transform="translate(460 250)">
  <circle r="50" fill="none" stroke="{INK}" stroke-width="7"/>
  <g class="tealp o"><path d="M0 0q42-26 52 14-30 22-52-14z"/><path d="M0 0q-26 42-58 12 20-30 58-12z"/><path d="M0 0q-14-46 30-46 6 34-30 46z"/></g>
</g>
<path d="M215 240h20M360 250h40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('indulge', '好きなだけ甘い物を食べて、ふけっているイラスト。', f"""
{person(200,346,1.2,1,'coral','blue','carry','bob','smile')}
<g transform="translate(400 300)">
  <ellipse rx="110" ry="34" fill="#fffdf6" class="o"/>
  <g class="coralp o"><circle cx="-50" cy="-24" r="26"/><circle cx="0" cy="-30" r="26"/><circle cx="50" cy="-24" r="26"/></g>
  <g class="goldp o"><circle cx="-24" cy="-54" r="22"/><circle cx="26" cy="-56" r="22"/></g>
</g>
<g class="golds" style="stroke-width:4"><path d="M300 200l24-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('infect', '一人から周りへ、病気が広がっていくイラスト。', f"""
{person(160,346,1.1,1,'coral','blue','stand','short','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 8">
  <path d="M230 240h90" marker-end="url(#ar)"/><path d="M230 290h180" marker-end="url(#ar)"/>
</g>
<g opacity=".85">{person(380,346,1.0,1,'teal','gold','stand','bob','sad')}{person(480,346,1.0,1,'violet','teal','stand','cap','sad')}</g>
<g class="coral o"><circle cx="270" cy="200" r="9"/><circle cx="330" cy="180" r="7"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('inflict', '一方が他方に、損害を負わせているイラスト。', f"""
{person(180,346,1.15,1,'blue','violet','point','cap','neutral')}
{person(440,346,1.1,-1,'coral','gold','hold','bob','sad')}
<path d="M270 240h80" class="a" marker-end="url(#ar)" style="stroke-width:7"/>
<g class="corals" style="stroke-width:7"><path d="M370 180l30 30M400 180l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('inherit', '親から子へ、持ち物が受け継がれるイラスト。', f"""
{person(170,346,1.15,1,'gold','violet','give','short','smile')}
{person(440,346,1.1,-1,'teal','blue','hold','bob','smile')}
<g transform="translate(300 250)">
  <path d="M-60-40h120v80h-120z" class="goldd o"/>
  <path d="M-60-14h120" fill="none" stroke="{TONES['gold'][1]}" stroke-width="5"/>
</g>
<path d="M250 190h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('inhibit', '柵が動きを妨げて、先に進めないイラスト。', f"""
<path d="M60 320h480" fill="none" stroke="#e6dcc9" stroke-width="46" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round">
  <path d="M320 190v170M380 190v170M290 240h120M290 300h120"/>
</g>
<path d="M120 260h130" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:8"><path d="M260 220l40 40M300 220l-40 40"/></g>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
