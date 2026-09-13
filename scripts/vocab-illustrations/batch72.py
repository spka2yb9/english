"""第72回: 獲得・同盟・分析・怒りなど45語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('accused', '法廷で訴えられた側の人を示したイラスト。', f"""
<g transform="translate(300 130)">
  <path d="M-90 40h180v20h-180z" class="goldd o"/>
  <path d="M-6-60h12v100h-12z" class="ink"/>
  <path d="M-70-60h140v10h-140z" class="ink"/>
  <g class="goldp o"><path d="M-70-50l-24 34h48z"/><path d="M70-50l-24 34h48z"/></g>
</g>
{person(420,346,1.2,-1,'violet','violet','stand','cap','sad')}
<circle cx="420" cy="280" r="90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
{person(160,346,1.1,1,'blue','blue','point','short','neutral')}
<path d="M240 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('acid', '金属を溶かす酸のイラスト。', f"""
<g transform="translate(230 240)">
  <path d="M-16-90h32v40l50 110h-132l50-110z" fill="#e2eee2" stroke="{INK}" stroke-width="3"/>
  <path d="M-56 40h112l22 20h-156z" class="greenp o"/>
</g>
{drop(360,220,1.0,'green')}
<g transform="translate(430 320)">
  <path d="M-60-20h120v40h-120z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <g class="muted"><path d="M-20-40q20-30 0-50M20-40q20-30 0-50"/></g>
  <g fill="#fffaf1"><path d="M-10-20h20v20h-20z"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('acquisition', '努力して手に入れるイラスト。', f"""
{person(180,346,1.15,1,'teal','blue','reach','short','smile')}
{box(430,250,120,90,0,'gold')}
<path d="M260 250h100" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 190l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('acre', '広い土地の面積を区切って示したイラスト。', f"""
<g class="green o" opacity=".85"><path d="M60 200h480v160H60z"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="14 10"><rect x="140" y="220" width="320" height="120"/></g>
<g class="a" marker-end="url(#ar)"><path d="M140 380h320M460 380H140"/></g>
<path d="M60 396h480" class="a"/>
""", ground=False, arrow=True)

add('adaptation', '環境に合わせて姿を変えるイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-70-60h140v120h-140z" fill="#eaf5fb" class="o"/>
  <circle r="40" class="teal o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-70-60h140v120h-140z" fill="#f4ead2" class="o"/>
  <path d="M0-44l44 76h-88z" class="teal o"/>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 350l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('addiction', 'それが手放せなくなるイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','reach','short','flat')}
<g transform="translate(380 250)">
  <path d="M-50-70h100l-10 140h-80z" fill="#f7fbfe" class="o"/>
  <path d="M-44-20h88l-6 90h-76z" class="coralp o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"><path d="M280 250h50"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="380" cy="250" r="100"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('adjustment', 'つまみを少し回して合わせ直すイラスト。', f"""
<g transform="translate(200 250)">
  <circle r="70" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <path d="M0 0v-50" fill="none" stroke="{INK}" stroke-width="9"/>
  <circle r="10" class="ink"/>
</g>
<g transform="translate(430 250)">
  <path d="M-60-100h120v200h-120z" fill="#f7fbfe" class="o"/>
  <path d="M-60 10h120v90h-120z" class="teal o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="10 8"><path d="M-90 10h180"/></g>
</g>
<path d="M290 190a80 80 0 0 1 30-30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('administrator', '名簿と設定を管理する管理者のイラスト。', f"""
{person(160,346,1.2,1,'blue','blue','reach','short','neutral')}
<g transform="translate(400 240)">
  <path d="M-130-110h260v220h-260z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-90-60h180M-90-20h180M-90 20h140"/></g>
  <g fill="none" stroke="{INK}" stroke-width="8"><circle cx="80" cy="60" r="24"/></g>
</g>
<path d="M250 230h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('admission', '受付を通って中に入れてもらうイラスト。', f"""
<g transform="translate(400 240)">
  <path d="M-20-140h40v280h-40z" fill="#c9d3dc" class="o"/>
  <g transform="rotate(-70 0 -120)"><path d="M0-130h180v20H0z" class="coral o"/></g>
</g>
{person(190,346,1.05,1,'teal','blue','walk','short','smile')}
<g transform="translate(260 250)">
  <path d="M-40-24h80v40h-40z" fill="#fffdf6" stroke="{INK}" stroke-width="2"/>
  <path d="M-40-24h80v40h-80z" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<path d="M290 300h140" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('adolescent', '子どもと大人のあいだの年ごろのイラスト。', f"""
{person(150,346,0.8,1,'coral','gold','stand','cap','smile')}
{person(300,346,1.05,1,'teal','blue','stand','bob','neutral')}
{person(460,346,1.3,1,'blue','blue','stand','short','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="240" y="200" width="120" height="160" rx="12"/></g>
<path d="M300 150v40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('adoption', '新しいやり方を選んで取り入れるイラスト。', f"""
<g transform="translate(160 250)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
</g>
<g transform="translate(430 250)">
  <path d="M-90-80h180v160h-180z" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-60-50h120v100h-120z" class="teal o"/>
</g>
<path d="M250 250h80" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 350l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('advantage', '高い側に立って有利なイラスト。', f"""
<path d="M60 340L300 200h240v140z" class="green o"/>
{person(430,200,1.05,1,'teal','blue','stand','short','smile')}
{person(160,340,1.05,1,'coral','gold','stand','bob','neutral')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 130l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('affect', 'こちらの動きがあちらに響くイラスト。', f"""
<g transform="translate(160 250)"><circle r="60" class="teal o"/></g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M230 250h110"/></g>
<g transform="translate(430 250)">
  <circle r="60" class="coral o"/>
  <g class="corals" style="stroke-width:5"><path d="M0-80v-24M-70-60l-20-16M70-60l20-16"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('affection', '寄り添って情をかけ合うイラスト。', f"""
{person(240,346,1.2,1,'coral','gold','give','bob','smile')}
{person(370,346,1.2,-1,'teal','blue','give','short','smile')}
<path d="M295 250h20" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(305 160)">
  <path d="M0 36c-34-26-48-38-48-58a26 26 0 0 1 48-14 26 26 0 0 1 48 14c0 20-14 32-48 58z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('agency', '窓口で手続きを代わりに行う代理店のイラスト。', f"""
<g transform="translate(360 260)">
  <path d="M-160-120h320v240h-320z" fill="#fffdf6" class="o"/>
  <path d="M-160-120h320v40h-320z" class="teal o"/>
  <path d="M-110-40h220v40h-220z" fill="#dfe6ea" class="o"/>
  <g fill="{INK}"><rect x="-70" y="-110" width="140" height="18"/></g>
</g>
{person(150,346,1.05,1,'coral','gold','give','bob','smile')}
{person(400,300,0.95,-1,'blue','blue','reach','short','smile')}
<path d="M220 300h50" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('aid', '支援の物資を届けるイラスト。', f"""
{person(160,346,1.1,1,'blue','blue','give','short','smile')}
{box(320,270,110,80,0,'gold')}
<g transform="translate(320 240)"><path d="M-10-16h20v12h12v20h-12v12h-20v-12h-12v-20h12z" class="coral o"/></g>
{person(490,346,1.1,-1,'coral','gold','reach','bob','smile')}
<path d="M240 320h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('aide', '長のかたわらで補佐する人のイラスト。', f"""
{person(300,346,1.35,1,'blue','blue','stand','short','neutral')}
{person(430,346,1.0,1,'teal','gold','carry','bob','neutral')}
<g transform="translate(430 260)"><path d="M-36-24h72v34h-72z" class="paper"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M360 250h40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('aids', '免疫が弱まる病を示したイラスト。', f"""
<g transform="translate(220 240)">
  <path d="M0-80q56 22 56 66 0 56-56 78-56-22-56-78 0-44 56-66z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-24-10l48 48M24-10l-48 48"/></g>
</g>
<g transform="translate(440 240)">
  <g fill="none" stroke="{TONES['coral'][2]}" stroke-width="5">{''.join(f'<path d="M0 0L{int(56*__import__("math").cos(i*3.14159/4))} {int(56*__import__("math").sin(i*3.14159/4))}"/>' for i in range(8))}</g>
  <circle r="30" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M370 190h-60"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('alert', '警報が鳴って、身がまえるイラスト。', f"""
<g transform="translate(360 220)">
  <path d="M-50 20q0-70 50-70t50 70z" class="coral o"/>
  <path d="M-70 20h140v24h-140z" class="coralp o"/>
  <g class="corals" opacity=".9" style="stroke-width:6"><path d="M-100-20q-30 20-30 50M100-20q30 20 30 50"/></g>
</g>
{person(150,346,1.15,1,'teal','blue','up','short','surprised')}
<path d="M230 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('alien', '別の国から来た人を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="14 10"><path d="M40-140v280"/></g>
  <g transform="translate(-110 -90)"><path d="M-4-30h8v50h-8z" class="ink"/><path d="M4-28h44v28H4z" class="teal o"/></g>
  <g transform="translate(140 -90)"><path d="M-4-30h8v50h-8z" class="ink"/><path d="M4-28h44v28H4z" class="coral o"/></g>
</g>
{person(400,320,0.8,-1,'coral','gold','walk','bob','neutral')}
<path d="M330 250h-60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('alignment', 'ばらばらの並びが一直線にそろうイラスト。', f"""
<g transform="translate(170 240)">
  <g class="tealp o"><rect x="-70" y="-50" width="50" height="30" transform="rotate(-12 -45 -35)"/><rect x="0" y="-20" width="50" height="30" transform="rotate(10 25 -5)"/><rect x="-50" y="20" width="50" height="30" transform="rotate(6 -25 35)"/></g>
</g>
<g transform="translate(430 240)">
  <g class="teal o"><rect x="-70" y="-50" width="50" height="30"/><rect x="-70" y="-10" width="50" height="30"/><rect x="-70" y="30" width="50" height="30"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><path d="M-70-70v160"/></g>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('allegation', '証拠のないまま疑いを申し立てるイラスト。', f"""
{person(150,346,1.15,1,'blue','blue','point','short','flat')}
<g transform="translate(330 220)">
  <path d="M-80-70h160v140h-160z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50-40h100M-50-10h100"/></g>
  <g fill="{INK}"><path d="M-20 20q0-24 20-24t20 24q0 12-14 16v10h-12v-18q14-4 14-14t-8-8-8 14z"/><rect x="-6" y="52" width="12" height="12"/></g>
</g>
{person(480,346,1.15,-1,'coral','gold','stand','bob','sad')}
<path d="M420 260h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('alliance', '二国が旗を並べて手を組むイラスト。', f"""
<g transform="translate(170 200)"><path d="M-4-70h8v100h-8z" class="ink"/><path d="M4-66h60v40H4z" class="teal o"/></g>
<g transform="translate(430 200)"><path d="M-4-70h8v100h-8z" class="ink"/><path d="M-64-66h60v40h-60z" class="coral o"/></g>
{person(230,346,1.05,1,'teal','blue','reach','short','smile')}
{person(370,346,1.05,-1,'coral','gold','reach','bob','smile')}
<path d="M280 270h40" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('allocation', '全体を分けて、それぞれに割り当てるイラスト。', f"""
<g transform="translate(160 230)">
  <circle r="80" fill="#fffdf6" class="o"/>
  <path d="M0-80A80 80 0 0 1 69 40z" class="teal o"/>
  <path d="M0 0L69 40A80 80 0 0 1-69 40z" class="coralp o"/>
  <path d="M0-80A80 80 0 0 0-69 40z" class="goldp o"/>
</g>
<g class="teal o"><rect x="350" y="150" width="60" height="50"/></g>
<g class="coralp o"><rect x="350" y="220" width="60" height="50"/></g>
<g class="goldp o"><rect x="350" y="290" width="60" height="50"/></g>
<g class="a" marker-end="url(#ar)"><path d="M260 190h70M260 245h70M260 300h70"/></g>
""", ground=False, arrow=True)

add('ally', '同じ側に立つ味方のイラスト。', f"""
{person(200,346,1.15,1,'teal','gold','give','short','smile')}
{person(320,346,1.15,1,'teal','gold','give','bob','smile')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="140" y="180" width="250" height="180" rx="16"/></g>
{person(490,346,1.15,-1,'coral','coral','point','cap','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M430 250h-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('aluminium', '軽い金属のアルミ板と缶のイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-100-70h200v140h-200z" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <g fill="#ffffff" opacity=".7"><path d="M-60-70h40l-90 140h-40z"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-40-80h80v160h-80z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="-80" rx="40" ry="12" fill="#dbe3ea" stroke="{INK}" stroke-width="3"/>
  <g fill="#ffffff" opacity=".6"><rect x="-26" y="-60" width="10" height="120"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('amateur', 'まだ慣れていない、素人のイラスト。', f"""
{person(200,346,1.2,1,'coral','gold','reach','bob','flat')}
<g transform="translate(300 260) rotate(24)">
  <path d="M-10-60h20v80h-20z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-24-80h48v22h-48z" class="coral o"/>
</g>
<g transform="translate(450 270)">
  <path d="M-70-50h140v100h-140z" class="tealp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M-40-20q30 30 60 0"/></g>
</g>
{drop(250,220,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('ambassador', '国を代表して他国に赴く大使のイラスト。', f"""
{person(220,346,1.3,1,'blue','blue','carry','short','neutral')}
<g transform="translate(220 240)"><path d="M-40-30h80v10h-80z" class="teal o"/></g>
<g transform="translate(150 200)"><path d="M-4-60h8v80h-8z" class="ink"/><path d="M4-56h50v34H4z" class="teal o"/></g>
<g transform="translate(450 250)">
  <path d="M-90 90h180v-140h-180z" fill="#f4ead2" class="o"/>
  <path d="M-110-50l110-70 110 70z" class="coral o"/>
</g>
<path d="M310 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('amendment', '条文の一部を書き直して改めるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-140-90h280M-140-40h280M-140 60h280"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><path d="M-140 6h140"/><path d="M-10-14h150v40h-150z"/></g>
</g>
<g transform="translate(500 320) rotate(28)"><path d="M-10-80h20v110h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('analogy', '別のものにたとえて説明するイラスト。', f"""
<g transform="translate(170 240)">
  <g fill="none" stroke="{INK}" stroke-width="10"><circle r="46"/></g>
  <g fill="{INK}">{''.join(f'<rect x="-8" y="-64" width="16" height="18" transform="rotate({i*60})"/>' for i in range(6))}</g>
</g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M280 220h40M280 260h40"/></g>
<g transform="translate(430 240)">
  <circle cy="-20" r="34" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-50 70q0-70 50-70t50 70z" class="teal o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('analysis', 'ひとまとまりを分けて調べるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-70-70h140v140h-140z" class="teal o"/>
</g>
<g transform="translate(430 240)">
  <g class="tealp o"><rect x="-70" y="-70" width="60" height="60"/><rect x="10" y="-70" width="60" height="60"/><rect x="-70" y="10" width="60" height="60"/><rect x="10" y="10" width="60" height="60"/></g>
</g>
<path d="M250 240h100" class="a" marker-end="url(#ar)"/>
<g transform="translate(300 350) rotate(20)">
  <circle r="30" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="5"/>
  <path d="M0 30v34" fill="none" stroke="{INK}" stroke-width="10"/>
</g>
""", ground=True, arrow=True)

add('analyst', '数字を読み解いて分析する人のイラスト。', f"""
{person(160,340,1.15,1,'blue','blue','point','bob','neutral')}
<g transform="translate(400 230)">
  <path d="M-130-110h260v220h-260z" fill="#f7fbfe" class="o"/>
  <path d="M-100 70l60-70 40 40 60-90" fill="none" stroke="{TONES['teal'][0]}" stroke-width="5"/>
  <g fill="{INK}"><circle cx="-100" cy="70" r="7"/><circle cx="-40" cy="0" r="7"/><circle cx="0" cy="40" r="7"/><circle cx="60" cy="-50" r="7"/></g>
</g>
<path d="M250 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('ancestor', '代々の先祖から自分へつながるイラスト。', f"""
{person(140,346,1.05,1,'violet','violet','stand','short','neutral')}
{person(280,346,1.1,1,'blue','blue','stand','bob','neutral')}
{person(420,346,1.15,1,'teal','gold','stand','cap','smile')}
<g class="a" marker-end="url(#ar)"><path d="M120 170h330"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="90" y="200" width="110" height="160" rx="12"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('anchor', '船をつなぎとめるいかりのイラスト。', f"""
<path d="M0 120h600v280H0z" class="bluep" opacity=".5"/>
<g transform="translate(300 220)">
  <circle cy="-90" r="24" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M-6-66h12v170h-12z" class="ink"/>
  <path d="M-70-40h140v16h-140z" class="ink"/>
  <path d="M-80 60q10 60 80 44 70 16 80-44" fill="none" stroke="{INK}" stroke-width="12"/>
</g>
<g fill="none" stroke="#fffdf6" stroke-width="5" opacity=".8"><path d="M40 140q40-20 80 0t80 0M340 140q40-20 80 0t80 0"/></g>
""", ground=False)

add('angel', '輪と羽をもつ天使のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#f6f0dc"/>
<g fill="#f7e6bd" opacity=".6"><circle cx="300" cy="210" r="150"/></g>
{person(300,346,1.25,1,'gold','gold','up','bob','smile')}
<g fill="none" stroke="#d9c286" stroke-width="6"><ellipse cx="300" cy="176" rx="40" ry="12"/></g>
<g fill="#fffdf6" stroke="#d9c286" stroke-width="3"><path d="M250 260q-70-50-30-90 40 20 40 60zM350 260q70-50 30-90-40 20-40 60z"/></g>
""", ground=False)

add('anger', '怒りがこみ上げて燃えるイラスト。', f"""
{face(260,200,95,'flat')}
<g fill="none" stroke="{INK}" stroke-width="8"><path d="M200 150l42 16M320 150l-42 16"/></g>
<circle cx="176" cy="232" r="24" class="coralp"/><circle cx="344" cy="232" r="24" class="coralp"/>
{flame(430,220,1.0)}
<g class="corals" opacity=".9" style="stroke-width:5"><path d="M120 170q-26 26-26 50"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('angle', '二本の線がつくる角度のイラスト。', f"""
<g transform="translate(200 320)">
  <path d="M0 0h260" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M0 0L220-180" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M90 0a90 90 0 0 0-16-52" fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"/>
</g>
<g fill="{INK}"><rect x="300" y="270" width="40" height="10"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('animation', '少しずつ動く絵が続いて動画になるイラスト。', f"""
<g transform="translate(300 230)">
  <g class="paper"><path d="M-230-70h130v140h-130z"/><path d="M-60-70h130v140h-130z"/><path d="M110-70h130v140h-130z"/></g>
  <g class="teal o"><circle cx="-190" cy="30" r="20"/><circle cx="-10" cy="-10" r="20"/><circle cx="180" cy="-50" r="20"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 350h400"/></g>
""", ground=False, arrow=True)

add('anxiety', '先が心配で、胸がざわつくイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','think','short','sad')}
{cloud(200,150,1.0)}
<g transform="translate(430 200)">
  <path d="M-120-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><path d="M-20-20q0-30 24-30t24 30q0 16-16 20v12h-16v-22q16-4 16-16t-9-9-9 15z"/><rect x="-4" y="26" width="14" height="14"/></g>
</g>
{drop(260,240,0.7)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('anxious', '落ち着かずそわそわして待つイラスト。', f"""
{person(240,346,1.25,1,'coral','blue','stand','bob','sad')}
{drop(310,220,0.8)}{drop(180,230,0.7)}
<g class="muted"><path d="M330 300q30 20 0 40M350 300q30 20 0 40"/></g>
<g transform="translate(470 200)">
  <circle r="54" fill="#fffdf6" class="o"/>
  <path d="M0-34v34l26 14" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('apart', '二つが離れて間があくイラスト。', f"""
<g class="teal o"><rect x="100" y="200" width="110" height="120"/></g>
<g class="coral o"><rect x="390" y="200" width="110" height="120"/></g>
<g class="a" marker-end="url(#ar)"><path d="M230 260h140M370 260H230"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M300 160v200"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('apology', '頭を下げてあやまるイラスト。', f"""
<g transform="translate(230 346) rotate(26)">{person(0,0,1.25,1,'teal','blue','stand','short','sad')}</g>
{person(470,346,1.15,-1,'coral','gold','stand','bob','neutral')}
<g transform="translate(350 170)">
  <path d="M-70-40h140v60h-140z" fill="#fffdf6" class="o"/>
  <path d="M-40 20l-14 28 40-28z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-50" y="-20" width="100" height="14"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('appetite', 'おなかがすいて、食べたくなるイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','stand','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="9 8"><circle cx="216" cy="290" r="36"/></g>
<g transform="translate(430 280)">
  <ellipse rx="110" ry="30" fill="#fffdf6" class="o"/>
  <g class="coralp o"><ellipse cy="-16" rx="70" ry="24"/></g>
  <g class="greenp o"><circle cx="40" cy="-20" r="16"/></g>
</g>
<path d="M280 250h60" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('applicant', '応募書類を出す人のイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','give','bob','smile')}
<g transform="translate(330 240)">
  <path d="M-80-80h160v160h-160z" class="paper"/>
  <g fill="{INK}"><rect x="-50" y="-50" width="90" height="14"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-50-10h100M-50 20h80"/></g>
</g>
<g transform="translate(480 250)">
  <path d="M-60-60h120v120h-120z" fill="#dfe6ea" class="o"/>
  <path d="M-30-70h60v14h-60z" class="ink"/>
</g>
<path d="M420 300h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('appreciation', '感謝の気持ちを伝えるイラスト。', f"""
{person(220,346,1.2,1,'teal','blue','give','short','smile')}
{person(400,346,1.2,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(310 180)">
  <path d="M0 40c-40-30-56-46-56-68a30 30 0 0 1 56-16 30 30 0 0 1 56 16c0 22-16 38-56 68z" class="coralp o"/>
</g>
<g transform="translate(310 260)"><path d="M-40-24h80v40h-80z" class="paper"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
