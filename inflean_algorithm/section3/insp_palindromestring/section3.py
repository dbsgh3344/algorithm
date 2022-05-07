import sys
sys.stdin = open("inputs.txt",'r')

n= int(input())

for iter in range(n) : 
    strs = input().lower()
    size = len(strs)
    cnt=0
    for i in range(size//2) :
        rev =strs[size-1-i]
        inv = strs[i]
        if rev==inv :
            cnt+=1
        else :
            break
    
    if cnt== size//2:
        print(f'#{iter+1} YES')
    else :
        print(f'#{iter+1} NO') 

