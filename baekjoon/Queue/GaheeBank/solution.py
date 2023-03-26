import sys
sys.stdin = open('./inputs.txt')
from collections import deque

n,t,w = map(int,sys.stdin.readline().split())
waiting_c = deque([tuple(map(int,sys.stdin.readline().split())) for _ in range(n)])
m= int(sys.stdin.readline())
added_c = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]
added_c = deque(sorted(added_c,key=lambda x:x[2]))

q = waiting_c
cur_t=0
ans= []

while q and len(ans)<w:
    customer= q.popleft()
    idx,work_t= customer
    add_q=None
    if t-work_t>=0:
        add_t= work_t
        
    else :
        add_t=t
        add_q = (idx,work_t-t)
    cur_t+=add_t
    ans += [idx]*add_t
        
    while added_c and cur_t>=added_c[0][2]:
        tmpidx,tmpwork_t,_=added_c.popleft()
        q.append((tmpidx,tmpwork_t))
    
    if add_q!=None:
        q.append(add_q)

print(*ans[:w],sep='\n')



# 시간초과 풀이
# while q and len(ans)<w:
#     customer= q.popleft()
#     if len(customer)==2:
#         idx,work_t= customer
#         if t-work_t>=0:
#             add_t= work_t
#         else :
#             add_t=t
#             add_q = (idx,work_t-t)
#             q.append(add_q)        
#         cur_t+=add_t
#         ans += [idx]*add_t
            
#     else :
#         idx,work_t,c= customer
#         if cur_t<c:
#             q.append(customer)
#         else :
#             if t-work_t>0:
#                 add_t= work_t
#             else :
#                 add_t=t
#                 add_q = (idx,work_t-t)
#                 q.append(add_q)
            
#             ans += [idx]*add_t
#             cur_t+=add_t
        
# print(*ans[:w],sep='\n')
    
            









        
