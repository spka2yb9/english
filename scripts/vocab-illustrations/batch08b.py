"""第8回の描き直し分。batch08.py のあとに実行する。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('close', '開いていた本の表紙を、手でぱたんと閉じているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="tealp"/>
<g transform="translate(300 290)">
  <path d="M0 20q-70-34-150-14v-120q80-20 150 14z" class="tealp o"/>
  <path d="M0 20V-100" class="a"/>
  <g transform="rotate(-42)"><path d="M0 20q70-34 150-14v-120q-80-20-150 14z" class="teal o"/></g>
</g>
<path d="M420 130q30 60-10 110" class="a" marker-end="url(#ar)"/>
{hand(430,110,-1)}
""", ground=True, arrow=True)

add('dressed', 'コートを着てくつをはき、身支度を終えた人のイラスト。', f"""
<circle cx="470" cy="100" r="56" class="violetp"/>
{person(280,336,1.3,1,'violet','blue','stand','short','smile')}
<g transform="translate(280 250)">
  <path d="M-64-30q64-18 128 0l18 60-26 12-10-24v90h-92v-90l-10 24-26-12z" class="violetd o"/>
  <path d="M0-40v130" fill="none" stroke="{TONES['violet'][1]}" stroke-width="3"/>
  <path d="M-30-32q30 22 60 0" fill="none" stroke="{TONES['violet'][1]}" stroke-width="3"/>
</g>
<g class="coralp o"><path d="M244 208q36-14 72 0l-6 20h-60z"/></g>
<g class="ink"><rect x="240" y="330" width="34" height="16" rx="5"/><rect x="288" y="330" width="34" height="16" rx="5"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M430 300l18 18 30-36"/></g>
""", ground=True)

add('handle', 'なべの取っ手を手で握って、しっかり持ち上げているイラスト。', f"""
<circle cx="480" cy="100" r="56" class="goldp"/>
<g transform="translate(360 280)">
  <path d="M-100-40h200l-14 100h-172z" fill="#dfe6ea" class="o"/>
  <path d="M-100-40h200" class="a"/>
  <path d="M-100-26q-90 0-90 22t90 22" fill="none" stroke="{INK}" stroke-width="15"/>
</g>
{hand(212,276,1)}
<path d="M212 190v46" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('leap', '両足で強くけって、深いみぞの向こう側へ大きく跳び越えるイラスト。', f"""
<path d="M0 320h190v80H0zM410 320h190v80H410z" class="ground"/>
<path d="M190 320h220v80H190z" fill="#5d6b78"/>
<path d="M190 320v80M410 320v80M0 320h190M410 320h190" class="a"/>
{person(300,236,1.05,1,'coral','blue','up','short','neutral')}
<path d="M150 300q120-170 310-30" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('observe', '虫めがねを通して、葉の上の虫をじっくり観察しているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
<g transform="translate(320 290)">
  <path d="M-10 30C-90 22-94-50-2-58 78-52 84 22-10 30z" class="green o"/>
</g>
<g transform="translate(300 200)">
  <circle r="94" fill="#e8f4fb" opacity=".35"/>
  <g transform="scale(0.62)">
    <ellipse cy="40" rx="52" ry="70" class="teal o"/>
    <circle cy="-32" r="30" class="teald o"/>
    <g fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"><path d="M-40 20l-64-22M40 20l64-22M-42 74l-70 32M42 74l70 32"/></g>
    <path d="M-12-56q-20-30-40-34M12-56q20-30 40-34" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  </g>
  <circle r="94" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M66 66l70 70" fill="none" stroke="{INK}" stroke-width="15" stroke-linecap="round"/>
</g>
""", ground=True)

add('cheerful', '明るい表情で手をふっている人のイラスト。まわりに光が差している。', f"""
{sun(480,100,44)}
{person(260,346,1.35,1,'coral','blue','up','bun','smile')}
<g class="golds" style="stroke-width:5"><path d="M140 170l-26-26M380 170l26-26M120 250H90M400 250h30"/></g>
<path d="M60 366h460" class="a"/>
""", ground=True)

add('cooker', '台所の調理器の火の上で、なべを加熱しているイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-170-30h340v100h-340z" fill="#dfe6ea" class="o"/>
  <path d="M-170-30h340" class="a"/>
  <g class="coral o"><circle cx="100" cy="26" r="16"/><circle cx="140" cy="26" r="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><circle cx="-90" cy="-60" r="36"/></g>
</g>
{flame(210,282,0.85)}
<g transform="translate(210 226)">
  <path d="M-74-30h148l-12 56h-124z" fill="#eef4f8" class="o"/>
  <path d="M-88-30h176" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M0-30v-16" class="a"/>
</g>
<g class="muted" opacity=".8"><path d="M190 156q-14-30 4-52M232 152q-14-34 6-56"/></g>
""", ground=True)

add('musician', 'ギターをかまえて演奏している人と、音符が飛び出しているイラスト。', f"""
<circle cx="470" cy="110" r="66" class="violetp"/>
{person(230,346,1.2,1,'violet','blue','carry','bun','smile')}
<g transform="translate(310 266) rotate(-16)">
  <path d="M0-76q46 0 46 40 0 22-16 30 16 10 16 34 0 40-46 40s-46 0-46-40q0-24 16-34-16-8-16-30 0-40 46-40z" class="goldp o"/>
  <circle cy="14" r="20" class="goldd o"/>
  <path d="M-7-76h14v-84h-14z" class="goldd o"/>
  <path d="M-12-160h24v18h-24z" class="ink"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="2"><path d="M-6-140v140M0-140v140M6-140v140"/></g>
</g>
<g fill="{INK}">
  <g transform="translate(410 170)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g>
  <g transform="translate(468 226) scale(0.8)"><ellipse rx="12" ry="9" transform="rotate(-20)"/><path d="M10-4v-42h5v42z"/></g>
</g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('patrol', '懐中電灯を持った警備の人が、決まった道を見回っているイラスト。', f"""
{building(120,290,0.8,'blue')}
{building(490,290,0.8,'blue')}
{person(290,340,1.1,1,'blue','violet','point','cap','neutral')}
<g transform="translate(336 236)">
  <path d="M0-11h44v22H0z" class="goldd o"/>
  <path d="M44-14l90-40v108l-90-40z" class="goldp" opacity=".65"/>
  <path d="M44-14v28" class="a"/>
</g>
<path d="M130 372q80 22 160 0t170 0" class="muted" marker-end="url(#ar)"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
