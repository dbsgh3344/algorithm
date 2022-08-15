import sys
from collections import deque

sys.stdin= open('inputs.txt')

n,w,l = map(int,sys.stdin.readline().split())
trucks = deque(map(int,sys.stdin.readline().split()))
bridge = deque([])
cnt= []
idx= 0
ans =0
while len(trucks)!=0 :
    if sum(map(lambda x: x[1],bridge))+trucks[0]<=l and len(bridge)<w:
        bridge.append((idx,trucks.popleft()))
        cnt.append(0)
        idx+=1
    
    if len(cnt)>0:
        cnt = list(map(lambda x: x+1,cnt))
        if cnt[bridge[0][0]]==w:
            bridge.popleft()

res= cnt[0]
if cnt[-1] <=w:
    res+=(w-cnt[-1])+1

print(res)

        
        



    