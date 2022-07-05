import sys
from collections import deque
# sys.stdin = open('inputs.txt','r')

n,k = map(int,input().split())
arr= deque(range(1,n+1))
iter =1
while len(arr)!=1:
    
    if iter ==k :
        iter =1
        arr.popleft()
    else :
        arr.append(arr.popleft())
        iter+=1

print(arr[0])