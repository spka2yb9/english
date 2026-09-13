from lib import *
emit('dressed', 'コートを着てくつをはき、身支度を終えた人のイラスト。', f"""
<circle cx="470" cy="100" r="56" class="violetp"/>
{person(280,336,1.3,1,'violet','blue','stand','short','smile')}
<g transform="translate(280 286)">
  <path d="M-60-26q60-16 120 0l16 54-24 10-8-20v76h-88v-76l-8 20-24-10z" class="violetd o"/>
  <path d="M0-34v120" fill="none" stroke="{TONES['violet'][1]}" stroke-width="3"/>
  <path d="M-28-28q28 20 56 0" fill="none" stroke="{TONES['violet'][1]}" stroke-width="3"/>
</g>
<path d="M244 244q36-16 72 0l-8 22h-56z" class="coralp o"/>
<g class="ink"><rect x="240" y="330" width="34" height="16" rx="5"/><rect x="288" y="330" width="34" height="16" rx="5"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M430 300l18 18 30-36"/></g>
""", ground=True)
emit('cooker', '台所の調理器の火の上で、なべを加熱しているイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-170-40h340v110h-340z" fill="#dfe6ea" class="o"/>
  <path d="M-170-40h340" class="a"/>
  <g class="coral o"><circle cx="110" cy="26" r="16"/><circle cx="150" cy="26" r="16"/></g>
</g>
<g transform="translate(200 290)">{flame(0,0,0.8)}</g>
<g transform="translate(200 236)">
  <path d="M-86-40h172l-14 66h-144z" fill="#eef4f8" class="o"/>
  <path d="M-102-40h204" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M0-40v-18" class="a"/>
</g>
<g class="muted" opacity=".8"><path d="M178 150q-14-30 4-52M228 146q-14-34 6-56"/></g>
""", ground=True)
print(sheet(['dressed','cooker']))
