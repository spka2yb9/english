"""第101回の描き直し: tuition（taxpayer と同じ構図だったため）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('tuition', '授業を受けるために払う月謝のイラスト。', f"""
<g transform="translate(340 150)">
  <path d="M-150-80h300v140h-300z" class="ink"/>
  <path d="M-136-66h272v112h-272z" fill="#2c3a30"/>
  <g fill="none" stroke="#e8f1e8" stroke-width="5" stroke-linecap="round">
    <path d="M-100-30h120M-100 0h90M-100 30h140"/>
  </g>
</g>
{person(470,352,1.15,-1,'violet','violet','point','bun','smile')}
{person(150,352,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(280 280)">
  <path d="M-56-28h112v56h-112z" class="greenp o"/>
  <circle r="15" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 220h120"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

print(len(W), ' '.join(W))
print(sheet(W, '/tmp/vocab-sheet2.html'))
