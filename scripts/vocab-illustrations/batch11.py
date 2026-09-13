"""第11回: 与える・許す・量・服など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('donate', '募金箱にお金を入れて、見返りを求めず差し出しているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="greenp"/>
<g transform="translate(340 290)">
  <path d="M-90-70h180v140h-180z" class="greenp o"/>
  <path d="M-30-70h60v-10h-60z" class="ink"/>
  <path d="M-50-44h100v10h-100z" class="ink"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="4"><path d="M-60 10h120M-60 40h120"/></g>
</g>
<g transform="translate(250 170)">
  <circle r="24" class="goldp o"/>
  <path d="M-8-10h16v20h-16z" class="goldd"/>
</g>
<path d="M250 210v50" class="a" marker-end="url(#ar)"/>
{hand(170,170,1)}
""", ground=True, arrow=True)

add('edit', '原稿の一部に赤で線を入れて、書き直しているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(280 240)">
  <path d="M-150-140h300v280h-300z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-110-100h220M-110-60h220M-110-20h220M-110 20h220M-110 60h160"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4">
    <path d="M-110-60h100"/><path d="M-30-74q30-16 60 0"/><path d="M-110 20h150"/>
  </g>
</g>
<g transform="translate(400 170) rotate(36)">
  <path d="M-10-90h20v130h-20z" class="coral o"/>
  <path d="M-10 40h20l-10 28z" class="ink"/>
</g>
""", ground=True)

add('foreign', '自国とは違う国旗と、海をまたいで届いた荷物のイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250h140v150H0zM460 250h140v150H460z" class="ground"/>
<path d="M0 250h140M460 250h140" class="a"/>
<g>
  <path d="M70 250V110" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M78 116l64 20-64 20z" class="teal o"/>
  <path d="M530 250V110" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M522 116l-64 20 64 20z" class="coral o"/>
</g>
{box(300,270,90,64,0,'gold')}
<path d="M440 200q-70-40-140 0" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('helpful', '道具を手渡してくれて、作業がはかどっているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
{person(180,346,1.1,1,'coral','blue','point','short','smile')}
{person(400,346,-1 * -1,'green','violet','give','bob','smile') if False else person(400,346,1.1,-1,'green','violet','give','bob','smile')}
<g transform="translate(300 260) rotate(-10)">
  <path d="M-46-24h92v30h-92z" class="goldd o"/>
  <path d="M0 6v54" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<path d="M348 210q-40-16-70-8" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 200l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('pleased', 'もらった贈り物を見て、うれしそうにほほえんでいる人のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
{person(240,346,1.2,1,'coral','blue','hold','bob','smile')}
<g transform="translate(240 260)">
  <path d="M-50-40h100v80h-100z" class="goldp o"/>
  <path d="M-10-40h20v80h-20zM-50-6h100v12h-100z" class="coral o"/>
  <path d="M0-40l-20-20 20 6 20-6z" class="coral o"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M330 180l24-24M150 180l-24-24M340 240h26"/></g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('rent', '部屋の鍵を受け取り、家賃を毎月わたしているイラスト。', f"""
{building(160,300,0.95,'teal')}
{person(430,346,1.05,-1,'coral','blue','give','bob','neutral')}
<g transform="translate(300 250)">
  <circle cx="-40" r="14" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
  <path d="M-26 0h50v9h-13v9h-9v-9h-28z" class="goldd o"/>
</g>
<g transform="translate(310 310)">
  <path d="M-40-20h80v40h-80z" class="greenp o"/>
  <circle r="10" class="green o"/>
</g>
<path d="M250 210h-60" class="a" marker-end="url(#ar)"/>
<path d="M360 330h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('survive', '嵐のあとの荒れた土地で、一本だけ折れずに残った木のイラスト。', f"""
<g class="muted" opacity=".8"><path d="M40 60q120 20 240 0t280 20"/></g>
<g transform="translate(140 340) rotate(-70)"><path d="M-7 0v-90h14V0z" class="goldd o"/></g>
<g transform="translate(470 340) rotate(58)"><path d="M-7 0v-80h14V0z" class="goldd o"/></g>
{tree(300,340,1.2)}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M420 130l18 18 30-36"/></g>
""", ground=True)

add('united', '別々だった人たちが手をつないで、一つにまとまっているイラスト。', f"""
<circle cx="300" cy="200" r="150" class="tealp" opacity=".5"/>
{person(160,336,1.0,1,'teal','blue','give','short','smile')}
{person(300,336,1.0,1,'coral','gold','give','bob','smile')}
{person(440,336,1.0,1,'violet','teal','give','cap','smile')}
<g fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"><circle cx="230" cy="266" r="14"/><circle cx="370" cy="266" r="14"/></g>
<path d="M100 200h400" class="muted"/>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('appreciate', 'もらった助けに対して、両手を添えて感謝を示しているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
{person(360,346,1.15,-1,'teal','blue','hold','short','smile')}
{person(180,346,1.15,1,'coral','violet','give','bob','smile')}
<g transform="translate(270 250)">
  <path d="M0 24l-28-34 14-16 14 14 14-14 14 16z" class="coral o"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M300 180l20-22M240 180l-20-22"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('aspire', '高い所にある星に向かって、手を伸ばして目指しているイラスト。', f"""
<g transform="translate(460 90)"><path d="M0-40l12 26 28 4-20 20 5 28-25-14-25 14 5-28-20-20 28-4z" class="gold o"/></g>
{person(200,346,1.2,1,'violet','blue','reach','bun','smile')}
<path d="M280 220q90-60 150-100" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('reasonable', '天びんが釣り合い、値札の数字と品物の価値が見合っているイラスト。', f"""
<path d="M300 340V140" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M250 356h100" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>
<path d="M150 140h300" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="300" cy="140" r="13" class="teal o"/>
<path d="M150 140v34M450 140v34" class="a"/>
{box(150,220,80,60,0,'gold')}
<g transform="translate(450 210)">
  <path d="M-50-30h100v60h-100z" class="paper"/>
  <circle cx="0" cy="0" r="18" class="goldp o"/>
</g>
<path d="M130 126h340" class="muted"/>
""", ground=True)

add('sack', '荷物を入れる大きな袋の口をしばったイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(280 280)">
  <path d="M-90-40q-16-60 90-60t90 60q16 100-90 100t-90-100z" class="goldp o"/>
  <path d="M-60-90q60-24 120 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"/>
  <path d="M-30-110q30-14 60 0l-6 20h-48z" class="goldd o"/>
</g>
""", ground=True)

add('satisfied', '食事を終えて満足そうに座っている人と、空になった皿のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
{person(220,346,1.15,1,'teal','blue','hold','short','smile')}
<g transform="translate(390 300)">
  <path d="M-140-20h280v20h-280z" class="goldp o"/>
  <path d="M-120 0v60M120 0v60" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
  <ellipse cy="-32" rx="70" ry="24" fill="#fffdf6" class="o"/>
  <ellipse cy="-34" rx="44" ry="14" class="muted"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M290 190l18 18 30-36"/></g>
""", ground=True)

add('smart', 'きちんとしたスーツを着て、身だしなみを整えた人のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="bluep"/>
{person(280,346,1.3,1,'blue','blue','stand','short','smile')}
<g transform="translate(280 262)">
  <path d="M-40-24h80v6h-80z" class="paper"/>
  <path d="M-12-20l12 18 12-18z" class="coral o"/>
  <path d="M-46-20l14 90h-30zM46-20l-14 90h30z" class="blued o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"><path d="M370 180l22-22M180 180l-22-22"/></g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('specific', 'たくさんの同じ箱の中から、ある一つだけを指し示しているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{80+ i%5*96}" y="{140 + i//5*100}" width="70" height="70"/>' for i in range(10))}
</g>
<rect x="272" y="240" width="70" height="70" class="coral o"/>
<circle cx="307" cy="275" r="58" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
{hand(180,340,1)}
<path d="M240 340h20" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('speech', '大勢の前の演台に立ち、話をしている人のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-70-40h140v100h-140z" class="goldp o"/>
  <path d="M-80-40h160" class="a"/>
  <path d="M0-40v-30" class="a"/>
  <circle cy="-84" r="14" class="ink"/>
</g>
{person(300,266,0.95,1,'teal','blue','point','short','neutral')}
<g transform="translate(430 170)">
  <path d="M-60-40h120q14 0 14 14v40q0 14-14 14h-84l-22 20 6-20h-20q-14 0-14-14v-40q0-14 14-14z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-16h80M-40 4h56"/></g>
</g>
<g opacity=".5">{person(110,366,0.7,-1,'violet','teal','stand','bob','smile')}{person(180,366,0.7,-1,'gold','blue','stand','short','smile')}</g>
""", ground=True)

add('spoken', '口から出た言葉が吹き出しで表され、紙の文字と対比されているイラスト。', f"""
{person(170,346,1.1,1,'teal','blue','stand','short','neutral')}
<g transform="translate(320 200)">
  <path d="M-70-46h140q16 0 16 16v46q0 16-16 16h-96l-26 24 6-24h-24q-16 0-16-16v-46q0-16 16-16z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-18h92M-46 6h60"/></g>
</g>
<g transform="translate(500 300)">
  <path d="M-56-70h112v140h-112z" class="paper" opacity=".55"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3" opacity=".6"><path d="M-36-40h72M-36-14h72M-36 12h50"/></g>
</g>
<path d="M420 250q30 20 40 40" class="muted"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('submit', '相手の前で両手を上げて、抵抗をやめているイラスト。', f"""
{person(220,346,1.2,1,'coral','blue','up','short','sad')}
{person(430,346,1.1,-1,'blue','violet','point','cap','neutral')}
<path d="M330 200h-40" class="a" marker-end="url(#ar)"/>
<g class="muted"><path d="M180 220v-40M260 220v-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('suit', '体にぴったり合ったスーツを着て、寸法が合っていることを示すイラスト。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
{person(280,346,1.3,1,'violet','violet','stand','short','smile')}
<g transform="translate(280 268)">
  <path d="M-46-30h92v6h-92z" class="paper"/>
  <path d="M-14-26l14 20 14-20z" class="coral o"/>
  <path d="M-50-26l16 96h-34zM50-26l-16 96h34z" class="violetd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M170 250h60"/><path d="M390 250h-60"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M420 300l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('supplement', '足りない分を上から付け足して、必要な量にしているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="greenp"/>
<g transform="translate(300 290)">
  <path d="M-90-120h180v200h-180z" fill="#f4fbff" class="o"/>
  <path d="M-82 0h164l-6 74h-152z" class="tealp o"/>
  <path d="M-82 0h164" class="a"/>
  <path d="M-90-60h180" class="muted"/>
</g>
<g transform="translate(300 130)">
  <path d="M-40-40h80v50h-80z" class="greenp o"/>
  <path d="M-6-30h12v30h-12zM-20-16h40v-8h-40z" class="green o"/>
</g>
<path d="M300 190v56" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('surrender', '白旗をかかげて、争いをやめて降伏しているイラスト。', f"""
{person(240,346,1.2,1,'coral','blue','up','cap','sad')}
<path d="M330 380V150" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
<path d="M338 156q60 0 76 22-40 26-76 24z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
{person(470,346,1.1,-1,'blue','violet','stand','cap','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('terminate', '進んでいた線が終点にぶつかり、そこで打ち切られるイラスト。', f"""
<path d="M60 200h330" fill="none" stroke="{TONES['teal'][0]}" stroke-width="16" stroke-linecap="round"/>
<path d="M420 100v200" fill="none" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>
<path d="M440 200h100" class="muted"/>
<g class="corals" style="stroke-width:8"><path d="M470 170l40 40M510 170l-40 40"/></g>
<path d="M200 260h150" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('tolerate', 'うるさい音のそばでも、我慢して座り続けている人のイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','stand','short','neutral')}
<g transform="translate(430 240)">
  <path d="M-60-60h120v120h-120z" class="coralp o"/>
  <circle r="30" class="coral o"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:5">
  <path d="M340 200q-26 26-26 40t26 40"/><path d="M300 180q-34 34-34 60t34 60"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 200l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('use', '道具を実際に手に取って、作業に役立てているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="goldp"/>
{hand(200,220,1)}
<g transform="translate(340 240) rotate(-14)">
  <path d="M-70-16h140v32h-140z" class="goldd o"/>
  <path d="M70-24h40v48H70z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M300 320h140" class="a" marker-end="url(#ar)"/>
{box(470,320,80,60,0,'gold')}
""", ground=True, arrow=True)

add('vehicle', '車・トラック・バスなど、人や物を運ぶ乗り物を並べたイラスト。', f"""
<g transform="translate(140 250) scale(0.6)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <path d="M-110-16h80v-44h-58zM-10-60h74l26 44H-10z" class="bluep o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g transform="translate(360 250) scale(0.6)">
  <path d="M-200 40h130v-120h-130z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-70 40h270v-90H-70z" class="tealp o"/>
  <path d="M-190-60h100v40h-100z" class="bluep o"/>
  <circle cx="-150" cy="52" r="30" class="ink"/><circle cx="110" cy="52" r="30" class="ink"/>
</g>
<g transform="translate(300 350) scale(0.5)">
  <path d="M-200-60h400v100h-400z" class="goldp o"/>
  <g class="bluep o"><rect x="-170" y="-40" width="60" height="40"/><rect x="-90" y="-40" width="60" height="40"/><rect x="-10" y="-40" width="60" height="40"/><rect x="70" y="-40" width="60" height="40"/></g>
  <circle cx="-120" cy="46" r="26" class="ink"/><circle cx="120" cy="46" r="26" class="ink"/>
</g>
""", ground=True)

add('withdraw', '現金自動機からお金を引き出しているイラスト。', f"""
<g transform="translate(340 220)">
  <path d="M-110-140h220v280h-220z" fill="#dfe6ea" class="o"/>
  <path d="M-80-110h160v70h-160z" class="bluep o"/>
  <g class="ink"><rect x="-70" y="-20" width="30" height="24"/><rect x="-30" y="-20" width="30" height="24"/><rect x="10" y="-20" width="30" height="24"/></g>
  <path d="M-60 60h120v20h-120z" class="ink"/>
</g>
<g transform="translate(200 290)">
  <path d="M-50-20h100v40h-100z" class="greenp o"/>
  <circle r="12" class="green o"/>
</g>
<path d="M270 290h-30" class="a" marker-end="url(#ar)"/>
{hand(140,240,1)}
""", ground=True, arrow=True)

add('witness', '事故の場面を、そばで実際に見ていた人のイラスト。', f"""
<g transform="translate(430 300) scale(0.7)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M320 180l-30-30M360 160v-40M280 220h-40"/></g>
{person(140,346,1.15,1,'teal','blue','point','short','surprised')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M200 220h120" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('abroad', '海をこえて、別の国へ渡っていくイラスト。', f"""
<path d="M0 260h600v140H0z" class="bluep"/>
<path d="M0 260h150v140H0zM450 260h150v140H450z" class="ground"/>
<path d="M0 260h150M450 260h150" class="a"/>
{building(70,260,0.5,'teal')}
{building(530,260,0.5,'gold')}
{plane(300,150,0.8,-6,'teal')}
<path d="M150 220q140-80 300-20" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('absent', 'いすが並ぶ中で、一つだけ人がいない空席があるイラスト。', f"""
{person(140,336,1.0,1,'teal','blue','stand','short','smile')}
{person(460,336,1.0,1,'violet','gold','stand','bob','smile')}
<g class="goldp o">
  <rect x="100" y="340" width="80" height="16"/><rect x="260" y="340" width="80" height="16"/><rect x="420" y="340" width="80" height="16"/>
</g>
<circle cx="300" cy="250" r="50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
<g class="corals" style="stroke-width:7"><path d="M280 230l40 40M320 230l-40 40"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('act', '思い立った人が、実際に立ち上がって動き出すイラスト。', f"""
{person(200,346,1.1,1,'teal','blue','walk','short','neutral')}
<g opacity=".4">{person(120,346,1.1,1,'teal','blue','stand','short','neutral')}</g>
<path d="M280 250h140" class="a" marker-end="url(#ar)"/>
{box(500,300,90,66,0,'gold')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
