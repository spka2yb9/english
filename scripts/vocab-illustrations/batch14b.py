from lib import *
emit('fur', '柔らかい毛におおわれた動物の、ふさふさした毛並みのイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(260 260)">
  <ellipse cx="0" cy="30" rx="110" ry="70" class="goldp o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3">
    {''.join(f'<path d="M{-96+i*24} {84 - abs(i-4)*6}q6-30 12-54"/>' for i in range(9))}
  </g>
  <circle cx="-70" cy="-40" r="46" class="goldp o"/>
  <path d="M-104-64q-14-40 8-42 20-2 22 26z" class="goldd o"/>
  <path d="M-40-66q16-36 34-16 12 14-8 30z" class="goldd o"/>
  <circle cx="-84" cy="-44" r="3.6" class="ink"/><circle cx="-56" cy="-44" r="3.6" class="ink"/>
  <path d="M-78-26q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="2.5"><path d="M-110-40h-22M-110-30h-22M-30-40h22M-30-30h22"/></g>
</g>
""", ground=True)
emit('heat', '火にかけたなべの温度が上がり、湯気が立つイラスト。', f"""
{thermometer(470,300,0.85,1.0)}
<g transform="translate(240 230)">
  <path d="M-100-40h200l-14 100h-172z" fill="#dfe6ea" class="o"/>
  <path d="M-114-40h228" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M-86-12h172l-10 72h-152z" class="bluep o"/>
</g>
{flame(240,346,0.85)}
<g class="muted" opacity=".85"><path d="M210 140q-16-40 6-70M270 136q-16-44 8-76"/></g>
<path d="M380 190v-46" class="corals" marker-end="url(#ar)"/>
""", ground=True, arrow=True)
emit('expert', '長年の経験で、複雑な作業を難なくこなしている人のイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
{person(190,346,1.15,1,'teal','blue','point','cap','smile')}
<g transform="translate(380 250)">
  <path d="M-90-70h180v140h-180z" class="tealp o"/>
  <g fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"><path d="M-60-40h120M-60-10h120M-60 20h90"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M290 160l18 18 30-36"/></g>
<g transform="translate(190 150)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(sheet(['fur','heat','expert']))
