"""第74回: 恩恵・境界・重荷・計算など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('beast', '牙をもつ大きな獣のイラスト。', f"""
<g transform="translate(300 250)">
  <ellipse rx="130" ry="80" fill="#8b6f4e" stroke="{INK}" stroke-width="3"/>
  <circle cx="110" cy="-50" r="56" fill="#8b6f4e" stroke="{INK}" stroke-width="3"/>
  <path d="M84-92q-14-34 8-38 16-2 20 28z" fill="#8b6f4e" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><circle cx="126" cy="-62" r="6"/></g>
  <path d="M84-20h70l-10 24h-54z" fill="#6f5739"/>
  <g fill="#fffdf6"><path d="M96-20l8 20-16-14zM140-20l-8 20 16-14z"/></g>
  <g fill="#8b6f4e" stroke="{INK}" stroke-width="3"><rect x="-90" y="60" width="26" height="50"/><rect x="40" y="60" width="26" height="50"/></g>
  <path d="M-130-10q-60-30-70 20" fill="none" stroke="#8b6f4e" stroke-width="14" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('behalf', '本人の代わりに立って話すイラスト。', f"""
{person(200,346,1.2,1,'blue','blue','point','short','neutral')}
<g opacity=".4">{person(120,346,1.0,1,'coral','gold','stand','bob','neutral')}</g>
<g transform="translate(360 190)">
  <path d="M-80-50h160v80h-160z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-56" y="-26" width="112" height="16"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M150 250h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('being', '人としてそこに在ることを示したイラスト。', f"""
{person(300,346,1.4,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 10"><circle cx="300" cy="250" r="150"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bench', '腰かけるための長いベンチのイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-160-20h320v26h-320z" class="goldd o"/>
  <path d="M-160-60h320v26h-320z" class="goldd o"/>
  <path d="M-140 6h20v70h-20zM120 6h20v70h-20z" class="goldd o"/>
  <path d="M-150-100h20v40h-20zM130-100h20v40h-20z" class="goldd o"/>
</g>
{tree(120,320,0.6)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('benchmark', '比べるためのめじるしの線を引くイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o"><rect x="120" y="240" width="70" height="100"/><rect x="220" y="200" width="70" height="140"/><rect x="420" y="260" width="70" height="80"/></g>
<rect x="320" y="220" width="70" height="120" class="coral o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 9"><path d="M100 220h420"/></g>
""", ground=False)

add('benefit', '受け取って得になる分を示したイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','reach','short','smile')}
<g transform="translate(400 260)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="18" class="goldd o"/>
</g>
<path d="M330 250h-60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 190l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('besides', 'すでにあるものに、さらに付け加えるイラスト。', f"""
<g class="tealp o"><rect x="120" y="220" width="80" height="100"/><rect x="210" y="220" width="80" height="100"/></g>
<g fill="{INK}" transform="translate(340 270)"><rect x="-24" y="-6" width="48" height="12"/><rect x="-6" y="-24" width="12" height="48"/></g>
<g class="coral o"><rect x="410" y="220" width="80" height="100"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('beyond', '境の向こう側を示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-20-140h40v280h-40z" fill="#c9d3dc" class="o"/>
</g>
{person(170,346,1.05,1,'teal','blue','point','short','neutral')}
<g class="green o" opacity=".7"><path d="M340 340q60-40 120-20t120-10v50H340z"/></g>
<path d="M250 200h180" class="a" marker-end="url(#ar)"/>
<path d="M60 396h480" class="a"/>
""", ground=True, arrow=True)

add('bias', '天びんが片方に寄って偏るイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-6-40h12v60h-12z" class="ink"/>
  <g transform="rotate(-14)"><path d="M-170 20h340" fill="none" stroke="{INK}" stroke-width="7"/><path d="M-170 20v50M170 20v50" fill="none" stroke="{INK}" stroke-width="3"/></g>
</g>
<g transform="translate(120 250)"><circle r="34" class="coral o"/><circle cx="46" cy="16" r="34" class="coral o"/></g>
<g transform="translate(470 290)"><circle r="26" class="tealp o"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M290 350l30 30M320 350l-30 30"/></g>
""", ground=False)

add('biography', 'ある人の一生をつづった本のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-150-140h300v280h-300z" class="violet o"/>
  <path d="M-130-120h260v240h-260z" fill="#fffdf6" class="o"/>
  <g transform="translate(0 -50)">
    <circle r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
    <path d="M-40 60q0-50 40-50t40 50z" class="tealp o"/>
  </g>
  <g fill="{INK}"><rect x="-70" y="50" width="140" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70 84h140"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('bishop', '高い帽子と杖をもつ司教のイラスト。', f"""
{person(300,346,1.3,1,'violet','violet','carry','short','neutral')}
<g transform="translate(300 200)">
  <path d="M-24-70q24-30 48 0v56h-48z" class="violetp o"/>
</g>
<g transform="translate(390 250)">
  <path d="M-6-90h12v170h-12z" class="goldd o"/>
  <path d="M0-90q30-30 0-50-30 20 0 50z" class="gold o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('blade', 'よく切れる刃の部分を示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-20h240l60 20-60 20h-240z" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-160-20h-60v40h60z" class="goldd o"/>
  <path d="M20-12h110l40 12-40 12H20z" fill="#f7fbfe"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="300" y="200" width="200" height="100"/></g>
<path d="M420 160v30" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('blanket', 'ベッドをおおう毛布のイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-200-20h400v50h-400z" fill="#fffdf6" class="o"/>
  <path d="M-200 30h20v50h-20zM180 30h20v50h-20z" fill="#c9d3dc"/>
  <path d="M-60-30h260v-30h-260z" class="tealp o"/>
  <path d="M-60-30h260v50h-260z" class="teal o"/>
  <path d="M-200-20h100v-40h-100z" fill="#e8f4fb" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('blessing', '光が降りて祝福を受けるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#f6f0dc"/>
<g fill="#f7e6bd" opacity=".7"><path d="M300 40L120 400h360z"/></g>
{person(300,346,1.2,1,'violet','blue','up','short','smile')}
<g transform="translate(300 110)"><circle r="40" fill="#f7e6bd" stroke="#d9c286" stroke-width="3"/></g>
""", ground=False)

add('bombing', '空から爆撃を受けて町がこわれるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#8b98a6"/>
{plane(140,90,0.7,6)}
<g fill="{INK}"><ellipse cx="300" cy="180" rx="12" ry="24"/><ellipse cx="360" cy="230" rx="10" ry="20"/></g>
<g fill="#7d7a67" stroke="{INK}" stroke-width="3"><path d="M200 340v-90l50-20v110z"/><path d="M300 340v-70l50 20v50z"/><path d="M400 340v-100l60 40v60z"/></g>
<g class="corals" style="stroke-width:6"><path d="M420 200l30-24"/></g>
""", ground=False)

add('bond', '二人のあいだに強い結びつきがあるイラスト。', f"""
{person(220,346,1.2,1,'teal','blue','give','short','smile')}
{person(380,346,1.2,-1,'coral','gold','give','bob','smile')}
<path d="M290 250h20" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="8"><path d="M220 180q80-40 160 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bonus', '決まった分に上乗せが加わるイラスト。', f"""
<g transform="translate(220 280)">
  <path d="M-90-40h180v70h-180z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="20" class="goldd o"/>
</g>
<g fill="{INK}" transform="translate(360 270)"><rect x="-24" y="-6" width="48" height="12"/><rect x="-6" y="-24" width="12" height="48"/></g>
<g transform="translate(470 270)">
  <path d="M-50-30h100v60h-100z" class="gold o"/>
  <g class="golds" style="stroke-width:5"><path d="M0-50v-24M-56-40l-20-16"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('booking', '予約の欄に印を入れて席を確保するイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-130h380v260h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-190+c*95}-130v260"/>' for c in range(1,4))}{''.join(f'<path d="M-190 {-44+r*86}h380"/>' for r in range(2))}</g>
  <g class="coralp o"><rect x="-95" y="-44" width="95" height="86"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-70-10l16 16 30-34"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('boom', '売り上げが急に伸びる好況のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100h340M-170-110v210" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-150 80q100 0 150-180" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" marker-end="url(#ar)"/>
</g>
<g class="golds" style="stroke-width:6"><path d="M240 130l-24-18M300 100v-26"/></g>
""", ground=True, arrow=True)

add('boundary', '土地の境目に線が引かれるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-130h220v260h-220z" class="tealp o"/>
  <path d="M0-130h220v260H0z" class="goldp o"/>
  <path d="M0-130v260" fill="none" stroke="{INK}" stroke-width="8" stroke-dasharray="18 12"/>
</g>
<path d="M300 380v-30" class="a" marker-end="url(#ar)" transform="rotate(180 300 365)"/>
""", ground=False, arrow=True)

add('breakdown', '機械が壊れて動かなくなるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-110h280v220h-280z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="-50" cy="-30" r="40"/><circle cx="40" cy="40" r="26"/></g>
  <g class="coral o"><circle cx="90" cy="-70" r="14"/></g>
  <g class="muted"><path d="M0-140q30-40 0-70"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M470 160l40 40M510 160l-40 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('breast', '胸のふくらみの位置を示したイラスト。', f"""
<g transform="translate(300 250)">
  <circle cy="-130" r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-84 130q0-140 84-140t84 140z" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"><path d="M-40-30q40 30 80 0"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4" stroke-dasharray="10 8"><ellipse cx="300" cy="230" rx="70" ry="46"/></g>
<path d="M450 230h-70" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('brick', '積み上げたれんがのイラスト。', f"""
<g fill="#c07a5e" stroke="{INK}" stroke-width="3">
  {''.join(f'<rect x="{110+c*100+(50 if r%2 else 0)}" y="{300-r*50}" width="90" height="44"/>' for r in range(4) for c in range(4))}
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('broadband', '太い線で大量の信号が速く流れるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220-40h440v80h-440z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <g fill="{TONES['teal'][0]}">{''.join(f'<rect x="{-200+i*60}" y="-24" width="36" height="48"/>' for i in range(7))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 150h360"/></g>
<g class="a" marker-end="url(#ar)"><path d="M120 340h360"/></g>
""", ground=False, arrow=True)

add('broadcaster', '電波にのせて番組を流す放送局のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-50 100L0-100l50 200z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-6-140h12v40h-12z" class="ink"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M240 140q30 30 30 60t-30 60M280 110q46 46 46 90t-46 90"/></g>
<g transform="translate(450 250)">
  <path d="M-90-70h180v130h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-70-50h140v90h-140z" class="bluep o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('browser', 'ページを表示するブラウザーのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-200-140h400v50h-400z" fill="#c9d3dc" class="o"/>
  <g fill="{MUTED}"><circle cx="-170" cy="-115" r="10"/><circle cx="-140" cy="-115" r="10"/><circle cx="-110" cy="-115" r="10"/></g>
  <path d="M-80-128h250v26h-250z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
  <path d="M-170-70h340v200h-340z" fill="#fffdf6" class="o"/>
  <g fill="{MUTED}"><rect x="-140" y="-40" width="180" height="18"/><rect x="-140" y="0" width="140" height="18"/></g>
  <g class="tealp o"><rect x="60" y="-40" width="100" height="80"/></g>
</g>
""", ground=True)

add('buck', '一ドル札を示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-170-90h340v180h-340z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="46" fill="#d5e6c4" stroke="{TONES['green'][2]}" stroke-width="3"/>
  <g fill="{TONES['green'][2]}"><rect x="-10" y="-30" width="20" height="60"/></g>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="3"><rect x="-150" y="-70" width="300" height="140"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('buddy', '肩を組んだ相棒のイラスト。', f"""
{person(240,346,1.2,1,'teal','blue','give','short','smile')}
{person(360,346,1.2,-1,'coral','gold','give','bob','smile')}
<path d="M295 240h20" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g class="golds" style="stroke-width:5"><path d="M160 200l-24-18M440 200l24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('buffer', '間にはさんだ緩衝材が衝撃を受け止めるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-40-90h80v180h-80z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#d9c286" stroke-width="3">{''.join(f'<path d="M-40 {-70+i*40}h80"/>' for i in range(5))}</g>
</g>
<g transform="translate(150 250)">{box(150,250,120,100,0,'teal')}</g>
<g transform="translate(470 250)"><path d="M-40-90h80v180h-80z" fill="#c9d3dc" class="o"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M240 180h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('bulk', '大部分をまとめて扱うイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200-90h400v180h-400z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="teal o">{''.join(f'<rect x="{-190+c*54}" y="{-80+r*58}" width="46" height="50"/>' for r in range(3) for c in range(6))}</g>
  <g class="tealp o"><rect x="134" y="36" width="46" height="50"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 380h340"/></g>
""", ground=False, arrow=True)

add('bullet', '銃から放たれる弾丸のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-60-40q60-30 120 0v80q-60 30-120 0z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <path d="M60-40q60 20 60 40t-60 40z" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#8b5e3c" stroke-width="3"><path d="M-30-46v92M0-50v100"/></g>
</g>
<g class="muted"><path d="M120 240h-50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bunch', 'ひとまとめに束ねた花のイラスト。', f"""
<g transform="translate(300 280)">
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="6"><path d="M0 90q-30-70-60-120M0 90v-130M0 90q30-70 60-120"/></g>
  <g class="coral o"><circle cx="-60" cy="-120" r="30"/><circle cy="-140" r="30"/><circle cx="60" cy="-120" r="30"/></g>
  <g class="gold o"><circle cx="-60" cy="-120" r="12"/><circle cy="-140" r="12"/><circle cx="60" cy="-120" r="12"/></g>
  <path d="M-20 60h40v40h-40z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('burden', '背中に重荷を負って歩くイラスト。', f"""
<g transform="translate(280 346) rotate(10)">{person(0,0,1.3,1,'teal','blue','carry','short','flat')}</g>
{box(300,190,180,90,0,'gold')}
{drop(220,220,0.7)}
<g class="a" marker-end="url(#ar)"><path d="M470 190v60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('bureaucracy', '判子と書類が積み上がるお役所仕事のイラスト。', f"""
<g transform="translate(300 300)"><path d="M-220-20h440v26h-440z" class="goldd o"/></g>
<g class="paper" transform="translate(180 240)"><path d="M-70-60h140v90h-140z"/></g>
<g class="paper" transform="translate(300 230)"><path d="M-70-60h140v100h-140z"/></g>
<g class="paper" transform="translate(420 245)"><path d="M-70-60h140v85h-140z"/></g>
<g transform="translate(500 180)"><path d="M-30-24h60v34h-60z" class="ink"/><path d="M-12-60h24v36h-24z" class="ink"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('burial', '土に埋めて葬るイラスト。', f"""
<g fill="#8b6f4e"><path d="M60 300h480v100H60z"/></g>
<g transform="translate(300 260)">
  <path d="M-40-10h80v20h-80z" fill="#c9d3dc" class="o"/>
  <path d="M-10-80h20v70h-20z" fill="#c9d3dc" class="o"/>
</g>
<g fill="#6f5739"><ellipse cx="300" cy="320" rx="90" ry="24"/></g>
<g class="a" marker-end="url(#ar)"><path d="M450 250v60"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True, arrow=True)

add('by', '締め切りの時刻までに間に合わせるイラスト。', f"""
<g transform="translate(430 200)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <path d="M0-44v44l30 16" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
{person(170,346,1.1,1,'teal','blue','walk','short','neutral')}
<path d="M250 280h120" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 330l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('cabin', '森の中の小さな小屋のイラスト。', f"""
{tree(120,320,1.0)}{tree(510,320,0.9)}
<g transform="translate(310 280)">
  <path d="M-90 50h180V-30h-180z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <path d="M-110-30l110-70 110 70z" fill="#8b5e3c" stroke="{INK}" stroke-width="3"/>
  <path d="M-24 50V0h48v50z" class="goldd o"/>
  <g fill="none" stroke="#8b5e3c" stroke-width="2"><path d="M-90 0h180M-90 24h180"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('cabinet', '扉のついた戸棚のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-130h280v260h-280z" class="goldd o"/>
  <path d="M-120-110h110v100h-110zM10-110h110v100H10zM-120 10h110v100h-110zM10 10h110v100H10z" fill="#d9b476" stroke="{INK}" stroke-width="2"/>
  <g fill="{INK}"><circle cx="-20" cy="-60" r="6"/><circle cx="20" cy="-60" r="6"/><circle cx="-20" cy="60" r="6"/><circle cx="20" cy="60" r="6"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('cable', '太い電線のケーブルのイラスト。', f"""
<g fill="none" stroke="#41506a" stroke-width="30" stroke-linecap="round"><path d="M80 300q120-160 240 0t200-60"/></g>
<g fill="none" stroke="#8b98a6" stroke-width="10"><path d="M80 300q120-160 240 0t200-60"/></g>
<g transform="translate(520 240)">
  <path d="M-10-20h40v40h-40z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="26" y="-12" width="30" height="8"/><rect x="26" y="4" width="30" height="8"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('calculation', '筆算と電卓で計算するイラスト。', f"""
<g transform="translate(220 230)">
  <path d="M-130-130h260v260h-260z" class="paper"/>
  <g fill="{INK}"><rect x="-40" y="-100" width="90" height="12"/><rect x="-40" y="-60" width="90" height="12"/><rect x="-100" y="-24" width="200" height="6"/><rect x="-40" y="4" width="90" height="12"/></g>
</g>
<g transform="translate(460 250)">
  <path d="M-50-70h100v140h-100z" fill="#dfe6ea" class="o"/>
  <g fill="{INK}"><rect x="-34" y="-54" width="68" height="24"/>{''.join(f'<rect x="{-34+c*24}" y="{-16+r*26}" width="18" height="18"/>' for r in range(3) for c in range(3))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('canal', '人の手で掘った運河のイラスト。', f"""
<g class="green o" opacity=".85"><path d="M60 200h480v180H60z"/></g>
<path d="M60 250h480v80H60z" class="bluep o"/>
<g fill="none" stroke="{TONES['blue'][2]}" stroke-width="3" opacity=".8"><path d="M80 290h440"/></g>
<g fill="#dfe6ea" stroke="{INK}" stroke-width="2"><rect x="60" y="238" width="480" height="14"/><rect x="60" y="328" width="480" height="14"/></g>
<g transform="translate(360 270)">
  <path d="M-60 20h120l-20 26h-80z" class="tealp o"/>
  <path d="M-6-40h12v60h-12z" class="ink"/>
</g>
""", ground=False)

add('cancer', '体の中で異常な細胞が増えるイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="150" fill="#e7f6fb" opacity=".7" stroke="{INK}" stroke-width="3"/>
  <g class="tealp o"><circle cx="-80" cy="-40" r="26"/><circle cx="-30" cy="60" r="26"/><circle cx="80" cy="-70" r="26"/></g>
  <g class="coral o"><circle cx="30" cy="0" r="34"/><circle cx="80" cy="40" r="30"/><circle cx="10" cy="60" r="26"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="340" cy="240" r="80"/></g>
""", ground=False)

add('candle', '火のともったろうそくのイラスト。', f"""
{flame(300,180,1.1)}
<g transform="translate(300 300)">
  <path d="M-30-70h60v130h-60z" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/>
  <path d="M-4-86h8v16h-8z" class="ink"/>
  <path d="M-50 60h100v20h-100z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('canvas', '布を張った画布とイーゼルのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-140-120h280v200h-280z" fill="#fffdf6" stroke="{INK}" stroke-width="4"/>
  <path d="M-110-90h220v140h-220z" fill="#f7f3e8"/>
  <path d="M-150 80l-40 140h20l40-140zM150 80l40 140h-20l-40-140z" class="goldd o"/>
  <path d="M-10 80h20v140h-20z" class="goldd o"/>
</g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('capability', 'その機械にできることの幅を示したイラスト。', f"""
<g transform="translate(220 250)">
  <path d="M-110-90h220v180h-220z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="-40" cy="-20" r="34"/><circle cx="40" cy="30" r="24"/></g>
</g>
<g class="teal o"><rect x="400" y="150" width="60" height="50"/></g>
<g class="tealp o"><rect x="400" y="220" width="60" height="50"/><rect x="400" y="290" width="60" height="50"/></g>
<g class="a" marker-end="url(#ar)"><path d="M340 180h50M340 245h50M340 310h50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
