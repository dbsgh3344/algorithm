import sys
from collections import deque
sys.stdin = open('inputs.txt','r')

num,m = input().split()
m = int(m)
num = deque(num)
lens = len(num)-m
stack= []
idx= 0
while m!=0 and len(num)!=0:
    if len(stack)==0:
        stack.append(num.popleft())
    elif stack[-1] >= num[0]:
        stack.append(num.popleft())
    else :
        stack.pop()
        m-=1
    

ans =''.join(stack+list(num))[:-m]
print(ans)
    