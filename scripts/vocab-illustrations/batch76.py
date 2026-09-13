"""第76回: 通勤・集中・合意・中核など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('commodity', '市場で売り買いされる産物のイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-220-30h440v40h-440z" class="goldd o"/>
</g>
<g transform="translate(150 240)">
  <path d="M-60-20h120l-14 40h-92z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g class="gold o"><ellipse cx="-20" cy="-30" rx="20" ry="12"/><ellipse cx="20" cy="-36" rx="20" ry="12"/></g>
</g>
<g transform="translate(320 240)">
  <path d="M-60-20h120l-14 40h-92z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g class="coral o"><circle cx="-20" cy="-30" r="18"/><circle cx="20" cy="-34" r="18"/></g>
</g>
{box(480,250,90,70,0,'teal')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('commute', '毎日電車で通って行き来するイラスト。', f"""
<g transform="translate(340 250)">
  <path d="M-160 60h320v-140h-320z" class="bluep o"/>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="3"><rect x="-120" y="-60" width="80" height="50"/><rect x="0" y="-60" width="80" height="50"/></g>
  <circle cx="-90" cy="76" r="24" class="ink"/><circle cx="90" cy="76" r="24" class="ink"/>
</g>
{person(140,340,0.95,1,'blue','blue','carry','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M120 160h360M480 200H120"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('companion', '道中をともにする連れのイラスト。', f"""
{person(230,346,1.2,1,'teal','blue','walk','short','smile')}
{person(340,346,1.2,1,'coral','gold','walk','bob','smile')}
<path d="M430 250h90" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M230 180q55-30 110 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('compassion', 'つらそうな相手に心を寄せるイラスト。', f"""
<g transform="translate(430 346) rotate(18)">{person(0,0,1.1,-1,'coral','gold','stand','bob','sad')}</g>
{person(220,346,1.2,1,'teal','blue','reach','short','sad')}
<path d="M300 260h60" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(310 170)">
  <path d="M0 34c-34-26-48-38-48-58a26 26 0 0 1 48-14 26 26 0 0 1 48 14c0 20-14 32-48 58z" class="coralp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('compensation', '損した分をお金で埋め合わせるイラスト。', f"""
<g transform="translate(160 250)">
  <g fill="#cfe0ea" stroke="{INK}" stroke-width="3"><path d="M-60 60l30-60 24 40z"/><path d="M20 60l30-40 20 40z"/></g>
</g>
<g fill="{INK}" transform="translate(300 250)"><rect x="-24" y="-6" width="48" height="12"/><rect x="-6" y="-24" width="12" height="48"/></g>
<g transform="translate(450 260)">
  <path d="M-70-30h140v60h-140z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="18" class="goldd o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('competence', '任せた仕事をきちんとこなす力のイラスト。', f"""
{person(200,346,1.25,1,'blue','blue','reach','short','smile')}
<g transform="translate(420 240)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-50h120M-60-10h120M-60 30h90"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M-84-56l14 14 22-26"/><path d="M-84-16l14 14 22-26"/><path d="M-84 24l14 14 22-26"/></g>
</g>
<path d="M290 240h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('completion', '最後の一片が入って完成するイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-100h280v200h-280z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="teal o">{''.join(f'<rect x="{-130+c*70}" y="{-90+r*95}" width="60" height="85"/>' for r in range(2) for c in range(4) if not (r==1 and c==3))}</g>
  <g class="coral o"><rect x="80" y="5" width="60" height="85"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 160l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('complexity', '線が入り組んで複雑になるイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80 0h160" fill="none" stroke="{TONES['teal'][0]}" stroke-width="7"/>
</g>
<g transform="translate(430 240)">
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5">
    <path d="M-90-60q60 60 0 120t90 0-60-120t60 60"/>
    <path d="M-60 40q80-40 140 20"/>
  </g>
</g>
<path d="M280 240h50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('complication', '順調な流れに、やっかいな要素が加わるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220 0h440" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10"/>
  <g transform="translate(20 0) rotate(24)"><path d="M-50-14h100v28h-100z" class="coral o"/></g>
  <g class="corals" style="stroke-width:5"><path d="M20-60v-26"/></g>
</g>
<g fill="{INK}" transform="translate(470 150)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('composition', '部品を組み合わせて全体をつくるイラスト。', f"""
<g transform="translate(160 240)">
  <g class="tealp o"><circle cx="-40" cy="-40" r="24"/><rect x="0" y="-60" width="50" height="44"/><path d="M-30 60l26-44 26 44z"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-90-80h180v160h-180z" fill="#fffdf6" class="o"/>
  <g class="tealp o"><circle cx="-50" cy="-40" r="24"/><rect x="0" y="-60" width="50" height="44"/><path d="M-30 50l26-44 26 44z"/></g>
</g>
<path d="M280 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('concentration', '一点に集中して取り組むイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(430 230)">
  <circle r="90" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
  <circle r="50" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
  <circle r="18" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M260 240h100"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('concession', '主張を一歩引いて譲るイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','give','short','neutral')}
{person(430,346,1.2,-1,'coral','gold','point','bob','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M360 230h-60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M250 300h-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('confession', '隠していたことを打ち明けるイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','stand','short','sad')}
<g transform="translate(400 200)">
  <path d="M-90-60h180v90h-180z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-60" y="-34" width="120" height="16"/><rect x="-60" y="-6" width="90" height="16"/></g>
</g>
{person(540,346,0.9,-1,'blue','blue','stand','bob','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('configuration', 'つまみと札の組み合わせで設定を表すイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-190-120h380v240h-380z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="8"><circle cx="-120" cy="-40" r="30"/><circle cx="-120" cy="50" r="30"/></g>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="3"><rect x="-40" y="-70" width="200" height="26"/><rect x="-40" y="-24" width="200" height="26"/><rect x="-40" y="22" width="200" height="26"/></g>
  <g class="teal o"><rect x="-40" y="-24" width="90" height="26"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('confirmation', '内容を照らし合わせて確認の印をつけるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-130h320v260h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-110-70h220M-110-30h220M-110 10h180"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="11" stroke-linecap="round"><path d="M-40 60l24 24 50-58"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('confrontation', '正面から向き合って対立するイラスト。', f"""
{person(190,346,1.25,1,'teal','blue','point','short','flat')}
{person(410,346,1.25,-1,'coral','gold','point','bob','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" marker-end="url(#ar)"><path d="M260 220h50M340 260h-50"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 150v200"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('confusion', '道しるべが入り乱れて混乱するイラスト。', f"""
<g transform="translate(340 210)">
  <path d="M-140-110h280v190h-280z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="6" marker-end="url(#ar)">
    <path d="M-100-70h80"/><path d="M100-30h-80"/><path d="M-40 10l60 50"/><path d="M60-70L-20-20"/>
  </g>
  <path d="M-14 80h28v90h-28z" class="ink"/>
</g>
{person(130,346,1.0,1,'teal','blue','think','short','flat')}
<g fill="{INK}" transform="translate(130 170)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('congregation', '集まって席につく人々のイラスト。', f"""
<g transform="translate(300 320)">
  <g class="goldd o">{''.join(f'<rect x="{-230+c*160}" y="{-20-r*70}" width="140" height="18"/>' for r in range(2) for c in range(3))}</g>
</g>
{person(160,300,0.7,1,'teal','blue','stand','short','smile')}
{person(320,300,0.7,1,'coral','gold','stand','bob','smile')}
{person(480,300,0.7,1,'gold','blue','stand','cap','smile')}
{person(240,230,0.7,1,'violet','blue','stand','short','smile')}
{person(400,230,0.7,1,'teal','gold','stand','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('conscience', '胸の中の良心が正しい方を示すイラスト。', f"""
{person(220,346,1.25,1,'teal','blue','stand','short','neutral')}
<g transform="translate(220 250)">
  <circle r="34" class="goldp o"/>
  <g class="golds" style="stroke-width:4"><path d="M0-50v-14M-34-34l-12-8M34-34l12-8"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M430 200l20 20 34-40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M430 320l30 30M460 320l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('consciousness', '目を覚まして意識が戻るイラスト。', f"""
<g transform="translate(170 320) rotate(-90)">{person(0,0,1.0,1,'teal','blue','stand','short','flat')}</g>
{person(430,346,1.15,1,'teal','blue','stand','short','smile')}
<path d="M270 250h80" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:5"><path d="M500 200l24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('consensus', '全員がうなずいて意見が一つになるイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','stand','short','smile')}
{person(300,346,1.1,1,'coral','gold','stand','bob','smile')}
{person(440,346,1.1,1,'gold','blue','stand','cap','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M140 190l14 14 24-30"/><path d="M280 190l14 14 24-30"/><path d="M420 190l14 14 24-30"/>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><path d="M150 130q150-50 300 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('conservation', '自然を囲って守り残すイラスト。', f"""
<g class="green o" opacity=".85"><path d="M60 300h480v70H60z"/></g>
{tree(200,300,1.1)}{tree(380,300,0.9)}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="5" stroke-dasharray="14 10"><rect x="120" y="150" width="360" height="180" rx="16"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M500 130l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('consideration', '大事な点として取り上げて考えるイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','think','short','neutral')}
<g transform="translate(430 220)">
  <path d="M-110-100h220v200h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-50h160M-80 30h160"/></g>
  <g class="coralp o"><rect x="-86" y="-20" width="172" height="40"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="290" r="12"/><circle cx="266" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('conspiracy', '陰で人目を避けて企むイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#3b4a63"/>
<g transform="translate(230 346)">{person(0,0,1.1,1,'violet','violet','reach','cap','flat')}</g>
<g transform="translate(370 346)">{person(0,0,1.1,-1,'blue','blue','reach','cap','flat')}</g>
<g transform="translate(300 200)">
  <path d="M-70-40h140v56h-140z" fill="#f2f6fa"/>
  <path d="M-20 16l-14 28 40-28z" fill="#f2f6fa"/>
  <g fill="{MUTED}"><circle cx="-26" cy="-12" r="7"/><circle cx="0" cy="-12" r="7"/><circle cx="26" cy="-12" r="7"/></g>
</g>
""", ground=False)

add('constantly', 'とぎれずに、ずっと続いているイラスト。', f"""
<path d="M60 250h480" fill="none" stroke="{TONES['teal'][0]}" stroke-width="16"/>
<g class="a" marker-end="url(#ar)"><path d="M100 350h400"/></g>
{drop(180,150,0.8)}{drop(300,150,0.8)}{drop(420,150,0.8)}
""", ground=False, arrow=True)

add('constituency', '選挙区の一帯とその有権者のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-130h400v260h-400z" class="paper"/>
  <path d="M-140-90q120-30 180 40t-40 140-160-20-20-160z" class="tealp o" opacity=".8"/>
  <path d="M-140-90q120-30 180 40t-40 140-160-20-20-160z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 9"/>
</g>
{person(430,340,0.7,1,'coral','gold','stand','bob','smile')}
{person(500,340,0.7,1,'teal','blue','stand','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('constitution', '国の基本を定めた憲法のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-140h320v280h-320z" class="violet o"/>
  <path d="M-140-120h280v240h-280z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-90" y="-90" width="180" height="20"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-90 {-40+i*34}h180"/>' for i in range(5))}</g>
  <g transform="translate(0 -130)"><path d="M-40 20l-8-44 24 18 24-30 24 30 24-18-8 44z" class="gold o"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('constraint', '両側から締められて動きが限られるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-240-100h140v200h-140zM100-100h140v200H100z" fill="#c9d3dc" class="o"/>
  <g class="teal o"><rect x="-70" y="-60" width="140" height="120"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M120 180h60M480 180h-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('consultant', '専門の助言を与える人のイラスト。', f"""
{person(430,346,1.2,-1,'blue','blue','point','short','neutral')}
{person(180,346,1.15,1,'coral','gold','think','bob','neutral')}
<g transform="translate(310 190)">
  <path d="M-80-50h160v80h-160z" fill="#fffdf6" class="o"/>
  <path d="M40 30l14 30-40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M-50-20h60M-50 4h80"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('contempt', '相手を見下してさげすむイラスト。', f"""
{person(200,346,1.3,1,'violet','blue','stand','short','flat')}
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M170 200l38 10"/></g>
{person(430,346,0.85,-1,'coral','gold','stand','bob','sad')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M270 220l100 60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('contender', '同じ座をねらう競争者のイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-50-40h100l-12 50a44 26 0 0 1-76 0z" class="gold o"/>
  <path d="M-20 20h40v26h-40z" class="goldd o"/>
</g>
{person(180,346,1.2,1,'teal','blue','up','cap','neutral')}
{person(420,346,1.2,-1,'coral','gold','up','bob','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M230 220l50-50M370 220l-50-50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('contention', '双方が言い張って争点になるイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','short','flat')}
{person(440,346,1.15,-1,'coral','gold','point','bob','flat')}
<g transform="translate(300 200)">
  <path d="M0-50l24 46 52 6-38 36 10 52-48-26-48 26 10-52-38-36 52-6z" class="coralp o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="5" marker-end="url(#ar)"><path d="M230 230h30M370 230h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('contrary', '向きがまったく逆のイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" marker-end="url(#ar)"><path d="M120 200h240"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14" marker-end="url(#ar)"><path d="M480 300H240"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 140v220"/></g>
""", ground=False, arrow=True)

add('contribution', '自分の分を出して全体に加えるイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','give','short','smile')}
<g transform="translate(420 280)">
  <path d="M-110-60h220v120h-220z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o"><rect x="-90" y="-10" width="60" height="60"/><rect x="-20" y="-10" width="60" height="60"/></g>
</g>
<g transform="translate(300 200)"><path d="M-30-30h60v60h-60z" class="teal o"/></g>
<path d="M340 200q60-20 90 30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('contributor', '原稿を寄せて載せてもらう人のイラスト。', f"""
{person(160,346,1.15,1,'coral','gold','give','bob','smile')}
<g transform="translate(300 240)">
  <path d="M-60-60h120v100h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-30h72M-36-6h72M-36 18h50"/></g>
</g>
<g transform="translate(460 240)">
  <path d="M-90-100h180v200h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-70" width="120" height="16"/></g>
  <path d="M-60-30h60v120h-60z" class="goldp o" opacity=".7"/>
</g>
<path d="M370 280h20" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('convenience', '手近にあってすぐ使えるイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','reach','short','smile')}
<g transform="translate(340 250)">
  <path d="M-50-50h100v100h-100z" class="teal o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M460 200l20 20 34-40"/></g>
<path d="M270 250h20" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('convention', '大勢が集まる党大会のイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-200-60h400v40h-400z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-120" y="-50" width="240" height="20"/></g>
</g>
<g transform="translate(300 220) scale(0.8)">{person(0,60,1.0,1,'blue','blue','up','short','neutral')}</g>
{person(130,346,0.7,1,'coral','gold','up','bob','smile')}
{person(220,346,0.7,1,'teal','blue','up','short','smile')}
{person(400,346,0.7,1,'gold','blue','up','cap','smile')}
{person(490,346,0.7,1,'violet','gold','up','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('conversion', '一つの形が別の形に変わるイラスト。', f"""
<g transform="translate(160 240)"><circle r="60" class="teal o"/></g>
<g transform="translate(430 240)"><path d="M-60-60h120v120h-120z" class="coral o"/></g>
<path d="M250 240h100" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M300 140v200"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('conviction', '法廷で有罪の判決が下るイラスト。', f"""
<g transform="translate(300 140)">
  <path d="M-90 40h180v20h-180z" class="goldd o"/>
  <path d="M-6-60h12v100h-12z" class="ink"/>
  <path d="M-70-60h140v10h-140z" class="ink"/>
  <g class="goldp o"><path d="M-70-50l-24 34h48z"/><path d="M70-50l-24 34h48z"/></g>
</g>
{person(420,346,1.2,-1,'violet','violet','stand','cap','sad')}
<g transform="translate(180 260) rotate(-24)">
  <path d="M-40-24h80v48h-80z" fill="#8b5e3c" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 24h20v70h-20z" class="goldd o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M300 300l34 34M334 300l-34 34"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('coordination', '複数の動きを合わせて回すイラスト。', f"""
<g transform="translate(300 230)">
  <g fill="none" stroke="{INK}" stroke-width="12"><circle cx="-90" r="50"/><circle cx="30" cy="40" r="36"/><circle cx="120" cy="-40" r="40"/></g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M-40 20h30M66 20h20"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 340l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('coordinator', '全体の段取りをまとめる人のイラスト。', f"""
{person(160,346,1.2,1,'blue','blue','point','bob','neutral')}
<g transform="translate(112 250) rotate(-10)"><path d="M-30-40h60v80h-60z" class="paper"/><g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-18-20h36M-18 0h36M-18 20h24"/></g></g>
{person(380,346,0.9,1,'teal','gold','reach','short','neutral')}
{person(490,346,0.9,1,'coral','blue','carry','cap','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M250 200h80M250 240h140"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('cop', '制服と帽子の警察官のイラスト。', f"""
{person(300,346,1.45,1,'blue','blue','stand','cap','neutral')}
<g transform="translate(300 236)"><path d="M-14-16l6 14 16 2-12 11 3 16-13-8-13 8 3-16-12-11 16-2z" class="gold o"/></g>
<g transform="translate(300 150)"><path d="M-40-8h80v10h-80z" class="bluep o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('copper', '赤みのある銅の板と線のイラスト。', f"""
<g transform="translate(210 250)">
  <path d="M-90-70h180v140h-180z" fill="#c07a4e" stroke="{INK}" stroke-width="3"/>
  <g fill="#ffffff" opacity=".5"><path d="M-60-70h40l-90 140h-40z"/></g>
</g>
<g fill="none" stroke="#c07a4e" stroke-width="12"><path d="M330 300q60-100 120-40t100-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('core', '果実の中心にある芯を示したイラスト。', f"""
<g transform="translate(300 230)">
  <circle r="130" class="coralp o"/>
  <path d="M-16-70h32v140h-32z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><ellipse cy="-20" rx="8" ry="12"/><ellipse cy="20" rx="8" ry="12"/></g>
  <path d="M0-130v-30" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<path d="M500 130l-140 70" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('correction', '誤りに赤を入れて直すイラスト。', f"""
<g transform="translate(290 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-130-90h260M-130-40h260M-130 60h260"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-130 6h120"/><path d="M-10-14h140v40h-140z"/></g>
</g>
<g transform="translate(500 320) rotate(28)"><path d="M-10-80h20v110h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
