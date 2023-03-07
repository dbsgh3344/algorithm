import sys
from collections import deque
sys.stdin = open('./baekjoon/Queue/queuestack/inputs.txt')


n= int(input())
ds_list=list(map(int,input().split()))
# queue자료구조 원소만 보관 후 list의 마지막이 첫 원소가 되도록 list reverse
values = deque([i for idx,i in enumerate(input().split()) if ds_list[idx]==0][::-1]) 
m = int(input())
new_values= list(map(int,input().split()))
ans=[]

# 시간초과

# for v in new_values:
#     replace_val =v
#     for i in range(n):
#         if ds_list[i]==0:
#             tmp = values[i]
#             values[i]=replace_val
#             replace_val=tmp

#     ans.append(str(replace_val))

# print(' '.join(ans))
# --------------------------

for v in new_values:
    values.append(v)    
    ans.append(values.popleft())    # 결국 맨 처음 원소를 pop하는 것과 마찬가지기 때문에 새로운 원소 들어올 때마다 pop

    
[print(i,end=' ') for i in ans]
