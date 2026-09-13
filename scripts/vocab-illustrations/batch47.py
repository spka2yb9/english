"""第47回: くつろぐ・救助・回復・回転など39語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('relaxed', '肩の力が抜けて、ゆったり構えている人のイラスト。', f"""
<g transform="translate(160 346)" opacity=".45">{person(0,0,1.2,1,'coral','blue','up','short','flat')}</g>
{person(420,346,1.2,1,'teal','gold','stand','bob','smile')}
<g class="muted"><path d="M340 210q40-20 60 0"/></g>
<path d="M250 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('relaxing', 'ハンモックで、のんびりくつろげる場のイラスト。', f"""
{sun(510,90,28)}
{tree(120,330,1.1)}
{tree(490,330,1.1)}
<path d="M130 250q170 90 340 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="12" stroke-linecap="round"/>
<g transform="translate(300 290)">
  <path d="M-70-20q70 34 140 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
  <ellipse cx="-60" cy="-30" rx="26" ry="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-40-14h130v20h-130z" class="teal o" transform="rotate(6)"/>
</g>
<g class="muted"><path d="M300 160q40-20 60 0"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('relieve', '痛みが薬でやわらいで、楽になるイラスト。', f"""
{face(170,200,80,'flat')}
<g class="corals" style="stroke-width:5"><path d="M250 150q22 20 22 44"/></g>
<g transform="translate(300 250)">
  <path d="M-34-20h68v40h-68z" fill="#f4fbff" class="o"/>
  <path d="M0-20v40" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-34-20h34v40h-34z" class="coralp o"/>
</g>
{face(470,200,80,'smile')}
<path d="M370 200h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('religious', '手を合わせて祈りをささげるイラスト。', f"""
<g transform="translate(400 230)">
  <path d="M-110 110h220v-160h-220z" fill="#f4ead2" class="o"/>
  <path d="M-130-50l130-90 130 90z" class="tealp o"/>
  <path d="M-16-160h32v50h-32z" class="ink"/><path d="M-40-140h80v20h-80z" class="ink"/>
  <path d="M-40 110V40h80v70z" class="goldd o"/>
</g>
{person(160,346,1.15,1,'violet','blue','stand','short','neutral')}
<g transform="translate(160 226)"><path d="M-20 26q-4-38 20-50 24 12 20 50z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('remark', 'ひと言だけ短く言い添えるイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','stand','short','neutral')}
<g transform="translate(390 190)">
  <path d="M-120-60h240v100h-240z" fill="#fffdf6" class="o"/>
  <path d="M-90 40l-14 40 50-40z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-80" y="-20" width="120" height="14"/></g>
</g>
<path d="M240 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('render', '白い形に色をつけて、別の状態に変えるイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-80h160v160h-160z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-80-80h160v160h-160z" class="teal o"/>
</g>
<path d="M280 240h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(300 130) rotate(20)"><path d="M-10-50h20v70h-20z" class="coral o"/><path d="M-10 20h20l-10 22z" class="ink"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('renew', '期限切れの証を新しいものに取りかえるイラスト。', f"""
<g transform="translate(170 230)" opacity=".5">
  <path d="M-100-70h200v140h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-30h140M-70 0h140"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-90 60l180-120"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-100-70h200v140h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-30h140M-70 0h140"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M40 40l14 14 26-30"/></g>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('repeated', '同じ言葉が何度もくり返されるイラスト。', f"""
{person(140,346,1.05,1,'teal','blue','stand','short','neutral')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="3">
  <path d="M220 120h150v60H220z"/><path d="M250 190h150v60H250z"/><path d="M280 260h150v60H280z"/>
</g>
<g fill="{INK}"><rect x="250" y="142" width="90" height="14"/><rect x="280" y="212" width="90" height="14"/><rect x="310" y="282" width="90" height="14"/></g>
<path d="M470 140q40 90 0 170" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('reporter', 'マイクを差し出して取材する記者のイラスト。', f"""
{person(160,346,1.15,1,'coral','blue','reach','bob','neutral')}
<g transform="translate(280 250)">
  <path d="M-10-10h60v20h-60z" class="ink"/>
  <circle cx="60" r="20" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
</g>
{person(460,346,1.15,-1,'blue','blue','stand','short','neutral')}
<g transform="translate(160 236)"><path d="M-40-30h80v14h-80z" class="paper"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('reproduce', '元の絵と同じものをもう一枚作り出すイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-100h200v200h-200z" fill="#fffdf6" class="o"/>
  <path d="M-70 60l60-80 40 40 44-60 36 100z" class="tealp o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-100-100h200v200h-200z" fill="#fffdf6" class="o"/>
  <path d="M-70 60l60-80 40 40 44-60 36 100z" class="tealp o"/>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('rescue', '水に落ちた人に手を伸ばして助け出すイラスト。', f"""
<path d="M0 290h600v110H0z" class="bluep"/>
<g transform="translate(400 290)">
  <circle cy="-10" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-30-30q30-30 60 0" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/>
</g>
{person(170,290,1.15,1,'coral','blue','reach','short','neutral')}
<path d="M240 240h100" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="14"><circle cx="330" cy="250" r="34"/></g>
""", ground=False, arrow=True)

add('researcher', '顕微鏡をのぞいて調べる研究者のイラスト。', f"""
{person(180,340,1.1,1,'blue','blue','reach','bob','neutral')}
<g transform="translate(400 300)">
  <path d="M-60 40h120v14h-120z" fill="#c9d3dc" class="o"/>
  <path d="M-10-60h20v100h-20z" fill="#7f8ea6" class="o"/>
  <path d="M-10-60q-50-20-60-50l40-20q20 30 40 40z" fill="#7f8ea6" class="o"/>
  <path d="M-40 0h60v14h-60z" fill="#c9d3dc" class="o"/>
</g>
<g transform="translate(500 200)">
  <path d="M-60-60h120v120h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-20h72M-36 10h72"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('resemble', 'よく似た二つの形を並べたイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M0-90l90 90-90 90-90-90z" class="teal o"/>
</g>
<g transform="translate(430 230)">
  <path d="M0-84l84 84-84 84-84-84z" class="tealp o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M280 210h50M280 250h50"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('reserve', '一つの席を取っておいて、名札を置くイラスト。', f"""
<g transform="translate(300 300)">
  <g class="goldd o"><rect x="-250" y="-20" width="140" height="20"/><rect x="-90" y="-20" width="140" height="20"/><rect x="70" y="-20" width="140" height="20"/></g>
</g>
{person(160,300,0.8,1,'teal','blue','stand','short','smile')}
{person(460,300,0.8,1,'coral','gold','stand','bob','smile')}
<g transform="translate(300 250)">
  <path d="M-50 30h100l-10-50h-80z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-30" y="0" width="60" height="10"/></g>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('reside', '一つの家に住まいを定めて暮らすイラスト。', f"""
<g transform="translate(360 280)">
  <path d="M-110 60h220v-110h-220z" fill="#f4ead2" class="o"/>
  <path d="M-130-50l130-80 130 80z" class="coral o"/>
  <path d="M-30 60V0h60v60z" class="goldd o"/>
  <path d="M40-20h50v40H40z" fill="#e8f4fb" stroke="{INK}" stroke-width="3"/>
</g>
{person(160,340,1.05,1,'teal','blue','stand','short','smile')}
<path d="M230 300h40" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('resign', '辞表を置いて、職場を去るイラスト。', f"""
<g transform="translate(200 290)">
  <path d="M-110-20h220v26h-220z" class="goldd o"/>
  <path d="M-100 6h14v60h-14zM86 6h14v60H86z" class="goldd o"/>
  <g transform="translate(0 -50)">
    <path d="M-60-30h120v50h-120z" class="paper"/>
    <g fill="{INK}"><rect x="-36" y="-14" width="72" height="10"/></g>
  </g>
</g>
{person(450,346,1.05,1,'teal','blue','walk','short','neutral')}
<path d="M520 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('resist', '押されても踏みとどまって、押し返すイラスト。', f"""
{person(400,346,1.2,-1,'coral','gold','point','bob','flat')}
{person(200,346,1.2,1,'teal','blue','point','short','flat')}
<path d="M270 230h50" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8" marker-end="url(#ar)"/>
<path d="M340 270h-50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('resolve', 'こじれた糸をほどいて、まっすぐにするイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-70 40q60-90 30-40t50-30-20 60 60-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M-40-40q50 10 20 50t60 10" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
</g>
<path d="M330 240h190" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"/>
<path d="M260 230h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 320l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('restore', '傷んだ絵を手当てして、元の姿に戻すイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-100h200v200h-200z" fill="#e8e2d4" class="o"/>
  <path d="M-70 60l60-80 40 40 44-60 36 100z" fill="#c8c2b0"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-40-90l20 60-30 40M60-80l-20 50"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-100-100h200v200h-200z" fill="#fffdf6" class="o"/>
  <path d="M-70 60l60-80 40 40 44-60 36 100z" class="green o"/>
  {sun(390,190,20)}
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('restrict', '通れる幅をせばめて、量を制限するイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-240-120h140v240h-140zM100-120h140v240H100z" fill="#c9d3dc" class="o"/>
</g>
<path d="M60 230h180" class="a" marker-end="url(#ar)"/>
<g class="teal o"><circle cx="300" cy="230" r="26"/></g>
<g class="muted"><path d="M300 130v-40M300 370v-40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M340 160h-20M340 300h-20"/></g>
""", ground=False, arrow=True)

add('resume', 'いったん止めた作業を、また動かし始めるイラスト。', f"""
<g transform="translate(160 210)">
  <circle r="80" class="mutedfill" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <g fill="{MUTED}"><rect x="-30" y="-40" width="22" height="80"/><rect x="8" y="-40" width="22" height="80"/></g>
</g>
<g transform="translate(430 210)">
  <circle r="80" class="tealp o"/>
  <path d="M-26-44l70 44-70 44z" class="teal"/>
</g>
<path d="M270 210h60" class="a" marker-end="url(#ar)"/>
<g transform="translate(300 340)">
  <path d="M-200-10h400v20h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-200-10h240v20h-240z" class="teal"/>
</g>
""", ground=False, arrow=True)

add('retain', '手放さずに、そのまま持ち続けるイラスト。', f"""
{person(240,346,1.25,1,'teal','blue','carry','short','neutral')}
<g transform="translate(240 250)">{box(0,0,110,80,0,'gold')}</g>
<g class="muted" marker-end="url(#ar)"><path d="M420 250h60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 210l40 40M510 210l-40 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('retired', '仕事を終えて、いすでのんびり過ごすイラスト。', f"""
<g transform="translate(360 300)">
  <path d="M-90-40h180v30h-180z" class="goldd o"/>
  <path d="M-90-40h30v-90h-30z" class="goldd o"/>
  <path d="M-70-10h14v50h-14zM56-10h14v50H56z" class="goldd o"/>
</g>
<g transform="translate(390 230) scale(0.9)">{person(0,60,1.0,1,'teal','gold','stand','short','smile')}</g>
<g transform="translate(160 260)">
  <path d="M-50-40h100v80h-100z" class="ink"/>
  <path d="M-16-52h32v12h-32z" class="ink"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-70-70l140 140M70-70L-70 70"/></g>
</g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('retrieve', '取られたものを、また自分の手に取り戻すイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','reach','short','neutral')}
<g transform="translate(380 250)">{box(0,0,100,80,0,'gold')}</g>
<path d="M340 220q-90-40-120 20" class="a" marker-end="url(#ar)"/>
<g opacity=".3" transform="translate(520 250)">{box(0,0,100,80,0,'gold')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('reveal', '布を取り去って、隠れていたものを見せるイラスト。', f"""
<g transform="translate(170 250)" >
  <path d="M-80 80q0-120 80-120t80 120z" fill="#dfe6ea" class="o"/>
</g>
<g transform="translate(430 250)">
  <circle cy="10" r="70" class="coral o"/>
  <path d="M-80-70q60-30 120 10" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
</g>
<path d="M280 240h50" class="a" marker-end="url(#ar)"/>
{sun(500,110,22)}
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('revise', '原稿に赤を入れて、書き直すイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-130-90h260M-130-40h260M-130 10h260M-130 60h200"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">
    <path d="M-120-46h100"/><path d="M-20-60h120"/>
    <path d="M20 4h60"/><path d="M60 74h80"/>
  </g>
</g>
<g transform="translate(500 300) rotate(28)"><path d="M-10-80h20v110h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('revive', 'しおれた草に水をやって、生き返らせるイラスト。', f"""
<g transform="translate(160 300)">
  <path d="M-40 40h80v-16h-80z" class="goldd o"/>
  <path d="M0 24q-30-30-40-70" fill="none" stroke="#a8a37f" stroke-width="7"/>
  <path d="M-40-46q-20 10-10 26" fill="none" stroke="#a8a37f" stroke-width="7"/>
</g>
<g transform="translate(430 300)">
  <path d="M-40 40h80v-16h-80z" class="goldd o"/>
  <path d="M0 24v-90" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
  <g class="green o"><ellipse cx="-30" cy="-50" rx="26" ry="14" transform="rotate(-20 -30 -50)"/><ellipse cx="30" cy="-70" rx="26" ry="14" transform="rotate(20 30 -70)"/></g>
</g>
{drop(300,200,1.0)}
<path d="M280 260h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('rid', 'いらないものを取り除いて、さっぱりさせるイラスト。', f"""
<g transform="translate(170 250)">
  <g class="mutedfill" fill="#c8c2b0" stroke="{INK}" stroke-width="2"><circle cx="-40" cy="20" r="26"/><circle cx="20" cy="-20" r="22"/><circle cx="40" cy="50" r="20"/><circle cx="-10" cy="60" r="18"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-90-80h180v170h-180z" fill="#fffdf6" class="o"/>
</g>
<path d="M280 250h50" class="a" marker-end="url(#ar)"/>
<g transform="translate(180 130)">
  <path d="M-40-20h80v20h-80z" class="ink"/>
  <path d="M-30 0h60v40h-60z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('rip', '紙を両手で引き裂くイラスト。', f"""
{hand(140,180,1)}
{hand(460,180,-1)}
<g transform="translate(300 250)">
  <path d="M-140-90h130l20 40-20 40 20 40-20 60h-130z" class="paper"/>
  <path d="M140-90H10l-20 40 20 40-20 40 20 60h130z" class="paper"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M170 300h-70M430 300h70"/></g>
""", ground=True, arrow=True)

add('rob', 'かばんをうばって、持ち去るイラスト。', f"""
{person(180,346,1.1,1,'coral','blue','reach','short','sad')}
<g transform="translate(320 240)">
  <path d="M-50-30h100v70h-100z" class="goldd o"/>
  <path d="M-20-30q20-20 40 0" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
{person(470,346,1.15,1,'violet','violet','carry','cap','flat')}
<path d="M380 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('rock', 'ごつごつした大きな岩のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-180 80l40-120 70-40 90 20 60 60-20 80z" fill="#b6bfc9" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#8b98a6" stroke-width="4"><path d="M-100-40l40 60-30 60M60-40l-20 60 60 40"/></g>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('romantic', '二人のあいだにハートが浮かぶイラスト。', f"""
{person(220,346,1.15,1,'coral','gold','stand','bob','smile')}
{person(380,346,1.15,-1,'teal','blue','stand','short','smile')}
<g transform="translate(300 180)">
  <path d="M0 40c-40-30-56-46-56-70a30 30 0 0 1 56-16 30 30 0 0 1 56 16c0 24-16 40-56 70z" class="coral o"/>
</g>
<g class="coral o" opacity=".7"><circle cx="200" cy="150" r="10"/><circle cx="410" cy="140" r="14"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('roof', '家の上をおおう屋根のイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-140 70h280v-110h-280z" fill="#f4ead2" class="o"/>
  <path d="M-40 70V10h80v60z" class="goldd o"/>
</g>
<g transform="translate(300 250)">
  <path d="M-180 0l180-120 180 120z" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"><path d="M-120 0l120-80 120 80"/></g>
</g>
<path d="M180 160h-60" class="a" marker-end="url(#ar)" transform="rotate(180 150 160)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('rotate', '軸のまわりをぐるりと回るイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="110" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
  <circle r="20" class="ink"/>
  <g class="teal o"><rect x="-16" y="-110" width="32" height="60"/></g>
  <g class="tealp o"><rect x="-16" y="50" width="32" height="60"/></g>
</g>
<path d="M420 130a130 130 0 0 1 30 90" class="a" marker-end="url(#ar)"/>
<path d="M180 290a130 130 0 0 1-30-90" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('royal', '王冠と紋章で、王家のものを示したイラスト。', f"""
<g transform="translate(300 150)"><path d="M-70 40l-14-90 42 34 42-58 42 58 42-34-14 90z" class="gold o"/>
<g fill="{TONES['coral'][0]}"><circle cx="-40" cy="-20" r="8"/><circle cx="0" cy="-30" r="8"/><circle cx="40" cy="-20" r="8"/></g></g>
<g transform="translate(300 300)">
  <path d="M-80-70h160v60q0 60-80 80-80-20-80-80z" class="violet o"/>
  <path d="M0-40l12 26 28 4-20 20 5 28-25-14-25 14 5-28-20-20 28-4z" fill="#fffdf6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rub', '布で表面をこすってみがくイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-220-20h440v40h-440z" class="goldd o"/>
</g>
<g transform="translate(300 250)">
  <path d="M-70-30q70-30 140 0 10 30-70 40-80-10-70-40z" class="tealp o"/>
</g>
{hand(300,180,1)}
<g class="a" marker-end="url(#ar)"><path d="M180 200h-40M420 200h40"/></g>
<g class="golds" style="stroke-width:4"><path d="M420 280l24-16M430 310h26"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('rude', '背を向けて、ぶしつけにふるまうイラスト。', f"""
{person(220,346,1.2,1,'coral','gold','point','bob','flat')}
{person(400,346,-1.2,-1,'teal','blue','stand','short','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M470 160l44 44M514 160l-44 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('runner', 'ゼッケンをつけて走る走者のイラスト。', f"""
<g transform="translate(280 346) rotate(-8)">{person(0,0,1.4,1,'coral','blue','walk','short','neutral')}</g>
<g transform="translate(272 250)">
  <path d="M-34-24h68v48h-68z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-20" y="-6" width="40" height="12"/></g>
</g>
<g class="muted"><path d="M170 220h-90M160 270h-90"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('running', '足を運んで走り続けているイラスト。', f"""
<g opacity=".3">{person(180,346,1.2,1,'teal','blue','walk','short','neutral')}</g>
<g opacity=".6">{person(300,346,1.2,1,'teal','blue','walk','short','neutral')}</g>
{person(430,346,1.2,1,'teal','blue','walk','short','neutral')}
<path d="M120 200h380" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
