import sys
from itertools import combinations
# sys.stdin = open('inputs.txt','r')

n,m = map(int,input().split())
numlist = list(map(int,input().split()))

answer = 0


for i in range(len(numlist)):
    cnt = numlist[i]    
    for j in range(i+1,len(numlist)) :
        if cnt ==m :
            break
        elif cnt > m:
            break
        else :
            cnt+=numlist[j]
    
    if cnt ==m :
        answer+=1

print(answer)
    
