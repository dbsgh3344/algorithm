import sys
from itertools import combinations
# sys.stdin = open('inputs.txt','r')

n,m = map(int,input().split())
numlist = list(map(int,input().split()))
answer = 0


# for i in range(len(numlist)):
#     cnt = numlist[i]    
#     for j in range(i+1,len(numlist)) :
#         if cnt ==m :
#             break
#         elif cnt > m:
#             break
#         else :
#             cnt+=numlist[j]
    
#     if cnt ==m :
#         answer+=1

# print(answer)
    

lt = 0
rt = 1
tot = numlist[lt]

while lt!=len(numlist)-1 :
    if tot < m:
        if rt >= len(numlist) :
            break
        tot+=numlist[rt]
        rt+=1
    elif tot ==m :
        answer+=1
        tot-=numlist[lt]
        lt+=1
    else :
        tot-=numlist[lt]
        lt+=1



print(answer)