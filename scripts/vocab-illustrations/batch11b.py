from lib import *
emit('vehicle', '車・トラック・バスなど、人や物を運ぶ乗り物を並べたイラスト。', f"""
<g transform="translate(150 190) scale(0.5)">
  <path d="M-150 40h300l-16-56h-50l-34-56h-120l-34 56h-62z" class="coral o"/>
  <path d="M-110-16h80v-44h-58zM-10-60h74l26 44H-10z" class="bluep o"/>
  <circle cx="-84" cy="48" r="30" class="ink"/><circle cx="84" cy="48" r="30" class="ink"/>
</g>
<g transform="translate(410 190) scale(0.5)">
  <path d="M-200 40h130v-120h-130z" fill="#e7eef4" stroke="{INK}" stroke-width="3"/>
  <path d="M-70 40h270v-90H-70z" class="tealp o"/>
  <path d="M-190-60h100v40h-100z" class="bluep o"/>
  <circle cx="-150" cy="52" r="30" class="ink"/><circle cx="110" cy="52" r="30" class="ink"/>
</g>
<g transform="translate(300 320) scale(0.5)">
  <path d="M-200-60h400v100h-400z" class="goldp o"/>
  <g class="bluep o"><rect x="-170" y="-40" width="60" height="40"/><rect x="-90" y="-40" width="60" height="40"/><rect x="-10" y="-40" width="60" height="40"/><rect x="70" y="-40" width="60" height="40"/></g>
  <circle cx="-120" cy="46" r="26" class="ink"/><circle cx="120" cy="46" r="26" class="ink"/>
</g>
""", ground=True)
print(sheet(['vehicle']))
