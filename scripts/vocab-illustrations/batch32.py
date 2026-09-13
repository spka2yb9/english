"""第32回: 骨・血・城・現金など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('biscuit', '皿にのった丸いビスケットのイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(280 290)">
  <ellipse rx="130" ry="40" fill="#fffdf6" class="o"/>
  <g transform="translate(-40 -20)"><circle r="44" class="goldd o"/><g fill="{INK}"><circle cx="-14" cy="-10" r="5"/><circle cx="12" cy="6" r="5"/><circle cx="-4" cy="20" r="5"/></g></g>
  <g transform="translate(50 -14)"><circle r="38" class="goldd o"/><g fill="{INK}"><circle cx="-10" cy="-8" r="5"/><circle cx="10" cy="8" r="5"/></g></g>
</g>
""", ground=True)

add('bit', '大きなかたまりから、ほんの少しだけ取り分けたイラスト。', f"""
{box(200,250,180,130,0,'gold')}
<g transform="translate(450 300)"><path d="M-20-16h40v32h-40z" class="gold o"/></g>
<path d="M320 300h80" class="a" marker-end="url(#ar)"/>
<path d="M430 350h40" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('blame', '割れた皿を指して、相手のせいだと責めているイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','point','short','neutral')}
{person(460,346,1.1,-1,'teal','gold','stand','bob','sad')}
<g transform="translate(320 320)">
  <path d="M-60 0l40-30 20 14 30-20 30 36z" fill="#fffdf6" class="o"/>
  <g class="corals" style="stroke-width:4"><path d="M-20-40v-20M20-44l14-16"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M250 230h130" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('bleed', '指の傷から血がにじみ出ているイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-30-100h60v150a30 30 0 0 1-60 0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-14-40h28v8h-28z" class="coral"/>
</g>
{drop(280,300,1.3,'coral')}
{drop(300,350,1.0,'coral')}
<path d="M420 260q-60 10-100 20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('bless', '手をかざして、相手に祝福を与えているイラスト。', f"""
<circle cx="300" cy="140" r="86" class="goldp" opacity=".5"/>
{person(180,346,1.15,1,'violet','blue','reach','short','smile')}
{person(430,346,1.1,-1,'teal','gold','hold','bob','smile')}
<g class="golds" style="stroke-width:4"><path d="M320 200l-16-24M360 210l0-26M400 220l16-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('blood', '試験管に入れた赤い血液のイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-24-110h48v170a24 24 0 0 1-48 0z" fill="#f4fbff" class="o"/>
  <path d="M-24-20h48v80a24 24 0 0 1-48 0z" class="coral o"/>
  <path d="M-30-120h60v14h-60z" class="ink"/>
</g>
{drop(430,240,1.6,'coral')}
<path d="M340 250h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('boast', '胸を張って、自分の成果を大きく語っているイラスト。', f"""
{person(200,346,1.2,1,'coral','blue','up','short','smile')}
<g transform="translate(420 190)">
  <path d="M-90-46h180q16 0 16 16v50q0 16-16 16h-120l-26 22 6-22h-40q-16 0-16-16v-50q0-16 16-16z" class="paper"/>
  <path d="M0 20l-16-28 8-10 8 8 8-8 8 10z" class="gold o"/>
  <path d="M-8-24h16v14h-16z" class="coral o"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M290 230l24-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bone', '体を支える一本の骨を示したイラスト。', f"""
<g transform="translate(300 220) rotate(-16)">
  <path d="M-120-14h240v28h-240z" fill="#f7f2ea" stroke="{INK}" stroke-width="3"/>
  <circle cx="-130" cy="-22" r="26" fill="#f7f2ea" stroke="{INK}" stroke-width="3"/>
  <circle cx="-130" cy="22" r="26" fill="#f7f2ea" stroke="{INK}" stroke-width="3"/>
  <circle cx="130" cy="-22" r="26" fill="#f7f2ea" stroke="{INK}" stroke-width="3"/>
  <circle cx="130" cy="22" r="26" fill="#f7f2ea" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('boost', '下から押し上げて、高さを増しているイラスト。', f"""
<g class="tealp o"><rect x="150" y="240" width="90" height="120"/></g>
<rect x="360" y="150" width="90" height="210" class="teal o"/>
<path d="M405 400V370" class="a" marker-end="url(#ar)" transform="rotate(180 405 385)"/>
{hand(405,400,1)}
<path d="M280 200h50" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=False, arrow=True)

add('boss', '部下に指示を出している上司のイラスト。', f"""
{person(180,346,1.25,1,'blue','violet','point','short','neutral')}
{person(430,346,1.0,-1,'teal','gold','stand','bob','neutral')}
<g transform="translate(300 200)">
  <path d="M-50-30h100q12 0 12 12v30q0 12-12 12h-70l-18 16 4-16q-12 0-12-12v-30q0-12 12-12z" class="paper"/>
  <path d="M-6-14h12v22h-6z" class="ink"/>
</g>
<g transform="translate(180 180)"><path d="M-30 0l-4-30 16 12 10-20 10 20 16-12-4 30z" class="gold o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bother', '作業中の人のそばで、音を立てて邪魔をするイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','point','short','sad')}
<g transform="translate(430 250)">
  <path d="M-60-60h120v120h-120z" class="goldp o"/>
  <circle r="30" class="gold o"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:5">
  <path d="M340 210q-26 26-26 40t26 40"/><path d="M300 190q-34 34-34 60t34 60"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('bottom', '容器の底の部分を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-100-120h200l-16 240h-168z" fill="#f7fbfe" class="o"/>
  <path d="M-84 100h168" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<path d="M460 330h60" class="a" marker-end="url(#ar)" transform="rotate(180 490 330)"/>
<path d="M120 380h360" class="a"/>
""", ground=True, arrow=True)

add('bounce', 'ボールが床に当たって、跳ね返るイラスト。', f"""
<path d="M120 100q60 220 130 0t130 0 120-60" class="muted" marker-end="url(#ar)"/>
<circle cx="120" cy="110" r="24" class="coral o" opacity=".4"/>
<circle cx="250" cy="300" r="24" class="coral o" opacity=".7"/>
<circle cx="380" cy="140" r="26" class="coral o"/>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('bow', '腰を折って、深くおじぎをしているイラスト。', f"""
<g transform="translate(280 346)">
  <path d="M-12-8l-7 35M12-8l7 35" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <path d="M-30-90q30-16 60 0l-10 82h-40z" class="teal o"/>
  <path d="M-26-80l-16 46M26-80l16 46" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <g transform="translate(34 -96) rotate(58)">
    <circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-26-4q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
    <path d="M-10 6h6M8 6h6" class="a"/>
  </g>
</g>
<path d="M420 220a90 90 0 0 1-40 70" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('bowl', '深い形の器に、料理が入っているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(280 260)">
  <path d="M-120-30h240q-16 130-120 130T-120-30z" fill="#fffdf6" class="o"/>
  <path d="M-120-30h240" class="a"/>
  <path d="M-104-6h208q-14 90-104 90T-104-6z" class="goldp o"/>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('brain', '頭の中にある脳の形を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M0-120q90 0 90 80 0 70-90 70t-90-70q0-80 90-80z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="4">
    <path d="M0-116v146M-50-100q30 30 0 60t20 60M50-100q-30 30 0 60t-20 60"/>
  </g>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('brave', '大きな相手にも、まっすぐ立ち向かっているイラスト。', f"""
{person(180,346,1.1,1,'coral','blue','point','short','neutral')}
<g fill="#3d4c5c" stroke="{INK}" stroke-width="3"><path d="M420 350q-40-140 60-170 60-18 90 40 34 62-30 130z"/></g>
<g fill="#f7e6a8"><circle cx="470" cy="220" r="9"/><circle cx="520" cy="220" r="9"/></g>
<path d="M250 250h100" class="a" marker-end="url(#ar)" style="stroke-width:6"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('breach', '塀の一部が破られて、穴が開いているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-240-90h180v180h-180zM60-90h180v180H60z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#c9bda6" stroke-width="4"><path d="M-240-30h180M-240 30h180M60-30h180M60 30h180"/></g>
</g>
<g fill="#cfc7b8" stroke="{INK}" stroke-width="2.5"><path d="M270 330q10-24 40-16t14 16z"/></g>
<path d="M180 200h140" class="a" marker-end="url(#ar)"/>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('briefly', '長い話を短くまとめて、一言で伝えるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-120h180v240h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-60 {-90+i*24}h120"/>' for i in range(8))}</g>
</g>
<g transform="translate(430 230)">
  <path d="M-70-40h140q16 0 16 16v40q0 16-16 16h-90l-24 20 6-20h-32q-16 0-16-16v-40q0-16 16-16z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-44-8h88"/></g>
</g>
<path d="M280 230h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('broadcast', '電波塔から、電波が広く送り出されるイラスト。', f"""
<g transform="translate(200 260)">
  <path d="M-50 100L-16-60h32L50 100z" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-36 40h72M-26 0h52" fill="none" stroke="{INK}" stroke-width="5"/>
  <path d="M0-60v-30" class="a"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:5">
  <path d="M250 140q34 34 34 60t-34 60"/><path d="M300 110q46 46 46 90t-46 90"/><path d="M350 80q58 58 58 120t-58 120"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('businessman', 'スーツにかばんを持った実業家のイラスト。', f"""
{person(280,346,1.3,1,'blue','blue','carry','short','neutral')}
<g transform="translate(280 258)">
  <path d="M-42-24h84v6h-84z" class="paper"/>
  <path d="M-12-20l12 18 12-18z" class="ink"/>
  <path d="M-46-20l14 90h-30zM46-20l-14 90h30z" class="blued o"/>
</g>
<g transform="translate(400 300)">
  <path d="M-50-30h100v60h-100z" class="goldd o"/>
  <path d="M-20-30q0-20 20-20t20 20" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('button', '服のボタンを穴に留めているイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-140-120h140v240h-140z" class="tealp o"/>
  <path d="M20-120h140v240H20z" class="tealp o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2.5">
    {''.join(f'<circle cx="-40" cy="{-70+i*60}" r="18"/>' for i in range(4))}
  </g>
  <g fill="{INK}">{''.join(f'<g><circle cx="-46" cy="{-76+i*60}" r="3"/><circle cx="-34" cy="{-76+i*60}" r="3"/><circle cx="-46" cy="{-64+i*60}" r="3"/><circle cx="-34" cy="{-64+i*60}" r="3"/></g>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3">{''.join(f'<path d="M30 {-78+i*60}v24"/>' for i in range(4))}</g>
</g>
""", ground=True)

add('camping', 'テントを張って野外で過ごす、キャンプのイラスト。', f"""
{tree(90,330,0.8)}{tree(520,330,0.7)}
<g transform="translate(230 330)">
  <path d="M-100 0L0-140 100 0z" class="tealp o"/>
  <path d="M0-140L-34 0h68z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
</g>
{flame(410,326,1.0)}
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"><path d="M370 340l80-20M450 340l-80-20"/></g>
""", ground=True)

add('carpet', '床に敷かれた模様入りのじゅうたんのイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-200-60h400v120h-400z" class="coralp o"/>
  <path d="M-180-40h360v80h-360z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3">
    {''.join(f'<path d="M{-140+i*70} -20l20 20-20 20-20-20z"/>' for i in range(5))}
  </g>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3">{''.join(f'<path d="M{-200+i*20} 60v14"/>' for i in range(21))}</g>
</g>
""", ground=True)

add('case', '一つの事例を、書類にまとめて示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-140h280v280h-280z" class="paper"/>
  <path d="M-140-140h280v50h-280z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-50h200M-100-10h200M-100 30h160"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><rect x="-110" y="60" width="220" height="50"/></g>
</g>
""", ground=True)

add('cash', '財布から取り出した紙幣と硬貨のイラスト。', f"""
<g transform="translate(220 250)">
  <path d="M-90-50h180v100h-180z" class="greenp o"/>
  <circle r="24" class="green o"/>
  <path d="M-90-20h180" fill="none" stroke="{TONES['green'][2]}" stroke-width="4"/>
</g>
<g class="goldp o"><circle cx="400" cy="290" r="26"/><circle cx="450" cy="300" r="26"/><circle cx="425" cy="250" r="26"/></g>
<path d="M330 270h30" class="a" marker-end="url(#ar)"/>
<path d="M120 350h380" class="a"/>
""", ground=True, arrow=True)

add('cast', '網を投げ広げて、水面へ放つイラスト。', f"""
<path d="M0 280h600v120H0z" class="bluep"/>
<path d="M0 280q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
{person(160,280,1.0,1,'teal','blue','up','cap','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="3">
  <path d="M300 200q80 0 120 60M300 200q60 20 60 90M300 200q100 20 140 90"/>
  <path d="M330 230q70 20 90 60M300 260q60 10 80 50"/>
</g>
<path d="M230 200q40-30 70-10" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('castle', '塔と城壁を備えた大きな城のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-180 110V-20h360v130z" fill="#cfc7b8" stroke="{INK}" stroke-width="3"/>
  <g fill="#cfc7b8" stroke="{INK}" stroke-width="3">
    <path d="M-200 0V-90h60V0zM140 0V-90h60V0z"/>
    <path d="M-200-90l-14-30h88l-14 30zM200-90l14-30h-88l14 30z"/>
  </g>
  <g fill="#cfc7b8" stroke="{INK}" stroke-width="3">{''.join(f'<rect x="{-180+i*60}" y="-44" width="30" height="24"/>' for i in range(6))}</g>
  <path d="M-40 110V30h80v80z" class="goldd o"/>
  <g class="bluep o"><rect x="-186" y="-70" width="30" height="34"/><rect x="156" y="-70" width="30" height="34"/></g>
</g>
<path d="M60 360h480" class="a"/>
""", ground=True)

add('cater', '会場に料理を用意して、提供しているイラスト。', f"""
<g transform="translate(340 300)">
  <path d="M-180-20h360v20h-360z" class="goldp o"/>
  <g><ellipse cx="-100" cy="-40" rx="60" ry="20" fill="#fffdf6" class="o"/><ellipse cx="20" cy="-40" rx="60" ry="20" fill="#fffdf6" class="o"/><ellipse cx="130" cy="-40" rx="50" ry="18" fill="#fffdf6" class="o"/></g>
  <g class="coralp o"><circle cx="-100" cy="-48" r="16"/><circle cx="20" cy="-48" r="16"/></g>
</g>
{person(130,346,1.0,1,'teal','teal','give','bob','smile')}
<path d="M200 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('cease', '動いていた線が止まって、そこで終わるイラスト。', f"""
<path d="M60 200h300" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" stroke-linecap="round"/>
<path d="M390 130v140" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
<path d="M420 200h120" class="muted"/>
<g class="corals" style="stroke-width:8"><path d="M450 170l40 40M490 170l-40 40"/></g>
<path d="M180 270h140" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('celebrity', 'カメラを向けられて注目を集める有名人のイラスト。', f"""
{person(300,346,1.25,1,'violet','blue','up','bun','smile')}
<g transform="translate(140 280)"><path d="M-40-26h80v52h-40z" class="ink"/><circle r="14" fill="#dfe6ea" stroke="{INK}" stroke-width="2.5"/></g>
<g transform="translate(470 280)"><path d="M-40-26h80v52h-40z" class="ink"/><circle r="14" fill="#dfe6ea" stroke="{INK}" stroke-width="2.5"/></g>
<g class="golds" style="stroke-width:5"><path d="M200 180l-24-24M400 180l24-24M300 130v-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('central', '円の中心に位置するものを示したイラスト。', f"""
<circle cx="300" cy="220" r="140" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-dasharray="16 12"/>
<g class="tealp o">
  {''.join(f'<circle cx="{300 + int(120*__import__("math").cos(i*3.14159/3))}" cy="{220 + int(120*__import__("math").sin(i*3.14159/3))}" r="24"/>' for i in range(6))}
</g>
<circle cx="300" cy="220" r="42" class="coral o"/>
""", ground=False)

add('chance', '扉が一つだけ開いていて、通れる機会があるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-240-140h140v280h-140zM100-140h140v280H100z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
  <path d="M-100-140h200v280h-200z" fill="#fffaf1"/>
  <path d="M-100-140v280M100-140v280" class="a"/>
</g>
{person(120,346,0.9,1,'teal','blue','walk','short','smile')}
<path d="M200 200h120" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:4"><path d="M300 120v-20"/></g>
""", ground=True, arrow=True)

add('character', '違う性格を表す表情を、三つ並べたイラスト。', f"""
{face(140,220,80,'smile')}
{face(300,220,80,'flat')}
{face(460,220,80,'sad')}
<path d="M60 340h480" class="muted"/>
""", ground=False)

add('charge', '機器を電源につないで、充電しているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-70-120h140q14 0 14 14v212q0 14-14 14h-140q-14 0-14-14v-212q0-14 14-14z" fill="#dfe6ea" class="o"/>
  <path d="M-52-96h104v170h-104z" class="bluep o"/>
  <g class="green o"><rect x="-30" y="-60" width="60" height="100"/></g>
</g>
<g transform="translate(300 160)">
  <path d="M-14-40l-16 46h20l-10 34 30-50h-20l16-30z" class="gold o"/>
</g>
<path d="M300 400v-20" fill="none" stroke="{INK}" stroke-width="8"/>
<path d="M300 380h180v-60" fill="none" stroke="{INK}" stroke-width="8"/>
""", ground=True)

add('chart', '棒グラフと折れ線を組み合わせた図表のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-160 100h320M-160 100V-100" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o"><rect x="-130" y="20" width="50" height="80"/><rect x="-60" y="-20" width="50" height="120"/><rect x="10" y="-60" width="50" height="160"/><rect x="80" y="0" width="50" height="100"/></g>
  <path d="M-105 0l70-40 70-50 70 40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
""", ground=True)
print(' '.join(W)); print(sheet(W))
