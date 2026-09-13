from lib import *
emit('heel', 'くつのかかとの位置に印をつけたイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(280 250)">
  <path d="M-130 40q-6-40 26-52l70-26q40-14 74 2 26 12 26 40v36z" class="coralp o"/>
  <path d="M-130 40h196v22h-196z" class="coral o"/>
  <path d="M66 40h30v46H66z" class="coral o"/>
  <path d="M-100-6q40-16 90-16" fill="none" stroke="{TONES['coral'][2]}" stroke-width="4"/>
  <circle cx="80" cy="56" r="46" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="11 9"/>
</g>
<path d="M120 340h360" class="a"/>
""", ground=True)
print(sheet(['heel']))
