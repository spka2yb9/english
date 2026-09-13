"""第78回: 防衛・否定・深さ・区別など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('discovery', '隠れていたものを見つけ出すイラスト。', f"""
<g transform="translate(200 260)">
  <path d="M-140-100h280v200h-280z" fill="#fffdf6" class="o"/>
  <g class="gold o"><circle cx="20" cy="20" r="30"/></g>
  <g class="golds" style="stroke-width:5"><path d="M20-30v-20M-30 0l-18-14M70 0l18-14"/></g>
</g>
<g transform="translate(400 200) rotate(24)">
  <circle r="70" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <path d="M0 70v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('disease', '体を弱らせる病のイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','stand','short','sad')}
{thermometer(280,250,0.9,0.9)}
<g transform="translate(450 230)">
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="5">{''.join(f'<path d="M0 0L{int(56*__import__("math").cos(i*3.14159/4))} {int(56*__import__("math").sin(i*3.14159/4))}"/>' for i in range(8))}</g>
  <circle r="30" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M380 190h-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('defence', '盾で守りを固めるイラスト。', f"""
{person(230,346,1.25,1,'teal','blue','carry','short','neutral')}
<g transform="translate(320 250)">
  <path d="M0-90q60 24 60 70 0 60-60 84-60-24-60-84 0-46 60-70z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M520 200h-140M520 300h-140"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('defender', '前に立って守る守り手のイラスト。', f"""
{person(220,346,1.25,1,'blue','blue','carry','cap','neutral')}
<g transform="translate(300 250)">
  <path d="M0-80q56 22 56 66 0 56-56 78-56-22-56-78 0-44 56-66z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
</g>
{person(420,346,0.9,1,'coral','gold','stand','bob','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M150 200h60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('definitely', '疑いなくそうだと言い切るイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','stand','short','smile')}
<g transform="translate(430 210)">
  <path d="M-90-60h180v90h-180z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="12" stroke-linecap="round"><path d="M-36-18l24 24 48-50"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('delegation', '代表として数人が送られるイラスト。', f"""
{person(150,346,1.0,1,'blue','blue','stand','short','neutral')}
{person(240,346,1.0,1,'blue','blue','stand','bob','neutral')}
{person(330,346,1.0,1,'blue','blue','stand','cap','neutral')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="100" y="200" width="280" height="160" rx="14"/></g>
<path d="M410 250h60" class="a" marker-end="url(#ar)"/>
{building(520,320,0.6,'teal')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('delicate', '割れやすい薄いガラスを扱うイラスト。', f"""
{hand(180,180,1)}
<g transform="translate(330 270)">
  <path d="M-60-90h120l-16 160h-88z" fill="#e7f6fb" opacity=".8" stroke="{INK}" stroke-width="2"/>
  <path d="M-40-70h20l-8 130h-16z" fill="#ffffff" opacity=".8"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><circle cx="330" cy="250" r="120"/></g>
<g fill="{INK}" transform="translate(490 160)"><rect x="-6" y="-30" width="12" height="40"/><rect x="-6" y="18" width="12" height="12"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('delight', '飛び上がるほど大喜びするイラスト。', f"""
<g transform="translate(280 330) rotate(-6)">{person(0,0,1.4,1,'coral','gold','up','bob','smile')}</g>
<g class="golds" style="stroke-width:6"><path d="M150 180l-30-24M400 180l30-24M280 110v-30"/></g>
<g class="coral o"><circle cx="200" cy="140" r="12"/><circle cx="380" cy="130" r="14"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('demon', '角のある悪霊のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a52"/>
<g transform="translate(300 240)">
  <path d="M-90 110q-20-170 90-170t90 170z" fill="#5b4a7a" stroke="#8b7aa8" stroke-width="3"/>
  <path d="M-70-56l-16-52 44 28zM70-56l16-52-44 28z" fill="#5b4a7a" stroke="#8b7aa8" stroke-width="3"/>
  <g fill="{TONES['coral'][0]}"><path d="M-40-20l32 18-32 18zM40-20l-32 18 32 18z"/></g>
  <path d="M-40 50q40 30 80 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
  <g fill="#fffdf6"><path d="M-20 60l8 20-16-12zM20 60l-8 20 16-12z"/></g>
</g>
""", ground=False)

add('denial', '差し出された話をきっぱり否定するイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','give','short','neutral')}
<g transform="translate(300 230)">
  <path d="M-60-40h120v70h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-16h72M-36 4h50"/></g>
</g>
{person(470,346,1.2,-1,'blue','blue','point','bob','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M360 160l44 44M404 160l-44 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('density', '同じ枠に詰まる量のちがいを示したイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-100h180v200h-180z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o"><circle cx="-40" cy="-40" r="18"/><circle cx="30" cy="20" r="18"/><circle cx="-20" cy="60" r="18"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-90-100h180v200h-180z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="teal o">{''.join(f'<circle cx="{-70+c*35}" cy="{-80+r*35}" r="16"/>' for r in range(6) for c in range(5))}</g>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('deny', '要求を突き返して拒むイラスト。', f"""
{person(160,346,1.1,1,'coral','gold','give','bob','sad')}
<g transform="translate(310 250)">
  <path d="M-60-40h120v70h-120z" class="paper"/>
</g>
{person(470,346,1.2,-1,'blue','blue','point','short','flat')}
<path d="M390 310h-60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M370 160l44 44M414 160l-44 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('dependence', '支えなしでは立てない依存のイラスト。', f"""
<g transform="translate(380 250)"><path d="M-18-130h36v260h-36z" fill="#c9d3dc" class="o"/></g>
<g transform="translate(300 346) rotate(16)">{person(0,0,1.25,1,'coral','blue','stand','bob','neutral')}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M480 140v220"/></g>
<path d="M190 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('deployment', '人と物を現場へ配備するイラスト。', f"""
{person(140,346,0.9,1,'green','green','stand','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M200 250h120"/></g>
{person(380,346,0.9,1,'green','green','stand','cap','neutral')}
{person(470,346,0.9,1,'green','green','stand','cap','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="340" y="200" width="200" height="160" rx="14"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('depression', '気分が沈み込んで動けないイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#8b98a6"/>
{cloud(300,110,1.6)}
<g transform="translate(300 340) rotate(8)">{person(0,0,1.2,1,'blue','blue','stand','short','sad')}</g>
<g fill="none" stroke="#cfd8e0" stroke-width="4" stroke-linecap="round">{''.join(f'<path d="M{180+i*50} 190l-14 40"/>' for i in range(6))}</g>
""", ground=False)

add('depth', '水面から底までの深さを示したイラスト。', f"""
<path d="M0 160h600v240H0z" class="bluep"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" opacity=".8"><path d="M20 170q40-20 80 0t80 0t80 0t80 0t80 0t80 0"/></g>
<g fill="#8b6f4e"><path d="M0 360h600v40H0z"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 170v180M300 350V170"/></g>
""", ground=False, arrow=True)

add('deputy', '長のすぐ下で代わりを務める人のイラスト。', f"""
{person(230,346,1.35,1,'blue','blue','stand','short','neutral')}
<g transform="translate(230 226)"><path d="M-16-16l6 14 16 2-12 11 3 16-13-8-13 8 3-16-12-11 16-2z" class="gold o"/></g>
{person(400,346,1.15,1,'teal','blue','stand','bob','neutral')}
<g transform="translate(400 246)"><path d="M-12-12l4 10 12 2-9 8 2 12-9-6-9 6 2-12-9-8 12-2z" class="goldd o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('desire', '欲しくてたまらず手を伸ばすイラスト。', f"""
{person(200,346,1.25,1,'coral','gold','reach','bob','smile')}
<g transform="translate(430 220)">
  <path d="M0-70l24 50 54 6-40 38 10 54-48-28-48 28 10-54-40-38 54-6z" class="gold o"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M300 200l-24-18M310 240h-28"/></g>
<path d="M300 280h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('desktop', '机の上に置く卓上型の機械のイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-220-20h440v30h-440z" class="goldd o"/>
</g>
<g transform="translate(320 200)">
  <path d="M-140-100h280v170h-280z" fill="#41506a"/>
  <path d="M-116-78h232v126h-232z" class="bluep"/>
  <path d="M-30 70h60v20h-60z" fill="#41506a"/>
  <path d="M-70 90h140v10h-140z" class="ink"/>
</g>
<g transform="translate(140 250)"><path d="M-40-70h80v140h-80z" fill="#dfe6ea" class="o"/><g class="green o"><circle cy="-40" r="10"/></g></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('despite', '雨にもかかわらず出かけるイラスト。', f"""
<g class="muted" opacity=".9">{''.join(f'<path d="M{120+i*60} 90l-16 44"/>' for i in range(7))}</g>
{person(280,346,1.2,1,'teal','blue','walk','short','smile')}
<g transform="translate(300 190)">
  <path d="M-110 0q0-70 110-70t110 70z" class="violetp o"/>
  <path d="M-4 0h8v90h-8z" class="ink"/>
</g>
<path d="M400 300h120" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('destruction', 'すべてが打ちこわされた状態のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#c9c6b8"/>
<g fill="#8b8161" stroke="{INK}" stroke-width="3">
  <path d="M120 340v-120l50-26v146z" transform="rotate(-10 150 300)"/>
  <path d="M230 340v-90l60 24v66z"/>
  <path d="M340 340v-140l70 50v90z" transform="rotate(8 380 300)"/>
  <path d="M450 340l40-50 50 50z"/>
</g>
<g class="muted" opacity=".9"><path d="M200 200q30-40 0-70M420 180q30-40 0-70"/></g>
""", ground=False)

add('detection', '装置が異常を見つけて知らせるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-150-110h300v220h-300z" fill="#dfe6ea" class="o"/>
  <path d="M-120-80h240v140h-240z" class="bluep o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><circle cx="40" cy="-10" r="30"/></g>
  <g class="coral o"><circle cx="40" cy="-10" r="12"/></g>
  <g class="coral o"><circle cx="110" cy="-90" r="14"/></g>
</g>
<g class="corals" style="stroke-width:5"><path d="M470 130q26 20 26 44"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('detention', '居残りで別室にとどめられるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-180-140h360v280h-360z" fill="#e4e9ee" class="o"/>
  <g fill="{INK}">{''.join(f'<rect x="{-150+i*50}" y="-120" width="12" height="240"/>' for i in range(7))}</g>
</g>
<g transform="translate(300 250) scale(0.8)">{person(0,60,1.0,1,'coral','gold','stand','bob','sad')}</g>
<g transform="translate(500 130)"><circle r="34" fill="#fffdf6" class="o"/><path d="M0-22v22l16 10" fill="none" stroke="{INK}" stroke-width="4"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('determination', '歯を食いしばって決意するイラスト。', f"""
{person(280,346,1.4,1,'coral','blue','point','short','flat')}
{flame(430,220,0.9)}
<g class="corals" style="stroke-width:5"><path d="M160 190l-26-18M170 230h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('devil', '角と尾のある悪魔のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#33445c"/>
<g transform="translate(300 250)">
  <path d="M-80 100q-20-160 80-160t80 160z" fill="#c0574a" stroke="{INK}" stroke-width="3"/>
  <path d="M-60-50l-14-46 40 26zM60-50l14-46-40 26z" fill="#c0574a" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><path d="M-34-16l28 16-28 16zM34-16l-28 16 28 16z"/></g>
  <path d="M-34 46q34 26 68 0" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M80 60q50 20 40 60" fill="none" stroke="#c0574a" stroke-width="10"/>
  <path d="M118 118l20 10-24 12z" fill="#c0574a"/>
</g>
""", ground=False)

add('diagnosis', '検査の結果から病名を見立てるイラスト。', f"""
{person(160,340,1.1,1,'blue','blue','think','bob','neutral')}
<g transform="translate(400 230)">
  <path d="M-130-110h260v220h-260z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-100-40q30 0 40-40t40 80 40-60 60 20"/></g>
  <g fill="{INK}"><rect x="-100" y="40" width="140" height="16"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M60 40l14 14 24-30"/></g>
</g>
<path d="M250 220h30" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('dictator', 'ひとりの意向だけで決める独裁者のイラスト。', f"""
{person(200,346,1.4,1,'violet','violet','point','short','flat')}
<g transform="translate(200 196)"><path d="M-30 14l-6-36 18 14 18-24 18 24 18-14-6 36z" class="gold o"/></g>
{person(420,346,0.9,1,'teal','blue','stand','bob','sad')}
{person(510,346,0.9,1,'coral','gold','stand','short','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M290 220h80"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('dignity', '背筋を伸ばして威厳をもって立つイラスト。', f"""
{person(300,346,1.45,1,'violet','violet','stand','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 120v60"/></g>
<g class="golds" style="stroke-width:5"><path d="M420 200l24-18M180 200l-24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('dilemma', 'どちらの道も選びにくい板挟みのイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','think','short','flat')}
<path d="M240 250q90 0 130-70h130" fill="none" stroke="{MUTED}" stroke-width="8"/>
<path d="M240 290q90 0 130 70h130" fill="none" stroke="{MUTED}" stroke-width="8"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 150l30 30M500 150l-30 30M470 330l30 30M500 330l-30 30"/></g>
<g fill="{INK}" transform="translate(230 150)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('diplomat', '国旗を背に他国と話をつける外交官のイラスト。', f"""
<g transform="translate(140 200)"><path d="M-4-60h8v90h-8z" class="ink"/><path d="M4-56h50v34H4z" class="teal o"/></g>
<g transform="translate(460 200)"><path d="M-4-60h8v90h-8z" class="ink"/><path d="M-54-56h50v34h-50z" class="coral o"/></g>
{person(230,346,1.2,1,'blue','blue','reach','short','smile')}
{person(370,346,1.2,-1,'violet','blue','reach','bob','smile')}
<path d="M285 260h30" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('directly', 'よそに寄らずまっすぐ行くイラスト。', f"""
<circle cx="110" cy="230" r="24" class="teal o"/>
<path d="M150 230h300" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" marker-end="url(#ar)"/>
<g transform="translate(500 230)"><circle r="24" class="coral o"/></g>
<path d="M150 300q140 90 300 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M280 350l30 30M310 350l-30 30"/></g>
""", ground=False, arrow=True)

add('directory', '名前が並んだ名簿のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="{MUTED}">{''.join(f'<rect x="-100" y="{-100+i*45}" width="200" height="14"/>' for i in range(5))}</g>
  <g class="tealp o">{''.join(f'<circle cx="-130" cy="{-94+i*45}" r="16"/>' for i in range(5))}</g>
</g>
""", ground=True)

add('disagreement', '意見が食い違って一致しないイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','short','flat')}
{person(440,346,1.15,-1,'coral','gold','point','bob','flat')}
<g transform="translate(230 170)"><path d="M-60-40h120v56h-120z" fill="#fffdf6" class="o"/><g class="teal o"><circle r="16" transform="translate(0 -12)"/></g></g>
<g transform="translate(390 170)"><path d="M-60-40h120v56h-120z" fill="#fffdf6" class="o"/><g class="coral o"><rect x="-18" y="-28" width="36" height="34"/></g></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M295 140l30 30M325 140l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('disappointment', '期待が外れて肩を落とすイラスト。', f"""
<g transform="translate(200 346) rotate(8)">{person(0,0,1.25,1,'teal','blue','stand','short','sad')}</g>
<g transform="translate(430 240)">
  <path d="M-90-70h180v140h-180z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M400 130l30 30M430 130l-30 30"/></g>
{drop(260,240,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('disc', '円盤状のディスクのイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="140" class="violet o"/>
  <circle r="130" fill="none" stroke="#fffdf6" stroke-width="3" opacity=".6"/>
  <circle r="40" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle r="14" fill="#fffaf1" stroke="{INK}" stroke-width="2"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('discipline', '決まりに沿って自分を律するイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','stand','short','neutral')}
<g transform="translate(430 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-50h140M-70-10h140M-70 30h100"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M-92-56l14 14 22-26"/><path d="M-92-16l14 14 22-26"/><path d="M-92 24l14 14 22-26"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M290 250h40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('disclosure', '封をあけて中身を公開するイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-90-60h180v120h-180z" class="paper"/>
  <path d="M-90-60l90 70 90-70" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(430 240)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-60" width="120" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-20h120M-60 10h100M-60 40h80"/></g>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('discomfort', 'かたい椅子で居心地が悪いイラスト。', f"""
<g transform="translate(330 300)">
  <path d="M-70-20h140v20h-140z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
  <path d="M-70-20h20v-70h-20z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
  <path d="M-56 0h12v50h-12zM44 0h12v50H44z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(360 230) scale(0.95)">{person(0,60,1.0,1,'coral','blue','stand','bob','sad')}</g>
{drop(420,190,0.8)}
<g class="corals" style="stroke-width:4"><path d="M250 240q-20 16-20 40"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('discretion', '自分の判断で選ぶ裁量のイラスト。', f"""
{person(160,346,1.2,1,'blue','blue','think','short','neutral')}
<g class="tealp o"><rect x="300" y="180" width="90" height="70"/><rect x="420" y="180" width="90" height="70"/></g>
<g class="teal o"><rect x="300" y="280" width="90" height="70"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M420 300l18 18 30-36"/></g>
<path d="M240 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('discrimination', '同じ資格なのに扱いを分けられるイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','stand','short','neutral')}
{person(400,346,1.2,1,'coral','gold','stand','bob','sad')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 190l20 20 34-40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 180l30 30M510 180l-30 30"/></g>
<g class="paper"><rect x="170" y="130" width="60" height="40"/><rect x="370" y="130" width="60" height="40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('disk', '円い板のディスクのイラスト。', f"""
<g transform="translate(300 230)">
  <circle r="130" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <circle r="34" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#8b98a6" stroke-width="3"><circle r="80"/><circle r="110"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('dismissal', '職を解かれて出て行くイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','point','short','flat')}
{person(420,346,1.15,1,'teal','gold','walk','bob','sad')}
<g transform="translate(280 210)">
  <path d="M-70-40h140v70h-140z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-40-20l80 40M40-20l-80 40"/></g>
</g>
<path d="M490 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('disorder', '整っていた並びが乱れるイラスト。', f"""
<g transform="translate(170 240)">
  <g class="teal o"><rect x="-70" y="-60" width="50" height="40"/><rect x="-70" y="-10" width="50" height="40"/><rect x="-70" y="40" width="50" height="40"/></g>
</g>
<g transform="translate(430 240)">
  <g class="coralp o"><rect x="-70" y="-60" width="50" height="40" transform="rotate(-16 -45 -40)"/><rect x="0" y="-20" width="50" height="40" transform="rotate(20 25 0)"/><rect x="-50" y="40" width="50" height="40" transform="rotate(8 -25 60)"/></g>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('disposal', 'いらないものを処分するイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-60-50h120v100h-120z" class="mutedfill" fill="#c9c6b8" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(430 290)">
  <path d="M-80 60h160l-16-140h-128z" fill="#8b8161" stroke="{INK}" stroke-width="3"/>
  <path d="M-90-90h180v20h-180z" fill="#6f6a4a"/>
</g>
<path d="M270 220q70-60 120 0" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('disruption', '流れが途切れて混乱するイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-230 0h180" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14"/>
  <path d="M50 0h180" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M-30-40l60 80M30-40l-60 80"/></g>
</g>
<g fill="{INK}" transform="translate(470 140)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('distinction', '二つのちがいをはっきり分けるイラスト。', f"""
<g transform="translate(170 240)"><circle r="70" class="teal o"/></g>
<g transform="translate(430 240)"><path d="M-70-70h140v140h-140z" class="coral o"/></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M300 140v200"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 380h-60M330 380h60"/></g>
""", ground=False, arrow=True)

add('distribution', '中心から各所に配って行きわたるイラスト。', f"""
{box(300,210,120,84,0,'gold')}
<g class="tealp o"><rect x="90" y="300" width="70" height="50"/><rect x="260" y="320" width="70" height="50"/><rect x="440" y="300" width="70" height="50"/></g>
<g class="a" marker-end="url(#ar)"><path d="M260 260l-120 40M300 270v40M340 260l120 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
