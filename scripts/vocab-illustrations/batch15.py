"""第15回: 発明・招待・液体・印など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('initial', '一列に並んだ手順の中で、最初の一つに印がついているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{110+i*80}" cy="220" r="34"/>' for i in range(6))}
</g>
<circle cx="110" cy="220" r="34" class="coral o"/>
<path d="M110 130V90" class="a" marker-end="url(#ar)" transform="rotate(180 110 110)"/>
<path d="M144 220h430" class="muted"/>
<path d="M110 300v40" class="a"/>
""", ground=False, arrow=True)

add('innocent', '判決の場で罪がないと示され、手錠が外されるイラスト。', f"""
{person(230,346,1.15,1,'teal','blue','stand','short','smile')}
<g transform="translate(340 260)">
  <circle cx="-30" r="24" fill="none" stroke="{MUTED}" stroke-width="8"/>
  <circle cx="30" r="24" fill="none" stroke="{MUTED}" stroke-width="8"/>
  <path d="M-6 0h12" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="4 6"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M450 180l20 20 34-40"/></g>
<g class="corals" style="stroke-width:6"><path d="M410 260l30-30M440 260l-30-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('instrument', '弦を張った楽器と、目盛りのついた計器を並べたイラスト。', f"""
<g transform="translate(180 250) rotate(-10)">
  <path d="M0-60q40 0 40 34 0 20-14 26 14 10 14 30 0 36-40 36s-40 0-40-36q0-20 14-30-14-6-14-26 0-34 40-34z" class="goldp o"/>
  <circle cy="16" r="18" class="goldd o"/>
  <path d="M-6-60h12v-70h-12z" class="goldd o"/>
</g>
<g transform="translate(420 250)">
  <circle r="80" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0l44-40" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-56-56l-12-12M56-56l12-12M0-70v-14M-70 0h-14M70 0h14"/></g>
</g>
""", ground=True)

add('internal', '箱の外側と、切り開いて見せた内部の構造を並べたイラスト。', f"""
<g transform="translate(160 250)">{box(0,0,150,110,34,'gold')}</g>
<g transform="translate(430 250)">
  <path d="M-80-60h160v120h-160z" fill="#fffdf6" class="o"/>
  <g class="tealp o"><rect x="-56" y="-36" width="44" height="34"/><rect x="4" y="-36" width="44" height="34"/><rect x="-56" y="10" width="104" height="30"/></g>
  <path d="M-80-60h160v120h-160z" fill="none" class="a"/>
</g>
<path d="M280 250h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('invent', 'これまでなかった仕掛けを考え出して、初めて形にするイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','think','bun','smile')}
<g transform="translate(390 240)">
  <path d="M-100-70h200v140h-200z" fill="#dfe6ea" class="o"/>
  <circle cx="-40" cy="-20" r="30" fill="none" stroke="{INK}" stroke-width="5"/>
  <circle cx="30" cy="10" r="24" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M-40-20l70 30" class="a"/>
  <path d="M-100 30h200" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g transform="translate(250 150)">
  <circle r="34" class="goldp o"/>
  <path d="M-14 34h28v14h-28z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-48v-18M-40-26l-16-10M40-26l16-10"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('invisible', '足あとだけが残り、その主の姿は見えないイラスト。', f"""
<g fill="#c9bda6">
  <ellipse cx="150" cy="340" rx="12" ry="18"/><ellipse cx="200" cy="316" rx="11" ry="17"/>
  <ellipse cx="250" cy="292" rx="11" ry="17"/><ellipse cx="300" cy="270" rx="10" ry="16"/>
</g>
<g opacity=".18">{person(400,300,1.1,1,'teal','blue','walk','short','neutral')}</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8">
  <path d="M360 300q0-90 40-90t40 90"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('invite', '招待状を差し出して、集まりに来てほしいと伝えるイラスト。', f"""
<circle cx="300" cy="130" r="70" class="coralp"/>
{person(160,346,1.1,1,'teal','blue','give','bob','smile')}
{person(450,346,1.1,-1,'coral','gold','hold','short','smile')}
<g transform="translate(310 250)">
  <path d="M-56-36h112v72h-112z" class="paper"/>
  <path d="M-56-36L0 8l56-44" fill="none" class="a"/>
  <circle cy="6" r="11" class="coral o"/>
</g>
<path d="M380 200h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('item', '棚に並んだ商品の中の、一つ一つの品物を示したイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-200-20h400v20h-400z" class="goldp o"/>
  <g class="tealp o"><rect x="-180" y="-80" width="60" height="60"/><rect x="-100" y="-80" width="60" height="60"/></g>
  <g class="coralp o"><rect x="-20" y="-80" width="60" height="60"/><rect x="60" y="-80" width="60" height="60"/></g>
  <rect x="140" y="-80" width="60" height="60" class="violetp o"/>
</g>
<circle cx="330" cy="230" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
<path d="M330 320v30" class="a" marker-end="url(#ar)" transform="rotate(180 330 335)"/>
""", ground=True, arrow=True)

add('joke', '冗談を言って、二人で笑い合っているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','point','short','smile')}
{person(430,346,1.15,-1,'coral','gold','up','bob','smile')}
<g transform="translate(300 180)">
  <path d="M-64-40h128q14 0 14 14v40q0 14-14 14h-84l-24 20 6-20h-12q-14 0-14-14v-40q0-14 14-14z" class="paper"/>
  <path d="M-30-8q30 30 60 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M500 220l24-24M120 220l-24-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('junior', '背の高い先輩の横に、背の低い後輩が並んでいるイラスト。', f"""
{person(220,346,1.3,1,'teal','blue','stand','short','neutral')}
{person(400,346,0.85,1,'coral','gold','stand','bob','smile')}
<path d="M160 160h120M340 250h120" class="muted"/>
<path d="M140 160v186M470 250v96" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('kill', '水をやらなかった鉢植えが、枯れて倒れているイラスト。', f"""
<g transform="translate(180 320)">
  <path d="M-50-40h100l-14 60h-72z" class="coralp o"/>
  <path d="M0-40v-60" fill="none" stroke="{TONES['green'][2]}" stroke-width="7" stroke-linecap="round"/>
  <path d="M0-70c-34-8-44-30-44-30 30-8 44 30 44 30z" class="green o"/>
</g>
<g transform="translate(420 320)">
  <path d="M-50-40h100l-14 60h-72z" class="coralp o"/>
  <path d="M0-40q10-40-20-56" fill="none" stroke="#a08b62" stroke-width="7" stroke-linecap="round"/>
  <path d="M-20-96q-24 8-24 20 20 4 24-20z" fill="#c9b48c" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M280 260h60" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:6"><path d="M290 190l30 30M320 190l-30 30"/></g>
""", ground=True, arrow=True)

add('laboratory', '実験台と器具がそろった研究室を、広く見せたイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-250-30h500v24h-500z" fill="#dfe6ea" class="o"/>
  <path d="M-220-6v60M220-6v60" fill="none" stroke="{MUTED}" stroke-width="10"/>
</g>
<g transform="translate(150 260)">
  <path d="M-10-70h20v26l34 62H-44l34-62z" fill="#f4fbff" class="o"/>
  <path d="M-34 24h68l10 12H-44z" class="coralp o"/>
</g>
<g transform="translate(300 270)">
  <path d="M-14-80h28v66a14 14 0 0 1-28 0z" fill="#f4fbff" class="o"/>
  <path d="M-14-30h28v16a14 14 0 0 1-28 0z" class="greenp o"/>
</g>
<g transform="translate(440 250)">
  <circle r="46" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle r="24" class="bluep o"/>
  <path d="M0 46v40" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<path d="M60 130h480" class="muted"/>
""", ground=True)

add('lack', '必要な数に足りず、空きが残っているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{100+i*80}" y="200" width="60" height="60"/>' for i in range(4))}
</g>
<g class="muted">
  <rect x="420" y="200" width="60" height="60"/><rect x="500" y="200" width="60" height="60"/>
</g>
<path d="M100 300h360" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:7"><path d="M470 150l30 30M500 150l-30 30"/></g>
""", ground=False, arrow=True)

add('land', '飛行機が車輪を出して、滑走路に降りるイラスト。', f"""
{cloud(120,90,1.1)}
{plane(330,180,0.9,16,'teal')}
<path d="M0 330h600v70H0z" fill="#d8d3ca"/>
<path d="M0 330h600" class="a"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" stroke-dasharray="30 24"><path d="M0 365h600"/></g>
<path d="M150 120q140 60 240 180" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('level', '同じ高さにそろった三つの台と、水平を示す線のイラスト。', f"""
<g class="tealp o">
  <rect x="90" y="220" width="110" height="110"/><rect x="240" y="220" width="110" height="110"/><rect x="390" y="220" width="110" height="110"/>
</g>
<path d="M60 220h480" class="muted"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M60 200h480"/></g>
<path d="M60 350h480" class="a"/>
""", ground=False)

add('liquid', 'コップの中で、注いだ液体が水平な面をつくっているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="bluep"/>
<g transform="translate(260 240)">
  <path d="M-80-120h160l-16 240h-128z" fill="#f7fbfe" class="o"/>
  <path d="M-70-20h140l-12 140h-116z" class="bluep o"/>
  <path d="M-70-20h140" class="a"/>
</g>
<g transform="translate(430 240) rotate(20)">
  <path d="M-80-120h160l-16 240h-128z" fill="#f7fbfe" class="o" opacity=".5"/>
</g>
<path d="M350 130h-30" class="muted"/>
""", ground=True)

add('loyal', '同じ旗のもとに残り続け、味方から離れない人のイラスト。', f"""
<path d="M300 340V110" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
<path d="M308 116l80 24-80 24z" class="teal o"/>
{person(220,346,1.1,1,'teal','blue','stand','short','smile')}
{person(380,346,1.1,-1,'teal','blue','stand','bob','smile')}
<g opacity=".35">{person(520,346,1.0,-1,'coral','gold','walk','cap','neutral')}</g>
<path d="M470 260h60" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('magic', 'つえを一振りすると、何もない所から花が現れるイラスト。', f"""
<circle cx="300" cy="180" r="130" class="violetp" opacity=".5"/>
<g transform="translate(180 260) rotate(-30)">
  <path d="M-70-8h140v16H-70z" class="ink"/>
  <path d="M50-10h20v20H50z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(380 210)">
  <circle r="26" class="violet o"/>
  <g class="coral o"><circle cx="-40" cy="-22" r="20"/><circle cx="40" cy="-22" r="20"/><circle cx="0" cy="-46" r="20"/><circle cx="-28" cy="24" r="20"/><circle cx="28" cy="24" r="20"/></g>
  <circle r="16" class="gold o"/>
  <path d="M0 50v46" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M300 120l-14-24M460 150l24-16M280 300l-20 20"/></g>
""", ground=True)

add('mail', 'ポストに封筒を入れて、郵送しているイラスト。', f"""
<g transform="translate(400 260)">
  <path d="M-70 100V-40h140v140z" class="coral o"/>
  <path d="M-80-40a80 60 0 0 1 160 0z" class="coral o"/>
  <path d="M-40-20h80v16h-80z" class="ink"/>
  <path d="M-30 40h60v10h-60z" class="coralp o"/>
</g>
<g transform="translate(230 230) rotate(-10)">
  <path d="M-56-36h112v72h-112z" class="paper"/>
  <path d="M-56-36L0 8l56-44" fill="none" class="a"/>
</g>
<path d="M300 220h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('marine', '海の中を泳ぐ魚と海草を描いたイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#dbeaf8"/>
<path d="M0 340q120-40 240-10t360-20v90H0z" fill="#e7d9c4" stroke="{INK}" stroke-width="3"/>
<g transform="translate(240 200)">
  <path d="M-46 0c26-40 90-40 116 0-26 40-90 40-116 0z" class="teal o"/>
  <path d="M-46 0l-36-26v52z" class="teal o"/>
  <circle cx="44" cy="-6" r="3.6" class="ink"/>
</g>
<g transform="translate(430 260) scale(0.7)">
  <path d="M-46 0c26-40 90-40 116 0-26 40-90 40-116 0z" class="coral o"/>
  <path d="M-46 0l-36-26v52z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round">
  <path d="M120 350q-20-60 10-90M150 350q20-50-6-80"/>
</g>
<g fill="#ffffff" opacity=".6"><circle cx="330" cy="120" r="10"/><circle cx="356" cy="90" r="7"/></g>
""", ground=False)

add('mark', '紙の上に印をつけて、目立たせているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(260 240)">
  <path d="M-120-140h240v280h-240z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-90-90h180M-90-40h180M-90 10h180M-90 60h140"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"><path d="M-70-52l16 16 30-34"/></g>
</g>
{hand(430,180,-1)}
""", ground=True)

add('marry', '指輪を交わして、二人が夫婦になるイラスト。', f"""
<circle cx="300" cy="140" r="80" class="coralp"/>
{person(200,346,1.15,1,'violet','violet','give','bob','smile')}
{person(400,346,1.15,-1,'blue','blue','give','short','smile')}
<g transform="translate(300 250)">
  <circle cx="-18" r="20" fill="none" stroke="{TONES['gold'][0]}" stroke-width="7"/>
  <circle cx="18" r="20" fill="none" stroke="{TONES['gold'][0]}" stroke-width="7"/>
</g>
<g transform="translate(300 180)"><path d="M0 24l-28-34 14-16 14 14 14-14 14 16z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('matter', '天びんの片方に重いものを載せ、重要さを示したイラスト。', f"""
<path d="M300 340V140" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M250 356h100" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>
<path d="M150 168h300" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round" transform="rotate(-10 300 168)"/>
<circle cx="300" cy="150" r="13" class="teal o"/>
{box(170,240,90,66,0,'gold')}
<path d="M430 130h60v14h-60z" class="paper"/>
<path d="M120 320h360" class="muted"/>
""", ground=True)

add('medium', '大・中・小の三つのコップのうち、中くらいの一つを選ぶイラスト。', f"""
<g transform="translate(150 280)">
  <path d="M-60-120h120l-12 200h-96z" fill="#f7fbfe" class="o"/>
</g>
<g transform="translate(300 290)">
  <path d="M-46-90h92l-10 150h-72z" fill="#f7fbfe" class="o"/>
</g>
<g transform="translate(440 300)">
  <path d="M-34-60h68l-8 100h-52z" fill="#f7fbfe" class="o"/>
</g>
<circle cx="300" cy="240" r="76" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"/>
<path d="M300 130v30" class="a" marker-end="url(#ar)" transform="rotate(180 300 145)"/>
""", ground=True, arrow=True)

add('mention', '話の途中で、ある名前に軽く触れているイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','stand','short','neutral')}
<g transform="translate(370 200)">
  <path d="M-100-50h200q16 0 16 16v54q0 16-16 16h-140l-26 22 6-22h-40q-16 0-16-16v-54q0-16 16-16z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-20h60M30-20h60M-70 8h40M60 8h30"/></g>
  <path d="M0-30h24v40H0z" class="coralp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('may', '二つの道のどちらもありえることを、点線で示したイラスト。', f"""
<circle cx="100" cy="200" r="24" class="teal o"/>
<path d="M130 190q120-90 220-80t150 20" class="muted" marker-end="url(#ar)"/>
<path d="M130 220q120 100 220 90t150-20" class="muted" marker-end="url(#ar)"/>
<g fill="{INK}"><path d="M280 60q0-30 30-30t30 30q0 20-24 26v14h-12v-24q26-2 26-16 0-14-20-14t-20 12z"/><circle cx="310" cy="126" r="7"/></g>
""", ground=False, arrow=True)

add('humanitarian', '被災地へ食料と水を届けている支援のイラスト。', f"""
<circle cx="300" cy="130" r="70" class="coralp"/>
<g transform="translate(300 176)"><path d="M0 30l-34-42 16-20 18 18 18-18 16 20z" class="coral o"/></g>
{person(150,346,1.05,1,'teal','blue','carry','bob','smile')}
{box(230,286,80,58,0,'gold')}
{person(450,346,1.05,-1,'gold','violet','hold','short','sad')}
<path d="M300 280h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('infamous', '割れた窓の写真が大きく貼り出され、悪い評判が広がっているイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <path d="M-100-80h200v120h-200z" class="bluep o"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-40-80l30 60-40 40M40-80l-20 70 50 30"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M-100 60h200"/></g>
</g>
<g class="corals" opacity=".9" style="stroke-width:5">
  <path d="M440 180q26 26 26 40t-26 40"/><path d="M480 160q34 34 34 60t-34 60"/>
</g>
""", ground=True)

add('instrumental', '大きな歯車を動かすのに欠かせない、小さな歯車のイラスト。', f"""
<g transform="translate(360 230)">
  <circle r="110" fill="none" stroke="{TONES['teal'][0]}" stroke-width="24"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="14">
    {''.join(f'<path d="M0 -110v-24" transform="rotate({i*45})"/>' for i in range(8))}
  </g>
  <circle r="24" class="teald o"/>
</g>
<g transform="translate(170 300)">
  <circle r="54" fill="none" stroke="{TONES['coral'][0]}" stroke-width="18"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="11">
    {''.join(f'<path d="M0 -54v-18" transform="rotate({i*60})"/>' for i in range(6))}
  </g>
  <circle r="14" class="coral o"/>
</g>
<path d="M170 220a120 120 0 0 1 80-40" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('intended', '狙った的の中心へ、矢がまっすぐ向かっているイラスト。', f"""
<g transform="translate(420 220)">
  <circle r="100" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle r="72" class="coralp o"/><circle r="44" fill="#fffdf6" stroke="{INK}" stroke-width="3"/><circle r="18" class="coral o"/>
</g>
<path d="M80 300L380 230" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
<path d="M380 230l-24-12 4 24z" class="ink"/>
<path d="M80 300l-18-14 6 30z" class="goldp o"/>
<path d="M140 340q80-40 240-60" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('legendary', '語り継がれる英雄の像が、台の上に立っているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="goldp"/>
<g transform="translate(300 300)">
  <path d="M-110 60h220v-40h-220z" class="goldp o"/>
  <path d="M-90 20h180v-20h-180z" class="goldd o"/>
</g>
<g transform="translate(300 280) scale(1.15)">{person(0,0,1.0,1,'gold','gold','up','cap','neutral')}</g>
<g class="golds" style="stroke-width:4"><path d="M180 180l-24-24M420 180l24-24M170 260h-30M430 260h30"/></g>
""", ground=True)

add('disabled', '車いすを使う人のために、段差にスロープがついているイラスト。', f"""
<path d="M300 330h300v70H300z" class="ground"/>
<path d="M100 330h200l-100-60z" fill="none" stroke="none"/>
<path d="M60 400h240l60-70H120z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
<g transform="translate(360 290)">
  <circle cx="0" cy="30" r="40" fill="none" stroke="{INK}" stroke-width="8"/>
  <circle cx="-40" cy="52" r="14" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-30-10h40v40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="-30" cy="-40" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-54-48q4-26 26-26 22 0 26 24-14-8-28-2-10-6-24 4z" fill="{HAIR}"/>
</g>
<path d="M180 260q60-20 120-10" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(' '.join(W)); print(sheet(W))
