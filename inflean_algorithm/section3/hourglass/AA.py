from collections import deque
import sys
# sys.stdin =open('inputs.txt','r')

n= int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

m = int(input())
orders= [list(map(int,input().split())) for _ in range(m)]


for i in range(m) :
    row,direction,rotate = orders[i]
    row = row-1
    if direction ==0 :
        tmp = deque(arr[row])
        for i in range(rotate) :
            tmp.append(tmp.popleft())            
            
        arr[row] = tmp

    elif direction==1 :
        tmp = deque(arr[row])
        for i in range(rotate) :
            # tmp.insert(0,tmp.pop())
            tmp.appendleft(tmp.pop())

        arr[row] = tmp    

e= len(arr)
s= 0
cnt = 0
for i in range(len(arr)):
    for j in range(s,e) :
        cnt+=arr[i][j]
    
    if i<n//2 :
        s+=1
        e-=1
    else :
        s-=1
        e+=1



print(cnt)