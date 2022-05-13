
import sys
sys.stdin = open('inputs.txt','r')

n= int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt =0
# for i in range(n) :
#     cnt+=sum(arr[i])
#     for j in range(abs((n//2)-i)) :
#         front =arr[i][j]
#         end = arr[i][n-j-1]
#         cnt-=front
#         cnt-=end
s=e= n//2
for i in range(n) :
    for j in range(s,e+1) :
        cnt+= arr[i][j]

    if i >= n//2 :
        s +=1
        e-=1
    else :
        s -=1
        e+=1
        

print(cnt)
