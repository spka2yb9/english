"""第90回の描き直し: prosperity / protein / radiation / rail。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('prosperity', '商いがのびて富が積み上がる繁栄のイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-150-120h300v240h-300z" class="paper"/>
  <g class="teal o">{''.join(f'<rect x="{-120+i*56}" y="{60-i*40}" width="40" height="{40+i*40}"/>' for i in range(5))}</g>
  <path d="M-130 100h270" class="a"/>
  <path d="M-120 40q120-60 250-130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"/>
</g>
<g class="gold o">
  <ellipse cx="470" cy="340" rx="66" ry="22"/><ellipse cx="470" cy="310" rx="66" ry="22"/>
  <ellipse cx="470" cy="280" rx="56" ry="20"/><ellipse cx="470" cy="252" rx="44" ry="17"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('protein', '体をつくるもとになる蛋白質のイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-70-40q70-40 130 0 20 50-50 70-70-10-80-70z" class="corald o"/>
  <path d="M56 26l50 26M100 38l22 26" fill="none" stroke="#fffdf6" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(300 320)">
  <ellipse rx="40" ry="50" fill="#fffdf6" class="o"/>
  <circle r="19" class="gold o"/>
</g>
<g transform="translate(420 200)">
  <ellipse rx="70" ry="38" class="bluep o"/>
  <path d="M64 0l40-26v52z" class="blue o"/>
  <circle cx="-44" cy="-6" r="5" class="ink"/>
</g>
{person(530,352,0.85,-1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M400 330h70"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('radiation', '見えない線を出す放射のイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="150" class="goldp o"/>
  <circle r="26" class="ink"/>
  <g fill="{INK}">
    <path d="M-12-43A45 45 0 0 1 32-32L85-85A120 120 0 0 0-31-116z" transform="rotate(0)"/>
    <path d="M-12-43A45 45 0 0 1 32-32L85-85A120 120 0 0 0-31-116z" transform="rotate(120)"/>
    <path d="M-12-43A45 45 0 0 1 32-32L85-85A120 120 0 0 0-31-116z" transform="rotate(240)"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('rail', 'まくら木の上に伸びる二本のレールのイラスト。', f"""
<g fill="{TONES['gold'][2]}">
  {''.join(f'<rect x="{120+i*22}" y="{356-i*32}" width="{360-i*44}" height="{15-i}" rx="4"/>' for i in range(7))}
</g>
<g fill="none" stroke="#b9c2c9" stroke-width="14" stroke-linecap="round">
  <path d="M170 390L272 150M430 390L328 150"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="3">
  <path d="M170 390L272 150M430 390L328 150"/>
</g>
""", ground=False)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
