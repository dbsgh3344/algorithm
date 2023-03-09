import sys
sys.stdin=open('./baekjoon/Queue/Olympiad_Pizza/inputs.txt')
from collections import deque

n= int(input())
contestant = {idx:int(i) for idx,i in enumerate(input().split())}
q = deque()
ans= [0]*n
i=0
cnt=0
for (k,v) in contestant.items():
    if contestant[k]!=0:
        q.append(k)
        contestant[k]-=1
        

while q:
    k=q.popleft()
    cnt+=1
    if contestant[k]!=0:
        q.append(k)
        contestant[k]-=1        
    else :
        ans[k]=str(cnt)


print(' '.join(ans))
# 출력 format 좀 정답에 맞추자






