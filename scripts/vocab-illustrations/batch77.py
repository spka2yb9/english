"""第77回: 相関・危機・通貨・締め切りなど45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('correlation', '二つの量がともに増える関係のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100h340M-170-110v210" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="{INK}"><circle cx="-140" cy="70" r="8"/><circle cx="-80" cy="30" r="8"/><circle cx="-20" cy="0" r="8"/><circle cx="40" cy="-40" r="8"/><circle cx="110" cy="-80" r="8"/></g>
  <path d="M-160 90L140-90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 9"/>
</g>
""", ground=True)

add('correspondence', '手紙をやりとりする文通のイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','give','short','smile')}
{person(470,346,1.1,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(300 200)">
  <path d="M-60-40h120v80h-120z" class="paper"/>
  <path d="M-60-40l60 46 60-46" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 150q70-40 140 0M370 290q-70 40-140 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('correspondent', '現地から様子を伝える特派員のイラスト。', f"""
{person(180,346,1.15,1,'coral','blue','reach','bob','neutral')}
<g transform="translate(240 250)">
  <path d="M-6-10h44v20h-44z" class="ink"/>
  <circle cx="46" r="18" fill="#7f8ea6" stroke="{INK}" stroke-width="2"/>
</g>
{building(430,300,0.7,'teal')}
<g class="corals" style="stroke-width:5"><path d="M320 200q26 20 26 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('corruption', '裏金で仕組みがゆがむイラスト。', f"""
{person(160,346,1.1,1,'violet','blue','give','cap','flat')}
<g transform="translate(300 290)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="16" class="goldd o"/>
</g>
{person(450,346,1.1,-1,'blue','blue','reach','short','flat')}
<g transform="translate(300 170)">
  <path d="M-70-40h140v70h-140z" class="paper"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-40-20l80 40M40-20l-80 40"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('counselling', '向かい合って相談を受けるイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M-90-20h180v26h-180z" class="goldd o"/>
</g>
{person(180,330,1.1,1,'coral','gold','stand','bob','sad')}
{person(430,330,1.1,-1,'blue','blue','reach','short','smile')}
<g transform="translate(300 190)">
  <path d="M-70-40h140v60h-140z" fill="#fffdf6" class="o"/>
  <path d="M20 20l14 26-34-26z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{MUTED}"><circle cx="-26" cy="-10" r="7"/><circle cx="0" cy="-10" r="7"/><circle cx="26" cy="-10" r="7"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('counsellor', '相談に応じて助言する相談員のイラスト。', f"""
{person(400,346,1.2,-1,'blue','blue','point','short','smile')}
{person(180,346,1.15,1,'coral','gold','think','bob','neutral')}
<g transform="translate(300 190)">
  <path d="M-80-50h160v80h-160z" fill="#fffdf6" class="o"/>
  <path d="M40 30l14 30-40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M-50-20h60M-50 4h80"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('counter', '店の受け渡し台のイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-200-40h400v50h-400z" class="goldd o"/>
  <path d="M-200 10h400v80h-400z" class="goldp o"/>
  <path d="M-200-40h400v-16h-400z" fill="#fffdf6" class="o"/>
</g>
{person(400,240,0.9,-1,'blue','blue','reach','bob','smile')}
{person(180,346,0.95,1,'coral','gold','reach','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('county', '地図の中の郡の区画のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-200-40h400M-200 50h400M-70-140v280M70-140v280"/></g>
  <path d="M-70-40h140v90h-140z" class="tealp o"/>
  <path d="M-70-40h140v90h-140z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
</g>
<path d="M500 130l-120 60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('coup', '力で政権が突然入れかわるイラスト。', f"""
<g transform="translate(170 250)" opacity=".4">
  <path d="M-60-80h120v160h-120z" class="tealp o"/>
  <g transform="translate(0 -110)"><path d="M-30 16l-6-34 18 14 18-24 18 24 18-14-6 34z" class="gold o"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M130 170l80 80M210 170l-80 80"/></g>
<g transform="translate(430 250)">
  <path d="M-60-80h120v160h-120z" class="coralp o"/>
  <g transform="translate(0 -110)"><path d="M-30 16l-6-34 18 14 18-24 18 24 18-14-6 34z" class="gold o"/></g>
</g>
<path d="M280 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('courage', '恐ろしいものに立ち向かう勇気のイラスト。', f"""
<g transform="translate(450 250)">
  <path d="M-90 110q-20-170 90-170t90 170z" fill="#41506a"/>
  <g fill="{TONES['coral'][0]}"><path d="M-40-40l30 20-30 20zM40-40l-30 20 30 20z"/></g>
</g>
{person(180,346,1.25,1,'coral','blue','stand','short','neutral')}
{flame(180,180,0.9)}
<path d="M270 220h70" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('courtesy', 'ていねいな作法でふるまうイラスト。', f"""
<g transform="translate(230 346) rotate(22)">{person(0,0,1.25,1,'blue','blue','give','short','smile')}</g>
{person(470,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M110 180l20 20 34-40"/></g>
<path d="M320 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('craft', '手仕事で器をこしらえるイラスト。', f"""
{hand(200,180,1)}
<g transform="translate(320 280)">
  <path d="M-70-60q70-30 140 0 10 60-70 70t-70-70z" fill="#c9a06b" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#8b5e3c" stroke-width="3"><path d="M-56-30q56-20 112 0M-50 10q50-16 100 0"/></g>
</g>
<g transform="translate(320 340)"><ellipse rx="90" ry="16" fill="#dfe6ea" class="o"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('creation', '何もない所から作り出すイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-70-70h140v140h-140z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g transform="translate(430 240)">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
  <g class="golds" style="stroke-width:5"><path d="M-90-90l-22-18M90-90l22-18"/></g>
</g>
<path d="M280 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('creativity', '思いつきが次々に形になるイラスト。', f"""
{person(170,346,1.15,1,'violet','blue','think','bob','smile')}
<g transform="translate(420 190)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g class="coralp o"><circle cx="-60" r="26"/></g>
  <g class="tealp o"><rect x="-10" y="-26" width="52" height="52"/></g>
  <g class="goldp o"><path d="M70 26l30-52 30 52z"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="280" cy="290" r="12"/><circle cx="256" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('creator', '作品を作り出した人のイラスト。', f"""
{person(180,346,1.2,1,'violet','blue','reach','bob','smile')}
<g transform="translate(420 240)">
  <path d="M-110-110h220v220h-220z" class="goldd o"/>
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <path d="M-60 60l60-90 40 40 50-60 40 110z" class="green o"/>
</g>
<path d="M270 240h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('creature', '見なれない生き物のイラスト。', f"""
<g transform="translate(300 250)">
  <ellipse rx="100" ry="70" class="greenp o"/>
  <g fill="{INK}"><circle cx="-30" cy="-20" r="12"/><circle cx="30" cy="-20" r="12"/></g>
  <g fill="#fffdf6"><circle cx="-26" cy="-24" r="4"/><circle cx="34" cy="-24" r="4"/></g>
  <path d="M-30 20q30 24 60 0" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="5"><path d="M-40-70l-16-30M40-70l16-30"/></g>
  <g class="greenp o"><rect x="-60" y="60" width="30" height="40"/><rect x="30" y="60" width="30" height="40"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('credit', '信用でつけ買いができるカードのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-170-100h340v200h-340z" class="tealp o"/>
  <path d="M-170-60h340v40h-340z" fill="#41506a"/>
  <g class="goldd o"><rect x="-130" y="10" width="60" height="44"/></g>
  <g fill="{TONES['teal'][2]}"><rect x="-40" y="30" width="180" height="14"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('crisis', '線が急落して危機に陥るイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100h340" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-170-60q80-20 120 0t60 140" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9"/>
  <path d="M10 80q60 20 160 20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="9"/>
</g>
<g transform="translate(500 130)"><path d="M0-40l40 70h-80z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/><g fill="{INK}"><rect x="-4" y="-10" width="8" height="24"/><rect x="-4" y="18" width="8" height="8"/></g></g>
""", ground=True)

add('criterion', '合否を分ける基準の線を示したイラスト。', f"""
<path d="M60 346h480" class="a"/>
<g class="tealp o"><rect x="110" y="180" width="70" height="166"/><rect x="200" y="230" width="70" height="116"/></g>
<g class="coralp o"><rect x="330" y="270" width="70" height="76"/><rect x="420" y="250" width="70" height="96"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-dasharray="14 10"><path d="M90 240h430"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M120 150l14 14 24-30"/></g>
""", ground=False)

add('criticism', '作品に赤で批判を書き込むイラスト。', f"""
<g transform="translate(290 230)">
  <path d="M-160-130h320v260h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-120 {-80+i*40}h240"/>' for i in range(5))}</g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M-130-86h100"/><path d="M-30-46h140"/><path d="M-130 34h80"/></g>
</g>
<g transform="translate(500 320) rotate(28)"><path d="M-10-80h20v110h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('critique', '作品を評して良い点と悪い点を示すイラスト。', f"""
<g transform="translate(200 240)">
  <path d="M-90-90h180v180h-180z" fill="#fffdf6" class="o"/>
  <path d="M-60 60l50-70 40 40 40-50 30 80z" class="green o"/>
</g>
<g transform="translate(440 240)">
  <path d="M-80-90h160v180h-160z" class="paper"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-56-60l12 12 20-24"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-56 0l24 24M-32 0l-24 24"/></g>
  <g fill="{MUTED}"><rect x="-16" y="-56" width="80" height="12"/><rect x="-16" y="4" width="80" height="12"/></g>
</g>
<path d="M310 240h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('crop', '畑に育つ作物のイラスト。', f"""
<g fill="#8b6f4e"><path d="M60 320h480v60H60z"/></g>
<g transform="translate(160 300)">
  <path d="M0 20V-60" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
  <g class="gold o">{''.join(f'<ellipse cx="{-14 if i%2 else 14}" cy="{-60-i*20}" rx="14" ry="9" transform="rotate({-24 if i%2 else 24} {-14 if i%2 else 14} {-60-i*20})"/>' for i in range(4))}</g>
</g>
<g transform="translate(300 300)">
  <path d="M0 20V-60" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
  <g class="gold o">{''.join(f'<ellipse cx="{-14 if i%2 else 14}" cy="{-60-i*20}" rx="14" ry="9" transform="rotate({-24 if i%2 else 24} {-14 if i%2 else 14} {-60-i*20})"/>' for i in range(4))}</g>
</g>
<g transform="translate(440 300)">
  <path d="M0 20V-60" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
  <g class="gold o">{''.join(f'<ellipse cx="{-14 if i%2 else 14}" cy="{-60-i*20}" rx="14" ry="9" transform="rotate({-24 if i%2 else 24} {-14 if i%2 else 14} {-60-i*20})"/>' for i in range(4))}</g>
</g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('crown', '宝石をあしらった王冠のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-140 80l-24-160 76 56 88-100 88 100 76-56-24 160z" class="gold o"/>
  <path d="M-150 80h300v40h-300z" class="goldd o"/>
  <g fill="{TONES['coral'][0]}"><circle cx="-70" cy="20" r="16"/><circle cx="0" cy="6" r="16"/><circle cx="70" cy="20" r="16"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('cue', '合図を出して始めさせるイラスト。', f"""
{person(160,346,1.1,1,'blue','blue','point','short','neutral')}
<g transform="translate(300 220)">
  <circle r="34" class="coral o"/>
  <g class="corals" style="stroke-width:5"><path d="M-50-50l-20-16M50-50l20-16"/></g>
</g>
{person(460,346,1.15,1,'coral','gold','walk','bob','smile')}
<path d="M350 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('cult', '一人を熱狂的に囲んで崇めるイラスト。', f"""
{person(300,300,1.2,1,'violet','violet','up','short','neutral')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><circle cx="300" cy="250" r="150"/></g>
{person(150,346,0.85,1,'gold','blue','up','bob','smile')}
{person(450,346,0.85,-1,'gold','blue','up','cap','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('curiosity', '虫めがねでのぞきこんで知りたがるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','reach','bob','smile')}
<g transform="translate(340 210) rotate(24)">
  <circle r="66" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <path d="M0 66v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<g fill="{INK}" transform="translate(470 150)">
  <path d="M0 0q0-26 20-26t20 26q0 14-14 18v12h-12v-20q14-4 14-14t-8-8-8 12z"/><rect x="12" y="42" width="12" height="12"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('currency', '国ごとの通貨のイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-110-70h220v140h-220z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="34" fill="#d5e6c4" stroke="{TONES['green'][2]}" stroke-width="3"/>
</g>
<g transform="translate(420 260)">
  <circle r="60" class="goldd o"/>
  <circle r="44" fill="#e5b56b" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-20" y="-6" width="40" height="12"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('curriculum', '学期ごとに学ぶ内容を並べた課程のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-200+c*100}-140v280"/>' for c in range(1,4))}<path d="M-200-80h400"/></g>
  <g fill="{INK}"><rect x="-180" y="-120" width="60" height="14"/><rect x="-80" y="-120" width="60" height="14"/><rect x="20" y="-120" width="60" height="14"/><rect x="120" y="-120" width="60" height="14"/></g>
  <g class="tealp o"><rect x="-180" y="-60" width="60" height="40"/><rect x="-80" y="0" width="60" height="40"/><rect x="20" y="-60" width="60" height="40"/><rect x="120" y="60" width="60" height="40"/></g>
</g>
""", ground=True)

add('dairy', '牛乳とチーズの乳製品のイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-50-70h100v140h-100z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M-50-70l50-40 50 40z" fill="#e8f4fb" stroke="{INK}" stroke-width="3"/>
  <g class="bluep o"><rect x="-34" y="-20" width="68" height="50"/></g>
</g>
<g transform="translate(420 280)">
  <path d="M-80 40h160l-20-80h-120z" fill="#f3c94f" stroke="{INK}" stroke-width="3"/>
  <g fill="#e0b43c"><circle cx="-20" cy="10" r="10"/><circle cx="30" cy="-6" r="8"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('dam', '川をせき止めるダムのイラスト。', f"""
<path d="M60 200h240v180H60z" class="bluep o"/>
<g fill="#c9d3dc" stroke="{INK}" stroke-width="3"><path d="M300 160h60v220h-60z"/></g>
<path d="M360 300h180v80H360z" class="bluep o"/>
<g fill="none" stroke="#fffdf6" stroke-width="5" opacity=".8"><path d="M360 300q40-20 80 0t80 0"/></g>
<g class="a" marker-end="url(#ar)"><path d="M120 250h140"/></g>
""", ground=False, arrow=True)

add('darkness', '灯りのない暗さのイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#1f2b3d"/>
<g fill="#2b3a52"><circle cx="300" cy="210" r="150"/></g>
<g opacity=".5">{person(300,346,1.1,1,'blue','blue','stand','short','neutral')}</g>
<g fill="#3b4a63"><rect x="60" y="330" width="480" height="50"/></g>
""", ground=False)

add('database', '記録がそろって並ぶ台帳のイラスト。', f"""
<g transform="translate(300 230)">
  <g fill="#dfe6ea" stroke="{INK}" stroke-width="3">
    <ellipse cy="-110" rx="130" ry="34"/>
    <path d="M-130-110v70a130 34 0 0 0 260 0v-70z"/>
    <path d="M-130-40v70a130 34 0 0 0 260 0v-70z"/>
    <path d="M-130 30v70a130 34 0 0 0 260 0V30z"/>
  </g>
  <g fill="{TONES['teal'][0]}"><circle cx="90" cy="-70" r="8"/><circle cx="90" cy="0" r="8"/><circle cx="90" cy="70" r="8"/></g>
</g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('dawn', '空が白んで夜が明けるイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#f8e2c8"/>
<g fill="#f7d0a8"><path d="M0 0h600v200H0z"/></g>
<g class="green o" opacity=".85"><path d="M0 300q150-30 300-10t300-20v130H0z"/></g>
<g fill="#f3c94f"><circle cx="300" cy="300" r="70"/></g>
<g fill="none" stroke="#f3c94f" stroke-width="5">{''.join(f'<path d="M300 300l{int(130*__import__("math").cos((i+1)*3.14159/7+3.14159))} {int(130*__import__("math").sin((i+1)*3.14159/7+3.14159))}"/>' for i in range(6))}</g>
""", ground=False)

add('deadline', 'カレンダーの締め切り日が迫るイラスト。', f"""
<g transform="translate(270 220)">
  <path d="M-180-130h360v260h-360z" class="paper"/>
  <path d="M-180-130h360v50h-360z" class="coral o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-180+c*90}-80v210"/>' for c in range(1,4))}{''.join(f'<path d="M-180 {-10+r*70}h360"/>' for r in range(2))}</g>
  <circle cx="90" cy="25" r="30" fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"/>
</g>
<g transform="translate(500 130)">
  <circle r="44" fill="#fffdf6" class="o"/>
  <path d="M0-28v28l20 12" fill="none" stroke="{INK}" stroke-width="5"/>
</g>
""", ground=True)

add('debris', '壊れた破片が散らばるがれきのイラスト。', f"""
<g fill="#b6bfc9" stroke="{INK}" stroke-width="3">
  <path d="M120 330l50-60 30 60z"/><path d="M200 330l60-40 20 40z"/><path d="M300 330l50-70 40 70z"/><path d="M400 330l40-50 50 50z"/>
</g>
<g fill="#8b98a6"><rect x="180" y="300" width="80" height="14" transform="rotate(-12 220 307)"/><rect x="330" y="310" width="90" height="12" transform="rotate(8 375 316)"/></g>
<g class="muted" opacity=".9"><path d="M300 260q30-40 0-70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('debt', '返さなければならない借りがあるイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','stand','short','sad')}
<g transform="translate(400 240)">
  <path d="M-100-90h200v180h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-70" y="-60" width="120" height="16"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-20h140M-70 10h100"/></g>
  <g class="goldd o"><circle cx="60" cy="50" r="20"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 300h-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('debut', '初めて舞台に出るイラスト。', f"""
<g transform="translate(300 140)">
  <path d="M-200-60h400v40h-400z" class="coral o"/>
  <path d="M-200-20h60q10 100 0 160h-60z" class="coralp o"/>
  <path d="M140-20h60v160h-60q-10-60 0-160z" class="coralp o"/>
</g>
<g transform="translate(300 250) scale(0.95)">{person(0,60,1.0,1,'violet','gold','up','bob','smile')}</g>
<g class="golds" style="stroke-width:5"><path d="M200 200l-24-18M400 200l24-18"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="260" r="110"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('decade', '十年ごとの区切りを示したイラスト。', f"""
<path d="M60 250h480" fill="none" stroke="{MUTED}" stroke-width="5"/>
<g class="teal o">{''.join(f'<circle cx="{100+i*44}" cy="250" r="14"/>' for i in range(10))}</g>
<g class="a" marker-end="url(#ar)"><path d="M100 340h396M496 340H100"/></g>
""", ground=False, arrow=True)

add('deck', '船の甲板のイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<g transform="translate(300 260)">
  <path d="M-200 40h400l-40 40h-320z" class="tealp o"/>
  <path d="M-190 10h380v30h-380z" class="goldd o"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="3">{''.join(f'<path d="M{-170+i*44} 10v30"/>' for i in range(9))}</g>
  <g fill="none" stroke="{INK}" stroke-width="4"><path d="M-170 10v-40M-90 10v-40M-10 10v-40M70 10v-40M150 10v-40M-190-30h380"/></g>
</g>
{person(300,270,0.7,1,'blue','blue','stand','cap','smile')}
""", ground=False)

add('declaration', '広く宣言を告げるイラスト。', f"""
{person(180,346,1.25,1,'violet','blue','up','short','neutral')}
<g transform="translate(410 220)">
  <path d="M-110-100h220v200h-220z" class="paper"/>
  <g fill="{INK}"><rect x="-80" y="-70" width="160" height="20"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-20h160M-80 20h120"/></g>
  <g transform="translate(60 60)"><circle r="22" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/></g>
</g>
<g class="corals" style="stroke-width:5"><path d="M260 180q26 20 26 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('decoration', '飾りをつけて彩るイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-160-40h320v20h-320z" class="ink"/>
  <g class="coralp o"><circle cx="-110" cy="20" r="26"/></g>
  <g class="tealp o"><circle cx="-40" cy="30" r="26"/></g>
  <g class="goldp o"><circle cx="30" cy="18" r="26"/></g>
  <g class="violetp o"><circle cx="100" cy="32" r="26"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="2"><path d="M-110-20v14M-40-20v24M30-20v12M100-20v26"/></g>
</g>
{person(140,346,0.8,1,'teal','blue','up','short','smile')}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('dedication', 'ひとつの道にすべてを注ぐイラスト。', f"""
<g transform="translate(170 220)">
  <circle r="90" fill="#fffdf6" class="o"/>
  <path d="M0 0v-90A90 90 0 1 1-64 64z" class="teal o"/>
  <circle r="90" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(430 240)">
  <path d="M-80-70h160v140h-160z" class="tealp o"/>
  <g fill="{TONES['teal'][2]}"><rect x="-50" y="-40" width="100" height="20"/><rect x="-50" y="0" width="70" height="20"/></g>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
<g class="golds" style="stroke-width:5"><path d="M520 150l24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('deed', '行いが記録として残るイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','give','short','smile')}
<g transform="translate(410 230)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-60h160M-80-20h160M-80 20h120"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round"><path d="M-100-66l14 14 22-26"/></g>
  <g transform="translate(60 70)"><circle r="22" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/></g>
</g>
<path d="M270 280h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('default', '初期の設定に戻すイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-190-120h380v240h-380z" fill="#dfe6ea" class="o"/>
  <g fill="#fffdf6" stroke="{INK}" stroke-width="3"><rect x="-140" y="-70" width="280" height="30"/><rect x="-140" y="-20" width="280" height="30"/><rect x="-140" y="30" width="280" height="30"/></g>
  <g class="teal o"><rect x="-140" y="-70" width="100" height="30"/><rect x="-140" y="-20" width="100" height="30"/><rect x="-140" y="30" width="100" height="30"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M480 340a60 60 0 0 1-30-50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('defect', '一つだけ欠陥のある品を見つけるイラスト。', f"""
<g class="tealp o">{''.join(f'<rect x="{100+i*70}" y="220" width="52" height="80"/>' for i in range(6))}</g>
<g transform="translate(326 260)">
  <path d="M-26-40h52v80h-52z" class="coralp o"/>
  <path d="M-10-40l10 30-16 24 14 26" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><rect x="290" y="205" width="72" height="110"/></g>
<path d="M326 150v40" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
