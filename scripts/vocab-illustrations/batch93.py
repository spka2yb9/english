"""第93回: se〜su の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'

add('secure', 'しっかり鍵をかけて守るイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140-60h280v160h-280z" class="tealp o"/>
  <path d="M-70 0h140v70h-140z" class="gold o"/>
  <path d="M-40 0v-30q0-40 40-40t40 40V0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14"/>
  <circle cx="0" cy="34" r="12" class="goldd"/>
</g>
{ck(480,150,1.1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('sensitive', '軽く触れられただけでも痛むほど敏感なイラスト。', f"""
{person(340,352,1.3,1,'teal','blue','up','short','sad')}
{hand(120,250,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M186 250h60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M290 220l-20-20M340 200v-26M390 220l20-20"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><circle cx="270" cy="260" r="26"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('shape', 'いろいろな形を並べたイラスト。', f"""
<g transform="translate(300 210)">
  <circle cx="-160" cy="-60" r="56" class="tealp o"/>
  <path d="M-40-116h112v112h-112z" class="coralp o"/>
  <path d="M180-116l60 112H120z" class="goldp o"/>
  <path d="M-160 20l60 60-60 60-60-60z" class="violetp o"/>
  <ellipse cx="20" cy="80" rx="70" ry="46" class="greenp o"/>
  <path d="M180 30h70v100h-70z" class="bluep o"/>
</g>
""", ground=False)

add('slot', '細いすき間に差し込むイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-140-70h280v150h-280z" class="tealp o"/>
  <path d="M-50-50h100v18h-100z" class="ink"/>
</g>
<g transform="translate(300 140)">
  <ellipse rx="34" ry="14" class="gold o"/>
  <ellipse rx="18" ry="7" class="goldd o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 170v40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('solicitor', '書類を扱う事務弁護士のイラスト。', f"""
{sit(230,352,1.3,1,'violet','violet','short','neutral','lap')}
{chair(240,356,1.25,'gold',1)}
<g transform="translate(400 320)">
  <path d="M-130-30h260v20h-260z" class="goldd o"/>
  <path d="M-110-10v46M110-10v46" class="a"/>
  <path d="M-70-90h140v60h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-46-70h92M-46-50h70"/></g>
</g>
<g transform="translate(520 220)">
  <path d="M-40-70h80v140h-80z" class="teal o"/>
  <path d="M-26-54h52v108h-52z" fill="#fffdf6" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('solidarity', '腕を組み合ってひとつになる連帯のイラスト。', f"""
{person(140,352,1.1,1,'teal','blue','give','short','smile')}
{person(280,352,1.1,1,'coral','gold','give','bob','smile')}
{person(420,352,1.1,1,'gold','violet','give','short','smile')}
{person(540,352,1.1,1,'green','blue','stand','bun','smile')}
<g fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round">
  <path d="M190 290h40M330 290h40M470 290h40"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('solo', 'ひとりだけで演じる独奏のイラスト。', f"""
<path d="M300 60l150 300H150z" fill="{TONES['gold'][1]}" opacity="0.7"/>
{person(300,346,1.35,1,'violet','violet','up','bun','smile')}
<g transform="translate(300 200)">
  <path d="M0 30q-14 0-14-12t14-12q8 0 12 5v-45l30-9v14l-20 6v40q0 13-22 13z" fill="{INK}"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('soul', '体から立ちのぼる光のような魂のイラスト。', f"""
{person(220,352,1.2,1,'blue','blue','stand','short','neutral')}
<g opacity="0.55">
  <circle cx="420" cy="180" r="34" fill="{TONES['gold'][1]}" stroke="{TONES['gold'][0]}" stroke-width="3"/>
  <path d="M380 340v-90q0-50 40-50t40 50v90z" fill="{TONES['gold'][1]}" stroke="{TONES['gold'][0]}" stroke-width="3"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M290 250h60"/></g>
<g class="golds"><path d="M420 120v-24M340 150l-20-20M500 150l20-20"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('spam', '受信箱にあふれる迷惑メールのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-120h180v120h-180z" fill="#fffdf6" class="o"/>
  <path d="M-200-120L-110-52-20-120" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M-100-60h180v120h-180z" fill="#fffdf6" class="o"/>
  <path d="M-100-60L-10 8 80-60" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M20-130h180v120H20z" fill="#fffdf6" class="o"/>
  <path d="M20-130L110-62 200-130" fill="none" stroke="{INK}" stroke-width="3"/>
  <path d="M40 20h180v120H40z" fill="#fffdf6" class="o"/>
  <path d="M40 20l90 68 90-68" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
{xx(150,330,1.2)}
""", ground=False)

add('specification', '寸法まで書き込んだ仕様書のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-210-150h420v300h-420z" class="paper"/>
  <path d="M-120-80h240v140h-240z" class="tealp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="3" marker-end="url(#ar)">
    <path d="M-120-110h240M120-110h-240"/>
    <path d="M150-80v140M150 60V-80"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="2"><path d="M-120-124v20M120-124v20M136-80h28M136 60h28"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-180 96h340M-180 122h260"/></g>
</g>
""", ground=False, arrow=True)

add('specimen', 'ケースに留めて並べた標本のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="goldd o"/>
  <path d="M-176-116h352v232h-352z" fill="#fdf6e3" class="o"/>
  <g class="tealp o"><ellipse cx="-100" cy="-50" rx="26" ry="40"/></g>
  <g fill="none" stroke="{INK}" stroke-width="3"><path d="M-100-90v-20M-100-10v20"/></g>
  <g class="greenp o"><path d="M20-70q50-4 56 44-50 4-56-44z"/></g>
  <g class="coralp o"><circle cx="-60" cy="60" r="26"/></g>
  <g class="goldp o"><path d="M60 40h70v50H60z"/></g>
</g>
""", ground=False)

add('spectacle', '花火が上がる壮大な光景のイラスト。', f"""
<path d="M0 0h600v300H0z" fill="#1f2b3d"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M180 110l{int(70*__import__("math").cos(__import__("math").radians(a)))} {int(70*__import__("math").sin(__import__("math").radians(a)))}"/>' for a in range(0,360,30))}
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-linecap="round">
  {''.join(f'<path d="M430 160l{int(54*__import__("math").cos(__import__("math").radians(a)))} {int(54*__import__("math").sin(__import__("math").radians(a)))}"/>' for a in range(0,360,45))}
</g>
<path d="M0 300h600v100H0z" class="ground"/>
{person(180,376,0.8,1,'coral','blue','up','short','surprised')}
{person(300,376,0.8,1,'gold','violet','up','bob','surprised')}
{person(420,376,0.8,-1,'teal','gold','up','short','surprised')}
""", ground=False)

add('spectator', 'スタンドから試合を見つめる観客のイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-260-40h520v30h-520z" class="goldd o"/>
  <path d="M-260-80h520v30h-520z" class="goldd o"/>
</g>
{sit(130,290,0.8,1,'teal','blue','short','smile','down')}
{sit(250,290,0.8,1,'coral','gold','bob','smile','down')}
{sit(370,290,0.8,1,'gold','violet','short','smile','down')}
{sit(490,290,0.8,1,'green','blue','bun','smile','down')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M300 150v-60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('spectrum', '赤から紫へ続く帯のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-260-90h86v180h-86z" class="coral o"/>
  <path d="M-174-90h86v180h-86z" class="gold o"/>
  <path d="M-88-90h86v180h-86z" class="goldp o"/>
  <path d="M-2-90h86v180H-2z" class="green o"/>
  <path d="M84-90h86v180H84z" class="teal o"/>
  <path d="M170-90h90v180h-90z" class="violet o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="4" marker-end="url(#ar)"><path d="M40 350h520"/></g>
""", ground=False, arrow=True)

add('speculation', '確かな根拠なしに当て推量するイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-130h400v260h-400z" class="paper"/>
  <path d="M-160 60l50-30 40 20" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
  <path d="M-70 50q50-40 80-60t90-20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="12 10"/>
  <path d="M-160-100v190h330" class="a"/>
</g>
<g transform="translate(470 120)">
  <path d="M-26-26q0-28 28-28t28 26q0 22-28 28v12" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="36" r="7" class="coral"/>
</g>
{person(110,370,0.7,1,'teal','blue','think','short','neutral')}
""", ground=False)

add('spell', '杖をふって唱える呪文のイラスト。', f"""
{person(180,352,1.2,1,'violet','violet','reach','bun','neutral')}
<g transform="translate(300 210) rotate(30)">
  <path d="M-10-90h20v180h-20z" fill="{TONES['gold'][2]}"/>
  <circle cx="0" cy="-100" r="16" class="gold o"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="4" stroke-dasharray="10 9"><circle cx="430" cy="220" r="90"/></g>
<g class="golds"><path d="M430 100v-20M340 140l-20-20M520 140l20-20M430 340v20"/></g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2">
  <path d="M430 180l12 26 28 3-20 20 5 28-25-14-25 14 5-28-20-20 28-3z"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('sphere', 'まるい球のイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="150" class="tealp o"/>
  <path d="M0-150a150 150 0 0 1 0 300 90 150 0 0 0 0-300z" class="teal" opacity="0.5"/>
  <ellipse cx="-50" cy="-60" rx="40" ry="26" fill="#fffdf6" opacity="0.7" transform="rotate(-30 -50 -60)"/>
</g>
<ellipse cx="300" cy="376" rx="140" ry="24" fill="#c7d3c7" opacity="0.7"/>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('spice', '舌にぴりっとくる香辛料のイラスト。', f"""
<g transform="translate(230 250)">
  <path d="M0-90q20 40 10 90-10 50-50 60-40-10-30-70 10-56 70-80z" class="coral o"/>
  <path d="M0-90q-14-24 10-34 14 20 4 34z" class="greenp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M340 200q24 24 0 48M386 170q44 44 0 88M432 140q64 64 0 128"/>
</g>
<g transform="translate(500 300)">
  <path d="M-40-30h80l-8 60h-64z" class="goldp o"/>
  <path d="M-40-30h80v-14h-80z" class="goldd o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('spine', '背中を通る背骨のイラスト。', f"""
<g transform="translate(300 210)">
  <circle cx="0" cy="-140" r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-120 150v-110q0-90 120-90t120 90v110z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <g fill="#e7dfd0" stroke="{INK}" stroke-width="2.5">
    {''.join(f'<rect x="-20" y="{-90+i*26}" width="40" height="18" rx="7"/>' for i in range(9))}
  </g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M480 220h-140"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('spotlight', '一点を照らし出すスポットライトのイラスト。', f"""
<g transform="translate(120 110)">
  <path d="M-40-30h60v60h-60z" class="ink"/>
  <path d="M20-40l50-20v100L20 40z" class="gold o"/>
</g>
<path d="M190 60l290 280H200z" fill="{TONES['gold'][1]}" opacity="0.75"/>
{person(340,346,1.2,1,'coral','blue','up','short','smile')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('spouse', '指輪を交わした連れ合いのイラスト。', f"""
{person(220,352,1.2,1,'teal','blue','give','short','smile')}
{person(390,352,1.2,-1,'coral','gold','give','bob','smile')}
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="12">
  <circle cx="280" cy="180" r="38"/><circle cx="330" cy="180" r="38"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('squad', '少人数で組む分隊のイラスト。', f"""
{person(160,352,1.05,1,'green','green','stand','cap','neutral')}
{person(280,352,1.05,1,'green','green','stand','cap','neutral')}
{person(400,352,1.05,1,'green','green','stand','cap','neutral')}
{person(510,352,1.05,1,'green','green','stand','cap','neutral')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="100" y="200" width="470" height="170" rx="22"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('stance', '足を踏みしめて構える立場のイラスト。', f"""
{person(280,352,1.4,1,'teal','blue','point','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"><ellipse cx="280" cy="372" rx="110" ry="24"/></g>
<g transform="translate(490 260)">
  <path d="M-6 110V-70" class="a"/>
  <path d="M-6-70h80l-16 24 16 24H-6z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('steel', 'かたく丈夫な鋼のはりのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-70h440v40h-440zM-40-30h80v90h-80zM-220 60h440v40h-440z" fill="#b9c2c9" class="o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="6" opacity="0.8"><path d="M-180-60h380M-180 80h380"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"><path d="M120 130l30-30M180 120l24-24"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stereotype', '型に流しこんで同じ形にする固定観念のイラスト。', f"""
<g transform="translate(180 200)">
  <path d="M-80-70h160v140h-160z" class="goldd o"/>
  <path d="M-50-40h100v80h-100z" fill="#fffaf1" class="o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 200h50"/></g>
{person(420,352,0.9,1,'teal','blue','stand','short','neutral')}
{person(500,352,0.9,1,'teal','blue','stand','short','neutral')}
{person(570,352,0.9,1,'teal','blue','stand','short','neutral')}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('stock', '棚に積まれた在庫のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-230-140h460v280h-460z" fill="#fffdf6" class="o"/>
  <path d="M-230-50h460M-230 40h460" class="a"/>
</g>
{box(170,170,110,70,20,'gold')}
{box(310,170,110,70,20,'gold')}
{box(450,170,110,70,20,'gold')}
{box(170,262,110,70,20,'coral')}
{box(310,262,110,70,20,'coral')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('storage', '物をしまっておく倉庫のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-230 100v-180h460v180z" fill="#fffdf6" class="o"/>
  <path d="M-250-80L0-170l250 90z" class="teal o"/>
  <path d="M-120 100v-120h240v120z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">{''.join(f'<path d="M-120 {-20+i*30}h240"/>' for i in range(4))}</g>
</g>
{box(300,270,90,60,0,'gold')}
<path d="M60 356h480" class="a"/>
""", ground=True)

add('strand', '束からより分けた一本の糸のイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="8" stroke-linecap="round">
  <path d="M60 180q140-40 240 0t240 20M60 220q140-40 240 0t240 20M60 260q140-40 240 0t240 20"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round">
  <path d="M60 320q140-40 240 10t240 30"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M520 150l-80 150"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('stroke', '筆でひと息に引いた一画のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <path d="M-140-60q80 120 280 100" fill="none" stroke="{INK}" stroke-width="26" stroke-linecap="round"/>
</g>
<g transform="translate(490 320) rotate(28)">
  <path d="M-12-130h24v130l-12 40-12-40z" class="goldd o"/>
  <path d="M-12 0h24l-12 40z" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('structure', '内側の組み立てが分かる構造のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-170 110v-220h340v220z" fill="#fffdf6" class="o"/>
  <path d="M-190-110L0-190l190 80z" class="teal o"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="7">
    <path d="M-170-40h340M-170 30h340M-60-110v220M60-110v220"/>
  </g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8">
    <path d="M-170-110l340 220M170-110L-170 110"/>
  </g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('subscriber', '定期に届くものを受け取る購読者のイラスト。', f"""
{person(430,352,1.25,-1,'teal','blue','reach','bob','smile')}
<g transform="translate(210 250)">
  <path d="M-110-90h220v180h-220z" class="paper"/>
  <path d="M-110-90h220v50h-220z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-80-10h160M-80 20h160M-80 50h110"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M330 250h40"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M120 360h180M140 386h160"/></g>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('subscription', '毎月払って続ける定期購読のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-150h400v300h-400z" class="paper"/>
  <path d="M-200-150h400v50h-400z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-200 {-40+i*60}h400"/>' for i in range(4))}
    {''.join(f'<path d="M{-140+c*70} -100v250"/>' for c in range(5))}
  </g>
  <g class="coralp o">{''.join(f'<circle cx="{-170+c*70}" cy="{-70+r*60}" r="18"/>' for r in range(4) for c in range(1))}</g>
</g>
<g class="gold o"><ellipse cx="130" cy="140" rx="24" ry="10"/><ellipse cx="130" cy="200" rx="24" ry="10"/><ellipse cx="130" cy="260" rx="24" ry="10"/><ellipse cx="130" cy="320" rx="24" ry="10"/></g>
""", ground=False)

add('subsidy', '国が事業にお金を出して支える補助金のイラスト。', f"""
{building(150,300,0.8,'violet')}
{tower(470,320,0.65,'teal',4)}
<g transform="translate(300 220)">
  <path d="M-60-30h120v60h-120z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 150h130"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('substitute', '代わりに使う品のイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-70-70h140v140h-140z" fill="#dfe6ea" class="o"/>
  <circle r="40" fill="none" stroke="{MUTED}" stroke-width="10"/>
</g>
{xx(180,120,0.8,MUTED)}
<g class="a" marker-end="url(#ar)"><path d="M290 240h50"/></g>
<g transform="translate(440 240)">
  <path d="M-70-70h140v140h-140z" class="goldp o"/>
  <circle r="40" fill="none" stroke="{TONES['gold'][0]}" stroke-width="10"/>
</g>
{ck(440,120,0.9)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('substitution', '選手を入れかえる交代のイラスト。', f"""
{person(190,352,1.15,-1,'teal','blue','walk','short','sad')}
{person(410,352,1.15,1,'coral','gold','walk','bob','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="6" marker-end="url(#ar)"><path d="M240 180h120"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M360 240H240"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"><path d="M300 130v240"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('suburb', '町のはずれに広がる郊外の住宅地のイラスト。', f"""
{tower(100,300,0.55,'blue',5)}
{tower(180,300,0.5,'blue',4)}
<g transform="translate(330 300)">
  <path d="M-60 0v-60h120V0z" fill="#fffdf6" class="o"/>
  <path d="M-74-60L0-104l74 44z" class="coral o"/>
  <path d="M-16-40h32V0h-32z" class="corald o"/>
</g>
<g transform="translate(480 300)">
  <path d="M-60 0v-60h120V0z" fill="#fffdf6" class="o"/>
  <path d="M-74-60L0-104l74 44z" class="teal o"/>
  <path d="M-16-40h32V0h-32z" class="teald o"/>
</g>
{tree(400,300,0.7)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><path d="M250 140v210"/></g>
<path d="M60 320h480" class="a"/>
""", ground=True)

add('succession', '次から次へと続いて受け継ぐイラスト。', f"""
{person(130,352,0.95,1,'violet','violet','give','bun','smile')}
{person(280,352,0.95,1,'teal','blue','give','short','smile')}
{person(430,352,0.95,1,'coral','gold','give','bob','smile')}
{chair(540,356,1,'gold',1)}
<g class="a" marker-end="url(#ar)"><path d="M180 200h50M330 200h50M480 200h30"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('successor', '前任者のあとを引き受ける後継者のイラスト。', f"""
{person(140,352,1.15,1,'violet','violet','give','bun','smile')}
{person(470,352,1.15,-1,'teal','blue','reach','short','smile')}
{chair(300,356,1.1,'gold',1)}
<g class="a" marker-end="url(#ar)"><path d="M220 170h160"/></g>
{ck(470,190,0.9)}
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('suffering', '痛みに耐えて苦しんでいるイラスト。', f"""
{sit(300,352,1.35,1,'blue','blue','short','sad','down')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M210 200l-18-24M300 180v-28M390 200l18-24"/>
</g>
{cloud(300,90,1.4,'violet')}
{drop(266,240,1,'blue')}
{drop(334,246,1,'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('superiority', '一方が上に立つ優位のイラスト。', f"""
{person(200,250,1.25,1,'coral','blue','stand','short','neutral')}
<g transform="translate(200 260)">
  <path d="M-90-10h180v110h-180z" class="teal o"/>
</g>
{person(450,352,1,-1,'teal','gold','stand','bob','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M330 200v-60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('supervision', '作業をそばで見守る監督のイラスト。', f"""
{person(150,352,1.25,1,'violet','blue','point','bun','neutral')}
{person(380,356,0.9,1,'teal','blue','reach','short','neutral')}
{person(500,356,0.9,1,'gold','violet','reach','bob','neutral')}
{box(440,280,110,70,20,'gold')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M230 230h120"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('supervisor', '手帳を手に指示を出す監督者のイラスト。', f"""
{person(300,352,1.4,1,'violet','blue','carry','cap','neutral')}
<g transform="translate(410 270)">
  <path d="M-40-56h80v112h-80z" class="paper"/>
  <path d="M-40-56h80v20h-80z" class="ink"/>
  <g fill="none" stroke="{GRN}" stroke-width="5"><path d="M-24-16l8 10 18-22M-24 12l8 10 18-22"/></g>
</g>
<g transform="translate(220 250)">
  <circle r="26" class="gold o"/>
  <path d="M0-14l6 12 14 2-10 10 2 14-12-7-12 7 2-14-10-10 14-2z" class="goldd"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('supply', '荷を届けて必要な物をそろえる供給のイラスト。', f"""
<g transform="translate(190 280)">
  <path d="M-130 0v-60l40-50h130l40 50V0z" class="teal o"/>
  <g fill="#fffdf6" class="o"><rect x="-70" y="-100" width="60" height="40"/><rect x="0" y="-100" width="60" height="40"/></g>
  <g fill="{INK}"><circle cx="-70" cy="6" r="24"/><circle cx="70" cy="6" r="24"/></g>
</g>
{box(430,280,120,80,24,'gold')}
{box(430,180,90,60,18,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M320 300h50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('surface', '水の表面を示したイラスト。', f"""
<path d="M0 0h600v200H0z" fill="#e6f0fb"/>
<path d="M0 200h600v200H0z" class="bluep"/>
<path d="M0 200h600" fill="none" stroke="{INK}" stroke-width="5"/>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M60 260q40-16 80 0t80 0M340 300q40-16 80 0t80 0"/></g>
<g class="goldp o"><ellipse cx="240" cy="196" rx="50" ry="16"/></g>
<g class="teal o"><ellipse cx="420" cy="310" rx="46" ry="26"/><path d="M466 310l30-18v36z"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M120 120v60"/></g>
""", ground=False, arrow=True)

add('surgeon', 'マスクをして手術する外科医のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-200-30h400v30h-400z" class="teal o"/>
  <path d="M-200 0h400v16h-400z" class="teald o"/>
  <ellipse cx="-150" cy="-44" rx="26" ry="18" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-120-30h260v-20q0-12-14-12h-232q-14 0-14 12z" fill="#dfe6ea" class="o"/>
</g>
{person(300,270,1.15,1,'teal','teal','reach','cap','neutral')}
<g transform="translate(300 174)">
  <path d="M-24 0h48v20h-48z" fill="#dfe6ea" class="o"/>
</g>
<g transform="translate(390 240) rotate(40)">
  <path d="M-5-40h10v60h-10z" fill="#b9c2c9" class="o"/>
  <path d="M-5 20h10l-5 24z" fill="#b9c2c9" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
