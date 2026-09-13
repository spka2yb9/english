"""第82回の描き直し: glimpse / gaming / gut / handling / guilt。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('glimpse', 'とびらのすき間からちらっとのぞくイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-250-160h230v320h-230z" fill="#dfe6ea" class="o"/>
  <path d="M30-160h220v320H30z" fill="#dfe6ea" class="o"/>
  <circle cx="-50" cy="10" r="9" class="ink"/>
  <circle cx="60" cy="10" r="9" class="ink"/>
  <path d="M-20-160h50v320h-50z" fill="#fffdf6"/>
  <path d="M-20-160v320M30-160v320" class="a"/>
  <circle cx="5" cy="-70" r="26" class="goldp o"/>
  <path d="M-20 70h50v90h-50z" class="greenp"/>
  <path d="M5 70v-40" class="greens"/>
  <path d="M-20 30h50v40h-50z" class="green o"/>
</g>
<g transform="translate(140 190)">
  <ellipse rx="52" ry="30" fill="#fffdf6" class="o"/>
  <circle r="18" class="blue o"/><circle r="8" class="ink"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M196 190h84"/></g>
""", ground=False)

add('gaming', 'コントローラーを握ってゲームを楽しむイラスト。', f"""
<g transform="translate(320 130)">
  <path d="M-120-70h240v140h-240z" class="ink"/>
  <path d="M-108-58h216v116h-216z" class="bluep"/>
  <g class="coral o"><path d="M-60 20h34v26h-34z"/><path d="M-26-6h34v52h-34z"/><path d="M8 12h34v34H8z"/></g>
  <circle cx="66" cy="-24" r="15" class="gold o"/>
</g>
<g transform="translate(300 300)">
  <path d="M-160-20q-40 0-40 46t46 46q28 0 42-26h104q14 26 42 26t46-46-40-46q-60-14-100-14t-100 14z" class="violet o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2.5">
    <rect x="-124" y="20" width="56" height="16" rx="8"/><rect x="-104" y="0" width="16" height="56" rx="8"/>
  </g>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2.5">
    <circle cx="80" cy="6" r="13"/><circle cx="116" cy="28" r="13"/><circle cx="44" cy="28" r="13"/><circle cx="80" cy="50" r="13"/>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('gut', 'おなかの中で曲がりくねる腸のイラスト。', f"""
<g transform="translate(300 230)">
  <circle cx="0" cy="-160" r="42" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-120 140v-90q0-70 60-88 60-16 120 0 60 18 60 88v90z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-66-40q0-34 66-34t66 34v22q0 26-44 26t-44 28 44 28 40 26" fill="none" stroke="{TONES['coral'][0]}" stroke-width="24" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M-66-40q0-34 66-34t66 34v22q0 26-44 26t-44 28 44 28 40 26" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4" stroke-dasharray="4 16"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('handling', '壊れ物をそっと持ち上げてていねいに扱うイラスト。', f"""
{box(300,210,170,120,32,'gold')}
{hand(120,270,1)}
{hand(480,270,-1)}
<g transform="translate(300 200)">
  <path d="M-22-40h44l-6 34q-2 16-16 16t-16-16z" fill="#fffdf6" class="o"/>
  <path d="M0 10v30M-20 40h40" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8">
  <path d="M170 200q30-40 70-56M430 200q-30-40-70-56"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('guilt', '自分のしたことを悔いて心が重くなるイラスト。', f"""
{person(230,352,1.2,1,'blue','blue','think','short','sad')}
{cloud(210,90,1.2,'violet')}
<g transform="translate(430 320)">
  <path d="M-40-50h80l-10 50h-60z" fill="#fffdf6" class="o" transform="rotate(28 0 0)"/>
  <path d="M-30 26q40-16 90 4-50 20-90-4z" class="bluep o"/>
</g>
{hand(540,250,-1)}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M486 250H340"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
