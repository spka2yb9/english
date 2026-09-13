from lib import *
emit('rest', '作業を止めていすに座り、ひと休みしているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(300 320)">
  <path d="M-80-20h160v18h-160z" class="goldp o"/>
  <path d="M-70 0v50M70 0v50" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M60-20v-110h18v110z" class="goldd o"/>
</g>
<g transform="translate(290 300)">
  <path d="M-30-70q30-14 60 0l-8 68h-44z" class="teal o"/>
  <path d="M-24-8l-56 20M20-8l14 30" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-80 12h-26M34 40h-8" fill="none" stroke="{TONES['blue'][2]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-26-58l-30 34M26-58l26 26" fill="none" stroke="{SKIN}" stroke-width="10" stroke-linecap="round"/>
  <circle cx="0" cy="-96" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-24-98q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" fill="{HAIR}"/>
  <circle cx="-8" cy="-92" r="2.2" class="ink"/><circle cx="8" cy="-92" r="2.2" class="ink"/>
  <path d="M-8-82q8 8 16 0" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g class="muted"><path d="M410 220q-14-30 4-52M446 216q-14-34 6-56"/></g>
<path d="M120 370h360" class="a"/>
""", ground=True)
print(sheet(['rest']))
