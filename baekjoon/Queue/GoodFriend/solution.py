import sys
from collections import deque
sys.stdin = open('inputs.txt','r')

n,k = map(int,sys.stdin.readline().split())
names = deque([sys.stdin.readline().strip() for _ in range(n)])

# --------------------- 시간초과 코드
# deq = deque([])
# cnt=deque([0])
# idx= 0
# ans=0

# deq.append(names.popleft())
# # while len(deq)!=0:
# while len(names)!=0:
#     if idx==k:
#         ans+=cnt.popleft()
#         deq.popleft()
#         idx=0

#     # if len(names)!=0:
#     next = names.popleft()
#     for i in range(len(deq)):
#         if len(deq[i])==len(next) :
#             cnt[i]+=1
    
#     deq.append(next)
#     cnt.append(0)
#     # else :
#     #     break

#     idx+=1

# ans+=sum(cnt)
# print(ans) 
    

q= list([deque() for _ in range(21)])
cnt=0
for i in range(n):
    name_len = len(names[i])-1

    while q[name_len] and i-q[name_len][0]>k:
        q[name_len].popleft()
    
    cnt+=len(q[name_len])
    q[name_len].append(i)

print(cnt)