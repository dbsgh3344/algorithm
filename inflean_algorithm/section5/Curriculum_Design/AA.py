import sys
from collections import deque
# sys.stdin=open('inputs.txt','r')

subject= input()
n= int(input())

for i in range(n) :
    arr= input()
    deq_sbj = deque([c for c in subject])
    for char in arr:
        if char in deq_sbj:
            if char!=deq_sbj.popleft() :
                print(f'#{i+1} NO')
                break                
    else :
        if len(deq_sbj)==0:
            print(f'#{i+1} YES')
        else:
            print(f'#{i+1} NO')            
