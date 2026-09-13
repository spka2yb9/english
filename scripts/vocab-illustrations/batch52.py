"""第52回: 公開・確認・広げる・包むなど39語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('unveil', '布を取り払って、新作をお披露目するイラスト。', f"""
<g transform="translate(390 250)">
  <path d="M-90 90V-70h180v160z" class="teal o"/>
  <path d="M-110-80q110-50 220 0" fill="none" stroke="{MUTED}" stroke-width="12" stroke-linecap="round"/>
</g>
{person(150,346,1.1,1,'coral','blue','up','bob','smile')}
<path d="M240 180q60-40 120-20" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:5"><path d="M500 150l26-20M510 190h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('upgrade', '古い型から、性能のよい新しい型へ上げるイラスト。', f"""
<g transform="translate(170 270)">
  <path d="M-80-60h160v120h-160z" fill="#dfe6ea" class="o"/>
  <g fill="{MUTED}"><rect x="-50" y="-30" width="100" height="20"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-90-80h180v160h-180z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-60" y="-40" width="120" height="24"/><rect x="-60" y="0" width="80" height="24"/></g>
  <g transform="translate(60 -70)"><path d="M0-24l8 16 18 2-13 13 3 18-16-9-16 9 3-18-13-13 18-2z" class="gold o"/></g>
</g>
<path d="M280 240l50-30" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('uphold', '決まりの札を高くかかげて支えるイラスト。', f"""
{person(300,346,1.3,1,'blue','blue','up','short','neutral')}
<g transform="translate(300 130)">
  <path d="M-100-50h200v90h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-20h140M-70 10h100"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M170 260v-60M430 260v-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('upset', '積み木がくずれて、ろうばいするイラスト。', f"""
<g transform="translate(400 320)">
  <g class="tealp o" transform="rotate(20)"><rect x="-50" y="-30" width="100" height="30"/></g>
  <g class="coralp o" transform="translate(90 -10) rotate(-30)"><rect x="-50" y="-30" width="100" height="30"/></g>
  <g class="goldp o" transform="translate(-60 -20) rotate(40)"><rect x="-50" y="-30" width="100" height="30"/></g>
</g>
{person(160,346,1.2,1,'coral','blue','up','bob','surprised')}
{drop(220,240,0.8)}
<path d="M260 230h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('urge', '身を乗り出して、強くこうしろと勧めるイラスト。', f"""
<g transform="translate(200 346) rotate(12)">{person(0,0,1.25,1,'coral','blue','point','short','flat')}</g>
<g transform="translate(360 180)">
  <path d="M-70-50h140v70h-140z" fill="#fffdf6" class="o"/>
  <path d="M-40 20l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><path d="M-14-30h28v40h-28zM-14 18h28v14h-28z" transform="translate(0 4)"/></g>
</g>
{person(490,346,1.1,-1,'teal','gold','stand','bob','neutral')}
<path d="M290 260h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('used', '何度も使って手になじんだ道具のイラスト。', f"""
{hand(200,200,1)}
<g transform="translate(300 290) rotate(20)">
  <path d="M-20-90h40v150h-40z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <path d="M-40-120h80v30h-80z" fill="#8b98a6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{SKINL}" stroke-width="3" opacity=".6"><path d="M-16-40h32M-16-10h32"/></g>
</g>
<g class="muted"><path d="M420 250q40-20 60 0M420 300q40-20 60 0"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M460 150l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('user', '道具を実際に使っている人のイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','reach','short','smile')}
<g transform="translate(370 250)">
  <path d="M-90-70h180v140h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-70-50h140v100h-140z" class="bluep o"/>
</g>
<path d="M270 250h30" class="a" marker-end="url(#ar)"/>
<circle cx="200" cy="230" r="90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('utilize', '余っていたものを役立つ形に使うイラスト。', f"""
<g transform="translate(160 260)">
  <g fill="#c8bfa4" stroke="{INK}" stroke-width="2"><rect x="-70" y="-40" width="60" height="80"/><rect x="0" y="-20" width="60" height="60"/></g>
</g>
<g transform="translate(430 260)">
  <path d="M-70-60h140v120h-140z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-40" y="-30" width="80" height="20"/><rect x="-40" y="10" width="50" height="20"/></g>
</g>
<path d="M270 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 150l20 20 34-40"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('valley', '二つの山にはさまれた谷のイラスト。', f"""
<path d="M0 400L180 120 300 300 420 120 600 400z" class="green o"/>
<path d="M240 400l60-100 60 100z" fill="#d9e6d9"/>
<path d="M260 400q40-40 80 0" fill="none" stroke="{TONES['blue'][0]}" stroke-width="10"/>
{sun(500,90,26)}
<path d="M300 200v60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('valuable', '厳重に守られた、値打ちのある宝石のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-130-80h260v180h-260z" fill="#dfe6ea" class="o"/>
  <path d="M-100-50h200v130h-200z" fill="#f7fbfe" class="o"/>
  <g transform="translate(0 20)">
    <path d="M0-60l50 30v50L0 50l-50-30v-50z" class="violet o"/>
    <path d="M0-60v110" fill="none" stroke="#fffdf6" stroke-width="3"/>
  </g>
  <circle cx="100" cy="-14" r="14" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M180 120l-24-20M420 120l24-20"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('vanish', 'あったものが、跡形もなく消えるイラスト。', f"""
<g transform="translate(140 240)"><circle r="60" class="coral o"/></g>
<g transform="translate(300 240)" opacity=".4"><circle r="60" class="coral o"/></g>
<g transform="translate(460 240)"><circle r="60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"/></g>
<path d="M120 350h360" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('variety', '形も色もちがうものが取りそろえられたイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-230-110h460v220h-460z" fill="#fffdf6" class="o"/>
  <g class="teal o"><circle cx="-160" cy="-40" r="34"/></g>
  <g class="coral o"><rect x="-80" y="-74" width="68" height="68"/></g>
  <g class="gold o"><path d="M60-74l40 68H20z"/></g>
  <g class="violet o"><path d="M170-74l40 34-40 34-40-34z"/></g>
  <g class="bluep o"><rect x="-170" y="30" width="90" height="50"/></g>
  <g class="greenp o"><circle cx="20" cy="55" r="28"/></g>
  <g class="goldp o"><rect x="120" y="26" width="90" height="58" rx="20"/></g>
</g>
""", ground=True)

add('various', 'いろいろな色の旗が並ぶイラスト。', f"""
<g transform="translate(300 300)"><path d="M-240-10h480v14h-480z" class="goldd o"/></g>
<g transform="translate(140 240)"><path d="M-4-90h8v90h-8z" class="ink"/><path d="M4-86h60v50H4z" class="coralp o"/></g>
<g transform="translate(260 240)"><path d="M-4-90h8v90h-8z" class="ink"/><path d="M4-86h60v50H4z" class="tealp o"/></g>
<g transform="translate(380 240)"><path d="M-4-90h8v90h-8z" class="ink"/><path d="M4-86h60v50H4z" class="goldp o"/></g>
<g transform="translate(500 240)"><path d="M-4-90h8v90h-8z" class="ink"/><path d="M4-86h60v50H4z" class="violetp o"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('verify', '書かれた数と実物を照らし合わせて確かめるイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-70" width="80" height="14"/><rect x="-60" y="-20" width="80" height="14"/><rect x="-60" y="30" width="80" height="14"/></g>
</g>
<g transform="translate(440 250)">
  <g class="teal o"><rect x="-60" y="-30" width="50" height="50"/><rect x="10" y="-30" width="50" height="50"/><rect x="-25" y="30" width="50" height="50"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M90 150l14 14 22-26"/><path d="M90 200l14 14 22-26"/><path d="M90 250l14 14 22-26"/>
</g>
<path d="M300 230h50M350 260h-50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('violate', '立入禁止の線を踏みこえて、決まりを破るイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-10-140h20v280h-20z" class="ink"/>
  <path d="M-160-60h320v20h-320z" class="coral o"/>
  <path d="M-160-20h320v20h-320z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
</g>
{person(360,346,1.15,1,'violet','blue','walk','cap','flat')}
<path d="M220 320h120" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 150l34 34M504 150l-34 34"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('violent', '激しく暴れて、物が飛び散るイラスト。', f"""
{person(200,346,1.3,1,'coral','blue','up','short','flat')}
<g class="coralp o" transform="translate(420 200) rotate(24)"><rect x="-50" y="-24" width="100" height="48"/></g>
<g class="tealp o" transform="translate(500 320) rotate(-30)"><rect x="-40" y="-20" width="80" height="40"/></g>
<g class="corals" style="stroke-width:6"><path d="M300 160l30-26M320 210h34M300 260l30 26"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('virus', 'とげのある形をしたウイルスのイラスト。', f"""
<g transform="translate(300 220)">
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="7">
    {''.join(f'<path d="M0 0L{int(150*__import__("math").cos(i*3.14159/6))} {int(150*__import__("math").sin(i*3.14159/6))}"/>' for i in range(12))}
  </g>
  <g class="coral o">{''.join(f'<circle cx="{int(150*__import__("math").cos(i*3.14159/6))}" cy="{int(150*__import__("math").sin(i*3.14159/6))}" r="14"/>' for i in range(12))}</g>
  <circle r="70" class="coralp o"/>
  <g class="coral o"><circle cx="-20" cy="-16" r="14"/><circle cx="24" cy="10" r="12"/><circle cx="-6" cy="30" r="10"/></g>
</g>
""", ground=False)

add('voice', '口から声が出て、波になって届くイラスト。', f"""
{face(200,200,85,'smile')}
<g transform="translate(200 240)"><ellipse rx="22" ry="16" fill="#8b4a3e"/></g>
<g class="corals" opacity=".9" style="stroke-width:6"><path d="M300 170q30 40 30 70t-30 70M360 140q46 56 46 100t-46 100M420 110q60 70 60 130t-60 130"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('vow', '指輪を交わして誓いを立てるイラスト。', f"""
{person(220,346,1.2,1,'blue','blue','reach','short','smile')}
{person(380,346,1.2,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(300 230)">
  <circle r="26" fill="none" stroke="{TONES['gold'][0]}" stroke-width="8"/>
  <path d="M0-40l8 14h-16z" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 170l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('wait', 'いすに座って、順番が来るのを待つイラスト。', f"""
<g transform="translate(300 300)">
  <g class="goldd o"><rect x="-230" y="-20" width="140" height="20"/><rect x="-70" y="-20" width="140" height="20"/><rect x="90" y="-20" width="140" height="20"/></g>
</g>
{person(160,300,0.85,1,'teal','blue','stand','short','neutral')}
{person(300,300,0.85,1,'coral','gold','stand','bob','neutral')}
<g transform="translate(470 200)">
  <circle r="54" fill="#fffdf6" class="o"/>
  <path d="M0-34v34l26 14" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('wander', '道からそれて、あてもなく歩き回るイラスト。', f"""
<path d="M60 300h180" fill="none" stroke="#e6dcc9" stroke-width="18"/>
<path d="M240 300q60-80 130-40t150-40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"/>
{person(420,300,1.05,1,'teal','blue','walk','short','neutral')}
{tree(120,340,0.8)}
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('war', '二つの陣営がぶつかり、町がこわれるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#dfe3e6"/>
<g transform="translate(140 250)"><path d="M-4-100h8v100h-8z" class="ink"/><path d="M4-96h70v46H4z" class="coralp o"/></g>
<g transform="translate(460 250)"><path d="M-4-100h8v100h-8z" class="ink"/><path d="M-74-96h70v46h-70z" class="tealp o"/></g>
<g fill="#c8c2b0" stroke="{INK}" stroke-width="3">
  <path d="M220 340v-90l40-30v120z"/><path d="M280 340v-60l50 20v40z"/><path d="M350 340v-100l40 40v60z"/>
</g>
<g class="muted" opacity=".9"><path d="M250 200q20-40 0-70M340 190q20-40 0-70"/></g>
<g class="a" marker-end="url(#ar)"><path d="M180 160h80M420 160h-80"/></g>
<path d="M60 350h480" class="a"/>
""", ground=False, arrow=True)

add('weaken', '太かった支えが細くなって、力が弱まるイラスト。', f"""
<g transform="translate(170 250)"><path d="M-40-100h80v200h-80z" class="teal o"/></g>
<g transform="translate(430 250)"><path d="M-12-100h24v200h-24z" class="tealp o"/></g>
<path d="M280 240h50" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:4"><path d="M470 150q20 20 0 40"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('web', 'クモが張った網の目のイラスト。', f"""
<g transform="translate(300 200)">
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M0 0L{int(180*__import__("math").cos(i*3.14159/4))} {int(180*__import__("math").sin(i*3.14159/4))}"/>' for i in range(8))}
    {''.join(f'<circle r="{40+i*45}"/>' for i in range(4))}
  </g>
</g>
<g transform="translate(300 200) scale(0.5)">
  <ellipse rx="56" ry="46" class="ink"/><circle cy="-50" r="26" class="ink"/>
  <g fill="none" stroke="{INK}" stroke-width="8"><path d="M-40-10l-70-40M-40 10l-80 20M40-10l70-40M40 10l80 20"/></g>
</g>
""", ground=False)

add('wedding', '式で誓いを交わす結婚式のイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-150 60q0-90 150-90t150 90z" class="coralp o" opacity=".6"/>
</g>
{person(240,346,1.25,1,'blue','blue','give','short','smile')}
<g transform="translate(370 346)">
  <path d="M-50-130q50-24 100 0 20 70 0 130h-100z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <circle cy="-160" r="30" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-32-170q4-34 32-34t32 34q-30-16-64 0z" fill="{HAIR}"/>
  <path d="M-50-100q-30 20-20 50" fill="none" stroke="{SKIN}" stroke-width="13" stroke-linecap="round"/>
</g>
<path d="M290 250h30" fill="none" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('welcome', '両手を広げて、うれしそうに迎え入れるイラスト。', f"""
{person(200,346,1.25,1,'coral','gold','up','bob','smile')}
{person(450,346,1.1,-1,'teal','blue','walk','short','smile')}
<g transform="translate(320 160)">
  <path d="M-80-50h160v70h-160z" fill="#fffdf6" class="o"/>
  <path d="M-40 20l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-56" y="-28" width="112" height="14"/></g>
</g>
<path d="M390 300h-90" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('western', '地図の西側の地域を示したイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-200-140h140v280h-140z" class="goldp o"/>
  <path d="M-60-140v280" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="10 8"/>
</g>
<g transform="translate(490 120)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M-26 0l26 12 26-12-26-12z" class="coral o"/>
</g>
<path d="M120 350h-40" class="a" marker-end="url(#ar)" transform="rotate(180 100 350)"/>
""", ground=True, arrow=True)

add('whip', '泡立て器でクリームをあわ立てるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-110-40h220l-20 100h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-96-10h192l-14 60h-164z" fill="#fffdf6" class="o"/>
  <path d="M-60-20q60-30 120 0 10 30-60 36t-60-36z" fill="#ffffff" stroke="{INK}" stroke-width="2"/>
</g>
<g transform="translate(300 170) rotate(14)">
  <path d="M-10-80h20v80h-20z" class="goldd o"/>
  <g fill="none" stroke="#8b98a6" stroke-width="4"><path d="M0 0q-40 30-30 80M0 0q40 30 30 80M0 0v80"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 200a90 90 0 0 1 40-40M420 200a90 90 0 0 0-40-40"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('whole', '切り分けていない、丸ごと全部のイラスト。', f"""
<g transform="translate(170 230)">
  <circle r="100" class="goldp o"/>
  <circle r="100" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(440 230)">
  <g fill="none" stroke="{INK}" stroke-width="3">
    <path d="M0 0v-100a100 100 0 0 1 86 50z" fill="#f7e6bd"/>
    <path d="M0 0l86 50a100 100 0 0 1-86 50z" fill="#f7e6bd" transform="translate(14 6)"/>
    <path d="M0 0l-86 50A100 100 0 0 1-86-50z" fill="#f7e6bd" transform="translate(-14 4)"/>
    <path d="M0 0v-100a100 100 0 0 0-86 50z" fill="#f7e6bd" transform="translate(-8-8)"/>
  </g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M130 350l20 20 34-40"/></g>
""", ground=True)

add('widen', 'せまかった道が、広い道に広がるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-240 100h480v20h-480z" fill="none"/>
  <path d="M-240 60L-60-80h120L240 60z" fill="#e6dcc9" stroke="{INK}" stroke-width="3"/>
  <path d="M-60-80h120" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 380h140M300 380H160"/></g>
<path d="M60 336h480" class="a"/>
""", ground=True, arrow=True)

add('winner', 'ゴールテープを切って一番になった人のイラスト。', f"""
{person(300,346,1.3,1,'coral','blue','up','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M180 260q120-30 240 0"/></g>
<g transform="translate(300 150)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
<g class="golds" style="stroke-width:5"><path d="M420 200l26-20M180 200l-26-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('wipe', '布で机の汚れをふき取るイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-230-20h460v40h-460z" class="goldd o"/>
  <g fill="#c8bfa4" opacity=".8"><circle cx="120" cy="-2" r="12"/><circle cx="170" cy="6" r="9"/></g>
</g>
<g transform="translate(220 260)">
  <path d="M-70-30q70-30 140 0 10 30-70 40-80-10-70-40z" class="tealp o"/>
</g>
{hand(220,180,1)}
<g class="a" marker-end="url(#ar)"><path d="M300 200h80"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 160l18 18 30-36"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('worldwide', '地球全体に広がっていることを示したイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="140" class="bluep o"/>
  <g class="green o"><path d="M-110-40q60-40 110-10t100-20v40q-60 30-110 0t-100 20z"/><path d="M-60 50q50-30 100 0t80-10v40q-50 30-100 0t-80 10z"/></g>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="3"><ellipse rx="140" ry="60"/><ellipse rx="60" ry="140"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="210" r="176"/></g>
""", ground=False)

add('worse', '状態がさらに悪くなっていくイラスト。', f"""
{face(150,200,70,'flat')}
{face(300,210,70,'sad')}
<g transform="translate(460 220)">
  {face(460,220,70,'sad')}
</g>
<path d="M120 340h360" class="a" marker-end="url(#ar)"/>
{drop(500,160,0.8)}
""", ground=False, arrow=True)

add('worship', '祭壇に向かって頭を下げ、あがめるイラスト。', f"""
<g transform="translate(420 250)">
  <path d="M-110 90h220v-30h-220z" class="goldd o"/>
  <path d="M-70 60V-40h140v100z" class="goldp o"/>
  <g transform="translate(0 -80)"><circle r="34" class="gold o"/><g class="golds" style="stroke-width:4"><path d="M0-50v-16M-40-30l-14-10M40-30l14-10"/></g></g>
</g>
<g transform="translate(180 346) rotate(24)">{person(0,0,1.2,1,'violet','blue','stand','short','neutral')}</g>
<path d="M260 260h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('worst', '三つのうち、いちばん悪いものを示したイラスト。', f"""
{face(150,200,66,'smile')}
{face(300,200,66,'flat')}
{face(460,200,66,'sad')}
<circle cx="460" cy="200" r="90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M120 330h360" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('wound', '腕の傷に手当てをするイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-180-40q30-30 90-30h120q40 0 40 40t-40 40h-120q-60 0-90-30z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-40-30q20 20 0 40" fill="none" stroke="{TONES['coral'][2]}" stroke-width="6"/>
  <g class="corals" style="stroke-width:5"><path d="M-40-70q-20-20-40-20M20-70q20-20 40-20"/></g>
</g>
<g transform="translate(430 320) rotate(-12)">
  <path d="M-70-24h140v48h-140z" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/>
  <path d="M-24-24h48v48h-48z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
</g>
<path d="M370 300h-60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('wow', '目を丸くして、思わず感嘆するイラスト。', f"""
{face(280,200,95,'smile')}
<g fill="#fffdf6" stroke="{INK}" stroke-width="3"><circle cx="244" cy="184" r="18"/><circle cx="316" cy="184" r="18"/></g>
<g fill="{INK}"><circle cx="244" cy="184" r="8"/><circle cx="316" cy="184" r="8"/></g>
<g transform="translate(280 250)"><ellipse rx="24" ry="26" fill="#8b4a3e"/></g>
<g class="golds" style="stroke-width:6"><path d="M410 130l30-24M430 180h34M410 230l30 24M150 130l-30-24M130 180H96"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('wrap', '箱を紙で包んで、ひもをかけるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-130-90h260v180h-260z" class="goldp o"/>
  <path d="M-16-90h32v180h-32z" class="coral o"/>
  <path d="M-130-16h260v32h-260z" class="coral o"/>
  <path d="M0-90q-40-50-70-20 20 30 70 20zM0-90q40-50 70-20-20 30-70 20z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 190a180 180 0 0 1 40-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
