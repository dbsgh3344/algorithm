import sys
# sys.stdin = open('inputs.txt','r')

k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]

lt=0
rt=max(arr)
result = 0
while lt<rt :
    thres = (lt+rt)//2
    cnt = 0
    for i in range(len(arr)) :
        cnt+= arr[i]//thres

    if cnt>n :
        lt = thres
    elif cnt<n :
        rt = thres
    else :
        result = thres
        break


print(result)