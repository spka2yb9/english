from lib import *
emit('fly', '鳥が翼を広げて空を飛んでいるイラスト。', f"""
{cloud(120,110,1.2)}{cloud(470,260,1.0)}
<g transform="translate(300 200) scale(1.5) rotate(-8)">
  <ellipse cx="0" cy="0" rx="56" ry="30" class="teal o"/>
  <path d="M-56 0l-42 14 10-30z" class="teal o"/>
  <ellipse cx="42" cy="-18" rx="26" ry="22" class="teal o"/>
  <path d="M62-22l26-8-16 20z" class="gold o"/>
  <circle cx="48" cy="-24" r="3.6" class="ink"/>
  <path d="M-16-14q-6-44 34-42 34 2 30 30-4 24-64 12z" class="tealp o"/>
  <path d="M-10-8q10-24 34-24" fill="none" stroke="{TONES['teal'][2]}" stroke-width="2.5"/>
</g>
<path d="M110 280q90-42 150-54" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(sheet(['fly']))
