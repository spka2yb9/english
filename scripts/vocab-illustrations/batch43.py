"""第43回: 合併・修正・監視・従うなど40語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('merge', '二本の流れが合わさって一本になるイラスト。', f"""
<path d="M60 160q160 0 200 60" fill="none" stroke="{TONES['teal'][0]}" stroke-width="22" stroke-linecap="round"/>
<path d="M60 300q160 0 200-60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="22" stroke-linecap="round"/>
<path d="M258 230h200" fill="none" stroke="{TONES['violet'][0]}" stroke-width="30" stroke-linecap="round"/>
<path d="M470 230h60" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('metal', '光沢のある金属の板とインゴットのイラスト。', f"""
<g transform="translate(230 250)">
  <path d="M-140-60h280v120h-280z" fill="#d7dfe6" class="o"/>
  <g fill="#ffffff" opacity=".7"><path d="M-100-60l60 0-120 120h-20z"/><path d="M-20-60l40 0-120 120h-40z"/></g>
</g>
<g transform="translate(450 290)">
  <path d="M-70 30h140l-24-50h-92z" fill="#c9d3dc" class="o"/>
  <path d="M-46-20h92l-16-34h-60z" fill="#dbe3ea" class="o"/>
</g>
<path d="M60 330h480" class="a"/>
""", ground=True)

add('middle', '三つの箱のうち、真ん中を示したイラスト。', f"""
<g class="tealp o"><rect x="90" y="200" width="110" height="110"/><rect x="400" y="200" width="110" height="110"/></g>
<rect x="245" y="200" width="110" height="110" class="coral o"/>
<path d="M300 140v40" class="a" marker-end="url(#ar)"/>
<path d="M60 330h480" class="a"/>
""", ground=True, arrow=True)

add('mild', 'とがった形とやわらかい丸い形を比べたイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80 60L0-70 80 60z" class="coralp o"/>
  <g class="corals" style="stroke-width:5"><path d="M0-100v-20"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-90 60q10-110 90-110t90 110z" class="tealp o"/>
</g>
<path d="M270 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 306h480" class="a"/>
""", ground=True, arrow=True)

add('minimize', '大きさをできるだけ小さく抑えるイラスト。', f"""
<g transform="translate(180 230)" opacity=".35"><path d="M-100-100h200v200h-200z" class="teal o"/></g>
<g transform="translate(430 290)"><path d="M-30-30h60v60h-60z" class="teal o"/></g>
<path d="M300 200l70 60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M370 330h30M490 330h-30"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True, arrow=True)

add('mistake', '答案に赤い×がついた、間違いのイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-160-140h320v280h-320z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-120-80h240M-120-20h240M-120 40h180"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M60-104l50 50M110-104l-50 50"/></g>
</g>
<g transform="translate(490 320) rotate(28)"><path d="M-10-70h20v100h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('mobile', '手のひらに収まる携帯電話のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-70-130h140v260h-140z" fill="#2f4055"/>
  <path d="M-56-112h112v210h-112z" class="tealp"/>
  <circle cy="112" r="12" fill="#546b83"/>
  <g class="teal o"><rect x="-36" y="-90" width="30" height="30"/><rect x="6" y="-90" width="30" height="30"/><rect x="-36" y="-48" width="30" height="30"/><rect x="6" y="-48" width="30" height="30"/></g>
</g>
<g class="tealsx" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"><path d="M420 120q30 30 30 60t-30 60M450 90q46 46 46 90t-46 90"/></g>
""", ground=True)

add('mobilize', '散らばっていた人を集めて、まとめて動かすイラスト。', f"""
<g opacity=".4">{person(110,180,0.55,1,'gold','blue','stand','short','neutral')}{person(180,150,0.55,1,'teal','gold','stand','bob','neutral')}{person(120,300,0.55,1,'coral','blue','stand','cap','neutral')}</g>
{person(380,346,0.9,1,'teal','blue','walk','short','neutral')}
{person(450,346,0.9,1,'coral','gold','walk','cap','neutral')}
{person(520,346,0.9,1,'gold','blue','walk','bob','neutral')}
<path d="M220 230h100" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('model', '見本となる型から、同じ形が作られるイラスト。', f"""
<g transform="translate(160 240)">
  <path d="M-70-80h140v160h-140z" class="teal o"/>
  <path d="M0-40l10 22 24 4-17 17 4 24-21-12-21 12 4-24-17-17 24-4z" fill="#fffdf6"/>
</g>
<g transform="translate(400 240)">
  <path d="M-60-70h120v140h-120z" class="tealp o"/>
</g>
<g transform="translate(520 240)">
  <path d="M-60-70h120v140h-120z" class="tealp o"/>
</g>
<path d="M250 230h60" class="a" marker-end="url(#ar)"/>
<path d="M60 326h480" class="a"/>
""", ground=True, arrow=True)

add('modify', '書かれた図の一部を書き直して直すイラスト。', f"""
<g transform="translate(280 230)">
  <path d="M-170-130h340v260h-340z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4"><path d="M-130-70h240M-130-10h240"/></g>
  <path d="M-130 50h120" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="0" opacity=".4"/>
  <path d="M-130 50h120" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" transform="translate(0 -6)"/>
  <path d="M-10 44h130" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
</g>
<g transform="translate(480 300) rotate(28)"><path d="M-10-80h20v110h-20z" class="coral o"/><path d="M-10 30h20l-10 24z" class="ink"/></g>
""", ground=True)

add('monitor', '画面をじっと見て、様子を見張るイラスト。', f"""
{person(140,346,1.05,1,'blue','blue','stand','short','neutral')}
<g transform="translate(400 240)">
  <path d="M-150-110h300v200h-300z" fill="#dfe6ea" class="o"/>
  <path d="M-126-88h252v156h-126z" class="bluep"/>
  <path d="M-126-88h252v156h-252z" fill="none" stroke="{INK}" stroke-width="2"/>
  <path d="M-100 40l50-70 40 40 40-60 44 90z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
  <path d="M-30 90h60v26h-60z" fill="#c9d3dc" class="o"/>
</g>
<path d="M200 230h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('moon', '夜空に浮かぶ三日月のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#2b3a52"/>
<g fill="#f3e3ae" stroke="#d9c286" stroke-width="3"><path d="M340 60a150 150 0 1 0 0 280 120 120 0 1 1 0-280z"/></g>
<g fill="#fdf6e0"><circle cx="120" cy="110" r="5"/><circle cx="190" cy="200" r="4"/><circle cx="140" cy="300" r="4"/><circle cx="470" cy="120" r="5"/><circle cx="520" cy="250" r="4"/><circle cx="430" cy="320" r="4"/></g>
""", ground=False)

add('motivate', 'やる気の火をつけられて、走り出す人のイラスト。', f"""
{person(200,346,1.15,1,'coral','blue','walk','short','smile')}
<g transform="translate(200 170)">
  {flame(0,0,1.1)}
</g>
{person(430,346,1.1,1,'teal','gold','point','bob','smile')}
<path d="M370 230h-80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('motorcycle', '二輪のオートバイのイラスト。', f"""
<g transform="translate(300 270)">
  <circle cx="-140" cy="40" r="52" fill="none" stroke="{INK}" stroke-width="12"/>
  <circle cx="140" cy="40" r="52" fill="none" stroke="{INK}" stroke-width="12"/>
  <path d="M-140 40L-30-30h100l70 70" fill="none" stroke="{TONES['coral'][0]}" stroke-width="14"/>
  <path d="M-40-40h110v-30h-90z" class="coral o"/>
  <path d="M-30-30l-50-40h-40" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M60 0h80v20H60z" class="goldp o"/>
</g>
<path d="M60 340h480" class="a"/>
""", ground=True)

add('movement', '腕を大きく動かしている、動きのイラスト。', f"""
{person(280,346,1.3,1,'teal','blue','up','short','smile')}
<g opacity=".3">{person(280,346,1.3,1,'teal','blue','stand','short','smile')}</g>
<g class="corals" style="stroke-width:5"><path d="M180 180q-24 20-24 50M400 180q24 20 24 50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('multiply', '一つが増えて、たくさんになるイラスト。', f"""
<g transform="translate(140 240)"><circle r="34" class="teal o"/></g>
<g transform="translate(300 240)"><circle cx="-30" r="26" class="teal o"/><circle cx="30" r="26" class="teal o"/></g>
<g class="teal o">
  <circle cx="440" cy="180" r="22"/><circle cx="490" cy="180" r="22"/><circle cx="540" cy="180" r="22"/>
  <circle cx="440" cy="240" r="22"/><circle cx="490" cy="240" r="22"/><circle cx="540" cy="240" r="22"/>
  <circle cx="440" cy="300" r="22"/><circle cx="490" cy="300" r="22"/><circle cx="540" cy="300" r="22"/>
</g>
<path d="M190 240h60M350 240h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('musical', '音符が並んだ楽譜と楽器のイラスト。', f"""
<g transform="translate(280 200)">
  <path d="M-180-90h360v180h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-150 {-50+i*24}h300"/>' for i in range(5))}</g>
  <g fill="{INK}"><ellipse cx="-90" cy="22" rx="16" ry="11"/><ellipse cx="0" cy="-2" rx="16" ry="11"/><ellipse cx="90" cy="22" rx="16" ry="11"/>
  <rect x="-78" y="-48" width="5" height="66"/><rect x="12" y="-72" width="5" height="66"/><rect x="102" y="-48" width="5" height="66"/></g>
</g>
<g transform="translate(430 330)">
  <ellipse rx="52" ry="40" class="goldd o"/>
  <path d="M-6-40h12v-90h-12z" class="ink"/>
</g>
""", ground=True)

add('myself', '鏡に映る自分を指さしているイラスト。', f"""
{person(180,346,1.2,1,'teal','blue','point','short','smile')}
<g transform="translate(430 220)">
  <path d="M-90-130h180v260h-180z" fill="#e6f2f7" stroke="{INK}" stroke-width="4"/>
  <g transform="translate(0 126) scale(0.85)" opacity=".85">{person(0,0,1.2,-1,'teal','blue','point','short','smile')}</g>
</g>
<path d="M270 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('national', '国旗が掲げられた、国全体を表すイラスト。', f"""
<g transform="translate(180 240)">
  <path d="M-6-140h12v280h-12z" class="ink"/>
  <path d="M6-130h150v90H6z" class="coralp o"/>
  <circle cx="80" cy="-85" r="26" class="coral o"/>
</g>
{building(430,300,1.0,'teal')}
<path d="M60 350h480" class="a"/>
""", ground=True)

add('neck', '頭と体をつなぐ首を示したイラスト。', f"""
{face(300,150,80,'smile')}
<g transform="translate(300 250)">
  <path d="M-26-30h52v56h-52z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/>
  <path d="M-90 26h180v90h-180z" class="teal o"/>
</g>
<circle cx="300" cy="248" r="56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M420 248h-56" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('neglect', '手入れをせず、放ったままで荒れていくイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-80-40h160v120h-160z" fill="#e4e0d4" stroke="{INK}" stroke-width="3"/>
  <path d="M-80-40l40-50h160l-40 50z" fill="#d8d2c2" stroke="{INK}" stroke-width="3"/>
  <path d="M-40 20h50v60h-50z" fill="#c8c2b0"/>
  <g class="muted"><path d="M-60 0h30M20-10h40"/></g>
</g>
<g class="green o" opacity=".8"><path d="M120 340q10-40 30-40t20 40zM300 344q8-34 26-34t18 34z"/></g>
{person(470,346,1.0,-1,'coral','blue','walk','short','neutral')}
<path d="M400 240h60" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('negotiate', '机をはさんで条件を話し合う二人のイラスト。', f"""
{person(140,330,1.05,1,'blue','blue','reach','short','neutral')}
{person(460,330,1.05,-1,'coral','gold','reach','bob','neutral')}
<g transform="translate(300 300)">
  <path d="M-110-16h220v22h-220z" class="goldd o"/>
  <path d="M-96 6h14v60h-14zM82 6h14v60H82z" class="goldd o"/>
</g>
<g transform="translate(300 240)">
  <path d="M-60-40h120v70h-120z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40-20h80M-40 0h80"/></g>
</g>
<path d="M220 200h50M380 200h-50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('network', '点と点が線でつながった網の目のイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="3">
  <path d="M120 120L300 200 480 110M120 120L200 300 300 200M300 200L440 310 480 110M200 300L440 310M120 120L480 110"/>
</g>
<g class="teal o"><circle cx="120" cy="120" r="22"/><circle cx="300" cy="200" r="26"/><circle cx="480" cy="110" r="22"/><circle cx="200" cy="300" r="22"/><circle cx="440" cy="310" r="22"/></g>
""", ground=False)

add('nod', '首を縦に振ってうなずくイラスト。', f"""
{face(280,190,85,'smile')}
<g opacity=".3">{face(280,250,85,'smile')}</g>
<path d="M430 170q30 40 0 90" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M110 300l18 18 30-36"/></g>
""", ground=False, arrow=True)

add('noise', '大きな音が耳にひびいて、うるさいイラスト。', f"""
<g transform="translate(180 230)">
  <path d="M-70-70h100l70-50v240l-70-50h-100z" class="ink"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:6"><path d="M300 170q34 34 34 60t-34 60M350 140q50 50 50 90t-50 90M400 110q66 66 66 120t-66 120"/></g>
{person(520,346,0.9,-1,'teal','blue','think','short','sad')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('nominate', '候補として一人の名前を挙げるイラスト。', f"""
{person(150,346,1.1,1,'blue','blue','point','short','neutral')}
<g transform="translate(400 230)">
  <path d="M-110-100h220v200h-220z" class="paper"/>
  <g fill="{INK}"><rect x="-80" y="-70" width="100" height="10"/><rect x="-80" y="-20" width="100" height="10"/><rect x="-80" y="30" width="100" height="10"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4"><rect x="-92" y="-34" width="150" height="40"/></g>
</g>
<path d="M240 210h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('normal', '波形が乱れず、いつもの状態に収まっているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-120h440v240h-440z" fill="#f7fbfe" class="o"/>
  <path d="M-190 0h380" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-190 0q40-40 80 0t80 0q40-40 80 0t80 0q40-40 60 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="6"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 350l18 18 30-36"/></g>
""", ground=True)

add('northern', '地図の北側の地域を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <path d="M-180-140h360v110h-360z" class="bluep o"/>
  <path d="M-180-30h360" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="10 8"/>
</g>
<g transform="translate(500 110)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M0-26l12 26-12 26-12-26z" class="coral o"/>
</g>
<path d="M120 120v-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('notify', '知らせが相手のもとに届くイラスト。', f"""
{person(140,346,1.05,1,'teal','blue','give','short','smile')}
<g transform="translate(300 210)">
  <path d="M-60-40h120v80h-120z" class="paper"/>
  <path d="M-60-40l60 46 60-46" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
{person(470,346,1.05,-1,'coral','gold','reach','bob','surprised')}
<path d="M220 160q80-50 160 0" class="a" marker-end="url(#ar)"/>
<g transform="translate(470 200)"><circle r="18" class="coral o"/><path d="M-2-10h4v12h-4zM-2 6h4v4h-4z" fill="#fffdf6"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('novel', '物語が書かれた分厚い本のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-150-140h300v280h-300z" class="violet o"/>
  <path d="M-130-120h260v240h-260z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-70" y="-90" width="140" height="12"/><rect x="-40" y="-60" width="80" height="8"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-90 {0+i*24}h180"/>' for i in range(5))}</g>
</g>
<path d="M60 390h480" class="a"/>
""", ground=True)

add('nuclear', '原子核から大きな力が出ることを示したイラスト。', f"""
<g transform="translate(300 210)">
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4">
    <ellipse rx="130" ry="50"/><ellipse rx="130" ry="50" transform="rotate(60)"/><ellipse rx="130" ry="50" transform="rotate(-60)"/>
  </g>
  <circle r="30" class="coral o"/>
</g>
<g class="corals" opacity=".9" style="stroke-width:5"><path d="M300 300v40M240 300l-24 34M360 300l24 34"/></g>
""", ground=False)

add('nut', 'ねじを留める六角ナットのイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M0-120l104 60v120L0 120l-104-60v-120z" fill="#c9d3dc" class="o"/>
  <circle r="46" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(300 330)"><path d="M-14 0h28v60h-28z" fill="#dbe3ea" class="o"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('obey', '示された指示のとおりに動くイラスト。', f"""
{person(140,346,1.05,1,'blue','blue','point','short','neutral')}
<g transform="translate(300 200)">
  <circle r="52" fill="#fffdf6" class="o"/>
  <path d="M-24 0h40M10-16l18 16-18 16" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
</g>
{person(470,346,1.05,1,'teal','gold','walk','bob','neutral')}
<path d="M370 200h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M500 140l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('object', '手に取れる、形のあるものを並べたイラスト。', f"""
<g transform="translate(160 270)"><path d="M-50-50h100v100h-100z" class="tealp o"/></g>
<g transform="translate(300 270)"><circle r="52" class="coralp o"/></g>
<g transform="translate(450 270)"><path d="M-52 50h104L0-56z" class="goldp o"/></g>
<path d="M60 330h480" class="a"/>
""", ground=True)

add('oblige', '書面の決まりに縛られて、やらねばならないイラスト。', f"""
{person(180,346,1.1,1,'teal','blue','stand','short','sad')}
<g transform="translate(420 220)">
  <path d="M-110-110h220v220h-220z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-80-70h160M-80-30h160M-80 10h160M-80 50h110"/></g>
  <g fill="{INK}"><rect x="-80" y="-100" width="60" height="10"/></g>
</g>
<path d="M310 230h-60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M150 250q30 20 60 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('obvious', '明るい光の下で、はっきり見えているイラスト。', f"""
{sun(300,90,34)}
<g transform="translate(300 250)">
  <circle r="80" class="coral o"/>
  <path d="M-40 0h80" fill="none" stroke="#fffdf6" stroke-width="12"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 200l18 18 30-36"/></g>
<path d="M120 350h360" class="a"/>
""", ground=True)

add('occupy', '席を人がふさいで、空きがないイラスト。', f"""
<g transform="translate(300 300)">
  <g class="goldd o"><rect x="-240" y="-20" width="100" height="20"/><rect x="-110" y="-20" width="100" height="20"/><rect x="20" y="-20" width="100" height="20"/><rect x="150" y="-20" width="100" height="20"/></g>
</g>
{person(140,300,0.85,1,'teal','blue','stand','short','neutral')}
{person(250,300,0.85,1,'coral','gold','stand','bob','neutral')}
{person(370,300,0.85,1,'gold','blue','stand','cap','neutral')}
{person(490,300,0.85,1,'violet','teal','stand','short','neutral')}
<path d="M60 340h480" class="a"/>
""", ground=True)

add('ocean', '果てしなく広がる大海原のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#dff0fa"/>
<path d="M0 170h600v230H0z" class="bluep"/>
<g fill="none" stroke="{TONES['blue'][2]}" stroke-width="4" opacity=".8">
  <path d="M40 230q40-20 80 0t80 0t80 0t80 0t80 0t80 0"/>
  <path d="M20 290q40-20 80 0t80 0t80 0t80 0t80 0t80 0"/>
  <path d="M40 350q40-20 80 0t80 0t80 0t80 0t80 0t80 0"/>
</g>
{sun(500,80,30)}
""", ground=False)

add('odd', '同じ形の中に、一つだけ奇妙な形があるイラスト。', f"""
<g class="tealp o"><circle cx="130" cy="180" r="40"/><circle cx="250" cy="180" r="40"/><circle cx="370" cy="180" r="40"/><circle cx="490" cy="180" r="40"/><circle cx="130" cy="300" r="40"/><circle cx="370" cy="300" r="40"/><circle cx="490" cy="300" r="40"/></g>
<g transform="translate(250 300)"><path d="M-38-34l30 20-20 30 40 8 12 34-34-20-30 22 4-40-30-24 40-6z" class="coral o"/></g>
<circle cx="250" cy="300" r="60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
""", ground=False)
print(len(W), ' '.join(W)); print(sheet(W))
