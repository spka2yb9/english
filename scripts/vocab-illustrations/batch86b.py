"""第86回の描き直し: mask / metaphor / meantime / manipulation。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('mask', '仮面を顔の前にかざして隠すイラスト。', f"""
{face(280,210,96,'flat')}
<g transform="translate(310 210)">
  <path d="M-100-80q100-46 200 0 0 130-100 130T-100-80z" class="goldp o"/>
  <g fill="{INK}"><path d="M-56-40q26-18 52 0-26 18-52 0zM24-40q26-18 52 0-26 18-52 0z"/></g>
  <path d="M10 30q24 18 48 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
  <path d="M0 180V50" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('metaphor', '心を炎にたとえて言い表す隠喩のイラスト。', f"""
<g transform="translate(150 210)">
  <path d="M-96-80h192v160h-192z" class="paper"/>
  <path d="M0-20q-40-46-70-10-28 34 70 96 98-62 70-96-30-36-70 10z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"><path d="M262 190h76M262 230h76"/></g>
<g transform="translate(450 210)">
  <path d="M-96-80h192v160h-192z" class="paper"/>
</g>
{flame(450,286,0.9)}
<path d="M60 356h480" class="a"/>
""", ground=True)

add('meantime', 'ふたつの出来事のあいだ、待っている時間のイラスト。', f"""
<g transform="translate(300 160)">
  <circle cx="-210" cy="0" r="44" class="teal o"/>
  <circle cx="210" cy="0" r="44" class="teal o"/>
  <path d="M-210 0h420" class="a"/>
  <path d="M-150 60h300v44h-300z" class="goldp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M300 160h-100M300 160h100"/></g>
{person(200,376,0.8,1,'coral','blue','think','short','neutral')}
<g transform="translate(400 320)">
  <circle r="44" fill="#fffdf6" class="o"/>
  <path d="M0 0v-30M0 0l20 12" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="5" class="ink"/>
</g>
""", ground=False, arrow=True)

add('manipulation', '糸をあやつって人形を思うままに動かすイラスト。', f"""
{hand(300,80,1)}
<g transform="translate(300 150)">
  <path d="M-90-10h180v16h-180z" fill="{TONES['gold'][2]}" class="o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="3">
  <path d="M215 160l-25 80M300 160v70M385 160l25 80"/>
</g>
<g transform="translate(300 330)">
  <circle cy="-100" r="36" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30-62q30-12 60 0l-8 62h-44z" class="teal o"/>
  <path d="M-26-56l-36 34M26-56l36 34" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-20 0l-16 52M20 0l16 52" fill="none" stroke="{TONES['blue'][2]}" stroke-width="13" stroke-linecap="round"/>
  <g fill="{INK}"><circle cx="-12" cy="-104" r="3"/><circle cx="12" cy="-104" r="3"/></g>
  <path d="M-10-88h20" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
