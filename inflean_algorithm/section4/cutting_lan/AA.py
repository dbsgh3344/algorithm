import sys
# sys.stdin = open('inputs.txt','r')

k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]

lt=1
rt=max(arr)

result = 0
while lt <=rt :
    thres = (lt+rt)//2
    cnt = 0
    for i in range(len(arr)) :
        cnt+= arr[i]//thres

    if cnt>=n :
        if result < thres :
            result = thres

        lt = thres+1
    elif cnt<n :
        rt = thres-1
    # else :
    #     result = thres
    #     break


print(result)