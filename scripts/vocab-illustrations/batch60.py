"""第60回: 爆発・欠陥・燃料・世代など41語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('explicit', 'あいまいな言い方と、はっきり書いた言い方を比べたイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="#cfd8e0"><rect x="-70" y="-50" width="140" height="16"/><rect x="-70" y="-10" width="100" height="16"/></g>
</g>
<g transform="translate(430 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-70" y="-50" width="140" height="18"/><rect x="-70" y="-10" width="140" height="18"/><rect x="-70" y="30" width="100" height="18"/></g>
</g>
<path d="M290 230h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 360l20 20 34-40"/></g>
""", ground=True, arrow=True)

add('explosion', '中心から一気にはじけ飛ぶ爆発のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M0-160l40 84 90-30-56 76 66 60-92-8-8 92-40-78-70 50 24-88-96-22 82-46z" class="coral o"/>
  <circle r="50" class="goldp o"/>
</g>
<g fill="{TONES['coral'][1]}"><circle cx="120" cy="330" r="12"/><circle cx="480" cy="330" r="10"/><circle cx="530" cy="120" r="9"/><circle cx="90" cy="120" r="8"/></g>
""", ground=False)

add('expression', '顔つきと言い回しで気持ちを表すイラスト。', f"""
{face(180,200,80,'smile')}
<g transform="translate(410 200)">
  <path d="M-100-60h200v90h-200z" fill="#fffdf6" class="o"/>
  <path d="M-60 30l-14 34 44-34z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-70" y="-34" width="140" height="16"/><rect x="-70" y="-6" width="100" height="16"/></g>
</g>
<path d="M280 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('extensive', '一面いっぱいに広がっているイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-230-120h460v240h-460z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="teal o">{''.join(f'<rect x="{-215+c*57}" y="{-105+r*77}" width="50" height="70"/>' for r in range(3) for c in range(8))}</g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M70 380h460M530 380H70"/></g>
""", ground=False, arrow=True)

add('external', '箱の外側についている部品のイラスト。', f"""
<g transform="translate(260 240)">
  <path d="M-140-110h280v220h-280z" fill="#dfe6ea" class="o"/>
  <g class="tealp o"><rect x="-100" y="-70" width="200" height="140"/></g>
</g>
<g transform="translate(470 250)">
  <path d="M-50-50h100v100h-100z" class="coral o"/>
  <path d="M-50 0h-60" fill="none" stroke="{INK}" stroke-width="8"/>
</g>
<circle cx="470" cy="250" r="76" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M470 140v40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('extra', '基本のぶんに、さらに一つ足されるイラスト。', f"""
<g class="tealp o"><rect x="120" y="220" width="80" height="100"/><rect x="210" y="220" width="80" height="100"/><rect x="300" y="220" width="80" height="100"/></g>
<g transform="translate(460 270)"><path d="M-40-50h80v100h-80z" class="coral o"/></g>
<g fill="{INK}" transform="translate(415 180)"><rect x="-24" y="-6" width="48" height="12"/><rect x="-6" y="-24" width="12" height="48"/></g>
<path d="M460 190v30" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('extraordinary', '並の高さを大きく越えた、並外れたイラスト。', f"""
<path d="M60 350h480" class="a"/>
<g class="tealp o">{''.join(f'<rect x="{100+i*60}" y="270" width="44" height="80"/>' for i in range(5))}</g>
<rect x="420" y="90" width="90" height="260" class="coral o"/>
<g class="golds" style="stroke-width:6"><path d="M400 70l-26-20M540 70l26-20"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M90 270h430"/></g>
""", ground=False)

add('fabulous', '思わず声が出るほど、すばらしいものを見るイラスト。', f"""
<g transform="translate(420 220)">
  <path d="M-90-60h180l-20 200h-140z" fill="#f7fbfe" class="o"/>
  <path d="M0-60l30 60-30 40-30-40z" class="violet o"/>
</g>
{person(150,346,1.1,1,'coral','gold','up','bob','smile')}
<g class="golds" style="stroke-width:6"><path d="M250 160l26-20M260 210h30M300 120l10-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('failed', '線が途中で切れて、うまくいかなかったイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-140h400v280h-400z" fill="#f7fbfe" class="o"/>
  <path d="M-170 100h340" fill="none" stroke="{MUTED}" stroke-width="3"/>
  <path d="M-170 60q80-60 140-80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8"/>
  <path d="M-30-20l40 60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-dasharray="14 12"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M60 40l50 50M110 40l-50 50"/></g>
</g>
""", ground=True)

add('failure', '機械が止まって動かなくなるイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-140-120h280v240h-280z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="12"><circle cx="-40" cy="-30" r="44"/><circle cx="50" cy="40" r="30"/></g>
  <g class="coral o"><circle cx="90" cy="-80" r="14"/></g>
  <g class="corals" style="stroke-width:5"><path d="M-120-140l-24-24M120-140l24-24"/></g>
</g>
<g class="muted" opacity=".9"><path d="M300 90q30-40 0-70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('farm', '畑を耕して作物を育てるイラスト。', f"""
{sun(500,90,28)}
<g fill="none" stroke="{TONES['green'][2]}" stroke-width="5"><path d="M120 340q80-30 160 0M120 370q80-30 160 0"/></g>
<g class="green o"><path d="M340 340q10-40 26-40t24 40zM420 340q10-40 26-40t24 40zM500 340q10-40 26-40t24 40z"/></g>
{person(180,300,1.0,1,'coral','blue','reach','cap','smile')}
<g transform="translate(250 290) rotate(30)"><path d="M-8-70h16v110h-16z" class="goldd o"/><path d="M-30 40h60v20h-60z" fill="#8b98a6" stroke="{INK}" stroke-width="2"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fatal', 'ひとつの傷が命取りになることを示したイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M0 90c-70-56-100-80-100-124a54 54 0 0 1 100-28 54 54 0 0 1 100 28c0 44-30 68-100 124z" class="coral o"/>
  <path d="M-20-60l60 90-60 40" fill="none" stroke="#fffdf6" stroke-width="10"/>
</g>
<g fill="none" stroke="{TONES['coral'][2]}" stroke-width="6"><path d="M170 340h260"/></g>
<g class="muted"><path d="M300 370v20"/></g>
""", ground=False)

add('fault', '割れ目という欠陥を指し示すイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-110h320v220h-320z" class="tealp o"/>
  <path d="M-40-110l30 80-40 60 50 80" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="270" cy="240" r="80"/></g>
<path d="M470 140l-80 60" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('favourable', '風が背中を押して、進みやすいイラスト。', f"""
{person(320,346,1.25,1,'teal','blue','walk','short','smile')}
<g class="muted" opacity=".9"><path d="M60 180q80-20 140 0M60 240q80-20 140 0M60 300q80-20 140 0"/></g>
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M90 210h120"/></g>
<path d="M420 220h100" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M470 320l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('feasible', '手もとの道具でやれる見通しが立つイラスト。', f"""
<g transform="translate(400 230)">
  <path d="M-120-110h240v220h-240z" fill="#e8f2fb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M-80-60h160v120h-160zM-80 0h160"/></g>
</g>
<g transform="translate(160 260)">
  <path d="M-70-20h40v70h-40z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M0-60h20v110H0z" class="coral o"/>
  <path d="M50-30h40v80H50z" class="goldd o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M270 170l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('federal', 'いくつもの州が一つの国にまとまるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-200-130h400v260h-400z" fill="none" stroke="{INK}" stroke-width="5"/>
  <g class="tealp o"><rect x="-190" y="-120" width="120" height="110"/><rect x="-60" y="-120" width="120" height="110"/><rect x="70" y="-120" width="120" height="110"/><rect x="-190" y="10" width="120" height="110"/><rect x="-60" y="10" width="120" height="110"/><rect x="70" y="10" width="120" height="110"/></g>
</g>
<g transform="translate(300 230)"><path d="M-4-160h8v40h-8z" class="ink"/><path d="M4-158h60v30H4z" class="coral o"/></g>
""", ground=False)

add('fellow', '同じしるしをつけた仲間どうしのイラスト。', f"""
{person(200,346,1.2,1,'teal','gold','give','short','smile')}
{person(400,346,1.2,-1,'teal','gold','give','bob','smile')}
<path d="M280 250h40" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g class="coral o"><circle cx="170" cy="250" r="12"/><circle cx="430" cy="250" r="12"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fence', '敷地を囲う板の柵のイラスト。', f"""
<g fill="#d9b476" stroke="{INK}" stroke-width="3">
  {''.join(f'<path d="M{90+i*62} 330v-140l24-24v164z"/>' for i in range(7))}
</g>
<g fill="#c9a06b" stroke="{INK}" stroke-width="2"><rect x="80" y="220" width="450" height="18"/><rect x="80" y="290" width="450" height="18"/></g>
<path d="M60 350h480" class="a"/>
""", ground=True)

add('fever', '体温計が高い値を示す、熱のあるイラスト。', f"""
{face(200,200,80,'flat')}
<g class="coralp"><circle cx="150" cy="230" r="20"/><circle cx="250" cy="230" r="20"/></g>
<g class="corals" opacity=".9" style="stroke-width:5"><path d="M290 140q26 26 26 50M330 120q34 34 34 66"/></g>
{thermometer(450,250,0.9,1.1)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fierce', '牙をむいて激しく襲いかかるイラスト。', f"""
<g transform="translate(320 240)">
  <ellipse rx="120" ry="90" fill="#c08d55" stroke="{INK}" stroke-width="3"/>
  <path d="M-60 20h120l-16 40h-88z" fill="#8b4a3e"/>
  <g fill="#fffdf6"><path d="M-50 20l14 30-24-24zM50 20l-14 30 24-24z"/><path d="M-20 60l10 24-20-16zM20 60l-10 24 20-16z"/></g>
  <g fill="{INK}"><path d="M-70-40l40 20-40 20zM70-40l-40 20 40 20z"/></g>
</g>
<g class="corals" style="stroke-width:6"><path d="M120 150l-30-24M520 150l30-24"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fighting', '両者がぶつかり合って争うイラスト。', f"""
{person(190,346,1.2,1,'coral','blue','point','short','flat')}
{person(410,346,1.2,-1,'teal','gold','point','bob','flat')}
<g transform="translate(300 220)">
  <path d="M0-60l24 46 52 6-38 36 10 52-48-26-48 26 10-52-38-36 52-6z" class="coralp o"/>
</g>
<g class="corals" style="stroke-width:5"><path d="M300 120v-24M240 140l-20-20M360 140l20-20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('film', 'カメラを回して場面を撮るイラスト。', f"""
<g transform="translate(180 260)">
  <path d="M-80-50h160v100h-160z" fill="#2f4055"/>
  <path d="M80-20l60-36v92l-60-36z" fill="#2f4055"/>
  <circle cx="-30" cy="-70" r="26" fill="#41506a" stroke="{INK}" stroke-width="3"/>
  <circle cx="30" cy="-70" r="26" fill="#41506a" stroke="{INK}" stroke-width="3"/>
  <path d="M-40 50h80v60h-80z" fill="#41506a"/>
</g>
<g transform="translate(430 260)">{person(430,260,1.0,-1,'coral','gold','up','bob','smile')}</g>
<path d="M290 220h60" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('finally', '長い道の末に、ついに旗へたどり着くイラスト。', f"""
<path d="M100 340q120-60 200 0t180-40" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="14 12"/>
{person(420,300,1.1,1,'coral','blue','up','short','smile')}
<g transform="translate(500 250)"><path d="M-4-90h8v100h-8z" class="ink"/><path d="M4-88h60v40H4z" class="coral o"/></g>
<g opacity=".3">{person(140,340,0.8,1,'coral','blue','walk','short','neutral')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('firstly', '手順の一番目を指し示すイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-180-140h360v280h-360z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-100-80h240M-100-20h240M-100 40h240M-100 100h200"/></g>
  <g class="tealp o"><circle cx="-140" cy="-20" r="20"/><circle cx="-140" cy="40" r="20"/><circle cx="-140" cy="100" r="20"/></g>
  <g class="coral o"><circle cx="-140" cy="-80" r="24"/></g>
  <g fill="#fffdf6"><rect x="-144" y="-94" width="8" height="28"/></g>
</g>
<path d="M500 140h-40" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('flag', '風にはためく一本の旗のイラスト。', f"""
<g transform="translate(240 220)">
  <path d="M-8-160h16v320h-16z" class="ink"/>
  <path d="M8-150q80 20 160 0 20 60 0 110-80 20-160 0z" class="coral o"/>
</g>
<g class="muted"><path d="M440 130q30 20 0 40M470 190q30 20 0 40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('flawed', '一か所ひび割れて、欠陥のあるイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M50-110l20 20 34-40"/></g>
</g>
<g transform="translate(430 240)">
  <path d="M-80-80h160v160h-160z" class="tealp o"/>
  <path d="M-20-80l20 50-40 40 30 50" fill="none" stroke="{INK}" stroke-width="6"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M50-110l30 30M80-110l-30 30"/></g>
</g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('flexible', 'よく曲がる棒と、折れる棒を比べたイラスト。', f"""
<path d="M110 300q90-160 180 0" fill="none" stroke="{TONES['teal'][0]}" stroke-width="18" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M170 350l20 20 34-40"/></g>
<path d="M340 260h80M450 300h80" fill="none" stroke="{TONES['coral'][0]}" stroke-width="18" stroke-linecap="round"/>
<g class="corals" style="stroke-width:5"><path d="M435 240v-26"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M430 350l30 30M460 350l-30 30"/></g>
""", ground=False)

add('flour', '袋から出した白い小麦粉のイラスト。', f"""
<g transform="translate(230 250)">
  <path d="M-80-90h160l-10 190h-140z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-40" y="-40" width="80" height="14"/></g>
  <path d="M-80-90q80-30 160 0" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="#fffdf6" stroke="{MUTED}" stroke-width="2"><ellipse cx="430" cy="330" rx="90" ry="30"/><ellipse cx="430" cy="316" rx="60" ry="20"/></g>
<g fill="#fffdf6" opacity=".9"><circle cx="380" cy="250" r="7"/><circle cx="420" cy="220" r="5"/><circle cx="450" cy="260" r="6"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('folding', '折りたたんで小さくできる椅子のイラスト。', f"""
<g transform="translate(170 260)">
  <path d="M-70-20h140v20h-140z" class="goldd o"/>
  <path d="M-70-20h20v-80h-20z" class="goldd o"/>
  <path d="M-60 0l-20 80M60 0l20 80" fill="none" stroke="{TONES['gold'][2]}" stroke-width="12"/>
</g>
<g transform="translate(440 260) rotate(-8)">
  <path d="M-20-100h40v200h-40z" class="goldd o"/>
  <path d="M20-90h30v180H20z" class="goldp o"/>
</g>
<path d="M290 240h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('fond', '大事なものを胸に抱いて、好きだと示すイラスト。', f"""
{person(280,346,1.3,1,'coral','gold','carry','bob','smile')}
<g transform="translate(280 250)">
  <ellipse rx="46" ry="34" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <circle cx="34" cy="-24" r="24" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <circle cx="42" cy="-28" r="4" class="ink"/>
</g>
<g transform="translate(400 170)">
  <path d="M0 30c-30-24-42-34-42-52a22 22 0 0 1 42-12 22 22 0 0 1 42 12c0 18-12 28-42 52z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('forgetful', '思い出せなくて、頭に空白があるイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','think','short','flat')}
<g transform="translate(430 200)">
  <path d="M-120-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="-50" y="-40" width="100" height="70"/></g>
  <g fill="{INK}"><path d="M74-10q0-26 20-26t20 26q0 14-16 18v12h-10v-20q14-4 14-14t-8-10-10 12z"/><rect x="82" y="34" width="10" height="10"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="300" cy="300" r="12"/><circle cx="276" cy="324" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('former', '二つ並ぶうち、前のほうを指すイラスト。', f"""
<g transform="translate(180 240)"><path d="M-90-70h180v140h-180z" class="coral o"/></g>
<g transform="translate(430 240)"><path d="M-90-70h180v140h-180z" class="tealp o"/></g>
<path d="M180 120v40" class="a" marker-end="url(#ar)"/>
<g class="a" style="stroke-dasharray:0" marker-end="url(#ar)"><path d="M120 350h360"/></g>
""", ground=False, arrow=True)

add('forthcoming', 'すぐ先の予定が近づいてくるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-130h380v260h-380z" class="paper"/>
  <path d="M-190-130h380v50h-380z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-190+c*95}-80v210"/>' for c in range(1,4))}{''.join(f'<path d="M-190 {-10+r*70}h380"/>' for r in range(2))}</g>
  <circle cx="0" cy="25" r="28" class="coral o"/>
  <circle cx="-95" cy="-45" r="20" class="tealp o"/>
</g>
<path d="M420 100l-60 60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('fortunate', 'たまたま良い方に転がって、運のよいイラスト。', f"""
{person(180,346,1.2,1,'coral','gold','up','bob','smile')}
<g transform="translate(430 250)">
  <g class="green o">
    <ellipse cy="-36" rx="28" ry="34"/><ellipse cx="36" rx="34" ry="28"/><ellipse cy="36" rx="28" ry="34"/><ellipse cx="-36" rx="34" ry="28"/>
  </g>
  <path d="M0 36v50" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M280 170l26-20M290 210h30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fortunately', '落ちる寸前で受け止められ、事なきを得るイラスト。', f"""
<g transform="translate(300 200)"><path d="M-50-40h100v70h-100z" class="goldd o"/></g>
<path d="M300 240v50" class="a" marker-end="url(#ar)"/>
{hand(300,330,1)}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M450 200l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('found', '礎石を据えて、新しく組織を起こすイラスト。', f"""
<g transform="translate(300 330)">
  <path d="M-160-20h320v40h-320z" fill="#c9d3dc" class="o"/>
  <path d="M-60-40h120v20h-120z" class="goldd o"/>
</g>
<g transform="translate(300 220)">
  <path d="M-110-60h220v120h-220z" class="teal o"/>
  <path d="M-130-60l130-70 130 70z" class="teald o"/>
</g>
{person(120,346,0.8,1,'coral','blue','reach','short','smile')}
<path d="M470 200v60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('frequent', '短い間をおいて、たびたび起こるイラスト。', f"""
<path d="M60 250h480" fill="none" stroke="{MUTED}" stroke-width="4"/>
<g class="coral o">{''.join(f'<circle cx="{100+i*44}" cy="250" r="16"/>' for i in range(10))}</g>
<g class="a" marker-end="url(#ar)"><path d="M100 330h44M144 330h-44"/></g>
<path d="M60 380h480" class="a"/>
""", ground=False, arrow=True)

add('friendship', '肩を組んだ二人のあいだに絆があるイラスト。', f"""
{person(230,346,1.2,1,'teal','blue','give','short','smile')}
{person(370,346,1.2,-1,'coral','gold','give','bob','smile')}
<path d="M295 250h20" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(300 160)">
  <path d="M0 40c-40-30-56-46-56-68a30 30 0 0 1 56-16 30 30 0 0 1 56 16c0 22-16 38-56 68z" class="coralp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('frustrated', 'うまく通らず、いら立っているイラスト。', f"""
{person(200,346,1.25,1,'coral','blue','up','short','flat')}
<g transform="translate(430 250)"><path d="M-20-120h40v240h-40z" fill="#c9d3dc" class="o"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M300 230h90"/></g>
<g class="corals" style="stroke-width:5"><path d="M140 170q-24 16-24 44M270 170q24 16 24 44"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('frustrating', '鍵が合わず、もどかしいイラスト。', f"""
<g transform="translate(380 250)">
  <path d="M-100-140h200v280h-200z" class="goldd o"/>
  <circle cx="50" cy="0" r="14" class="ink"/>
</g>
<g transform="translate(230 250) rotate(-10)">
  <circle r="30" fill="none" stroke="{INK}" stroke-width="10"/>
  <path d="M26 0h90v18h-90z" class="ink"/>
  <path d="M96 18h14v20H96z" class="ink"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M290 150l34 34M324 150l-34 34"/></g>
{drop(160,200,0.7)}
<path d="M60 386h480" class="a"/>
""", ground=True)

add('fuel', '燃料を入れて火を強めるイラスト。', f"""
<g transform="translate(180 240) rotate(20)">
  <path d="M-60-60h120v120h-120z" fill="#c9d3dc" class="o"/>
  <path d="M60-40q60 6 80 40" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M-30-80h60v20h-60z" fill="#dbe3ea" class="o"/>
</g>
<path d="M330 260q10 30 6 50" fill="none" stroke="{TONES['gold'][0]}" stroke-width="10" stroke-linecap="round"/>
{flame(400,300,1.4)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('function', 'ボタンを押すと決まった働きをするイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-90-70h180v140h-180z" fill="#dfe6ea" class="o"/>
  <circle cy="0" r="34" class="coral o"/>
</g>
{hand(200,140,1)}
<g transform="translate(450 250)">
  <g fill="none" stroke="{INK}" stroke-width="12"><circle r="50"/></g>
  <g fill="{INK}">{''.join(f'<rect x="-8" y="-70" width="16" height="20" transform="rotate({i*60})"/>' for i in range(6))}</g>
</g>
<path d="M310 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('fundamental', '積み上げのいちばん下の土台を示したイラスト。', f"""
<g class="tealp o"><rect x="230" y="150" width="140" height="60"/><rect x="210" y="215" width="180" height="60"/></g>
<rect x="170" y="280" width="260" height="70" class="coral o"/>
<path d="M300 400v-30" class="a" marker-end="url(#ar)" transform="rotate(180 300 385)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
