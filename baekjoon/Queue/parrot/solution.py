import sys
from collections import deque
import time
sys.stdin = open('inputs.txt','r')

st= time.time()
n= int(sys.stdin.readline())
texts= [deque(sys.stdin.readline().split()) for _ in range(n)]
answer = deque(sys.stdin.readline().split())
ans_len =len(answer)

while len(answer) :
    for i in range(len(texts)) :
        if not len(answer): break
        if len(texts[i]):
            if texts[i][0]==answer[0]:
                texts[i].popleft()
                answer.popleft()
    
    if len(answer) == ans_len:break
    else : ans_len = len(answer)
        
for i in range(len(texts)):
    if texts[i]:
        answer.append(0)
        break
        
if len(answer): print('Impossible')
else : print('Possible')
