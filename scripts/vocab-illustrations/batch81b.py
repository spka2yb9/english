"""第81回の描き直し: fraud / forever / fossil / freedom。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('fraud', '仮面で顔を隠してお金をだまし取る詐欺のイラスト。', f"""
{person(160,350,1.15,1,'violet','blue','give','short','neutral')}
<g transform="translate(196 236)">
  <path d="M-56-22q56-30 112 0-6 46-56 46t-56-46z" class="goldp o"/>
  <g fill="{INK}"><path d="M-34-10q14-10 28 0-14 10-28 0z"/><path d="M6-10q14-10 28 0-14 10-28 0z"/></g>
  <path d="M0 24v70" class="a"/>
</g>
<g transform="translate(340 262)">
  <path d="M-50-26h100v52h-100z" class="greenp o"/>
  <circle r="14" class="gold o"/>
</g>
{person(480,350,1.1,-1,'coral','gold','give','bob','sad')}
<path d="M412 306h-110" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M320 150l40 40M360 150l-40 40"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('forever', '終わりなく回り続ける永遠のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M0 0q-46-80-110-80T-220 0q0 80 110 80T0 0q46-80 110-80T220 0q0 80-110 80T0 0z"
        fill="none" stroke="{TONES['teal'][0]}" stroke-width="22" stroke-linejoin="round"/>
  <path d="M0 0q-46-80-110-80T-220 0q0 80 110 80T0 0q46-80 110-80T220 0q0 80-110 80T0 0z"
        fill="none" stroke="{TONES['teal'][1]}" stroke-width="8"/>
</g>
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5" stroke-linecap="round" marker-end="url(#ar)">
  <path d="M250 340q50 30 100 0"/>
</g>
<path d="M60 372h480" class="a"/>
""", ground=True, arrow=True)

add('fossil', '岩に残った魚の骨の化石のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-110h360v220h-360z" fill="#cdd6dd" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round">
    <path d="M-110 0q80-80 190-40 40 14 46 40-6 26-46 40-110 40-190-40z"/>
    <path d="M-110 0l-56-40v80z"/>
    <path d="M-60-34v68M-20-46v92M20-48v96M60-42v84M100-30v60"/>
  </g>
  <circle cx="120" cy="-12" r="8" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-180-60h50M130-80h50M-180 70h40M140 60h40"/></g>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('freedom', 'かごから大空へ飛び立つ鳥の自由のイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-70 90v-120q0-50 70-50t70 50v120z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-46+i*30} 90V-30"/>' for i in range(3))}</g>
  <path d="M0-90v-20" class="a"/>
  <path d="M20-30h56v120H20z" fill="#fffaf1"/>
  <path d="M20-30v120M76-30v106" class="a"/>
</g>
<g transform="translate(430 150)">
  <path d="M-40-40q40-34 74 6 34 6 42 30-40 40-96 24-44-14-20-60z" class="gold o"/>
  <circle cx="54" cy="-24" r="22" class="gold o"/>
  <path d="M74-28l30 10-30 12z" class="coral o"/>
  <circle cx="60" cy="-30" r="4" class="ink"/>
  <path d="M-16-34q26-56 62-18-32 22-62 18z" class="goldp o"/>
  <path d="M-60 20l-52 22 44 8z" class="goldd o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 9"><path d="M250 220q60-70 130-84"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
