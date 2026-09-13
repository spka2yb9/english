"""第39回: 凍る・生み出す・握る・治すなど42語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('frozen', '氷になって固まった水のイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-90-100h180l-12 200h-156z" fill="#f7fbfe" class="o"/>
  <path d="M-80-30h160l-10 130h-140z" fill="#e8f4fb" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#ffffff" stroke-width="5"><path d="M-40 10l80 60M40 10l-80 60M0-20v110"/></g>
</g>
{thermometer(470,300,0.15,1.0)}
""", ground=True)

add('fulfil', '約束の一覧すべてに印がついて、果たされたイラスト。', f"""
<g transform="translate(290 240)">
  <path d="M-130-130h260v260h-260z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-50 {-90+i*45}h150"/>' for i in range(5))}</g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
    {''.join(f'<path d="M-100 {-94+i*45}l12 12 20-24"/>' for i in range(5))}
  </g>
</g>
{person(500,346,0.85,-1,'teal','blue','up','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fulfill', '思い描いた夢が、実物として実現するイラスト。', f"""
<g transform="translate(160 200)">
  <path d="M-110-50q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 6)">{building(0,20,0.4,'teal')}</g>
</g>
{building(440,330,0.95,'teal')}
<path d="M290 230h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 140l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('furthermore', '説明の下に、さらに項目が付け足されるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-120-100h240M-120-70h240M-120-40h200"/></g>
  <path d="M-130 0h260" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="8 8"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M-120 40h240M-120 70h200"/></g>
  <g class="teals" style="stroke-width:8"><path d="M-152 20h-0M-150 10v20M-160 20h20"/></g>
</g>
""", ground=True)

add('gallery', '壁に絵が並んだ、展示室のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-240-120h480v240h-240z" fill="#fffdf6" class="o"/>
  <g class="goldd o"><rect x="-200" y="-90" width="110" height="90"/><rect x="-50" y="-90" width="110" height="90"/><rect x="100" y="-90" width="110" height="90"/></g>
  <g class="tealp o"><rect x="-188" y="-78" width="86" height="66"/><rect x="-38" y="-78" width="86" height="66"/><rect x="112" y="-78" width="86" height="66"/></g>
</g>
{person(300,340,0.85,-1,'coral','blue','point','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('gas', 'ボンベから、目に見えない気体が出ているイラスト。', f"""
<g transform="translate(220 260)">
  <path d="M-50-90h100v170h-100z" class="tealp o"/>
  <path d="M-50-90a50 40 0 0 1 100 0z" class="tealp o"/>
  <path d="M-16-136h32v46h-32z" class="ink"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8">
  <path d="M280 160q60-30 120 0M300 210q60-30 120 0M290 260q60-30 120 0"/>
</g>
<g fill="#cfd8de" opacity=".7"><circle cx="440" cy="150" r="16"/><circle cx="480" cy="200" r="12"/></g>
""", ground=True)

add('generate', '発電機が回って、電気を生み出すイラスト。', f"""
<g transform="translate(220 250)">
  <circle r="90" fill="none" stroke="{INK}" stroke-width="18"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="9">{''.join(f'<path d="M0 -70v-20" transform="rotate({i*45})"/>' for i in range(8))}</g>
  <circle r="22" class="goldd o"/>
</g>
<path d="M220 130a120 120 0 0 1 90 44" class="muted" marker-end="url(#ar)"/>
<g transform="translate(450 250)">
  <path d="M-14-40l-16 46h20l-10 34 30-50h-20l16-30z" class="gold o"/>
</g>
<path d="M330 250h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('generous', 'たっぷりの量を分け与えているイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','give','bob','smile')}
{person(450,346,1.1,-1,'coral','gold','hold','short','smile')}
<g transform="translate(300 250)">
  <path d="M-70-40h140l-12 90h-116z" class="goldp o"/>
  <g class="coral o"><circle cx="-30" cy="-52" r="20"/><circle cx="10" cy="-58" r="20"/><circle cx="46" cy="-48" r="20"/></g>
</g>
<path d="M370 200h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('gentle', '子猫をそっと、優しくなでているイラスト。', f"""
{hand(180,240,1)}
<g transform="translate(360 300)">
  <ellipse cx="0" cy="-10" rx="76" ry="42" class="goldp o"/>
  <circle cx="66" cy="-46" r="34" class="goldp o"/>
  <path d="M40-70q-12-30 8-30 16 0 16 22zM86-72q16-28 32-10 12 14-8 28z" class="goldd o"/>
  <circle cx="56" cy="-46" r="3.4" class="ink"/><circle cx="78" cy="-46" r="3.4" class="ink"/>
  <path d="M-76-20q-30 6-30 40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9" stroke-linecap="round"/>
</g>
<g class="muted"><path d="M250 210q40-20 70-10"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('gift', '生まれつきの才能が、輝いて示されるイラスト。', f"""
{person(280,346,1.25,1,'violet','blue','up','bun','smile')}
<g transform="translate(280 150)">
  <path d="M0-40l14 28 30 4-22 22 6 30-28-16-28 16 6-30-22-22 30-4z" class="gold o"/>
</g>
<g class="golds" style="stroke-width:4"><path d="M180 200l-24-24M380 200l24-24M170 260h-30M390 260h30"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('glad', 'よい知らせを受けて、うれしそうにしている人のイラスト。', f"""
{person(220,346,1.2,1,'coral','blue','up','bob','smile')}
<g transform="translate(430 230)">
  <path d="M-70-46h140v92h-140z" class="paper"/>
  <path d="M-70-46L0 6l70-52" fill="none" class="a"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-20 30l14 14 26-30"/></g>
</g>
<g class="golds" style="stroke-width:4"><path d="M310 200l24-24M300 260h-26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('global', '地球全体をまわる線で、世界規模を示したイラスト。', f"""
<circle cx="300" cy="210" r="140" class="bluep o"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M160 210h280M300 70v280M300 70q70 70 0 280M300 70q-70 70 0 280"/></g>
<path d="M240 160q60 30 130 10q-20 60-90 60t-60-40z" class="greenp o"/>
<g class="a" marker-end="url(#ar)"><path d="M300 40a170 170 0 0 1 150 90"/></g>
""", ground=False, arrow=True)

add('god', '天から光が差す、信仰の対象を示したイラスト。', f"""
<circle cx="300" cy="120" r="100" class="goldp" opacity=".55"/>
<g class="golds" style="stroke-width:5">
  <path d="M300 240v40M200 200l-40 40M400 200l40 40M180 130h-40M420 130h40"/>
</g>
{person(300,366,1.0,1,'violet','blue','hold','bob','neutral')}
<g transform="translate(300 274)">
  <path d="M-8-30q-14 30 0 60M8-30q14 30 0 60" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
</g>
<path d="M80 386h440" class="a"/>
""", ground=True)

add('gold', '金色に輝く金塊のイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-140-30h280l-30-40h-220z" class="gold o"/>
  <path d="M-140-30h280v60h-280z" class="goldd o"/>
  <path d="M-110-56h220" fill="none" stroke="{TONES['gold'][1]}" stroke-width="4"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M180 180l-24-24M420 180l24-24M300 150v-26"/></g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('golf', 'クラブでボールを打って、穴を狙うゴルフのイラスト。', f"""
<path d="M0 280q120-30 300 0t300-10v130H0z" fill="#e4efe2" stroke="{INK}" stroke-width="3"/>
<g transform="translate(180 290) rotate(-30)">
  <path d="M-10-120h20v120h-20z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 0h44v20h-44z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<circle cx="250" cy="300" r="14" fill="#fffdf6" class="o"/>
<g transform="translate(470 260)">
  <ellipse cy="34" rx="26" ry="9" class="ink"/>
  <path d="M0 30V-60" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M4-60l50 16-50 16z" class="coral o"/>
</g>
<path d="M280 280q100-50 180-10" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('good', '評価が高いことを示す、親指を立てた手のイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-70 90q-20-90 0-110 6-14 30-14h60q16 0 16 20v84q0 20-20 20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-70-20q-30-70 0-90 24-14 24 16v40z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2.5"><path d="M-20 20h56M-20 50h56"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M450 200l20 20 34-40"/></g>
""", ground=True)

add('grass', '一面に生えた芝生のイラスト。', f"""
<path d="M0 240h600v160H0z" fill="#e4efe2"/>
<path d="M0 240h600" class="a" opacity=".4"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="4" stroke-linecap="round">
  {''.join(f'<path d="M{40+i*28} 260q4-24 {-6 if i%2 else 8}-40"/>' for i in range(20))}
  {''.join(f'<path d="M{50+i*30} 330q4-26 {8 if i%2 else -6}-42"/>' for i in range(18))}
</g>
""", ground=False)

add('grateful', '受けた助けに、手を合わせて感謝するイラスト。', f"""
<circle cx="300" cy="140" r="76" class="goldp"/>
<g transform="translate(300 176)"><path d="M0 24l-28-34 14-16 14 14 14-14 14 16z" class="coral o"/></g>
{person(300,346,1.3,1,'teal','blue','hold','bob','smile')}
<g transform="translate(300 258)">
  <path d="M-8-26q-14 26 0 52M8-26q14 26 0 52" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('grind', 'ひきうすで粒をすりつぶして、粉にするイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-90-40h180v40h-180z" fill="#b9b1a3" stroke="{INK}" stroke-width="3"/>
  <path d="M-90 0h180v40h-180z" fill="#a49c8e" stroke="{INK}" stroke-width="3"/>
  <path d="M60-60h20v20h-20z" class="goldd o"/>
</g>
<path d="M280 160a120 120 0 0 1 90 40" class="muted" marker-end="url(#ar)"/>
<g fill="#e7dcc9"><circle cx="240" cy="330" r="7"/><circle cx="290" cy="340" r="6"/><circle cx="330" cy="330" r="5"/></g>
<path d="M120 360h360" class="a"/>
""", ground=True, arrow=True)

add('grip', '取っ手をしっかり握りしめているイラスト。', f"""
<path d="M300 380V100" fill="none" stroke="{TONES['gold'][2]}" stroke-width="22" stroke-linecap="round"/>
<g transform="translate(300 240)">
  <path d="M-56-38h112q18 0 18 18v40q0 18-18 18h-112q-18 0-18-18v-40q0-18 18-18z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2"><path d="M-30-38v76M-2-38v76M26-38v76"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M170 300q40-30 70-40"/><path d="M430 300q-40-30-70-40"/></g>
""", ground=True, arrow=True)

add('ground', '足元に広がる地面を示したイラスト。', f"""
<path d="M0 280h600v120H0z" fill="#e7d9c4"/>
<path d="M0 280h600" class="a"/>
{person(300,280,1.1,1,'teal','blue','stand','short','smile')}
<path d="M120 350h360" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<g fill="#c9a97c"><circle cx="150" cy="320" r="7"/><circle cx="480" cy="340" r="6"/></g>
""", ground=False, arrow=True)

add('guarantee', '保証の印がついた札を、品物に添えるイラスト。', f"""
{box(230,270,150,110,0,'gold')}
<g transform="translate(430 220) rotate(-8)">
  <path d="M-60-40h120v80h-120z" class="paper"/>
  <circle cx="0" cy="0" r="24" fill="none" stroke="{TONES['green'][0]}" stroke-width="5"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-12 0l10 10 18-20"/></g>
</g>
<path d="M360 240l-30 10" class="a" marker-end="url(#ar)"/>
<path d="M120 380h380" class="a"/>
""", ground=True, arrow=True)

add('guest', '玄関で迎えられて、家に招かれる客のイラスト。', f"""
{building(430,300,0.9,'teal')}
{person(180,346,1.1,1,'coral','blue','walk','bob','smile')}
{person(330,346,1.05,-1,'teal','gold','give','short','smile')}
<path d="M250 230h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('guilty', '悪いことをしたと感じて、うつむいている人のイラスト。', f"""
{person(280,346,1.25,1,'violet','blue','hold','short','sad')}
{cloud(430,150,1.3,'violet')}
<g class="corals" style="stroke-width:6"><path d="M410 190v26M456 196v22"/></g>
<g transform="translate(150 220)">
  <path d="M-40-24h80v48h-80z" class="paper"/>
  <g class="corals" style="stroke-width:5"><path d="M-16-8l32 16M16-8l-32 16"/></g>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('gun', '引き金と銃身を備えた銃のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-150-20h230v28h-230z" fill="#5d6b78" stroke="{INK}" stroke-width="3"/>
  <path d="M-150 8h60v40q0 28-30 28t-30-28z" class="goldd o"/>
  <path d="M-92 8h16v32h-16z" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M60-30h28v10H60z" fill="#5d6b78" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)

add('guy', '気軽な服装の男性が立っているイラスト。', f"""
{person(280,346,1.3,1,'teal','blue','stand','short','smile')}
<g transform="translate(280 216)"><path d="M-34-4a34 26 0 0 1 68 0z" class="blue o"/><path d="M34-4h34v8H34z" class="blued o"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('habit', '毎朝同じ動作をくり返す、習慣を示したイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="10">
  <circle cx="300" cy="220" r="130" stroke-dasharray="20 14"/>
</g>
{sun(300,90,26)}
<g transform="translate(430 220)">
  <path d="M-40-40h80l-8 80h-64z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(300 350)"><path d="M-30-16h60v32h-60z" class="tealp o"/></g>
<g transform="translate(170 220)"><circle r="26" class="goldp o"/></g>
<path d="M380 120a140 140 0 0 1 40 60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('hail', '空から氷の粒が降ってくるイラスト。', f"""
{cloud(300,110,1.9)}
<g fill="#e8f4fb" stroke="{TONES['blue'][0]}" stroke-width="2.5">
  {''.join(f'<circle cx="{160+i*50}" cy="{220 + (i%3)*50}" r="11"/>' for i in range(8))}
</g>
<path d="M0 380h600" class="ground"/>
<path d="M0 380h600" class="a"/>
""", ground=False)

add('hall', '天井の高い広間に、いすが並んだイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-240-140h480v280h-480z" fill="#fffdf6" class="o"/>
  <path d="M-240-140h480v40h-480z" class="goldd o"/>
  <g class="goldp o">{''.join(f'<rect x="{-200+i*70}" y="-20" width="50" height="16"/>' for i in range(6))}</g>
  <g class="goldp o">{''.join(f'<rect x="{-200+i*70}" y="50" width="50" height="16"/>' for i in range(6))}</g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('halt', '進んでいた列が、止まれの合図で停止するイラスト。', f"""
<path d="M60 300h300" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" stroke-linecap="round"/>
<g transform="translate(430 230)">
  <path d="M-60-60h120v120h-120z" class="coral o" transform="rotate(45)"/>
  <path d="M-30 0h60" fill="none" stroke="#fffdf6" stroke-width="10"/>
</g>
<g class="corals" style="stroke-width:8"><path d="M370 280l40 40M410 280l-40 40"/></g>
<path d="M150 360h150" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('haunt', '同じ影がいつまでも付いて回るイラスト。', f"""
{person(220,346,1.15,1,'coral','blue','walk','short','sad')}
<g fill="#3d4c5c" opacity=".65"><path d="M400 350q-24-80 30-104 46-20 74 14 30 40-18 90z"/></g>
<g fill="#f7e6a8"><circle cx="440" cy="270" r="7"/><circle cx="472" cy="270" r="7"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M380 250H300" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('heal', '傷口がふさがって、治っていくイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-90-70h180v140h-180z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40-20l14 20-18 20 16 20" fill="none" stroke="{TONES['coral'][2]}" stroke-width="5"/>
</g>
<g transform="translate(430 240)">
  <path d="M-90-70h180v140h-180z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30 0h60" fill="none" stroke="{SKINL}" stroke-width="3" stroke-dasharray="8 8"/>
</g>
<path d="M280 240h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 140l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('heart', '胸の中で動く心臓のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M0 90l-90-108 44-52 46 44 46-44 44 52z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][2]}" stroke-width="5" stroke-linecap="round">
  <path d="M100 340h90l20-36 26 70 24-52 18 18h130"/>
</g>
""", ground=False)

add('height', '人の身長を、目盛りで測って示したイラスト。', f"""
<path d="M150 100v260" fill="none" stroke="{INK}" stroke-width="5"/>
<g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M150 {120+i*40}h24"/>' for i in range(6))}</g>
{person(300,360,1.25,1,'teal','blue','stand','short','smile')}
<path d="M200 200h100" class="a" marker-end="url(#ar)"/>
<path d="M420 130v230" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('heighten', '低かった棒が、さらに高くなるイラスト。', f"""
<g class="tealp o"><rect x="150" y="240" width="100" height="120"/></g>
<rect x="350" y="140" width="100" height="220" class="teal o"/>
<path d="M280 220h50" class="a" marker-end="url(#ar)"/>
<path d="M400 110V70" class="a" marker-end="url(#ar)" transform="rotate(180 400 90)"/>
<path d="M60 360h480" class="a"/>
""", ground=False, arrow=True)

add('hero', '人を助けて、たたえられている英雄のイラスト。', f"""
<circle cx="300" cy="140" r="86" class="goldp" opacity=".55"/>
{person(300,346,1.3,1,'coral','blue','up','short','smile')}
<g transform="translate(300 300)">
  <path d="M-56-30q56-20 112 0l14 76h-140z" class="coralp o"/>
</g>
<g transform="translate(300 240)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('hers', '二つの持ち物のうち、片方が彼女のものと示すイラスト。', f"""
{person(160,346,1.15,1,'violet','blue','point','bob','smile')}
{box(360,300,110,80,0,'gold')}
{box(490,300,110,80,0,'teal')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4"><path d="M240 240h80" marker-end="url(#ar)"/></g>
<circle cx="360" cy="300" r="76" fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('herself', '鏡に映る自分を、本人が見ているイラスト。', f"""
<g transform="translate(420 210)">
  <path d="M-100-150h200v300h-200z" class="goldd o"/>
  <path d="M-84-134h168v268h-168z" class="bluep o"/>
</g>
<g opacity=".7">{person(430,330,0.92,-1,'violet','blue','point','bob','smile')}</g>
{person(170,346,1.1,1,'violet','blue','point','bob','smile')}
<path d="M250 210h60" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('hesitate', '一歩踏み出せずに、ためらっているイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','think','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"><path d="M280 300h160" marker-end="url(#ar)"/></g>
<g fill="{INK}"><path d="M320 180q0-24 24-24t24 24q0 16-18 22v10h-12v-18q18-2 18-14 0-10-12-10t-12 10z"/><circle cx="344" cy="238" r="7"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('hill', 'なだらかに盛り上がった丘のイラスト。', f"""
{sun(490,90,42)}
<path d="M0 320q100-120 240-100t360-40v220H0z" fill="#e4efe2" stroke="{INK}" stroke-width="3"/>
{tree(200,240,0.6)}{tree(430,240,0.5)}
<path d="M60 380h480" class="a" opacity=".3"/>
""", ground=False)

print(len(W), ' '.join(W)); print(sheet(W))
