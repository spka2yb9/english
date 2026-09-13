"""第59回: 距離・証拠・展覧会・爆発など40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('dishonest', '数をごまかして、うその申告をするイラスト。', f"""
{person(160,346,1.15,1,'violet','blue','give','cap','flat')}
<g transform="translate(340 230)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-70" y="-50" width="70" height="14"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-76-44h84"/><path d="M10-58h60v20H10z"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70 10h140M-70 50h100"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 140l34 34M514 140l-34 34"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('dismiss', '出された案を、手で払って退けるイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','give','short','neutral')}
<g transform="translate(300 240)">
  <path d="M-70-60h140v120h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-30h92M-46 0h92"/></g>
</g>
{person(470,346,1.2,-1,'blue','blue','point','bob','flat')}
<path d="M380 200h-60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M360 300l34 34M394 300l-34 34"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('display', 'ガラスケースに並べて見せるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200-120h400v40h-400z" class="goldd o"/>
  <path d="M-190-80h380v160h-380z" fill="#e7f6fb" opacity=".7" stroke="{INK}" stroke-width="3"/>
  <path d="M-200 80h400v30h-400z" class="goldd o"/>
  <g class="teal o"><circle cx="-110" cy="20" r="34"/></g>
  <g class="coral o"><rect x="-30" y="-14" width="66" height="66"/></g>
  <g class="gold o"><path d="M120 52l40-70 40 70z"/></g>
</g>
<g fill="#ffffff" opacity=".5"><path d="M-160-60l60 0-90 140h-40z" transform="translate(300 250)"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('distance', '二点のあいだの隔たりを示したイラスト。', f"""
<circle cx="120" cy="230" r="26" class="teal o"/>
<circle cx="480" cy="230" r="26" class="coral o"/>
<g class="a" marker-end="url(#ar)"><path d="M150 230h300M450 230H150"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M120 270v70M480 270v70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('distant', '遠くにかすんで見える山のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#eaf1f7"/>
<g fill="#b9c8d6" opacity=".7"><path d="M300 150l140 120H160z"/></g>
<g fill="#a8bacb" opacity=".5"><path d="M460 180l110 90H350z"/></g>
{person(140,346,1.1,1,'teal','blue','point','short','neutral')}
<path d="M220 250h140" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('distinct', 'ぼやけた形と、輪郭のはっきりした形を比べたイラスト。', f"""
<g transform="translate(170 230)">
  <circle r="70" fill="#cfe0ea" opacity=".7"/>
  <circle r="86" fill="#dbe6ee" opacity=".4"/>
</g>
<g transform="translate(430 230)">
  <circle r="70" class="teal o"/>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 350l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('distinctive', '並んだ中で、そこだけ形が際立つイラスト。', f"""
<g class="tealp o">{''.join(f'<circle cx="{110+i*70}" cy="230" r="30"/>' for i in range(7))}</g>
<g transform="translate(320 230)">
  <path d="M0-46l14 28 30 4-22 22 6 30-28-16-28 16 6-30-22-22 30-4z" class="coral o"/>
</g>
<circle cx="320" cy="230" r="56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M320 120v50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('disturbing', '見て心がざわつく、不穏なイラスト。', f"""
<g transform="translate(400 230)">
  <path d="M-110-100h220v200h-220z" fill="#41506a"/>
  <g fill="{TONES['coral'][0]}"><path d="M-50-30l40 24-40 24zM50-30l-40 24 40 24z"/></g>
  <path d="M-50 50q50 30 100 0" fill="none" stroke="#fffdf6" stroke-width="6"/>
</g>
{person(150,346,1.15,1,'teal','blue','up','short','surprised')}
{drop(210,240,0.7)}
<path d="M250 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ecological', '木と水と生き物がめぐる生態系のイラスト。', f"""
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-dasharray="18 12"><circle cx="300" cy="210" r="130"/></g>
{tree(300,120,0.55)}
{drop(430,210,1.1)}
<g transform="translate(300 320)">
  <ellipse rx="46" ry="22" class="bluep o"/>
  <path d="M-46 0l-30-20v40z" class="bluep o"/>
</g>
<g transform="translate(170 210)"><ellipse rx="30" ry="20" fill="#f3c94f" stroke="{INK}" stroke-width="3"/><circle cx="-28" cy="-6" r="14" class="ink"/></g>
<path d="M380 120a140 140 0 0 1 50 60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('editorial', '新聞の意見欄が載ったページのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <g fill="{INK}"><rect x="-160" y="-120" width="320" height="24"/></g>
  <path d="M-160-80h320" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-160-60h150v190h-150z" class="goldp o" opacity=".7"/>
  <g fill="{INK}"><rect x="-140" y="-40" width="110" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-140 {0+i*30}h110"/>' for i in range(4))}{''.join(f'<path d="M10 {-40+i*30}h150"/>' for i in range(6))}</g>
</g>
""", ground=True)

add('electoral', '投票所と票の集計で、選挙のしくみを示したイラスト。', f"""
<g transform="translate(180 270)">
  <path d="M-90-60h180v120h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-40-70h80v14h-80z" class="ink"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><rect x="-60" y="-20" width="120" height="56"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="{TONES['teal'][0]}"><rect x="-70" y="20" width="36" height="60"/><rect x="-20" y="-20" width="36" height="100"/><rect x="30" y="-60" width="36" height="140"/></g>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('encouraging', '背を押して、励ましてやるイラスト。', f"""
{person(230,346,1.2,1,'blue','blue','reach','short','smile')}
{person(390,346,1.2,1,'coral','gold','walk','bob','smile')}
<path d="M300 250h30" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M460 250h60" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:5"><path d="M340 170l26-20M350 210h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('enemy', '旗を挟んで向かい合う、敵どうしのイラスト。', f"""
{person(170,346,1.2,1,'coral','coral','stand','cap','flat')}
{person(430,346,1.2,-1,'teal','teal','stand','cap','flat')}
<g transform="translate(300 240)">
  <path d="M-4-90h8v190h-8z" class="ink"/>
  <path d="M-4-86h-60v40h60z" class="coralp o"/>
  <path d="M4-86h60v40H4z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M240 190h30M360 190h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('engage', '仕事に手をつけて、それに携わるイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','reach','short','neutral')}
<g transform="translate(400 260)">
  <path d="M-120-40h240v40h-240z" class="goldd o"/>
  <path d="M-90-90h180v50h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-70h120M-60-52h90"/></g>
  <g fill="none" stroke="{INK}" stroke-width="10"><circle cx="60" cy="30" r="26"/></g>
</g>
<path d="M280 240h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('engaging', '話に引き込まれて、身を寄せるイラスト。', f"""
{person(160,346,1.15,1,'blue','blue','point','short','smile')}
<g transform="translate(320 180)">
  <path d="M-80-50h160v80h-160z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-56" y="-26" width="112" height="14"/></g>
</g>
<g transform="translate(470 346) rotate(-14)">{person(0,0,1.15,-1,'coral','gold','reach','bob','smile')}</g>
<g class="golds" style="stroke-width:5"><path d="M420 170l26-20M430 210h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('engineering', '歯車と設計図で、工学を示したイラスト。', f"""
<g transform="translate(180 240)">
  <g fill="none" stroke="{INK}" stroke-width="14"><circle r="70"/></g>
  <g fill="{INK}">{''.join(f'<rect x="-10" y="-92" width="20" height="26" transform="rotate({i*45})"/>' for i in range(8))}</g>
  <circle r="20" class="ink"/>
</g>
<g transform="translate(430 240)">
  <path d="M-110-110h220v220h-220z" fill="#e8f2fb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M-70-60h140v120h-140zM-70 0h140M0-60v120"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('enjoyable', '笑いながら楽しく遊べるイラスト。', f"""
{person(200,346,1.2,1,'coral','gold','up','bob','smile')}
{person(340,346,1.2,-1,'teal','blue','up','short','smile')}
<g transform="translate(270 150)"><circle r="34" class="goldp o"/><path d="M-34 0h68" fill="none" stroke="{TONES['gold'][2]}" stroke-width="3"/></g>
<g class="golds" style="stroke-width:5"><path d="M440 180l26-20M450 220h30M120 180l-26-20"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 300l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('entertaining', '舞台の芸で客を楽しませるイラスト。', f"""
<g transform="translate(300 140)">
  <path d="M-200-60h400v40h-400z" class="coral o"/>
  <path d="M-200-20h60q10 100 0 160h-60z" class="coralp o"/>
  <path d="M140-20h60v160h-60q-10-60 0-160z" class="coralp o"/>
</g>
<g transform="translate(300 250) scale(0.9)">{person(0,60,1.0,1,'gold','violet','up','bob','smile')}</g>
<g class="golds" style="stroke-width:5"><path d="M200 180l-26-20M400 180l26-20"/></g>
{person(120,346,0.65,1,'teal','blue','stand','short','smile')}
{person(490,346,0.65,-1,'coral','gold','stand','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('entertainment', '映画や音楽など、楽しみの品が並ぶイラスト。', f"""
<g transform="translate(150 240)">
  <path d="M-80-70h160v130h-160z" fill="#dfe6ea" class="o"/>
  <path d="M-60-50h120v90h-120z" class="bluep o"/>
</g>
<g transform="translate(330 240)">
  <path d="M-70-70h140v140h-140z" class="paper"/>
  <g fill="{INK}"><ellipse cx="-20" cy="30" rx="18" ry="12"/><rect x="-6" y="-30" width="6" height="54"/><ellipse cx="40" cy="10" rx="18" ry="12"/><rect x="54" y="-50" width="6" height="54"/></g>
</g>
<g transform="translate(490 250)">
  <circle r="60" class="violet o"/>
  <circle r="18" fill="#fffdf6"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('enthusiasm', '目を輝かせて、熱をもって取り組むイラスト。', f"""
{person(230,346,1.3,1,'coral','blue','up','short','smile')}
{flame(230,150,1.1)}
<g class="golds" style="stroke-width:5"><path d="M340 200l26-20M350 240h30M120 200l-26-20"/></g>
<g transform="translate(450 260)">
  <path d="M-70-60h140v120h-140z" class="teal o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('episode', '連なる話のうち、一回分を示したイラスト。', f"""
<g class="tealp o"><rect x="80" y="200" width="100" height="120"/><rect x="320" y="200" width="100" height="120"/><rect x="440" y="200" width="100" height="120"/></g>
<rect x="200" y="190" width="100" height="130" class="coral o"/>
<g fill="#fffdf6"><path d="M230 240l40 25-40 25z"/></g>
<path d="M250 130v40" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('equivalent', '重さがぴたりと同じで、釣り合うイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-6-40h12v60h-12z" class="ink"/>
  <path d="M-170 20h340" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-170 20v50M170 20v50" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(130 260)"><circle r="40" class="teal o"/></g>
<g transform="translate(470 260)"><path d="M-36-36h72v72h-72z" class="coral o"/></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M280 330h40M280 360h40"/></g>
""", ground=False)

add('error', '計算の途中に一か所まちがいがあるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-100" width="120" height="14"/><rect x="-60" y="-50" width="120" height="14"/><rect x="-120" y="-10" width="240" height="6"/><rect x="-60" y="20" width="120" height="14"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M76 12l50 50M126 12l-50 50"/></g>
</g>
""", ground=True)

add('especially', '全体の中で、とりわけこれが目立つイラスト。', f"""
<g class="tealp o">{''.join(f'<rect x="{90+i*70}" y="240" width="52" height="80"/>' for i in range(7))}</g>
<rect x="230" y="150" width="72" height="170" class="coral o"/>
<path d="M266 100v30" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:5"><path d="M180 160l-24-18M350 160l24-18"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('establish', '土台に柱を据えて、組織を打ち立てるイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-180-20h360v40h-360z" fill="#c9d3dc" class="o"/>
</g>
<g transform="translate(300 230)">
  <path d="M-120-70h240v140h-240z" class="teal o"/>
  <path d="M-140-70l140-80 140 80z" class="teald o"/>
  <g fill="#fffdf6"><rect x="-30" y="-20" width="60" height="90"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 140v60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('estimate', 'ざっと目で測って、おおよその数を出すイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','think','short','neutral')}
<g class="tealp o">{''.join(f'<circle cx="{300+ (i%4)*60}" cy="{200+(i//4)*60}" r="22"/>' for i in range(12))}</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="270" y="170" width="250" height="180" rx="14"/></g>
<g transform="translate(240 150)">
  <path d="M-50-40h100v60h-100z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-30" y="-16" width="34" height="12"/></g>
  <g fill="{MUTED}"><circle cx="20" cy="-10" r="5"/><circle cx="32" cy="-10" r="5"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('eternal', '終わりなくめぐり続ける輪のイラスト。', f"""
<g transform="translate(300 210)">
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="26" stroke-linecap="round">
    <path d="M-60 0a60 60 0 1 1 60 60a60 60 0 1 0 60-60a60 60 0 1 1-60-60a60 60 0 1 0-60 60z"/>
  </g>
</g>
<path d="M420 110a150 150 0 0 1 40 70" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('ethnic', '民族ごとの衣や模様のちがいを示したイラスト。', f"""
{person(160,346,1.2,1,'coral','gold','stand','bob','smile')}
<g transform="translate(160 246)"><path d="M-40-14h80v10h-80z" class="goldd o"/></g>
{person(300,346,1.2,1,'teal','violet','stand','cap','smile')}
{person(440,346,1.2,1,'gold','blue','stand','short','smile')}
<g transform="translate(440 250)"><g fill="{TONES['coral'][0]}"><circle cx="-14" cy="-10" r="5"/><circle cx="14" cy="-10" r="5"/><circle cx="0" cy="10" r="5"/></g></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('even', 'でこぼこのない、平らな面のイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-90 60q20-50 40-20t30-40 40 20 40-30v70z" class="coralp o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-90 60V-10h180v70z" class="tealp o"/>
  <path d="M-90-10h180" fill="none" stroke="{TONES['teal'][0]}" stroke-width="7"/>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 350l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('everywhere', 'どの場所にも同じ印があるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-200-40h400M-200 40h400M-70-140v280M70-140v280"/></g>
  <g class="coral o">{''.join(f'<circle cx="{-135+c*135}" cy="{-90+r*90}" r="20"/>' for r in range(3) for c in range(3))}</g>
</g>
""", ground=True)

add('evidence', '現場に残った跡が、証拠として示されるイラスト。', f"""
<g transform="translate(220 250)">
  <path d="M-150-120h300v240h-300z" fill="#fffdf6" class="o"/>
  <g fill="{MUTED}" opacity=".9"><ellipse cx="-80" cy="40" rx="22" ry="14"/><ellipse cx="-20" cy="10" rx="22" ry="14"/><ellipse cx="40" cy="50" rx="22" ry="14"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="-20" cy="20" r="90"/></g>
</g>
<g transform="translate(450 210)">
  <path d="M-70-70h140v140h-140z" class="paper"/>
  <g fill="{INK}"><rect x="-40" y="-40" width="60" height="12"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-30 20l18 18 34-40"/></g>
</g>
<path d="M370 250h20" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('evident', '一目でそれと分かる、明白なイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-190-120h380v240h-380z" fill="#fffdf6" class="o"/>
  <circle r="80" class="coral o"/>
</g>
<g transform="translate(300 350)">
  <ellipse rx="60" ry="34" fill="#fffdf6" class="o"/>
  <circle r="16" class="ink"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 330l20 20 34-40"/></g>
""", ground=False)

add('evil', '角のある黒い影が、悪意を向けるイラスト。', f"""
<g transform="translate(400 250)">
  <path d="M-90 110q-20-160 90-160t90 160z" fill="#2f4055"/>
  <path d="M-70-60l-14-50 40 28zM70-60l14-50-40 28z" fill="#2f4055"/>
  <g fill="{TONES['coral'][0]}"><path d="M-40-20l34 20-34 20zM40-20l-34 20 34 20z"/></g>
  <path d="M-40 50q40 26 80 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
{person(140,346,1.05,1,'teal','blue','up','short','surprised')}
<path d="M220 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('exactly', '目盛りにぴったり合っているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-220-30h440v60h-440z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-200+i*40}-30v{22 if i%2 else 34}"/>' for i in range(11))}</g>
</g>
<g transform="translate(300 150)">
  <path d="M-40-60h80v60h-80z" class="teal o"/>
  <path d="M0 0v50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M460 330l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('exceptional', '並んだ点から大きく外れた一点のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-160h400v320h-400z" fill="#f7fbfe" class="o"/>
  <g class="tealp"><circle cx="-140" cy="60" r="14"/><circle cx="-90" cy="70" r="14"/><circle cx="-40" cy="50" r="14"/><circle cx="10" cy="66" r="14"/><circle cx="60" cy="56" r="14"/><circle cx="110" cy="70" r="14"/></g>
  <circle cx="120" cy="-100" r="20" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="120" cy="-100" r="44"/></g>
</g>
""", ground=True)

add('excessive', 'あふれるほど注ぎすぎているイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-70-90h140l-14 170h-112z" fill="#f7fbfe" class="o"/>
  <path d="M-64-70h128l-12 150h-104z" class="bluep o"/>
  <path d="M-70-90q70 30 140 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
</g>
<g class="bluep o"><ellipse cx="300" cy="360" rx="120" ry="20"/></g>
<g transform="translate(180 130) rotate(24)">
  <path d="M-50-40h100v70h-100z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M50-10q40 6 50 30" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 160l34 34M504 160l-34 34"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('excitement', '心がわき立って、胸が高鳴るイラスト。', f"""
{person(280,346,1.35,1,'coral','gold','up','bob','smile')}
<g transform="translate(280 140)">
  <path d="M0 40c-40-30-56-46-56-68a30 30 0 0 1 56-16 30 30 0 0 1 56 16c0 22-16 38-56 68z" class="coral o"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M160 200l-30-24M150 250h-34M400 200l30-24M410 250h34"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('exclusive', '限られた人だけが入れる扉のイラスト。', f"""
<g transform="translate(360 240)">
  <path d="M-110-140h220v280h-220z" fill="#e4e9ee" class="o"/>
  <path d="M-80-110h160v250h-160z" class="goldd o"/>
  <circle cx="60" cy="20" r="10" class="ink"/>
  <g transform="translate(0 -60)"><path d="M0-24l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="gold o"/></g>
</g>
{person(150,346,1.0,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 190l18 18 30-36"/></g>
{person(520,346,0.9,-1,'coral','gold','stand','bob','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 190l28 28M528 190l-28 28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('exhibition', '作品を並べて見せる展覧会のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-220-110h140v140h-140z" class="goldd o"/>
  <path d="M-200-90h100v100h-100z" fill="#fffdf6" class="o"/>
  <path d="M-180 0l30-40 24 24 26-34 20 50z" class="green o"/>
  <path d="M-60-110h140v140h-140z" class="goldd o"/>
  <path d="M-40-90h100v100h-100z" fill="#fffdf6" class="o"/>
  <circle cx="10" cy="-40" r="30" class="coralp o"/>
  <path d="M100-110h140v140h-140z" class="goldd o"/>
  <path d="M120-90h100v100h-100z" fill="#fffdf6" class="o"/>
  <path d="M140 0h60v-60h-60z" class="tealp o"/>
</g>
{person(200,340,0.75,1,'teal','blue','stand','short','smile')}
{person(400,340,0.75,-1,'coral','gold','stand','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('expedition', '荷を担いで、未知の地へ探検に出るイラスト。', f"""
<g fill="#b9c8d6" opacity=".7"><path d="M420 180l150 130H270z"/></g>
{person(180,340,1.1,1,'coral','blue','carry','cap','neutral')}
<g transform="translate(180 250)"><path d="M-40-30h80v60h-80z" class="goldd o"/></g>
<path d="M260 250h140" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12" marker-end="url(#ar)"/>
<g transform="translate(430 160)"><path d="M-4-40h8v50h-8z" class="ink"/><path d="M4-38h44v28H4z" class="coral o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('explanation', '図を指して、筋道を説き聞かせるイラスト。', f"""
{person(150,346,1.15,1,'blue','blue','point','short','neutral')}
<g transform="translate(390 220)">
  <path d="M-140-120h280v240h-280z" class="paper"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M-100-60h80M-100 0h80M-100 60h80"/></g>
  <g fill="{MUTED}"><rect x="0" y="-70" width="100" height="20"/><rect x="0" y="-10" width="100" height="20"/><rect x="0" y="50" width="70" height="20"/></g>
</g>
<path d="M230 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
