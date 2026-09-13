"""第10回: 支える・伝える・覆う・全体と部分などの30語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('assist', '重い荷物を運ぶ人に、もう一人が横から手を添えて助けているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="greenp"/>
{person(230,346,1.1,1,'coral','blue','carry','short','sad')}
{box(300,266,110,74,0,'gold')}
{person(400,346,1.1,-1,'green','violet','give','bob','smile')}
<path d="M356 272h-40" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<path d="M400 200q-40-30-70-24" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('assistant', '主となる人の隣で、道具を手渡して支えている助手のイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','point','short','neutral')}
{person(400,346,0.95,-1,'gold','violet','give','bob','smile')}
<g transform="translate(300 262) rotate(-14)">
  <path d="M-50-8h100v16h-100z" class="goldd o"/>
  <path d="M50-12h26v24H50z" class="coral o"/>
</g>
<path d="M352 220q-30-16-56-10" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('available', '棚に商品が並び、手に取れる状態になっているイラスト。空の棚と対比する。', f"""
<g transform="translate(180 250)">
  <path d="M-120-100h240v200h-240z" class="goldp o"/>
  <path d="M-120 0h240" fill="none" stroke="{TONES['gold'][2]}" stroke-width="6"/>
  <g class="coral o"><rect x="-100" y="-70" width="46" height="66"/><rect x="-44" y="-70" width="46" height="66"/><rect x="12" y="-70" width="46" height="66"/></g>
  <g class="tealp o"><rect x="-100" y="30" width="46" height="66"/><rect x="-44" y="30" width="46" height="66"/></g>
</g>
{hand(390,190,-1)}
<path d="M356 250q-40 20-70 22" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M430 330l18 18 30-36"/></g>
""", ground=True, arrow=True)

add('betray', '味方のふりをしていた人が、後ろで相手側へ情報をわたしているイラスト。', f"""
{person(160,346,1.05,1,'teal','blue','stand','short','smile')}
{person(300,346,1.05,1,'violet','gold','give','cap','neutral')}
{person(470,346,1.05,-1,'coral','violet','give','bob','neutral')}
<g transform="translate(390 258)">
  <path d="M-30-20h60v40h-60z" class="paper"/>
  <path d="M-30-20L0 8l30-28" fill="none" class="a"/>
</g>
<path d="M348 216q40-22 74-6" class="muted" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:6"><path d="M226 210l-24 24M202 210l24 24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('compliment', 'よくできた絵を指して、相手を褒めている人のイラスト。', f"""
{person(160,346,1.1,1,'teal','blue','point','short','smile')}
<g transform="translate(400 240)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <path d="M-70 60l50-70 34 40 34-50 26 80z" class="tealp o"/>
  <circle cx="46" cy="-52" r="20" class="goldp o"/>
</g>
<g transform="translate(300 170)">
  <path d="M0 20l-24-30 12-14 12 12 12-12 12 14z" class="coral o"/>
  <path d="M-46-10l-8-20M46-10l8-20" class="golds"/>
</g>
<path d="M240 240q40-20 66-10" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('conquer', '高い山の頂に旗を立て、登りきった人のイラスト。', f"""
<path d="M20 340L300 60l280 280z" class="tealp o"/>
<path d="M300 60l60 60q-30 16-60 4-28 12-56-4z" fill="#ffffff" stroke="{INK}" stroke-width="2.5"/>
<path d="M366 66v-56" class="a"/>
<path d="M366 12l70 20-70 22z" class="coral o"/>
{person(292,72,0.6,1,'coral','blue','up','short','smile')}
<path d="M110 336q86-30 116-104t74-116" class="muted" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('convey', 'ベルトコンベヤーが荷物を向こう側へ運んでいくイラスト。', f"""
<g transform="translate(300 280)">
  <path d="M-240-20h480v40h-480z" fill="#dfe6ea" class="o"/>
  <circle cx="-240" cy="0" r="26" fill="#cfd8de" stroke="{INK}" stroke-width="3"/>
  <circle cx="240" cy="0" r="26" fill="#cfd8de" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-160-20v40M-80-20v40M0-20v40M80-20v40M160-20v40"/></g>
</g>
{box(180,232,80,58,0,'gold')}
{box(350,232,80,58,0,'gold')}
<path d="M420 190h100" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('cope', '降りしきる雨の中、かさをさして落ち着いて歩いていくイラスト。', f"""
<g class="blues" opacity=".9"><path d="M100 40l-12 34M180 80l-12 34M300 40l-12 34M420 80l-12 34M500 40l-12 34M240 130l-12 34M380 140l-12 34"/></g>
{person(300,346,1.1,1,'teal','blue','walk','short','neutral')}
<g transform="translate(300 200)">
  <path d="M-110 0a110 74 0 0 1 220 0z" class="coral o"/>
  <path d="M-110 0q28 18 55 0 27 18 55 0" class="a"/>
  <path d="M0 0v96" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
</g>
<path d="M400 300h80" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('covered', '布をかけて中身をすっかり覆っているイラスト。下の形が透けて見える。', f"""
<circle cx="470" cy="96" r="54" class="violetp"/>
<g transform="translate(280 280)">
  <path d="M-120 60V-20h240v80z" class="muted"/>
  <path d="M-150 60q-20-90 40-120 50-24 110-24t110 24q60 30 40 120z" class="violetp o"/>
  <path d="M-150 60q60 20 150 20t150-20" fill="none" class="a"/>
  <path d="M-60-100q60-16 120 0" fill="none" stroke="{TONES['violet'][0]}" stroke-width="4"/>
</g>
<path d="M420 180q-40 10-64 20" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('demonstrate', '人前で道具の使い方を実際にやって見せているイラスト。', f"""
{person(160,346,1.15,1,'coral','blue','point','bun','neutral')}
<g transform="translate(300 250)">
  <path d="M-70-40h140v90h-140z" class="tealp o"/>
  <path d="M-70-40h140" class="a"/>
  <path d="M0-40v-30" class="a"/>
  <circle cy="-84" r="16" class="coral o"/>
</g>
<g opacity=".85">
  {person(430,346,0.8,-1,'violet','teal','stand','short','smile')}
  {person(520,346,0.8,-1,'gold','blue','stand','bob','smile')}
</g>
<path d="M240 190q40-20 66-6" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('dominate', '大きな一つの塔が、周りの小さな建物を圧して目立っているイラスト。', f"""
<g transform="translate(300 0)">
  <path d="M-60 360V100h120v260z" class="teal o"/>
  <path d="M-78 100L0 30l78 70z" class="teald o"/>
  <g class="bluep o"><rect x="-26" y="140" width="52" height="44"/><rect x="-26" y="212" width="52" height="44"/></g>
</g>
{building(110,360,0.6,'gold')}
{building(490,360,0.6,'gold')}
<path d="M120 200q60-40 118-60" class="muted" marker-end="url(#ar)"/>
<path d="M60 360h480" class="a"/>
""", ground=True, arrow=True)

add('embark', '船のタラップを渡って、荷物を持って乗り込んでいくイラスト。', f"""
<path d="M0 300h600v100H0z" class="bluep"/>
<path d="M0 300q60-14 120 0t120 0 120 0 120 0 120 0" class="a"/>
<g transform="translate(400 260)">
  <path d="M-160 0h320l-30 46h-260z" class="teal o"/>
  <path d="M-160 0h320" class="a"/>
  <path d="M-90 0v-60h130v60z" class="paper"/>
  <path d="M10-60v-30" class="a"/>
</g>
<path d="M120 330l130-70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
{person(180,318,0.8,1,'coral','blue','carry','cap','smile')}
<path d="M170 200q60-30 110-16" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('ensure', '出かける前に鍵をかけ、閉まっているか確かめているイラスト。', f"""
<path d="M60 40h240v340H60z" fill="#e0d6c2" stroke="{INK}" stroke-width="3"/>
<circle cx="272" cy="220" r="12" class="goldd"/>
<g transform="translate(220 220)">
  <path d="M-26-30v-20a26 26 0 0 1 52 0v20" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M-40-30h80q8 0 8 8v56q0 8-8 8h-80q-8 0-8-8v-56q0-8 8-8z" class="goldp o"/>
  <circle cy="6" r="9" class="ink"/>
</g>
{person(430,346,1.05,-1,'teal','blue','point','short','neutral')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M330 130l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('entire', 'ケーキが一切れも欠けず、丸ごとそろっているイラスト。', f"""
<circle cx="470" cy="96" r="54" class="coralp"/>
<g transform="translate(270 250)">
  <ellipse cy="30" rx="150" ry="46" class="goldp o"/>
  <path d="M-150 30V0a150 46 0 0 1 300 0v30" fill="#fff4d8" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="0" rx="150" ry="46" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <ellipse cy="0" rx="118" ry="34" class="coralp o"/>
</g>
<path d="M120 340h300" class="a" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('execute', '計画表のとおりに手を動かして、実際に組み立てを進めているイラスト。', f"""
<g transform="translate(150 220)">
  <path d="M-90-110h180v220h-180z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"><path d="M-60-80h120M-60-40h120M-60 0h120"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-70-84l10 10 16-18M-70-44l10 10 16-18"/></g>
</g>
{box(420,270,110,80,26,'gold')}
{hand(400,170,1)}
<path d="M270 200h80" class="a" marker-end="url(#ar)"/>
<path d="M60 356h480" class="a"/>
""", ground=True, arrow=True)

add('grasp', '棒をしっかり握りしめて、離さないようにしているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
<path d="M300 380V90" fill="none" stroke="{TONES['gold'][2]}" stroke-width="20" stroke-linecap="round"/>
<g transform="translate(300 240)">
  <path d="M-52-34h104q16 0 16 16v36q0 16-16 16h-104q-16 0-16-16v-36q0-16 16-16z" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
  <g fill="none" stroke="{SKINL}" stroke-width="2"><path d="M-30-34v68M-4-34v68M22-34v68"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M180 300q40-30 70-40"/><path d="M420 300q-40-30-70-40"/></g>
""", ground=True, arrow=True)

add('historical', '古い巻物と時代を示す年表が並んだイラスト。', f"""
<circle cx="470" cy="96" r="54" class="goldp"/>
<g transform="translate(250 240)">
  <path d="M-130-70h260v140h-260z" fill="#f3e6c8" stroke="{INK}" stroke-width="3"/>
  <ellipse cx="-130" cy="0" rx="18" ry="70" class="goldd o"/>
  <ellipse cx="130" cy="0" rx="18" ry="70" class="goldd o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-40h190M-100-10h190M-100 20h150"/></g>
</g>
<path d="M100 350h400" class="a" marker-end="url(#ar)"/>
<g fill="{INK}"><circle cx="160" cy="350" r="7"/><circle cx="280" cy="350" r="7"/><circle cx="400" cy="350" r="7"/></g>
""", ground=False, arrow=True)

add('imaginary', '頭の中に思い浮かべた架空の生き物が、雲の中に描かれているイラスト。', f"""
{person(150,346,1.1,1,'violet','blue','think','bun','smile')}
<g transform="translate(390 190)">
  <path d="M-170 40q-16-70 50-84 20-56 96-40 46 6 60 54 74-8 82 60 4 60-64 66h-180q-46-4-44-56z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 20)">
    <ellipse rx="60" ry="34" class="violetp o"/>
    <circle cx="52" cy="-24" r="24" class="violetp o"/>
    <path d="M-40-24q-16-40 10-38 20 2 22 26z" class="violet o"/>
    <path d="M-60 20l-30 26M60 24l30 26" fill="none" stroke="{TONES['violet'][2]}" stroke-width="7" stroke-linecap="round"/>
    <circle cx="60" cy="-28" r="3.4" class="ink"/>
  </g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="230" cy="290" r="12"/><circle cx="256" cy="266" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('indirect', 'まっすぐ行けるのに、大きく回り込んで進む道のイラスト。', f"""
<circle cx="90" cy="200" r="24" class="teal o"/>
<circle cx="520" cy="200" r="24" class="coral o"/>
<path d="M120 200h370" class="muted"/>
<path d="M110 226q40 120 190 120t200-130" fill="none" stroke="{TONES['violet'][0]}" stroke-width="12" stroke-linecap="round" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('intelligent', '難しい問いに答えを見つけ、頭の上に明かりがひらめいた人のイラスト。', f"""
{person(280,346,1.2,1,'teal','blue','think','short','smile')}
<g transform="translate(280 160)">
  <circle r="40" class="goldp o"/>
  <path d="M-18 40h36v16h-36z" class="ink"/>
  <g class="golds" style="stroke-width:4"><path d="M0-56v-20M-46-30l-18-12M46-30l18-12"/></g>
</g>
<g transform="translate(450 280)">
  <path d="M-30-40q0-30 30-30t30 30q0 20-24 26v14h-12v-24q26-2 26-16 0-14-20-14t-20 14z" class="ink"/>
  <circle cy="40" r="7" class="ink"/>
</g>
<path d="M400 240q-40-30-60-40" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('international', '二つの国の旗の間を、線でつないだ地球のイラスト。', f"""
<circle cx="300" cy="210" r="130" class="bluep o"/>
<path d="M170 210h260M300 80v260" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
<path d="M300 80q60 60 0 260M300 80q-60 60 0 260" fill="none" stroke="{TONES['blue'][0]}" stroke-width="3"/>
<path d="M240 160q60 30 130 10q-20 60-90 60t-60-40z" class="greenp o"/>
<g>
  <path d="M120 340V180" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M126 186l60 18-60 18z" class="coral o"/>
  <path d="M480 340V180" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
  <path d="M474 186l-60 18 60 18z" class="teal o"/>
</g>
<path d="M150 220q150-60 300 0" class="muted" marker-start="url(#ar)" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('keen', '前のめりに身を乗り出して、強く関心を示している人のイラスト。', f"""
{person(220,346,1.15,1,'coral','blue','point','short','smile')}
<g transform="translate(430 250)">
  <path d="M-70-70h140v140h-140z" class="goldp o"/>
  <path d="M-40-30h80v80h-80z" class="gold o"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M300 180l30-24M310 220h34M296 140l6-30"/></g>
<path d="M280 260q40-14 74-8" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('local', '同じ町の中だけをつなぐ短い道と、その土地の店のイラスト。', f"""
<circle cx="300" cy="200" r="150" class="muted"/>
{building(200,270,0.7,'teal')}
{building(390,270,0.7,'gold')}
<path d="M230 300h130" fill="none" stroke="#e6dcc9" stroke-width="26" stroke-linecap="round"/>
{person(300,320,0.6,1,'coral','blue','walk','short','smile')}
<path d="M470 120l70-50" class="muted" marker-end="url(#ar)"/>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('obtain', '申し込んで、証明書を正式に受け取っているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="greenp"/>
<path d="M600 250H480" fill="none" stroke="{TONES['teal'][0]}" stroke-width="28" stroke-linecap="round"/>
<path d="M490 250h-40" fill="none" stroke="{SKIN}" stroke-width="20" stroke-linecap="round"/>
<g transform="translate(300 240) rotate(-4)">
  <path d="M-100-70h200v140h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-70-40h140M-70-14h140M-70 12h100"/></g>
  <circle cx="60" cy="40" r="20" class="coral o"/>
</g>
{person(150,346,1.05,1,'coral','blue','give','bob','smile')}
<circle cx="222" cy="246" r="14" fill="{SKIN}" stroke="{SKINL}" stroke-width="2.5"/>
<path d="M400 170H260" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('organization', '複数の人が線でつながり、一つの団体をつくっているイラスト。', f"""
<circle cx="300" cy="130" r="46" class="teal o"/>
<g class="tealp o"><circle cx="140" cy="280" r="40"/><circle cx="300" cy="280" r="40"/><circle cx="460" cy="280" r="40"/></g>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M300 176v64M300 208h-160v32M300 208h160v32"/></g>
<path d="M60 340h480" class="muted"/>
""", ground=False)

add('overlook', 'たくさんの点の中で一つだけ印を見落とし、通り過ぎているイラスト。', f"""
<g class="tealp o">
  {''.join(f'<circle cx="{100+ i%6*70}" cy="{150 + i//6*70}" r="22"/>' for i in range(18))}
</g>
<circle cx="310" cy="220" r="22" class="coral o"/>
<path d="M60 100q120 40 240 0t240 40" class="muted" marker-end="url(#ar)"/>
<g class="corals" style="stroke-width:5"><path d="M310 300v40"/></g>
<circle cx="310" cy="220" r="40" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"/>
""", ground=False, arrow=True)

add('physical', '体を動かして運動している人と、筋肉の動きを示したイラスト。', f"""
<circle cx="470" cy="100" r="56" class="coralp"/>
{person(280,346,1.3,1,'coral','blue','up','short','neutral')}
<g transform="translate(280 240)">
  <path d="M-120-20h240v20h-240z" class="ink"/>
  <circle cx="-140" cy="-10" r="30" class="ink"/><circle cx="140" cy="-10" r="30" class="ink"/>
</g>
<g class="corals" style="stroke-width:4"><path d="M170 300l-26 20M390 300l26 20"/></g>
<path d="M80 366h420" class="a"/>
""", ground=True)

add('practical', '飾りのない道具が、実際の作業でそのまま役に立っているイラスト。', f"""
<circle cx="120" cy="100" r="56" class="goldp"/>
<g transform="translate(300 260)">
  <path d="M-160-30h320v20h-320z" class="goldp o"/>
  <path d="M-140-10v70M140-10v70" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(220 190) rotate(-12)">
  <path d="M-44-24h88v30h-88z" class="goldd o"/>
  <path d="M0 6v50" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12" stroke-linecap="round"/>
</g>
<g transform="translate(380 200)">
  <path d="M-12-60h24v50h-24z" class="coral o"/>
  <path d="M-5-10h10v60h-5z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 150l18 18 30-36"/></g>
""", ground=True)

add('perceive', '目と耳から入った合図に気づいて、頭で受け取っているイラスト。', f"""
{person(220,346,1.15,1,'teal','blue','stand','short','neutral')}
<g transform="translate(300 210)">
  <ellipse rx="34" ry="20" fill="#fffdf6" class="o"/>
  <circle r="9" class="ink"/>
</g>
<g transform="translate(300 280)">
  <path d="M-16-24q34-14 34 24t-34 24" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g class="teals" marker-end="url(#ar)"><path d="M430 200h-90"/><path d="M430 280h-90"/></g>
<circle cx="470" cy="200" r="24" class="goldp o"/>
<circle cx="470" cy="280" r="24" class="coralp o"/>
<path d="M262 216q20-6 32-6" class="a" marker-start="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('obsess', '一つのことばかりが頭に浮かんで、離れなくなっているイラスト。', f"""
{person(200,346,1.15,1,'violet','blue','think','short','sad')}
<g transform="translate(400 190)">
  <circle r="90" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g class="coral o"><circle cx="0" cy="0" r="40"/></g>
  <g class="coralp o"><circle cx="-52" cy="-46" r="16"/><circle cx="54" cy="-42" r="16"/><circle cx="-48" cy="50" r="16"/><circle cx="50" cy="52" r="16"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="292" cy="266" r="13"/><circle cx="264" cy="292" r="9"/></g>
<path d="M400 300a90 90 0 0 1-70-70" class="muted" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(' '.join(W)); print(sheet(W))
