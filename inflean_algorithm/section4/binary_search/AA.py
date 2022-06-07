from re import T
import sys
# sys.stdin = open('inputs.txt','r')

n,m = map(int,input().split())
arr= list(map(int,input().split()))
arr= sorted(arr)

lt =0
rt = n-1
res = 0
while lt<=rt :
    thres = (lt+rt)//2
    if arr[thres] >m :
        rt= thres
    elif arr[thres] < m:
        lt = thres 
    else :
        res = thres+1
        break

print(res)
