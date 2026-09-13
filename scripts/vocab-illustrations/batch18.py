"""第18回: 感覚・段階・力・輸送など30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('slice', 'パンから薄い一切れを切り分けているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(250 290)">
  <path d="M-140 30h280l-16 26h-248z" class="paper"/>
  <path d="M-100-70q60-26 130 0 20 60 0 96h-130z" class="goldp o"/>
  <path d="M-40-64v90" class="a"/>
</g>
<g transform="translate(410 280) rotate(10)">
  <path d="M-40-70q30-14 60 0 10 56 0 92h-60z" class="goldp o"/>
</g>
<g transform="translate(300 150) rotate(16)">
  <path d="M-10-6h140l30 24h-170z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-80-4h70v22h-70z" class="ink"/>
</g>
<path d="M330 200v40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('smell', '花に鼻を近づけて、においをかいでいるイラスト。', f"""
<g transform="translate(420 300)">
  <path d="M0 40v-70" fill="none" stroke="{TONES['green'][2]}" stroke-width="8" stroke-linecap="round"/>
  <circle cy="-60" r="26" class="coral o"/>
  <g class="coralp o"><circle cx="-34" cy="-84" r="18"/><circle cx="34" cy="-84" r="18"/><circle cx="0" cy="-106" r="18"/><circle cx="-30" cy="-40" r="18"/><circle cx="30" cy="-40" r="18"/></g>
  <circle cy="-72" r="14" class="gold o"/>
</g>
<g transform="translate(200 210)">
  <circle r="80" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-28" cy="-20" r="5" class="ink"/><circle cx="28" cy="-20" r="5" class="ink"/>
  <path d="M6 0q-10 14 6 16" fill="none" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-14 40q14 10 28 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="muted"><path d="M300 220q40-16 66-10" marker-end="url(#ar)"/><path d="M300 250q40-6 60-6" marker-end="url(#ar)"/></g>
""", ground=True, arrow=True)

add('smoke', '煙突から灰色の煙が立ちのぼっているイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-120 60V-40h240V60z" fill="#fffdf6" class="o"/>
  <path d="M-136-40L0-130l136 90z" class="coral o"/>
  <path d="M60-104h34v50H60z" class="ink"/>
</g>
<g fill="#c9ccd1" stroke="{MUTED}" stroke-width="2.5" opacity=".9">
  <circle cx="380" cy="180" r="22"/><circle cx="416" cy="140" r="17"/><circle cx="446" cy="104" r="13"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('soil', '掘り返した土の層と、その中の根を示したイラスト。', f"""
<path d="M0 200h600v200H0z" fill="#e7d9c4"/>
<path d="M0 200h600" class="a"/>
<path d="M0 280h600" fill="none" stroke="#c9a97c" stroke-width="4" stroke-dasharray="14 10"/>
<path d="M0 340h600" fill="none" stroke="#b79f7c" stroke-width="4" stroke-dasharray="14 10"/>
<g transform="translate(300 200)">
  <path d="M0 0v-70" fill="none" stroke="{TONES['green'][2]}" stroke-width="8" stroke-linecap="round"/>
  <path d="M0-40c-34-10-44-32-44-32 32-8 44 32 44 32z" class="green o"/>
  <g fill="none" stroke="#c9a97c" stroke-width="6" stroke-linecap="round"><path d="M0 0v90M0 30l-50 44M0 40l54 40"/></g>
</g>
<g fill="#c9a97c"><circle cx="120" cy="250" r="7"/><circle cx="480" cy="300" r="6"/></g>
""", ground=False)

add('sole', 'たくさんの席の中で、一つだけ埋まっている席のイラスト。', f"""
<g class="tealp o">
  {''.join(f'<rect x="{80+ (i%6)*80}" y="{190 + (i//6)*90}" width="60" height="20"/>' for i in range(12))}
</g>
{person(190,210,0.55,1,'coral','blue','stand','short','smile')}
<circle cx="110" cy="200" r="52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 360h480" class="muted"/>
""", ground=False)

add('solid', '形が変わらない固体の立方体と、流れる液体を比べたイラスト。', f"""
<g transform="translate(180 250)">{box(0,0,140,110,32,'gold')}</g>
<g transform="translate(430 260)">
  <path d="M-80-60h160l-14 120h-132z" fill="#f4fbff" class="o"/>
  <path d="M-70 0h140l-10 60h-120z" class="bluep o"/>
  <path d="M-70 0h140" class="a"/>
</g>
<path d="M300 130v230" class="muted"/>
<path d="M120 350h360" class="a"/>
""", ground=True)

add('sort', '混ざった三色の玉を、色ごとに三つの箱へ分けているイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-90-40h180l-16 60H-74z" class="paper"/>
  <g class="coral o"><circle cx="-50" cy="0" r="13"/><circle cx="20" cy="6" r="13"/></g>
  <g class="teal o"><circle cx="-20" cy="-4" r="13"/><circle cx="54" cy="0" r="13"/></g>
  <g class="gold o"><circle cx="-66" cy="-18" r="13"/><circle cx="6" cy="-20" r="13"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 200q-60 40-80 80"/><path d="M300 200v80"/><path d="M350 200q60 40 80 80"/></g>
<g transform="translate(150 330)"><path d="M-50-20h100l-12 44H-38z" class="coralp o"/></g>
<g transform="translate(300 330)"><path d="M-50-20h100l-12 44H-38z" class="tealp o"/></g>
<g transform="translate(450 330)"><path d="M-50-20h100l-12 44H-38z" class="goldp o"/></g>
""", ground=False, arrow=True)

add('speed', '速度計の針が高い数値を指し、車が速く走るイラスト。', f"""
<g transform="translate(180 200)">
  <circle r="90" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0l60-50" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-64 64l-12 12M64 64l12 12M-90 0h-14M90 0h14M0-90v-14"/></g>
  <circle r="10" class="ink"/>
</g>
<g transform="translate(400 300) scale(0.7)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g class="muted"><path d="M250 280h60M250 320h80"/></g>
<path d="M520 250h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('stage', '低い段から高い段へ、順に進む三つの段階のイラスト。', f"""
<g class="tealp o">
  <rect x="90" y="270" width="120" height="70"/><rect x="240" y="210" width="120" height="130"/><rect x="390" y="150" width="120" height="190"/>
</g>
<path d="M150 250V190" class="a" marker-end="url(#ar)"/>
<path d="M300 190V130" class="a" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
{person(450,150,0.5,1,'coral','blue','up','short','smile')}
""", ground=False, arrow=True)

add('standard', 'そろえるべき基準の線と、それに合わせて並ぶ品物のイラスト。', f"""
<path d="M60 190h480" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<g class="tealp o">
  <rect x="110" y="190" width="70" height="150"/><rect x="210" y="190" width="70" height="150"/>
  <rect x="310" y="190" width="70" height="150"/><rect x="410" y="190" width="70" height="150"/>
</g>
<path d="M60 170h480" class="muted"/>
<path d="M60 340h480" class="a"/>
""", ground=False)

add('star', '夜空に光る星と、星の形を示したイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a4a"/>
<g fill="#f7e6a8"><circle cx="120" cy="100" r="4"/><circle cx="200" cy="160" r="3"/><circle cx="480" cy="120" r="4"/><circle cx="520" cy="260" r="3"/><circle cx="90" cy="300" r="3"/></g>
<g transform="translate(300 200)">
  <path d="M0-110l26 66 70 6-54 46 16 70-58-38-58 38 16-70-54-46 70-6z" class="gold o"/>
</g>
<g class="golds" style="stroke-width:4" opacity=".8"><path d="M300-0v0"/></g>
""", ground=False)

add('state', '水・氷・湯気の三つの状態を並べたイラスト。', f"""
<g transform="translate(140 260)">
  <path d="M-60-40h120l-10 100h-100z" fill="#f4fbff" class="o"/>
  <path d="M-52 0h104l-6 60h-92z" class="bluep o"/>
</g>
<g transform="translate(300 280)">
  <path d="M-50-24q6-12 18-12h64q12 0 18 12l-14 14H-36z" fill="#f6fbfe" class="o"/>
  <path d="M-36-10h72q10 22 0 44-20 16-44 16t-44-16q-10-22 0-44z" fill="#e8f4fb" class="o"/>
</g>
<g transform="translate(470 260)">
  <path d="M-60 60h120l-14-40h-92z" fill="#dfe6ea" class="o"/>
  <g class="muted"><path d="M-30 0q-16-40 6-70M20-6q-16-44 8-76"/></g>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('steady', 'ぶれずに一定の高さを保って進む線と、揺れる線を比べたイラスト。', f"""
<path d="M60 170h480" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round" marker-end="url(#ar)"/>
<path d="M60 300q60-60 120 0t120 0 120 0 120 0" fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M520 110l18 18 30-36"/></g>
""", ground=False, arrow=True)

add('step', '一歩ずつ足を前へ運ぶ足あとのイラスト。', f"""
<g fill="#c9bda6">
  <ellipse cx="140" cy="330" rx="14" ry="22"/><ellipse cx="220" cy="300" rx="14" ry="22"/>
  <ellipse cx="300" cy="270" rx="14" ry="22"/><ellipse cx="380" cy="240" rx="14" ry="22"/>
</g>
{person(470,240,0.9,1,'teal','blue','walk','short','neutral')}
<path d="M160 350h60" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a" opacity=".3"/>
""", ground=True, arrow=True)

add('stiff', '曲がらない硬い板と、しなる柔らかい板を比べたイラスト。', f"""
<path d="M100 180h200v26H100z" class="goldd o"/>
<g class="corals" style="stroke-width:6"><path d="M200 240q0 20 0 20"/></g>
<path d="M100 240q100 60 200 0" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8"/>
<path d="M340 300q100 60 200 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="24" stroke-linecap="round"/>
<path d="M340 240h200" class="muted"/>
""", ground=False)

add('strength', '太い腕で重い物を持ち上げ、力の強さを示すイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(280 250)">
  <path d="M-140-14h280v28h-280z" class="ink"/>
  <circle cx="-170" cy="0" r="40" class="ink"/><circle cx="170" cy="0" r="40" class="ink"/>
</g>
{person(280,346,1.3,1,'coral','blue','up','short','neutral')}
<g class="corals" style="stroke-width:5"><path d="M170 300l-24 20M390 300l24 20"/></g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('stretch', 'ゴムひもを両手で引っぱって、長く伸ばしているイラスト。', f"""
<path d="M180 240h240" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="10 8"/>
<path d="M120 300h360" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round"/>
{hand(90,300,1)}
{hand(510,300,-1)}
<g class="a" marker-end="url(#ar)"><path d="M200 180h-80"/><path d="M400 180h80"/></g>
""", ground=True, arrow=True)

add('striking', '落ち着いた色の中に、一つだけ鮮やかな色があるイラスト。', f"""
<g class="muted" fill="#dfe1e0">
  {''.join(f'<rect x="{80+ (i%5)*90}" y="{170 + (i//5)*100}" width="70" height="70"/>' for i in range(10))}
</g>
<rect x="260" y="270" width="70" height="70" class="coral o"/>
<g class="golds" style="stroke-width:4"><path d="M295 240v-24M240 280h-24M350 280h24"/></g>
""", ground=False)

add('substantial', '小さな一切れに対して、かなり大きな量を示したイラスト。', f"""
<g transform="translate(150 300)">
  <path d="M-30-20h60v40h-60z" class="goldp o"/>
</g>
<g transform="translate(400 250)">
  <path d="M-120-90h240v180h-240z" class="goldp o"/>
  <path d="M-120-90l40-30h240l-40 30z" class="gold o"/>
  <path d="M120-90l40-30v180l-40 30z" class="goldd o"/>
</g>
<path d="M200 300h60" class="a" marker-end="url(#ar)"/>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('surgical', '手術用のメスとはさみが、清潔な布の上に並んだイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-200-60h400v130h-400z" class="bluep o"/>
  <path d="M-200-60h400" class="a"/>
</g>
<g transform="translate(220 240) rotate(-8)">
  <path d="M-70-8h110l30 8-30 8H-70z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-130-10h60v20h-60z" class="bluep o"/>
</g>
<g transform="translate(400 260) rotate(10)">
  <path d="M-40 0l80-30M-40 0l80 30" fill="none" stroke="#dfe6ea" stroke-width="9"/>
  <circle cx="-52" cy="-16" r="16" fill="none" stroke="{INK}" stroke-width="5"/>
  <circle cx="-52" cy="16" r="16" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
""", ground=True)

add('surprise', '思いがけない出来事に、目を丸くして驚いている人のイラスト。', f"""
{person(240,346,1.25,1,'coral','blue','up','short','surprised')}
<g transform="translate(430 240)">
  <path d="M-60-50h120v100h-120z" class="goldp o"/>
  <path d="M-12-50h24v100h-24zM-60-8h120v16h-120z" class="coral o"/>
  <path d="M0-50l-24-24 24 8 24-8z" class="coral o"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M320 190l-24-24M330 240h-30M320 290l-24 24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('taste', 'スープを一口すくって、舌で味を確かめているイラスト。', f"""
<g transform="translate(200 300)">
  <path d="M-90-30h180q-14 90-90 90T-90-30z" fill="#fffdf6" class="o"/>
  <path d="M-90-30h180" class="a"/>
  <path d="M-76-10h152q-12 62-76 62t-76-62z" class="coralp o"/>
</g>
<g transform="translate(300 200) rotate(-30)">
  <ellipse rx="26" ry="14" fill="#f0dfc2" stroke="{INK}" stroke-width="2.5"/>
  <path d="M22 0h70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9" stroke-linecap="round"/>
</g>
<g transform="translate(450 200)">
  <circle r="70" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="-24" cy="-18" r="4" class="ink"/><circle cx="24" cy="-18" r="4" class="ink"/>
  <ellipse cy="30" rx="30" ry="20" fill="#b7574c" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="38" rx="18" ry="10" class="coralp"/>
</g>
""", ground=True)

add('tender', '柔らかい布で、小さな鳥をそっと包んでいるイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
{hand(180,260,1)}
<g transform="translate(320 250)">
  <path d="M-70 30q-20-70 70-70t70 70q-30 24-70 24t-70-24z" class="coralp o"/>
  <g transform="translate(0 -6) scale(0.7)">
    <path d="M0 0c-26-14-24-40 6-40 22 0 34 14 34 30 0 14-16 24-40 10z" class="gold o"/>
    <path d="M32-14l22-8-16 18z" class="gold o"/>
    <circle cx="22" cy="-18" r="3" class="ink"/>
  </g>
</g>
<path d="M250 250h30" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('term', '学年の途中を区切った、一区間を示したイラスト。', f"""
<path d="M60 200h480" class="a"/>
<g fill="{INK}"><circle cx="60" cy="200" r="8"/><circle cx="220" cy="200" r="8"/><circle cx="380" cy="200" r="8"/><circle cx="540" cy="200" r="8"/></g>
<path d="M220 250h160" class="tealp o" transform="translate(0 0)"/>
<rect x="220" y="230" width="160" height="40" class="tealp o"/>
<path d="M220 300h160" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('text', '画面に短い文章のメッセージが表示されているイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-100-140h200q16 0 16 16v248q0 16-16 16h-200q-16 0-16-16v-248q0-16 16-16z" fill="#dfe6ea" class="o"/>
  <path d="M-80-110h160v190h-160z" fill="#fffdf6" class="o"/>
  <g transform="translate(-30 -70)">
    <path d="M-40-20h100q10 0 10 10v24q0 10-10 10h-70l-16 14 4-14q-10 0-10-10v-24q0-10 10-10z" class="bluep o"/>
  </g>
  <g transform="translate(34 20)">
    <path d="M40-20H-60q-10 0-10 10v24q0 10 10 10h70l16 14-4-14q10 0 10-10v-24q0-10-10-10z" class="tealp o"/>
  </g>
</g>
""", ground=True)

add('tip', '飲食の代金に少し足して、感謝の心づけを置くイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160-20h320v20h-320z" class="goldp o"/>
</g>
<g transform="translate(230 250)">
  <path d="M-60-40h120v70h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-20h80M-40 0h60"/></g>
</g>
<g transform="translate(400 260)">
  <circle r="22" class="goldp o"/><circle cx="-24" cy="10" r="22" class="goldp o"/>
</g>
{hand(430,180,-1)}
<path d="M420 220v20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('tour', 'いくつかの名所を順に回って見学するイラスト。', f"""
{building(120,240,0.55,'teal')}
{building(300,200,0.55,'gold')}
{building(480,250,0.55,'violet')}
<path d="M120 300q80 60 180 0t180 20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8" stroke-dasharray="16 12" marker-end="url(#ar)"/>
{person(200,346,0.8,1,'coral','blue','walk','cap','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('transport', 'トラックが荷物を積んで、別の場所へ運んでいくイラスト。', f"""
{building(90,300,0.6,'teal')}
{building(520,300,0.6,'gold')}
<g transform="translate(300 300) scale(0.6)">
  <path d="M-200 40h130v-120h-130z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-70 40h270v-90H-70z" class="coral o"/>
  <circle cx="-150" cy="52" r="30" class="ink"/><circle cx="110" cy="52" r="30" class="ink"/>
  <g class="goldp o"><rect x="-40" y="-90" width="70" height="40"/><rect x="40" y="-90" width="70" height="40"/></g>
</g>
<path d="M180 210h240" class="a" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('trouble', '前に立ちふさがった壁と、困っている人のイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','up','short','sad')}
<g transform="translate(400 260)">
  <path d="M-70-120h140v240h-140z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><path d="M-70-60h140M-70 0h140M-70 60h140"/></g>
</g>
<path d="M260 240h60" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:8"><path d="M300 180l40 40M340 180l-40 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('verbal', '言葉だけで伝えている場面と、書いた文書を比べたイラスト。', f"""
{person(170,346,1.1,1,'teal','blue','stand','short','neutral')}
<g transform="translate(320 200)">
  <path d="M-70-40h140q16 0 16 16v44q0 16-16 16h-90l-26 22 6-22h-30q-16 0-16-16v-44q0-16 16-16z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-30" cy="0" r="5"/><circle cx="0" cy="0" r="5"/><circle cx="30" cy="0" r="5"/></g>
</g>
<g transform="translate(500 300)" opacity=".5">
  <path d="M-56-70h112v140h-112z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-36-40h72M-36-14h72M-36 12h50"/></g>
</g>
<g class="corals" style="stroke-width:6"><path d="M470 200l30 30M500 200l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('view', '窓の外に広がる景色を、部屋の中から見ているイラスト。', f"""
<g transform="translate(340 200)">
  <path d="M-160-140h320v280h-320z" fill="#dbeaf8" stroke="{INK}" stroke-width="4"/>
  <path d="M-160 60L-40-60l90 90 60-50 110 80z" class="tealp o"/>
  {sun(90,-90,26)}
  <path d="M0-140v280M-160 0h320" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
{person(130,346,1.0,1,'coral','blue','stand','bob','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M180 200h70" marker-end="url(#ar)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('track', '地面に残った跡をたどって、対象を追っていくイラスト。', f"""
<g fill="#c9bda6">
  <ellipse cx="120" cy="330" rx="12" ry="18"/><ellipse cx="180" cy="306" rx="12" ry="18"/>
  <ellipse cx="240" cy="284" rx="11" ry="17"/><ellipse cx="300" cy="262" rx="11" ry="17"/>
</g>
{person(150,290,0.85,1,'teal','blue','point','cap','neutral')}
<g opacity=".5">{person(470,270,0.8,1,'coral','gold','walk','short','neutral')}</g>
<path d="M330 250q60-20 100-10" class="muted" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
