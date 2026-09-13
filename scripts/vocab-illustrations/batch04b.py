"""第4回の描き直し分。batch04.py のあとに実行する（こちらが最終版）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('climb', '急な岩場に手と足をかけて、上へよじ登っていく人のイラスト。', f"""
<circle cx="110" cy="90" r="54" class="goldp"/>
<path d="M250 400V70q0-30 60-30h290v360z" fill="#e7dcc9" stroke="{INK}" stroke-width="3"/>
<g fill="#c9b799" stroke="{INK}" stroke-width="2"><circle cx="330" cy="120" r="11"/><circle cx="460" cy="90" r="10"/><circle cx="420" cy="210" r="11"/><circle cx="330" cy="270" r="10"/><circle cx="500" cy="300" r="11"/></g>
<g transform="translate(378 268)">
  <path d="M-24-70q24-12 48 0l-8 68h-32z" class="coral o"/>
  <path d="M-22-62l-44-46M22-62l40-70" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-12-4l-34 22M12-4l26 30" fill="none" stroke="{TONES['blue'][2]}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="0" cy="-100" r="22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-23-108q8-24 27-20 18 3 21 21z" fill="{TONES['blue'][0]}"/>
  <circle cx="6" cy="-96" r="2.2" class="ink"/>
</g>
<path d="M180 300q-14-90 34-160" class="muted" marker-end="url(#ar)"/>
""", arrow=True)

add('crawl', '赤ちゃんが両手と両ひざを床につけて、ゆっくり前へはっていくイラスト。', f"""
<circle cx="480" cy="120" r="66" class="violetp"/>
<g transform="translate(300 292)">
  <ellipse cx="0" cy="-34" rx="86" ry="46" class="coral o"/>
  <path d="M-58-6q-6 30 10 34 18 4 16-26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M46-6q-6 30 10 34 18 4 16-26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-86-40q-34 6-34 34 0 20 20 20 16 0 18-22" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <circle cx="-112" cy="-72" r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-146-88q6-30 34-30 26 0 30 28-16-10-34-2-12-8-30 4z" fill="{HAIR}"/>
  <circle cx="-124" cy="-66" r="3" class="ink"/><circle cx="-104" cy="-66" r="3" class="ink"/>
  <path d="M-122-52q10 8 20 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="-136" cy="-52" r="7" class="coralp"/>
</g>
<path d="M140 240q-44 12-58 40" class="muted" marker-end="url(#ar)"/>
<path d="M110 340h420" class="a"/>
""", arrow=True)

add('hang', 'ドアのそばのフックに、コートを掛けてぶら下げているイラスト。', f"""
<path d="M40 40h170v340H40z" fill="#e7dcc9" stroke="{INK}" stroke-width="3"/>
<circle cx="182" cy="220" r="11" class="goldd"/>
<g transform="translate(390 120)">
  <path d="M-4-34a14 14 0 1 1 8 0v20" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-96 22h192L0-14z" fill="none" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
  <path d="M-70 18q30-16 70-16t70 16l40 60-30 20-16-24v150H-64V74l-16 24-30-20z" class="coral o"/>
  <path d="M0 8v190" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
  <path d="M-30 4L0 30l30-26" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
</g>
<path d="M270 110q-38 6-70 96" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('dig', 'シャベルで地面に穴を掘り、掘り出した土が横に積まれているイラスト。', f"""
<circle cx="110" cy="96" r="54" class="greenp"/>
<path d="M0 236h600v164H0z" fill="#e7d9c4"/>
<path d="M0 236h600" class="a"/>
<path d="M216 236q16 90 84 90t84-90z" fill="#8e7350" stroke="{INK}" stroke-width="3"/>
<path d="M232 250q22 62 68 62t68-62z" fill="#6d573b"/>
<path d="M430 236q34-58 82 0z" fill="#d3bb96" stroke="{INK}" stroke-width="2.5"/>
<path d="M446 236q26-34 50 0" fill="none" stroke="#b79f7c" stroke-width="2.5"/>
<g transform="translate(300 220) rotate(22)">
  <path d="M-7-140h14v112h-14z" class="goldd"/>
  <path d="M-30-30h60l-10 58h-40z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M-14-152h28v14h-28z" class="ink"/>
</g>
<path d="M180 190q40 34 44 74" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('mix', 'ボウルの中で白と赤の材料が、スプーンでかき混ぜられて一つになっていくイラスト。', f"""
<circle cx="480" cy="104" r="54" class="coralp"/>
<g transform="translate(280 220)">
  <path d="M-124-20h248q-16 130-124 130T-124-20z" fill="#fffdf6" class="o"/>
  <path d="M-124-20h248" class="a"/>
  <path d="M-108 6q46 24 108 8t100-14q-18 90-104 90T-108 6z" class="coralp o"/>
  <path d="M-60 30q34 44 90 12" fill="none" stroke="#ffffff" stroke-width="9" stroke-linecap="round"/>
  <path d="M-20 20L84-104" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
  <ellipse cx="-26" cy="26" rx="26" ry="12" fill="#f0dfc2" stroke="{INK}" stroke-width="2.5" transform="rotate(-46 -26 26)"/>
</g>
<path d="M160 168a124 54 0 0 0 232 0" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('weigh', 'はかりに載せた果物の重さを、目盛りの針が指し示しているイラスト。', f"""
<circle cx="110" cy="110" r="56" class="tealp"/>
<g transform="translate(300 306)">
  <path d="M-124-26h248v66h-248z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <circle cx="0" cy="8" r="34" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M0 8l22-18" class="a"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2.5"><path d="M-24-14l-6-6M24-14l6-6M0-24v-8"/></g>
  <path d="M-146-36h292l-12-16h-268z" class="tealp o"/>
</g>
<g transform="translate(300 240)">
  <path d="M-74 0h148l-12 22h-124z" class="paper"/>
  <circle cx="-30" cy="-24" r="24" class="coral o"/>
  <circle cx="22" cy="-18" r="28" class="green o"/>
</g>
""", ground=True)

add('bridge', '川の両岸をつなぐ橋を、人が渡っているイラスト。', f"""
<path d="M0 240h600v160H0z" class="bluep"/>
<path d="M0 240h150v160H0zM450 240h150v160H450z" class="ground"/>
<path d="M0 240h150M450 240h150" class="a"/>
<g class="blues" opacity=".7"><path d="M190 300q50-14 100 0t100 0"/><path d="M200 350q50-14 100 0t100 0"/></g>
<path d="M90 200h420" fill="none" stroke="{TONES['gold'][2]}" stroke-width="15" stroke-linecap="round"/>
<path d="M130 208v34M300 208v34M470 208v34" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8"/>
<path d="M90 168q106-44 210-44t210 44" fill="none" stroke="{TONES['gold'][0]}" stroke-width="7"/>
<path d="M130 176v20M210 168v28M300 164v32M390 168v28M470 176v20" fill="none" stroke="{TONES['gold'][0]}" stroke-width="4"/>
{person(300,192,0.6,1,'coral','blue','walk','short','smile')}
""", ground=False)

add('nest', '木の枝の上に組まれた深い巣の中で、卵とひなが守られているイラスト。', f"""
<circle cx="120" cy="110" r="58" class="greenp"/>
<path d="M0 330q160-40 300-30t300 20" fill="none" stroke="{TONES['gold'][2]}" stroke-width="14" stroke-linecap="round"/>
<g transform="translate(300 250)">
  <path d="M-116 0q0 80 116 80T116 0q-40-26-116-26T-116 0z" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3">
    <path d="M-108 14q108-30 216 0M-96 40q96-26 192 0M-76 62q76-20 152 0"/>
  </g>
  <ellipse cx="-40" cy="-14" rx="26" ry="21" fill="#fffdf6" class="o"/>
  <ellipse cx="14" cy="-10" rx="26" ry="21" fill="#fffdf6" class="o"/>
  <g transform="translate(66 -34)">
    <circle r="24" class="gold o"/>
    <path d="M20-6l24-8-16 20z" class="gold o"/>
    <circle cx="8" cy="-8" r="3" class="ink"/>
    <path d="M0-24v-14" class="a"/>
  </g>
</g>
""", ground=True)

add('whisper', '手を口元に添えて、隣の人の耳もとに小さな声で話しかけているイラスト。', f"""
<circle cx="480" cy="116" r="58" class="violetp"/>
{person(230,336,1.05,1,'teal','blue','point','short','neutral')}
{person(392,336,1.05,-1,'violet','gold','stand','bob','smile')}
<circle cx="298" cy="226" r="15" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<g transform="translate(330 190)">
  <path d="M-34-24h68q12 0 12 12v22q0 12-12 12h-52l-18 16 4-16h-2q-12 0-12-12v-22q0-12 12-12z" class="paper"/>
  <g fill="{MUTED}"><circle cx="-16" cy="0" r="3"/><circle cx="0" cy="0" r="3"/><circle cx="16" cy="0" r="3"/></g>
</g>
<path d="M372 214q12 8 12 18" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
