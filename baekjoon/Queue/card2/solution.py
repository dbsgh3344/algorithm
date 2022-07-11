import sys
from collections import deque
# sys.stdin = open('inputs.txt','r')

n= int(input())
arr= deque(range(1,n+1))

while len(arr)!=1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr.popleft())