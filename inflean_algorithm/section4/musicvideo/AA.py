import sys
# sys.stdin = open('inputs.txt','r')


n,m = map(int,input().split())
arr= list(map(int,input().split()))

lt=1
rt = sum(arr)
idx= 0
res = 23430435
thres = (lt+rt)//2
while lt <=rt :
    tmpcum=0
    cnt=1
    for i in range(len(arr)) :
        if tmpcum+arr[i] <=thres :
            tmpcum+=arr[i]
        else :
            tmpcum= arr[i]
            cnt+=1
            
    if cnt <=m :
        if res > thres :
            res = thres
        rt= thres-1
    elif cnt>m :
        lt = thres+1
    

    thres = (lt+rt)//2
       
    
print(res)
    