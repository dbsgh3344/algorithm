import sys
from collections import deque
# sys.stdin = open('inputs.txt','r')

n,m = map(int,input().split())
riskvalue = deque(map(int,input().split()))
cnt =0
m=m+1
while True :
    cur_val = riskvalue.popleft()
    m-=1
    if cur_val >=max(riskvalue) :
        cnt+=1
        # print(m,cur_val)
        if m==0:
            break
    else :
        riskvalue.append(cur_val)
        if m==0 :
            m= len(riskvalue)
        

print(cnt)    