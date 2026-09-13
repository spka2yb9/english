"""第84回の描き直し: injustice / inflation。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'

add('injustice', 'てんびんがかたよって不当に扱われるイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-14 0h28v190h-28z" class="ink"/>
  <path d="M-70 190h140v20h-140z" class="ink"/>
  <path d="M-190-40L190 30" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-186-38v50M186 32v50" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-246 12h120q0 44-60 44t-60-44z" class="tealp o"/>
  <path d="M126 82h120q0 44-60 44t-60-44z" class="coralp o"/>
</g>
<path d="M186 150v12" class="a"/>
<path d="M486 232v12" class="a"/>
<g class="coral o"><ellipse cx="486" cy="248" rx="40" ry="16"/><ellipse cx="486" cy="228" rx="40" ry="16"/><ellipse cx="486" cy="208" rx="40" ry="16"/></g>
{xx(150,330,1)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('inflation', '物の値段がどんどんふくらんで上がるイラスト。', f"""
<g transform="translate(150 250)">
  <ellipse rx="50" ry="58" class="coralp o"/>
  <path d="M0 58l-12 18h24z" class="coral o"/>
</g>
<g transform="translate(340 220)">
  <ellipse rx="96" ry="112" class="coral o"/>
  <path d="M0 112l-18 26h36z" class="corald o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M212 230h34"/></g>
<g transform="translate(490 180)">
  <path d="M-56-70h70l42 42-70 70-42-42z" class="goldp o"/>
  <circle cx="-24" cy="-38" r="10" class="goldd o"/>
</g>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="9" stroke-linecap="round" marker-end="url(#ar)"><path d="M490 350v-80"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
