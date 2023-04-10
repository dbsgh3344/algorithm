import sys
sys.stdin = open('./AtCoder/Beginner_Contest_296/Gap_Existence/inputs.txt')
from itertools import combinations


# 시간초과
def solution():
    n,x = map(int,input().split())
    d_list = list(map(int,input().split()))
    if not x:
        return 'Yes'

    # a= list(filter(lambda c: c[0]-c[1]==x or c[1]-c[0]==x ,combinations(d_list,2)))
    for c in combinations(d_list,2):
        if c[0]-c[1]==x or c[1]-c[0]==x:
            return 'Yes'
        
    return 'No'
# print(solution())


# 최대값에서 그 다음 최대값을 뺀 값이 x보다 클 때까지 반복
# x보다 크면 break 후 다음 최대값을 기준으로 위 과정 반복
def solution2() :
    n,x = map(int,input().split())
    d_list = sorted(list(map(int,input().split())),reverse=True)
    x=abs(x)
    if not x:
        return 'Yes'
    
    r=1
    for i in range(n-1):
        cur_d = d_list[i]
        while r < n and cur_d - d_list[r] <= x :
            if cur_d - d_list[r] == x:
                return 'Yes'
            r+=1

    return 'No'
    
print(solution2())
    