"""第62回: 改善・保険・招待・講義など44語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('impatient', '時計を何度も見て、待ちきれないイラスト。', f"""
{person(200,346,1.25,1,'coral','blue','point','short','flat')}
<g transform="translate(430 200)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <path d="M0-44v44l34 18" fill="none" stroke="{INK}" stroke-width="7"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M330 150l24-18M336 190h28"/></g>
<g fill="{MUTED}"><ellipse cx="230" cy="366" rx="26" ry="8"/><ellipse cx="270" cy="374" rx="20" ry="7"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('impressed', '見事なものを見て、感心するイラスト。', f"""
{person(170,346,1.2,1,'teal','blue','up','short','smile')}
<g transform="translate(430 230)">
  <path d="M-110-110h220v220h-220z" fill="#fffdf6" class="o"/>
  <path d="M0-70l26 52 58 6-42 40 12 58-54-30-54 30 12-58-42-40 58-6z" class="gold o"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M270 160l-26-20M280 200h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('impressive', '目をひく立派な出来ばえのイラスト。', f"""
<g transform="translate(320 250)">
  <path d="M-160 100h320v-180h-320z" fill="#f4ead2" class="o"/>
  <path d="M-180-80l180-110 180 110z" class="teal o"/>
  <g class="goldp o"><rect x="-120" y="-40" width="60" height="140"/><rect x="-30" y="-40" width="60" height="140"/><rect x="60" y="-40" width="60" height="140"/></g>
</g>
{person(120,346,0.7,1,'coral','blue','up','short','surprised')}
<g class="golds" style="stroke-width:5"><path d="M500 130l24-18M510 170h28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('improvement', '線が右上へ伸びて、良くなっていくイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100h340M-170-110v210" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-150 70q80-10 140-60t140-70" fill="none" stroke="{TONES['teal'][0]}" stroke-width="8" marker-end="url(#ar)"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 370l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('inadequate', '必要な線に届かず、足りないイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-90-130h180v260h-180z" fill="#f7fbfe" class="o"/>
  <path d="M-90 60h180v70h-180z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 8"><path d="M-130-40h260"/></g>
  <path d="M-90-130h180v260h-180z" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M420 200v-40"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 300l30 30M500 300l-30 30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('inappropriate', '場にふさわしくない服装を示したイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-80-80h160v70h-160z" class="coralp o"/>
  <path d="M-50-10h100v100h-100z" class="coralp o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-90-100h180v200h-180z" fill="#f4ead2" class="o"/>
  <path d="M-60-60h120v40h-120z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60 0h120M-60 40h90"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M170 140l40 40M210 140l-40 40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('including', '袋の中に、それも一緒に入っているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-100h320v200h-320z" fill="none" stroke="{INK}" stroke-width="5"/>
  <g class="tealp o"><circle cx="-100" cy="-30" r="30"/><circle cx="-20" cy="20" r="30"/><circle cx="60" cy="-40" r="30"/></g>
  <g class="coral o"><circle cx="110" cy="40" r="30"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="410" cy="280" r="52"/></g>
<path d="M480 160l-50 70" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('incorrect', '答えが違っていて、×がつくイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-100" width="100" height="14"/><rect x="-60" y="-40" width="100" height="14"/><rect x="-120" y="0" width="220" height="6"/><rect x="-60" y="30" width="100" height="14"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M70 20l60 60M130 20l-60 60"/></g>
</g>
""", ground=True)

add('indifferent', '差し出されても、興味なく目もくれないイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(300 250)"><path d="M-50-40h100v80h-100z" class="gold o"/></g>
{person(470,346,1.2,1,'violet','blue','stand','bob','flat')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M500 200h50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M370 170l28 28M398 170l-28 28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('indigenous', 'その土地に元から住む人と、あとから来た人を分けたイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-230-140h460v280h-460z" class="paper"/>
  <path d="M-230 20q120-40 230 0t230-20v140h-460z" class="green o"/>
</g>
{person(180,320,1.0,1,'gold','coral','stand','bob','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 180l18 18 30-36"/></g>
<g opacity=".5">{person(450,320,1.0,-1,'blue','blue','walk','short','neutral')}</g>
<path d="M540 250h-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('inevitable', '道が一本しかなく、避けられないイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-240-140h140v280h-140zM100-140h140v280H100z" fill="#c9d3dc" class="o"/>
</g>
{person(160,300,0.95,1,'teal','blue','walk','short','flat')}
<path d="M230 250h140" class="a" marker-end="url(#ar)"/>
<g transform="translate(430 250)"><path d="M0-60l60 120h-120z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/><g fill="{INK}"><rect x="-6" y="-14" width="12" height="40"/><rect x="-6" y="36" width="12" height="12"/></g></g>
<path d="M60 396h480" class="a"/>
""", ground=True, arrow=True)

add('inherent', '生まれつき、内側に備わっているイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="140" class="tealp o"/>
  <circle r="140" fill="none" stroke="{TONES['teal'][2]}" stroke-width="4"/>
  <g transform="translate(0 0)"><path d="M0-50l16 32 36 4-26 26 8 36-34-18-34 18 8-36-26-26 36-4z" class="gold o"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="220" r="70"/></g>
<path d="M500 130l-100 60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('injury', '転んで足をけがしたイラスト。', f"""
<g transform="translate(280 300) rotate(-70)">{person(0,0,1.15,1,'coral','blue','stand','short','sad')}</g>
<g transform="translate(370 330)">
  <path d="M-30-24h60v48h-60z" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/>
  <path d="M-10-24h20v48h-20z" fill="#fffdf6"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M420 280q24 6 30 26M420 250q34 0 50 20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('inner', '外側の輪の内側にある部分を示したイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="140" fill="none" stroke="{INK}" stroke-width="6"/>
  <circle r="80" class="teal o"/>
</g>
<path d="M470 100l-120 70" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('innovative', '今までにない形を新しく作り出すイラスト。', f"""
<g class="tealp o"><rect x="90" y="220" width="80" height="100"/><rect x="190" y="220" width="80" height="100"/></g>
<g transform="translate(430 260)">
  <path d="M-70 60q0-120 70-120t70 120z" class="coral o"/>
  <g class="golds" style="stroke-width:5"><path d="M-90-80l-24-20M90-80l24-20M0-100v-26"/></g>
</g>
<path d="M300 260h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('instant', 'ボタンを押した瞬間にでき上がるイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-70-50h140v100h-140z" fill="#dfe6ea" class="o"/>
  <circle r="26" class="coral o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-70-70h140l-14 140h-112z" fill="#f7fbfe" class="o"/>
  <path d="M-60-20h120l-10 90h-100z" class="goldp o"/>
  <g class="muted"><path d="M-20-90q20-30 0-50M20-90q20-30 0-50"/></g>
</g>
<path d="M270 250h60" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:6"><path d="M300 170l-10-30M330 190l30-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('instead', '一方をやめて、代わりにもう一方を選ぶイラスト。', f"""
<g transform="translate(170 240)" opacity=".4">
  <path d="M-70-70h140v140h-140z" class="tealp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M130 200l80 80M210 200l-80 80"/></g>
<g transform="translate(430 240)">
  <path d="M-70-70h140v140h-140z" class="coral o"/>
</g>
<path d="M270 240h60" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('insufficient', '人数に対して席が足りていないイラスト。', f"""
<g transform="translate(300 300)">
  <g class="goldd o"><rect x="-200" y="-20" width="120" height="20"/><rect x="-60" y="-20" width="120" height="20"/></g>
</g>
{person(140,300,0.8,1,'teal','blue','stand','short','neutral')}
{person(280,300,0.8,1,'coral','gold','stand','bob','neutral')}
{person(430,346,0.9,1,'gold','blue','stand','cap','sad')}
{person(520,346,0.9,1,'violet','blue','stand','short','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M450 180l30 30M480 180l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('insurance', '万一の損に備えて、傘のように守るイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-160 0q0-100 160-100t160 100z" class="violetp o"/>
  <path d="M-6 0h12v120h-12z" class="ink"/>
</g>
<g transform="translate(300 320)">
  <path d="M-70-30h140v60h-140z" class="goldd o"/>
</g>
<g class="muted" opacity=".9">{''.join(f'<path d="M{110+i*70} 60l-14 40"/>' for i in range(7))}</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('intact', '包みを解いても、傷ひとつないイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-80-70h160v140h-160z" class="goldp o"/>
  <path d="M-12-70h24v140h-24z" class="coral o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 360l20 20 34-40"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('integrated', 'ばらばらの部品が一つにまとまるイラスト。', f"""
<g transform="translate(160 240)">
  <g class="tealp o" ><rect x="-60" y="-60" width="50" height="50" transform="rotate(-10 -35 -35)"/><rect x="10" y="-50" width="50" height="50" transform="rotate(12 35 -25)"/><rect x="-40" y="20" width="50" height="50" transform="rotate(6 -15 45)"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="3"><path d="M0-70v140M-70 0h140"/></g>
</g>
<path d="M280 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('intense', '光と熱が強烈に押し寄せるイラスト。', f"""
{sun(300,200,80)}
<g class="corals" opacity=".9" style="stroke-width:8">
  <path d="M300 40v-0M120 200h-40M480 200h40M300 340v40M170 70l-28-28M430 70l28-28M170 330l-28 28M430 330l28 28"/>
</g>
{person(120,346,0.8,1,'coral','blue','up','short','flat')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('intensive', '短い期間に集中して詰め込むイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-190-130h380v260h-380z" class="paper"/>
  <path d="M-190-130h380v50h-380z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-190+c*95}-80v210"/>' for c in range(1,4))}{''.join(f'<path d="M-190 {-10+r*70}h380"/>' for r in range(2))}</g>
  <g class="coral o"><rect x="-180" y="-70" width="80" height="55"/><rect x="-85" y="-70" width="80" height="55"/><rect x="10" y="-70" width="80" height="55"/><rect x="-180" y="0" width="80" height="55"/><rect x="-85" y="0" width="80" height="55"/></g>
</g>
""", ground=True)

add('intention', 'こうするつもりだと的を見定めるイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','short','neutral')}
<g transform="translate(450 220)">
  <circle r="70" fill="#fffdf6" class="o"/>
  <circle r="46" class="coralp o"/>
  <circle r="20" class="coral o"/>
</g>
<path d="M240 240h130" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"/>
<g transform="translate(230 150)">
  <path d="M-50-40h100v56h-100z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="4" marker-end="url(#ar)"><path d="M-26-14h50"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('interactive', '画面と人がやりとりして進むイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','reach','short','smile')}
<g transform="translate(410 240)">
  <path d="M-120-110h240v220h-240z" fill="#dfe6ea" class="o"/>
  <path d="M-96-86h192v172h-192z" class="bluep o"/>
  <g fill="#fffdf6"><rect x="-60" y="-40" width="120" height="24"/><rect x="-60" y="10" width="80" height="24"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M240 200h50M290 280h-50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('interim', '本番までのあいだをつなぐ、仮の置きかえのイラスト。', f"""
<g class="tealp o"><rect x="100" y="200" width="100" height="130"/><rect x="400" y="200" width="100" height="130"/></g>
<g transform="translate(300 265)">
  <path d="M-50-65h100v130h-100z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 9"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M110 380h380"/></g>
<path d="M300 150v30" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('intermediate', '初級と上級のあいだの段を示したイラスト。', f"""
<g class="tealp o"><rect x="110" y="280" width="100" height="60"/><rect x="390" y="140" width="100" height="200"/></g>
<rect x="250" y="210" width="100" height="130" class="coral o"/>
<path d="M300 150v40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('intimate', '身を寄せて小声で語り合う、親密なイラスト。', f"""
{person(250,346,1.2,1,'teal','blue','reach','short','smile')}
{person(360,346,1.2,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(305 180)">
  <path d="M-60-40h120v56h-120z" fill="#fffdf6" class="o"/>
  <path d="M-20 16l-12 26 34-26z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{MUTED}"><circle cx="-26" cy="-12" r="7"/><circle cx="0" cy="-12" r="7"/><circle cx="26" cy="-12" r="7"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('invitation', '招待状を受け取るイラスト。', f"""
<g transform="translate(320 230)">
  <path d="M-130-90h260v180h-260z" class="paper"/>
  <path d="M-130-90l130 100 130-100" fill="none" stroke="{INK}" stroke-width="3"/>
  <g class="coralp o"><rect x="-60" y="20" width="120" height="50"/></g>
  <g fill="{INK}"><rect x="-40" y="38" width="80" height="14"/></g>
</g>
{hand(140,300,1)}
<path d="M200 300h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('involved', '輪の中に加わって、関わっているイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><circle cx="300" cy="240" r="150"/></g>
{person(200,320,0.85,1,'teal','blue','give','short','smile')}
{person(400,320,0.85,-1,'coral','gold','give','bob','smile')}
{person(300,180,0.85,1,'gold','blue','give','cap','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('ironic', '雨の日に日傘を差すような、皮肉なイラスト。', f"""
<g class="muted" opacity=".9">{''.join(f'<path d="M{120+i*60} 90l-14 40"/>' for i in range(7))}</g>
<g transform="translate(300 200)">
  <path d="M-110 0q0-70 110-70t110 70z" class="goldp o"/>
  <path d="M-4 0h8v100h-8z" class="ink"/>
</g>
{sun(500,110,22)}
{person(300,346,1.0,1,'teal','blue','stand','short','flat')}
<g fill="{INK}" transform="translate(120 200)">
  <path d="M0 0q0-26 20-26t20 26q0 14-14 18v12h-10v-20q14-4 14-14t-8-8-8 12z"/><rect x="12" y="42" width="10" height="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('isolated', 'ぽつんと一軒だけ離れて立つイラスト。', f"""
<g class="green o" opacity=".8"><path d="M0 330q150-40 300-20t300-10v100H0z"/></g>
<g transform="translate(430 280)">
  <path d="M-70 50h140V-20h-140z" fill="#f4ead2" class="o"/>
  <path d="M-90-20l90-60 90 60z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><circle cx="430" cy="270" r="130"/></g>
<g opacity=".4">{building(120,320,0.6,'teal')}</g>
<g class="muted"><path d="M200 250h100"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('journey', '長い道を、いくつも越えて進む旅のイラスト。', f"""
<path d="M80 340q100-60 180 0t180-60 100 20" fill="none" stroke="#e6dcc9" stroke-width="16"/>
{person(160,320,0.9,1,'coral','blue','carry','cap','smile')}
{tree(320,320,0.6)}
<g fill="#b9c8d6"><path d="M470 260l90 80H380z"/></g>
<path d="M240 250h180" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('judge', '法廷で判断を下す裁判官のイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160-40h320v50h-320z" class="goldd o"/>
  <path d="M-140 10h280v60h-280z" class="goldp o"/>
</g>
<g transform="translate(300 190) scale(0.95)">{person(0,60,1.0,1,'violet','violet','stand','short','neutral')}</g>
<g transform="translate(430 200)">
  <path d="M-6-40h12v50h-12z" class="ink"/>
  <path d="M-60-40h120v8h-120z" class="ink"/>
  <g class="goldp o"><path d="M-60-32l-24 34h48z"/><path d="M60-32l-24 34h48z"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('just', '天びんが水平で、公正なことを示すイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-6-40h12v60h-12z" class="ink"/>
  <path d="M-170 20h340" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-170 20v50M170 20v50" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(130 260)"><circle r="34" class="teal o"/></g>
<g transform="translate(470 260)"><circle r="34" class="teal o"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M280 340l20 20 34-40"/></g>
""", ground=False)

add('keyboard', 'キーを打って文字を入れるイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-200-50h400v100h-400z" fill="#dfe6ea" class="o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="2">{''.join(f'<rect x="{-180+c*45}" y="{-36+r*30}" width="38" height="24"/>' for r in range(3) for c in range(8))}</g>
</g>
{hand(300,160,1)}
<path d="M300 200v30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('killing', '命が絶たれることを、消えた灯で示したイラスト。', f"""
<g transform="translate(180 250)">
  {flame(180,250,1.2)}
</g>
<g transform="translate(430 250)">
  <path d="M-40 90h80l-10-60h-60z" fill="#dfe6ea" class="o"/>
  <g class="muted"><path d="M0-20q20-40 0-60"/></g>
</g>
<path d="M280 250h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M420 130l30 30M450 130l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('knowledge', '頭の中に本の中身が積み上がるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(430 200)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g class="tealp o"><rect x="-60" y="10" width="120" height="20"/><rect x="-50" y="-14" width="100" height="20"/><rect x="-40" y="-38" width="80" height="20"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="290" cy="300" r="12"/><circle cx="266" cy="324" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('label', '品にラベルを貼って表示するイラスト。', f"""
<g transform="translate(280 260)">
  <path d="M-90-100h180l-10 200h-160z" fill="#e7f6fb" stroke="{INK}" stroke-width="3"/>
  <path d="M-70-20h140v70h-140z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-50" y="0" width="100" height="12"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50 24h80"/></g>
</g>
{hand(470,230,-1)}
<path d="M420 230h-40" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('latter', '二つ並ぶうち、後ろのほうを指すイラスト。', f"""
<g transform="translate(180 240)"><path d="M-90-70h180v140h-180z" class="tealp o"/></g>
<g transform="translate(430 240)"><path d="M-90-70h180v140h-180z" class="coral o"/></g>
<path d="M430 120v40" class="a" marker-end="url(#ar)"/>
<g class="a" marker-end="url(#ar)"><path d="M120 350h360"/></g>
""", ground=False, arrow=True)

add('laziness', 'やることを放って、寝転がっているイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-160-20h320v40h-320z" class="goldd o"/>
  <g transform="translate(-40 -60) rotate(-90)">{person(0,0,1.0,1,'teal','blue','stand','short','smile')}</g>
</g>
<g transform="translate(460 260)">
  <path d="M-70-70h140v140h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-30h80M-40 0h80M-40 30h60"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-60-60h20v20h-20z"/></g>
</g>
<g fill="{MUTED}" transform="translate(230 180)">
  <path d="M0-20h30l-30 26h30" fill="none" stroke="{MUTED}" stroke-width="4"/>
  <path d="M44-50h24l-24 22h24" fill="none" stroke="{MUTED}" stroke-width="4"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('lean', '体を斜めに傾けて、柱に寄りかかるイラスト。', f"""
<g transform="translate(400 250)"><path d="M-20-140h40v280h-40z" fill="#c9d3dc" class="o"/></g>
<g transform="translate(320 346) rotate(16)">{person(0,0,1.25,1,'teal','blue','stand','short','smile')}</g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M300 350V180"/></g>
<path d="M240 200a80 80 0 0 1 30-40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('leather', 'なめし革の表面と、革の靴のイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-90-80h180v160h-180z" fill="#a8724a" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#8b5e3c" stroke-width="3"><path d="M-60-40q40 20 80 0M-60 0q40 20 80 0M-60 40q40 20 80 0"/></g>
</g>
<g transform="translate(430 290)">
  <path d="M-90 40h180q10-40-30-50l-40-40h-60q-20 40-50 50z" fill="#a8724a" stroke="{INK}" stroke-width="3"/>
  <path d="M-30-30h60v20h-60z" fill="#8b5e3c"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('lecture', '教壇から大勢に講義するイラスト。', f"""
<g transform="translate(430 200)">
  <path d="M-150-110h300v190h-300z" fill="#31473d" class="o"/>
  <g fill="none" stroke="#e9f3ec" stroke-width="4"><path d="M-110-60h180M-110-20h220M-110 20h150"/></g>
</g>
<g transform="translate(160 300)">
  <path d="M-60-20h120v90h-120z" class="goldd o"/>
  <path d="M-70-36h140v16h-140z" class="goldp o"/>
</g>
<g transform="translate(160 200)">{person(0,60,1.0,1,'violet','blue','point','short','neutral')}</g>
{person(300,346,0.65,1,'teal','gold','stand','bob','smile')}
{person(380,346,0.65,1,'coral','blue','stand','short','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('leftover', '食べ残しが皿に残っているイラスト。', f"""
<g transform="translate(170 260)">
  <ellipse rx="110" ry="34" fill="#fffdf6" class="o"/>
  <g class="coralp o"><path d="M-40-20q40-16 80 0 0 20-40 20t-40-20z"/></g>
  <g class="greenp o"><circle cx="30" cy="6" r="14"/></g>
</g>
<g transform="translate(430 260)">
  <ellipse rx="110" ry="34" fill="#fffdf6" class="o"/>
  <g class="coralp o"><circle cx="-30" cy="-6" r="12"/></g>
  <g class="greenp o"><circle cx="20" cy="4" r="9"/></g>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="430" cy="250" r="60"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('length', '棒の長さを目盛りで測るイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-200-30h400v60h-400z" class="teal o"/>
</g>
<g transform="translate(300 300)">
  <path d="M-200-24h400v48h-400z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<path d="M{-180+i*40}-24v{16 if i%2 else 26}"/>' for i in range(10))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 380h400M500 380H100"/></g>
""", ground=False, arrow=True)

add('lengthy', 'いつまでも終わらない長い文書のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-140-160h280v300h-280z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-120+i*26}h200"/>' for i in range(10))}</g>
</g>
<g transform="translate(300 370)">
  <path d="M-140-30h280v60h-280z" class="paper" opacity=".7"/>
  <g class="muted"><path d="M-40 40h80"/></g>
</g>
<path d="M480 120v240" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
