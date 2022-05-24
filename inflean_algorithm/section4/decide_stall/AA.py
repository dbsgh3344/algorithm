import sys
sys.stdin = open('inputs.txt','r')

n,c = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])

lt =0
rt = n-1
thres = (rt+lt)//2
res= 234234
while lt<=rt :
    left = abs(arr[lt]-arr[thres])
    right = abs(arr[rt]-arr[thres])
    minimum= min(left,right)
    # if left > right :
        
    
    if res > minimum:
        res = minimum
    