"""第69回: 構造・要約・象徴・技術など46語。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('string', '巻いた糸のイラスト。', f"""
<g transform="translate(280 250)">
  <path d="M-60-70h120v140h-120z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#d9c286" stroke-width="3">{''.join(f'<path d="M-60 {-50+i*24}h120"/>' for i in range(5))}</g>
</g>
<path d="M340 240q80-30 120 20t60 60" fill="none" stroke="{TONES['coral'][0]}" stroke-width="5"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('structural', '建物の骨組みを示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-160-130h320v260h-320z" fill="none" stroke="{INK}" stroke-width="6"/>
  <g fill="none" stroke="{INK}" stroke-width="5"><path d="M-160-130L160 130M160-130L-160 130M-160 0h320M0-130v260"/></g>
  <g class="teal o"><circle cx="-160" cy="-130" r="12"/><circle cx="160" cy="-130" r="12"/><circle cx="-160" cy="130" r="12"/><circle cx="160" cy="130" r="12"/><circle r="12"/></g>
</g>
""", ground=False)

add('stubborn', '押されても一歩も動かない頑固なイラスト。', f"""
{person(400,346,1.3,1,'violet','blue','stand','short','flat')}
{person(180,346,1.1,1,'teal','blue','point','bob','neutral')}
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="8" marker-end="url(#ar)"><path d="M260 250h60"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="9 8"><path d="M400 130v60"/></g>
<g fill="none" stroke="{TONES['coral'][0]}" stroke-width="9" stroke-linecap="round"><path d="M480 170l30 30M510 170l-30 30"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('studio', '照明とカメラのある撮影スタジオのイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-220-140h440v280h-440z" fill="#dfe6ea" class="o"/>
  <path d="M-160-100h320v180h-320z" fill="#fffdf6" class="o"/>
</g>
<g transform="translate(150 200)">
  <path d="M-30-40h60l20 50h-100z" fill="#f3e3ae" stroke="{INK}" stroke-width="3"/>
  <path d="M-4 10h8v120h-8z" class="ink"/>
</g>
<g transform="translate(430 260)">
  <path d="M-60-40h120v80h-120z" fill="#41506a"/>
  <path d="M60-16l50-30v76l-50-30z" fill="#41506a"/>
  <path d="M-20 40h40v50h-40z" fill="#41506a"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('stuff', '雑多な持ち物が詰め込まれたイラスト。', f"""
<g transform="translate(300 260)">
  <path d="M-160-60h320v140h-320z" fill="none" stroke="{INK}" stroke-width="5"/>
  <g class="tealp o"><rect x="-140" y="-20" width="70" height="60"/></g>
  <g class="coralp o"><circle cx="-30" cy="10" r="34"/></g>
  <g class="goldp o"><rect x="30" y="-30" width="60" height="70"/></g>
  <g class="violetp o"><path d="M110 40l40-60 40 60z"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('stunning', '息をのむほど見事な景色のイラスト。', f"""
<rect width="600" height="400" rx="20" fill="#fdf3dc"/>
{sun(300,120,50)}
<g fill="#b9c8d6"><path d="M300 180l180 160H120z"/></g>
<g class="green o" opacity=".85"><path d="M0 330q150-40 300-20t300-10v100H0z"/></g>
{person(120,346,0.8,1,'coral','blue','up','short','surprised')}
<g class="golds" style="stroke-width:6"><path d="M480 200l26-20M490 240h30"/></g>
""", ground=False)

add('subject', '教科書が並ぶ、学ぶ科目のイラスト。', f"""
<g transform="translate(300 250)">
  <path d="M-200 90h400v20h-400z" class="goldd o"/>
  <g class="tealp o"><rect x="-170" y="-50" width="60" height="140"/></g>
  <g class="coralp o"><rect x="-100" y="-70" width="60" height="160"/></g>
  <g class="goldp o"><rect x="-30" y="-40" width="60" height="130"/></g>
  <g class="violetp o"><rect x="40" y="-60" width="60" height="150"/></g>
  <g class="greenp o"><rect x="110" y="-30" width="60" height="120"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('subsequent', '先の出来事のあとに続くものを示すイラスト。', f"""
<g class="tealp o"><rect x="110" y="200" width="100" height="120"/></g>
<g class="coral o"><rect x="270" y="200" width="100" height="120"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><rect x="430" y="200" width="100" height="120"/></g>
<path d="M320 150v30" class="a" marker-end="url(#ar)"/>
<g class="a" marker-end="url(#ar)"><path d="M100 360h430"/></g>
<path d="M60 340h480" class="a"/>
""", ground=True, arrow=True)

add('subtle', 'ほんのわずかな色のちがいを示したイラスト。', f"""
<rect x="110" y="180" width="120" height="150" fill="{TONES['teal'][0]}" class="o"/>
<rect x="240" y="180" width="120" height="150" fill="#2b968d" class="o"/>
<rect x="370" y="180" width="120" height="150" fill="#2f9f95" class="o"/>
<g fill="{INK}" transform="translate(500 150)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M120 366h360" class="a"/>
""", ground=True)

add('suburban', '町の外側に住宅が広がる郊外のイラスト。', f"""
<g transform="translate(300 300)"><path d="M-250-10h500v14h-500z" fill="#e6dcc9"/></g>
<g opacity=".6">{building(120,290,0.6,'teal')}{building(190,290,0.5,'blue')}</g>
<g transform="translate(340 270)"><path d="M-56 40h112V-16h-112z" fill="#f4ead2" class="o"/><path d="M-70-16l70-46 70 46z" class="coral o"/></g>
<g transform="translate(470 270)"><path d="M-56 40h112V-16h-112z" fill="#f4ead2" class="o"/><path d="M-70-16l70-46 70 46z" class="teal o"/></g>
{tree(270,320,0.5)}
<g class="a" marker-end="url(#ar)"><path d="M230 180h100"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('success', '旗の立つ頂に登りついたイラスト。', f"""
<path d="M0 400l240-260 120 130 80-90 160 220z" class="green o"/>
<g transform="translate(240 140)">
  <path d="M-4-70h8v70h-8z" class="ink"/>
  <path d="M4-66h70v40H4z" class="coralp o"/>
</g>
<g transform="translate(300 160) scale(0.7)">{person(0,60,1.0,1,'teal','blue','up','short','smile')}</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M470 130l20 20 34-40"/></g>
""", ground=False)

add('successive', '同じ印が切れ目なく続くイラスト。', f"""
<g class="teal o">{''.join(f'<rect x="{100+i*62}" y="200" width="50" height="120"/>' for i in range(7))}</g>
<g class="a" marker-end="url(#ar)"><path d="M100 360h430"/></g>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 6">{''.join(f'<path d="M{156+i*62} 200v120"/>' for i in range(6))}</g>
""", ground=False, arrow=True)

add('sufficient', '必要な線をきちんと満たしているイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-90-130h180v260h-180z" fill="#f7fbfe" class="o"/>
  <path d="M-90-40h180v170h-180z" class="teal o"/>
  <g fill="none" stroke="{TONES['coral'][0]}" stroke-width="5" stroke-dasharray="12 8"><path d="M-130-40h260"/></g>
  <path d="M-90-130h180v260h-180z" fill="none" stroke="{INK}" stroke-width="3"/>
</g>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="9" stroke-linecap="round"><path d="M460 200l20 20 34-40"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('suggestion', 'こうしたらと案を差し出すイラスト。', f"""
{person(160,346,1.15,1,'teal','blue','point','short','smile')}
<g transform="translate(370 190)">
  <path d="M-100-60h200v90h-200z" fill="#fffdf6" class="o"/>
  <path d="M-60 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g transform="translate(0 -14)"><circle r="26" class="goldp o"/><g class="golds" style="stroke-width:4"><path d="M0-40v-12M-30-24l-12-8M30-24l12-8"/></g></g>
</g>
{person(500,346,1.05,-1,'coral','gold','stand','bob','smile')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('summary', '長い文書を短くまとめ直すイラスト。', f"""
<g transform="translate(160 220)">
  <path d="M-100-130h200v260h-200z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-70 {-100+i*26}h140"/>' for i in range(9))}</g>
</g>
<g transform="translate(430 220)">
  <path d="M-100-80h200v160h-200z" class="paper"/>
  <g fill="{INK}"><rect x="-70" y="-50" width="140" height="14"/><rect x="-70" y="-10" width="110" height="14"/><rect x="-70" y="30" width="80" height="14"/></g>
</g>
<path d="M290 220h50" class="a" marker-end="url(#ar)"/>
""", ground=True, arrow=True)

add('super', 'ふつうをはるかに超えているイラスト。', f"""
<path d="M60 346h480" class="a"/>
<g class="tealp o">{''.join(f'<rect x="{100+i*66}" y="270" width="50" height="76"/>' for i in range(4))}</g>
<rect x="400" y="90" width="120" height="256" class="coral o"/>
<g class="golds" style="stroke-width:6"><path d="M380 80l-26-20M540 80l26-20"/></g>
""", ground=False)

add('superb', 'ひときわ見事な出来ばえのイラスト。', f"""
<g transform="translate(320 240)">
  <path d="M-140-120h280v240h-280z" class="goldd o"/>
  <path d="M-110-90h220v180h-220z" fill="#fffdf6" class="o"/>
  <path d="M-80 60l70-110 50 60 60-80 70 130z" class="green o"/>
</g>
<g transform="translate(320 100)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<g class="golds" style="stroke-width:5"><path d="M500 160l24-18M140 160l-24-18"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('superior', '二つのうち、優れて上に立つほうを示したイラスト。', f"""
<path d="M60 346h480" class="a"/>
<rect x="140" y="120" width="130" height="226" class="coral o"/>
<rect x="360" y="230" width="130" height="116" class="tealp o"/>
<path d="M205 80v30" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{MUTED}" stroke-width="3" stroke-dasharray="9 8"><path d="M120 230h380"/></g>
""", ground=False, arrow=True)

add('supporter', '旗を振って応援する支持者のイラスト。', f"""
{person(180,346,1.15,1,'coral','gold','up','bob','smile')}
{person(300,346,1.15,1,'coral','gold','up','short','smile')}
<g transform="translate(250 160)"><path d="M-4-50h8v70h-8z" class="ink"/><path d="M4-46h60v40H4z" class="coralp o"/></g>
{person(470,346,1.15,-1,'teal','blue','stand','cap','smile')}
<path d="M390 250h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('supportive', '倒れそうな側をそっと支えるイラスト。', f"""
<g transform="translate(400 260) rotate(12)">{person(0,80,1.15,1,'coral','gold','stand','bob','neutral')}</g>
{person(230,346,1.2,1,'teal','blue','reach','short','smile')}
<path d="M300 250h50" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M120 190l18 18 30-36"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('supreme', 'いちばん高い座に置かれるイラスト。', f"""
<g transform="translate(300 320)">
  <path d="M-60-120h120v120h-120z" class="gold o"/>
  <path d="M-190-60h120v60h-120z" class="tealp o"/>
  <path d="M70-40h120v40H70z" class="coralp o"/>
</g>
<g transform="translate(300 170)"><path d="M-40 16l-8-46 24 18 24-30 24 30 24-18-8 46z" class="gold o"/></g>
<path d="M60 336h480" class="a"/>
""", ground=True)

add('sure', 'これで間違いないと、確信してうなずくイラスト。', f"""
{person(200,346,1.25,1,'teal','blue','stand','short','smile')}
<g transform="translate(420 200)">
  <path d="M-80-50h160v80h-160z" fill="#fffdf6" class="o"/>
  <path d="M-50 30l-14 30 40-30z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="10" stroke-linecap="round"><path d="M-30-14l20 20 38-42"/></g>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('survey', '質問に答えてもらって集計するイラスト。', f"""
<g transform="translate(200 230)">
  <path d="M-110-130h220v260h-220z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<rect x="-80" y="{-100+i*50}" width="26" height="26"/>' for i in range(4))}</g>
  <g fill="{MUTED}">{''.join(f'<rect x="-40" y="{-96+i*50}" width="110" height="14"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-74-90l10 10 18-22"/><path d="M-74 10l10 10 18-22"/></g>
</g>
<g transform="translate(450 250)">
  <path d="M-80-70h160v140h-160z" fill="#f7fbfe" class="o"/>
  <g fill="{TONES['teal'][0]}"><rect x="-50" y="0" width="26" height="50"/><rect x="-10" y="-30" width="26" height="80"/><rect x="30" y="-50" width="26" height="100"/></g>
</g>
<path d="M330 240h40" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('suspicious', 'ふるまいがあやしく、目をつけられるイラスト。', f"""
{person(430,346,1.15,-1,'violet','violet','carry','cap','flat')}
{person(160,346,1.15,1,'blue','blue','think','short','flat')}
<path d="M240 240h120" fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="11 9" marker-end="url(#ar)"/>
<g fill="{INK}" transform="translate(280 150)">
  <path d="M0 0q0-24 18-24t18 24q0 12-12 16v10h-10v-18q12-4 12-12t-7-8-7 12z"/><rect x="11" y="38" width="10" height="10"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('symbol', 'ハートの記号が意味を表すイラスト。', f"""
<g transform="translate(200 220)">
  <path d="M0 60c-50-40-70-56-70-84a36 36 0 0 1 70-20 36 36 0 0 1 70 20c0 28-20 44-70 84z" class="coral o"/>
</g>
<g transform="translate(440 220)">
  <path d="M-80-40h160v90h-160z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-56" y="-16" width="112" height="14"/><rect x="-56" y="12" width="80" height="14"/></g>
</g>
<path d="M300 220h50" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('symbolic', '鳩が平和を表す、象徴のイラスト。', f"""
<g transform="translate(220 210)">
  <ellipse rx="80" ry="50" fill="#fffdf6" class="o"/>
  <circle cx="70" cy="-38" r="30" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
  <path d="M96-32l28 8-28 12z" class="gold o"/>
  <path d="M-80 6l-70-32 16 36-24 26 74-10z" fill="#fffdf6" stroke="{INK}" stroke-width="3"/>
</g>
<g transform="translate(450 230)">
  <path d="M-70-40h140v80h-140z" fill="#fffdf6" class="o"/>
  <g fill="{INK}"><rect x="-50" y="-10" width="100" height="16"/></g>
</g>
<path d="M330 220h40" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)

add('sympathetic', '落ち込む相手に寄り添うイラスト。', f"""
<g transform="translate(430 346) rotate(14)">{person(0,0,1.1,-1,'coral','gold','stand','bob','sad')}</g>
{person(230,346,1.2,1,'teal','blue','reach','short','sad')}
<path d="M300 260h60" fill="none" stroke="{SKIN}" stroke-width="16" stroke-linecap="round"/>
<g transform="translate(320 170)">
  <path d="M0 34c-34-26-48-38-48-58a26 26 0 0 1 48-14 26 26 0 0 1 48 14c0 20-14 32-48 58z" class="coralp o"/>
</g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('system', '歯車と流れが組み合わさった仕組みのイラスト。', f"""
<g transform="translate(300 230)">
  <g fill="none" stroke="{INK}" stroke-width="12"><circle cx="-110" cy="-20" r="50"/><circle cx="0" cy="50" r="36"/><circle cx="110" cy="-30" r="44"/></g>
  <g fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8"><path d="M-60-20h20M40 40l30-30"/></g>
</g>
<g class="a" marker-end="url(#ar)"><path d="M120 360h360"/></g>
""", ground=False, arrow=True)

add('systematic', '手順どおりに整えて進めるイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-190-140h380v280h-380z" class="paper"/>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M-100 {-90+i*45}h240"/>' for i in range(5))}</g>
  <g class="tealp o">{''.join(f'<circle cx="-140" cy="{-96+i*45}" r="16"/>' for i in range(5))}</g>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" marker-end="url(#ar)">{''.join(f'<path d="M-140 {-76+i*45}v22"/>' for i in range(4))}</g>
</g>
""", ground=True, arrow=True)

add('tactical', '一手ごとの駆け引きを図で示したイラスト。', f"""
<g transform="translate(300 240)">
  <path d="M-180-130h360v260h-360z" class="green o"/>
  <g fill="none" stroke="#fffdf6" stroke-width="3"><path d="M0-130v260"/><circle r="50"/></g>
  <g class="teal o"><circle cx="-110" cy="-60" r="18"/><circle cx="-60" cy="40" r="18"/></g>
  <g class="coral o"><circle cx="80" cy="-20" r="18"/></g>
  <g fill="none" stroke="#fffdf6" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"><path d="M-110-60l40 80M-60 40l120-50"/></g>
</g>
""", ground=False, arrow=True)

add('tail', '動物の後ろに伸びる尾を示したイラスト。', f"""
<g transform="translate(280 270)">
  <ellipse rx="100" ry="60" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <circle cx="90" cy="-40" r="44" fill="#d9a86b" stroke="{INK}" stroke-width="3"/>
  <circle cx="104" cy="-46" r="5" class="ink"/>
  <g fill="#d9a86b" stroke="{INK}" stroke-width="3"><rect x="-70" y="50" width="20" height="46"/><rect x="40" y="50" width="20" height="46"/></g>
  <path d="M-100-10q-70-40-90 10" fill="none" stroke="#d9a86b" stroke-width="16" stroke-linecap="round"/>
</g>
<circle cx="150" cy="270" r="56" fill="none" stroke="{TONES['coral'][0]}" stroke-width="4" stroke-dasharray="11 9"/>
<path d="M100 180l30 50" class="a" marker-end="url(#ar)"/>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('talent', '人並みはずれた腕前が輝くイラスト。', f"""
{person(230,346,1.3,1,'violet','blue','up','bob','smile')}
<g transform="translate(230 140)"><path d="M0-40l14 28 30 4-22 21 6 30-28-15-28 15 6-30-22-21 30-4z" class="gold o"/></g>
<g transform="translate(450 260)">
  <path d="M-80-60h160v120h-160z" class="paper"/>
  <path d="M-50 40l50-70 34 40 40-60 26 90z" class="tealp o"/>
</g>
<g class="golds" style="stroke-width:5"><path d="M330 190l-24-18M340 230h-28"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('tape', '巻かれたテープと引き出した先のイラスト。', f"""
<g transform="translate(240 250)">
  <circle r="90" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/>
  <circle r="34" fill="#fffaf1" stroke="{INK}" stroke-width="3"/>
  <g fill="none" stroke="#d9c286" stroke-width="3"><circle r="62"/></g>
</g>
<path d="M330 250h190v26H330z" fill="#f7e6bd" stroke="{INK}" stroke-width="3"/>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('target', '中心をねらう的のイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="140" fill="#fffdf6" class="o"/>
  <circle r="100" class="coralp o"/>
  <circle r="60" fill="#fffdf6" class="o"/>
  <circle r="24" class="coral o"/>
</g>
<path d="M120 380l150-140" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)

add('task', '割り当てられた仕事の一覧のイラスト。', f"""
<g transform="translate(300 220)">
  <path d="M-170-140h340v280h-340z" class="paper"/>
  <g fill="none" stroke="{INK}" stroke-width="3">{''.join(f'<rect x="-130" y="{-100+i*50}" width="28" height="28"/>' for i in range(4))}</g>
  <g fill="{MUTED}">{''.join(f'<rect x="-90" y="{-96+i*50}" width="200" height="14"/>' for i in range(4))}</g>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round"><path d="M-124-90l10 10 18-22"/></g>
</g>
""", ground=True)

add('technical', '専門の工具で細かい部分を扱うイラスト。', f"""
<g transform="translate(340 250)">
  <path d="M-120-90h240v180h-240z" fill="#dfe6ea" class="o"/>
  <g fill="none" stroke="{INK}" stroke-width="8"><circle cx="-40" cy="-20" r="30"/><circle cx="40" cy="30" r="22"/></g>
  <g fill="{INK}"><circle cx="70" cy="-60" r="8"/><circle cx="90" cy="-40" r="6"/></g>
</g>
<g transform="translate(160 250) rotate(-20)">
  <path d="M-10-70h20v100h-20z" fill="#c9d3dc" stroke="{INK}" stroke-width="3"/>
  <path d="M-24-90h48v22h-48z" class="coral o"/>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('technique', '型どおりの手つきで、うまくやるコツのイラスト。', f"""
{hand(200,200,1)}
<g transform="translate(380 250)">
  <path d="M-90-70h180v140h-180z" class="paper"/>
  <g fill="none" stroke="{TONES['teal'][0]}" stroke-width="4" marker-end="url(#ar)"><path d="M-60-30h60M-60 10h100"/></g>
  <g fill="{MUTED}"><rect x="20" y="-38" width="60" height="14"/></g>
</g>
<path d="M270 240h20" class="a" marker-end="url(#ar)"/>
<g fill="none" stroke="{TONES['green'][0]}" stroke-width="8" stroke-linecap="round"><path d="M150 320l18 18 30-36"/></g>
<path d="M60 386h480" class="a"/>
""", ground=True, arrow=True)

add('technological', '歯車と回路が組み合わさる科学技術のイラスト。', f"""
<g transform="translate(200 240)">
  <g fill="none" stroke="{INK}" stroke-width="12"><circle r="56"/></g>
  <g fill="{INK}">{''.join(f'<rect x="-8" y="-78" width="16" height="22" transform="rotate({i*45})"/>' for i in range(8))}</g>
</g>
<g transform="translate(430 240)">
  <path d="M-90-70h180v140h-180z" fill="#1f2b3d"/>
  <g fill="none" stroke="#7fd6c2" stroke-width="4"><path d="M-60-40h60v40h60M-60 20h40v20h80"/></g>
  <g fill="#7fd6c2"><circle cx="0" cy="0" r="7"/><circle cx="60" cy="0" r="7"/><circle cx="-20" cy="40" r="7"/></g>
</g>
<path d="M60 386h480" class="a"/>
""", ground=True)

add('technology', '機械と画面で成り立つ科学技術のイラスト。', f"""
<g transform="translate(300 230)">
  <path d="M-190-130h380v230h-380z" fill="#41506a"/>
  <path d="M-165-105h330v180h-330z" class="bluep"/>
  <g fill="none" stroke="#fffdf6" stroke-width="4"><circle cx="-60" cy="-20" r="34"/><path d="M-26-20h60v40h40"/></g>
  <g fill="#fffdf6"><circle cx="74" cy="20" r="8"/></g>
  <path d="M-40 100h80v30h-80z" fill="#41506a"/>
</g>
<path d="M60 396h480" class="a"/>
""", ground=True)

add('tent', '布を張ってつくったテントのイラスト。', f"""
<g transform="translate(300 300)">
  <path d="M0-160l150 160h-300z" class="tealp o"/>
  <path d="M0-160l50 160h-100z" fill="#fffdf6" class="o"/>
  <path d="M-150 0h300v14h-300z" class="goldd o"/>
</g>
{tree(120,320,0.7)}
{sun(500,110,26)}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('terrific', '飛び上がって喜ぶほど、すばらしいイラスト。', f"""
<g transform="translate(280 330) rotate(-6)">{person(0,0,1.35,1,'coral','gold','up','bob','smile')}</g>
<g class="golds" style="stroke-width:6"><path d="M150 180l-30-24M400 180l30-24M280 120v-30"/></g>
<g transform="translate(470 250)"><path d="M0-30l10 20 22 4-16 16 4 22-20-12-20 12 4-22-16-16 22-4z" class="gold o"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('theatrical', '幕の開いた舞台で大きく演じるイラスト。', f"""
<g transform="translate(300 150)">
  <path d="M-210-70h420v40h-420z" class="coral o"/>
  <path d="M-210-30h70q10 110 0 190h-70z" class="coralp o"/>
  <path d="M140-30h70v190h-70q-10-80 0-190z" class="coralp o"/>
</g>
<g transform="translate(300 260) scale(1.0)">{person(0,60,1.0,1,'violet','gold','up','bob','smile')}</g>
<g class="golds" style="stroke-width:5"><path d="M200 200l-24-18M400 200l24-18"/></g>
<path d="M60 366h480" class="a"/>
""", ground=True)

add('theirs', 'あの人たちのものだと囲って示すイラスト。', f"""
{person(340,346,1.15,1,'coral','gold','stand','bob','smile')}
{person(460,346,1.15,1,'teal','blue','stand','short','smile')}
{box(400,240,120,90,0,'gold')}
<g fill="none" stroke="{TONES['violet'][0]}" stroke-width="4" stroke-dasharray="11 9"><rect x="290" y="160" width="250" height="200" rx="18"/></g>
{person(150,346,1.15,1,'blue','blue','point','short','neutral')}
<path d="M60 366h480" class="a"/>
""", ground=True)

add('theme', '全体をつらぬく主題を中心に置いたイラスト。', f"""
<g transform="translate(300 220)">
  <circle r="70" class="coral o"/>
  <g class="tealp o">{''.join(f'<circle cx="{int(150*__import__("math").cos(i*3.14159/3))}" cy="{int(150*__import__("math").sin(i*3.14159/3))}" r="34"/>' for i in range(6))}</g>
  <g fill="none" stroke="{MUTED}" stroke-width="3">{''.join(f'<path d="M0 0L{int(120*__import__("math").cos(i*3.14159/3))} {int(120*__import__("math").sin(i*3.14159/3))}"/>' for i in range(6))}</g>
</g>
""", ground=False)

add('theoretical', '紙の上の理屈と、実物を対比したイラスト。', f"""
<g transform="translate(170 230)">
  <path d="M-100-100h200v200h-200z" class="paper"/>
  <g fill="none" stroke="{TONES['blue'][0]}" stroke-width="4"><path d="M-60 40h120v-100h-120z"/><path d="M-60-60l60-40 60 40"/></g>
</g>
<g transform="translate(430 250)">
  <path d="M-80 60h160V-30h-160z" fill="#f4ead2" class="o"/>
  <path d="M-100-30l100-70 100 70z" class="coral o"/>
</g>
<g class="a" marker-end="url(#ar)"><path d="M290 230h50"/></g>
<path d="M60 346h480" class="a"/>
""", ground=True, arrow=True)

add('thorough', '隅から隅までもれなく調べるイラスト。', f"""
<g transform="translate(280 240)">
  <path d="M-170-130h340v260h-340z" fill="#fffdf6" class="o"/>
  <g fill="none" stroke="{TONES['green'][0]}" stroke-width="6" stroke-linecap="round">
    {''.join(f'<path d="M{-140+c*90} {-100+r*80}l12 12 20-24"/>' for r in range(4) for c in range(4))}
  </g>
</g>
<g transform="translate(470 340) rotate(24)">
  <circle r="44" fill="#e7f6fb" opacity=".85" stroke="{INK}" stroke-width="6"/>
  <path d="M0 44v50" fill="none" stroke="{INK}" stroke-width="12"/>
</g>
<path d="M60 396h480" class="a"/>
""", ground=True)
print(len(W), ' '.join(W)); print(sheet(W))
