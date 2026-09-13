"""第70回の描き直し: tube（注射器に見えたため歯みがき型に）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('tube', '中身を絞り出して使うチューブのイラスト。', f"""
<g transform="translate(280 260)">
  <path d="M-150-60h230q30 0 30 60t-30 60h-230z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-150-60l-22-16v152l22-16z" fill="#cfe0ea" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#9ec7dd" stroke-width="4"><path d="M-120-30h140M-120 0h120M-120 30h140"/></g>
  <path d="M110-26h44v52h-44z" class="teal o"/>
  <path d="M154-16h26v32h-26z" class="teald o"/>
</g>
<path d="M470 260q14 26 10 50" fill="none" stroke="{TONES['teal'][0]}" stroke-width="14" stroke-linecap="round"/>
{hand(240,140,1)}
<path d="M240 180v40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
