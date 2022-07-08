import sys
from collections import deque
sys.stdin = open('inputs.txt','r')

n,m = map(int,input().split())
emergency_score = list(map(int,input().split()))
cnt =0
# m=m+1
# while True :
#     cur_val = riskvalue.popleft()
#     m-=1
#     if cur_val >=max(riskvalue) :
#         cnt+=1
#         # print(m,cur_val)
#         if m==0:
#             break
#     else :
#         riskvalue.append(cur_val)
#         if m==0 :
#             m= len(riskvalue)
        

# print(cnt)    

emergency_score = deque([(idx,item) for idx,item in enumerate(emergency_score)])

while True :
    cur_val = emergency_score.popleft()
    
    if cur_val[1]>=max(list(map(lambda x: x[1],emergency_score))) :
        cnt+=1
        if cur_val[0]==m :
            break
    else :
        emergency_score.append(cur_val)


print(cnt)