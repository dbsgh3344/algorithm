import sys
# sys.stdin = open('inputs.txt','r')

n= int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

peaks =0
x= [-1,0,1,0]
y= [0,1,0,-1]
for i in range(n) :
    for j in range(n) :
        cur_val = arr[i][j]
        tmp_val = cur_val
        for ax in range(4) :
            xx= i+x[ax]
            yy= j+y[ax]
            if xx >= 0 and xx<n and yy >=0 and yy<n :
                if cur_val <=arr[xx][yy] :
                    tmp_val = 0
                    break
                
        if cur_val ==tmp_val :
            peaks+=1

print(peaks)

# comment
# 상하좌우에 같은 값이 존재해도 cur_val은 봉우리가 될 수 없다.

        