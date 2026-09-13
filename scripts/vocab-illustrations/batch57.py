"""第57回: 損害・定義・配達・距離など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('crude', 'ざっくり削っただけの、粗雑な作りのイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-80-70l160 10-10 140-150-20z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-50-40l20 60-10 50M30-50l-20 70 20 60"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80-70h160v140h-160z" class="teal o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="3"><path d="M-50-40h100M-50 0h100M-50 40h100"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h60"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('curtain', '窓の前に下がったカーテンのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-160-140h320v280h-320z" fill="#cfe6f5" class="o"/>
  <path d="M-170-160h340v20h-340z" fill="#c9d3dc" class="o"/>
  <path d="M-160-140h100q10 140 0 280h-100z" class="coralp o"/>
  <path d="M60-140h100v280H60q-10-140 0-280z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"><path d="M-130-140q6 140 0 280M-95-140q6 140 0 280M95-140q-6 140 0 280M130-140q-6 140 0 280"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('custom', '毎年きまって同じことをする慣習のイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="10" stroke-dasharray="20 14"><circle cx="300" cy="210" r="130"/></g>
<g transform="translate(300 80)">
  <path d="M-50 30h100V-10h-100z" class="coralp o"/>
  <g class="gold o"><rect x="-6" y="-40" width="12" height="30"/></g>
</g>
<g transform="translate(430 210)">{person(0,0,0.6,1,'teal','blue','up','short','smile')}</g>
<g transform="translate(170 210)">{person(0,0,0.6,1,'coral','gold','up','bob','smile')}</g>
<path d="M380 100a140 140 0 0 1 50 60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('cute', '丸い目をした、かわいらしい子犬のイラスト。', f"""
<g transform="translate(300 260)">
  <ellipse rx="90" ry="70" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <circle cy="-90" r="60" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <ellipse cx="-56" cy="-120" rx="24" ry="34" fill="#c08d55" stroke="{INK}" stroke-width="3"/>
  <ellipse cx="56" cy="-120" rx="24" ry="34" fill="#c08d55" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><circle cx="-22" cy="-96" r="9"/><circle cx="22" cy="-96" r="9"/></g>
  <g fill="#fffdf6"><circle cx="-18" cy="-100" r="3.5"/><circle cx="26" cy="-100" r="3.5"/></g>
  <ellipse cy="-66" rx="16" ry="11" fill="{INK}"/>
  <path d="M-14-52q14 12 28 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="coral o" opacity=".8"><circle cx="420" cy="150" r="12"/><circle cx="450" cy="120" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('cynical', '差し出された話を、うたぐって受け取らないイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(300 220)">
  <path d="M-60-40h120v70h-120z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-16h72M-36 4h50"/></g>
</g>
{person(460,346,1.2,-1,'violet','blue','think','bob','flat')}
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M430 190l40 12"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M370 150l34 34M404 150l-34 34"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('damage', 'ぶつかって、車体がへこんだイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-160 40h320v-50l-60-50h-200l-60 50z" class="tealp o"/>
  <circle cx="-90" cy="46" r="28" class="ink"/><circle cx="90" cy="46" r="28" class="ink"/>
  <path d="M100-40h60v30h-60z" fill="#e8f4fb"/>
  <path d="M-160-10q40 20 0 50" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M120 180l-26-20M110 230h-30"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('damaging', '薬品がかかって、表面がだめになるイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
  <path d="M-50-40q60-20 90 30t-40 70-80-20 30-80z" fill="#8b8161" opacity=".85"/>
</g>
{drop(300,150,1.0,'green')}
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('deadly', 'どくろの印がついた、命にかかわるもののイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="130" class="coralp o"/>
  <g transform="translate(0 -10)">
    <circle r="66" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
    <g fill="{INK}"><circle cx="-22" cy="-12" r="12"/><circle cx="22" cy="-12" r="12"/><rect x="-6" y="10" width="12" height="18"/></g>
    <path d="M-30 40h60" fill="none" stroke="{INK}" stroke-width="5"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"><circle r="120"/></g>
</g>
""", ground=False)

add('decent', 'ひどくはない、まずまずの出来を示したイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o"><rect x="120" y="280" width="80" height="60"/><rect x="400" y="140" width="80" height="200"/></g>
<rect x="260" y="210" width="80" height="130" class="teal o"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M270 160l20 20 34-40"/></g>
""", ground=False)

add('decisive', '迷いを断って、こちらと決めるイラスト。', f"""
{person(150,346,1.2,1,'blue','blue','point','short','neutral')}
<path d="M230 250q90 0 130-70h140" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" marker-end="url(#ar)"/>
<path d="M230 280q90 0 130 70h140" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M420 320l34 34M454 320l-34 34"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('dedicate', '時間のすべてを一つのことに注ぐイラスト。', f"""
<g transform="translate(170 220)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <path d="M0 0v-70A90 90 0 1 1-64 64z" class="teal o"/>
  <circle r="90" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(440 240)">
  <path d="M-80-60h160v140h-160z" fill="#fffdf6" class="o"/>
  <path d="M-50-30h100v20h-100zM-50 10h100v20h-100z" class="teal"/>
</g>
<path d="M290 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('dedicated', 'ひとつのことに打ち込んで働き続けるイラスト。', f"""
<g transform="translate(320 300)">
  <path d="M-160-20h320v26h-320z" class="goldd o"/>
</g>
{person(300,300,1.15,1,'teal','blue','reach','short','neutral')}
<g transform="translate(380 250)"><path d="M-50-30h100v40h-100z" class="paper"/></g>
<g transform="translate(150 200)">
  <circle r="46" fill="#fffdf6" class="o"/>
  <path d="M0-30v30l20 12" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M470 190l24-18M478 230h28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('defensive', '盾を前に構えて、身を守るイラスト。', f"""
{person(230,346,1.25,1,'teal','blue','carry','short','neutral')}
<g transform="translate(320 250)">
  <path d="M0-80q56 22 56 66 0 56-56 78-56-22-56-78 0-44 56-66z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M520 200h-140M520 280h-140"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('definition', '語の意味を短く言い切った説明のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-130h380v260h-380z" class="paper"/>
  <g fill="{INK}"><rect x="-150" y="-100" width="120" height="20"/></g>
  <path d="M-150-60h300" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-150-20h300M-150 20h300M-150 60h240"/></g>
  <g class="teal o"><circle cx="-166" cy="-90" r="8"/></g>
</g>
""", ground=True)

add('degree', '温度計の目盛りで度合いを示したイラスト。', f"""
{thermometer(200,240,0.55,1.3)}
<g transform="translate(430 230)">
  <path d="M-90 60a90 90 0 0 1 180 0z" fill="#f7fbfe" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M0 60l{int(-76*__import__("math").cos(i*3.14159/6))} {int(60-76*__import__("math").sin(i*3.14159/6))}"/>' for i in range(7))}</g>
  <path d="M0 60L50 10" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('deliberate', 'よく考え、図面のとおりに手を進めるイラスト。', f"""
<g transform="translate(400 230)">
  <path d="M-130-120h260v240h-260z" fill="#e8f2fb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M-90-70h180v140h-180zM-90 0h180M0-70v140"/></g>
</g>
{person(150,346,1.1,1,'teal','blue','think','short','neutral')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="240" cy="280" r="12"/><circle cx="216" cy="304" r="8"/></g>
<path d="M250 220h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('delighted', '両手を挙げて、心から喜ぶイラスト。', f"""
{person(280,346,1.4,1,'coral','gold','up','bob','smile')}
<g class="golds" style="stroke-width:6"><path d="M160 170l-30-24M150 220h-34M400 170l30-24M410 220h34"/></g>
<g class="coral o"><circle cx="200" cy="130" r="10"/><circle cx="380" cy="120" r="12"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('delivery', '荷物を家まで届けるイラスト。', f"""
<g transform="translate(160 270)">
  <path d="M-100 40h90v-90h-90z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 40h130v-70H-10z" class="tealp o"/>
  <circle cx="-60" cy="52" r="26" class="ink"/><circle cx="70" cy="52" r="26" class="ink"/>
</g>
{person(330,340,0.95,1,'teal','blue','carry','cap','smile')}
<g transform="translate(330 260)">{box(330,260,80,60,0,'gold')}</g>
<g transform="translate(490 290)">
  <path d="M-70 50h140V-20h-140z" fill="#f4ead2" class="o"/>
  <path d="M-90-20l90-60 90 60z" class="coral o"/>
</g>
<path d="M400 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('demand', '欲しい人が列をつくって、強く求めるイラスト。', f"""
{person(140,346,1.0,1,'coral','blue','up','short','neutral')}
{person(230,346,1.0,1,'gold','blue','up','bob','neutral')}
{person(320,346,1.0,1,'teal','gold','up','cap','neutral')}
<g transform="translate(470 260)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><rect x="-60" y="-140" width="120" height="60"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M380 250h40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('dense', 'すきまなくびっしり詰まっているイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-100h180v200h-180z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o"><circle cx="-40" cy="-40" r="20"/><circle cx="30" cy="10" r="20"/><circle cx="-20" cy="60" r="20"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-90-100h180v200h-180z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="teal o">{''.join(f'<circle cx="{-70+c*35}" cy="{-80+r*35}" r="16"/>' for r in range(6) for c in range(5))}</g>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('departure', '駅を出て行く列車のイラスト。', f"""
<g transform="translate(240 250)">
  <path d="M-180 60h360v-140h-360z" class="bluep o"/>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="3"><rect x="-140" y="-60" width="80" height="50"/><rect x="-20" y="-60" width="80" height="50"/></g>
  <circle cx="-100" cy="76" r="24" class="ink"/><circle cx="100" cy="76" r="24" class="ink"/>
</g>
<g transform="translate(500 290)"><path d="M-60-20h120v40h-120z" fill="#dfe6ea" class="o"/></g>
{person(510,270,0.7,-1,'coral','gold','up','bob','smile')}
<path d="M120 180h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('dependable', '重い荷を任せても崩れない、頼れる支えのイラスト。', f"""
<g transform="translate(300 200)">{box(300,200,180,90,0,'gold')}</g>
<g transform="translate(300 320)">
  <path d="M-140-40h280v40h-280z" class="teal o"/>
  <path d="M-110 0h40v60h-40zM70 0h40v60H70z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 200l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('dependent', '支えがないと立てない、頼りきりのイラスト。', f"""
<g transform="translate(360 250)">
  <path d="M-16-120h32v240h-32z" fill="#c9d3dc" class="o"/>
</g>
<g transform="translate(280 346) rotate(14)">{person(0,0,1.2,1,'coral','blue','stand','bob','neutral')}</g>
<path d="M180 200h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M470 140v200"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('depressed', '肩を落として、気分が沈んでいるイラスト。', f"""
<g transform="translate(280 346) rotate(6)">{person(0,0,1.35,1,'blue','blue','stand','short','sad')}</g>
<g class="muted"><path d="M170 190q-16 20-16 44M390 190q16 20 16 44"/></g>
<g fill="{MUTED}" opacity=".9"><path d="M300 120q30-40 60 0-30 40-60 0z" opacity="0"/></g>
{cloud(300,110,1.0)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('depressing', '雨降りの空が続いて、気がめいるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#8b98a6"/>
<g fill="#6d7c8c"><path d="M60 130q-10-50 50-56 20-40 80-24 40-40 100 0 60-20 80 30 60 0 60 50z"/></g>
<g fill="none" stroke="#cfd8e0" stroke-width="4" stroke-linecap="round">
  {''.join(f'<path d="M{80+i*50} 200l-16 50"/>' for i in range(10))}
</g>
<g transform="translate(300 340) scale(0.9)">{person(0,0,1.0,1,'blue','blue','stand','short','sad')}</g>
""", ground=False)

add('description', '見たものを言葉で書き表すイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <path d="M-60 50l50-70 40 40 40-60 30 90z" class="green o"/>
  {sun(140,190,20)}
</g>
<g transform="translate(430 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-70 {-60+i*34}h140"/>' for i in range(5))}</g>
</g>
<path d="M280 230h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('desirable', 'みんなが手を伸ばす、望ましいもののイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M0-70l24 50 54 6-40 38 10 54-48-28-48 28 10-54-40-38 54-6z" class="gold o"/>
</g>
{hand(180,300,1)}{hand(420,300,-1)}
<g class="a" marker-end="url(#ar)"><path d="M200 260l40-30M400 260l-40-30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('destructive', 'すべてを打ちこわしてしまうイラスト。', f"""
<g transform="translate(300 140) rotate(-14)">
  <path d="M-90-40h180v60h-180z" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <path d="M-12 20h24v120h-24z" class="goldd o"/>
</g>
<g fill="#b6bfc9" stroke="{INK}" stroke-width="3">
  <path d="M120 340l50-70 30 50z"/><path d="M230 340l60-50 20 50z"/><path d="M340 340l50-60 40 60z"/><path d="M440 340l40-40 30 40z"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M120 240l-30 20M480 240l30 20"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('detail', '虫めがねで細かい部分まで見るイラスト。', f"""
<g transform="translate(250 240)">
  <path d="M-150-120h300v240h-300z" fill="#fffdf6" class="o"/>
  <g class="tealp o">{''.join(f'<circle cx="{-110+c*55}" cy="{-80+r*55}" r="18"/>' for r in range(4) for c in range(5))}</g>
</g>
<g transform="translate(400 190) rotate(24)">
  <circle r="80" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <g class="teal o"><circle cx="-24" cy="-14" r="26"/><circle cx="30" cy="20" r="26"/></g>
  <path d="M0 80v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('detailed', '細かいところまで書き込まれた図のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v280h-380z" fill="#e8f2fb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3">
    <path d="M-140-100h280v200h-280z"/><path d="M-140-40h280M-140 20h280M-60-100v200M60-100v200"/>
    <path d="M-120-80h40v30h-40zM-40-20h40v30h-40zM80 40h40v30H80z"/>
  </g>
  <g class="a" style="stroke-width:2" marker-end="url(#ar)"><path d="M-140 120h280"/></g>
</g>
""", ground=True, arrow=True)

add('development', '小さな芽が段を追って育っていくイラスト。', f"""
<g transform="translate(120 330)">
  <path d="M0 10v-30" fill="none" stroke="{TONES['green'][2]}" stroke-width="5"/>
  <g class="green o"><ellipse cx="-14" cy="-24" rx="14" ry="8" transform="rotate(-20 -14 -24)"/></g>
</g>
{tree(280,330,0.8)}
{tree(460,330,1.5)}
<path d="M100 230h400" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('diagram', '関係を線と箱で表した図表のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g class="tealp o"><rect x="-60" y="-110" width="120" height="50"/><rect x="-160" y="0" width="110" height="50"/><rect x="50" y="0" width="110" height="50"/></g>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M0-60v30M-105 0v-30h210v30"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M-105 50v40h210V50"/></g>
</g>
""", ground=True)

add('diamond', 'かたく輝くダイヤモンドのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-120-50h240l-120 160z" fill="#cfe6f5" stroke="{INK}" stroke-width="3"/>
  <path d="M-120-50l40-50h160l40 50z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="2"><path d="M-120-50h240M-80-100l-40 50 120 160M80-100l40 50-120 160M-40-100l40 50 40-50"/></g>
</g>
<g class="golds" style="stroke-width:5"><path d="M170 110l-26-20M430 110l26-20M300 80V50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('differently', '同じ課題に、別々のやり方で取り組むイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-80h160v160h-160z" fill="#fffdf6" class="o"/>
  <circle r="46" class="teal o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-80-80h160v160h-160z" fill="#fffdf6" class="o"/>
  <path d="M-46-46h92v92h-92z" class="coral o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M280 220h40M280 260h40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M282 200l36 80"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('difficulty', '重い岩が道をふさいで、進みにくいイラスト。', f"""
<g transform="translate(380 280)">
  <path d="M-120 60l30-90 60-30 70 20 40 50-20 50z" fill="#b6bfc9" stroke="{INK}" stroke-width="3"/>
</g>
{person(160,346,1.15,1,'teal','blue','walk','short','flat')}
<path d="M230 250h40" class="a" marker-end="url(#ar)"/>
{drop(200,230,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('diplomatic', '両国の代表が席をはさんで話し合うイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-140-20h280v26h-280z" class="goldd o"/>
</g>
<g transform="translate(160 200)"><path d="M-4-60h8v90h-8z" class="ink"/><path d="M4-56h50v34H4z" class="teal o"/></g>
<g transform="translate(440 200)"><path d="M-4-60h8v90h-8z" class="ink"/><path d="M-54-56h50v34h-50z" class="coral o"/></g>
{person(180,330,1.0,1,'blue','blue','reach','short','smile')}
{person(420,330,1.0,-1,'violet','blue','reach','bob','smile')}
<path d="M250 250h100" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('direct', 'よそに寄らず、まっすぐ目的地へ行くイラスト。', f"""
<circle cx="110" cy="230" r="24" class="teal o"/>
<path d="M150 230h300" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" marker-end="url(#ar)"/>
<g transform="translate(500 230)"><path d="M0 40c-30-40-40-56-40-72a40 40 0 0 1 80 0c0 16-10 32-40 72z" class="coral o"/><circle cy="-34" r="13" fill="#fffdf6"/></g>
<path d="M150 300q120 80 300 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M280 350l30 30M310 350l-30 30"/></g>
""", ground=False, arrow=True)

add('disadvantage', '一方だけ坂の下にいて、不利なイラスト。', f"""
<path d="M60 340L300 200h240v140z" class="green o"/>
{person(430,200,1.05,1,'teal','blue','stand','short','smile')}
{person(160,340,1.05,1,'coral','gold','stand','bob','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M140 200l30 30M170 200l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('disaster', '地震で建物が崩れる災害のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#e0dfd8"/>
<g fill="#c8c2b0" stroke="{INK}" stroke-width="3">
  <path d="M120 340v-120l60-30v150z" transform="rotate(-8 150 300)"/>
  <path d="M240 340v-90l60 20v70z"/>
  <path d="M360 340v-140l70 50v90z" transform="rotate(6 400 300)"/>
</g>
<g class="muted" opacity=".9"><path d="M200 180q30-40 0-70M420 160q30-40 0-70"/></g>
<g class="corals" style="stroke-width:6"><path d="M300 150v-30M240 170l-24-24M360 170l24-24"/></g>
<path d="M60 350h480" class="a"/>
""", ground=False)

add('disastrous', '計画の線が急落して、大失敗になるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100h340" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-170-60q80-20 140 0t60 160" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M30 100q60 0 140 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M440 130l34 34M474 130l-34 34"/></g>
""", ground=True)

add('discount', 'もとの値段に線を引いて、安くするイラスト。', f"""
<g transform="translate(300 220) rotate(-8)">
  <path d="M-140-90h230l50 90-50 90h-230z" class="coral o"/>
  <circle cx="80" r="14" fill="#fffdf6"/>
  <g fill="#fffdf6"><rect x="-110" y="-50" width="140" height="24"/></g>
  <g fill="none" stroke="#fffdf6" stroke-width="6"><path d="M-116-46h150"/></g>
  <g fill="#fffdf6"><rect x="-110" y="10" width="100" height="34"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 350v-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
