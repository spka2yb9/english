"""第97回の描き直し: maximize / powerful。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('maximize', 'いっぱいまで大きく広げるイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-250-170h500v340h-500z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"/>
  <path d="M-240-160h480v320h-480z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round">
  <path d="M130 130L70 70M70 110V70h40"/>
  <path d="M470 130l60-60M530 110V70h-40"/>
  <path d="M130 290l-60 60M70 310v40h40"/>
  <path d="M470 290l60 60M530 310v40h-40"/>
</g>
""", ground=False)

add('powerful', '腕に力こぶを作って強さを示すイラスト。', f"""
<g transform="translate(250 300)">
  <path d="M-140 40v-40q0-24 24-24h70" fill="none" stroke="{SKIN}" stroke-width="46" stroke-linecap="round"/>
  <path d="M-46-24q30-70 76-30 40 34 4 74" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M34 20v-90" fill="none" stroke="{SKIN}" stroke-width="46" stroke-linecap="round"/>
  <rect x="6" y="-140" width="60" height="56" rx="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-30-16q26-30 56-6" fill="none" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-140 24h-40v40h40z" class="teal o"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M450 90l-56 110h46l-26 90 80-120h-50l30-80z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
