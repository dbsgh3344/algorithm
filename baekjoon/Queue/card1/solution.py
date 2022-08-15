import sys
from collections import deque

# sys.stdin = open('inputs.txt')
arr= list(map(str,range(1,int(sys.stdin.readline())+1)))
arr= deque(arr)
lists =[]
while len(arr)!=1:
    lists.append(arr.popleft())
    arr.append(arr.popleft())

print(' '.join(lists+list(arr)))
