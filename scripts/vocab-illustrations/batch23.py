"""第23回: 修理・凍る・狩る・隠すなど30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('file', '書類をフォルダに入れて、棚に保管しているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="bluep"/>
<g transform="translate(230 250) rotate(-6)">
  <path d="M-90-100h180v200h-180z" class="bluep o"/>
  <path d="M-70-116h100v16h-100z" class="blue o"/>
  <path d="M-60-70h120v130h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-40h80M-40-14h80M-40 12h60"/></g>
</g>
<g transform="translate(440 290)">
  <path d="M-80-60h160v120h-160z" class="goldp o"/>
  <path d="M-80 0h160" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
</g>
<path d="M340 240h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('firearm', '引き金と銃身のある銃を、横から見たイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-20h240v30h-240z" fill="#5d6b78" stroke="{INK}" stroke-width="3"/>
  <path d="M-160 10h60v40q0 30-30 30t-30-30z" class="goldd o"/>
  <path d="M-100 10h16v34h-16z" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M60-30h30v10H60z" fill="#5d6b78" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('firework', '夜空に打ち上がった花火が広がっているイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a4a"/>
<g transform="translate(240 160)" fill="none" stroke-linecap="round">
  <g stroke="{TONES['coral'][0]}" stroke-width="5">{''.join(f'<path d="M0 0l{int(100*__import__("math").cos(i*3.14159/6))} {int(100*__import__("math").sin(i*3.14159/6))}"/>' for i in range(12))}</g>
  <g fill="{TONES['gold'][0]}" stroke="none">{''.join(f'<circle cx="{int(110*__import__("math").cos(i*3.14159/6))}" cy="{int(110*__import__("math").sin(i*3.14159/6))}" r="6"/>' for i in range(12))}</g>
</g>
<g transform="translate(430 250) scale(0.6)" fill="none" stroke="{TONES['gold'][0]}" stroke-width="6" stroke-linecap="round">
  {''.join(f'<path d="M0 0l{int(100*__import__("math").cos(i*3.14159/4))} {int(100*__import__("math").sin(i*3.14159/4))}"/>' for i in range(8))}
</g>
<g fill="#f7e6a8"><circle cx="120" cy="330" r="3"/><circle cx="520" cy="90" r="3"/></g>
""", ground=False)

add('fit', 'ちょうどの大きさの穴に、部品がぴったり収まるイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-140-40h280v100h-280z" class="goldp o"/>
  <path d="M-50-40h100v60h-100z" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(300 160)">
  <path d="M-48-30h96v58h-96z" class="teal o"/>
</g>
<path d="M300 200v40" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M460 180l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('fix', '壊れた機器を工具で直しているイラスト。', f"""
<g transform="translate(320 260)">
  <path d="M-110-80h220v160h-220z" fill="#dfe6ea" class="o"/>
  <path d="M-80-50h160v90h-160z" class="bluep o"/>
  <g class="green o"><circle cx="-80" cy="58" r="12"/></g>
</g>
<g transform="translate(180 190) rotate(-24)">
  <path d="M-26-90q-16-26 4-38 20-12 40 0 20 12 6 38l-12 12h-26z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-11-78h22v150h-22z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 160l18 18 30-36"/></g>
""", ground=True)

add('flavour', '料理の香りが立ちのぼり、味わいを感じているイラスト。', f"""
<g transform="translate(240 300)">
  <ellipse rx="90" ry="30" fill="#fffdf6" class="o"/>
  <g class="coralp o"><circle cx="-30" cy="-14" r="20"/><circle cx="10" cy="-8" r="20"/></g>
</g>
<g class="muted" opacity=".9"><path d="M210 240q-16-40 6-70M250 232q-16-44 8-76M290 244q-16-40 6-70"/></g>
<g transform="translate(430 230)">
  <circle r="52" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-16" cy="-14" r="3.4" class="ink"/><circle cx="16" cy="-14" r="3.4" class="ink"/>
  <path d="M-4-4q-8 10 4 12" fill="none" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-10 20q10 10 20 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M340 220q30-6 44 0" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('fleet', '同じ形の船が何隻も並んで進む艦隊のイラスト。', f"""
<path d="M0 250h600v150H0z" class="bluep"/>
<path d="M0 250q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
{''.join(f'<g transform="translate({120+i*160} {250+ (i%2)*50}) scale({0.7 - (i%2)*0.1})"><path d="M-110 0h220l-24 34h-172z" class="teal o"/><path d="M-40 0v-40h70v40z" class="paper"/><path d="M-5-40v-30" class="a"/></g>' for i in range(3))}
<path d="M120 160h240" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('flood', '水があふれて、家の低い部分まで浸かっているイラスト。', f"""
{building(300,300,1.0,'teal')}
<path d="M0 300h600v100H0z" class="bluep o"/>
<path d="M0 300q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g class="blues" opacity=".7"><path d="M60 340q50-14 100 0t100 0M340 360q50-14 100 0t100 0"/></g>
<path d="M500 240v40" class="blues" marker-end="url(#ar)" style="stroke-width:6"/>
""", ground=False, arrow=True)

add('forward', '前方へ進む向きを、矢印で示したイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','walk','short','smile')}
<path d="M280 240h240" class="a" marker-end="url(#ar)" style="stroke-width:8"/>
<g class="muted"><path d="M140 300h-60M150 340h-70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('foundation', '建物の下に打たれた基礎の部分を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-120-100h240v170h-240z" fill="#fffdf6" class="o"/>
  <path d="M-136-100L0-180l136 80z" class="teal o"/>
  <g class="bluep o"><rect x="-80" y="-70" width="60" height="50"/><rect x="20" y="-70" width="60" height="50"/></g>
</g>
<path d="M150 290h300v70H150z" class="goldd o"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 8"><path d="M120 290h360"/></g>
<path d="M500 300v50" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('freeze', '水が冷えて、氷になって固まるイラスト。', f"""
<g transform="translate(170 260)">
  <path d="M-70-90h140l-10 170h-120z" fill="#f7fbfe" class="o"/>
  <path d="M-62-20h124l-8 110h-108z" class="bluep o"/>
  <path d="M-62-20h124" class="a"/>
</g>
<g transform="translate(430 260)">
  <path d="M-70-90h140l-10 170h-120z" fill="#f7fbfe" class="o"/>
  <path d="M-62-20h124l-8 110h-108z" fill="#e8f4fb" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#ffffff" stroke-width="4"><path d="M-30 20l60 40M30 20l-60 40M0 0v90"/></g>
</g>
<path d="M270 240h60" class="blues" marker-end="url(#ar)"/>
<g class="blues" style="stroke-width:4"><path d="M300 180v-30"/></g>
""", ground=True, arrow=True)

add('fresh', 'とれたての野菜が、みずみずしく並んでいるイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
<g transform="translate(280 290)">
  <path d="M-140-20h280l-16 60h-248z" class="goldp o"/>
  <g transform="translate(-70 -40)">
    <ellipse rx="34" ry="46" class="green o"/>
    <path d="M0-46v-20" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  </g>
  <g transform="translate(0 -30)"><circle r="34" class="coral o"/><path d="M0-34v-14" class="a"/></g>
  <g transform="translate(70 -40)">
    <ellipse rx="30" ry="44" class="gold o"/>
    <path d="M0-44v-16" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
  </g>
</g>
{drop(200,180,1.0)}{drop(360,170,1.0)}
""", ground=True)

add('fry', 'フライパンで油を使って、具材を炒めているイラスト。', f"""
<g transform="translate(280 260)">
  <path d="M-110-20h220l-14 50h-192z" fill="#5d6b78" stroke="{INK}" stroke-width="3"/>
  <path d="M110-10h130v18H110z" class="goldd o"/>
  <g class="goldp o"><circle cx="-50" cy="-4" r="16"/><circle cx="0" cy="4" r="16"/><circle cx="50" cy="-4" r="16"/></g>
</g>
{flame(280,340,0.85)}
<g class="muted" opacity=".85"><path d="M240 180q-16-40 6-70M320 176q-16-44 8-76"/></g>
""", ground=True)

add('fun', '遊具で遊んで、笑い声が上がっているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160 60L-40-80h80L160 60z" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linejoin="round"/>
  <path d="M-40-80h80v14h-80z" class="goldd o"/>
  <path d="M40-70L160 60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16"/>
</g>
{person(210,300,0.85,1,'coral','blue','up','bob','smile')}
<g class="golds" style="stroke-width:4"><path d="M160 200l-24-24M270 190l-8-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('further', '近い地点よりもっと遠くの地点を、長い矢印で示したイラスト。', f"""
<circle cx="90" cy="250" r="20" class="teal o"/>
<circle cx="280" cy="250" r="20" class="goldp o"/>
<circle cx="520" cy="250" r="20" class="coral o"/>
<path d="M110 200h150" class="muted" marker-end="url(#ar)"/>
<path d="M110 320h390" class="a" marker-end="url(#ar)" style="stroke-width:6"/>
""", ground=False, arrow=True)

add('gear', '登山の装備が一そろい並んでいるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-220-20h440v20h-440z" class="goldp o"/>
</g>
<g transform="translate(140 250)">
  <path d="M-50-50h100v90h-100z" class="tealp o"/>
  <path d="M-30-50q0-30 30-30t30 30" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
<g transform="translate(300 250)">
  <path d="M-40 0a40 30 0 0 1 80 0z" class="coral o"/>
  <ellipse cy="2" rx="56" ry="12" class="coralp o"/>
</g>
<g transform="translate(440 250)">
  <path d="M-40 20q40-60 80 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="16" stroke-linecap="round"/>
  <path d="M-40 40q40-60 80 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="16" stroke-linecap="round"/>
</g>
""", ground=True)

add('general', '細かい違いを気にせず、全体をまとめて示したイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{140+ (i%5)*80}" cy="{190 + (i//5)*90}" r="30"/>' for i in range(10))}
</g>
<path d="M90 140h420v250H90z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 10"/>
<path d="M300 400v0" class="a"/>
""", ground=False)

add('gig', '小さな会場で一晩の演奏をしているイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-200-20h400v40h-400z" class="goldd o"/>
</g>
{person(280,310,1.1,1,'violet','blue','carry','bun','smile')}
<g transform="translate(330 250) rotate(-16)">
  <path d="M0-60q40 0 40 34 0 20-14 26 14 10 14 30 0 36-40 36s-40 0-40-36q0-20 14-30-14-6-14-26 0-34 40-34z" class="goldp o"/>
  <circle cy="16" r="16" class="goldd o"/>
  <path d="M-6-60h12v-70h-12z" class="goldd o"/>
</g>
<g fill="{INK}"><g transform="translate(450 200) scale(0.8)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g></g>
<g opacity=".6">{person(140,366,0.7,1,'coral','gold','up','short','smile')}</g>
""", ground=False)

add('grade', '成績を段階に分けて、上から順に並べたイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-120h320v240h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-160-60h320M-160 0h320M-160 60h320"/></g>
  <g fill="{INK}">
    <rect x="-120" y="-96" width="60" height="8"/><rect x="-120" y="-36" width="60" height="8"/><rect x="-120" y="24" width="60" height="8"/>
  </g>
  <g class="coral o"><circle cx="100" cy="-90" r="20"/></g>
  <g class="goldp o"><circle cx="100" cy="-30" r="20"/></g>
  <g class="tealp o"><circle cx="100" cy="30" r="20"/></g>
</g>
<path d="M120 380h360" class="a"/>
""", ground=True)

add('grocery', '食料品が並んだ店先のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-190 110V-60h380v170z" fill="#fffdf6" class="o"/>
  <path d="M-206-60h412l-40-50h-332z" class="green o"/>
  <path d="M-150-30h130v60h-130z" class="goldp o"/>
  <g class="coral o"><circle cx="-120" cy="-10" r="12"/><circle cx="-90" cy="-10" r="12"/></g>
  <g class="greenp o"><rect x="-60" y="-24" width="30" height="24"/></g>
  <path d="M20-30h130v60H20z" class="goldp o"/>
  <g class="gold o"><circle cx="50" cy="-10" r="12"/><circle cx="80" cy="-10" r="12"/></g>
</g>
<path d="M60 360h480" class="a"/>
""", ground=True)

add('guard', '入口の前に立って、見張っている警備員のイラスト。', f"""
{building(430,300,0.9,'teal')}
{person(200,346,1.2,1,'blue','violet','stand','cap','neutral')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M260 220h60" marker-end="url(#ar)"/></g>
<g class="muted"><path d="M120 240v100"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('head', '列の先頭に立って、集団を率いているイラスト。', f"""
{person(160,346,1.2,1,'coral','blue','walk','cap','neutral')}
{person(310,346,0.95,1,'teal','gold','walk','bob','neutral')}
{person(430,346,0.95,1,'violet','teal','walk','short','neutral')}
<circle cx="160" cy="212" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M110 240h-50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('heel', 'くつのかかとの位置を示したイラスト。', f"""
<g transform="translate(280 260)">
  <path d="M-140 60q0-40 40-50l80-20q60-14 90 10 20 16 0 30l-40 30z" class="coralp o"/>
  <path d="M-140 60h250v20h-250z" class="ink"/>
  <path d="M-140 60q-10-30 10-40" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
  <circle cx="-120" cy="46" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
</g>
<path d="M120 360h360" class="a"/>
""", ground=True)

add('hide', '箱の後ろに隠れて、姿を見せないイラスト。', f"""
<g transform="translate(360 300)">
  <path d="M-120-60h240v120h-240z" class="goldp o"/>
  <path d="M-120-60l30-30h240l-30 30z" class="gold o"/>
</g>
<g transform="translate(300 260)">
  <circle r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-26-4q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
  <circle cx="-8" cy="2" r="2.4" class="ink"/><circle cx="8" cy="2" r="2.4" class="ink"/>
</g>
{person(140,346,0.9,1,'teal','blue','point','cap','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M200 240h100" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('highway', '車線が分かれた広い幹線道路のイラスト。', f"""
<path d="M0 170h600v230H0z" fill="#d8d3ca"/>
<path d="M0 170h600" class="a"/>
<g fill="none" stroke="#fffdf6" stroke-width="6" stroke-dasharray="40 30"><path d="M0 250h600M0 320h600"/></g>
<g transform="translate(200 220) scale(0.45)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g transform="translate(420 300) scale(0.45)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="teal o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
""", ground=False)

add('hire', '面接して、新しい人を雇い入れるイラスト。', f"""
{person(160,346,1.1,1,'coral','blue','give','bob','smile')}
{person(440,346,1.1,-1,'teal','violet','give','short','smile')}
<g transform="translate(300 250)">
  <path d="M-56-70h112v140h-112z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-34-40h68M-34-16h68"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-24 30l14 14 24-28"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('historian', '古い記録を調べて、歴史をまとめている人のイラスト。', f"""
{person(160,346,1.15,1,'gold','blue','point','bun','neutral')}
<g transform="translate(400 250)">
  <path d="M-130-70h260v140h-260z" fill="#f3e6c8" stroke="{INK}" stroke-width="3"/>
  <ellipse cx="-130" cy="0" rx="18" ry="70" class="goldd o"/>
  <ellipse cx="130" cy="0" rx="18" ry="70" class="goldd o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-40h190M-100-10h190M-100 20h150"/></g>
</g>
<path d="M240 220h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('honesty', '拾った財布を、正直に届けているイラスト。', f"""
<circle cx="300" cy="130" r="70" class="greenp"/>
<g transform="translate(300 176)"><path d="M-30 20l30-40 30 40z" class="green o"/></g>
{person(170,346,1.1,1,'teal','blue','give','short','smile')}
{person(430,346,1.1,-1,'coral','gold','give','bob','smile')}
<g transform="translate(300 280)">
  <path d="M-50-30h100v60h-100z" class="goldd o"/>
  <path d="M-50-6h100" fill="none" stroke="{TONES['gold'][1]}" stroke-width="5"/>
</g>
<path d="M240 280h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('host', '客を迎え入れて、会をもてなしている人のイラスト。', f"""
{building(430,300,0.85,'teal')}
{person(180,346,1.15,1,'coral','blue','give','bob','smile')}
{person(320,346,0.95,-1,'teal','gold','walk','short','smile')}
<path d="M240 220h50" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:4"><path d="M150 200l-24-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('household', '一つの家に暮らす家族のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-180 110V-40h360v150z" fill="#fffdf6" class="o"/>
  <path d="M-196-40L0-140l196 100z" class="teal o"/>
</g>
{person(230,346,0.85,1,'coral','blue','stand','short','smile')}
{person(310,346,0.85,1,'gold','violet','stand','bob','smile')}
{person(380,346,0.6,1,'violet','teal','stand','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('hunt', '弓を持って、野生の動物を追って探しているイラスト。', f"""
{tree(100,340,0.7)}{tree(520,340,0.6)}
{person(200,346,1.05,1,'gold','blue','point','cap','neutral')}
<g transform="translate(420 310)">
  <ellipse cx="0" cy="0" rx="66" ry="36" class="goldp o"/>
  <path d="M-44 30v26M-12 34v22M18 34v22M44 26v30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
  <g transform="translate(70 -30)">
    <ellipse rx="28" ry="22" class="goldp o"/>
    <path d="M-14-20q-12-30 8-30 16 0 16 22z" class="goldd o"/>
    <circle cx="8" cy="-4" r="3" class="ink"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M270 250h80" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('hurry', '時計を見ながら、走って急いでいるイラスト。', f"""
<g transform="translate(450 160)">
  <circle r="56" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-34M0 0l26 16" class="a"/>
</g>
{person(230,346,1.2,1,'coral','blue','walk','short','surprised')}
<g class="muted"><path d="M150 280h-60M160 320h-70M140 240h-50"/></g>
<path d="M320 250h70" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('hydrogen', '水素の分子が、二つの小さな球で表されたイラスト。', f"""
<g transform="translate(240 220)">
  <circle cx="-50" r="60" class="bluep o"/>
  <circle cx="50" r="60" class="bluep o"/>
  <path d="M-50 0h100" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g transform="translate(440 300)">
  <circle r="34" class="bluep o"/>
  <circle cx="-40" cy="-30" r="20" class="bluep o"/>
  <circle cx="40" cy="-30" r="20" class="bluep o"/>
  <path d="M-30-22L-8-10M30-22L8-10" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<path d="M120 360h360" class="muted"/>
""", ground=False)
print(' '.join(W)); print(sheet(W))
