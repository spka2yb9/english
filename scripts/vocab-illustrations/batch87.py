"""第87回: mi〜ob の名詞を中心に45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def gear(x,y,r=60,cls='teal',teeth=8):
    t=''.join(f'<rect x="-12" y="{-r-22}" width="24" height="26" transform="rotate({i*360//teeth})"/>' for i in range(teeth))
    return (f'<g transform="translate({x} {y})"><g class="{cls} o">{t}</g>'
            f'<circle r="{r}" class="{cls} o"/><circle r="{r*0.35:.0f}" fill="#fffdf6" stroke="{INK}" stroke-width="3"/></g>')

add('miner', 'つるはしで地下を掘る鉱夫のイラスト。', f"""
<path d="M0 120h600v280H0z" fill="#5e4a3c"/>
<path d="M60 200q90-70 200-50t200 50v170H60z" fill="#7a6252"/>
{person(230,330,1.2,1,'gold','blue','reach','cap','neutral')}
<g transform="translate(340 200) rotate(28)">
  <path d="M-8-10h16v120h-16z" fill="{TONES['gold'][2]}"/>
  <path d="M-70-16q70-26 140 0-70 16-140 0z" fill="#b9c2c9" stroke="{INK}" stroke-width="3"/>
</g>
<circle cx="230" cy="200" r="14" class="gold"/>
<g class="golds"><path d="M244 190l30-14M244 210l30 14"/></g>
""", ground=False)

add('mineral', '岩の中の結晶した鉱物のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-190 90q-30-90 30-140 70-56 170-30 90 24 70 100-20 74-140 80-100 4-130-10z" fill="#8b98a6" class="o"/>
</g>
<g transform="translate(250 230)">
  <path d="M-60-20h120l-30 90h-60z" class="tealp o"/>
  <path d="M-60-20l30-40h60l30 40z" class="teal o"/>
  <path d="M-30-60l-30 40 30 90M30-60l30 40-30 90" fill="none" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(400 270)">
  <path d="M-36-14h72l-18 54h-36z" class="goldp o"/>
  <path d="M-36-14l18-26h36l18 26z" class="gold o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('minimum', 'これ以上は下がらない下限のイラスト。', f"""
<g transform="translate(300 240)">
  <g class="teal o">{''.join(f'<rect x="{-200+i*80}" y="{-20-i*30}" width="56" height="{80+i*30}"/>' for i in range(5))}</g>
  <path d="M-210 60h420v20h-420z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M550 160v130"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('minister', '国の役所を代表して話す大臣のイラスト。', f"""
{person(200,352,1.3,1,'violet','blue','point','short','neutral')}
<g transform="translate(280 330)">
  <path d="M-40-30h80v50h-80z" class="goldd o"/>
  <path d="M-14-40h28v10h-28z" class="a" fill="none"/>
</g>
{building(460,320,0.85,'teal')}
<path d="M460 200v-40" class="a"/>
<path d="M460 160h60v34h-60z" class="coral o"/>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('ministry', '国の役所が入る大きな庁舎のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-230 0h460v20h-460z" class="teald o"/>
  <path d="M-200-200h400v200h-400z" fill="#fffdf6" class="o"/>
  <g class="tealp o">{''.join(f'<rect x="{-170+c*70}" y="{-180+r*60}" width="46" height="40"/>' for r in range(3) for c in range(5))}</g>
  <path d="M-200-200h400v24h-400z" class="teal o"/>
  <path d="M-40 0v-56h80V0z" class="teald o"/>
</g>
<path d="M300 100v-40" class="a"/>
<path d="M300 60h70v34h-70z" class="coral o"/>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('minority', '全体の中のごく少ない側のイラスト。', f"""
{person(110,336,0.75,1,'teal','blue','stand','short','neutral')}
{person(180,336,0.75,1,'teal','blue','stand','bob','neutral')}
{person(250,336,0.75,1,'teal','blue','stand','short','neutral')}
{person(320,336,0.75,1,'teal','blue','stand','bun','neutral')}
{person(390,336,0.75,1,'teal','blue','stand','short','neutral')}
{person(490,336,0.85,-1,'coral','gold','stand','bob','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><rect x="440" y="200" width="110" height="170" rx="20"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('miracle', '枯れた枝に一夜で花が咲く奇跡のイラスト。', f"""
<g transform="translate(150 320)">
  <path d="M0 0v-120M0-70l-40-40M0-40l40-40" fill="none" stroke="#8a7a63" stroke-width="10" stroke-linecap="round"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 240h60"/></g>
<g transform="translate(430 320)">
  <path d="M0 0v-120M0-70l-40-40M0-40l40-40" fill="none" stroke="#8a7a63" stroke-width="10" stroke-linecap="round"/>
  <g class="coralp o"><circle cx="0" cy="-124" r="20"/><circle cx="-42" cy="-114" r="18"/><circle cx="42" cy="-84" r="18"/></g>
  <g class="gold"><circle cx="0" cy="-124" r="7"/><circle cx="-42" cy="-114" r="6"/><circle cx="42" cy="-84" r="6"/></g>
</g>
<g class="golds"><path d="M430 130v-30M340 170l-22-22M530 170l22-22"/></g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('misery', '雨の中でうずくまるみじめさのイラスト。', f"""
{cloud(280,90,1.5,'blue')}
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="5" stroke-linecap="round">
  {''.join(f'<path d="M{180+i*32} {170+(i%3)*16}l-14 50"/>' for i in range(8))}
</g>
{sit(300,352,1.25,1,'blue','blue','short','sad','down')}
<g transform="translate(420 340)">
  <path d="M-40-14h80q0 30-40 30t-40-30z" fill="#fffdf6" class="o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('mission', '果たすべき使命に向かって進むイラスト。', f"""
{person(160,352,1.15,1,'teal','blue','walk','cap','neutral')}
<g transform="translate(250 250)">
  <path d="M-36-46h72v92h-72z" class="paper"/>
  <g fill="none" stroke="{GRN}" stroke-width="4"><path d="M-20-24l6 8 14-16M-20 0l6 8 14-16"/></g>
</g>
<g transform="translate(490 250)">
  <path d="M-6 106V-90" class="a"/>
  <path d="M-6-90h90l-18 26 18 26H-6z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M300 330h140"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('mob', '大勢が押し寄せる群衆のイラスト。', f"""
{person(110,352,0.9,1,'coral','blue','up','short','sad')}
{person(190,352,0.95,1,'gold','violet','up','bob','sad')}
{person(270,352,1,1,'coral','gold','up','cap','sad')}
{person(350,352,0.95,1,'violet','blue','up','short','sad')}
{person(430,352,0.9,1,'green','blue','up','bun','sad')}
{person(510,352,0.85,1,'coral','violet','up','short','sad')}
<g class="a" marker-end="url(#ar)"><path d="M100 110h420"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('mode', '切りかえで働き方が変わる方式のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-120h400v240h-400z" fill="#fffdf6" class="o"/>
  <path d="M-140-40h280v80h-280z" fill="#dfe6ea" class="o"/>
  <circle cx="-70" cy="0" r="26" class="tealp o"/>
  <circle cx="0" cy="0" r="26" class="tealp o"/>
  <circle cx="70" cy="0" r="26" class="coral o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="8 7"><circle cx="70" cy="0" r="44"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 150h40M300 150h40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('modification', '一部を作り変えて直す修正のイラスト。', f"""
<g transform="translate(150 240)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
  <path d="M-40-30h80v60h-80z" class="teal o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M260 240h60"/></g>
<g transform="translate(450 240)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
  <circle r="44" class="coral o"/>
</g>
<g transform="translate(340 340) rotate(-30)">
  <path d="M-8-40h16v80h-16z" fill="{MUTED}" class="o"/>
  <path d="M-18-52h36v20h-36z" fill="{MUTED}" class="o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('momentum', '転がるほどに勢いを増すイラスト。', f"""
<path d="M60 130L520 350H60z" class="greenp o"/>
<circle cx="160" cy="200" r="20" class="tealp o"/>
<circle cx="290" cy="262" r="30" class="teal o"/>
<circle cx="450" cy="330" r="44" class="teald o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-linecap="round">
  <path d="M110 190h-30M110 210h-40M238 250h-40M238 274h-50M394 316h-50M394 344h-60"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('monopoly', '一社だけが市場をすべて握る独占のイラスト。', f"""
<g transform="translate(230 210)">
  <circle r="140" class="teal o"/>
  <circle r="46" fill="#fffdf6" class="o"/>
</g>
{tower(230,220,0.4,'blue',3)}
{person(470,352,0.9,-1,'coral','gold','stand','short','sad')}
{person(540,352,0.9,-1,'gold','violet','stand','bob','sad')}
{xx(500,180,1)}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('monster', '大きな牙と角を持つ怪物のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-140 110q-40-100 0-160 40-62 140-62t140 62q40 60 0 160z" class="green o"/>
  <path d="M-90-140l-26-60 60 34zM90-140l26-60-60 34z" class="greend o"/>
  <circle cx="-56" cy="-60" r="30" fill="#fffdf6" class="o"/>
  <circle cx="56" cy="-60" r="30" fill="#fffdf6" class="o"/>
  <circle cx="-50" cy="-56" r="13" class="ink"/><circle cx="62" cy="-56" r="13" class="ink"/>
  <path d="M-80 20q80 60 160 0z" fill="#fffdf6" class="o"/>
  <path d="M-56 26l14 26 16-26zM24 26l14 26 16-26z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('monument', '広場に立つ記念像のイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-130 0h260v26h-260z" class="teald o"/>
  <path d="M-90-70h180v70h-180z" fill="#dfe6ea" class="o"/>
  <path d="M-40-260l40-40 40 40v190h-80z" fill="#cdd6dd" class="o"/>
  <path d="M-40-170h80" class="a"/>
</g>
<g class="greenp o"><circle cx="130" cy="330" r="24"/><circle cx="470" cy="330" r="24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('mortgage', '家を担保に借りて毎月返す住宅ローンのイラスト。', f"""
<g transform="translate(160 300)">
  <path d="M-70 0v-80h140V0z" fill="#fffdf6" class="o"/>
  <path d="M-84-80L0-134l84 54z" class="coral o"/>
  <path d="M-20-50h40V0h-40z" class="corald o"/>
</g>
{tower(460,320,0.6,'blue',4)}
<g class="a" marker-end="url(#ar)"><path d="M290 160h100"/></g>
<g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M390 250H280"/></g>
<g class="gold o"><ellipse cx="330" cy="300" rx="26" ry="11"/><ellipse cx="330" cy="284" rx="26" ry="11"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True, arrow=True)

add('mosque', '丸屋根と塔のあるモスクのイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-160 0v-120h320V0z" fill="#fffdf6" class="o"/>
  <path d="M-160-120q160-140 320 0z" class="teal o"/>
  <path d="M-40 0v-70q0-40 40-40t40 40V0z" class="tealp o"/>
  <path d="M-110-70q0-40 34-40t34 40z" class="tealp o"/>
  <path d="M42-70q0-40 34-40t34 40z" class="tealp o"/>
</g>
<g transform="translate(140 330)">
  <path d="M-24 0v-170h48V0z" fill="#fffdf6" class="o"/>
  <path d="M-30-170q30-50 60 0z" class="teal o"/>
</g>
<g transform="translate(460 330)">
  <path d="M-24 0v-170h48V0z" fill="#fffdf6" class="o"/>
  <path d="M-30-170q30-50 60 0z" class="teal o"/>
</g>
<path d="M300 190v-30" class="a"/>
<path d="M300 130a30 30 0 1 0 20 52 34 34 0 1 1-20-52z" class="gold o"/>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('motion', '残像を引きながら動いているイラスト。', f"""
<circle cx="420" cy="220" r="60" class="teal o"/>
<circle cx="300" cy="220" r="60" class="tealp o" opacity="0.6"/>
<circle cx="190" cy="220" r="60" class="tealp o" opacity="0.3"/>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round">
  <path d="M80 180h60M60 220h70M80 260h60"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 340h380"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('motivation', '胸の中の火に押されて前へ進むイラスト。', f"""
{person(200,352,1.25,1,'teal','blue','walk','short','smile')}
{flame(200,266,0.55)}
<g transform="translate(500 250)">
  <path d="M-6 106V-70" class="a"/>
  <path d="M-6-70h80l-16 24 16 24H-6z" class="gold o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M300 330h150"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True, arrow=True)

add('motive', '行いの裏にある動機のイラスト。', f"""
{person(200,352,1.2,1,'violet','blue','reach','short','neutral')}
<g transform="translate(390 300)">
  <path d="M-70-30h140v60h-140z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
<g transform="translate(300 130)">
  <path d="M-100-50q-6-40 30-44 14-30 46-18 26-4 32 24 30 4 26 34-4 26-32 26h-70q-28-2-32-22z" class="bluep o"/>
  <circle cx="0" cy="-16" r="22" class="gold o"/>
</g>
<g class="o" fill="#e1edfb"><circle cx="230" cy="200" r="13"/><circle cx="212" cy="228" r="9"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('motor', '軸を回して力を出すモーターのイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-130-80h260v160h-260z" class="bluep o"/>
  <g fill="none" stroke="{TONES['blue'][2]}" stroke-width="8">{''.join(f'<path d="M{-100+i*40} -80v160"/>' for i in range(6))}</g>
  <path d="M130-20h90v40h-90z" fill="{MUTED}" class="o"/>
  <path d="M-130-30h-40v60h40z" class="blued o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)">
  <path d="M480 190a44 44 0 1 1-30 76"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('myth', '神殿と雷で語られる神話のイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-170 0h340v22h-340z" class="goldd o"/>
  <g class="goldp o">{''.join(f'<rect x="{-150+i*60}" y="-130" width="40" height="130"/>' for i in range(5))}</g>
  <path d="M-170-130h340v26h-340z" class="gold o"/>
  <path d="M-190-156L0-220l190 64z" class="gold o"/>
</g>
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M300 40l-44 82h34l-24 66 64-90h-38l28-58z"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True)

add('naturally', '手を加えなくてもひとりでに育つイラスト。', f"""
{sun(490,90,40)}
<g transform="translate(300 340)">
  <path d="M0 0v-120" class="greens"/>
  <path d="M0-60q-44-6-50-44 42-6 50 44zM0-84q44-6 50-44-42-6-50 44z" class="greenp o"/>
</g>
{drop(200,120,1.4,'blue')}
{drop(390,150,1.2,'blue')}
{hand(110,250,1)}
{xx(200,250,0.8,MUTED)}
<path d="M60 346h480" class="a"/>
""", ground=True)

add('necessarily', '必ずしもそうとは限らないイラスト。', f"""
<g transform="translate(300 200)">
  <g class="teal o">{''.join(f'<circle cx="{-200+i*80}" cy="0" r="34"/>' for i in range(5))}</g>
  <path d="M166-34h68v68h-68z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 280v40"/></g>
{xx(300,360,0.9)}
""", ground=False, arrow=True)

add('necessity', 'これがないと生きられない必需品のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-56-60h112v40h-112z" class="bluep o"/>
  <path d="M-46-20h92l-10 100h-72z" class="blue o"/>
</g>
<g transform="translate(400 260)">
  <path d="M-70-40h140l-16 110h-108z" class="goldp o"/>
  <path d="M-70-40q70-40 140 0z" class="gold o"/>
</g>
<g fill="none" stroke="{GRN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"><path d="M280 130l18 20 34-42"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="90" y="150" width="420" height="200" rx="26"/></g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('negative', 'そうではないと打ち消す否定のイラスト。', f"""
<g transform="translate(300 210)">
  <circle r="130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="24"/>
  <path d="M-70 0h140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="24" stroke-linecap="round"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M520 130v130"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('negotiation', '条件を出し合って折り合う交渉のイラスト。', f"""
{person(140,352,1.1,1,'teal','blue','point','short','neutral')}
{person(470,352,1.1,-1,'coral','gold','point','bob','neutral')}
<g transform="translate(300 320)">
  <path d="M-140-20h280v20h-280z" class="goldd o"/>
  <path d="M-110 0v40M110 0v40" class="a"/>
</g>
<g transform="translate(230 260)"><path d="M-40-30h80v50h-80z" class="paper"/></g>
<g transform="translate(370 260)"><path d="M-40-30h80v50h-80z" class="paper"/></g>
<g class="a" marker-end="url(#ar)"><path d="M240 180h40M360 180h-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('nerve', '信号を伝える神経のイラスト。', f"""
<g transform="translate(180 210)">
  <circle r="56" class="goldp o"/>
  <circle r="20" class="gold o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="6" stroke-linecap="round">
    <path d="M-40-40l-40-30M-56 10l-50 10M-30 46l-30 44M30-50l24-40"/>
  </g>
</g>
<path d="M236 210q60 40 120 0t120 0" fill="none" stroke="{TONES['gold'][0]}" stroke-width="16" stroke-linecap="round"/>
<g class="coral o"><circle cx="300" cy="232" r="16"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M330 150h80"/></g>
<g transform="translate(520 210)">
  <path d="M-30-40h60v80h-60z" class="tealp o"/>
</g>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('newsletter', '定期に配られる会報のイラスト。', f"""
<g transform="translate(260 210)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <path d="M-160-140h320v56h-320z" class="teal o"/>
  <path d="M-130-60h140v90h-140z" class="tealp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">
    <path d="M30-60h100M30-34h100M30-8h100M30 18h80M-130 56h260M-130 82h260M-130 108h200"/>
  </g>
</g>
<g transform="translate(500 300)">
  <path d="M-70-46h140v92h-140z" fill="#fffdf6" class="o"/>
  <path d="M-70-46L0 10l70-56" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('niche', '壁のくぼみにぴたりと収まる場所のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-250-160h500v320h-500z" fill="#dfe6ea" class="o"/>
  <path d="M-70 160v-180q0-70 70-70t70 70v180z" fill="#fffaf1" class="o"/>
  <path d="M-40 160v-140q0-40 40-40t40 40v140z" class="tealp o"/>
</g>
<circle cx="300" cy="240" r="34" class="teal o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><circle cx="300" cy="240" r="56"/></g>
""", ground=False)

add('nightmare', '眠りの中で見る恐ろしい夢のイラスト。', f"""
<path d="M0 0h600v400H0z" fill="#2c2f3d"/>
<g transform="translate(220 330)">
  <path d="M-130-30h260v60h-260z" fill="#48506a" class="o"/>
  <path d="M-100-60h90v30h-90z" fill="#dfe6ea" class="o"/>
  <circle cx="-58" cy="-76" r="24" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-40-30h150v-18q0-12-14-12H-30q-14 0-14 12z" fill="#6f7a99" class="o"/>
</g>
<g fill="#3b4157" stroke="#8b98a6" stroke-width="3">
  <path d="M420 90q-60 40-40 110 16 56 80 56t80-56q20-70-40-110-30-20-40-40-10 20-40 40z"/>
</g>
<g fill="{TONES['coral'][0]}"><circle cx="440" cy="180" r="9"/><circle cx="500" cy="180" r="9"/></g>
<g fill="none" stroke="#8b98a6" stroke-width="3"><circle cx="330" cy="240" r="14"/><circle cx="300" cy="270" r="9"/></g>
""", ground=False)

add('nomination', '候補として名前を推し上げるイラスト。', f"""
{person(170,352,1.15,1,'teal','blue','up','short','smile')}
<g transform="translate(200 180)">
  <path d="M-56-40h112v70h-112z" class="paper"/>
  <circle cx="-20" cy="-6" r="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M8-12h34M8 6h34"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 180h80"/></g>
<g transform="translate(470 220)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-56-60h112M-56-20h112M-56 20h112M-56 60h80"/></g>
  <g fill="none" stroke="{GRN}" stroke-width="6"><path d="M-70-66l10 12 20-24"/></g>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('nominee', '候補に選ばれて壇上に立つ人のイラスト。', f"""
<path d="M300 60l150 300H150z" fill="{TONES['gold'][1]}" opacity="0.6"/>
{person(300,340,1.3,1,'coral','blue','stand','bun','smile')}
<g transform="translate(300 250)">
  <path d="M-40-20l30 40h-30zM40-20l-30 40h30z" class="coral o"/>
  <circle cy="34" r="26" class="gold o"/>
</g>
{person(110,352,0.75,1,'teal','blue','stand','short','neutral')}
{person(510,352,0.75,-1,'green','violet','stand','bob','neutral')}
<path d="M60 380h480" class="a"/>
""", ground=True)

add('noon', '太陽が真上に来る正午のイラスト。', f"""
{sun(300,90,52)}
<g transform="translate(300 250)">
  <circle r="110" fill="#fffdf6" class="o"/>
  <path d="M0 0v-80" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>
  <path d="M0 0v-70" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"/>
  <circle r="8" class="ink"/>
  <g fill="{INK}">{''.join(f'<rect x="-4" y="-102" width="8" height="18" transform="rotate({a})"/>' for a in range(0,360,30))}</g>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('norm', 'たいていの人がそろう標準のイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-240-20h480v6h-480z" fill="{TONES['teal'][0]}"/>
</g>
{person(130,240,0.75,1,'teal','blue','stand','short','neutral')}
{person(230,240,0.75,1,'teal','blue','stand','bob','neutral')}
{person(330,240,0.75,1,'teal','blue','stand','short','neutral')}
{person(430,240,0.75,1,'teal','blue','stand','bun','neutral')}
{person(530,290,0.75,1,'coral','gold','stand','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="8 8"><path d="M60 240h480"/></g>
<path d="M60 316h480" class="a"/>
""", ground=True)

add('nostalgia', '古い写真を眺めて懐かしむイラスト。', f"""
{person(180,352,1.2,1,'violet','blue','hold','bun','smile')}
<g transform="translate(430 230)">
  <path d="M-140-110h280v220h-280z" class="paper" transform="rotate(-4)"/>
  <g transform="rotate(-4)">
    <path d="M-110-80h250v130h-250z" class="goldp o"/>
    <circle cx="70" cy="-46" r="24" class="gold o"/>
    <path d="M-110 50l70-70 60 50 50-40 70 60z" class="greenp o"/>
  </g>
</g>
<g class="golds"><path d="M300 130l-20-20M560 130l20-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('notebook', 'リング留めのノートのイラスト。', f"""
<g transform="translate(310 210)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <path d="M-170-150h34v300h-34z" class="coralp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-110 {-100+i*44}h240"/>' for i in range(6))}</g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="7">{''.join(f'<circle cx="140" cy="{100+i*44}" r="13"/>' for i in range(6))}</g>
""", ground=False)

add('nursery', 'おもちゃの並ぶ保育の部屋のイラスト。', f"""
<g transform="translate(300 200)">
  <path d="M-250-160h500v320h-500z" fill="#fffdf6" class="o"/>
  <path d="M-250 140h500" class="a"/>
</g>
{person(180,338,0.65,1,'gold','coral','up','short','smile')}
{person(280,338,0.65,1,'teal','blue','up','bob','smile')}
{person(380,338,0.65,-1,'violet','green','up','short','smile')}
<circle cx="470" cy="320" r="26" class="coralp o"/>
<g transform="translate(120 310)">
  <path d="M-30 30h60v-30h-60z" class="tealp o"/>
  <path d="M-20 0h40v-30h-40z" class="goldp o"/>
  <path d="M-10-30h20v-24h-20z" class="violetp o"/>
</g>
<path d="M60 350h480" class="a"/>
""", ground=False)

add('nursing', 'ベッドの人を世話する看護のイラスト。', f"""
<g transform="translate(230 300)">
  <path d="M-130 20h260v16h-260z" class="ink"/>
  <path d="M-130-20h260v40h-260z" fill="#fffdf6" class="o"/>
  <path d="M-130-56h50v36h-50z" class="bluep o"/>
  <ellipse cx="-96" cy="-66" rx="20" ry="16" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <path d="M-76-20h190v-22q0-14-16-14H-60q-16 0-16 14z" class="tealp o"/>
</g>
{person(470,346,1.1,-1,'coral','violet','reach','bun','smile')}
<g transform="translate(470 216)">
  <path d="M-10-30h20v20h20v20h-20v20h-20v-20h-20v-20h20z" class="coral o"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('nutrition', 'いろいろな食品からとる栄養のイラスト。', f"""
<g transform="translate(300 250)">
  <circle r="150" fill="#fffdf6" class="o"/>
  <circle r="120" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M0 0v-120A120 120 0 0 1 104 60z" class="greenp o"/>
  <path d="M0 0l104 60A120 120 0 0 1-104 60z" class="coralp o"/>
  <path d="M0 0l-104 60A120 120 0 0 1 0-120z" class="goldp o"/>
  <circle cx="50" cy="-40" r="20" class="green o"/>
  <circle cx="0" cy="66" r="20" class="coral o"/>
  <circle cx="-50" cy="-40" r="20" class="gold o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('obligation', '果たさなければならない義務のイラスト。', f"""
{person(190,352,1.2,1,'teal','blue','stand','short','neutral')}
<g transform="translate(450 250)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-56-70h112M-56-40h112M-56-10h112M-56 20h80"/></g>
  <circle cx="40" cy="70" r="26" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="8">
  <circle cx="260" cy="290" r="18"/><circle cx="300" cy="290" r="18"/><circle cx="340" cy="290" r="18"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('observation', 'じっと見て記録する観察のイラスト。', f"""
{person(180,352,1.15,1,'teal','blue','hold','cap','neutral')}
<g transform="translate(180 236)">
  <path d="M-44-20h40v40h-40zM4-20h40v40H4z" class="ink"/>
  <circle cx="-24" cy="0" r="12" class="bluep"/><circle cx="24" cy="0" r="12" class="bluep"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M230 236h160"/></g>
<g transform="translate(460 240)">
  <ellipse rx="60" ry="40" class="goldp o"/>
  <circle cx="44" cy="-30" r="26" class="goldp o"/>
  <path d="M64-36l26 8-26 12z" class="gold o"/>
  <circle cx="52" cy="-36" r="4" class="ink"/>
  <path d="M-30 40v34M20 42v32" fill="none" stroke="{TONES['gold'][2]}" stroke-width="9" stroke-linecap="round"/>
</g>
<path d="M60 376h480" class="a"/>
""", ground=True)

add('observer', '加わらず外から見ている人のイラスト。', f"""
{person(180,340,0.85,1,'teal','blue','up','short','smile')}
{person(260,340,0.85,-1,'gold','violet','up','bob','smile')}
{person(340,340,0.85,1,'green','blue','up','short','smile')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10"><circle cx="260" cy="250" r="140"/></g>
{person(520,352,1,-1,'violet','blue','hold','bun','neutral')}
<g transform="translate(520 240)">
  <path d="M-40-16h34v34h-34zM6-16h34v34H6z" class="ink"/>
</g>
<path d="M60 380h480" class="a"/>
""", ground=True)

add('obsession', '同じことばかりが頭を離れない執着のイラスト。', f"""
{person(200,352,1.2,1,'blue','blue','think','short','neutral')}
<g transform="translate(400 190)">
  <circle r="120" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12"/>
  <circle cx="0" cy="-120" r="30" class="coral o"/>
  <circle cx="104" cy="60" r="30" class="coral o"/>
  <circle cx="-104" cy="60" r="30" class="coral o"/>
</g>
<g class="o" fill="#e1edfb"><circle cx="268" cy="212" r="14"/><circle cx="246" cy="244" r="9"/></g>
<path d="M60 380h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
