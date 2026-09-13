"""第106回: 句動詞45語。"""
from lib import *
W=[]
def add(slug,a,b,**k): W.append(emit(slug,a,b,**k))
GRN=TONES['green'][0]
def ck(x,y,s=1,c=GRN): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round" stroke-linejoin="round"><path d="M{x-22*s} {y}l{18*s} {20*s} {32*s}-{40*s}"/></g>'
def xx(x,y,s=1,c=TONES['coral'][0]): return f'<g fill="none" stroke="{c}" stroke-width="{8*s}" stroke-linecap="round"><path d="M{x-20*s} {y-20*s}l{40*s} {40*s}M{x+20*s} {y-20*s}l{-40*s} {40*s}"/></g>'
def house(x,y,s=1,cls='teal'):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-80 0v-80h160V0z" fill="#fffdf6" class="o"/>'
            f'<path d="M-94-80L0-136l94 56z" class="{cls} o"/>'
            f'<path d="M-24-50h48V0h-48z" class="{cls}d o"/></g>')
def scissors(x,y,s=1,r=-16):
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})">'
            f'<path d="M-60-40L40-6" fill="none" stroke="#b9c2c9" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-60 40L40 6" fill="none" stroke="#b9c2c9" stroke-width="9" stroke-linecap="round"/>'
            f'<circle cx="-74" cy="-48" r="18" fill="none" stroke="{TONES["blue"][0]}" stroke-width="8"/>'
            f'<circle cx="-74" cy="48" r="18" fill="none" stroke="{TONES["blue"][0]}" stroke-width="8"/></g>')

add('back-up', '後ろから支えて裏づけるイラスト。', f"""
{person(320,352,1.25,1,'coral','blue','point','short','neutral')}
{person(210,352,1.1,1,'teal','blue','reach','bob','neutral')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="7" marker-end="url(#ar)"><path d="M180 200h90"/></g>
{ck(470,200,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('blow-up', '風船がふくらんでぱんと割れるイラスト。', f"""
<g transform="translate(160 260)">
  <ellipse rx="50" ry="60" class="coralp o"/>
  <path d="M0 60l-12 18h24z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 250h50"/></g>
<g transform="translate(430 240)">
  <path d="M0-140l34 66 72-22-24 68 66 34-66 34 24 68-72-22-34 66-34-66-72 22 24-68-66-34 66-34-24-68 72 22z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('call-off', '予定していた催しを取りやめるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-150h340v300h-340z" class="paper"/>
  <path d="M-130-110h260v80h-260z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-130 {0+i*44}h260"/>' for i in range(3))}</g>
</g>
{xx(300,220,2.4)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('come-up-with', '新しい考えを思いつくイラスト。', f"""
{person(200,352,1.25,1,'teal','blue','up','short','smile')}
<g transform="translate(420 210)">
  <path d="M0-90q58 0 58 56 0 32-26 46v22h-64v-22q-26-14-26-46 0-56 58-56z" class="gold o"/>
  <path d="M-32 34h64v20h-64z" class="goldd o"/>
  <g class="golds"><path d="M-100-40l-30-16M100-40l30-16M0-116v-30"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('cut-out', '紙から形を切り抜くイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <path d="M-70-70h140v140h-140z" fill="#fffaf1" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
{scissors(300,290,1,-20)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('deal-with', '起きた問題に道具を持って当たるイラスト。', f"""
{person(170,352,1.2,1,'teal','blue','reach','cap','neutral')}
<g transform="translate(250 250) rotate(30)">
  <path d="M-8-40h16v80h-16z" fill="{MUTED}" class="o"/>
  <path d="M-18-52h36v20h-36z" fill="{MUTED}" class="o"/>
</g>
<g transform="translate(440 240)">
  <path d="M0-120l100 180h-200z" class="coralp o"/>
  <g fill="{TONES['coral'][2]}"><rect x="-11" y="-50" width="22" height="60" rx="11"/><circle cy="34" r="13"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M300 320h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('find-out', '覆いをめくって突きとめるイラスト。', f"""
<g transform="translate(320 260)">
  <path d="M-120-40h240v130h-240z" class="tealp o"/>
  <circle cx="0" cy="10" r="46" class="coral o"/>
</g>
<g transform="translate(320 140) rotate(-16)">
  <path d="M-140-40h280v60h-280z" class="bluep o"/>
</g>
{hand(520,140,-1)}
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M130 170h26l-6 70h-14zM143 262a13 13 0 1 0 0 26 13 13 0 1 0 0-26z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('get-rid-of', 'いらない物を処分してしまうイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','reach','short','neutral')}
<g transform="translate(450 300)">
  <path d="M-80 0h160l-16 90h-128z" class="tealp o"/>
  <path d="M-90-16h180v16h-180z" class="teal o"/>
</g>
<g transform="translate(310 190)"><path d="M-30-24h60v48h-60z" class="goldd o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M250 220q90-70 170 40"/></g>
{xx(310,110,0.8)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('give-up', '白旗を上げてあきらめるイラスト。', f"""
{person(250,352,1.25,1,'blue','blue','up','short','sad')}
<g transform="translate(310 200)">
  <path d="M-6 60V-70" class="a"/>
  <path d="M-6-70h90v56H-6z" fill="#fffdf6" class="o"/>
</g>
{box(460,350,120,70,0,'gold')}
{xx(460,220,0.9)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('leave-out', 'ひとつだけ外して除くイラスト。', f"""
<g transform="translate(280 250)">
  <g class="teal o">{''.join(f'<circle cx="{-180+i*90}" cy="0" r="34"/>' for i in range(5) if i!=2)}</g>
  <circle cx="0" cy="0" r="34" fill="#fffaf1" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"/>
</g>
<circle cx="500" cy="150" r="34" class="coralp o"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M320 210l140-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('look-back', '後ろを振り返って昔を思うイラスト。', f"""
{person(400,352,1.25,-1,'teal','blue','stand','short','neutral')}
<g transform="translate(160 220)" opacity="0.5">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <path d="M-70 60l50-70 40 40 30-30 40 60z" class="greenp o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M330 240H280"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('look-after', '世話をして面倒を見るイラスト。', f"""
{person(180,352,1.25,1,'violet','violet','reach','bun','smile')}
<g transform="translate(400 320)">
  <path d="M-60-30h120l-16 60h-88z" class="goldp o"/>
  <path d="M0-30v-60" class="greens"/>
  <path d="M0-60q-44-6-50-44 42-6 50 44z" class="greenp o"/>
</g>
{drop(300,200,1.3,'blue')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('look-forward-to', 'その日を楽しみに待つイラスト。', f"""
{person(160,352,1.25,1,'coral','blue','up','short','smile')}
<g transform="translate(410 220)">
  <path d="M-140-130h280v250h-280z" class="paper"/>
  <path d="M-140-130h280v46h-280z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">
    {''.join(f'<path d="M-140 {-40+i*48}h280"/>' for i in range(3))}
    {''.join(f'<path d="M{-100+c*68} -84v204"/>' for c in range(4))}
  </g>
  <circle cx="36" cy="-16" r="24" class="coralp o"/>
</g>
<g fill="{TONES['coral'][0]}" stroke="{TONES['coral'][2]}" stroke-width="2">
  <path d="M250 160q-18-24 0-34 18-10 18 14 0-24 18-14 18 10 0 34l-18 18z"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('make-up', 'いくつかの部分が集まって全体を作るイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-70-60h60v60h-60z" class="tealp o"/>
  <path d="M10-60h60v60H10z" class="coralp o"/>
  <path d="M-70 10h60v60h-60z" class="goldp o"/>
  <path d="M10 10h60v60H10z" class="violetp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('move-in', '荷物を運び込んで住み始めるイラスト。', f"""
{house(430,330,1)}
{person(160,352,1.15,1,'teal','blue','carry','short','smile')}
{box(250,320,90,60,18,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M300 230h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('move-on', '今の所を離れて次へ進むイラスト。', f"""
<g class="ink"><circle cx="140" cy="330" r="18"/><circle cx="470" cy="330" r="18"/></g>
{person(280,352,1.2,1,'teal','blue','walk','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 12" marker-end="url(#ar)"><path d="M180 260h260"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('move-out', '荷物を運び出して引っ越すイラスト。', f"""
{house(150,330,1)}
{person(410,352,1.15,1,'teal','blue','carry','short','neutral')}
{box(320,320,90,60,18,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M240 230h80"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('pass-away', 'ろうそくの火が静かに消えるイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-30 90v-140h60v140z" fill="#fffdf6" class="o"/>
  <path d="M0-50v-20" fill="none" stroke="{MUTED}" stroke-width="5"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-linecap="round">
  <path d="M300 190q-16-26 0-40M330 170q-20-34 0-54"/>
</g>
<g class="coral o"><circle cx="180" cy="350" r="16"/><circle cx="420" cy="350" r="16"/></g>
<g class="greens"><path d="M180 366v22M420 366v22"/></g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('pay-back', '借りたお金を返すイラスト。', f"""
{person(150,352,1.2,1,'teal','blue','give','short','neutral')}
{person(470,352,1.2,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(310 250)">
  <path d="M-60-30h120v60h-120z" class="greenp o"/>
  <circle r="16" class="gold o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 170h160"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('pay-off', '努力が実って報われるイラスト。', f"""
{person(160,352,1.2,1,'teal','blue','reach','short','neutral')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M120 250l-20-30M200 230v-30"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 250h60"/></g>
<g transform="translate(440 260)">
  <path d="M-70-40h140v80h-140z" class="gold o"/>
  <path d="M0-40q-30-30-40-6 20 12 40 6zM0-40q30-30 40-6-20 12-40 6z" class="goldp o"/>
</g>
{ck(440,140,1)}
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('pull-out', '差さっているものを引き抜くイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-26-40h52v100l-26 30-26-30z" class="goldd o"/>
</g>
{hand(300,150,1)}
<g class="a" marker-end="url(#ar)"><path d="M420 250v-80"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="8 8"><path d="M240 300h120"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('put-down', '手に持った物を下に置くイラスト。', f"""
{hand(230,180,1)}
<g transform="translate(400 320)">
  <path d="M-140-20h280v20h-280z" class="goldd o"/>
  <path d="M-110 0v46M110 0v46" class="a"/>
  <path d="M-40-70h80v50h-80z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M310 200l60 60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('put-out', '水をかけて火を消すイラスト。', f"""
{flame(400,330,1.1)}
{person(150,352,1.15,1,'coral','blue','reach','cap','neutral')}
<g transform="translate(230 250)">
  <path d="M-30-20h60v50h-60z" fill="{MUTED}" class="o"/>
  <path d="M30-10h50v20H30z" fill="{MUTED}" class="o"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="9" stroke-linecap="round"><path d="M290 250q60 10 90 50"/></g>
{xx(400,150,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('put-together', 'ばらばらの部品を組み立てるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-60-60h50v50h-50z" class="tealp o" transform="rotate(-14)"/>
  <path d="M10-50h50v50H10z" class="tealp o" transform="rotate(12)"/>
  <path d="M-50 20h50v50h-50z" class="tealp o" transform="rotate(8)"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 240h60"/></g>
<g transform="translate(460 240)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
  <path d="M-60 0h120M0-60v120" class="a"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('put-up', '壁にポスターを掲げるイラスト。', f"""
<g transform="translate(400 210)">
  <path d="M-120-120h240v240h-240z" class="paper"/>
  <path d="M-90-90h180v100h-180z" class="coralp o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5"><path d="M-90 40h180M-90 70h120"/></g>
</g>
{person(160,352,1.2,1,'teal','blue','up','short','neutral')}
<g class="a" marker-end="url(#ar)"><path d="M250 170h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('rule-out', '選択肢から線を引いて外すイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M-190-150h380v300h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5">{''.join(f'<path d="M-140 {-90+i*60}h280"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-150-32h300M-150 88h300"/></g>
</g>
""", ground=False)

add('run-into', '思いがけず人にばったり会うイラスト。', f"""
{person(220,352,1.2,1,'teal','blue','walk','short','surprised')}
{person(390,352,1.2,-1,'coral','gold','walk','bob','surprised')}
<g fill="{TONES['gold'][0]}" stroke="{TONES['gold'][2]}" stroke-width="2.5">
  <path d="M300 130h26l-6 70h-14zM313 222a13 13 0 1 0 0 26 13 13 0 1 0 0-26z"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M250 320h30M360 320h-30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('run-over', '書いたものをざっと目で追うイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-150 {-100+i*48}h300"/>' for i in range(5))}</g>
</g>
<g transform="translate(150 110)">
  <ellipse rx="50" ry="30" fill="#fffdf6" class="o"/>
  <circle r="18" class="blue o"/><circle r="8" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 12" marker-end="url(#ar)">
  <path d="M160 170q120 30 300 40"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('set-aside', '一部をわきに取り分けておくイラスト。', f"""
<g class="gold o">
  {''.join(f'<ellipse cx="{180+ (i%3)*44}" cy="{300-(i//3)*26}" rx="30" ry="13"/>' for i in range(6))}
</g>
<g class="gold o"><ellipse cx="470" cy="320" rx="30" ry="13"/><ellipse cx="470" cy="300" rx="30" ry="13"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="410" y="260" width="120" height="90" rx="14"/></g>
<g class="a" marker-end="url(#ar)"><path d="M330 210h100"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('set-off', '荷物を持って出発するイラスト。', f"""
{house(150,330,0.9)}
{person(340,352,1.2,1,'teal','blue','carry','short','smile')}
<g transform="translate(400 320)"><path d="M-34-26h68v52h-68z" class="goldd o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M420 240h120"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('set-out', '使う物を順に並べておくイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-220-30h440v20h-440z" class="goldd o"/>
  <path d="M-190-10v46M190-10v46" class="a"/>
</g>
<g class="tealp o">{''.join(f'<rect x="{-180+i*90+300}" y="220" width="60" height="50"/>' for i in range(5))}</g>
{hand(120,190,1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8" marker-end="url(#ar)"><path d="M180 210h40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('settle-down', '腰を落ち着けて住みつくイラスト。', f"""
{house(430,330,1)}
{sit(200,352,1.25,1,'teal','blue','short','smile','down')}
{chair(210,356,1.2,'gold',1)}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M290 250h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('shut-down', '機械の電源を落として止めるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-160-130h320v240h-320z" class="ink"/>
  <path d="M-146-116h292v212h-292z" fill="#3a3f4d"/>
  <g fill="none" stroke="{MUTED}" stroke-width="10"><circle r="46"/></g>
  <path d="M0-56v50" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
</g>
<g transform="translate(300 350)"><path d="M-90-20h180v20h-180z" class="ink"/></g>
{xx(490,140,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stand-by', 'すぐ動けるように控えて待つイラスト。', f"""
{person(300,352,1.3,1,'teal','blue','stand','cap','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="12 10"><circle cx="300" cy="250" r="150"/></g>
<g transform="translate(480 200)">
  <circle r="50" fill="#fffdf6" class="o"/>
  <path d="M0 0v-32M0 0l22 14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <circle r="6" class="ink"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stand-for', '旗が国を表すイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-6 110V-110" class="a"/>
  <path d="M-6-110h110v70H-6z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="9"><path d="M270 220h80M270 260h80"/></g>
<g transform="translate(460 250)">
  <path d="M-100 70q0-130 100-130t100 130z" class="greenp o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stick-to', '決めた道を最後まで守り通すイラスト。', f"""
<path d="M240 400q0-140 60-200t60-100h60q0 140-60 200t-60 100z" fill="#dfe6ea" class="o"/>
{person(280,370,1,1,'teal','blue','walk','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"><path d="M300 340q40-120 90-190"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="10 8"><path d="M120 300q60-40 90 20"/></g>
{xx(140,240,0.7,MUTED)}
""", ground=False, arrow=True)

add('take-after', '親に顔つきが似ているイラスト。', f"""
{face(180,210,84,'smile')}
{face(430,220,66,'smile')}
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="8"><path d="M290 200q28-16 56 0M290 236q28-16 56 0"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('take-down', '壁の掲示を外すイラスト。', f"""
<g transform="translate(380 220)">
  <path d="M-130-130h260v260h-260z" class="paper"/>
  <path d="M-100-100h200v110h-200z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
{hand(180,180,1)}
<g transform="translate(210 290) rotate(-16)"><path d="M-60-40h120v80h-120z" class="coralp o"/></g>
<g class="a" marker-end="url(#ar)"><path d="M300 190l-60 60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('take-in', '内容を受け取って頭に入れるイラスト。', f"""
<g transform="translate(160 230)">
  <path d="M-100-110h200v220h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M-66 {-60+i*44}h132"/>' for i in range(4))}</g>
</g>
<g transform="translate(430 230)">
  <path d="M-30 140v-40q-70-16-70-90 0-90 90-90 92 0 92 86 0 44-36 62v72z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 200h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('take-on', '新しい仕事を引き受けるイラスト。', f"""
{person(300,352,1.3,1,'teal','blue','up','short','neutral')}
{box(300,180,190,90,30,'gold')}
<g class="a" marker-end="url(#ar)"><path d="M480 120L370 160"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('take-up', '新しく習い事を始めるイラスト。', f"""
{person(220,352,1.25,1,'teal','blue','carry','short','smile')}
<g transform="translate(330 280) rotate(-18)">
  <ellipse cy="30" rx="56" ry="70" class="goldp o"/>
  <circle cy="20" r="20" class="goldd o"/>
  <path d="M-8-90h16v50h-16z" fill="{TONES['gold'][2]}"/>
  <g fill="none" stroke="{INK}" stroke-width="2"><path d="M-6-40v100M6-40v100"/></g>
</g>
{ck(490,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('turn-around', 'くるりと向きを変えるイラスト。', f"""
{person(220,352,1.2,-1,'teal','blue','stand','short','neutral')}
{person(420,352,1.2,1,'teal','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M260 200q60-60 120 0"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('turn-down', 'つまみを回して音量をさげるイラスト。', f"""
<g transform="translate(200 240)">
  <circle r="80" fill="#fffdf6" class="o"/>
  <path d="M0 0l-56 56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle r="12" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M0 -92v-14" transform="rotate({-90+i*45})"/>' for i in range(5))}</g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-linecap="round">
  <path d="M380 220q16 16 0 32"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round" opacity="0.35">
  <path d="M420 190q40 40 0 92M460 160q64 70 0 152"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M170 130a70 70 0 0 0-60 30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('turn-into', 'まるごと別のものに変わるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-70-70h140v140h-140z" class="tealp o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M280 240h60"/></g>
<g transform="translate(450 240)">
  <circle r="80" class="coral o"/>
</g>
<g class="golds"><path d="M290 160l-20-20M370 160l20-20"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('turn-out', 'ふたを開けて結果が分かるイラスト。', f"""
<g transform="translate(300 270)">
  <path d="M-110-40h220v130h-220z" class="goldd o"/>
  <circle cx="0" cy="20" r="50" class="teal o"/>
</g>
<g transform="translate(300 140) rotate(-20)">
  <path d="M-130-30h260v50h-260z" class="gold o"/>
</g>
{hand(520,130,-1)}
{ck(150,180,1)}
<path d="M60 386h480" class="a"/>
""", ground=True)

print(len(W), ' '.join(W))
print(sheet(W))
