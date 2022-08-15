import sys
from collections import deque
# sys.stdin = open('inputs.txt','r')

n,k = map(int,sys.stdin.readline().split())
names = deque([sys.stdin.readline().strip() for _ in range(n)])
deq = deque([])
cnt=0
idx= 0
deq.append(names.popleft())
while len(names)!=1:
    if len(deq)>k:
        deq.popleft()
    
    if len(deq)>1:
        if len(deq[0])==len(deq[-1]) :
            cnt+=1
    

    deq.append(names.popleft())
        

    
print(cnt)