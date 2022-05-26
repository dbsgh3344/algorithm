import sys
# sys.stdin = open('inputs.txt','r')

n= int(input())
arr= [tuple(map(int,input().split())) for _ in range(n)]
sortarr= sorted(arr,key=lambda x:x[0])
idx=0
res = 0
while idx!=n :
    cnt =1
    base =sortarr[idx]
    start = sortarr[idx][0]
    end =sortarr[idx][1]

    for i in range(n) :
        if i==idx:
            continue
        else :
            if end >sortarr[i][0] :
                continue
            else :
                start = sortarr[i][0]
                end = sortarr[i][1]
                cnt+=1 
    
    if res <cnt :
        res = cnt

    idx+=1
    
print(res)
    