import sys
from collections import deque
# sys.stdin= open('inputs.txt','r')

n,k = map(int,input().split())
arr = deque(range(1,n+1))
ans='<'

while len(arr)!=1:
    for i in range(k-1):
        cur_val = arr.popleft()
        arr.append(cur_val)
    
    cur_val=arr.popleft()
    ans+=f'{str(cur_val)}, '
        
print(ans+str(arr.pop())+'>')


# while문 안에서 idx증가시켜가며 실행시키면 시간초과
# while문 안에서 반복문 사용해야 함