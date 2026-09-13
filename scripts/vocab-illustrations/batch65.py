"""第65回: 支払い・割合・港・準備など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('overwhelming', '押し寄せる量が多すぎて、抗しがたいイラスト。', f"""
<path d="M140 340q30-240 240-220 160 14 160 220z" class="blue o"/>
<path d="M200 340q26-180 200-166" fill="none" stroke="#fffdf6" stroke-width="10" opacity=".7"/>
{person(110,340,0.75,-1,'coral','gold','up','short','surprised')}
<g fill="none" stroke="{TONES['blue'][2]}" stroke-width="6" marker-end="url(#ar)"><path d="M300 120q-90 60-140 120"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pan', 'カメラを横へ振って景色を追うイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-70-40h140v80h-140z" fill="#41506a"/>
  <path d="M70-16l60-30v76l-60-30z" fill="#41506a"/>
  <path d="M-20 40h40v70h-40z" fill="#41506a"/>
  <path d="M-70 110h140v14h-140z" class="ink"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 140h240"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M180 120v40M420 120v40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('parental', '親が子の手を引いて見守るイラスト。', f"""
{person(230,346,1.35,1,'blue','blue','give','short','smile')}
{person(370,346,0.8,-1,'coral','gold','give','cap','smile')}
<path d="M300 270h20" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M230 170q70-40 140 20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('partial', '全体のうち一部だけ塗られているイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <path d="M0-130A130 130 0 0 1 113 65z" class="coral o"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M0 0v-130M0 0l113 65"/></g>
</g>
<path d="M500 130h-60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('passion', '大好きなものに、胸を熱くするイラスト。', f"""
{person(200,346,1.3,1,'coral','gold','carry','bob','smile')}
{flame(200,180,1.1)}
<g transform="translate(430 250)">
  <path d="M-70-60h140v130h-140z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-40" y="-30" width="80" height="18"/></g>
</g>
<g class="golds" style="stroke-width:5"><path d="M320 190l24-18M330 230h28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('passionate', '身を乗り出して熱っぽく語るイラスト。', f"""
<g transform="translate(200 346) rotate(12)">{person(0,0,1.3,1,'coral','blue','up','short','smile')}</g>
{flame(300,150,0.9)}
<g transform="translate(430 230)">
  <path d="M-80-50h160v80h-160z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-56" y="-26" width="112" height="14"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('passive', '自分から動かず、されるままのイラスト。', f"""
{person(180,346,1.2,1,'blue','blue','point','short','neutral')}
{person(430,346,1.2,-1,'teal','gold','stand','bob','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M260 230h100"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M500 230h50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 300l28 28M528 300l-28 28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('past', '過ぎ去った側を指し示すイラスト。', f"""
<path d="M60 240h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
<g class="tealp o"><circle cx="140" cy="240" r="22"/><circle cx="230" cy="240" r="22"/></g>
<g class="coral o"><circle cx="330" cy="240" r="28"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><circle cx="440" cy="240" r="22"/><circle cx="520" cy="240" r="22"/></g>
<path d="M270 330h-160" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('payment', 'お金を払って支払いを済ませるイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(300 250)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="16" class="goldd o"/>
</g>
{person(470,346,1.1,-1,'blue','blue','reach','bob','smile')}
<path d="M230 300h140" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M300 160l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('peculiar', 'ふつうの形の中に、そこだけ変わった形があるイラスト。', f"""
<g class="tealp o">{''.join(f'<rect x="{100+i*70}" y="200" width="52" height="80"/>' for i in range(6))}</g>
<g transform="translate(346 240)">
  <path d="M-30-46q40-20 60 10t-14 60-56 6 10-76z" class="coral o"/>
</g>
<g fill="{INK}" transform="translate(480 150)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 320h480" class="a"/>
""", ground=True)

add('per', '一つあたりいくら、と割り当てるイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-60-60h120v120h-120z" class="tealp o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="16" class="goldd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 240h80"/></g>
<g fill="none" stroke="{INK}" stroke-width="5"><path d="M290 320h40"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('percentage', '全体に対する割合を円で示したイラスト。', f"""
<g transform="translate(240 220)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <path d="M0-130A130 130 0 0 1 92 92z" class="teal o"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M0 0v-130M0 0l92 92"/></g>
</g>
<g transform="translate(470 220)">
  <g fill="{INK}"><circle cx="-16" cy="-24" r="12"/><circle cx="16" cy="24" r="12"/><path d="M-24 30l50-60" stroke="{INK}" stroke-width="6"/></g>
</g>
""", ground=False)

add('performance', '舞台での演奏や演技を披露するイラスト。', f"""
<g transform="translate(300 140)">
  <path d="M-200-60h400v40h-400z" class="coral o"/>
  <path d="M-200-20h60q10 100 0 160h-60z" class="coralp o"/>
  <path d="M140-20h60v160h-60q-10-60 0-160z" class="coralp o"/>
</g>
<g transform="translate(300 250) scale(0.95)">{person(0,60,1.0,1,'violet','blue','up','bob','smile')}</g>
<g fill="{INK}"><ellipse cx="420" cy="180" rx="14" ry="10" transform="rotate(-18 420 180)"/><rect x="430" y="144" width="5" height="34"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('perhaps', 'どちらとも言えず、たぶんと迷うイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(420 200)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g class="tealp o"><rect x="-70" y="-30" width="60" height="60"/></g>
  <g class="coralp o"><circle cx="40" r="30"/></g>
  <g fill="{INK}"><path d="M96-16q0-22 18-22t18 22q0 12-14 16v10h-10v-18q12-4 12-12t-7-7-7 11z"/><rect x="105" y="24" width="10" height="10"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="300" r="12"/><circle cx="266" cy="324" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('permanent', '時が過ぎても変わらず残るイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-70-90h140v180h-140z" class="teal o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-70-90h140v180h-140z" class="teal o"/>
</g>
<path d="M280 250h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(300 130)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M0-22v22l16 10" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 370l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('persistent', '何度たたかれても立ち続けるイラスト。', f"""
<g opacity=".3" transform="rotate(-40 160 340)">{person(160,340,1.0,1,'teal','blue','stand','short','neutral')}</g>
<g opacity=".6" transform="rotate(-20 320 340)">{person(320,340,1.0,1,'teal','blue','stand','short','neutral')}</g>
{person(470,340,1.05,1,'teal','blue','stand','short','flat')}
<g class="a" marker-end="url(#ar)"><path d="M180 180q140-40 280 0"/></g>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('persuasive', '筋の通った説明で、相手をうなずかせるイラスト。', f"""
{person(150,346,1.15,1,'blue','blue','point','short','neutral')}
<g transform="translate(330 200)">
  <path d="M-90-60h180v90h-180z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M-60-30h60M-60-6h60M-60 18h40"/></g>
</g>
{person(490,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M440 300l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pessimistic', '先ゆきを暗く見て、うつむくイラスト。', f"""
{person(180,346,1.2,1,'blue','blue','stand','short','sad')}
<g transform="translate(430 230)">
  <path d="M-120-100h240v200h-240z" fill="#f7fbfe" class="o"/>
  <path d="M-90 60q60-20 100-60" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
  <path d="M10 0q50 40 80 60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="12 9" marker-end="url(#ar)"/>
</g>
{cloud(180,150,0.9)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('philosophical', '腕を組んで、物事の根本を考えるイラスト。', f"""
{person(180,346,1.2,1,'violet','blue','think','short','neutral')}
<g transform="translate(430 200)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><path d="M-30-30q0-40 30-40t30 40q0 22-20 28v16h-20v-30q20-6 20-16t-10-10-10 12z"/><rect x="-10" y="30" width="16" height="16"/></g>
  <g class="muted"><path d="M60-30h50"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="300" r="12"/><circle cx="266" cy="324" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('photography', 'カメラで写真を撮る技のイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-140-80h280v160h-280z" fill="#41506a"/>
  <circle r="56" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <circle r="28" fill="#e8f4fb"/>
  <path d="M-100-80h70v-26h-70z" fill="#41506a"/>
  <g class="coral o"><circle cx="100" cy="-50" r="12"/></g>
</g>
<g transform="translate(470 200) rotate(-8)">
  <path d="M-60-50h120v100h-120z" fill="#fffdf6" class="o"/>
  <path d="M-46 34l40-50 26 26 24-34 26 58z" class="green o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('pipe', '曲がった管がつながるイラスト。', f"""
<g fill="none" stroke="#8b98a6" stroke-width="34" stroke-linecap="round">
  <path d="M80 300h140q40 0 40-40v-80q0-40 40-40h180"/>
</g>
<g fill="none" stroke="#c9d3dc" stroke-width="10"><path d="M80 300h140q40 0 40-40v-80q0-40 40-40h180"/></g>
<g fill="#7f8ea6" stroke="{INK}" stroke-width="2"><rect x="230" y="230" width="60" height="26"/><rect x="330" y="122" width="26" height="60" transform="rotate(90 343 152)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('pity', 'うずくまる人に、そっと心を寄せるイラスト。', f"""
<g transform="translate(430 346) rotate(20)">{person(0,0,1.05,-1,'coral','gold','stand','bob','sad')}</g>
{person(200,346,1.2,1,'teal','blue','reach','short','sad')}
<g transform="translate(310 190)">
  <path d="M0 40c-40-30-56-46-56-68a30 30 0 0 1 56-16 30 30 0 0 1 56 16c0 22-16 38-56 68z" class="coralp o"/>
</g>
<path d="M280 280h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('planning', '手順を書き出して段取りを組むイラスト。', f"""
<g transform="translate(330 220)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-80 {-90+i*45}h200"/>' for i in range(5))}</g>
  <g class="tealp o">{''.join(f'<circle cx="-110" cy="{-96+i*45}" r="14"/>' for i in range(5))}</g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M-110-70v30M-110-25v30"/></g>
</g>
{person(130,346,0.95,1,'blue','blue','think','short','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pleasure', '好きなことをして、心地よく喜ぶイラスト。', f"""
{person(220,346,1.3,1,'coral','gold','stand','bob','smile')}
<g transform="translate(420 250)">
  <path d="M-60-40h120l-14 100h-92z" fill="#f7fbfe" class="o"/>
  <path d="M-50 0h100l-10 50h-80z" class="coralp o"/>
  <g class="muted"><path d="M-20-60q20-30 0-50M20-60q20-30 0-50"/></g>
</g>
<g class="golds" style="stroke-width:5"><path d="M320 180l-24-18M330 220h-28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('plenty', '器からあふれるほど、たくさんあるイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-140-40h280l-20 120h-240z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g class="coral o"><circle cx="-80" cy="-50" r="30"/><circle cx="-20" cy="-70" r="30"/><circle cx="40" cy="-50" r="30"/><circle cx="100" cy="-64" r="30"/></g>
  <g class="green o"><circle cx="-50" cy="-100" r="26"/><circle cx="30" cy="-108" r="26"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 190l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('plus', '二つを合わせて足すイラスト。', f"""
<g transform="translate(150 230)"><circle r="60" class="teal o"/></g>
<g fill="{INK}" transform="translate(300 230)"><rect x="-40" y="-10" width="80" height="20"/><rect x="-10" y="-40" width="20" height="80"/></g>
<g transform="translate(450 230)"><circle r="60" class="coral o"/></g>
<path d="M120 350h360" class="a"/>
""", ground=False)

add('poem', '短い行を並べて書かれた詩のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-110" width="120" height="16"/></g>
  <g fill="{MUTED}">
    <rect x="-110" y="-60" width="140" height="12"/><rect x="-110" y="-24" width="180" height="12"/>
    <rect x="-110" y="12" width="110" height="12"/><rect x="-110" y="48" width="160" height="12"/>
  </g>
</g>
""", ground=True)

add('poet', '詩を書きつける詩人のイラスト。', f"""
{person(180,346,1.15,1,'violet','blue','reach','bob','smile')}
<g transform="translate(400 240)">
  <path d="M-110-120h220v240h-220z" class="paper"/>
  <g fill="{MUTED}"><rect x="-70" y="-80" width="100" height="12"/><rect x="-70" y="-44" width="130" height="12"/><rect x="-70" y="-8" width="80" height="12"/></g>
</g>
<g transform="translate(280 280) rotate(28)"><path d="M-8-70h16v90h-16z" class="coral o"/><path d="M-8 20h16l-8 20z" class="ink"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('poetry', '詩の本と、そこから広がるイメージのイラスト。', f"""
<g transform="translate(220 240)">
  <path d="M-120-100h240v200h-240z" class="violet o"/>
  <path d="M-100-80h200v160h-200z" fill="#fffdf6" class="o"/>
  <g fill="{MUTED}"><rect x="-70" y="-50" width="90" height="10"/><rect x="-70" y="-20" width="120" height="10"/><rect x="-70" y="10" width="70" height="10"/></g>
</g>
<g transform="translate(450 200)">
  <path d="M-90-60q40-40 90 0t80-10" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"/>
  <g class="coralp o"><circle cx="-40" cy="20" r="24"/><circle cx="40" cy="0" r="20"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('politeness', '礼をつくして、ていねいにふるまうイラスト。', f"""
<g transform="translate(230 346) rotate(24)">{person(0,0,1.25,1,'blue','blue','stand','short','smile')}</g>
{person(470,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M110 180l20 20 34-40"/></g>
<path d="M320 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('politician', '演壇に立って支持を訴える政治家のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-90-30h180v40h-180z" class="goldd o"/>
  <path d="M-70 10h140v60h-140z" class="goldp o"/>
</g>
<g transform="translate(300 190) scale(0.95)">{person(0,60,1.0,1,'blue','blue','up','short','neutral')}</g>
<g transform="translate(300 120)">
  <path d="M-70-40h140v50h-140z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-50" y="-24" width="100" height="14"/></g>
</g>
{person(120,346,0.6,1,'teal','gold','up','bob','smile')}
{person(480,346,0.6,-1,'coral','blue','up','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('pollution', '煙と汚れで空気と水がよごれるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#c9c6b8"/>
<g transform="translate(180 250)">
  <path d="M-90 90h180v-140h-180z" fill="#8b8161" stroke="{INK}" stroke-width="3"/>
  <path d="M-60-90h40v40h-40zM20-90h40v40H20z" fill="#6f6a4a"/>
  <g fill="#9b9683" opacity=".9"><ellipse cx="-40" cy="-130" rx="40" ry="26"/><ellipse cx="40" cy="-150" rx="46" ry="30"/></g>
</g>
<path d="M0 330h600v70H0z" fill="#7d8a6a"/>
<g fill="#6f6a4a"><circle cx="380" cy="350" r="12"/><circle cx="440" cy="366" r="9"/></g>
""", ground=False)

add('port', '船が着く港のイラスト。', f"""
<path d="M0 280h600v120H0z" class="bluep"/>
<g transform="translate(180 300)">
  <path d="M-160 20h320l-40 40h-240z" fill="#dfe6ea" class="o"/>
</g>
<g transform="translate(380 250)">
  <path d="M-110 40h220l-30 40h-160z" class="tealp o"/>
  <path d="M-60-10h140v50h-140z" fill="#fffdf6" class="o"/>
  <path d="M-6-90h12v80h-12z" class="ink"/>
</g>
<g transform="translate(120 230)">
  <path d="M-6-90h12v130h-12z" class="ink"/>
  <path d="M-6-90h80v10h-80z" class="ink"/>
  <path d="M60-80v30" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
""", ground=False)

add('powder', 'さらさらした粉が山になるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-120 40q30-100 120-100t120 100z" fill="#fffdf6" stroke="{MUTED}" stroke-width="3"/>
</g>
<g transform="translate(200 140) rotate(30)">
  <path d="M-50-40h100v70h-100z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="#fffdf6" stroke="{MUTED}" stroke-width="2"><circle cx="270" cy="210" r="6"/><circle cx="300" cy="180" r="5"/><circle cx="240" cy="180" r="4"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('power', '大きな力で重い物を動かすイラスト。', f"""
<g transform="translate(400 260)">
  <path d="M-90-60h180v120h-180z" fill="#8b98a6" stroke="{INK}" stroke-width="4"/>
</g>
{person(180,340,1.25,1,'coral','blue','reach','short','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" marker-end="url(#ar)"><path d="M250 250h60"/></g>
<g class="corals" style="stroke-width:5"><path d="M120 190l-24-18M130 230h-28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('precious', '大切にしまわれた宝石のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-120-40h240v120h-240z" class="goldd o"/>
  <path d="M-120-40q120-60 240 0" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 20)">
    <path d="M0-50l40 26v34L0 40l-40-24v-34z" class="violet o"/>
    <path d="M0-50v90" fill="none" stroke="#fffdf6" stroke-width="3"/>
  </g>
</g>
<g class="golds" style="stroke-width:5"><path d="M170 150l-24-18M430 150l24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('precise', '細かい目盛りできっちり測るイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-220-30h440v60h-440z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="2">{''.join(f'<path d="M{-210+i*20}-30v{12 if i%5 else 24}"/>' for i in range(22))}</g>
</g>
<g transform="translate(300 160)">
  <path d="M-30-50h60v50h-60z" class="teal o"/>
  <path d="M0 0v60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 170l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('predictable', '同じ形がくり返され、次が読めるイラスト。', f"""
<g class="teal o"><circle cx="120" cy="230" r="26"/><rect x="184" y="204" width="52" height="52"/><circle cx="300" cy="230" r="26"/><rect x="364" y="204" width="52" height="52"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="480" cy="230" r="26"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M460 320l18 18 30-36"/></g>
<path d="M100 150h400" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('preliminary', '本番の前に、ひとまず下ごしらえをするイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-90-70h180v140h-180z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 9"/>
  <g fill="{MUTED}"><rect x="-50" y="-30" width="100" height="14"/><rect x="-50" y="0" width="70" height="14"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-90-70h180v140h-180z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-50" y="-30" width="100" height="16"/><rect x="-50" y="0" width="80" height="16"/></g>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('premier', '並ぶ中で最上位に置かれるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-60-90h120v90h-120z" class="gold o"/>
  <path d="M-190-50h120v50h-120z" class="tealp o"/>
  <path d="M70-30h120v30H70z" class="coralp o"/>
</g>
<g transform="translate(300 170)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<path d="M60 316h480" class="a"/>
""", ground=True)

add('preparation', '道具と材料をそろえて支度するイラスト。', f"""
<g transform="translate(300 300)"><path d="M-230-20h460v26h-460z" class="goldd o"/></g>
<g transform="translate(140 250)"><path d="M-50-40h100v60h-100z" class="tealp o"/></g>
<g transform="translate(280 250)"><path d="M-40-40h80v60h-80z" class="coralp o"/></g>
{box(430,250,100,64,0,'gold')}
{person(520,340,0.8,-1,'teal','blue','reach','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('presentation', '資料を映して、みんなに発表するイラスト。', f"""
<g transform="translate(400 220)">
  <path d="M-150-130h300v230h-300z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"><path d="M-110 60l60-70 50 40 60-80"/></g>
  <g fill="{INK}"><rect x="-110" y="-110" width="140" height="14"/></g>
  <path d="M0 100v40" class="ink" stroke="{INK}" stroke-width="6"/>
</g>
{person(140,346,1.1,1,'blue','blue','point','short','smile')}
{person(250,366,0.6,-1,'coral','gold','stand','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('priest', '祭壇の前に立つ聖職者のイラスト。', f"""
<g transform="translate(430 250)">
  <path d="M-90 90h180v-40h-180z" class="goldd o"/>
  <path d="M-60 50V-30h120v80z" class="goldp o"/>
  <g fill="{TONES['gold'][2]}"><rect x="-8" y="-100" width="16" height="70"/><rect x="-34" y="-80" width="68" height="16"/></g>
</g>
{person(180,346,1.25,1,'violet','violet','stand','short','neutral')}
<g transform="translate(180 226)"><path d="M-10-10h20v22h-20z" fill="#fffdf6"/></g>
<path d="M260 260h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('primary', 'いちばん最初で主要なものを示したイラスト。', f"""
<g class="tealp o"><rect x="300" y="220" width="80" height="100"/><rect x="400" y="220" width="80" height="100"/></g>
<rect x="140" y="180" width="120" height="140" class="coral o"/>
<g transform="translate(200 130)"><circle r="26" class="gold o"/><path d="M-4-14h8v28h-8z" fill="#fffdf6"/></g>
<path d="M280 270h20" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('prime', 'いちばん盛りの、最良の状態を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100q80-20 130-140t130 140" fill="none" stroke="{TONES['teal'][0]}" stroke-width="7"/>
  <circle cx="-40" cy="-40" r="14" class="coral o"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M230 110l-24-18M290 90v-26"/></g>
""", ground=True)

add('prince', '王冠をかぶった若い王子のイラスト。', f"""
{person(300,346,1.35,1,'violet','blue','stand','short','smile')}
<g transform="translate(300 196)"><path d="M-40 18l-8-46 24 18 24-32 24 32 24-18-8 46z" class="gold o"/></g>
<g transform="translate(300 260)"><path d="M-10-10h20v22h-20z" class="gold o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
