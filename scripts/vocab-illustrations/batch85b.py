"""第85回の描き直し: lap / loop / legend / kidney。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('lap', 'いすに座ったひざの上に本をのせたイラスト。', f"""
<g transform="translate(300 350)">
  <path d="M-100-20h40v20h-40z" class="goldd o"/>
  <path d="M-96 0v36M-24 0v36M56 0v36" class="a"/>
  <path d="M-100-20v-150h30v150z" class="gold o"/>
  <path d="M-70-40h130v20H-70z" class="goldd o"/>
</g>
{sit(300,350,1.5,1,'teal','blue','short','smile','lap')}
<g transform="translate(326 288)">
  <path d="M-56-14h112v34h-112z" class="paper"/>
  <path d="M0-14v34M-56-14q56-16 112 0" class="a"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"><ellipse cx="324" cy="298" rx="74" ry="38"/></g>
<path d="M500 298h-90" class="a" marker-end="url(#ar)"/>
<path d="M60 390h480" class="a"/>
""", ground=True, arrow=True)

add('loop', 'ぐるりと回ってもとに戻り、くり返す輪のイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="24" stroke-linecap="round">
  <path d="M300 90a130 130 0 1 1-92 38"/>
</g>
<g fill="none" stroke="{TONES['teal'][1]}" stroke-width="8">
  <path d="M300 90a130 130 0 1 1-92 38"/>
</g>
<path d="M300 46l64 44-64 44z" fill="{TONES['teal'][2]}" stroke="{INK}" stroke-width="3"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('legend', 'たき火を囲んで語り継がれる伝説のイラスト。', f"""
<g transform="translate(300 160)">
  <path d="M-190-100q-28 0-28 26t28 26h380q28 0 28-26t-28-26z" class="goldp o"/>
  <path d="M-190-48h380v96h-380z" fill="#fdf6e3" class="o"/>
  <path d="M-140 30l60-60 40 34 34-30 46 56z" class="greenp o"/>
  <path d="M120-16l10 22 24 3-17 17 4 24-21-12-21 12 4-24-17-17 24-3z" class="gold o"/>
</g>
{flame(300,330,0.8)}
{sit(150,340,0.75,1,'teal','blue','short','smile','down')}
{sit(450,340,0.75,-1,'coral','gold','bob','smile','down')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('kidney', '背中側に左右ひとつずつある腎臓のイラスト。', f"""
<g transform="translate(300 210)">
  <circle cx="0" cy="-140" r="40" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-130 150v-110q0-90 130-90t130 90v110z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-80-40q-44 0-44 50t40 60q34 0 34-34t-20-38 20-14-30-24z" class="coral o"/>
  <path d="M80-40q44 0 44 50t-40 60q-34 0-34-34t20-38-20-14 30-24z" class="coral o"/>
  <path d="M-46 20q30 30 46 60M46 20q-30 30-46 60" fill="none" stroke="{TONES['coral'][2]}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-6 80h12v60h-12z" class="corald o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
