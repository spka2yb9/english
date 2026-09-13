"""第80回（3,000語到達）: 検査・例外・期待・欠点など46語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('comparative', '二つを並べて比べる見方のイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-90-90h180v180h-180z" class="tealp o"/>
  <circle r="40" class="teal o"/>
</g>
<g transform="translate(430 230)">
  <path d="M-90-90h180v180h-180z" class="coralp o"/>
  <path d="M-40-40h80v80h-80z" class="coral o"/>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M300 120v220"/></g>
<g class="a" marker-end="url(#ar)"><path d="M270 370h-60M330 370h60"/></g>
""", ground=False, arrow=True)

add('constitutional', '憲法に沿っているかを照らすイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-120-130h240v260h-240z" class="violet o"/>
  <path d="M-100-110h200v220h-200z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-60" y="-80" width="120" height="18"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-60 {-30+i*30}h120"/>' for i in range(4))}</g>
</g>
<g transform="translate(450 240)">
  <path d="M-80-70h160v140h-160z" class="paper"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M-30 0l20 20 34-40"/></g>
</g>
<path d="M340 240h30" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('convincing', '筋の通った説明で相手を納得させるイラスト。', f"""
{person(150,346,1.15,1,'blue','blue','point','short','neutral')}
<g transform="translate(330 200)">
  <path d="M-90-60h180v90h-180z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M-60-30h60M-60-6h60M-60 18h40"/></g>
</g>
{person(490,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M440 290l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('critical', '全体を支える、きわめて重要な一点のイラスト。', f"""
{box(300,170,220,80,0,'gold')}
<g transform="translate(300 300)">
  <path d="M-160-40h320v30h-320z" class="teal o"/>
  <path d="M-130-10h40v70h-40zM90-10h40v70H90z" class="tealp o"/>
  <path d="M-20-10h40v70h-40z" class="coral o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="300" cy="320" r="60"/></g>
<path d="M470 330h-100" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('crucial', 'そこが抜けると崩れる決め手のイラスト。', f"""
<g transform="translate(200 250)">
  <g class="teal o">{''.join(f'<rect x="{-80+c*56}" y="{-60+r*56}" width="50" height="50"/>' for r in range(2) for c in range(3))}</g>
  <g class="coral o"><rect x="-24" y="-4" width="50" height="50"/></g>
</g>
<g transform="translate(450 250)">
  <g class="tealp o" transform="rotate(14)">{''.join(f'<rect x="{-70+c*50}" y="{-40+r*50}" width="44" height="44" transform="rotate({-10+c*8} {-48+c*50} {-18+r*50})"/>' for r in range(2) for c in range(3))}</g>
</g>
<path d="M320 250h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" stroke-linecap="round"><path d="M330 150l28 28M358 150l-28 28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('examination', '道具でよく調べる検査のイラスト。', f"""
<g transform="translate(240 250)">
  <path d="M-150-120h300v240h-300z" fill="#fffdf6" class="o"/>
  <g class="tealp o"><circle cx="-80" cy="-40" r="26"/><circle cx="10" cy="30" r="26"/><circle cx="90" cy="-20" r="26"/></g>
</g>
<g transform="translate(420 200) rotate(24)">
  <circle r="76" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="8"/>
  <path d="M0 76v70" fill="none" stroke="{INK}" stroke-width="16"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('excellence', 'ずば抜けて優れた出来ばえのイラスト。', f"""
<path d="M60 346h480" class="a"/>
<g class="tealp o">{''.join(f'<rect x="{100+i*66}" y="270" width="50" height="76"/>' for i in range(4))}</g>
<rect x="400" y="110" width="120" height="236" class="coral o"/>
<g transform="translate(460 70)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<g class="golds" style="stroke-width:5"><path d="M380 120l-24-18M540 120l24-18"/></g>
""", ground=False)

add('exception', '規則から一つだけ外れるもののイラスト。', f"""
<g class="tealp o">{''.join(f'<circle cx="{110+i*70}" cy="240" r="28"/>' for i in range(6))}</g>
<g transform="translate(530 240)"><path d="M-28-28h56v56h-56z" class="coral o"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="70" y="190" width="410" height="100" rx="14"/></g>
<path d="M530 150v40" class="a" marker-end="url(#ar)"/>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('excess', '決められた線を越えて多すぎるイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-90-130h180v260h-180z" fill="#f7fbfe" class="o"/>
  <path d="M-90-90h180v220h-180z" class="coralp o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 8"><path d="M-130-40h260"/></g>
  <path d="M-90-130h180v260h-180z" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M450 200v-60"/></g>
<path d="M60 396h480" class="a"/>
""", ground=True, arrow=True)

add('exclusion', '輪の外にはじき出されるイラスト。', f"""
<g fill="none" stroke="{TONES['teal'][0]}" stroke-width="5" stroke-dasharray="12 10"><circle cx="250" cy="250" r="140"/></g>
{person(180,300,0.85,1,'teal','blue','stand','short','smile')}
{person(300,300,0.85,1,'gold','blue','stand','bob','smile')}
{person(510,346,0.95,-1,'coral','gold','stand','cap','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M420 200h60"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('executive', '会社の意思を決める役員のイラスト。', f"""
{person(220,346,1.35,1,'blue','blue','stand','short','neutral')}
<g transform="translate(220 240)"><path d="M-40-30h80v10h-80z" class="teal o"/></g>
<g transform="translate(440 250)">
  <path d="M-110-100h220v200h-220z" fill="#dfe6ea" class="o"/>
  <g fill="{TONES['teal'][0]}"><rect x="-80" y="20" width="40" height="60"/><rect x="-20" y="-20" width="40" height="100"/><rect x="40" y="-60" width="40" height="140"/></g>
</g>
<g transform="translate(220 226)"><path d="M-14-14l6 12 14 2-10 10 2 14-12-8-12 8 2-14-10-10 14-2z" class="gold o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('exile', '国を追われて外へ出るイラスト。', f"""
<g transform="translate(230 230)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <path d="M170-140v280" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="14 10"/>
  <g transform="translate(-60 -90)"><path d="M-4-30h8v50h-8z" class="ink"/><path d="M4-28h44v28H4z" class="teal o"/></g>
</g>
{person(470,346,1.0,1,'coral','gold','walk','bob','sad')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M360 250h70"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('existence', 'そこに在ることを示したイラスト。', f"""
<g transform="translate(170 240)">
  <path d="M-80-80h160v160h-160z" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"/>
</g>
<g transform="translate(430 240)">
  <path d="M-80-80h160v160h-160z" class="teal o"/>
</g>
<path d="M280 240h50" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 350l20 20 34-40"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('expansion', '枠が外へ広がって大きくなるイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-60-60h120v120h-120z" class="teal o"/>
  <path d="M-150-150h300v300h-300z" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 9"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 160l-60-60M370 160l60-60M230 300l-60 60M370 300l60 60"/></g>
""", ground=False, arrow=True)

add('expectation', 'こう来るはずだと先を思い描くイラスト。', f"""
{person(170,346,1.15,1,'teal','blue','think','short','smile')}
<g transform="translate(430 190)">
  <path d="M-130-70q-14-52 44-62 18-44 86-30 40 6 50 44 64-6 68 50 4 48-56 52h-166q-38-4-26-54z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 -6)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
</g>
<g fill="#fffdf6" stroke="{INK}" stroke-width="2.5"><circle cx="280" cy="290" r="12"/><circle cx="256" cy="314" r="8"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('exploitation', '働かせて利益だけ吸い上げるイラスト。', f"""
{person(200,346,1.1,1,'teal','gold','carry','cap','sad')}
{box(200,250,90,64,0,'gold')}
{person(450,346,1.25,-1,'violet','blue','reach','short','flat')}
<g transform="translate(360 250)">
  <path d="M-50-30h100v50h-100z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="14" class="goldd o"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="6" marker-end="url(#ar)"><path d="M280 200h80"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('exploration', '未知の地を分け入って調べるイラスト。', f"""
<g fill="#b9c8d6" opacity=".7"><path d="M430 180l150 140H280z"/></g>
{person(170,340,1.05,1,'coral','blue','carry','cap','neutral')}
<path d="M250 250h160" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="14 12" marker-end="url(#ar)"/>
<g transform="translate(120 200)">
  <circle r="34" fill="#fffdf6" class="o"/>
  <path d="M0-26l12 26-12 26-12-26z" class="coral o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('explore', '知らない土地に足を踏み入れて探るイラスト。', f"""
{tree(120,330,0.9)}
{person(230,340,1.1,1,'teal','blue','walk','cap','neutral')}
<path d="M300 250h160" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 10" marker-end="url(#ar)"/>
<g fill="{INK}" transform="translate(480 160)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('explosive', '一瞬で破裂する爆発力のイラスト。', f"""
<g transform="translate(300 210)">
  <path d="M0-150l38 80 86-28-54 74 64 58-90-6-6 90-38-76-68 48 22-86-92-24 80-44z" class="coral o"/>
  <circle r="46" class="goldp o"/>
</g>
<g fill="{TONES['coral'][1]}"><circle cx="110" cy="330" r="12"/><circle cx="490" cy="330" r="10"/></g>
""", ground=False)

add('exposure', '覆いが外れて表にさらされるイラスト。', f"""
<g transform="translate(170 250)">
  <path d="M-80 80q0-140 80-140t80 140z" fill="#dfe6ea" class="o"/>
</g>
<g transform="translate(430 250)">
  <circle r="70" class="coral o"/>
  <path d="M-90-80q60-30 120 10" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>
</g>
{sun(520,100,26)}
<path d="M290 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('extension', '長さを継ぎ足して延ばすイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-220-30h240v60h-240z" class="teal o"/>
  <path d="M20-30h200v60H20z" class="tealp o"/>
  <g fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="9 8"><path d="M20-60v120"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M330 340h190"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('extent', 'どこまで及ぶかの範囲を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-120h440v240h-440z" fill="#fffdf6" class="o"/>
  <path d="M-200-100h300v200h-300z" class="tealp o"/>
  <path d="M-200-100h300v200h-300z" fill="none" stroke="{TONES['teal'][0]}" stroke-width="4"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M100 380h300M400 380H100"/></g>
""", ground=False, arrow=True)

add('extract', '中から必要なものだけ取り出すイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-100-80h200v160h-200z" fill="none" stroke="{INK}" stroke-width="4"/>
  <g class="tealp o"><circle cx="-50" cy="-30" r="20"/><circle cx="30" cy="20" r="20"/><circle cx="-20" cy="50" r="20"/></g>
  <g class="coral o"><circle cx="50" cy="-40" r="22"/></g>
</g>
<g transform="translate(460 250)"><circle r="26" class="coral o"/></g>
<path d="M330 230h70" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('extremely', '目盛りが端まで振り切れて極端なイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-170 40a170 170 0 0 1 340 0z" fill="#f7fbfe" class="o"/>
  <path d="M0 40L150 20" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10" stroke-linecap="round"/>
  <circle cy="40" r="12" class="ink"/>
  <path d="M110-70a170 170 0 0 1 60 110" fill="none" stroke="{TONES['coral'][0]}" stroke-width="10"/>
</g>
<g class="corals" style="stroke-width:6"><path d="M500 160l24-18"/></g>
<path d="M60 320h480" class="a"/>
""", ground=True)

add('eyesight', '視力表を見て目の見え方を測るイラスト。', f"""
<g transform="translate(400 220)">
  <path d="M-120-130h240v260h-240z" class="paper"/>
  <g fill="{INK}"><rect x="-30" y="-100" width="60" height="16"/><rect x="-22" y="-50" width="44" height="12"/><rect x="-16" y="-10" width="32" height="10"/><rect x="-10" y="26" width="20" height="8"/><rect x="-6" y="56" width="12" height="6"/></g>
</g>
{person(150,346,1.05,1,'teal','blue','point','short','neutral')}
<path d="M220 220h50" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="12 9" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('facility', '設備のそろった施設のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200 90h400v-160h-400z" fill="#dfe6ea" class="o"/>
  <path d="M-220-70l220-80 220 80z" class="teal o"/>
  <g fill="#cfe6f5" stroke="{INK}" stroke-width="2">{''.join(f'<rect x="{-160+c*90}" y="{-40+r*60}" width="60" height="44"/>' for r in range(2) for c in range(4))}</g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('faction', '一つの集まりの中で分かれる派閥のイラスト。', f"""
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9"><rect x="90" y="170" width="420" height="190" rx="16"/></g>
{person(170,340,1.0,1,'teal','blue','stand','short','neutral')}
{person(260,340,1.0,1,'teal','blue','stand','bob','neutral')}
{person(390,340,1.0,1,'coral','gold','stand','cap','neutral')}
{person(470,340,1.0,1,'coral','gold','stand','short','neutral')}
<g fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="10 8"><path d="M325 180v170"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('faculty', '学部の建物と教員のイラスト。', f"""
<g transform="translate(380 260)">
  <path d="M-140 80h280v-140h-280z" fill="#f4ead2" class="o"/>
  <path d="M-160-60l160-80 160 80z" class="teal o"/>
  <g class="goldp o"><rect x="-100" y="-20" width="50" height="100"/><rect x="-25" y="-20" width="50" height="100"/><rect x="50" y="-20" width="50" height="100"/></g>
</g>
{person(140,346,1.05,1,'violet','blue','stand','short','smile')}
<g transform="translate(140 240)"><path d="M-40-26h80v10h-80z" class="paper"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fairly', 'どちらにもかたよらず公平に分けるイラスト。', f"""
<g transform="translate(300 170)">
  <path d="M-6-40h12v60h-12z" class="ink"/>
  <path d="M-170 20h340" fill="none" stroke="{INK}" stroke-width="7"/>
  <path d="M-170 20v50M170 20v50" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(130 260)"><g class="teal o"><circle r="28"/><circle cx="44" cy="10" r="28"/></g></g>
<g transform="translate(470 260)"><g class="teal o"><circle r="28"/><circle cx="-44" cy="10" r="28"/></g></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M280 350l20 20 34-40"/></g>
""", ground=False)

add('fairness', 'えこひいきなく等しく扱う公正さのイラスト。', f"""
{person(200,346,1.15,1,'teal','blue','stand','short','smile')}
{person(400,346,1.15,1,'coral','gold','stand','bob','smile')}
<g class="paper"><rect x="170" y="150" width="60" height="44"/><rect x="370" y="150" width="60" height="44"/></g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M180 220l18 18 30-36"/><path d="M380 220l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('faith', '目に見えないものを固く信じるイラスト。', f"""
{person(200,346,1.25,1,'violet','blue','stand','short','neutral')}
<g transform="translate(200 226)"><path d="M-20 26q-4-38 20-50 24 12 20 50z" fill="{SKIN}" stroke="{SKINL}" stroke-width="3"/></g>
<g transform="translate(440 220)">
  <circle r="60" class="goldp o"/>
  <g class="golds" style="stroke-width:5"><path d="M0-80v-20M-60-60l-18-14M60-60l18-14M0 80v20"/></g>
</g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M290 240h70"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fake', '本物そっくりの偽物を示したイラスト。', f"""
<g transform="translate(170 240)">
  <circle r="76" class="goldd o"/>
  <circle r="56" fill="#e5b56b" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M50-110l20 20 34-40"/></g>
</g>
<g transform="translate(430 240)">
  <circle r="76" fill="#cfc9a8" stroke="{INK}" stroke-width="3"/>
  <circle r="56" fill="#ddd7bb" stroke="{INK}" stroke-width="2"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M50-110l30 30M80-110l-30 30"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fame', '大勢に知られて名声を得るイラスト。', f"""
{person(300,300,1.2,1,'coral','gold','up','bob','smile')}
<g transform="translate(300 160)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
{person(120,346,0.6,1,'teal','blue','up','short','smile')}
{person(200,346,0.6,1,'gold','blue','up','bob','smile')}
{person(410,346,0.6,1,'violet','gold','up','cap','smile')}
{person(490,346,0.6,1,'teal','gold','up','short','smile')}
<g class="golds" style="stroke-width:5"><path d="M400 200l24-18M200 200l-24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fare', '乗るために払う運賃のイラスト。', f"""
<g transform="translate(380 260)">
  <path d="M-140 60h280v-140h-280z" class="bluep o"/>
  <g fill="#e8f4fb" stroke="{INK}" stroke-width="3"><rect x="-110" y="-60" width="80" height="50"/><rect x="10" y="-60" width="80" height="50"/></g>
  <circle cx="-80" cy="76" r="22" class="ink"/><circle cx="80" cy="76" r="22" class="ink"/>
</g>
<g transform="translate(150 250)">
  <path d="M-60-30h120v50h-120z" fill="#e6f2d9" stroke="{INK}" stroke-width="3"/>
  <circle r="16" class="goldd o"/>
</g>
<path d="M230 250h60" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('fate', '行き先があらかじめ定められているイラスト。', f"""
{person(150,346,1.1,1,'teal','blue','walk','short','neutral')}
<path d="M220 250h200" fill="none" stroke="{MUTED}" stroke-width="6" stroke-dasharray="14 10" marker-end="url(#ar)"/>
<g transform="translate(480 250)">
  <circle r="56" class="violetp o"/>
  <g class="violets" fill="none" stroke="{TONES['violet'][0]}" stroke-width="4"><path d="M0-76v-16M-60-60l-14-12M60-60l14-12"/></g>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M300 340l30 30M330 340l-30 30"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('favor', '頼みを聞いて手を貸すイラスト。', f"""
{person(200,346,1.2,1,'teal','blue','reach','short','smile')}
{person(420,346,1.2,-1,'coral','gold','reach','bob','smile')}
<g transform="translate(310 250)">
  <path d="M-50-30h100v50h-100z" class="goldp o"/>
</g>
<path d="M250 200h120" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M480 190l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('feather', '鳥の羽根のイラスト。', f"""
<g transform="translate(300 230) rotate(20)">
  <path d="M0-140q70 60 40 150-20 60-40 70-20-10-40-70-30-90 40-150z" fill="#e8f4fb" stroke="{INK}" stroke-width="3"/>
  <path d="M0-140v220" fill="none" stroke="{INK}" stroke-width="4"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2">{''.join(f'<path d="M0 {-100+i*30}l-34 {14+i*2}M0 {-100+i*30}l34 {14+i*2}"/>' for i in range(6))}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('feedback', '受け取った側から感想が返るイラスト。', f"""
{person(150,346,1.15,1,'teal','blue','give','short','smile')}
{person(450,346,1.15,-1,'coral','gold','stand','bob','smile')}
<g transform="translate(300 180)">
  <path d="M-70-40h140v60h-140z" class="paper"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M230 150h140"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" marker-end="url(#ar)"><path d="M380 270H230"/></g>
<g transform="translate(300 270)"><path d="M-60-24h120v40h-120z" fill="#fffdf6" class="o"/><g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-24-8l12 12 20-24"/></g></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('fibre', '細い繊維が寄り合わさるイラスト。', f"""
<g fill="none" stroke="{TONES['gold'][0]}" stroke-width="5">
  <path d="M80 200q120-40 240 0t200-20M80 240q120-40 240 0t200-20M80 280q120-40 240 0t200-20"/>
</g>
<g transform="translate(420 180) rotate(20)">
  <circle r="60" fill="#e7f6fb" opacity=".8" stroke="{INK}" stroke-width="6"/>
  <g fill="none" stroke="{TONES['gold'][2]}" stroke-width="4"><path d="M-40-10h80M-40 10h80"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('finding', '調べた末に出てきた結果のイラスト。', f"""
<g transform="translate(200 250)">
  <path d="M-120-100h240v200h-240z" fill="#fffdf6" class="o"/>
  <g class="tealp o"><circle cx="-60" cy="-40" r="22"/><circle cx="20" cy="30" r="22"/></g>
</g>
<g transform="translate(450 240)">
  <path d="M-90-90h180v180h-180z" class="paper"/>
  <g fill="{INK}"><rect x="-60" y="-60" width="120" height="16"/></g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M-40 10l18 18 30-36"/></g>
</g>
<path d="M340 250h30" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('firefighter', 'ホースで火を消す消防士のイラスト。', f"""
{flame(470,280,1.3)}
{person(180,346,1.2,1,'coral','coral','reach','cap','neutral')}
<g transform="translate(250 250)">
  <path d="M-10-10h60v20h-60z" class="ink"/>
  <path d="M50-14l40 14-40 14z" fill="#c9d3dc" stroke="{INK}" stroke-width="2"/>
</g>
<g fill="none" stroke="{TONES['blue'][0]}" stroke-width="10" stroke-linecap="round"><path d="M300 260q60 10 110 20"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('fixture', '壁に据えつけられた設備のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" fill="#fffdf6" class="o"/>
  <path d="M-220 60h440v80h-440z" class="goldp o"/>
  <g transform="translate(-120 -60)">
    <path d="M-40-30h80v30h-80z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
    <path d="M-30 0h60l20 40h-100z" class="goldp o"/>
  </g>
  <g transform="translate(110 20)">
    <path d="M-50-40h100v80h-100z" fill="#dfe6ea" stroke="{INK}" stroke-width="3"/>
    <g fill="{INK}"><circle cx="-20" r="8"/><circle cx="20" r="8"/></g>
  </g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('flame', 'ゆらめく一筋の炎のイラスト。', f"""
{flame(300,230,2.0)}
<g transform="translate(300 330)"><path d="M-70-10h140v24h-140z" class="goldd o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('flaw', '表面に走った傷という欠点のイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-110h320v220h-320z" class="tealp o"/>
  <path d="M-40-110l24 70-40 60 36 90" fill="none" stroke="{INK}" stroke-width="6"/>
</g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="10 8"><circle cx="270" cy="240" r="80"/></g>
<path d="M480 140l-140 60" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('flesh', '皮の内側の果肉を示したイラスト。', f"""
<g transform="translate(300 230)">
  <circle r="140" class="coral o"/>
  <circle r="104" fill="#f7c9a8" stroke="{INK}" stroke-width="3"/>
  <g fill="{INK}"><ellipse cx="-20" cy="10" rx="8" ry="12"/><ellipse cx="24" cy="-10" rx="8" ry="12"/></g>
  <path d="M0-140v-30" fill="none" stroke="{TONES['green'][2]}" stroke-width="6"/>
</g>
<path d="M500 140l-130 70" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('fool', 'ばかなまねをして笑われるイラスト。', f"""
{person(230,346,1.3,1,'gold','blue','up','short','smile')}
<g transform="translate(230 180)">
  <path d="M-46-30h92v34h-92z" class="coralp o"/>
  <path d="M-60 4h120v10h-120z" class="coral o"/>
</g>
{face(460,220,66,'smile')}
<g fill="none" stroke="{INK}" stroke-width="4"><path d="M430 210q14-12 28 0M466 206q14-12 28 0"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('footage', '撮った映像がフィルムに残るイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-230-90h460v180h-460z" fill="#41506a"/>
  <g fill="#1f2b3d">{''.join(f'<rect x="{-215+i*66}" y="-80" width="14" height="20"/>' for i in range(7))}{''.join(f'<rect x="{-215+i*66}" y="60" width="14" height="20"/>' for i in range(7))}</g>
  <g class="bluep"><rect x="-190" y="-46" width="110" height="92"/><rect x="-60" y="-46" width="110" height="92"/><rect x="70" y="-46" width="110" height="92"/></g>
  <g transform="translate(-135 10) scale(0.35)">{person(0,0,1.0,1,'coral','gold','walk','bob','smile')}</g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('forecast', 'これからの天気を予報するイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-200-140h400v280h-400z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="2"><path d="M-70-140v280M70-140v280"/></g>
  <g transform="translate(-135 -40) scale(0.6)">{sun(0,0,34)}</g>
  <g transform="translate(0 -40) scale(0.6)">{cloud(0,0,1.2)}</g>
  <g transform="translate(135 -60) scale(0.6)">{cloud(0,0,1.2)}</g>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4" stroke-linecap="round"><path d="M110 0l-10 30M140 0l-10 30M170 0l-10 30"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 380h360"/></g>
""", ground=True, arrow=True)

add('foreigner', '別の国から来た人を示したイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" class="paper"/>
  <path d="M40-140v280" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="14 10"/>
  <g transform="translate(-120 -100)"><path d="M-4-30h8v50h-8z" class="ink"/><path d="M4-28h44v28H4z" class="teal o"/></g>
  <g transform="translate(140 -100)"><path d="M-4-30h8v50h-8z" class="ink"/><path d="M4-28h44v28H4z" class="coral o"/></g>
</g>
{person(200,320,0.85,1,'coral','gold','walk','bob','smile')}
<path d="M250 260h60" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)
print(len(W), ' '.join(W)); print(sheet(W))
