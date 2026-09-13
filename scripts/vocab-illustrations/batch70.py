"""第70回: のど・翻訳・透明・緊急など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('thoughtful', '相手のことを考えて、そっと差し出すイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','give','short','smile')}
{person(430,346,1.15,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(310 250)">
  <path d="M-40-30h80v50h-80z" class="goldp o"/>
  <path d="M-4-40h8v10h-8z" class="coral o"/>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="150" cy="200" r="12"/><circle cx="128" cy="222" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('thrilled', '胸がおどるほど、わくわくするイラスト。', f"""
<g transform="translate(280 330) rotate(-8)">{person(0,0,1.35,1,'coral','gold','up','bob','smile')}</g>
<g class="corals" style="stroke-width:6"><path d="M150 190l-30-24M400 190l30-24"/></g>
<g transform="translate(280 130)">
  <path d="M0 36c-36-28-50-40-50-58a26 26 0 0 1 50-14 26 26 0 0 1 50 14c0 18-14 30-50 58z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('throat', '首の中を通るのどを示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-40-140q80-30 130 40 30 50-10 100t-40 60l-14 60h-66V60q-40-20-40-70 0-90 80-110z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="30" cy="-60" r="5" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><ellipse cx="288" cy="290" rx="40" ry="60"/></g>
<path d="M430 290h-90" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('throughout', '端から端まで、ずっと同じ印が続くイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-230-40h460v80h-460z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="teal o">{''.join(f'<rect x="{-215+i*64}" y="-26" width="50" height="52"/>' for i in range(7))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M70 340h460M530 340H70"/></g>
""", ground=False, arrow=True)

add('till', '始まりから終わりの時刻までを示したイラスト。', f"""
<g transform="translate(160 230)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <path d="M0-44v44l30 16" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g transform="translate(440 230)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <path d="M0-44v44l-30 16" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<path d="M240 340h120" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M440 320v40"/></g>
""", ground=False, arrow=True)

add('timely', 'ちょうどよい時に届くイラスト。', f"""
<g transform="translate(430 200)">
  <circle r="74" fill="#fffdf6" class="o"/>
  <path d="M0-46v46l32 18" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
{person(180,346,1.15,1,'teal','blue','give','short','smile')}
<g transform="translate(300 250)"><path d="M-46-30h92v54h-92z" class="paper"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M290 150l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('tin', 'ブリキの缶のイラスト。', f"""
<g transform="translate(300 250)">
  <ellipse cy="-90" rx="90" ry="26" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-90-90v130a90 26 0 0 0 180 0V-90z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <g fill="#fffdf6"><rect x="-60" y="-40" width="120" height="40"/></g>
  <g fill="#ffffff" opacity=".5"><path d="M-70-70q20 60 0 120"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('toe', '足の先の指を示したイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-120-20q-20-60 30-60t60 30l60 20q40 10 40 30t-40 20h-130q-20 0-20-40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="{SKIN}" stroke="{SKINL}" stroke-width="2"><circle cx="100" cy="6" r="14"/><circle cx="130" cy="10" r="12"/><circle cx="156" cy="16" r="10"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="430" cy="300" r="56"/></g>
<path d="M470 190l-40 50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('tongue', '口の中の舌を示したイラスト。', f"""
{face(280,200,110,'flat')}
<g transform="translate(280 250)">
  <path d="M-50-10q50-26 100 0 0 40-50 60t-50-60z" fill="#8b4a3e"/>
  <path d="M-30 10q30 40 60 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="280" cy="270" r="60"/></g>
<path d="M450 270h-100" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('touch', '指先が物に触れるイラスト。', f"""
{hand(240,170,1)}
<g transform="translate(400 280)">
  <path d="M-90-60h180v120h-180z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><circle cx="310" cy="230" r="26"/></g>
<path d="M270 210l30 20" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('tough', 'たたいても割れない、丈夫なイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-110-70h220v140h-220z" fill="#8b98a6" stroke="{INK}" stroke-width="4"/>
</g>
<g transform="translate(300 140) rotate(-18)">
  <path d="M-70-30h140v50h-140z" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 20h20v90h-20z" class="goldd o"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M180 210l-26-18M420 210l26-18"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 300l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('towards', 'そちらの方へ向かって進むイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','walk','short','neutral')}
<path d="M240 250h180" class="a" marker-end="url(#ar)"/>
<g transform="translate(490 250)">
  <path d="M0 46c-34-46-46-64-46-82a46 46 0 0 1 92 0c0 18-12 36-46 82z" class="coral o"/>
  <circle cy="-38" r="15" fill="#fffdf6"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('toxic', 'どくろの印がついた、有毒な液のイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-80-70h160l-16 160h-128z" fill="#e2eee2" stroke="{INK}" stroke-width="3"/>
  <path d="M-34-100h68v30h-68z" class="ink"/>
  <g transform="translate(0 30)">
    <circle r="40" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
    <g fill="{INK}"><circle cx="-14" cy="-8" r="8"/><circle cx="14" cy="-8" r="8"/><rect x="-5" y="8" width="10" height="12"/></g>
    <path d="M-20 26h40" fill="none" stroke="{INK}" stroke-width="4"/>
  </g>
</g>
{drop(460,220,1.0,'green')}
<g class="corals" style="stroke-width:5"><path d="M430 140q26 20 26 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('tragic', '取り返しのつかない悲しい結末のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#8b98a6"/>
<g fill="none" stroke="#cfd8e0" stroke-width="4" stroke-linecap="round">{''.join(f'<path d="M{100+i*50} 80l-16 50"/>' for i in range(9))}</g>
<g transform="translate(300 340) rotate(8)">{person(0,0,1.15,1,'blue','blue','stand','short','sad')}</g>
<g transform="translate(430 300)">
  <path d="M-40-10h80v20h-80z" fill="#6f7c8c"/>
  <path d="M-10-70h20v60h-20z" fill="#6f7c8c"/>
</g>
{drop(360,240,0.8)}
""", ground=False)

add('translation', '別の言葉に置きかえるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-70" y="-60" width="140" height="16"/><rect x="-70" y="-20" width="110" height="16"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="{TONES['teal'][0]}"><rect x="-70" y="-60" width="140" height="16"/><rect x="-70" y="-20" width="90" height="16"/></g>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('transparent', '向こう側が透けて見えるイラスト。', f"""
<g transform="translate(430 250)"><circle r="60" class="coral o"/></g>
<g transform="translate(300 240)">
  <path d="M-140-130h280v260h-280z" fill="#e7f6fb" opacity=".55" stroke="{INK}" stroke-width="3"/>
  <path d="M-110-100l60 0-140 200h-40z" fill="#ffffff" opacity=".5"/>
</g>
{person(140,346,1.0,1,'teal','blue','point','short','smile')}
<path d="M200 250h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('tremendous', 'とてつもなく大きな量を示したイラスト。', f"""
<path d="M60 350h480" class="a"/>
<g class="tealp o"><rect x="100" y="300" width="60" height="50"/></g>
<rect x="220" y="70" width="200" height="280" class="coral o"/>
<g class="a" marker-end="url(#ar)"><path d="M480 340V80"/></g>
{person(100,350,0.5,1,'teal','blue','up','short','surprised')}
""", ground=False, arrow=True)

add('trend', '流行の線が右上に伸びるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100h340M-170-110v210" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-150 70q80 10 130-50t150-70" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M480 120l24-18"/></g>
""", ground=True, arrow=True)

add('tribal', '部族のしるしをまとった人たちのイラスト。', f"""
{person(180,346,1.2,1,'gold','coral','stand','bob','neutral')}
{person(300,346,1.2,1,'gold','coral','stand','short','neutral')}
{person(420,346,1.2,1,'gold','coral','stand','cap','neutral')}
<g fill="{TONES['coral'][0]}"><circle cx="180" cy="250" r="8"/><circle cx="300" cy="250" r="8"/><circle cx="420" cy="250" r="8"/></g>
<g transform="translate(300 130)">
  <path d="M-60-30h120v50h-120z" class="goldp o"/>
  <g fill="{TONES['coral'][0]}"><circle cx="-30" cy="-4" r="7"/><circle cx="0" cy="-4" r="7"/><circle cx="30" cy="-4" r="7"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('troubled', '問題を抱えて、頭を悩ませるイラスト。', f"""
{person(200,346,1.2,1,'blue','blue','think','short','sad')}
<g transform="translate(430 200)">
  <path d="M-120-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-30-20l60 50M30-20l-60 50"/></g>
</g>
{drop(260,230,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('trustworthy', '任せても大丈夫だと印がつくイラスト。', f"""
{person(220,346,1.25,1,'blue','blue','stand','short','smile')}
<g transform="translate(430 230)">
  <path d="M0-90q60 24 60 70 0 60-60 84-60-24-60-84 0-46 60-70z" fill="#cfe6d6" stroke="{TONES['green'][2]}" stroke-width="4"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-24 10l18 20 34-40"/></g>
</g>
<path d="M310 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('truth', 'ふたを開けて、本当のことが現れるイラスト。', f"""
<g transform="translate(180 250)" opacity=".5">
  <path d="M-80-40h160v140h-160z" fill="#dfe6ea" class="o"/>
  <path d="M-90-60h180v20h-180z" fill="#c9d3dc"/>
</g>
<g transform="translate(430 250)">
  <path d="M-80-40h160v140h-160z" fill="#fffdf6" class="o"/>
  <path d="M-90-90q90-40 180 0" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
  <g class="gold o"><circle cy="20" r="40"/></g>
  <g class="golds" style="stroke-width:5"><path d="M0-40v-20M-50-20l-20-14M50-20l20-14"/></g>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('tube', '絞り出して使うチューブのイラスト。', f"""
<g transform="translate(280 260)">
  <path d="M-140-50h240v100h-240z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-160-50l20-20v140l-20-20z" fill="#cfe0ea" stroke="{INK}" stroke-width="3"/>
  <path d="M100-30h50v60h-50z" class="teal o"/>
  <path d="M150-16h30v32h-30z" class="teald o"/>
</g>
<path d="M470 250q10 30 6 50" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10" stroke-linecap="round"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('tyre', 'ゴムのタイヤのイラスト。', f"""
<g transform="translate(300 230)">
  <circle r="140" class="ink"/>
  <circle r="80" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <circle r="30" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
  <g fill="#41506a">{''.join(f'<rect x="-8" y="-138" width="16" height="26" transform="rotate({i*30})"/>' for i in range(12))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('ultimate', 'これ以上ない最後の段に届くイラスト。', f"""
<g class="goldd o">{''.join(f'<rect x="{90+i*80}" y="{320-i*50}" width="80" height="{50+i*50}"/>' for i in range(5))}</g>
<g transform="translate(450 100)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
{person(450,120,0.7,1,'coral','blue','up','short','smile')}
<path d="M120 250l300-140" class="a" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('unacceptable', '許せる範囲を外れていて、認められないイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-220-20h440v40h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-100-20h200v40h-200z" class="greenp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M-100-60v100M100-60v100"/></g>
  <circle cx="180" r="22" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M450 150l34 34M484 150l-34 34"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('unconscious', '倒れて意識をなくしているイラスト。', f"""
<g transform="translate(300 320) rotate(-90)">{person(0,0,1.2,1,'teal','blue','stand','short','flat')}</g>
<g fill="none" stroke="{INK}" stroke-width="3"><path d="M232 258q8 8 16 0M256 258q8 8 16 0"/></g>
<g fill="{MUTED}" transform="translate(400 200)">
  <path d="M0-20h30l-30 26h30" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M44-46h24l-24 22h24" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('underlying', '表に見える形の下に隠れた土台があるイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-140-80h280v120h-280z" class="tealp o"/>
</g>
<g transform="translate(300 320)">
  <path d="M-180-40h360v70h-360z" class="teald o"/>
</g>
<path d="M470 300v-60" class="a" marker-end="url(#ar)" transform="rotate(180 470 270)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M120 280h360"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('underwear', '上着の下に着る下着のイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-70-90h140v60h-140z" class="bluep o"/>
  <path d="M-60-30h120v130h-120z" class="blue o"/>
</g>
<g transform="translate(430 260)">
  <path d="M-70-30h140v40h-140z" fill="#fffdf6" class="o"/>
  <path d="M-70 10h60l10 50h-60zM10 10h60l-10 50h-60z" fill="#fffdf6" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('unexpected', '思ってもいなかったものが出てくるイラスト。', f"""
<g transform="translate(400 250)">
  <path d="M-90-20h180v110h-180z" class="goldd o"/>
  <path d="M-100-30h200v20h-200z" class="goldp o" transform="rotate(-14 -100 -30)"/>
  <g transform="translate(20 -70)"><path d="M0-50l24 46 52 6-38 36 10 52-48-26-48 26 10-52-38-36 52-6z" class="coral o"/></g>
</g>
{person(150,346,1.1,1,'teal','blue','up','short','surprised')}
<path d="M230 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('unfortunate', '運悪く、思わぬつまずきに遭うイラスト。', f"""
<g transform="translate(280 320) rotate(-24)">{person(0,0,1.2,1,'coral','blue','up','short','surprised')}</g>
<g fill="#c8bfa4" stroke="{INK}" stroke-width="2"><path d="M370 350q20-30 40 0z"/></g>
<g class="corals" style="stroke-width:5"><path d="M200 200l-24-18M210 240h-28"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 170l30 30M500 170l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('unfortunately', '運悪く、手にした品が落ちてしまうイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','reach','short','sad')}
<g transform="translate(360 300) rotate(24)"><path d="M-50-30h100v60h-100z" class="goldd o"/></g>
<path d="M280 200l60 70" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 170l30 30M500 170l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('union', '働く人たちが集まって組合をつくるイラスト。', f"""
{person(180,346,1.1,1,'teal','blue','up','cap','neutral')}
{person(300,346,1.1,1,'coral','blue','up','short','neutral')}
{person(420,346,1.1,1,'gold','blue','up','bob','neutral')}
<g transform="translate(300 140)">
  <path d="M-4-40h8v60h-8z" class="ink"/>
  <path d="M4-36h90v46H4z" class="coralp o"/>
</g>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="120" y="200" width="360" height="160" rx="16"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('unique', 'ほかに同じものがない、ただ一つの形のイラスト。', f"""
<g class="tealp o">{''.join(f'<circle cx="{110+i*70}" cy="290" r="26"/>' for i in range(6))}</g>
<g transform="translate(300 160)">
  <path d="M0-60l30 54 60 8-44 42 10 60-56-30-56 30 10-60-44-42 60-8z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><circle cx="300" cy="170" r="90"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('universal', 'どの地域にも当てはまることを示したイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="130" class="bluep o"/>
  <g class="green o"><path d="M-100-30q60-40 100-10t90-20v40q-60 30-100 0t-90 20z"/><path d="M-50 50q50-30 90 0t70-10v40q-50 30-90 0t-70 10z"/></g>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="3"><ellipse rx="130" ry="56"/><ellipse rx="56" ry="130"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 340l20 20 34-40"/></g>
""", ground=False)

add('unknown', '名前がわからないままの人物のイラスト。', f"""
<g transform="translate(300 240)">
  <circle cy="-60" r="52" fill="#7f8ea6"/>
  <path d="M-80 100q0-100 80-100t80 100z" fill="#7f8ea6"/>
  <g fill="#fffdf6"><path d="M-16-84q0-28 22-28t22 28q0 16-16 20v14h-12v-22q14-4 14-16t-9-9-9 13z"/><rect x="-2" y="-32" width="12" height="12"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="180" y="140" width="240" height="220" rx="16"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('unprecedented', 'これまでになかった高さに届くイラスト。', f"""
<path d="M60 350h480" class="a"/>
<g class="tealp o">{''.join(f'<rect x="{100+i*66}" y="{280-i*10}" width="50" height="{70+i*10}"/>' for i in range(5))}</g>
<rect x="430" y="70" width="100" height="280" class="coral o"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M80 240h480"/></g>
<g class="golds" style="stroke-width:6"><path d="M410 60l-26-20M550 60l26-20"/></g>
""", ground=False)

add('upcoming', 'すぐ先の予定が近づいてくるイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-180-130h360v260h-360z" class="paper"/>
  <path d="M-180-130h360v46h-360z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-180+c*90}-84v214"/>' for c in range(1,4))}{''.join(f'<path d="M-180 {-14+r*70}h360"/>' for r in range(2))}</g>
  <circle cx="0" cy="20" r="28" class="coral o"/>
</g>
<path d="M500 110l-100 70" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('upper', '二段のうち上の段を示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-120h320v110h-320z" class="teal o"/>
  <path d="M-160 10h320v110h-320z" class="tealp o"/>
</g>
<path d="M470 110v40" class="a" marker-end="url(#ar)" transform="rotate(180 470 130)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('urban', 'ビルが立ち並ぶ都市のイラスト。', f"""
<g transform="translate(300 260)">
  <g fill="#dfe6ea" stroke="{INK}" stroke-width="3">
    <rect x="-230" y="-80" width="90" height="160"/><rect x="-130" y="-140" width="100" height="220"/>
    <rect x="-20" y="-100" width="90" height="180"/><rect x="80" y="-170" width="100" height="250"/><rect x="190" y="-60" width="60" height="140"/>
  </g>
  <g fill="#cfe6f5">{''.join(f'<rect x="{-215+c*30}" y="{-60+r*40}" width="20" height="24"/>' for r in range(3) for c in range(2))}{''.join(f'<rect x="{-115+c*30}" y="{-120+r*40}" width="20" height="24"/>' for r in range(4) for c in range(2))}{''.join(f'<rect x="{95+c*30}" y="{-150+r*40}" width="20" height="24"/>' for r in range(5) for c in range(2))}</g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('urgent', '赤い印がついて、急ぎだと示すイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-90-40h180M-90 0h180M-90 40h140"/></g>
  <g fill="{TONES['coral'][0]}"><path d="M-30-100h60v44h-60zM-30-44h60v20h-60z"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><rect x="-150" y="-130" width="300" height="260"/></g>
</g>
<g transform="translate(490 130)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M0-22v22l16 10" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
""", ground=True)

add('useless', '刃が欠けて、道具として使えないイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-20h240l40 20-40 20h-240z" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-160-20h-40v40h40z" class="goldd o"/>
  <g fill="#fffaf1"><path d="M20-20l20 20-20 20-20-20z"/><path d="M80-20l16 20-16 20-16-20z"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M270 130l60 60M330 130l-60 60"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('vague', '輪郭がぼやけて、はっきりしないイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="90" fill="#cfe0ea" opacity=".6"/>
  <circle r="110" fill="#dbe6ee" opacity=".4"/>
  <circle r="130" fill="#e6eef4" opacity=".3"/>
</g>
<g fill="{INK}" transform="translate(470 320)">
  <path d="M0 0q0-26 20-26t20 26q0 14-14 18v12h-10v-20q14-4 14-14t-8-8-8 12z"/><rect x="12" y="42" width="10" height="10"/>
</g>
""", ground=False)

add('valid', '有効期限の内で、通用する券のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-150-100h300v200h-300z" class="paper"/>
  <g fill="{INK}"><rect x="-110" y="-70" width="130" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-110-20h220M-110 20h180"/></g>
  <g transform="translate(80 60)"><circle r="34" fill="none" stroke="{TONES['green'][0]}" stroke-width="6"/><path d="M-16 0l12 14 22-26" fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"/></g>
</g>
""", ground=True)

add('vast', '見わたす限り広がる大地のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#eaf5fb"/>
<g class="green o" opacity=".85"><path d="M0 260q150-40 300-20t300-20v180H0z"/></g>
{sun(500,90,30)}
{person(120,346,0.5,1,'coral','blue','stand','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M100 200h420M520 200H100"/></g>
""", ground=False, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
