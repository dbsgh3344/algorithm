import sys
from collections import deque
sys.stdin = open('inputs.txt','r')
n,k =map(int,sys.stdin.readline().split())

arr= list(map(str,range(1,n+1)))
idx=0
ans = []
# while len(arr)!=0:
#     if idx == k-1 :
#         ans.append(arr.popleft())
#         idx=0
#     else:
#         arr.append(arr.popleft())
#         idx+=1

# print('<'+', '.join(ans)+'>')

# 다른사람 풀이
q= 0
while len(arr)!=0:
    q = (k-1)%(n-idx)
    ans.append(arr.pop(q))
    idx+=1


print(ans)
