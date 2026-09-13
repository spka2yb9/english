"""第71回: 版・被害者・警告・価値など44語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('version', '同じものの新旧の版を並べたイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-80-90h160v180h-160z" class="tealp o"/>
  <g fill="{TONES['teal'][2]}"><rect x="-40" y="-50" width="80" height="16"/><rect x="-40" y="-16" width="60" height="16"/></g>
  <g fill="{INK}"><rect x="-20" y="50" width="14" height="10"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80-90h160v180h-160z" class="teal o"/>
  <g fill="#fffdf6"><rect x="-40" y="-50" width="80" height="16"/><rect x="-40" y="-16" width="70" height="16"/><rect x="-40" y="18" width="50" height="16"/></g>
  <g fill="#fffdf6"><rect x="-24" y="50" width="30" height="10"/></g>
</g>
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('vertical', 'まっすぐ上下に立つ線のイラスト。', f"""
<path d="M300 80v260" fill="none" stroke="{TONES['teal'][0]}" stroke-width="20" stroke-linecap="round"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M120 340h360"/></g>
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M300 300h-40v40"/></g>
<path d="M420 340v-200" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('very', '目盛りがぐっと端まで振れているイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-170 40a170 170 0 0 1 340 0z" fill="#f7fbfe" class="o"/>
  <path d="M0 40L140 10" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="40" r="12" class="ink"/>
  <g fill="none" stroke="{MUTED}" stroke-width="4">{''.join(f'<path d="M0 40l{int(-150*__import__("math").cos(i*3.14159/8))} {int(40-150*__import__("math").sin(i*3.14159/8))}" opacity=".4"/>' for i in range(9))}</g>
</g>
<g class="corals" style="stroke-width:5"><path d="M480 180l24-18"/></g>
<path d="M60 320h480" class="a"/>
""", ground=True)

add('viable', '手もとの道具でやっていけると見通すイラスト。', f"""
<g transform="translate(400 240)">
  <path d="M-110-100h220v200h-220z" fill="#e8f2fb" class="o"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M-70 60h140v-120h-140zM-70 0h140"/></g>
</g>
<g transform="translate(160 260)">
  <path d="M-60-20h40v70h-40z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M10-60h20v110H10z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M260 160l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('vibrant', '色があざやかで、活気にあふれるイラスト。', f"""
<g transform="translate(160 240)"><circle r="60" class="coral o"/></g>
<g transform="translate(300 220)"><path d="M-56-56h112v112h-112z" class="gold o"/></g>
<g transform="translate(450 250)"><path d="M0-70l70 130h-140z" class="violet o"/></g>
<g class="golds" style="stroke-width:6"><path d="M120 140l-24-18M340 130l24-18M520 160l24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('vicious', '悪意をもって、わざと傷つけるイラスト。', f"""
{person(180,346,1.2,1,'violet','violet','point','cap','flat')}
<g transform="translate(300 200)">
  <path d="M-70-50l24 14-6-30 30 18 10-32 22 26 20-22 6 32 30-8-14 28 26 12-30 20h-118z" class="coralp o"/>
</g>
{person(470,346,1.15,-1,'teal','gold','stand','bob','sad')}
<path d="M240 160h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 180l28 28M148 180l-28 28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('victim', '被害を受けた側を示したイラスト。', f"""
{person(400,346,1.2,-1,'coral','gold','stand','bob','sad')}
<g transform="translate(400 250)">
  <path d="M-40-10h30v20h-30z" fill="#f7e6bd" stroke="{INK}" stroke-width="2"/>
</g>
{person(160,346,1.15,1,'violet','violet','point','cap','flat')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M240 240h80"/></g>
<circle cx="400" cy="280" r="90" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('viewer', '画面を見ている視聴者のイラスト。', f"""
<g transform="translate(400 230)">
  <path d="M-140-110h280v200h-280z" fill="#41506a"/>
  <path d="M-116-88h232v172h-232z" class="bluep"/>
  <g transform="translate(0 30) scale(0.5)">{person(0,20,1.0,1,'coral','gold','up','bob','smile')}</g>
  <path d="M-40 90h80v26h-80z" fill="#41506a"/>
</g>
{person(150,346,1.1,1,'teal','blue','stand','short','smile')}
<path d="M220 240h40" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('virtual', '画面の中に作られた仮の世界のイラスト。', f"""
<g transform="translate(380 230)">
  <path d="M-140-110h280v220h-280z" fill="#1f2b3d"/>
  <g fill="none" stroke="#7fd6c2" stroke-width="4"><path d="M-90 60h180v-120h-180zM-90-60l90-40 90 40"/></g>
  <g fill="#7fd6c2" opacity=".5"><rect x="-40" y="-10" width="80" height="70"/></g>
</g>
{person(140,346,1.0,1,'teal','blue','reach','short','smile')}
<path d="M210 240h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('visual', '目で見て分かる図で示したイラスト。', f"""
<g transform="translate(330 220)">
  <path d="M-150-120h300v240h-300z" fill="#fffdf6" class="o"/>
  <g fill="{TONES['teal'][0]}"><rect x="-110" y="20" width="50" height="80"/><rect x="-40" y="-30" width="50" height="130"/><rect x="30" y="-80" width="50" height="180"/></g>
</g>
<g transform="translate(140 250)">
  <ellipse rx="60" ry="40" fill="#fffdf6" class="o"/>
  <circle r="18" class="ink"/>
</g>
<path d="M210 250h30" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('vocal', '声を張って、はっきり主張するイラスト。', f"""
{person(180,346,1.25,1,'coral','blue','up','short','flat')}
<g transform="translate(230 200)"><ellipse rx="20" ry="16" fill="#8b4a3e"/></g>
<g class="corals" opacity=".9" style="stroke-width:7"><path d="M300 160q34 40 34 80t-34 80M370 130q46 56 46 110t-46 110"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('voluntary', '自分から手を挙げて引き受けるイラスト。', f"""
{person(200,346,1.3,1,'teal','blue','up','short','smile')}
{person(430,346,1.05,1,'gold','blue','stand','bob','neutral')}
{person(520,346,1.05,1,'coral','blue','stand','cap','neutral')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M300 180l20 20 34-40"/></g>
<g class="a" marker-end="url(#ar)"><path d="M200 130v-30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('vulnerable', '守りがなく、傷つきやすい状態のイラスト。', f"""
{person(300,346,1.2,1,'coral','gold','stand','bob','sad')}
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M220 200q80-40 160 0"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M110 200h80M490 200h-80M110 300h80M490 300h-80"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('warning', '注意をうながす警告の標示のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M0-130l150 260h-300z" fill="#f3e3ae" stroke="{INK}" stroke-width="5"/>
  <g fill="{INK}"><rect x="-16" y="-50" width="32" height="100"/><rect x="-16" y="70" width="32" height="32"/></g>
</g>
<g class="corals" style="stroke-width:5"><path d="M480 150l24-18M120 150l-24-18"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('waste', '使わずに捨てられて、むだになるイラスト。', f"""
<g transform="translate(180 250)">
  <path d="M-70-60h140v130h-140z" class="tealp o"/>
</g>
<g transform="translate(430 280)">
  <path d="M-80 60h160l-14-140h-132z" fill="#8b8161" stroke="{INK}" stroke-width="3"/>
  <path d="M-90-90h180v20h-180z" fill="#6f6a4a"/>
</g>
<path d="M280 220q70-50 120 0" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M290 320l30 30M320 320l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('wealthy', 'お金がたっぷりある富裕なイラスト。', f"""
{person(180,346,1.25,1,'violet','blue','stand','short','smile')}
<g transform="translate(420 280)">
  <path d="M-90-40h180v100h-180z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <g class="goldd o"><circle cx="-40" cy="-70" r="26"/><circle cx="10" cy="-80" r="26"/><circle cx="56" cy="-66" r="26"/></g>
</g>
<g class="golds" style="stroke-width:5"><path d="M300 190l24-18M310 230h28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('weekly', '一週ごとに同じ印がつくイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-220-120h440v240h-440z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M{-220+c*63}-120v240"/>' for c in range(1,7))}{''.join(f'<path d="M-220 {-40+r*80}h440"/>' for r in range(2))}</g>
  <g class="coral o"><circle cx="-190" cy="-80" r="20"/><circle cx="-190" cy="0" r="20"/><circle cx="-190" cy="80" r="20"/></g>
</g>
<path d="M480 380v-60" class="a" marker-end="url(#ar)" transform="rotate(180 480 350)"/>
""", ground=False, arrow=True)

add('weird', '見なれない、おかしな形のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-70-70q80-40 110 20t-20 100-110 10-10-90 30-40z" fill="#a9a9c9" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><circle cx="-30" cy="-10" r="10"/><circle cx="30" cy="10" r="10"/></g>
  <path d="M-20 50q40 20 60-10" fill="none" stroke="{INK}" stroke-width="4"/>
  <path d="M-40-70l-10-40M40-60l20-40" fill="none" stroke="{INK}" stroke-width="4"/>
</g>
<g fill="{INK}" transform="translate(480 150)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('whatever', 'どれでもかまわないと、全部を受け入れるイラスト。', f"""
<g class="tealp o"><circle cx="140" cy="200" r="34"/><rect x="240" y="166" width="68" height="68"/><path d="M420 234l40-68 40 68z"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">
  <path d="M120 300l14 14 24-30"/><path d="M260 300l14 14 24-30"/><path d="M440 300l14 14 24-30"/>
</g>
""", ground=False)

add('widespread', '広い範囲に一様に行きわたるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-220-140h440v280h-440z" class="paper"/>
  <path d="M-200 20q120-50 220 0t200-30" fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"/>
  <g class="coralp o">{''.join(f'<circle cx="{-180+c*72}" cy="{-100+r*80}" r="20"/>' for r in range(4) for c in range(6))}</g>
</g>
""", ground=True)

add('will', 'これからやると決めて、前を向くイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','point','short','neutral')}
<path d="M290 230h100" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="410" y="180" width="120" height="100"/></g>
<g transform="translate(200 170)">
  <path d="M-60-40h120v50h-120z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="4" marker-end="url(#ar)"><path d="M-36-16h50"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('willing', 'すすんで手を貸そうとするイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','up','short','smile')}
<g transform="translate(420 280)">
  <path d="M-70-30h140v70h-140z" class="goldd o"/>
</g>
<path d="M290 250h60" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M120 190l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('win', '一位でゴールして勝つイラスト。', f"""
{person(280,346,1.3,1,'coral','blue','up','short','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6"><path d="M180 250q100-24 200 0"/></g>
<g transform="translate(280 140)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
<g opacity=".4">{person(460,346,1.1,1,'teal','gold','walk','bob','neutral')}</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('wing', '鳥の広げた羽のイラスト。', f"""
<g transform="translate(300 240)">
  <ellipse rx="60" ry="40" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <circle cx="50" cy="-30" r="26" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <path d="M70-36l26 8-26 12z" class="gold o"/>
  <path d="M-30-30q-90-70-160-10 60 70 160 30z" fill="#c08d55" stroke="{INK}" stroke-width="3"/>
  <path d="M-30-20q-70-40-130-6" fill="none" stroke="{INK}" stroke-width="2"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><ellipse cx="180" cy="210" rx="100" ry="50" transform="rotate(-12 180 210)"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('wise', '長く生きた人が、深い知恵で助言するイラスト。', f"""
{person(180,346,1.25,1,'violet','blue','point','short','smile')}
<g transform="translate(430 200)">
  <path d="M-120-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-156q-38-4-36-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 -6)"><circle r="34" class="goldp o"/><g class="golds" style="stroke-width:4"><path d="M0-50v-12M-34-34l-12-8M34-34l12-8"/></g></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('wool', 'ふわふわの羊毛と毛糸玉のイラスト。', f"""
<g transform="translate(200 270)">
  <g fill="#fffdf6" stroke="{MUTED}" stroke-width="2"><circle cx="-40" cy="-20" r="40"/><circle cx="20" cy="-30" r="44"/><circle cx="0" cy="20" r="40"/><circle cx="60" cy="10" r="36"/></g>
</g>
<g transform="translate(440 280)">
  <circle r="60" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#d9c286" stroke-width="3"><path d="M-50-20q50 30 100 0M-50 20q50 30 100 0M-40-50q40 40 90 20"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('worth', 'その品に見合う値がついているイラスト。', f"""
{box(170,250,140,110,28,'teal')}
<g transform="translate(300 170)">
  <path d="M-6-40h12v60h-12z" class="ink"/>
  <path d="M-120 20h240" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-120 20v40M120 20v40" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(420 260)"><circle r="30" class="goldd o"/><circle cx="-40" cy="10" r="30" class="goldd o"/></g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M290 340h40"/></g>
""", ground=False)

add('worthwhile', '手間をかけた分、見返りが大きいイラスト。', f"""
<g transform="translate(160 260)">
  <path d="M-60-30h120v70h-120z" class="goldd o"/>
  {drop(160,180,0.7)}
</g>
<g transform="translate(430 240)">
  <path d="M0-70l24 50 54 6-40 38 10 54-48-28-48 28 10-54-40-38 54-6z" class="gold o"/>
</g>
<path d="M270 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 350l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('worthy', 'たたえられるにふさわしいイラスト。', f"""
{person(220,346,1.3,1,'teal','blue','stand','short','smile')}
<g transform="translate(430 230)">
  <path d="M-70-70h140v140h-140z" class="paper"/>
  <g transform="translate(0 -10)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-40 40h80"/></g>
</g>
<path d="M310 250h40" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 190l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('wrong', '進む向きを間違えているイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','walk','short','flat')}
<path d="M280 250h140" fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10" marker-end="url(#ar)"/>
<g transform="translate(480 250)">
  <path d="M0-60l60 120h-120z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><rect x="-6" y="-16" width="12" height="40"/><rect x="-6" y="34" width="12" height="12"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M300 150l50 50M350 150l-50 50"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('young', '芽と子どもで、若さを示したイラスト。', f"""
{person(430,346,0.8,1,'coral','gold','up','cap','smile')}
<g transform="translate(200 330)">
  <path d="M0 20v-70" fill="none" stroke="{TONES['green'][2]}" stroke-width="7"/>
  <g class="green o"><ellipse cx="-26" cy="-48" rx="26" ry="14" transform="rotate(-22 -26 -48)"/><ellipse cx="26" cy="-66" rx="26" ry="14" transform="rotate(22 26 -66)"/></g>
</g>
{sun(510,100,26)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('youth', '若い人たちが並ぶ、青年期のイラスト。', f"""
{person(170,346,1.05,1,'coral','gold','up','cap','smile')}
{person(300,346,1.1,1,'teal','blue','up','bob','smile')}
{person(430,346,1.05,1,'gold','blue','up','short','smile')}
<g class="a" marker-end="url(#ar)"><path d="M150 160h300"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('abortion', '進めていた計画を途中で打ち切るイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-200-30h230v60h-230z" class="teal o"/>
  <g fill="none" stroke="{MUTED}" stroke-width="5" stroke-dasharray="12 10"><path d="M30 0h170"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"><path d="M300 160l50 50M350 160l-50 50"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True)

add('absence', '席がひとつだけ空いているイラスト。', f"""
<g transform="translate(300 310)">
  <g class="goldd o"><rect x="-230" y="-20" width="130" height="20"/><rect x="-65" y="-20" width="130" height="20"/><rect x="100" y="-20" width="130" height="20"/></g>
  <g class="goldd o"><rect x="-230" y="-90" width="20" height="70"/><rect x="-65" y="-90" width="20" height="70"/><rect x="100" y="-90" width="20" height="70"/></g>
</g>
{person(120,300,0.8,1,'teal','blue','stand','short','smile')}
{person(480,300,0.8,1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="240" y="190" width="120" height="120" rx="10"/></g>
<path d="M300 150v30" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('absolutely', '一分のすきもなく、完全にそろっているイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-130h380v260h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-90+i*45}h240"/>' for i in range(5))}</g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="7" stroke-linecap="round">{''.join(f'<path d="M-150 {-96+i*45}l14 14 24-30"/>' for i in range(5))}</g>
</g>
""", ground=True)

add('abundance', 'あふれるほど豊かに実るイラスト。', f"""
<g transform="translate(300 290)">
  <path d="M-150-30h300l-24 100h-252z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g class="coral o"><circle cx="-90" cy="-50" r="30"/><circle cx="-30" cy="-70" r="30"/><circle cx="30" cy="-52" r="30"/><circle cx="90" cy="-64" r="30"/></g>
  <g class="green o"><circle cx="-60" cy="-104" r="26"/><circle cx="20" cy="-112" r="26"/><circle cx="90" cy="-116" r="24"/></g>
</g>
<g class="golds" style="stroke-width:5"><path d="M480 160l24-18M120 160l-24-18"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('accent', '同じ語の一部が強く発音されるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-190-90h380v180h-380z" class="paper"/>
  <g fill="{MUTED}"><rect x="-150" y="-20" width="70" height="20"/><rect x="10" y="-20" width="80" height="20"/><rect x="110" y="-20" width="60" height="20"/></g>
  <g fill="{INK}"><rect x="-70" y="-26" width="70" height="32"/></g>
  <g class="corals" style="stroke-width:5"><path d="M-50-50q26-20 50 0"/></g>
</g>
""", ground=True)

add('acceptance', '差し出されたものを受け取って認めるイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','give','short','smile')}
<g transform="translate(300 250)">
  <path d="M-60-40h120v70h-120z" class="paper"/>
</g>
{person(470,346,1.15,-1,'blue','blue','reach','bob','smile')}
<path d="M240 300h140" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 170l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('access', '鍵で戸が開いて、中に入れるイラスト。', f"""
<g transform="translate(390 240)">
  <path d="M-100-140h200v280h-200z" class="goldd o"/>
  <circle cx="60" cy="0" r="12" class="ink"/>
</g>
<g transform="translate(230 240) rotate(-10)">
  <circle r="26" fill="none" stroke="{INK}" stroke-width="9"/>
  <path d="M22 0h80v16H22z" class="ink"/>
  <path d="M84 16h14v18H84z" class="ink"/>
</g>
<path d="M150 320h180" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('accordance', '見本と現物がぴたりと一致するイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-80h160v160h-160z" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="11 9"/>
  <circle r="50" class="tealp o"/>
</g>
<g transform="translate(430 240)">
  <path d="M-80-80h160v160h-160z" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle r="50" class="teal o"/>
</g>
<g fill="none" stroke="{INK}" stroke-width="6"><path d="M290 220h30M290 250h30"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M280 350l20 20 34-40"/></g>
""", ground=True)

add('accountability', '数字を示して、説明の責めを果たすイラスト。', f"""
{person(150,346,1.2,1,'blue','blue','point','short','neutral')}
<g transform="translate(400 230)">
  <path d="M-130-110h260v220h-260z" fill="#f7fbfe" class="o"/>
  <g fill="{TONES['teal'][0]}"><rect x="-90" y="20" width="44" height="70"/><rect x="-30" y="-30" width="44" height="120"/><rect x="30" y="-70" width="44" height="160"/></g>
  <g fill="{INK}"><rect x="-90" y="-90" width="100" height="14"/></g>
</g>
{person(540,346,0.9,-1,'coral','gold','stand','bob','neutral')}
<path d="M240 200h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('accountant', '帳簿と電卓で計算する会計係のイラスト。', f"""
{person(160,340,1.1,1,'blue','blue','reach','bob','neutral')}
<g transform="translate(330 260)">
  <path d="M-100-80h200v160h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-70 {-50+i*30}h140"/>' for i in range(4))}</g>
  <g fill="{INK}"><rect x="-70" y="-70" width="90" height="12"/></g>
</g>
<g transform="translate(480 280)">
  <path d="M-40-60h80v120h-80z" fill="#dfe6ea" class="o"/>
  <g fill="{INK}"><rect x="-28" y="-46" width="56" height="20"/>{''.join(f'<rect x="{-28+c*20}" y="{-14+r*24}" width="14" height="14"/>' for r in range(3) for c in range(3))}</g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('accumulation', '少しずつ積み上がって、たまっていくイラスト。', f"""
<path d="M60 350h480" class="a"/>
<g class="teal o">
  {''.join(f'<rect x="{100+c*70}" y="{330-r*22}" width="56" height="20"/>' for c in range(6) for r in range(c+1))}
</g>
<path d="M120 150h400" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('accuracy', '矢が的の中心に集まるイラスト。', f"""
<g transform="translate(320 220)">
  <circle r="140" fill="#fffdf6" class="o"/>
  <circle r="96" class="coralp o"/>
  <circle r="52" fill="#fffdf6" class="o"/>
  <circle r="20" class="coral o"/>
  <g fill="{INK}"><circle cx="-8" cy="-6" r="7"/><circle cx="6" cy="8" r="7"/><circle cx="10" cy="-10" r="7"/></g>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M110 340l20 20 34-40"/></g>
""", ground=False)

add('accusation', '指をさして非難の申し立てをするイラスト。', f"""
{person(150,346,1.2,1,'blue','blue','point','short','flat')}
<g transform="translate(320 220)">
  <path d="M-70-60h140v120h-140z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3"><path d="M-46-30h92M-46 0h92"/></g>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="7"><path d="M-40 34h80"/></g>
</g>
{person(480,346,1.15,-1,'coral','gold','up','bob','sad')}
<path d="M400 250h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
