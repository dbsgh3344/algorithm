import sys
from collections import deque
import time
sys.stdin = open('inputs.txt','r')

st= time.time()
n= int(sys.stdin.readline())
buffer =deque()
size= 0
while True:
    order = sys.stdin.readline().strip()
    if order=='-1': break
    elif order=='0': 
        buffer.popleft()
        size-=1
    else:
        if size<n:
            buffer.append(order)
            size+=1


if not buffer:print('empty')
else : print(*buffer)
# print(time.time()-st)