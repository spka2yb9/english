"""第51回: 泥棒・わな・ねじる・不当など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('themselves', 'その人たち自身が、自分たちを指さすイラスト。', f"""
{person(180,346,1.15,1,'coral','gold','point','bob','smile')}
{person(320,346,1.15,1,'teal','blue','point','short','smile')}
{person(460,346,1.15,1,'gold','blue','point','cap','smile')}
<path d="M180 170q140-40 280 0" fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M320 150v40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('thief', '袋を抱えてこっそり忍び込む泥棒のイラスト。', f"""
<g transform="translate(400 250)">
  <path d="M-110-110h220v220h-220z" fill="#e4e9ee" class="o"/>
  <path d="M-70-70h140v100h-140z" fill="#41506a" class="o"/>
</g>
{person(200,346,1.2,1,'violet','violet','carry','cap','flat')}
<g transform="translate(200 250)">
  <path d="M-46 40q-14-60 46-70 60 10 46 70z" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="{INK}"><rect x="168" y="196" width="64" height="14"/></g>
<path d="M300 300h-80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('thinking', '頭の中で考えを組み立てているイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(420 190)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="-40" cy="-10" r="26"/><circle cx="30" cy="20" r="20"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="290" r="12"/><circle cx="266" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('third', '三等分したうちの一つを示したイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="130" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M0 0v-130M0 0l113 65M0 0l-113 65"/></g>
  <path d="M0 0v-130a130 130 0 0 1 113 65z" class="coral o"/>
</g>
<path d="M470 130h-60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('thought', '頭に浮かんだ一つの考えのイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(420 190)">
  <path d="M-120-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 -6)">
    <circle r="34" class="goldp o"/>
    <path d="M-12 34h24v12h-24z" class="ink"/>
    <g class="golds" style="stroke-width:4"><path d="M0-50v-14M-36-26l-14-8M36-26l14-8"/></g>
  </g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="280" cy="290" r="12"/><circle cx="256" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('threaten', 'こぶしを見せて、おどしをかけるイラスト。', f"""
{person(180,346,1.25,1,'violet','blue','point','short','flat')}
<g transform="translate(310 230)">
  <circle r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M-10-14h24M-10 0h24M-10 14h20"/></g>
</g>
{person(470,346,1.15,-1,'coral','gold','up','bob','surprised')}
<path d="M360 200h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('thrive', '苗が大きく育って、よく茂るイラスト。', f"""
<g transform="translate(150 320)">
  <path d="M0 20v-50" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  <g class="green o"><ellipse cx="-20" cy="-34" rx="20" ry="11" transform="rotate(-20 -20 -34)"/><ellipse cx="20" cy="-44" rx="20" ry="11" transform="rotate(20 20 -44)"/></g>
</g>
{tree(430,330,1.6)}
<path d="M240 240h100" class="a" marker-end="url(#ar)"/>
{sun(520,90,26)}
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('tight', 'すきまなくぴったり詰まっているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-110h400v220h-400z" fill="none" stroke="{INK}" stroke-width="5"/>
  <g class="teal o">{''.join(f'<rect x="{-190+c*96}" y="{-100+r*100}" width="94" height="98"/>' for r in range(2) for c in range(4))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 380h60M480 380h-60"/></g>
""", ground=False, arrow=True)

add('time', '時を刻む時計と砂時計のイラスト。', f"""
<g transform="translate(200 210)">
  <circle r="100" fill="#fffdf6" class="o"/>
  <g fill="{INK}">{''.join(f'<rect x="-4" y="-92" width="8" height="18" transform="rotate({i*30})"/>' for i in range(12))}</g>
  <path d="M0 0v-64M0 0l44 30" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
<g transform="translate(450 220)">
  <path d="M-50-100h100v20h-100zM-50 100h100v20h-100z" class="goldd o"/>
  <path d="M-40-80h80l-40 80zM-40 100h80l-40-80z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('tiny', '大きな箱のわきにある、ごく小さな粒のイラスト。', f"""
<g transform="translate(220 250)">
  <path d="M-120-100h240v200h-240z" class="tealp o"/>
</g>
<g transform="translate(430 330)"><circle r="12" class="coral o"/></g>
<g transform="translate(500 240)">
  <circle r="46" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle r="8" class="coral o"/>
  <path d="M32 32l30 30" fill="none" stroke="{INK}" stroke-width="10"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('title', '書類の先頭に大きく置かれた見出しのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="{INK}"><rect x="-140" y="-110" width="240" height="26"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-140 {-40+i*34}h280"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="150" y="96" width="260" height="46"/></g>
<path d="M470 119h-50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('top', '積み重ねのいちばん上を示したイラスト。', f"""
<g class="tealp o"><rect x="220" y="300" width="160" height="60"/><rect x="230" y="240" width="140" height="60"/></g>
<rect x="245" y="170" width="110" height="70" class="coral o"/>
<path d="M300 100v40" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('torture', '縛られて痛みを与えられるイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-30-140h60v260h-60z" fill="#c9d3dc" class="o"/>
</g>
<g transform="translate(300 300)">
  <circle cy="-160" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40-130q40-20 80 0l-6 130h-70z" class="coralp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="7"><path d="M-46-80h92M-46-20h92"/></g>
</g>
<g class="corals" style="stroke-width:5"><path d="M180 200q-24 20-24 44M420 200q24 20 24 44"/></g>
{drop(240,220,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('towel', 'かけてある一枚のタオルのイラスト。', f"""
<g transform="translate(300 120)"><path d="M-200-10h400v14h-400z" fill="#c9d3dc" class="o"/></g>
<g transform="translate(300 250)">
  <path d="M-120-130h240v250h-240z" class="tealp o"/>
  <path d="M-120-130h240v20h-240z" class="teal o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M-120 60h240M-120 90h240"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('toy', '積み木とくまのぬいぐるみのイラスト。', f"""
<g transform="translate(160 300)">
  <path d="M-50-40h100v80h-100z" class="coralp o"/>
  <path d="M-30-100h60v60h-60z" class="tealp o"/>
  <path d="M-20-140h40v40h-40z" class="goldp o"/>
</g>
<g transform="translate(410 290)">
  <ellipse rx="70" ry="60" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <circle cy="-80" r="46" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <circle cx="-40" cy="-114" r="18" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <circle cx="40" cy="-114" r="18" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><circle cx="-14" cy="-86" r="5"/><circle cx="14" cy="-86" r="5"/></g>
  <ellipse cy="-66" rx="14" ry="10" fill="#f0d6b0"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('trace', '地面に残った足あとをたどるイラスト。', f"""
<g fill="{MUTED}" opacity=".8">
  <ellipse cx="120" cy="330" rx="18" ry="11"/><ellipse cx="190" cy="300" rx="18" ry="11"/><ellipse cx="260" cy="330" rx="18" ry="11"/><ellipse cx="330" cy="300" rx="18" ry="11"/>
</g>
<g transform="translate(430 230) rotate(24)">
  <circle r="60" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <g fill="{MUTED}"><ellipse cx="-10" cy="10" rx="20" ry="12"/></g>
  <path d="M0 60v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<path d="M120 240h200" fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('trainer', 'ホイッスルを手に、指導するトレーナーのイラスト。', f"""
{person(170,346,1.25,1,'blue','blue','point','cap','neutral')}
<g transform="translate(216 246)">
  <path d="M-16-10h34v20h-34z" class="ink"/>
  <circle cx="24" r="12" class="ink"/>
</g>
{person(420,346,1.0,1,'coral','gold','walk','short','neutral')}
{person(510,346,1.0,1,'teal','blue','walk','bob','neutral')}
<path d="M260 220h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('training', '同じ動きをくり返して身につける訓練のイラスト。', f"""
<g opacity=".35">{person(160,346,1.15,1,'teal','blue','up','short','neutral')}</g>
<g opacity=".6">{person(300,346,1.15,1,'teal','blue','stand','short','neutral')}</g>
{person(440,346,1.15,1,'teal','blue','up','short','neutral')}
<path d="M180 150q140 60 280 0" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('transfer', '荷物を別の入れ物へ移し替えるイラスト。', f"""
<g transform="translate(170 280)">
  <path d="M-80-60h160v120h-160z" fill="#fffdf6" class="o"/>
  <g class="tealp o"><circle cx="-30" cy="30" r="20"/></g>
</g>
<g transform="translate(430 280)">
  <path d="M-80-60h160v120h-160z" fill="#fffdf6" class="o"/>
  <g class="teal o"><circle cx="-20" cy="30" r="20"/><circle cx="30" cy="20" r="20"/></g>
</g>
<path d="M250 180q80-50 150 0" class="a" marker-end="url(#ar)"/>
<g class="teal o"><circle cx="320" cy="150" r="20"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('transmit', '電波にのせて、信号を遠くへ送るイラスト。', f"""
<g transform="translate(150 260)">
  <path d="M-40 100L0-80l40 180z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-6-120h12v40h-12z" class="ink"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M200 160q30 30 30 60t-30 60M240 130q46 46 46 90t-46 90"/></g>
<g transform="translate(460 250)">
  <path d="M-90-70h180v130h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-70-50h140v90h-140z" class="tealp o"/>
</g>
<path d="M300 200h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('trap', 'えさを置いた箱のわなのイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-120-20h240v100h-240z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <path d="M-120-20l-40-120 30-10 40 110z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <g class="coral o"><circle cx="0" cy="50" r="16"/></g>
  <path d="M-140-16h20v96h-20z" fill="#8b98a6"/>
</g>
<g transform="translate(120 330)">
  <ellipse rx="34" ry="22" fill="#8b8161" stroke="{INK}" stroke-width="2"/>
  <circle cx="26" cy="-14" r="16" fill="#8b8161" stroke="{INK}" stroke-width="2"/>
  <path d="M-30 8q-40 8-44-14" fill="none" stroke="#8b8161" stroke-width="4"/>
</g>
<path d="M180 300h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('traveller', 'かばんを持って旅を続ける人のイラスト。', f"""
{person(220,346,1.25,1,'coral','blue','carry','cap','smile')}
<g transform="translate(280 300)">
  <path d="M-40-30h80v70h-80z" class="goldd o"/>
  <path d="M-16-30q16-16 32 0" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g class="muted"><path d="M400 240h120M410 290h110"/></g>
{sun(510,100,26)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('trigger', '引き金を引いて、動きを起こすイラスト。', f"""
<g transform="translate(220 240)">
  <path d="M-120-30h200v50h-200z" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <path d="M40 20h50v70H40z" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <path d="M20 26q-20 20 0 40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"/>
</g>
<g transform="translate(470 240)">
  <path d="M0-70l24 56 60 6-44 42 12 60-52-30-52 30 12-60-44-42 60-6z" class="coralp o"/>
</g>
<path d="M330 230h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('trip', 'かばんを手に、遠くへ出かけるイラスト。', f"""
{person(160,340,1.05,1,'teal','gold','carry','bob','smile')}
<g transform="translate(214 300)"><path d="M-34-24h68v56h-68z" class="goldd o"/><path d="M-14-24q14-14 28 0" fill="none" stroke="{INK}" stroke-width="5"/></g>
{plane(430,120,0.9,-8)}
<path d="M270 250q120-40 200-60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"/>
{building(500,320,0.7,'teal')}
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('trust', '相手に背を預けて、任せきるイラスト。', f"""
{person(220,346,1.2,1,'teal','blue','give','short','smile')}
{person(380,346,1.2,-1,'coral','gold','give','bob','smile')}
<path d="M282 250h36" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(300 150)">
  <path d="M0 40c-36-28-52-42-52-64a28 28 0 0 1 52-15 28 28 0 0 1 52 15c0 22-16 36-52 64z" class="coralp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M-16-14l12 14 22-26"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('twin', 'そっくりの二人が並ぶふたごのイラスト。', f"""
{person(230,346,1.25,1,'coral','gold','stand','bob','smile')}
{person(380,346,1.25,1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M290 180h30M290 210h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('twist', 'タオルをねじって絞るイラスト。', f"""
{hand(140,220,1)}{hand(460,220,-1)}
<g transform="translate(300 250)">
  <path d="M-160-30q80 60 160 0t160 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="26" stroke-linecap="round"/>
  <path d="M-160 20q80-60 160 0t160 0" fill="none" stroke="{TONES['teal'][1]}" stroke-width="26" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M150 330a80 80 0 0 1 40-30M450 330a80 80 0 0 0-40-30"/></g>
""", ground=True, arrow=True)

add('ugly', '形のくずれた、見た目の悪いものを示したイラスト。', f"""
<g transform="translate(170 240)">
  <circle r="90" class="tealp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-14 0l12 14 22-26"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-70-70q60-40 100 10t30 60-70 50-80-20-10-70 30-30z" fill="#a2a58e" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-30-20q20 20 0 40M30-10q-20 20 0 40"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M500 130l30 30M530 130l-30 30"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('unable', '手が届かず、できないイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','up','short','sad')}
<g transform="translate(430 130)"><path d="M-50-30h100v60h-100z" class="gold o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M270 200h100"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M300 280l44 44M344 280l-44 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('uncomfortable', 'かたい椅子で、居心地の悪そうな人のイラスト。', f"""
<g transform="translate(320 300)">
  <path d="M-70-20h140v20h-140z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
  <path d="M-70-20h20v-70h-20z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
  <path d="M-56 0h12v50h-12zM44 0h12v50H44z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(350 230) scale(0.95)">{person(0,60,1.0,1,'coral','blue','stand','bob','sad')}</g>
{drop(410,190,0.8)}
<g class="corals" style="stroke-width:4"><path d="M250 240q-20 16-20 40"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('undergo', '検査の機械を通されて、それを受けるイラスト。', f"""
<g transform="translate(360 240)">
  <path d="M-140-120h280v240h-280z" fill="#dfe6ea" class="o"/>
  <circle r="70" fill="#fffaf1" stroke="{INK}" stroke-width="4"/>
</g>
<g transform="translate(300 300)"><path d="M-240-16h480v20h-480z" fill="#c9d3dc" class="o"/></g>
<g transform="translate(200 280) rotate(-90)">{person(0,0,0.9,1,'teal','blue','stand','short','neutral')}</g>
<path d="M240 200h80" class="a" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('undermine', '土台を下から削られて、崩れかけるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-120h280v180h-280z" fill="#f4ead2" stroke="{INK}" stroke-width="3" transform="rotate(-4)"/>
</g>
<g transform="translate(300 330)">
  <path d="M-160-20h320v40h-320z" fill="#c8bfa4" class="o"/>
  <path d="M-60-20h120v40h-120z" fill="#fffaf1"/>
  <g fill="#c8bfa4" stroke="{INK}" stroke-width="2"><circle cx="-40" cy="30" r="12"/><circle cx="20" cy="34" r="9"/></g>
</g>
<path d="M300 380v-30" class="a" marker-end="url(#ar)" transform="rotate(180 300 365)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('understanding', 'ばらばらの部品が頭の中でつながるイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(420 200)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g class="teal o"><path d="M-70-30h60v60h-60z"/><path d="M10-30h60v60H10z"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6"><path d="M-10 0h20"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="280" cy="300" r="12"/><circle cx="256" cy="324" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('undertake', '仕事を引き受けて、自分の肩に担うイラスト。', f"""
{person(300,346,1.3,1,'blue','blue','carry','short','neutral')}
<g transform="translate(300 220)">{box(0,0,150,90,0,'gold')}</g>
{person(500,346,1.0,-1,'teal','gold','give','bob','smile')}
<path d="M440 250h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('unfair', '片方だけ多くもらって、公平でないイラスト。', f"""
<g transform="translate(300 160)">
  <path d="M-6-40h12v60h-12z" class="ink"/>
  <path d="M-160 20h320" fill="none" stroke="{INK}" stroke-width="7" transform="rotate(-12)"/>
  <g transform="rotate(-12)"><path d="M-160 20v50" fill="none" stroke="{INK}" stroke-width="3"/><path d="M160 20v50" fill="none" stroke="{INK}" stroke-width="3"/></g>
</g>
<g transform="translate(140 250)"><g class="coral o"><circle r="30"/><circle cx="-30" cy="40" r="30"/><circle cx="30" cy="40" r="30"/></g></g>
<g transform="translate(470 200)"><circle r="30" class="tealp o"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M290 330l30 30M320 330l-30 30"/></g>
""", ground=False)

add('unfold', 'たたんだ紙を広げて開くイラスト。', f"""
<g transform="translate(160 260)">
  <path d="M-50-70h100v140h-100z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M0-70v140"/></g>
</g>
<g transform="translate(420 260)">
  <path d="M-140-90h280v180h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M0-90v180M-70-90v180M70-90v180"/></g>
</g>
<path d="M240 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('unit', 'ひとまとめの一組と、そろえた設備のイラスト。', f"""
<g fill="none" stroke="{INK}" stroke-width="4"><rect x="90" y="170" width="200" height="180" rx="10"/></g>
<g class="teal o"><rect x="120" y="200" width="60" height="60"/><rect x="200" y="200" width="60" height="60"/><rect x="120" y="270" width="60" height="60"/><rect x="200" y="270" width="60" height="60"/></g>
<g transform="translate(440 260)">
  <path d="M-90-90h180v180h-180z" fill="#dfe6ea" class="o"/>
  <g class="tealp o"><rect x="-60" y="-60" width="120" height="50"/><rect x="-60" y="10" width="120" height="50"/></g>
</g>
<path d="M320 260h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('unite', '別々の輪が一つに合わさるイラスト。', f"""
<g transform="translate(160 230)"><circle r="70" class="tealp o"/></g>
<g transform="translate(300 230)"><circle r="70" class="coralp o"/></g>
<g transform="translate(480 230)">
  <circle r="86" class="violet o"/>
</g>
<path d="M370 230h30" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('unlikely', '細い方の道で、まず起こらないと示すイラスト。', f"""
<circle cx="90" cy="230" r="22" class="teal o"/>
<path d="M120 210q120-80 220-60t140 20" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"/>
<path d="M120 250q120 80 220 60t140-20" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" stroke-linecap="round" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M300 130l34 34M334 130l-34 34"/></g>
""", ground=False, arrow=True)

add('unnecessary', 'なくてもよいものを外して、余りだと示すイラスト。', f"""
<g transform="translate(240 250)">
  <path d="M-150-90h300v180h-300z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="teal o"><rect x="-120" y="-60" width="70" height="120"/><rect x="-30" y="-60" width="70" height="120"/><rect x="60" y="-60" width="70" height="120"/></g>
</g>
<g transform="translate(490 250)">
  <path d="M-40-60h80v120h-80z" class="mutedfill" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-30-100l60 60M30-100l-60 60"/></g>
</g>
<path d="M400 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('unpleasant', 'いやなにおいに顔をしかめるイラスト。', f"""
{face(230,200,88,'flat')}
<g fill="none" stroke="{INK}" stroke-width="7"><path d="M186 154l38 14M274 154l-38 14"/></g>
<path d="M206 240q24 16 48 0" fill="none" stroke="{INK}" stroke-width="6"/>
<g transform="translate(440 290)">
  <path d="M-60 40h120l-14-70h-92z" fill="#8b8161" stroke="{INK}" stroke-width="3"/>
  <g class="muted" opacity=".9"><path d="M-30-40q20-40 0-70M20-40q20-40 0-70"/></g>
</g>
<path d="M340 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
