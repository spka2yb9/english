"""第7回の描き直し分。batch07.py のあとに実行する。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

def bird(x, y, s=1, r=0, cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({r})">'
            f'<path d="M-56 8q-24-40 10-58 30-16 60 4 26 18 22 44-4 24-40 26-38 2-52-16z" class="{cls} o"/>'
            f'<path d="M-10-16q-6-46 40-44 40 2 34 34-6 28-74 10z" class="{cls}p o"/>'
            f'<path d="M-56 8l-40 16 30 12z" class="{cls} o"/>'
            f'<path d="M62-2l30-10-18 24z" class="gold o"/>'
            f'<circle cx="44" cy="-14" r="4" class="ink"/></g>')

add('fly', '鳥が翼を広げて空を飛んでいるイラスト。', f"""
{cloud(120,110,1.2)}{cloud(470,260,1.0)}
{bird(300,190,1.5,-10)}
<path d="M110 270q90-40 150-52" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('airline', '航空会社の旅客機が、雲の上を飛んでいるイラスト。', f"""
{cloud(110,110,1.2)}{cloud(480,190,1.0)}{cloud(250,330,1.4)}
{plane(300,210,1.15,-8,'teal')}
<path d="M60 262q90-32 160-42" class="muted"/>
""", ground=False)

add('grab', '差し出されたかばんの取っ手を、手ですばやくつかみ取るイラスト。', f"""
<circle cx="120" cy="100" r="56" class="coralp"/>
<g transform="translate(340 316)">
  <path d="M-96-30h192v100h-192z" class="tealp o"/>
  <path d="M-96 10h192" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
  <path d="M-40-30q0-46 40-46t40 46" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
{hand(340,236,1)}
<g class="corals" style="stroke-width:4"><path d="M410 190l26-26M432 226l32-14M386 170l6-30"/></g>
<path d="M200 210q60-26 96-8" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('headache', '頭の両側を手で押さえ、頭の中で痛みが響いている人のイラスト。', f"""
{person(300,346,1.2,1,'teal','blue','hold','short','sad')}
<circle cx="252" cy="238" r="17" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<circle cx="348" cy="238" r="17" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<g class="corals" opacity=".95" style="stroke-width:5">
  <path d="M236 194q-26-10-30-34M364 194q26-10 30-34M300 172v-32"/>
</g>
<g transform="translate(300 216)">
  <path d="M-34-26l14 18-18 14 20 18" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round"/>
</g>
<path d="M80 366h440" class="a"/>
""", ground=True)

add('dip', 'クッキーをカップの飲み物に、半分だけ浸しているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(280 270)">
  <path d="M-90-80h180l-18 140h-144z" fill="#fffdf6" class="o"/>
  <path d="M-90-80h180" class="a"/>
  <path d="M-82-46h164l-14 106h-136z" class="goldp o"/>
  <path d="M-82-46h164" class="a"/>
  <path d="M90-60q40 0 40 28t-40 28" fill="none" stroke="{INK}" stroke-width="9"/>
</g>
<g transform="translate(300 216) rotate(14)">
  <circle r="44" class="goldd o"/>
  <g fill="{INK}"><circle cx="-14" cy="-12" r="5"/><circle cx="12" cy="4" r="5"/><circle cx="-4" cy="22" r="5"/><circle cx="20" cy="-18" r="5"/></g>
</g>
<path d="M300 224h-84" fill="none" stroke="{TONES['gold'][2]}" stroke-width="0"/>
<path d="M390 170v50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('erupt', '火山の火口から溶岩と煙が噴き上がっているイラスト。', f"""
{cloud(300,60,1.9,'gold')}
{cloud(180,110,1.1,'gold')}
<path d="M40 340L300 100l260 240z" class="tealp o"/>
<path d="M300 100l56 56H244z" fill="#fffaf1" stroke="{INK}" stroke-width="2.5"/>
<path d="M262 104q-40-56-18-84M338 104q40-56 18-84" class="corals" style="stroke-width:6"/>
<path d="M300 96V20" class="corals" style="stroke-width:7" marker-end="url(#ar)"/>
<path d="M282 140q-34 84-84 140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="18" stroke-linecap="round"/>
<path d="M322 140q34 74 90 128" fill="none" stroke="{TONES['coral'][0]}" stroke-width="16" stroke-linecap="round"/>
<path d="M282 140q-34 84-84 140" fill="none" stroke="{TONES['gold'][1]}" stroke-width="6" stroke-linecap="round"/>
<g class="coral o"><circle cx="180" cy="70" r="13"/><circle cx="430" cy="86" r="11"/><circle cx="130" cy="150" r="9"/></g>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
