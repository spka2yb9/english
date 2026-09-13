"""第6回: 日常動作・身近なものの30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('blow', '強い風が吹きつけて、木の葉と帽子が飛ばされていくイラスト。', f"""
{tree(120,330,1.0)}
<g class="muted" style="stroke-dasharray:none" opacity=".9">
  <path d="M40 120q120-40 240 0t260-20" marker-end="url(#ar)"/>
  <path d="M60 190q120-40 240 0t250-20" marker-end="url(#ar)"/>
</g>
<g transform="translate(330 240) rotate(24)"><path d="M0 0c-26-20-22-50 6-50 22 0 34 16 34 32 0 16-18 30-40 18z" class="goldp o"/></g>
<g transform="translate(420 300) rotate(-30)"><path d="M0 0c-26-20-22-50 6-50 22 0 34 16 34 32 0 16-18 30-40 18z" class="gold o"/></g>
<g transform="translate(500 210) rotate(16)">
  <path d="M-40 0h80l-6-20h-68z" class="coral o"/>
  <path d="M-52 0h104v12h-104z" class="coralp o"/>
</g>
""", ground=True, arrow=True)

add('collect', 'ばらばらの切手を一冊のアルバムへ一枚ずつ集めているイラスト。', f"""
<circle cx="470" cy="100" r="56" class="tealp"/>
<g transform="translate(300 280)">
  <path d="M-140-50h280v110h-280z" class="tealp o"/>
  <path d="M0-50v110" class="a"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><rect x="-120" y="-30" width="46" height="34"/><rect x="-64" y="-30" width="46" height="34"/><rect x="20" y="-30" width="46" height="34"/><rect x="76" y="-30" width="46" height="34"/></g>
</g>
<g transform="translate(140 130) rotate(-16)"><rect x="-26" y="-20" width="52" height="40" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/><circle cy="0" r="9" class="coral o"/></g>
<g transform="translate(470 190) rotate(18)"><rect x="-26" y="-20" width="52" height="40" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/><circle cy="0" r="9" class="green o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M180 170q50 24 66 52"/><path d="M440 226q-50 8-72 26"/></g>
""", ground=True, arrow=True)

add('cycle', '自転車のペダルをこいで進んでいるイラスト。車輪の回転を矢印が示す。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(300 300)">
  <circle cx="-110" cy="0" r="62" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle cx="110" cy="0" r="62" fill="none" stroke="{INK}" stroke-width="9"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5"><path d="M-110-62v124M-172 0h124M110-62v124M48 0h124"/></g>
  <path d="M-110 0l60-70h80l80 70M-50-70l60 70M10 0h100" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linejoin="round"/>
  <circle cx="10" cy="0" r="18" fill="none" stroke="{TONES['gold'][2]}" stroke-width="7"/>
  <path d="M-50-70v-22h34" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M30-70l40-30h40" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
</g>
<path d="M300 190a120 120 0 0 1 90 40" class="muted" marker-end="url(#ar)"/>
<path d="M60 370h480" class="a"/>
""", ground=True, arrow=True)

add('fish', '川に釣り糸を垂らし、魚が針にかかっているイラスト。', f"""
<path d="M0 220h600v180H0z" class="bluep"/>
<path d="M0 220q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<path d="M120 60l180 130" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
<path d="M300 190v90" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
<path d="M300 280q18 10 0 22" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(360 300)">
  <path d="M0 0c-46-30-46-60 0-88 40 24 40 60 0 88z" class="teal o" transform="rotate(90)"/>
  <path d="M-44 0l-30-20 6 40z" class="teal o"/>
  <circle cx="20" cy="-8" r="3" class="ink"/>
</g>
<g class="blues" opacity=".7"><path d="M60 300q40-12 80 0M440 350q40-12 80 0"/></g>
""", ground=False)

add('pick', 'たくさんのりんごの中から、気に入った一つだけを指でつまみ上げるイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(280 320)">
  <path d="M-150-20h300l-16 60h-268z" class="goldp o"/>
  <g class="coral o"><circle cx="-100" cy="-30" r="26"/><circle cx="-40" cy="-26" r="26"/><circle cx="60" cy="-28" r="26"/><circle cx="118" cy="-24" r="26"/></g>
</g>
<g transform="translate(292 200)">
  <circle r="30" class="coral o"/>
  <path d="M0-30v-14" class="a"/>
  <path d="M-46-40q22-24 46-6" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
  <path d="M46-40q-22-24-46-6" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
</g>
<path d="M292 130V90" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('receive', '差し出された小包を、両手を出して受け取っているイラスト。', f"""
<circle cx="470" cy="96" r="56" class="tealp"/>
<path d="M0 226h96" fill="none" stroke="{TONES['coral'][0]}" stroke-width="28" stroke-linecap="round"/>
<path d="M88 226h40" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
{box(230,226,110,84,0,'gold')}
<path d="M230 184v84M175 226h110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
<path d="M310 180q40-16 70 0" class="a" marker-end="url(#ar)"/>
{person(430,336,1.05,-1,'green','blue','give','bob','smile')}
<circle cx="348" cy="224" r="14" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
""", ground=True, arrow=True)

add('ship', '荷物を積んだ大きな船が、海の上を進んでいるイラスト。', f"""
<path d="M0 260h600v140H0z" class="bluep"/>
<path d="M0 260q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(300 236)">
  <path d="M-190 0h380l-40 58h-300z" class="teal o"/>
  <path d="M-190 0h380" class="a"/>
  <path d="M-120 0v-56h150v56z" class="paper"/>
  <g class="goldp o"><rect x="-100" y="-46" width="40" height="40"/><rect x="-50" y="-46" width="40" height="40"/><rect x="-100" y="-96" width="40" height="40"/></g>
  <path d="M60 0v-70h80v70z" fill="#fffdf6" class="o"/>
  <g class="bluep o"><rect x="76" y="-56" width="22" height="20"/><rect x="106" y="-56" width="22" height="20"/></g>
  <path d="M100-70v-30" class="a"/>
</g>
<g class="blues" opacity=".7"><path d="M60 330q50-14 100 0t100 0M340 360q50-14 100 0t100 0"/></g>
""", ground=False)

add('smile', '口の両端が上がった笑顔の顔を、大きく描いたイラスト。', f"""
<circle cx="300" cy="200" r="140" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
<path d="M-70-30q22-22 44 0" transform="translate(300 200)" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
<path d="M26-30q22-22 44 0" transform="translate(300 200)" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
<path d="M-64 30q64 78 128 0" transform="translate(300 200)" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="180" cy="240" r="20" class="coralp"/><circle cx="420" cy="240" r="20" class="coralp"/>
<g class="a" marker-end="url(#ar)"><path d="M196 300q-16 20-16 40"/><path d="M404 300q16 20 16 40"/></g>
""", ground=False, arrow=True)

add('train', 'ホームに止まった列車が、線路の上を走り出そうとしているイラスト。', f"""
<path d="M0 330h600v70H0z" fill="#d8d3ca"/>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M0 340h600M0 360h600"/></g>
<g fill="{TONES['gold'][2]}"><rect x="40" y="344" width="14" height="14"/><rect x="140" y="344" width="14" height="14"/><rect x="240" y="344" width="14" height="14"/><rect x="340" y="344" width="14" height="14"/><rect x="440" y="344" width="14" height="14"/><rect x="540" y="344" width="14" height="14"/></g>
<g transform="translate(320 250)">
  <path d="M-250-90h430q34 0 34 34v106h-464z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-250-90v140" class="a"/>
  <g class="bluep o"><rect x="-220" y="-62" width="70" height="54"/><rect x="-130" y="-62" width="70" height="54"/><rect x="-40" y="-62" width="70" height="54"/><rect x="50" y="-62" width="70" height="54"/><rect x="140" y="-62" width="60" height="54"/></g>
  <path d="M-250 30h464" class="a"/>
  <path d="M-250 30h464v20h-464z" class="coral"/>
  <circle cx="-170" cy="72" r="20" class="ink"/><circle cx="-90" cy="72" r="20" class="ink"/><circle cx="110" cy="72" r="20" class="ink"/><circle cx="190" cy="72" r="20" class="ink"/>
</g>
<path d="M540 200h50" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('wind', '風が旗を横へなびかせ、木の枝をしならせているイラスト。', f"""
{tree(500,340,0.9)}
<path d="M140 380V80" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
<path d="M148 96q70-30 120 10-50 40-120 14z" class="coral o"/>
<path d="M148 160q60-26 104 8-44 34-104 12z" class="coralp o"/>
<g class="muted" opacity=".9">
  <path d="M60 240q140-40 240 0t250-20" marker-end="url(#ar)"/>
  <path d="M40 296q140-40 240 0t250-20" marker-end="url(#ar)"/>
</g>
""", ground=True, arrow=True)

add('bake', 'オーブンの中でパンがふくらみ、焼き上がっているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(280 250)">
  <path d="M-150-110h300v220h-300z" fill="#dfe6ea" class="o"/>
  <path d="M-120-80h240v130h-240z" fill="#3d4c5c"/>
  <path d="M-110-70h220v110h-220z" class="goldp" opacity=".35"/>
  <g transform="translate(0 6)">
    <path d="M-70 30q-16-70 70-70t70 70z" class="gold o"/>
    <path d="M-40-16q20-16 40 0M10-24q20-14 40 4" fill="none" stroke="{TONES['gold'][2]}" stroke-width="3"/>
  </g>
  <path d="M-140 70h280" class="a"/>
  <path d="M-40 86h80v12h-80z" class="ink"/>
</g>
<g class="corals" opacity=".85"><path d="M400 200q20-30 0-60M440 210q24-36 0-72"/></g>
""", ground=True)

add('bite', '大きなりんごに歯を立てて、一口かじり取ったあとが残っているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(280 220)">
  <path d="M0-110c90 0 130 60 130 110s-58 110-130 110S-130 250-130 110 -90-110 0-110z" class="coral o"/>
  <path d="M130 60a60 60 0 0 1 0 100 66 66 0 0 0 0-100z" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
  <path d="M0-110v-30" class="a"/>
  <path d="M0-134c34-16 44-38 44-38-32-8-44 38-44 38z" class="green o"/>
  <path d="M-60-40q30-20 60 0" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M470 200q-40 20-64 30"/></g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><rect x="470" y="150" width="24" height="30" rx="6"/><rect x="500" y="150" width="24" height="30" rx="6"/></g>
""", ground=True, arrow=True)

add('divide', '一枚のケーキに切れ目を入れて、四つに分けているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
<g transform="translate(290 230)">
  <ellipse cy="20" rx="150" ry="46" class="goldp o"/>
  <path d="M-150 20v-30a150 46 0 0 1 300 0v30" fill="#fff4d8" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="-10" rx="150" ry="46" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="-10" rx="120" ry="34" class="coralp o"/>
  <path d="M-150-10h300M0-56v92" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 330q-30-20-40-46"/><path d="M460 330q30-20 40-46"/></g>
""", ground=True, arrow=True)

add('feed', '皿にえさを入れて、犬に食べさせているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="greenp"/>
<g transform="translate(400 320)">
  <ellipse rx="66" ry="20" class="bluep o"/>
  <path d="M-66 0q10 26 66 26t66-26" fill="none" class="a"/>
  <g class="goldd o"><circle cx="-24" cy="-6" r="12"/><circle cx="4" cy="-10" r="12"/><circle cx="30" cy="-4" r="12"/></g>
</g>
<g transform="translate(220 260)">
  <ellipse cx="0" cy="30" rx="76" ry="46" class="goldp o"/>
  <path d="M-60 66v20M-20 70v16M30 70v16M64 62v24" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-76 20q-40 10-40 40" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
  <g transform="translate(80 -10)">
    <ellipse rx="40" ry="34" class="goldp o"/>
    <path d="M20 20q26 8 40-4" fill="none" class="a"/>
    <path d="M-20-30q-14-30 10-24" class="goldd o"/>
    <circle cx="14" cy="-8" r="3" class="ink"/>
    <circle cx="44" cy="12" r="5" class="ink"/>
  </g>
</g>
<path d="M330 260q30 20 34 40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('fire', '私物の入った箱を持って職場から出ていく人と、空いた机のイラスト。', f"""
<g transform="translate(160 270)">
  <path d="M-110-10h220v14h-220z" class="goldp o"/>
  <path d="M-96 4v66M96 4v66" fill="none" stroke="{TONES['gold'][2]}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-70-10h140" class="a"/>
</g>
{box(410,214,96,72,0,'gold')}
<path d="M362 214h96" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
<path d="M362 266l-30 30M458 266l30 30" fill="none" stroke="{SKIN}" stroke-width="18" stroke-linecap="round"/>
{person(410,376,1.0,1,'coral','blue','stand','short','sad')}
<path d="M500 300h70" class="a" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:8"><path d="M140 190l50 50M190 190l-50 50"/></g>
""", ground=True, arrow=True)

add('hand', '書類を相手の手に直接わたしているイラスト。', f"""
<circle cx="300" cy="110" r="72" class="tealp"/>
<path d="M0 250h110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="28" stroke-linecap="round"/>
<path d="M100 250h48" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
<path d="M600 250H490" fill="none" stroke="{TONES['teal'][0]}" stroke-width="28" stroke-linecap="round"/>
<path d="M500 250h-48" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
<g transform="translate(300 236) rotate(-6)">
  <path d="M-70-56h140v112h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-30h92M-46-8h92M-46 14h60"/></g>
</g>
<path d="M170 180h120" class="a" marker-end="url(#ar)"/>
<circle cx="180" cy="250" r="14" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<circle cx="424" cy="250" r="14" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
""", ground=True, arrow=True)

add('pour', 'ポットを傾けて、カップへ飲み物を注ぎ込んでいるイラスト。', f"""
<circle cx="130" cy="100" r="56" class="goldp"/>
<g transform="translate(220 170) rotate(38)">
  <path d="M-70-60h140l-16 120h-108z" fill="#fffdf6" class="o"/>
  <path d="M-70-60h140" class="a"/>
  <path d="M70-40q42 0 42 28t-42 28" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-70-50l-34-16 6 26z" fill="#fffdf6" class="o"/>
</g>
<path d="M266 230q26 40 30 76" fill="none" stroke="{TONES['gold'][2]}" stroke-width="16" stroke-linecap="round"/>
<path d="M266 230q26 40 30 76" fill="none" stroke="{TONES['gold'][1]}" stroke-width="6" stroke-linecap="round"/>
<g transform="translate(300 330)">
  <path d="M-64-30h128l-14 60h-100z" fill="#fffdf6" class="o"/>
  <path d="M-56-6h112l-8 36h-96z" class="goldp o"/>
  <path d="M-64-30h128" class="a"/>
  <path d="M64-16q34 0 34 22t-34 22" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
""", ground=True)

add('remove', '積んだ皿の一枚を取り出して、外へ出しているイラスト。抜けたあとが点線で残る。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(230 300)">
  <g class="bluep o"><ellipse cy="0" rx="90" ry="22"/><ellipse cy="-30" rx="90" ry="22"/><ellipse cy="-90" rx="90" ry="22"/></g>
  <ellipse cy="-60" rx="90" ry="22" class="muted"/>
</g>
<g transform="translate(450 200)">
  <ellipse rx="90" ry="22" class="blue o"/>
</g>
<path d="M330 250q50-30 70-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('shine', '磨かれた金属のポットが、光を反射してきらりと輝いているイラスト。', f"""
{sun(110,96,44)}
<g transform="translate(320 250)">
  <ellipse cy="86" rx="90" ry="20" class="ground"/>
  <path d="M-80-70h160l-14 156h-132z" fill="#e7eef4" class="o"/>
  <path d="M-80-70h160" class="a"/>
  <path d="M-44-56h26l-10 130h-24z" fill="#ffffff" opacity=".9"/>
  <path d="M80-46q46 0 46 40t-46 40" fill="none" stroke="{INK}" stroke-width="10"/>
</g>
<g class="golds" style="stroke-width:5">
  <path d="M180 120l-40-30M420 130l44-34M186 210h-56M456 216h56M300 60V20"/>
</g>
""", ground=True)

add('shut', '開いていた扉が押されて、ぴたりと閉じるイラスト。', f"""
<path d="M60 40h230v340H60z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
<path d="M290 60v300l120-40V100z" class="goldp o"/>
<path d="M290 140l120-14M290 280l120-12" fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"/>
<circle cx="302" cy="210" r="10" class="goldd"/>
<path d="M480 210h-60" class="a" marker-end="url(#ar)"/>
<path d="M300 60h230v300H300z" class="muted"/>
""", ground=True, arrow=True)

add('soft', '指で押すと深くくぼむ、柔らかいクッションのイラスト。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
<g transform="translate(280 280)">
  <path d="M-140-60q140-30 280 0 30 60 0 120-140 30-280 0-30-60 0-120z" class="violetp o"/>
  <path d="M-40-58q40 50 0 96" fill="none" stroke="{TONES['violet'][0]}" stroke-width="3"/>
  <path d="M-70-46q80 20 160 0" fill="none" stroke="{TONES['violet'][0]}" stroke-width="3"/>
  <path d="M0-40q-56 20-30 54 20 26 60 4 30-20 0-54-14-14-30-4z" fill="{TONES['violet'][1]}" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(280 150)">
  <path d="M-22-40h44v70a22 22 0 0 1-44 0z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-22-40q-54 0-54-24h98v24z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M170 220v50"/><path d="M394 220v50"/></g>
""", ground=True, arrow=True)

add('store', '棚に品物を並べた小さな店のイラスト。看板と入口が見える。', f"""
<g transform="translate(300 250)">
  <path d="M-190 130V-60h380v190z" fill="#fffdf6" class="o"/>
  <path d="M-206-60h412l-40-50h-332z" class="teal o"/>
  <path d="M-140-40h130v60h-130z" class="bluep o"/>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="3"><path d="M-140-20h130M-140 0h130"/></g>
  <g class="coral o"><circle cx="-116" cy="-30" r="8"/><circle cx="-90" cy="-30" r="8"/><circle cx="-64" cy="-30" r="8"/></g>
  <g class="goldp o"><rect x="-116" y="-14" width="22" height="14"/><rect x="-86" y="-14" width="22" height="14"/></g>
  <path d="M40-40h120v170H40z" class="goldp o"/>
  <path d="M100-40v170" class="a"/>
  <path d="M-30 130V50h60v80z" class="tealp o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('water', 'じょうろで花に水をやっているイラスト。水が細く注がれている。', f"""
<circle cx="480" cy="96" r="54" class="bluep"/>
<g transform="translate(170 200) rotate(24)">
  <path d="M-60-40h120l-10 96h-100z" class="tealp o"/>
  <path d="M60-30h70l16-16-90-6z" class="teal o"/>
  <path d="M-60-56q60-16 120 0" fill="none" stroke="{INK}" stroke-width="6"/>
  <path d="M-60-30q-40 10-30 50" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<g stroke-linecap="round" fill="none">
  <path d="M296 178q30 40 34 90" stroke="{TONES['blue'][0]}" stroke-width="10"/>
  <path d="M312 176q30 44 34 92" stroke="{TONES['blue'][0]}" stroke-width="6"/>
</g>
<g transform="translate(390 330)">
  <path d="M0 0v-90" fill="none" stroke="{TONES['green'][2]}" stroke-width="8" stroke-linecap="round"/>
  <path d="M0-40c-40-10-52-34-52-34 36-10 52 34 52 34z" class="green o"/>
  <circle cx="0" cy="-106" r="24" class="coral o"/>
  <g class="coralp o"><circle cx="-26" cy="-124" r="16"/><circle cx="26" cy="-124" r="16"/><circle cx="0" cy="-140" r="16"/><circle cx="-24" cy="-90" r="16"/><circle cx="24" cy="-90" r="16"/></g>
  <circle cx="0" cy="-114" r="14" class="gold o"/>
</g>
""", ground=True)

add('wooden', '木目の見える木製のいすを描いたイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(280 240)">
  <path d="M-90-120h20v130h-20zM70-120h20v130h-20z" class="goldd o"/>
  <path d="M-90-96h180v22h-180zM-90-52h180v22h-180z" class="goldp o"/>
  <path d="M-104 10h208v24h-208z" class="gold o"/>
  <path d="M-90 34v100h20V34zM70 34v100h20V34z" class="goldd o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="2.5" opacity=".8">
    <path d="M-80-90h160M-80-64h160M-80-46h160M-96 20h190"/>
  </g>
</g>
<path d="M60 380h440" class="a"/>
""", ground=True)

add('ankle', '足首の位置を示した脚のイラスト。関節の部分に印がついている。', f"""
<circle cx="450" cy="110" r="66" class="coralp"/>
<g transform="translate(280 210)">
  <path d="M-30-160h60v210h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30 50h60v40h-60z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30 90h60q60 0 60 40h-140q-20 0-20-20z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <circle cx="0" cy="70" r="34" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"/>
</g>
<path d="M420 240q-60 30-96 40" class="a" marker-end="url(#ar)"/>
<path d="M120 380h360" class="a"/>
""", ground=True, arrow=True)

add('applaud', '観客が手のひらを打ち合わせて拍手しているイラスト。', f"""
<circle cx="300" cy="130" r="96" class="goldp"/>
{person(160,336,1.0,1,'teal','blue','hold','short','smile')}
{person(300,336,1.05,1,'coral','gold','hold','bob','smile')}
{person(440,336,1.0,1,'violet','teal','hold','cap','smile')}
<g class="golds" opacity=".9" style="stroke-width:4">
  <path d="M120 200q-20-20-16-40M180 190q0-24 10-40M266 186q-16-22-12-42M330 180q4-24 14-40M410 196q-18-20-14-40M470 190q2-24 12-40"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('assemble', 'ばらばらの部品を集めて、一つの形に組み立てているイラスト。', f"""
<circle cx="300" cy="200" r="130" class="tealp"/>
<g transform="translate(300 210)">
  <path d="M-60-60h120v120h-120z" fill="#fffdf6" class="o"/>
  <path d="M-60-60h60v60h-60z" class="teal o"/>
  <path d="M0 0h60v60H0z" class="gold o"/>
</g>
<g transform="translate(110 110)"><path d="M-30-30h60v60h-60z" class="teal o"/></g>
<g transform="translate(500 300)"><path d="M-30-30h60v60h-60z" class="gold o"/></g>
<g transform="translate(120 320)"><path d="M-30-30h60v60h-60z" class="coral o"/></g>
<g class="a" marker-end="url(#ar)">
  <path d="M156 146q40 24 60 40"/><path d="M452 286q-40-14-64-24"/><path d="M164 300q40-16 64-24"/>
</g>
""", ground=False, arrow=True)

add('bin', 'ふたの開いたごみ箱に、丸めた紙を捨て入れているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(300 300)">
  <path d="M-80-70h160l-16 140h-128z" class="tealp o"/>
  <path d="M-80-70h160" class="a"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-56-40h112M-52 0h104M-46 40h92"/></g>
  <g transform="translate(60 -100) rotate(28)">
    <path d="M-90-12h180v20h-180z" class="tealp o"/>
    <path d="M-10-12v-14h20v14z" class="a"/>
  </g>
</g>
<circle cx="300" cy="130" r="26" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
<path d="M286 118q14 14 28 0M290 142q16-10 22-22" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
<path d="M300 170v46" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('bind', 'ばらばらの棒をひもでぐるぐる巻いて、一束に縛っているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="16" stroke-linecap="round">
  <path d="M140 120h320M136 180h330M144 240h316M150 300h300"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="12" stroke-linecap="round">
  <path d="M240 96q-40 116 0 232M260 96q40 116 0 232"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M200 350q30-20 40-40"/><path d="M300 350q-20-20-26-40"/></g>
""", ground=True, arrow=True)

add('bury', 'スコップで土をかけて、箱を地面の下に埋めているイラスト。', f"""
<path d="M0 230h600v170H0z" fill="#e7d9c4"/>
<path d="M0 230h600" class="a"/>
<g transform="translate(250 320)">{box(0,0,120,80,0,'gold')}</g>
<path d="M150 230q40-40 100-40t100 40q-30 30-100 30t-100-30z" fill="#d3bb96" stroke="{INK}" stroke-width="2.5"/>
<g transform="translate(430 200) rotate(-26)">
  <path d="M-7-120h14v96h-14z" class="goldd"/>
  <path d="M-30-26h60l-10 54h-40z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 170q-30 30-40 50"/></g>
<g fill="#c9a97c"><circle cx="356" cy="196" r="6"/><circle cx="336" cy="216" r="5"/><circle cx="372" cy="222" r="4"/></g>
""", ground=False, arrow=True)
print(' '.join(W)); print(sheet(W))
