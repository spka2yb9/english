"""第6回の描き直し（2周目）。batch06b.py のあとに実行する。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('fish', '川に釣り糸を垂らし、魚が針にかかっているイラスト。', f"""
<path d="M0 210h600v190H0z" class="bluep"/>
<path d="M0 210q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<path d="M110 50l180 130" fill="none" stroke="{TONES['gold'][2]}" stroke-width="8" stroke-linecap="round"/>
<path d="M290 180v96" fill="none" stroke="{MUTED}" stroke-width="2.5"/>
<path d="M290 276q20 12 0 24" fill="none" stroke="{INK}" stroke-width="4"/>
<g transform="translate(330 316)">
  <path d="M-46 0c26-40 90-40 116 0-26 40-90 40-116 0z" class="teal o"/>
  <path d="M-46 0l-36-26v52z" class="teal o"/>
  <path d="M20-18q14 18 0 36" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="44" cy="-6" r="3.6" class="ink"/>
  <path d="M-4-22q22-16 40-4" fill="none" stroke="{TONES['teal'][2]}" stroke-width="3"/>
</g>
<g class="blues" opacity=".7"><path d="M60 270q40-12 80 0M460 350q40-12 80 0"/></g>
""", ground=False)

add('bite', 'りんごの右上が一口かじり取られ、欠けたあとが残っているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(280 236)">
  <path d="M56-104a120 120 0 1 1-56 224 120 120 0 0 1 0-240q30 0 56 16a46 46 0 0 0 0 74 46 46 0 0 1 0-74z" class="coral o"/>
  <path d="M4-118v-24" class="a"/>
  <path d="M4-140c32-16 42-38 42-38-30-8-42 38-42 38z" class="green o"/>
  <path d="M-70-20q28-20 56-2" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
</g>
<path d="M470 174q-36 4-58 8" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('fire', '私物の箱を抱えて職場の扉から出ていく人と、空になった机のイラスト。', f"""
<path d="M420 60h180v300H420z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
<path d="M420 60h30v300h-30z" class="goldd o"/>
<circle cx="472" cy="220" r="10" class="goldd"/>
<g transform="translate(130 250)">
  <path d="M-100-14h200v16h-200z" class="goldp o"/>
  <path d="M-86 2v84M86 2v84" fill="none" stroke="{TONES['gold'][2]}" stroke-width="11" stroke-linecap="round"/>
  <path d="M-60-14h120" class="a"/>
</g>
{person(280,360,1.0,1,'coral','blue','stand','short','sad')}
<g transform="translate(360 260)">
  {box(0,0,96,66,0,'gold')}
  <path d="M-48 0h96" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
</g>
<path d="M304 292l40-24" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M420 320h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('bin', 'ふたを開けたごみ箱に、丸めた紙くずを投げ入れているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(300 306)">
  <path d="M-80-66h160l-16 136h-128z" class="tealp o"/>
  <path d="M-80-66h160" class="a"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3"><path d="M-56-36h112M-52 4h104M-46 44h92"/></g>
</g>
<g transform="translate(392 194) rotate(34)">
  <path d="M-90-11h180v22h-180z" class="teal o"/>
  <path d="M-8-11v-16h16v16z" class="a"/>
</g>
<g transform="translate(286 136)">
  <path d="M-34-6l-6-20 22-8 10-14 20 12 22-4 2 20 14 14-16 14 2 20-24-4-16 12-14-16-20-2z" fill="#fffdf6" stroke="{INK}" stroke-width="2.5"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2"><path d="M-14-18l12 10-6 14 14 6M18-22l-10 16 14 8"/></g>
</g>
<path d="M286 180v46" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('bind', 'ばらばらの棒を一束に集め、ひもを巻きつけて縛っているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="15" stroke-linecap="round">
  <path d="M70 130l160 76 300-46M74 300l156-58 306 20M60 216l170-10 320-6"/>
</g>
<g transform="translate(276 208)">
  <path d="M-34-58h68v116h-68z" class="coral o"/>
  <path d="M-34-30h68M-34 0h68M-34 30h68" fill="none" stroke="{TONES['coral'][2]}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M196 330q40-30 56-54"/><path d="M370 330q-40-30-56-54"/></g>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
