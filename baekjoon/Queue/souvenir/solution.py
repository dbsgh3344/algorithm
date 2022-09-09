import sys
from collections import deque
# sys.stdin=open('inputs.txt','r')

n= int(sys.stdin.readline())
if n==1: print(1)
else :
    arr= deque(list(range(2,n+1)))
    cnt=2
    end = 1
    while len(arr)>1:
        stage =cnt**3
        if stage%len(arr)!=0:
            iters = stage%len(arr)
            for _ in range(iters) : 
                arr.append(arr.popleft())

        arr.pop()

        cnt+=1
    print(arr[0])

    

