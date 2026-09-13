"""第52回の描き直し: worse（3つめの顔が画面外に出ていた）。"""
from lib import *
W=[]
def add(w,a,b,**k): W.append(emit(w,a,b,**k))

add('worse', '同じ顔つきがだんだん悪くなっていくイラスト。', f"""
{face(140,190,66,'smile')}
{face(300,200,66,'flat')}
{face(465,210,66,'sad')}
{drop(520,150,0.8)}
<path d="M100 330h400" class="a" marker-end="url(#ar)"/>
""", ground=False, arrow=True)
print(len(W)); print(sheet(W, '/tmp/vocab-sheet2.html'))
