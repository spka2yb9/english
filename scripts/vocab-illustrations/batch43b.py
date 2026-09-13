"""第43回の描き直し: model, musical, obvious。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

star = '<path d="M0-42l12 25 27 4-19 19 4 27-24-13-24 13 4-27-19-19 27-4z"'

add('model', '見本の型と、それをまねて作られた同じ形のイラスト。', f"""
<g transform="translate(150 230)">
  <path d="M-80-90h160v180h-160z" class="teal o"/>
  {star} fill="#fffdf6"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-50 60h100"/></g>
</g>
<g transform="translate(390 230)">
  <path d="M-70-80h140v160h-140z" class="tealp o"/>
  {star} fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
</g>
<g transform="translate(530 230)">
  <path d="M-70-80h140v160h-140z" class="tealp o"/>
  {star} fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
</g>
<path d="M240 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 326h480" class="a"/>
""", ground=True, arrow=True)

add('musical', '音符が並ぶ楽譜と、ギターを置いた音楽のイラスト。', f"""
<g transform="translate(230 190)">
  <path d="M-160-100h320v190h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-130 {-56+i*26}h260"/>' for i in range(5))}</g>
  <g fill="{INK}"><ellipse cx="-80" cy="22" rx="16" ry="11"/><ellipse cx="0" cy="-4" rx="16" ry="11"/><ellipse cx="80" cy="22" rx="16" ry="11"/>
  <rect x="-68" y="-46" width="5" height="68"/><rect x="12" y="-72" width="5" height="68"/><rect x="92" y="-46" width="5" height="68"/></g>
</g>
<g transform="translate(470 280)">
  <path d="M-6-120h12v90h-12z" class="ink"/>
  <path d="M-22-130h44v16h-44z" class="goldd o"/>
  <ellipse cy="-4" rx="52" ry="60" class="goldd o"/>
  <circle cy="-4" r="20" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="2"><path d="M-8-110v100M0-110v100M8-110v100"/></g>
</g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('obvious', '暗くて見えなかったものが、明かりの下ではっきり見えるイラスト。', f"""
<g transform="translate(160 220)">
  <path d="M-110-110h220v220h-220z" fill="#41506a" class="o"/>
  <g opacity=".3"><circle r="60" fill="#7f8ea6"/></g>
  <path d="M-40 130h80" class="muted"/>
</g>
<g transform="translate(440 220)">
  <path d="M-110-110h220v220h-220z" fill="#fffdf6" class="o"/>
  <circle r="60" class="coral o"/>
</g>
{sun(440,80,24)}
<path d="M290 220h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 360l18 18 30-36"/></g>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
