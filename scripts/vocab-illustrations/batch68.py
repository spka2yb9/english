"""第68回: 影・棚・標識・安定など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('servant', '主人に仕えて給仕する召使のイラスト。', f"""
<g transform="translate(400 300)">
  <path d="M-110-20h220v26h-220z" class="goldd o"/>
</g>
{person(430,290,1.0,-1,'violet','blue','stand','bob','neutral')}
{person(200,340,1.1,1,'blue','blue','carry','short','neutral')}
<g transform="translate(250 260)">
  <ellipse rx="46" ry="14" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M300 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('setting', 'つまみで設定を選び分けるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-120h360v240h-360z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="-90" cy="-30" r="40"/></g>
  <path d="M-90-30v-30" fill="none" stroke="{INK}" stroke-width="8"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="3"><rect x="0" y="-60" width="140" height="24"/><rect x="0" y="-20" width="140" height="24"/><rect x="0" y="20" width="140" height="24"/></g>
  <g class="teal o"><rect x="0" y="-20" width="60" height="24"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('settle', 'もつれが片づいて、落ち着くイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-60 40q60-90 30-40t50-30-20 60 50-40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
</g>
<g transform="translate(430 240)">
  <path d="M-90-20h180v40h-180z" class="teal o"/>
  <path d="M-90 20h180v6h-180z" fill="{TONES['teal'][2]}"/>
</g>
<path d="M270 230h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 340l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('severe', '傷みがひどく、深刻なイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-110h320v220h-320z" class="tealp o"/>
  <g fill="none" stroke="{INK}" stroke-width="8"><path d="M-60-110l30 80-50 60 40 80M60-110l-20 70 60 60-40 90"/></g>
</g>
<g class="corals" style="stroke-width:6"><path d="M120 130l-26-20M480 130l26-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sexy', '人目を引く装いで、はっとさせるイラスト。', f"""
{person(300,346,1.35,1,'coral','coral','stand','bob','smile')}
<g class="coral o"><circle cx="220" cy="200" r="10"/><circle cx="390" cy="180" r="12"/></g>
<g class="golds" style="stroke-width:5"><path d="M420 240l24-18M180 240l-24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('shadow', '光を受けた人の影が地面に伸びるイラスト。', f"""
{sun(140,110,34)}
{person(300,300,1.15,1,'teal','blue','stand','short','neutral')}
<g fill="{MUTED}" opacity=".55"><path d="M330 300l150 40-20 20-150-40z"/></g>
<path d="M470 250l-60 40" class="a" marker-end="url(#ar)"/>
<path d="M60 326h480" class="a"/>
""", ground=True, arrow=True)

add('shallow', '浅い水と深い水を比べたイラスト。', f"""
<g transform="translate(170 270)">
  <path d="M-90-70h180v140h-180z" fill="#f7fbfe" class="o"/>
  <path d="M-90 40h180v30h-180z" class="bluep o"/>
</g>
<g transform="translate(430 270)">
  <path d="M-90-70h180v140h-180z" fill="#f7fbfe" class="o"/>
  <path d="M-90-40h180v110h-180z" class="blue o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M170 380v-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('shaped', '型どおりの形にかたどられたイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-80h160v160h-160z" fill="#fffdf6" class="o"/>
  <path d="M0 40c-30-40-40-56-40-72a40 40 0 0 1 80 0c0 16-10 32-40 72z" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g transform="translate(430 240)">
  <path d="M0 40c-30-40-40-56-40-72a40 40 0 0 1 80 0c0 16-10 32-40 72z" class="coral o"/>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('sheer', '切り立った崖のイラスト。', f"""
<g fill="#b6bfc9" stroke="{INK}" stroke-width="3"><path d="M300 60h240v340H300z"/></g>
<g fill="none" stroke="#8b98a6" stroke-width="5"><path d="M360 80v300M430 70v310M500 90v290"/></g>
<g class="green o" opacity=".8"><path d="M300 60h240v-0z"/><path d="M300 56h240v-20H300z" opacity="0"/></g>
<g class="a" marker-end="url(#ar)"><path d="M220 80v280"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True, arrow=True)

add('shelf', '物を並べる棚のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v20h-400zM-200-40h400v20h-400zM-200 60h400v20h-400zM-200 160h400v20h-400z" class="goldd o"/>
  <path d="M-210-140h20v320h-20zM190-140h20v320h-20z" class="goldd o"/>
  <g class="tealp o"><rect x="-170" y="-120" width="50" height="80"/><rect x="-110" y="-120" width="50" height="80"/></g>
  <g class="coralp o"><rect x="20" y="-20" width="60" height="80"/></g>
  <g class="goldp o"><rect x="-150" y="80" width="80" height="80"/></g>
</g>
<path d="M60 416h480" class="a"/>
""", ground=True)

add('shell', '固い殻に包まれた貝と中身のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M0 60q-90-20-90-70T0-70q90 10 90 60T0 60z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#d9c286" stroke-width="3"><path d="M-70-30q70-20 130 20M-60 10q70-20 120 20"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-90 40q0-90 90-90t90 90z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g class="coralp o"><ellipse cy="10" rx="50" ry="26"/></g>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('shock', '思わぬ知らせにぎょっとするイラスト。', f"""
{face(280,200,95,'flat')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="3"><circle cx="242" cy="182" r="22"/><circle cx="318" cy="182" r="22"/></g>
<g fill="{INK}"><circle cx="242" cy="182" r="8"/><circle cx="318" cy="182" r="8"/></g>
<g transform="translate(280 252)"><ellipse rx="26" ry="30" fill="#8b4a3e"/></g>
<g class="corals" style="stroke-width:6"><path d="M410 120l34-26M430 170h34M410 220l34 26M150 120l-34-26M130 170H96"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('shocking', '見出しの知らせが衝撃的なイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="{TONES['coral'][0]}"><rect x="-150" y="-110" width="300" height="34"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-150 {-40+i*34}h300"/>' for i in range(5))}</g>
</g>
<g class="corals" style="stroke-width:6"><path d="M120 90l-30-24M480 90l30-24"/></g>
{person(120,380,0.6,1,'teal','blue','up','short','surprised')}
""", ground=True)

add('sight', '目に映る広い光景のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-120h400v220h-400z" fill="#eaf5fb" class="o"/>
  <g fill="#b9c8d6"><path d="M-40 100l120-140 120 140z"/></g>
  <g class="green o"><path d="M-200 100q120-50 200-20t200-10v30h-400z"/></g>
  {sun(-120,-60,26)}
</g>
<g transform="translate(300 370)">
  <ellipse rx="60" ry="24" fill="#fffdf6" class="o"/>
  <circle r="12" class="ink"/>
</g>
""", ground=False)

add('sign', '道ばたに立つ標識のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-110-90h220v140h-220z" fill="#fffdf6" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" marker-end="url(#ar)"><path d="M-60-20h100"/></g>
  <path d="M-14 50h28v130h-28z" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('significant', '全体に大きく効く一点を示したイラスト。', f"""
<path d="M60 346h480" class="a"/>
<g class="tealp o">{''.join(f'<rect x="{90+i*60}" y="280" width="44" height="66"/>' for i in range(5))}</g>
<rect x="410" y="120" width="120" height="226" class="coral o"/>
<path d="M470 80v30" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:5"><path d="M390 110l-24-18"/></g>
""", ground=False, arrow=True)

add('silence', '音がひとつもない静けさのイラスト。', f"""
<g transform="translate(280 220)">
  <path d="M-60-60h60l60-50v220l-60-50h-60z" class="ink"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M80-40l60 60M140-40l-60 60"/></g>
</g>
{face(470,230,60,'flat')}
<g fill="none" stroke="{INK}" stroke-width="5"><path d="M450 250h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('similarity', '二つの形の似ている点を丸で示すイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M0-80l80 80-80 80-80-80z" class="teal o"/>
</g>
<g transform="translate(430 230)">
  <path d="M0-76l76 76-76 76-76-76z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><circle cx="180" cy="230" r="96"/><circle cx="430" cy="230" r="92"/></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M290 220h30M290 250h30"/></g>
""", ground=False)

add('site', '工事の現場となる敷地のイラスト。', f"""
<g transform="translate(300 300)"><path d="M-240-20h480v40h-480z" fill="#e6dcc9"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 10"><rect x="120" y="170" width="360" height="130"/></g>
<g transform="translate(200 250)">
  <path d="M-6-80h12v130h-12z" class="ink"/>
  <path d="M-6-80h90v10h-90z" class="ink"/>
  <path d="M70-70v30" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
{box(400,270,90,60,0,'gold')}
<path d="M60 346h480" class="a"/>
""", ground=True)

add('situated', '地図の一点に位置しているイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-200-40h400M-200 50h400M-70-140v280M70-140v280"/></g>
  <g class="greenp o"><rect x="-190" y="-130" width="110" height="80"/></g>
</g>
<g transform="translate(370 210)">
  <path d="M0 40c-30-40-40-56-40-72a40 40 0 0 1 80 0c0 16-10 32-40 72z" class="coral o"/>
  <circle cy="-34" r="13" fill="#fffdf6"/>
</g>
""", ground=True)

add('skilled', '道具を手なれた様子で使いこなすイラスト。', f"""
{person(200,346,1.25,1,'blue','blue','reach','short','smile')}
<g transform="translate(300 250) rotate(20)">
  <path d="M-10-70h20v90h-20z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-24-90h48v22h-48z" class="coral o"/>
</g>
<g transform="translate(450 260)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-30 0l18 18 30-36"/></g>
</g>
<g class="golds" style="stroke-width:5"><path d="M130 190l-24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('slight', 'ほんのわずかに傾いているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-20h320v40h-320z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
  <g transform="rotate(-4)"><path d="M-160-20h320v40h-320z" class="tealp o"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 350v-40"/></g>
<g fill="{INK}"><rect x="160" y="120" width="80" height="10"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('slip', '足がすべって転びそうになるイラスト。', f"""
<g transform="translate(280 320) rotate(-26)">{person(0,0,1.2,1,'coral','blue','up','short','surprised')}</g>
<g fill="#cfe6f5" opacity=".8"><ellipse cx="330" cy="356" rx="90" ry="18"/></g>
<g class="a" marker-end="url(#ar)"><path d="M400 300l60 40"/></g>
{drop(220,220,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('slowly', 'ゆっくりと少しずつ進むイラスト。', f"""
<g opacity=".3">{person(180,346,1.1,1,'teal','blue','walk','short','neutral')}</g>
<g opacity=".6">{person(250,346,1.1,1,'teal','blue','walk','short','neutral')}</g>
{person(320,346,1.1,1,'teal','blue','walk','short','neutral')}
<g class="muted"><path d="M420 250h100"/></g>
<path d="M180 180h150" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sociable', '輪の中に入って、人と交わるイラスト。', f"""
{person(180,346,1.15,1,'coral','gold','give','bob','smile')}
{person(300,346,1.15,1,'teal','blue','give','short','smile')}
{person(420,346,1.15,-1,'gold','blue','give','cap','smile')}
<path d="M240 250h20M360 250h20" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M180 170q120-50 240 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('society', '多くの人が集まってできる社会のイラスト。', f"""
{building(140,300,0.7,'teal')}
{building(470,300,0.7,'blue')}
{person(240,340,0.75,1,'coral','gold','stand','bob','smile')}
{person(310,340,0.75,1,'teal','blue','stand','short','smile')}
{person(380,340,0.75,1,'gold','violet','stand','cap','smile')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="90" y="170" width="430" height="190" rx="18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('software', '画面の中で動く手順書きのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v250h-380z" fill="#41506a"/>
  <path d="M-165-115h330v200h-330z" fill="#1f2b3d"/>
  <g fill="#7fd6c2"><rect x="-140" y="-90" width="120" height="12"/><rect x="-120" y="-64" width="150" height="12"/><rect x="-120" y="-38" width="90" height="12"/><rect x="-140" y="-12" width="140" height="12"/><rect x="-120" y="14" width="110" height="12"/></g>
  <g fill="#f3c94f"><rect x="-140" y="40" width="70" height="12"/></g>
  <path d="M-40 110h80v30h-80z" fill="#41506a"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('solar', '太陽の光を板で受けて使うイラスト。', f"""
{sun(140,110,40)}
<g transform="translate(400 260)">
  <g transform="rotate(-16)"><path d="M-110-70h220v140h-220z" class="bluep o"/>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="3">{''.join(f'<path d="M{-110+i*44}-70v140"/>' for i in range(1,5))}<path d="M-110 0h220"/></g></g>
  <path d="M-10 60h20v70h-20z" class="ink"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M200 160l100 50M180 210l110 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('sophisticated', '素朴な形から、洗練された形へ磨かれるイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-70 60q0-90 70-90t70 90z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(430 250)">
  <path d="M-50 60q-30-70 0-100t50-30 50 30-10 100z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-20-70h40v-20h-40z" class="tealp o"/>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:5"><path d="M520 150l24-18"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('sound', 'がたつきのない、しっかりした土台のイラスト。', f"""
{box(300,180,220,80,0,'gold')}
<g transform="translate(300 300)">
  <path d="M-160-40h320v40h-320z" class="teal o"/>
  <path d="M-130 0h60v60h-60zM70 0h60v60H70z" class="teald o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 220l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('source', '水が湧き出るもとを示したイラスト。', f"""
<g transform="translate(150 250)">
  <path d="M-70 60q0-80 70-80t70 80z" fill="#cfe4d5" class="o"/>
  <circle cy="20" r="32" class="bluep o"/>
  {drop(0,-40,0.8)}
</g>
<path d="M200 300q120 40 180-10t180 20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="18" stroke-linecap="round" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="150" cy="260" r="90"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('spectacular', '打ち上げ花火の壮観なイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a52"/>
<g fill="none" stroke="#f3c94f" stroke-width="5">{''.join(f'<path d="M300 160L{300+int(120*__import__("math").cos(i*3.14159/6))} {160+int(120*__import__("math").sin(i*3.14159/6))}"/>' for i in range(12))}</g>
<g fill="#f3c94f">{''.join(f'<circle cx="{300+int(126*__import__("math").cos(i*3.14159/6))}" cy="{160+int(126*__import__("math").sin(i*3.14159/6))}" r="8"/>' for i in range(12))}</g>
<g fill="none" stroke="#e97f6a" stroke-width="4">{''.join(f'<path d="M470 300L{470+int(60*__import__("math").cos(i*3.14159/4))} {300+int(60*__import__("math").sin(i*3.14159/4))}"/>' for i in range(8))}</g>
<g transform="translate(140 380) scale(0.8)">{person(0,0,1.0,1,'teal','blue','up','short','smile')}</g>
""", ground=False)

add('sporting', 'ボールと道具でスポーツを示したイラスト。', f"""
<g transform="translate(160 260)">
  <circle r="60" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0-34l30 24-12 36h-36l-12-36z" class="ink"/>
</g>
<g transform="translate(330 260) rotate(-20)">
  <ellipse cy="-40" rx="40" ry="56" fill="none" stroke="{INK}" stroke-width="8"/>
  <path d="M-8 16h16v90h-16z" class="goldd o"/>
</g>
<g transform="translate(470 280)">
  <ellipse rx="50" ry="30" fill="#8b5e3c" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#fffdf6" stroke-width="3"><path d="M-18-8h36M-18 8h36"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('spot', '地図の一点や、布のしみを示すイラスト。', f"""
<g transform="translate(220 240)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <g class="coral o"><circle cx="30" cy="20" r="20"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="30" cy="20" r="50"/></g>
</g>
<g transform="translate(470 250)">
  <path d="M-70-70h140v140h-140z" fill="#fffdf6" class="o"/>
  <g fill="#c8bfa4"><ellipse cx="-10" cy="0" rx="30" ry="22"/><circle cx="30" cy="30" r="10"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stable', 'ぐらつかず、しっかり立っているイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-40-120h80v200h-80z" class="teal o"/>
  <path d="M-140 80h280v30h-280z" class="teald o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M300 100v-40"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 200l20 20 34-40"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('stadium', '観客席が丸く囲むスタジアムのイラスト。', f"""
<g transform="translate(300 240)">
  <ellipse rx="240" ry="140" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <ellipse rx="180" ry="100" class="green o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="3"><ellipse rx="150" ry="80"/><path d="M0-80v160"/></g>
  <g fill="{MUTED}">{''.join(f'<circle cx="{int(212*__import__("math").cos(i*3.14159/8))}" cy="{int(122*__import__("math").sin(i*3.14159/8))}" r="7"/>' for i in range(16))}</g>
</g>
""", ground=False)

add('staff', 'そろいの制服で働く職員のイラスト。', f"""
{person(170,346,1.15,1,'blue','blue','stand','cap','smile')}
{person(300,346,1.15,1,'blue','blue','stand','cap','smile')}
{person(430,346,1.15,1,'blue','blue','stand','cap','smile')}
<g class="teal o"><circle cx="140" cy="250" r="10"/><circle cx="270" cy="250" r="10"/><circle cx="400" cy="250" r="10"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('standing', '長く据え置かれたままの看板のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-120-110h240v150h-240z" fill="#f4ead2" stroke="{INK}" stroke-width="4"/>
  <g fill="{INK}"><rect x="-80" y="-70" width="160" height="18"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-20h160"/></g>
  <path d="M-14 40h28v130h-28z" class="ink"/>
</g>
<g transform="translate(430 130)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M0-22v22l16 10" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g class="green o" opacity=".7"><path d="M270 380q10-30 20-30t16 30z"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stark', 'まっ白とまっ黒が並ぶ、はっきりした対比のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h200v280h-200z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0-140h200v280H0z" fill="#2f4055"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 380h60M360 380h-60"/></g>
""", ground=False, arrow=True)

add('statement', '声明の文が読み上げられるイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','point','short','neutral')}
<g transform="translate(390 220)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <g fill="{INK}"><rect x="-100" y="-90" width="140" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-40+i*34}h200"/>' for i in range(4))}</g>
</g>
<path d="M240 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('statue', '台座にのった人の像のイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-80-20h160v40h-160z" fill="#c9d3dc" class="o"/>
  <path d="M-60-40h120v20h-120z" fill="#c9d3dc" class="o"/>
</g>
<g transform="translate(300 230)">
  <circle cy="-70" r="36" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-50 60q0-90 50-90t50 90z" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <path d="M50 0q40-20 40-60" fill="none" stroke="#dbe3ea" stroke-width="18" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sticky', 'べたついて指にくっつくイラスト。', f"""
{hand(300,150,1)}
<g transform="translate(300 300)">
  <path d="M-90-40h180v70h-180z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"><path d="M-30-40q10-60 30-70M30-40q-10-60-30-70"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('stranger', '初めて来て、その場に不慣れな人のイラスト。', f"""
{person(160,346,1.15,1,'coral','gold','think','bob','flat')}
<g fill="{INK}" transform="translate(230 170)">
  <path d="M0 0q0-26 20-26t20 26q0 14-14 18v12h-10v-20q14-4 14-14t-8-8-8 12z"/><rect x="12" y="42" width="10" height="10"/>
</g>
{person(410,346,1.0,1,'teal','blue','stand','short','smile')}
{person(500,346,1.0,1,'gold','blue','stand','cap','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M320 300h40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('strategic', '盤の上で先を読んで手を打つイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-120h320v240h-320z" fill="#fffdf6" class="o"/>
  <g fill="#dfe6ea">{''.join(f'<rect x="{-160+c*80+(80 if r%2 else 0)}" y="{-120+r*60}" width="80" height="60"/>' for r in range(4) for c in range(2))}</g>
  <g class="teal o"><circle cx="-120" cy="-90" r="20"/><circle cx="40" cy="30" r="20"/></g>
  <g class="coral o"><circle cx="120" cy="-30" r="20"/></g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M40 30L110-10"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('stress', '重い圧に押されて、張りつめるイラスト。', f"""
{box(300,190,190,76,0,'gold')}
{person(300,346,1.15,1,'teal','blue','stand','short','flat')}
<g class="a" marker-end="url(#ar)"><path d="M180 150v50M420 150v50"/></g>
{drop(360,240,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('strike', '振り下ろした手が的を打つイラスト。', f"""
{hand(220,150,1)}
<g transform="translate(330 280)">
  <path d="M-90-40h180v80h-180z" class="goldd o"/>
</g>
<g transform="translate(330 210)">
  <path d="M0-40l20 40-20 40-20-40z" class="coralp o"/>
</g>
<path d="M250 200l60 40" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:5"><path d="M420 220l24-18M180 260l-24 18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
