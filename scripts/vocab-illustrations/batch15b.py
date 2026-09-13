from lib import *
emit('disabled', '車いすの人のために、段差にスロープが設けられているイラスト。', f"""
<path d="M330 240h270v160H330z" class="ground"/>
<path d="M330 240h270" class="a"/>
<path d="M60 340h270l0-100z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
<path d="M60 340h270" class="a"/>
<g transform="translate(200 250) rotate(-20)">
  <circle cx="10" cy="40" r="46" fill="none" stroke="{INK}" stroke-width="9"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M10-6v92M-36 40h92M-23 7l66 66M43 7l-66 66"/></g>
  <circle cx="-42" cy="66" r="16" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-30 4h50v40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="12" stroke-linecap="round"/>
  <path d="M-30 4l-4-40" fill="none" stroke="{TONES['teal'][0]}" stroke-width="10" stroke-linecap="round"/>
  <path d="M-24-30q30-14 54 6" fill="none" stroke="{SKIN}" stroke-width="11" stroke-linecap="round"/>
  <circle cx="-32" cy="-58" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-56-66q4-26 26-26 22 0 26 24-14-8-28-2-10-6-24 4z" fill="{HAIR}"/>
  <circle cx="-24" cy="-56" r="2.6" class="ink"/>
</g>
<path d="M120 200q60-30 120-14" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(sheet(['disabled']))
