"""第89回の描き直し: pill / predator / prey / plea / predecessor / presence。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('pill', '飲みこむ錠剤とカプセルのイラスト。', f"""
<g transform="translate(230 210)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <circle r="70" class="coralp"/>
  <path d="M0-88v176" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g transform="translate(430 260) rotate(-24)">
  <path d="M-100-40h100v80h-100q-40 0-40-40t40-40z" class="coral o"/>
  <path d="M0-40h60q40 0 40 40t-40 40H0z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(480 130)">
  <path d="M-40 40v-70q0-14 14-16v-14h52v14q14 2 14 16v70z" fill="#fffdf6" class="o"/>
  <path d="M-40 40V4q40-10 80 0v36z" class="goldp o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('predator', '獲物を追いかける捕食者のイラスト。', f"""
{beast(210,300,0.95,'#6b5a4a',1)}
<g transform="translate(500 330)">
  <ellipse rx="40" ry="26" fill="#b9a98f" class="o"/>
  <circle cx="34" cy="-18" r="18" fill="#b9a98f" class="o"/>
  <path d="M50-24l22 8-22 10z" class="corald o"/>
  <circle cx="40" cy="-24" r="4" class="ink"/>
  <path d="M-24 26v22M14 28v20" fill="none" stroke="#8a7a63" stroke-width="8" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M390 230h60"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('prey', '追われる側の獲物のイラスト。', f"""
{beast(170,290,0.75,'#4a4038',1)}
<g transform="translate(450 320)">
  <ellipse rx="56" ry="38" fill="#b9a98f" class="o"/>
  <circle cx="48" cy="-28" r="26" fill="#b9a98f" class="o"/>
  <path d="M70-36l28 10-28 12z" class="corald o"/>
  <circle cx="56" cy="-36" r="5" class="ink"/>
  <path d="M-36 38v32M18 40v30" fill="none" stroke="#8a7a63" stroke-width="10" stroke-linecap="round"/>
  <path d="M28-50q-6-32 16-38-4 22 4 38z" fill="#b9a98f" class="o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M300 240h80"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><ellipse cx="462" cy="290" rx="120" ry="94"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('plea', 'ひざをついて必死に願うイラスト。', f"""
<g transform="translate(280 350)">
  <path d="M-60 0h100v-16h-100z" fill="{TONES['blue'][2]}" class="o"/>
  <path d="M-30-16h30v-40h-30z" fill="{TONES['blue'][2]}" class="o"/>
  <path d="M-34-56q34-16 68 0l-10 46h-48z" class="coral o"/>
  <circle cx="10" cy="-88" r="26" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-15-85q4-30 27-30 26 0 30 27-14-11-29-4-13-11-28 7z" fill="{HAIR}" stroke="{HAIR}" stroke-width="2"/>
  <g fill="{INK}"><circle cx="2" cy="-86" r="2.5"/><circle cx="20" cy="-86" r="2.5"/></g>
  <path d="M2-72q10-8 18 0" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M30-50l40-16" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
</g>
{hand(440,270,-1)}
<g transform="translate(300 160)">
  <path d="M-70-40h140v70h-140zM-40 30l-10 26 34-26z" fill="#fffdf6" class="o"/>
  <g fill="{TONES['coral'][0]}"><rect x="-10" y="-24" width="20" height="34" rx="10"/><circle cy="20" r="10"/></g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('predecessor', '前の人から席を引き継ぐイラスト。', f"""
{person(140,352,1.15,1,'violet','violet','give','bun','smile')}
{person(470,352,1.15,-1,'teal','blue','reach','short','smile')}
{chair(300,356,1.1,'gold',1)}
<g class="a" marker-end="url(#ar)"><path d="M220 170h160"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('presence', '空いた席の中でその人が居合わせているイラスト。', f"""
{chair(300,356,1.25,'gold',1)}
{sit(290,352,1.25,1,'coral','blue','short','smile','down')}
{chair(110,356,1.15,'blue',1)}
{chair(500,356,1.15,'blue',1)}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><circle cx="300" cy="250" r="120"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
