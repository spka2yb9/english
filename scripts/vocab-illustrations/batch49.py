"""第49回: 滑る・砕く・浸す・安定など39語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('single', '並んだ場所に、たった一つだけあるイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8">
  <rect x="90" y="200" width="90" height="110"/><rect x="310" y="200" width="90" height="110"/><rect x="420" y="200" width="90" height="110"/>
</g>
<rect x="200" y="200" width="90" height="110" class="teal o"/>
<path d="M245 140v40" class="a" marker-end="url(#ar)"/>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('sir', '相手をうやうやしく呼びかけるイラスト。', f"""
<g transform="translate(200 346) rotate(16)">{person(0,0,1.15,1,'teal','blue','give','short','smile')}</g>
{person(450,346,1.3,-1,'blue','blue','stand','short','neutral')}
<g transform="translate(450 196)"><path d="M-40-10h80v10h-80z" class="bluep o"/></g>
<g transform="translate(330 180)">
  <path d="M-50-40h100v66h-100z" fill="#fffdf6" class="o"/>
  <path d="M-30 26l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-30" y="-14" width="60" height="12"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('ski', '板をはいて雪の斜面を滑るイラスト。', f"""
<path d="M0 400V300q160-40 260-120T600 60v340z" fill="#eef5fb"/>
<g transform="translate(300 250) rotate(-20)">
  {person(0,0,1.05,1,'coral','blue','reach','cap','smile')}
  <path d="M-70 14h150v10h-150z" class="teal o"/>
</g>
<g class="muted"><path d="M420 150q-40 40-90 60"/></g>
""", ground=False)

add('skiing', '斜面をスキーで下る、雪の遊びのイラスト。', f"""
<path d="M0 400V320q170-50 280-140T600 40v360z" fill="#eef5fb"/>
{tree(90,300,0.8)}
{tree(520,180,0.8)}
<g transform="translate(320 230) rotate(-24)">
  {person(0,0,1.0,1,'violet','blue','walk','cap','smile')}
  <path d="M-80 14h160v10h-160z" class="coral o"/>
  <path d="M-30-40l-60-30" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g class="muted"><path d="M430 130q-50 50-100 70"/></g>
""", ground=False)

add('skin', '腕の表面をおおう肌を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-160-50h320v100h-320z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-160-50h320v-24h-320z" fill="{SKINL}" opacity=".5"/>
</g>
<g transform="translate(430 130)">
  <circle r="46" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M32 32l40 40" fill="none" stroke="{INK}" stroke-width="10"/>
  <g fill="{SKINL}" opacity=".7"><circle cx="-16" cy="-10" r="5"/><circle cx="8" cy="8" r="5"/><circle cx="18" cy="-16" r="5"/></g>
</g>
<path d="M200 330h-40" class="a" marker-end="url(#ar)" transform="rotate(180 180 330)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('slam', '戸を勢いよくたたきつけて閉めるイラスト。', f"""
<g transform="translate(360 230)">
  <path d="M-20-140h140v280h-140z" fill="#e4d9c4" stroke="{INK}" stroke-width="3"/>
  <circle cx="-2" cy="10" r="10" class="ink"/>
</g>
<path d="M240 160q60-30 100 0" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:6"><path d="M180 200l-40-24M170 250h-44M180 300l-40 24"/></g>
{person(140,346,1.0,1,'coral','blue','point','short','flat')}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('slash', '棒グラフを大きく切り下げるイラスト。', f"""
<path d="M60 340h480" class="a"/>
<g class="tealp o" opacity=".4"><rect x="140" y="120" width="100" height="220"/><rect x="360" y="150" width="100" height="190"/></g>
<g class="coral o"><rect x="140" y="260" width="100" height="80"/><rect x="360" y="280" width="100" height="60"/></g>
<path d="M100 160L520 300" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
<path d="M300 130v100" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('sleep', 'ふとんで目を閉じて眠るイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-200-20h400v60h-400z" fill="#fffdf6" class="o"/>
  <path d="M-200 40h20v40h-20zM180 40h20v40h-20z" fill="#c9d3dc" class="o"/>
  <path d="M-60-20h260v-30h-260z" class="tealp o"/>
  <path d="M-200-20h100v-40h-100z" fill="#e8f4fb" class="o"/>
  <circle cx="-130" cy="-46" r="28" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <g fill="none" stroke="{INK}" stroke-width="2.5"><path d="M-142-50q6 6 12 0M-124-50q6 6 12 0"/></g>
</g>
<g fill="{MUTED}" transform="translate(360 170)">
  <path d="M0-30h34l-34 30h34" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M50-64h26l-26 24h26" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('slide', 'すべり台をすべり降りるイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-160 90L60-90h50L-100 90z" class="teal o"/>
  <path d="M60-90h20v180h-20z" fill="#c9d3dc" class="o"/>
  <path d="M60-90h60v14H60z" class="goldd o"/>
</g>
<g transform="translate(240 250) rotate(38)">{person(0,0,0.85,1,'coral','gold','up','bob','smile')}</g>
<path d="M400 160L180 340" class="a" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('smartphone', '画面に触れて操作するスマートフォンのイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-80-150h160v300h-160z" fill="#2f4055"/>
  <path d="M-66-132h132v264h-132z" fill="#e8f4fb"/>
  <g class="teal o"><rect x="-46" y="-110" width="36" height="36"/><rect x="10" y="-110" width="36" height="36"/><rect x="-46" y="-58" width="36" height="36"/><rect x="10" y="-58" width="36" height="36"/></g>
  <g fill="{MUTED}"><rect x="-40" y="10" width="80" height="10"/><rect x="-40" y="34" width="60" height="10"/></g>
</g>
{hand(400,300,-1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('smash', 'ハンマーで皿をたたき割るイラスト。', f"""
<g transform="translate(300 300)">
  <g fill="#e7f6fb" stroke="{INK}" stroke-width="3">
    <path d="M-140 20l40-60 30 40z"/><path d="M-40 20l50-40 20 40z"/><path d="M60 20l40-50 40 50z"/>
  </g>
</g>
<g transform="translate(300 160) rotate(-20)">
  <path d="M-70-30h140v50h-140z" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 20h20v130h-20z" class="goldd o"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M150 250l-30 20M450 250l30 20M300 250v30"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('smoking', 'たばこから煙が立ちのぼるイラスト。', f"""
<g transform="translate(280 300) rotate(-16)">
  <path d="M-120-16h200v32h-200z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M80-16h40v32H80z" class="goldd o"/>
  <path d="M-120-16h-24v32h24z" class="coral o"/>
</g>
<g class="muted" opacity=".9"><path d="M150 250q30-40 0-70t0-70M190 240q30-40 0-70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('smooth', 'でこぼこのない、なめらかな面を示したイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-90 60q10-40 30-20t20-40 30 10 30-30 30 20 30-10v70z" class="coralp o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-90 60V-20h180v80z" class="tealp o"/>
  <path d="M-90-20h180" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
</g>
{hand(430,150,1)}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M300 340l20 20 34-40"/></g>
""", ground=True)

add('snap', '棒がぽきりと二つに折れるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-16h150l20 16-20 16h-150z" class="goldd o" transform="rotate(-6)"/>
  <path d="M200-16H50l-20 16 20 16h150z" class="goldd o" transform="rotate(6)"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M300 130v-34M250 150l-24-26M350 150l24-26"/></g>
{hand(160,330,1)}{hand(440,330,-1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('soak', '布を水にひたしてびしょぬれにするイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-140-60h280l-20 140h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-130-20h260l-16 100h-228z" class="bluep o"/>
  <path d="M-60-10q60-30 120 0 10 40-60 50t-60-50z" class="teal o"/>
</g>
{drop(200,150,0.9)}{drop(400,140,0.9)}
<path d="M300 120v40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('soccer', 'ボールをけって、ゴールをねらうイラスト。', f"""
<g transform="translate(460 250)">
  <path d="M-90-90h180v180h-180z" fill="none" stroke="{INK}" stroke-width="6"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-90+i*22}-90v180"/>' for i in range(9))}{''.join(f'<path d="M-90 {-90+i*22}h180"/>' for i in range(9))}</g>
</g>
<g transform="translate(300 300)">
  <circle r="34" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0-20l18 14-8 22h-20l-8-22z" class="ink"/>
</g>
{person(150,346,1.1,1,'coral','blue','walk','short','neutral')}
<path d="M240 240h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('social', '人と人がつながって集まるイラスト。', f"""
{person(150,346,1.0,1,'teal','blue','give','short','smile')}
{person(300,346,1.0,1,'coral','gold','give','bob','smile')}
{person(450,346,1.0,-1,'gold','blue','give','cap','smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M150 200q75-60 150 0t150 0"/></g>
<path d="M210 250h30M360 250h30" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('soldier', '制服とヘルメットの兵士のイラスト。', f"""
{person(300,346,1.5,1,'green','green','stand','cap','neutral')}
<g transform="translate(300 246)"><path d="M-24-10h48v10h-48z" class="green o"/></g>
<g transform="translate(230 250) rotate(-16)"><path d="M-8-90h16v170h-16z" class="ink"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('somewhere', '地図のどこかに、はっきりしない印があるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-200 40q110-40 200 0t200-20" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"><circle cx="60" cy="-20" r="80"/></g>
</g>
<g fill="{INK}" transform="translate(340 190)">
  <path d="M0 0q0-30 22-30t22 30q0 16-18 20v16h-10v-24q16-4 16-16t-10-12-12 16z"/>
  <rect x="12" y="48" width="12" height="12"/>
</g>
""", ground=True)

add('southern', '地図の南側の地域を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <path d="M-180 30h360v110h-360z" class="coralp o"/>
  <path d="M-180 30h360" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="10 8"/>
</g>
<g transform="translate(500 110)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M0 26l12-26-12-26-12 26z" class="coral o"/>
</g>
<path d="M120 300v40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('span', '両端にわたって、はしがかかるイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-260 40h80v90h-80zM180 40h80v90h-80z" fill="#c9d3dc" class="o"/>
  <path d="M-190 20h380v30h-380z" class="teal o"/>
  <path d="M-180 20q180-100 360 0" fill="none" stroke="{TONES['teal'][2]}" stroke-width="8"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M110 180h380M490 180H110"/></g>
""", ground=False, arrow=True)

add('speaker', '声を届ける話し手とスピーカーのイラスト。', f"""
{person(170,346,1.2,1,'teal','blue','point','short','neutral')}
<g transform="translate(420 240)">
  <path d="M-70-110h140v220h-140z" fill="#41506a"/>
  <circle cy="-40" r="40" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
  <circle cy="50" r="24" fill="#7f8ea6" stroke="{INK}" stroke-width="3"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M250 200q26 20 26 44"/></g>
<path d="M280 260h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('specifically', '全体の中から、とくに一点を指し示すイラスト。', f"""
<g class="tealp o">{''.join(f'<circle cx="{120+c*80}" cy="{170+r*80}" r="26"/>' for r in range(3) for c in range(6))}</g>
<g transform="translate(280 250)"><circle r="34" class="coral o"/></g>
<circle cx="280" cy="250" r="56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M280 100v70" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('specify', '寸法をはっきり書き入れて指定するイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-140-90h280v180h-280z" class="tealp o"/>
  <g class="a" marker-end="url(#ar)"><path d="M-140 130h280M140 130h-280"/></g>
  <g class="a" marker-end="url(#ar)"><path d="M190-90v180M190 90V-90"/></g>
  <g fill="{INK}"><rect x="-30" y="112" width="60" height="12"/><rect x="210" y="-10" width="50" height="12"/></g>
</g>
""", ground=False, arrow=True)

add('speculate', '手がかりが少ないまま、あれこれ推し量るイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','neutral')}
<g transform="translate(430 190)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g opacity=".5"><circle cx="-50" r="26" class="tealp o"/><path d="M20-26h60v52H20z" class="coralp o"/></g>
  <g fill="{INK}"><path d="M104 6q0-26 20-26t20 26q0 14-16 18v14h-10v-20q14-4 14-14t-8-10-10 12z"/><rect x="112" y="50" width="10" height="10"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="280" cy="290" r="12"/><circle cx="256" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('spicy', '口から火が出るほど辛いイラスト。', f"""
{face(230,200,90,'flat')}
<g transform="translate(230 250)"><ellipse rx="26" ry="20" fill="#8b4a3e"/></g>
{flame(320,240,1.2)}
<g transform="translate(470 300)">
  <path d="M-16 40q-30-40 0-80 24-30 40-10 14 20-10 50z" class="coral o"/>
  <path d="M24-50q10-20 26-14" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('spider', '八本の脚をもつクモのイラスト。', f"""
<g transform="translate(300 240)">
  <g fill="none" stroke="{INK}" stroke-width="6">
    <path d="M-40-10l-80-50M-40 0l-90 10M-40 14l-80 60M-30 24l-50 70M40-10l80-50M40 0l90 10M40 14l80 60M30 24l50 70"/>
  </g>
  <ellipse rx="56" ry="46" class="ink"/>
  <circle cy="-50" r="26" class="ink"/>
  <g fill="#fffdf6"><circle cx="-10" cy="-56" r="6"/><circle cx="10" cy="-56" r="6"/></g>
</g>
<g class="muted"><path d="M300 90V40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('spin', 'こまが軸を中心に勢いよく回るイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-70-40h140l-70 90z" class="coral o"/>
  <path d="M-70-40h140v-24h-140z" class="coralp o"/>
  <path d="M-6-100h12v36h-12z" class="ink"/>
  <path d="M-6 50h12v40h-12z" class="ink"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M140 180a180 100 0 0 1 90-50M460 180a180 100 0 0 0-90-50"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('spoil', 'せっかくの絵に墨をこぼして、だいなしにするイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-100h200v200h-200z" fill="#fffdf6" class="o"/>
  <path d="M-70 60l60-80 40 40 44-60 36 100z" class="green o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-100-100h200v200h-200z" fill="#fffdf6" class="o"/>
  <path d="M-70 60l60-80 40 40 44-60 36 100z" class="green o"/>
  <path d="M-40-60q60-30 90 20t-30 90-90-20 30-90z" fill="#41506a" opacity=".85"/>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('sponsor', '資金を出して催しを後押しするイラスト。', f"""
{person(140,346,1.05,1,'blue','blue','give','short','smile')}
<g transform="translate(290 250)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="16" class="goldd o"/>
</g>
<g transform="translate(470 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <path d="M-60-60h120v60h-120z" class="coralp o"/>
  <g fill="{INK}"><rect x="-60" y="20" width="120" height="16"/></g>
</g>
<path d="M200 200h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('spoon', 'すくうためのスプーンのイラスト。', f"""
<g transform="translate(300 220) rotate(20)">
  <ellipse cy="-90" rx="52" ry="66" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="-90" rx="34" ry="46" fill="#c2ccd6"/>
  <path d="M-12-24h24v190h-24z" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('square', '四辺の長さが等しい正方形のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-110-110h220v220h-220z" class="tealp o"/>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-110-80h30v-30M110-80h-30v-30M-110 80h30v30M110 80h-30v30"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M190 350h220M410 350H190"/></g>
""", ground=False, arrow=True)

add('squeeze', 'レモンをぎゅっと絞るイラスト。', f"""
{hand(230,160,1)}{hand(370,160,-1)}
<g transform="translate(300 250)">
  <ellipse rx="80" ry="60" class="gold o"/>
  <path d="M-80 0q80-40 160 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M170 250h40M430 250h-40"/></g>
{drop(300,340,0.9,'gold')}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('stabilize', 'ぐらついていた台が、支えで安定するイラスト。', f"""
<g transform="translate(170 250)">
  <g transform="rotate(-12)"><path d="M-70-20h140v40h-140z" class="coralp o"/><path d="M-10 20h20v70h-20z" class="coralp o"/></g>
  <g class="corals" style="stroke-width:4"><path d="M90-30q20 20 0 40"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-70-20h140v40h-140z" class="tealp o"/>
  <path d="M-10 20h20v70h-20z" class="tealp o"/>
  <path d="M-70 90h140v14h-140z" class="teal o"/>
</g>
<path d="M280 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('stair', '一段ずつ上がっていく階段のイラスト。', f"""
<g class="goldd o">
  {''.join(f'<rect x="{110+i*70}" y="{320-i*50}" width="70" height="{50+i*50}"/>' for i in range(5))}
</g>
<path d="M120 240l260-190" class="a" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('start', '合図とともに走り出すイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-6-120h12v240h-12z" class="ink"/>
  <path d="M6-116h100v60H6z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="20" y="-100" width="20" height="20"/><rect x="60" y="-100" width="20" height="20"/><rect x="40" y="-80" width="20" height="20"/><rect x="80" y="-80" width="20" height="20"/></g>
</g>
{person(320,346,1.2,1,'coral','blue','walk','short','neutral')}
<path d="M400 230h140" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('starve', '食べ物がなく、腹をすかせているイラスト。', f"""
{person(220,346,1.25,1,'teal','blue','stand','short','sad')}
<g transform="translate(430 280)">
  <ellipse rx="110" ry="30" fill="#fffdf6" class="o"/>
  <ellipse cy="-10" rx="80" ry="22" fill="#f2f6f9" class="o"/>
</g>
<g class="muted"><path d="M300 220q40-20 70 0"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><circle cx="262" cy="300" r="36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('stay', '同じ場所に、そのままとどまるイラスト。', f"""
{person(220,346,1.2,1,'teal','blue','stand','short','smile')}
<circle cx="220" cy="330" r="90" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 10"/>
<g class="muted" marker-end="url(#ar)"><path d="M370 250h100"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M420 210l40 40M460 210l-40 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('steadily', '同じ歩幅で、着実に階段を上がるイラスト。', f"""
<g class="goldd o">{''.join(f'<rect x="{100+i*80}" y="{320-i*50}" width="80" height="{50+i*50}"/>' for i in range(5))}</g>
<g opacity=".35">{person(150,320,0.7,1,'teal','blue','walk','short','neutral')}</g>
<g opacity=".6">{person(310,220,0.7,1,'teal','blue','walk','short','neutral')}</g>
{person(470,120,0.7,1,'teal','blue','walk','short','neutral')}
<path d="M120 250l340-160" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="14 10" marker-end="url(#ar)"/>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('steer', 'ハンドルを切って進む向きを決めるイラスト。', f"""
<g transform="translate(200 250)">
  <circle r="80" fill="none" stroke="{INK}" stroke-width="16"/>
  <circle r="20" class="ink"/>
  <path d="M-64 0h128M0 20v60" fill="none" stroke="{INK}" stroke-width="12"/>
</g>
<path d="M300 300q120-20 200-140" class="a" marker-end="url(#ar)"/>
<path d="M300 320q120 20 200 40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
