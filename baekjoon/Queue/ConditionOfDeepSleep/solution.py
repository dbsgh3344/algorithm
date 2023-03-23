import sys
# sys.stdin = open('./Queue/ConditionOfDeepSleep/inputs.txt')
from collections import deque
sys.stdin = open('inputs.txt')
n,k = map(int,sys.stdin.readline().split())
s = deque(map(int,sys.stdin.readline().split()))
cnt=0
flip_cnt=0
new_s = [0 if i==0 else s[i]^s[i-1] for i in range(n)]
cnt= 0

# for i in range(1,n):
#     new_s[i] ^=s[i-1]
#     new_s[i+k] ^=s[]



# print(cnt) if flip_cnt==0 else print('Insomnia')


# 풀이 이해 못해서 다음에 다시 풀기