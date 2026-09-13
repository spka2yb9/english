"""第75回: 容量・洞窟・混乱・衝突など45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('capable', '重い荷を持ち上げられる力があるイラスト。', f"""
{person(260,346,1.3,1,'blue','blue','up','short','smile')}
{box(260,140,170,80,0,'gold')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M450 200l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('capacity', '入れ物にどれだけ入るかを示したイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-110-120h220v240h-220z" fill="#f7fbfe" stroke="{INK}" stroke-width="4"/>
  <path d="M-110 0h220v120h-220z" class="bluep o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M60 {-100+i*40}h50"/>' for i in range(6))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M480 370V130"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('carbon', '炭のかたまりと、燃えて出る炭素のイラスト。', f"""
<g transform="translate(200 290)">
  <path d="M-80 40l20-70 60-30 70 20 20 60-30 20z" fill="#41506a" stroke="{INK}" stroke-width="3"/>
</g>
<g class="muted" opacity=".9"><path d="M330 240q30-40 0-70M380 220q30-40 0-70"/></g>
<g transform="translate(470 220)">
  <circle r="34" class="ink"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><circle r="60"/></g>
  <g fill="{INK}"><circle cx="60" r="8"/><circle cx="-60" r="8"/><circle cy="60" r="8"/><circle cy="-60" r="8"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('cargo', '船に積まれた貨物のイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(300 270)">
  <path d="M-200 30h400l-40 40h-320z" class="tealp o"/>
  <g class="goldd o"><rect x="-160" y="-30" width="90" height="60"/><rect x="-60" y="-30" width="90" height="60"/><rect x="40" y="-30" width="90" height="60"/></g>
  <g class="coralp o"><rect x="-110" y="-90" width="90" height="60"/><rect x="-10" y="-90" width="90" height="60"/></g>
</g>
""", ground=False)

add('casino', 'カードとチップが並ぶカジノのイラスト。', f"""
<g transform="translate(240 260)">
  <path d="M-120-30h200v60h-200z" class="green o"/>
  <g transform="translate(-60 -60) rotate(-12)"><path d="M-40-50h80v100h-80z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/><path d="M0-20l16 16-16 16-16-16z" class="coral o"/></g>
  <g transform="translate(30 -60) rotate(10)"><path d="M-40-50h80v100h-80z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/><path d="M0 10c-16-14-24-20-24-30a12 12 0 0 1 24-6 12 12 0 0 1 24 6c0 10-8 16-24 30z" class="ink"/></g>
</g>
<g transform="translate(450 300)">
  <g class="coral o"><ellipse rx="46" ry="14"/><ellipse cy="-16" rx="46" ry="14"/></g>
  <g class="teal o"><ellipse cy="-32" rx="46" ry="14"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('casualty', '事故で傷ついた人が運ばれるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160-20h320v30h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160 10h20v50h-20zM140 10h20v50h-20z" fill="#c9d3dc"/>
  <path d="M-120-40h240v20h-240z" class="tealp o"/>
  <circle cx="-140" cy="-40" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g transform="translate(300 180)"><path d="M-10-16h20v12h12v20h-12v12h-20v-12h-12v-20h12z" class="coral o"/></g>
{person(500,346,0.9,-1,'blue','blue','reach','bob','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('cattle', '牧場の牛の群れのイラスト。', f"""
<g class="green o" opacity=".85"><path d="M0 320q150-40 300-20t300-20v120H0z"/></g>
<g transform="translate(200 280)">
  <ellipse rx="80" ry="46" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="#8b6f4e"><ellipse cx="-20" cy="-10" rx="24" ry="16"/><ellipse cx="30" cy="14" rx="18" ry="12"/></g>
  <circle cx="76" cy="-30" r="30" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M60-56q-14-20 4-22 14 0 14 18z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="3"><rect x="-50" y="40" width="18" height="40"/><rect x="30" y="40" width="18" height="40"/></g>
</g>
<g transform="translate(430 300) scale(0.7)">
  <ellipse rx="80" ry="46" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cx="76" cy="-30" r="30" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="#8b6f4e"><ellipse cx="0" cy="0" rx="24" ry="16"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('caution', '足もとに気をつけよという注意のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M0-120l140 240h-280z" fill="#f3e3ae" stroke="{INK}" stroke-width="5"/>
  <g fill="{INK}"><rect x="-14" y="-44" width="28" height="90"/><rect x="-14" y="62" width="28" height="28"/></g>
</g>
{person(120,346,0.85,1,'teal','blue','walk','short','neutral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('cave', '岩山にあいた洞窟のイラスト。', f"""
<g fill="#8b98a6" stroke="{INK}" stroke-width="3"><path d="M60 340V180q120-90 240-60t240 20v200z"/></g>
<g fill="#2f4055"><path d="M300 340q-80 0-80-90t80-70 80 70-80 90z"/></g>
<g fill="#6d7c8c"><path d="M240 250l20-30 20 30zM340 260l20-24 18 24z"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('cemetery', '墓標が並ぶ墓地のイラスト。', f"""
<g class="green o" opacity=".8"><path d="M0 300h600v100H0z"/></g>
<g fill="#c9d3dc" stroke="{INK}" stroke-width="3">
  <path d="M120 300v-70a30 30 0 0 1 60 0v70z"/><path d="M240 300v-90a30 30 0 0 1 60 0v90z"/><path d="M360 300v-70a30 30 0 0 1 60 0v70z"/><path d="M470 300v-60a26 26 0 0 1 52 0v60z"/>
</g>
{tree(60,300,0.6)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('certainty', '確かだと言い切れる状態のイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','stand','short','smile')}
<g transform="translate(420 210)">
  <path d="M-90-60h180v90h-180z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="11" stroke-linecap="round"><path d="M-34-18l22 22 44-46"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('certificate', '印のついた証明書のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-130h360v260h-360z" class="paper"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><rect x="-160" y="-110" width="320" height="220"/></g>
  <g fill="{INK}"><rect x="-100" y="-70" width="200" height="20"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-20h200M-100 10h160"/></g>
  <g transform="translate(90 60)"><circle r="30" class="gold o"/><path d="M-14 30h28v30l-14-14-14 14z" class="coralp o"/></g>
</g>
""", ground=True)

add('chamber', '議席が並ぶ議場のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220-140h440v280h-440z" fill="#f4ead2" class="o"/>
  <g class="goldd o">{''.join(f'<rect x="{-180+c*90}" y="{-40+r*70}" width="70" height="20"/>' for r in range(3) for c in range(4))}</g>
  <path d="M-60-120h120v50h-120z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('championship', '優勝旗をかけて争う選手権のイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-6-70h12v90h-12z" class="ink"/>
  <path d="M6-66h90v50H6z" class="coralp o"/>
</g>
{person(180,346,1.15,1,'teal','blue','up','cap','neutral')}
{person(420,346,1.15,-1,'coral','gold','up','bob','neutral')}
<g transform="translate(300 280)">
  <path d="M-50-60h100l-12 60a44 30 0 0 1-76 0z" class="gold o"/>
  <path d="M-20 20h40v30h-40z" class="goldd o"/>
  <path d="M-46 50h92v18h-92z" class="goldd o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('chaos', '物と線が入り乱れた大混乱のイラスト。', f"""
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5">
  <path d="M80 120q120 120 60 200t180-60 100 120"/>
  <path d="M120 320q100-160 220-60t180-140"/>
</g>
<g class="tealp o" transform="rotate(24 200 200)"><rect x="160" y="170" width="70" height="50"/></g>
<g class="goldp o" transform="rotate(-30 380 260)"><rect x="350" y="240" width="70" height="50"/></g>
<g class="violetp o" transform="rotate(50 300 130)"><rect x="270" y="110" width="60" height="44"/></g>
""", ground=False)

add('charm', '人を引きつける魅力のイラスト。', f"""
{person(250,346,1.3,1,'coral','gold','stand','bob','smile')}
<g class="golds" style="stroke-width:6"><path d="M360 190l26-20M370 230h30M360 270l26 20"/></g>
<g transform="translate(460 220)">
  <path d="M0 40c-40-30-56-46-56-68a30 30 0 0 1 56-16 30 30 0 0 1 56 16c0 22-16 38-56 68z" class="coralp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('charter', '基本の約束を記した憲章のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="{INK}"><rect x="-130" y="-110" width="180" height="20"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-130 {-60+i*34}h260"/>' for i in range(5))}</g>
  <g transform="translate(100 90)"><circle r="26" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/></g>
</g>
""", ground=True)

add('cheap', '同じ品に安い値がつくイラスト。', f"""
<g transform="translate(200 260)">{box(200,260,140,110,28,'teal')}</g>
<g transform="translate(430 210) rotate(-10)">
  <path d="M-90-50h140l30 50-30 50h-140z" class="coral o"/>
  <circle cx="50" r="10" fill="#fffdf6"/>
  <g fill="#fffdf6"><rect x="-70" y="-14" width="60" height="26"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M430 340v-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('cheek', '顔のほおの位置を示したイラスト。', f"""
{face(280,210,110,'smile')}
<g class="coralp"><circle cx="196" cy="240" r="26"/><circle cx="364" cy="240" r="26"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="196" cy="240" r="44"/></g>
<path d="M110 300l50-40" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('chief', '組織の先頭に立つ長のイラスト。', f"""
{person(300,346,1.4,1,'blue','blue','stand','cap','neutral')}
<g transform="translate(300 226)"><path d="M-16-16l6 14 16 2-12 11 3 16-13-8-13 8 3-16-12-11 16-2z" class="gold o"/></g>
{person(160,346,0.9,1,'teal','gold','stand','short','neutral')}
{person(450,346,0.9,1,'coral','blue','stand','bob','neutral')}
<path d="M300 140v-30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('choir', '声をそろえて歌う合唱団のイラスト。', f"""
{person(150,346,1.05,1,'violet','blue','stand','bob','smile')}
{person(260,346,1.05,1,'violet','blue','stand','short','smile')}
{person(370,346,1.05,1,'violet','blue','stand','cap','smile')}
{person(480,346,1.05,1,'violet','blue','stand','bob','smile')}
<g fill="{INK}"><ellipse cx="300" cy="140" rx="16" ry="11" transform="rotate(-18 300 140)"/><rect x="311" y="96" width="6" height="40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('chunk', '大きなかたまりを切り分けたイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-90-70h180v140h-180z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(430 250)">
  <path d="M-40-60h80v120h-80z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <g class="mutedfill" fill="#d9b476" stroke="{INK}" stroke-width="2"><rect x="50" y="-40" width="50" height="40"/><rect x="50" y="10" width="50" height="40"/></g>
</g>
<path d="M310 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('circuit', '一周してもとに戻る回路のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-110h360v220h-360z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"/>
  <g fill="{TONES['teal'][0]}"><circle cx="-180" cy="-110" r="14"/><circle cx="180" cy="-110" r="14"/><circle cx="180" cy="110" r="14"/><circle cx="-180" cy="110" r="14"/></g>
  <g class="coral o"><rect x="-30" y="-124" width="60" height="28"/></g>
</g>
<path d="M420 120a180 110 0 0 1 30 60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('circulation', 'ぐるぐるとめぐって戻るイラスト。', f"""
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="14" stroke-dasharray="26 18"><circle cx="300" cy="210" r="140"/></g>
<g transform="translate(300 70)">{drop(300,70,0.9)}</g>
<path d="M430 110a140 140 0 0 1 40 80" class="a" marker-end="url(#ar)"/>
<path d="M180 310a140 140 0 0 1-40-80" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('civilian', '軍でない、ふつうの市民のイラスト。', f"""
{person(190,346,1.25,1,'teal','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M110 180l20 20 34-40"/></g>
{person(430,346,1.25,1,'green','green','stand','cap','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M500 170l30 30M530 170l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('civilization', '都市と文字で文明を示したイラスト。', f"""
{building(150,300,0.8,'teal')}
{building(300,300,0.7,'blue')}
<g transform="translate(450 260)">
  <path d="M-70-60h140v120h-140z" class="paper"/>
  <g fill="{INK}"><rect x="-46" y="-30" width="92" height="12"/><rect x="-46" y="-6" width="70" height="12"/><rect x="-46" y="18" width="80" height="12"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('clarity', 'ぼやけた文字がはっきり読めるイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-70h180v140h-180z" fill="#fffdf6" class="o"/>
  <g fill="#cfd8e0"><rect x="-60" y="-30" width="120" height="18"/><rect x="-60" y="4" width="90" height="18"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-90-70h180v140h-180z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-60" y="-30" width="120" height="18"/><rect x="-60" y="4" width="90" height="18"/></g>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 340l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('clash', '二つがぶつかり合うイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M0-60l24 46 52 6-38 36 10 52-48-26-48 26 10-52-38-36 52-6z" class="coralp o"/>
</g>
<g class="teal o" transform="translate(140 230)"><rect x="-60" y="-40" width="120" height="80"/></g>
<g class="gold o" transform="translate(460 230)"><rect x="-60" y="-40" width="120" height="80"/></g>
<g fill="none" stroke="{INK}" stroke-width="6" marker-end="url(#ar)"><path d="M210 230h30M390 230h-30"/></g>
""", ground=False, arrow=True)

add('classic', '長く手本とされてきた作品のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-130h280v260h-280z" class="violet o"/>
  <path d="M-120-110h240v220h-240z" fill="#f7f3e8" class="o"/>
  <g fill="{TONES['gold'][2]}"><rect x="-70" y="-70" width="140" height="16"/></g>
  <g transform="translate(0 20)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('classification', '種類ごとに分けて並べるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-80-80h160v160h-160z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o"><circle cx="-40" cy="-40" r="18"/></g>
  <g class="coralp o"><rect x="10" y="-56" width="34" height="34"/></g>
  <g class="goldp o"><path d="M-30 50l24-40 24 40z"/></g>
</g>
<g transform="translate(430 240)">
  <g fill="none" stroke="{INK}" stroke-width="3"><rect x="-90" y="-80" width="60" height="160"/><rect x="-20" y="-80" width="60" height="160"/><rect x="50" y="-80" width="60" height="160"/></g>
  <g class="tealp o"><circle cx="-60" cy="-40" r="18"/><circle cx="-60" cy="10" r="18"/></g>
  <g class="coralp o"><rect x="-6" y="-56" width="32" height="32"/></g>
  <g class="goldp o"><path d="M60 20l20-34 20 34z"/></g>
</g>
<path d="M280 240h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('clerk', '窓口で書類を扱う係員のイラスト。', f"""
<g transform="translate(340 290)">
  <path d="M-150-30h300v40h-300z" class="goldd o"/>
  <path d="M-150-30h300v-16h-300z" class="goldp o"/>
</g>
{person(380,250,1.0,-1,'blue','blue','reach','bob','smile')}
<g transform="translate(260 250)"><path d="M-50-30h100v40h-100z" class="paper"/></g>
{person(140,346,1.0,1,'coral','gold','give','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('cliff', '切り立ったがけのイラスト。', f"""
<path d="M0 260h600v140H0z" class="bluep" opacity=".6"/>
<g fill="#b6bfc9" stroke="{INK}" stroke-width="3"><path d="M60 260V80h240v180z"/></g>
<g class="green o"><path d="M60 80h240v-24H60z"/></g>
<g fill="none" stroke="#8b98a6" stroke-width="5"><path d="M120 100v150M200 90v170M260 110v150"/></g>
<g fill="none" stroke="#fffdf6" stroke-width="5" opacity=".8"><path d="M340 300q40-20 80 0t80 0"/></g>
""", ground=False)

add('clinic', '小さな診療所のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-140 80h280V-40h-280z" fill="#fffdf6" class="o"/>
  <path d="M-160-40l160-80 160 80z" class="teal o"/>
  <g transform="translate(0 -70)"><path d="M-10-16h20v12h12v20h-12v12h-20v-12h-12v-20h12z" fill="#fffdf6"/></g>
  <path d="M-30 80V20h60v60z" class="goldd o"/>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="2"><rect x="-110" y="0" width="50" height="40"/><rect x="60" y="0" width="50" height="40"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('clip', '紙をとめるクリップのイラスト。', f"""
<g transform="translate(320 240)">
  <path d="M-90-110h180v200h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-60h120M-60-20h120M-60 20h90"/></g>
</g>
<g transform="translate(240 170) rotate(-8)">
  <path d="M-20-60q40-20 40 20t-30 40-24-30 30-24 22 40-40 20" fill="none" stroke="#8b98a6" stroke-width="9"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('closure', '店の戸が閉ざされて終わるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-130h320v260h-320z" fill="#e4e9ee" class="o"/>
  <path d="M-130-100h260v200h-260z" fill="#c9d3dc" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-130 {-80+i*30}h260"/>' for i in range(7))}</g>
  <g transform="translate(0 0) rotate(-8)"><path d="M-100-20h200v44h-200z" class="paper"/><g fill="{INK}"><rect x="-70" y="-6" width="140" height="16"/></g></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 130l34 34M514 130l-34 34"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('cluster', 'かたまって群れているイラスト。', f"""
<g class="teal o">
  <circle cx="200" cy="200" r="26"/><circle cx="250" cy="240" r="26"/><circle cx="190" cy="260" r="26"/><circle cx="250" cy="180" r="26"/><circle cx="150" cy="220" r="26"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><circle cx="205" cy="225" r="100"/></g>
<g class="tealp o"><circle cx="450" cy="180" r="20"/><circle cx="510" cy="290" r="20"/></g>
""", ground=False)

add('coalition', '複数の党が組んで一つになるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-70-60h140v120h-140z" class="tealp o"/>
</g>
<g transform="translate(300 240)">
  <path d="M-60-60h120v120h-120z" class="coralp o"/>
</g>
<g transform="translate(470 240)">
  <path d="M-90-80h180v160h-180z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o"><rect x="-70" y="-60" width="60" height="120"/></g>
  <g class="coralp o"><rect x="0" y="-60" width="60" height="120"/></g>
</g>
<path d="M370 240h20" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('cocktail', '飾りのついたカクテルのイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-80-70h160l-70 80v70h-20v-70z" fill="#f7fbfe" stroke="{INK}" stroke-width="3"/>
  <path d="M-56-50h112l-46 54h-20z" class="coralp o"/>
  <path d="M-60 80h120v14h-120z" fill="#f7fbfe" stroke="{INK}" stroke-width="3"/>
  <path d="M40-90l30-30" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
  <g class="gold o"><circle cx="74" cy="-124" r="16"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('coincidence', '二人がたまたま同じ物を持ち合わせるイラスト。', f"""
{person(190,346,1.15,1,'teal','blue','carry','short','surprised')}
{person(410,346,1.15,-1,'coral','gold','carry','bob','surprised')}
<g class="goldp o"><rect x="160" y="230" width="60" height="46"/><rect x="380" y="230" width="60" height="46"/></g>
<g class="golds" style="stroke-width:5"><path d="M300 200v-26M260 220l-20-20M340 220l20-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('collision', '二台がぶつかり合う衝突のイラスト。', f"""
<g transform="translate(180 280)">
  <path d="M-100 40h200v-40l-40-40h-120l-40 40z" class="tealp o"/>
  <circle cx="-60" cy="46" r="26" class="ink"/><circle cx="60" cy="46" r="26" class="ink"/>
</g>
<g transform="translate(430 280)">
  <path d="M-100 40h200v-40l-40-40h-120l-40 40z" class="coralp o"/>
  <circle cx="-60" cy="46" r="26" class="ink"/><circle cx="60" cy="46" r="26" class="ink"/>
</g>
<g transform="translate(300 230)">
  <path d="M0-60l24 46 52 6-38 36 10 52-48-26-48 26 10-52-38-36 52-6z" class="coral o"/>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('columnist', '新聞に自分の欄を書く人のイラスト。', f"""
{person(160,346,1.15,1,'violet','blue','reach','bob','neutral')}
<g transform="translate(400 230)">
  <path d="M-140-130h280v260h-280z" class="paper"/>
  <g fill="{INK}"><rect x="-110" y="-110" width="220" height="20"/></g>
  <path d="M-110-70h100v190h-100z" class="goldp o" opacity=".7"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M10 {-60+i*34}h100"/>' for i in range(6))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('comic', '笑いを誘う漫画のこまのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-130h400v260h-400z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M0-130v260M-200 0h400"/></g>
  <g transform="translate(-100 -66) scale(0.5)">{person(0,60,1.0,1,'coral','gold','up','bob','smile')}</g>
  <g transform="translate(100 -66)"><path d="M-50-30h100v40h-100z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/><g fill="none" stroke="{INK}" stroke-width="3"><path d="M-24-14q14 14 28 0"/></g></g>
  <g transform="translate(-100 66) scale(0.5)">{person(0,60,1.0,1,'teal','blue','up','short','smile')}</g>
  <g transform="translate(100 66)"><g class="golds" style="stroke-width:5"><path d="M-20-20l-24-18M20-20l24-18"/></g></g>
</g>
""", ground=True)

add('commander', '前に立って部隊に指示する指揮官のイラスト。', f"""
{person(180,346,1.3,1,'green','green','point','cap','neutral')}
<g transform="translate(180 236)"><path d="M-24-10h48v10h-48z" class="green o"/></g>
{person(400,346,1.0,1,'green','green','stand','cap','neutral')}
{person(490,346,1.0,1,'green','green','stand','cap','neutral')}
<path d="M260 220h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('commentator', '画面のわきで解説する人のイラスト。', f"""
<g transform="translate(400 230)">
  <path d="M-140-110h280v200h-280z" fill="#41506a"/>
  <path d="M-116-88h232v172h-232z" class="bluep"/>
  <g transform="translate(0 30) scale(0.5)">{person(0,20,1.0,1,'coral','gold','walk','short','neutral')}</g>
</g>
{person(140,346,1.1,1,'blue','blue','point','short','neutral')}
<g transform="translate(190 240)">
  <path d="M-6-10h40v20h-40z" class="ink"/>
  <circle cx="44" r="16" fill="#7f8ea6" stroke="{INK}" stroke-width="2"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('commitment', '約束に署名して、やり切ると決めるイラスト。', f"""
{person(180,346,1.2,1,'blue','blue','reach','short','neutral')}
<g transform="translate(400 240)">
  <path d="M-110-100h220v200h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-60h160M-80-20h160"/></g>
  <path d="M-80 50q40-24 80 0" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-80 70h160"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M270 170l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
