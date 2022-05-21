import sys
sys.stdin = open('inputs.txt','r')


n,m = map(int,input().split())
arr= list(map(int,input().split()))

lt=1
rt = sum(arr)
thres = (lt+rt)//2
idx= 0

while True :
    tmpcum=0
    cnt=0
    for i in range(len(arr)) :
        if tmpcum+arr[i] <=thres :
            tmpcum+=arr[i]
        else :
            
            cnt+=1
    
    
    