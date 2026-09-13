"""第88回の描き直し: opening / oxygen / peasant。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('opening', 'テープを切って始まる開幕のイラスト。', f"""
{person(140,352,1.1,1,'violet','blue','reach','bun','smile')}
{person(460,352,1.1,-1,'teal','gold','reach','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10">
  <path d="M100 250h150M350 250h150"/>
</g>
<g transform="translate(300 250) rotate(-16)">
  <path d="M-60-40L40-6" fill="none" stroke="#b9c2c9" stroke-width="9" stroke-linecap="round"/>
  <path d="M-60 40L40 6" fill="none" stroke="#b9c2c9" stroke-width="9" stroke-linecap="round"/>
  <circle cx="-74" cy="-48" r="18" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
  <circle cx="-74" cy="48" r="18" fill="none" stroke="{TONES['blue'][0]}" stroke-width="8"/>
  <circle cx="10" cy="0" r="6" class="ink"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('oxygen', '木が出し、息に取り込む酸素のイラスト。', f"""
{tree(130,340,1.3)}
<g transform="translate(410 190)">
  <path d="M-70 0h140" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10"/>
  <circle cx="-70" cy="0" r="54" class="tealp o"/>
  <circle cx="70" cy="0" r="54" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M230 250q50-50 90-60"/></g>
<g class="tealp o"><circle cx="480" cy="310" r="20"/><circle cx="530" cy="278" r="13"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('peasant', 'くわで畑を耕す農民のイラスト。', f"""
<path d="M0 300h600v100H0z" fill="#e8ded2"/>
<g fill="none" stroke="#c9b79f" stroke-width="6">{''.join(f'<path d="M0 {322+i*26}h600"/>' for i in range(3))}</g>
{person(210,340,1.25,1,'gold','green','reach','cap','neutral')}
<g transform="translate(266 296) rotate(34)">
  <path d="M-7 0h14v110h-14z" fill="{TONES['gold'][2]}"/>
  <path d="M-30 104h60v18h-60z" fill="#b9c2c9" stroke="{INK}" stroke-width="2.5"/>
</g>
<g class="greens">{''.join(f'<path d="M{430+i*50} 336v-34"/>' for i in range(3))}</g>
<g class="greenp o">{''.join(f'<circle cx="{430+i*50}" cy="296" r="13"/>' for i in range(3))}</g>
<path d="M0 300h600" class="a"/>
""", ground=False)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
