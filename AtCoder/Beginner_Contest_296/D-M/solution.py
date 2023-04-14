import sys
sys.stdin = open('./AtCoder/Beginner_Contest_296/D-M/inputs.txt')



# def solution():    
#     n,m = map(int,input().split())
#     a= list(range(1,n+1))
#     if a[-1]**2<m:
#         return -1
#     elif a[-1]**2==m:
#         return a[-1]**2
    
#     ans =-1
#     for i in range(n-1):
#         if a[i]*a[n-1] <m:
#             continue
#         elif a[i]*a[n-1] ==m:
#             ans = a[i]*a[n-1]
#             return ans
#         else :
#             r=i+1
#             while r<n-1 and a[i]*a[r]<m:
#                 r+=1
#                 if a[i]*a[r]>=m:
#                     ans = a[i]*a[r]
#                     return ans
        
#     return ans
# print(solution())

# 위에서 아래로
def solution():    
    n,m = map(int,input().split())
    a= list(range(1,n+1))
    if a[-1]**2<m:
        return -1
    elif a[-1]**2==m:
        return a[-1]**2

    r=n-1
    ans =9999999999999
    for i in range(n):
        while r>=i and a[r]*a[i]>m:
            if ans > a[r]*a[i]:
                ans = a[r]*a[i]
            r-=1
        
    return ans

# print(solution())

# 다른사람풀이
# 이해 못함 나중에 다시 풀기
def solution2():    
    n,m = map(int,input().split())

    ans =10e12
    for i in range(1,n+1):
        x= (m+i-1)/i
        print(x,i)
        if x<=n and x*i >=m: # x*i>=m 은 무조건 참 x<=n은 이해못함
            ans= min(ans,x*i)
    
        if i>=x:
            break
        
    return ans if ans!=10e12 else -1

print(solution2())





