import sys
from collections import deque
# sys.stdin = open('inputs.txt','r')

n,m = map(int,input().split())
arr= list(map(int,input().split()))
arr.sort()
arr= deque(arr)

lt = 0
rt = n-1

cnt=0
while lt<=rt :
    
    if arr[lt] +arr[rt] >m :
        rt-=1
    else :
        lt+=1
        rt-=1
    cnt+=1
    
print(cnt)
    