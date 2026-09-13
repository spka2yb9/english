"""第99回の描き直し: tourism / versus。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('tourism', 'カメラと荷物で名所をめぐる観光のイラスト。', f"""
<g transform="translate(440 230)">
  <path d="M-60 120L-16-90h32L60 120z" class="teal o"/>
  <path d="M-16-90l16-56 16 56z" class="tealp o"/>
  <path d="M-40 40h80M-30 0h60" fill="none" stroke="#fffdf6" stroke-width="6"/>
  <path d="M0-146v-24" class="a"/>
</g>
{person(170,352,1.2,1,'coral','blue','carry','bob','smile')}
<g transform="translate(212 290)">
  <path d="M-44-24h88v48h-88z" class="ink"/>
  <circle cx="6" cy="0" r="15" class="bluep o"/>
  <path d="M-36-34h26v10h-26z" class="ink"/>
</g>
<g transform="translate(280 340)">
  <path d="M-34-26h68v52h-68z" class="goldd o"/>
  <path d="M-14-36h28v10h-28z" class="a" fill="none"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('versus', '両者を向かい合わせて対にするイラスト。', f"""
<g transform="translate(150 240)">
  <path d="M-80-80h160v70q0 80-80 110-80-30-80-110z" class="tealp o"/>
</g>
<g transform="translate(450 240)">
  <path d="M-80-80h160v70q0 80-80 110-80-30-80-110z" class="coralp o"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M300 120l-44 92h36l-20 76 62-100h-40l24-68z"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" marker-end="url(#ar)"><path d="M250 330h-30M350 330h30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
