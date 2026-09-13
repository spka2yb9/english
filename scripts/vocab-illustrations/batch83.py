"""第83回: h〜i の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
add('headquarters', '各地の拠点をまとめる本社のイラスト。', f"""
{tower(300,320,1.15,'teal',6)}
<path d="M300 108v-40" class="a"/>
<path d="M300 68h70l-16 18 16 18h-70z" class="coral o"/>
{tower(110,330,0.5,'blue',3)}
{tower(500,330,0.5,'blue',3)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M160 300h80M440 300h-80"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('healthcare', '体を守る医療のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-34-120h68v86h86v68h-86v86h-68v-86h-86v-68h86z" class="coralp o"/>
  <path d="M0-40q-34-40-60-8-24 30 60 84 84-54 60-84-26-32-60 8z" class="coral o"/>
</g>
{hand(120,300,1)}
{hand(480,300,-1)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('hearing', '耳が音を捉える聴力のイラスト。', f"""
<g transform="translate(390 210)">
  <path d="M-60 130v-40q-60-20-60-90 0-80 76-80t76 76q0 46-40 60-16 6-16 24v50z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-20-40q0-30 30-30t30 34-30 30" fill="none" stroke="{SKINL}" stroke-width="6"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" stroke-linecap="round">
  <path d="M200 190q-24 30 0 60M150 160q-46 60 0 120M100 130q-70 90 0 180"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('heaven', '雲の上に開かれた天国の門のイラスト。', f"""
{cloud(180,290,1.4,'blue')}
{cloud(420,300,1.5,'blue')}
{cloud(300,320,1.3,'blue')}
<g transform="translate(300 180)">
  <path d="M-90 100v-70q0-70 90-70t90 70v70z" fill="#fffdf6" class="o"/>
  <path d="M0-40v140M-90 30h180" class="a"/>
  <circle cx="0" cy="-118" r="34" fill="none" stroke="{TONES['gold'][0]}" stroke-width="8"/>
</g>
<g class="golds"><path d="M120 120l-30-26M480 120l30-26M300 20v-6"/></g>
""", ground=False)

add('heavily', '激しく降りしきる雨のイラスト。', f"""
{cloud(300,110,2,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="6" stroke-linecap="round">
  {''.join(f'<path d="M{80+i*32} {190+(i%3)*16}l-18 70"/>' for i in range(16))}
</g>
{person(300,352,1,1,'coral','blue','stand','short','sad')}
<path d="M60 376h480" class="a"/>
""", ground=True)

add('hell', '炎に包まれた地獄のイラスト。', f"""
<path d="M0 250h600v150H0z" fill="#3a2a2c"/>
{flame(200,330,1.6)}
{flame(360,340,1.3)}
{flame(470,326,1.1)}
<g fill="none" stroke="#8b98a6" stroke-width="5" stroke-linecap="round">
  <path d="M60 250h480M100 300h60M470 300h50"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M300 90v90"/></g>
""", ground=False, arrow=True)

add('helmet', '頭を守るヘルメットのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-120 40v-30q0-120 120-120T120 10v30z" class="gold o"/>
  <path d="M-120 40h240v26h-240z" class="goldd o"/>
  <path d="M-60-90q60-30 120 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
  <path d="M120 10h40v40h-40z" class="goldp o"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('herb', '香りのよい草を摘むイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-60 0h120l-14 60h-92z" class="coralp o"/>
  <path d="M-66-12h132v14h-132z" class="coral o"/>
  <path d="M0 0v-70M-30 0v-50M30 0v-56" class="greens"/>
  <g class="greenp o">
    <ellipse cx="-16" cy="-56" rx="18" ry="10" transform="rotate(-30 -16 -56)"/>
    <ellipse cx="16" cy="-62" rx="18" ry="10" transform="rotate(30 16 -62)"/>
    <ellipse cx="-42" cy="-46" rx="16" ry="9" transform="rotate(-30 -42 -46)"/>
    <ellipse cx="44" cy="-50" rx="16" ry="9" transform="rotate(30 44 -50)"/>
    <ellipse cx="0" cy="-82" rx="16" ry="9"/>
  </g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7"><path d="M420 180q-30 20-40 50M440 200q-40 10-50 40"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('hesitation', 'どちらへ進むか決めきれずためらうイラスト。', f"""
{person(300,352,1.2,1,'teal','blue','think','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)">
  <path d="M240 300L110 240M360 300l130-60"/>
</g>
<g transform="translate(300 130)">
  <path d="M-22-46q0-26 24-26t24 24q0 20-24 26v14" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="2" cy="26" r="7" class="coral"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('hierarchy', '上下に段が分かれた序列のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-40-140h80v50h-80z" class="teal o"/>
  <path d="M-150-40h80v50h-80zM70-40h80v50H70z" class="tealp o"/>
  <path d="M-210 90h60v46h-60zM-100 90h60v46h-60zM40 90h60v46H40zM150 90h60v46h-60z" class="bluep o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
    <path d="M0-90v30M-110-60h220M-110-60v20M110-60v20"/>
    <path d="M-110 10v40M110 10v40M-180 50h140M-180 50v40M-40 50v40M40 50h140M40 50v40M180 50v40"/>
  </g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('hip', '体の腰のあたりを示したイラスト。', f"""
<g transform="translate(300 210)">
  <circle cx="0" cy="-140" r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-56-96q56-24 112 0l-16 96h-80z" class="teal o"/>
  <path d="M-72 0h144v46q0 20-20 20h-104q-20 0-20-20z" class="bluep o"/>
  <path d="M-46 66l-10 110M46 66l10 110" fill="none" stroke="{TONES['blue'][2]}" stroke-width="20" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><ellipse cx="300" cy="240" rx="100" ry="52"/></g>
<path d="M470 240h-70" class="a" marker-end="url(#ar)"/>
<path d="M60 392h480" class="a"/>
""", ground=True, arrow=True)

add('homeland', '心の帰る故国を思うイラスト。', f"""
{person(150,352,1.1,1,'teal','blue','stand','short','smile')}
<g transform="translate(400 220)">
  <path d="M-130 60q-30-70 20-110t130-20q60 20 60 70t-70 70q-90 20-140-10z" class="greenp o"/>
  <path d="M-10 20v-70h4l50 18-50 18" class="ink"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M240 150q-20-26 0-36 20-10 20 14 0-24 20-14 20 10 0 36l-20 20z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M210 220h60"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('honor', 'たたえられて贈られる名誉のメダルのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-60-140l40 90h-40zM60-140l-40 90h40z" class="coral o"/>
  <circle cx="0" cy="20" r="80" class="gold o"/>
  <circle cx="0" cy="20" r="58" class="goldp o"/>
  <path d="M0-26l16 34 38 4-28 26 8 38-34-20-34 20 8-38-28-26 38-4z" class="goldd"/>
</g>
<g class="golds"><path d="M150 120l-26-22M450 120l26-22M300 50v-24"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('hook', 'フックに物を引っかけるイラスト。', f"""
<g transform="translate(300 160)">
  <path d="M-140-60h280v20h-280z" class="ink"/>
  <path d="M0-40v70q0 50 44 50t44-44q0-24-24-30" fill="none" stroke="{MUTED}" stroke-width="14" stroke-linecap="round"/>
</g>
<g transform="translate(344 300)">
  <path d="M-70-40h140v90h-140z" class="teal o"/>
  <path d="M-30-40v-20h60v20" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('horizon', '空と海が交わる地平線のイラスト。', f"""
<path d="M0 0h600v230H0z" fill="#e6f0fb"/>
<path d="M0 230h600v170H0z" class="bluep"/>
<path d="M0 230h600" class="a"/>
<circle cx="300" cy="196" r="46" class="goldp o"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3">
  <path d="M60 300q40-16 80 0t80 0M340 340q40-16 80 0t80 0M120 380q40-16 80 0t80 0"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" marker-end="url(#ar)"><path d="M470 130v80"/></g>
""", ground=False, arrow=True)

add('horn', '頭に生えた角のイラスト。', f"""
<g transform="translate(300 250)">
  <ellipse cx="0" cy="20" rx="86" ry="96" class="goldp o"/>
  <ellipse cx="0" cy="70" rx="46" ry="40" class="gold o"/>
  <ellipse cx="-16" cy="66" rx="7" ry="10" class="ink"/><ellipse cx="16" cy="66" rx="7" ry="10" class="ink"/>
  <circle cx="-40" cy="-10" r="8" class="ink"/><circle cx="40" cy="-10" r="8" class="ink"/>
  <path d="M-70-64q-60-30-56-96 40 26 66 76z" fill="#e7ded0" class="o"/>
  <path d="M70-64q60-30 56-96-40 26-66 76z" fill="#e7ded0" class="o"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('horror', '暗がりの影におびえる恐怖のイラスト。', f"""
<path d="M0 0h600v400H0z" fill="#2c2f3d"/>
<path d="M0 306h600v94H0z" fill="#3b4050"/>
{person(200,352,1.2,1,'blue','blue','up','short','surprised')}
<g fill="#1d2029">
  <path d="M420 360q-40-90 0-150 20-30 60-30t60 30q40 60 0 150z"/>
  <circle cx="480" cy="150" r="46"/>
</g>
<g fill="{TONES['coral'][0]}"><circle cx="464" cy="146" r="7"/><circle cx="498" cy="146" r="7"/></g>
<g fill="none" stroke="#8b98a6" stroke-width="5" stroke-linecap="round"><path d="M140 170l-16-24M200 150v-26M264 168l16-24"/></g>
""", ground=False)

add('hostage', '閉じ込められ引き換えを求められる人質のイラスト。', f"""
<g transform="translate(220 220)">
  <path d="M-140-130h280v270h-280z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="8">{''.join(f'<path d="M{-100+i*50} -130v270"/>' for i in range(5))}</g>
</g>
{person(220,340,0.9,1,'coral','blue','stand','short','sad')}
<g transform="translate(470 250)">
  <path d="M-56-30h112v60h-112z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 190q-60-40-120-30"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('hostility', '仕切りをはさんでにらみ合う敵意のイラスト。', f"""
{person(160,352,1.2,1,'blue','blue','stand','short','sad')}
{person(440,352,1.2,-1,'coral','gold','stand','bob','sad')}
<g fill="none" stroke="{MUTED}" stroke-width="8"><path d="M300 130v240"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M232 214h48M320 214h48M240 180l-16-16M360 180l16-16"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('housing', 'ずらりと並ぶ住宅のイラスト。', f"""
<g transform="translate(150 320)">
  <path d="M-50 0v-60h100V0z" fill="#fffdf6" class="o"/>
  <path d="M-62-60L0-104l62 44z" class="coral o"/>
  <path d="M-14-36h28V0h-28z" class="corald o"/>
</g>
<g transform="translate(300 320)">
  <path d="M-50 0v-70h100V0z" fill="#fffdf6" class="o"/>
  <path d="M-62-70L0-114l62 44z" class="teal o"/>
  <path d="M-14-40h28V0h-28z" class="teald o"/>
</g>
<g transform="translate(450 320)">
  <path d="M-50 0v-60h100V0z" fill="#fffdf6" class="o"/>
  <path d="M-62-60L0-104l62 44z" class="gold o"/>
  <path d="M-14-36h28V0h-28z" class="goldd o"/>
</g>
{tower(540,320,0.55,'blue',5)}
<path d="M60 340h480" class="a"/>
""", ground=True)

add('humour', '冗談を言って笑い合うユーモアのイラスト。', f"""
{person(160,352,1.15,1,'teal','blue','point','short','smile')}
{person(450,352,1.15,-1,'coral','gold','up','bob','smile')}
<g transform="translate(300 150)">
  <path d="M-80-50h160v80h-160zM-40 30l-12 30 36-30z" fill="#fffdf6" class="o"/>
  <circle cx="0" cy="-10" r="30" class="goldp o"/>
  <g fill="{INK}"><circle cx="-11" cy="-18" r="4"/><circle cx="11" cy="-18" r="4"/></g>
  <path d="M-14 0q14 16 28 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round"><path d="M520 200l20-16M540 250h22"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('hunger', '皿が空でおなかがすいているイラスト。', f"""
{person(180,352,1.2,1,'teal','blue','hold','short','sad')}
<g transform="translate(430 280)">
  <ellipse rx="110" ry="30" fill="#fffdf6" class="o"/>
  <ellipse rx="70" ry="18" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-150-40v70M-150-40l-8 34h16z" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M150-40v70" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 8"><ellipse cx="196" cy="290" rx="46" ry="34"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('hunting', '弓を構えて獲物を狙う狩りのイラスト。', f"""
{tree(90,340,1)}
{tree(540,340,1.1)}
{person(200,350,1.1,1,'green','gold','point','cap','neutral')}
<g transform="translate(250 250)">
  <path d="M0-60q40 60 0 120" fill="none" stroke="{TONES['gold'][2]}" stroke-width="7"/>
  <path d="M0-60L-14 0 0 60" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-14 0h80M60-10l16 10-16 10" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g transform="translate(430 300)">
  <ellipse rx="56" ry="34" class="goldd o"/>
  <circle cx="46" cy="-40" r="22" class="goldd o"/>
  <path d="M40-58l-14-30 20 16M58-58l14-30-20 16" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
  <path d="M-40 30v30M20 32v28" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('hypothesis', 'たぶんこうだろうと立てる仮説のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-190-130h380v240h-380z" class="paper"/>
  <circle cx="-100" cy="-40" r="34" class="teal o"/>
  <path d="M-40-40h50" class="a" marker-end="url(#ar)"/>
  <path d="M50-80h100v80H50z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
  <path d="M84-64q0-16 16-16t16 14q0 12-16 16v10" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
  <circle cx="100" cy="-14" r="5" class="coral"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-150 50h300M-150 84h230"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('icon', '画面に並ぶ小さなアイコンのイラスト。', f"""
<g transform="translate(300 190)">
  <path d="M-160-140h320v280h-320z" class="ink"/>
  <path d="M-146-126h292v252h-292z" fill="#fffdf6"/>
  <g class="teal o"><rect x="-110" y="-96" width="70" height="70" rx="18"/></g>
  <g class="coral o"><rect x="-20" y="-96" width="70" height="70" rx="18"/></g>
  <g class="gold o"><rect x="70" y="-96" width="70" height="70" rx="18"/></g>
  <g class="violet o"><rect x="-110" y="0" width="70" height="70" rx="18"/></g>
  <g class="green o"><rect x="-20" y="0" width="70" height="70" rx="18"/></g>
  <g class="blue o"><rect x="70" y="0" width="70" height="70" rx="18"/></g>
  <g fill="#fffdf6"><circle cx="-75" cy="-61" r="16"/><path d="M-3-79h36v36H-3z"/><path d="M105-79l20 36h-40z"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><rect x="252" y="82" width="96" height="96" rx="24"/></g>
""", ground=False)

add('id', '顔写真つきの身分証のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-120h380v240h-380z" class="paper"/>
  <path d="M-190-120h380v40h-380z" class="teal o"/>
  <g transform="translate(-100 20)">
    <circle cx="0" cy="-30" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
    <path d="M-46 60v-16q0-30 46-30t46 30v16z" class="blue o"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M0-30h150M0 10h150M0 50h110"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('identification', '証明書と本人を照らし合わせて確かめるイラスト。', f"""
{face(160,210,80,'smile')}
<g transform="translate(430 210)">
  <path d="M-120-90h240v180h-240z" class="paper"/>
  <g transform="translate(-58 10)">
    <circle cx="0" cy="-24" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
    <path d="M-36 46v-12q0-24 36-24t36 24v12z" class="blue o"/>
  </g>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M10-30h90M10 6h90M10 40h70"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M250 200h50"/></g>
{ck(300,300,1)}
<path d="M60 356h480" class="a"/>
""", ground=True)

add('idiot', 'ばかげたことをして周りにあきれられるイラスト。', f"""
{person(300,352,1.2,1,'gold','blue','up','short','smile')}
<g transform="translate(300 196)">
  <path d="M-46 0h92l-10 40h-72z" class="bluep o"/>
  <ellipse cy="0" rx="46" ry="12" class="blue o"/>
</g>
<path d="M470 120v240" fill="none" stroke="{MUTED}" stroke-width="14"/>
<g class="a" marker-end="url(#ar)"><path d="M360 260h70"/></g>
{person(120,352,1,-1,'teal','violet','think','bob','sad')}
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('ignorance', '目かくしをされて何も知らないイラスト。', f"""
{person(220,352,1.25,1,'teal','blue','stand','short','neutral')}
<g transform="translate(220 218)">
  <path d="M-34-8h68v20h-68z" class="corald o"/>
</g>
<g transform="translate(450 210)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-56-40h112M-56 0h112M-56 40h80"/></g>
</g>
<g transform="translate(300 130)">
  <path d="M-20-30q0-24 22-24t22 22q0 18-22 24v12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"/>
  <circle cx="2" cy="34" r="6" class="coral"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('illustration', '本のページに描かれた挿絵のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-220-130h440v260h-440z" class="paper"/>
  <path d="M0-130v260" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-190-90h150M-190-56h150M-190-22h120"/></g>
  <path d="M-190 20h150v90h-150z" class="tealp o"/>
  <path d="M-190 110l50-56 40 34 34-30 26 52z" class="teal o"/>
  <circle cx="-70" cy="44" r="14" class="gold o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M40-90h150M40-56h150M40-22h120M40 12h150M40 46h100"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('imagery', '頭の中に鮮やかな情景が浮かぶイラスト。', f"""
{person(150,352,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(400 190)">
  <path d="M-160-110h320v220h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160 110v-70l90-80 70 60 60-50 100 70v70z" class="greenp o"/>
  <circle cx="80" cy="-60" r="34" class="goldp o"/>
  <path d="M-160 40l90-80 70 60" fill="none" stroke="{TONES['green'][2]}" stroke-width="4"/>
</g>
<g class="o" fill="#fffdf6"><circle cx="236" cy="270" r="16"/><circle cx="212" cy="300" r="11"/></g>
""", ground=False)

add('immediately', '合図と同時にただちに動き出すイラスト。', f"""
<g transform="translate(180 200)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <path d="M-16-104h32v20h-32z" class="ink"/>
  <path d="M0 0v-64" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M0 0l40 24" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7" stroke-linecap="round"/>
  <circle r="8" class="ink"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M320 120l-50 100h40l-20 80 70-110h-44l24-70z"/>
</g>
{person(480,352,1.15,1,'teal','blue','walk','short','smile')}
<path d="M60 376h480" class="a"/>
""", ground=True)

add('immigrant', '荷物を持って別の国へ移り住む人のイラスト。', f"""
{person(180,350,1.15,1,'teal','blue','carry','short','smile')}
<g transform="translate(240 320)">
  <path d="M-40-30h80v60h-80z" class="goldd o"/>
  <path d="M-16-44h32v14h-32z" class="a" fill="none"/>
  <path d="M-40 0h80" class="a"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12"><path d="M330 110v250"/></g>
<g transform="translate(470 250)">
  <path d="M-6 110V-90" class="a"/>
  <path d="M-6-90h96v66h-96z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M270 180h120"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('immigration', '入国審査の窓口で手続きをするイラスト。', f"""
<g transform="translate(370 250)">
  <path d="M-150 0h300v90h-300z" class="teal o"/>
  <path d="M-160-14h320v20h-320z" class="teald o"/>
  <path d="M-150-140h300v126h-300z" fill="#fffdf6" class="o"/>
  <path d="M-40-110h80v60h-80z" class="coralp o"/>
</g>
{person(140,352,1.1,1,'gold','blue','carry','bob','smile')}
<g transform="translate(300 200)">
  <path d="M-40-30h80v60h-80z" class="bluep o"/>
  <circle r="14" class="gold o"/>
</g>
<g fill="none" stroke="{GRN}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><path d="M470 170l16 18 30-36"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('impossible', 'どうやってもはまらず無理だと分かるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-180-40h360v130h-360z" class="tealp o"/>
  <circle cx="0" cy="-40" r="70" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(300 130)">
  <path d="M-70-70h140v140h-140z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 210v40"/></g>
{xx(470,150,1.2)}
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('impression', '判を押して残る印象のイラスト。', f"""
<g transform="translate(220 180)">
  <path d="M-70-40h140v60h-140z" class="violet o"/>
  <path d="M-30-90h60v50h-60z" class="violetd o"/>
  <path d="M-70 20h140v20h-140z" class="violetp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M220 250v40"/></g>
<g transform="translate(430 290)">
  <path d="M-120-70h240v130h-240z" class="paper"/>
  <circle cx="-10" cy="0" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M-40-16h60M-40 12h60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('imprisonment', '鉄格子の中に閉じ込められる投獄のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-180-140h360v290h-360z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="9">{''.join(f'<path d="M{-130+i*65} -140v290"/>' for i in range(5))}</g>
  <path d="M-180-140h360v24h-360z" class="ink"/>
</g>
{person(300,340,0.9,1,'blue','blue','stand','short','sad')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('inability', '力が足りずどうしてもできないイラスト。', f"""
{person(230,352,1.2,1,'teal','blue','up','short','sad')}
{box(230,180,180,90,0,'gold')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"><path d="M130 250l-20 20M330 250l20 20"/></g>
{xx(470,200,1.2)}
<path d="M60 376h480" class="a"/>
""", ground=True)

add('incentive', 'ごほうびに引かれて力が出るイラスト。', f"""
{person(180,352,1.15,1,'teal','blue','walk','short','smile')}
<g transform="translate(470 220)">
  <path d="M-6 140V-60" class="a"/>
  <path d="M-60-120h120v70h-120z" class="gold o"/>
  <path d="M0-120l16 34 38 6-28 26 8 38-34-20-34 20 8-38-28-26 38-6z" class="goldd" transform="translate(0 62) scale(0.8)"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M250 300h160"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('inch', 'ものさしの短い目盛りを示すイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-250-40h500v80h-500z" class="goldp o"/>
  <g fill="none" stroke="{INK}" stroke-width="3">
    {''.join(f'<path d="M{-230+i*40} -40v{30 if i%2==0 else 18}"/>' for i in range(12))}
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M70 150h36M146 150h-36"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3"><path d="M70 130v40M110 130v40"/></g>
<path d="M60 336h480" class="a"/>
""", ground=True, arrow=True)

add('incident', '突然起きた出来事のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M0-140l40 70 76-24-30 74 74 40-74 40 30 74-76-24-40 70-40-70-76 24 30-74-74-40 74-40-30-74 76 24z" class="coralp o"/>
  <g fill="{TONES['coral'][2]}"><rect x="-14" y="-70" width="28" height="86" rx="14"/><circle cy="42" r="17"/></g>
</g>
{person(110,356,0.8,-1,'teal','blue','walk','short','surprised')}
{person(500,356,0.8,1,'gold','violet','walk','bob','surprised')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('inclusion', '外にいた人を輪の中に迎え入れるイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="14 12"><circle cx="250" cy="240" r="150"/></g>
{person(180,330,0.85,1,'teal','blue','stand','short','smile')}
{person(300,330,0.85,-1,'gold','blue','stand','bob','smile')}
{person(490,340,0.9,-1,'coral','violet','walk','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M470 200q-60-30-110-20"/></g>
{ck(250,150,0.9)}
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('income', '手元に入ってくるお金のイラスト。', f"""
<g transform="translate(320 300)">
  <path d="M-140-50h280v110h-280z" class="goldd o"/>
  <path d="M-140-50h280v30h-280z" class="gold o"/>
  <path d="M40 0h100v40H40z" class="goldp o"/>
</g>
<g transform="translate(220 140)">
  <path d="M-70-30h140v60h-140z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 190l40 50"/></g>
<g class="gold o"><ellipse cx="420" cy="150" rx="30" ry="13"/><ellipse cx="420" cy="132" rx="30" ry="13"/></g>
<g class="a" marker-end="url(#ar)"><path d="M420 180v50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('independence', '支えの手が離れて自分の足で立つイラスト。', f"""
{person(340,352,1.3,1,'teal','blue','stand','short','smile')}
{hand(110,230,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 9"><path d="M170 230h60"/></g>
{xx(250,230,0.7,MUTED)}
{ck(460,200,1)}
<path d="M60 376h480" class="a"/>
""", ground=True)

add('index', 'ページの手がかりを並べた索引のイラスト。', f"""
<g transform="translate(280 210)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
    {''.join(f'<path d="M-140 {-90+i*40}h180"/>' for i in range(6))}
  </g>
  <g fill="{INK}">{''.join(f'<rect x="110" y="{-98+i*40}" width="30" height="8"/>' for i in range(6))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="5 7">{''.join(f'<path d="M50 {-92+i*40}h56"/>' for i in range(6))}</g>
</g>
<g class="coral o"><rect x="460" y="90" width="40" height="46" rx="6"/></g>
<g class="teal o"><rect x="460" y="150" width="40" height="46" rx="6"/></g>
<g class="gold o"><rect x="460" y="210" width="40" height="46" rx="6"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
