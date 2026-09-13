from lib import *
emit('appearance', '同じ人が服装と髪型を変えて、見た目の違いを並べたイラスト。', f"""
<g transform="translate(160 0)">
  <path d="M-110 60h220v300h-220z" fill="#fffdf6" stroke="{MUTED}" stroke-width="3"/>
  {person(0,340,1.05,1,'teal','blue','stand','short','smile')}
</g>
<g transform="translate(440 0)">
  <path d="M-110 60h220v300h-220z" fill="#fffdf6" stroke="{MUTED}" stroke-width="3"/>
  {person(0,340,1.05,1,'coral','violet','stand','bun','smile')}
  <path d="M-46 214q46-16 92 0l-8 26h-76z" class="coralp o"/>
</g>
<path d="M280 210h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
emit('chain', '輪が互いにかみ合って、一本の鎖になっているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
<g fill="none" stroke="{MUTED}" stroke-width="13" stroke-linejoin="round">
  {''.join(f'<ellipse cx="{120+i*52}" cy="230" rx="36" ry="20" transform="rotate({0 if i%2==0 else 90} {120+i*52} 230)"/>' for i in range(8))}
</g>
<path d="M120 330h380" class="muted"/>
""", ground=True)
print(sheet(['appearance','chain']))
