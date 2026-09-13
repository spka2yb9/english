"""第96回の描き直し: cultural。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('cultural', 'その土地に伝わる面・太鼓・扇のイラスト。', f"""
<g transform="translate(150 230)">
  <path d="M-60-70q60-44 120 0 0 120-60 120T-60-70z" class="goldp o"/>
  <g fill="{INK}"><path d="M-32-36q22-16 38 0-18 10-38 0zM18-36q22-16 38 0-18 10-38 0z"/></g>
  <path d="M4 34q24 18 48 0" fill="none" stroke="{TONES['gold'][2]}" stroke-width="5"/>
</g>
<g transform="translate(320 290)">
  <ellipse cy="50" rx="66" ry="30" class="goldd o"/>
  <path d="M-66 50V-10q0-32 66-32t66 32v60" class="gold o"/>
  <ellipse cy="-10" rx="66" ry="30" fill="#fdf6e3" class="o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4">{''.join(f'<path d="M{-46+i*30} 12v40"/>' for i in range(4))}</g>
</g>
<g transform="translate(490 240)">
  <path d="M0 110A130 130 0 0 1-92 18L0 110z" fill="#fffaf1"/>
  <path d="M0 110L-92 18A130 130 0 0 1 18-20z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="3">
    <path d="M0 110L-70 40M0 110L-52 8M0 110L-20-12"/>
  </g>
  <circle cx="0" cy="110" r="8" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
