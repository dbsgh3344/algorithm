import sys
# sys.stdin = open('inputs.txt','r')

n,c = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])

lt =1
rt = arr[-1]

res= 0
while lt<=rt :
    cnt =1
    thres = (rt+lt)//2
    
    tmp =0
    for i in range(1,len(arr)) :
        if abs(arr[tmp]-arr[i]) >=thres :
            cnt+=1
            tmp =i
    

    if cnt >=c:
        if res < thres :
            res = thres
        lt= thres +1
    else :
        rt = thres-1
    


print(res)