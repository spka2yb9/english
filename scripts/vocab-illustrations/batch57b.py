"""第57回の描き直し: delivery, dependable（box を translate 内で絶対座標指定していた）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('delivery', 'トラックで運んだ荷物を家まで届けるイラスト。', f"""
<g transform="translate(150 270)">
  <path d="M-100 40h90v-90h-90z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-10 40h130v-70H-10z" class="tealp o"/>
  <circle cx="-60" cy="52" r="26" class="ink"/><circle cx="70" cy="52" r="26" class="ink"/>
</g>
{person(320,340,0.95,1,'teal','blue','carry','cap','smile')}
{box(320,250,90,64,0,'gold')}
<g transform="translate(490 290)">
  <path d="M-70 50h140V-20h-140z" fill="#f4ead2" class="o"/>
  <path d="M-90-20l90-60 90 60z" class="coral o"/>
  <path d="M-20 50V10h40v40z" class="goldd o"/>
</g>
<path d="M390 240h30" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('dependable', '重い荷を任せても崩れない、頼れる台のイラスト。', f"""
{box(300,190,190,96,0,'gold')}
<g transform="translate(300 320)">
  <path d="M-150-40h300v40h-300z" class="teal o"/>
  <path d="M-120 0h44v60h-44zM76 0h44v60H76z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 110v40"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 200l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
