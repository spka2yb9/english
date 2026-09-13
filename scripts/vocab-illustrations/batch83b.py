"""第83回の描き直し: hip / hunger / honor / horn。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('hip', '体の腰まわりを指し示すイラスト。', f"""
{person(300,356,1.5,1,'teal','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10"><ellipse cx="300" cy="336" rx="76" ry="40"/></g>
<path d="M480 336h-90" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('hunger', 'お皿が空でおなかがすいているイラスト。', f"""
{person(170,352,1.2,1,'teal','blue','hold','short','sad')}
<g transform="translate(400 250)">
  <circle r="110" fill="#fffdf6" class="o"/>
  <circle r="76" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M-140-70v90M-148-70v40h16v-40" fill="none" stroke="{MUTED}" stroke-width="5"/>
  <path d="M140-70v90M140-70q16 10 0 40" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><circle cx="186" cy="292" r="40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round"><path d="M240 250q14-14 0-28M264 260q22-22 0-44"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('honor', 'たたえられて贈られる名誉のメダルのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-70-160h44l50 100h-44zM70-160H26l-50 100h44z" class="coral o"/>
  <path d="M-26-160h52v34h-52z" class="corald o"/>
  <circle cx="0" cy="20" r="82" class="gold o"/>
  <circle cx="0" cy="20" r="58" class="goldp o"/>
  <path d="M0-26l16 34 38 4-28 26 8 38-34-20-34 20 8-38-28-26 38-4z" class="goldd"/>
</g>
<g class="golds"><path d="M150 200l-26-22M450 200l26-22M300 336v20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('horn', '頭に生えた大きな角のイラスト。', f"""
<g transform="translate(300 270)">
  <ellipse cx="0" cy="0" rx="80" ry="90" class="goldp o"/>
  <ellipse cx="0" cy="46" rx="44" ry="38" class="gold o"/>
  <ellipse cx="-15" cy="42" rx="7" ry="10" class="ink"/><ellipse cx="15" cy="42" rx="7" ry="10" class="ink"/>
  <circle cx="-38" cy="-24" r="8" class="ink"/><circle cx="38" cy="-24" r="8" class="ink"/>
  <ellipse cx="-84" cy="-30" rx="20" ry="12" class="goldd o"/>
  <ellipse cx="84" cy="-30" rx="20" ry="12" class="goldd o"/>
</g>
<g fill="#b9a98f" stroke="{INK}" stroke-width="3" stroke-linejoin="round">
  <path d="M240 190q-40-40-30-90 40 10 56 66-14 10-26 24z"/>
  <path d="M360 190q40-40 30-90-40 10-56 66 14 10 26 24z"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="2.5">
  <path d="M224 156q14-8 24-14M216 132q14-8 24-14M212 108q12-6 22-12"/>
  <path d="M376 156q-14-8-24-14M384 132q-14-8-24-14M388 108q-12-6-22-12"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
