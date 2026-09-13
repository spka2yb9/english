from lib import *
emit('coach', '笛をくわえて選手に指示を出している指導者のイラスト。', f"""
<circle cx="120" cy="100" r="56" class="tealp"/>
{person(200,346,1.2,1,'teal','blue','point','cap','neutral')}
<g transform="translate(232 244)">
  <path d="M-6-10h26v20H-6z" class="goldd o"/>
  <circle cx="26" cy="0" r="12" class="gold o"/>
</g>
<g class="golds" opacity=".9" style="stroke-width:4"><path d="M262 214q20-14 22-32M276 240q24-6 34-20"/></g>
{person(460,346,0.9,-1,'coral','gold','walk','short','neutral')}
<path d="M310 200h80" class="a" marker-end="url(#ar)"/>
<path d="M60 366h480" class="a"/>
""", ground=True, arrow=True)
emit('desert', '砂の丘とサボテンが並ぶ、雨の少ない砂漠のイラスト。', f"""
{sun(480,90,48)}
<path d="M0 250q120-50 240-10t360-30v190H0z" fill="#efdcb8" stroke="{INK}" stroke-width="3"/>
<g transform="translate(200 310)">
  <path d="M-16 0v-120a16 16 0 0 1 32 0V0z" class="green o"/>
  <path d="M-16-70h-24a14 14 0 0 0-14 14v20a14 14 0 0 0 28 0v-14" class="green o"/>
  <path d="M16-86h24a14 14 0 0 1 14 14v26a14 14 0 0 1-28 0v-16" class="green o"/>
  <g fill="none" stroke="{TONES['green'][2]}" stroke-width="2.5"><path d="M0-116v112"/></g>
</g>
<g transform="translate(430 320) scale(0.6)">
  <path d="M-16 0v-120a16 16 0 0 1 32 0V0z" class="green o"/>
  <path d="M16-86h24a14 14 0 0 1 14 14v26a14 14 0 0 1-28 0v-16" class="green o"/>
</g>
<g fill="none" stroke="#dcc79c" stroke-width="3"><path d="M280 360q60-16 120 0M80 380q60-16 120 0"/></g>
""", ground=False)
print(sheet(['coach','desert']))
