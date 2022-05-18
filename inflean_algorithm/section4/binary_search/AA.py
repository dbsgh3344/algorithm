import sys
import time
# st = time.time()
# sys.stdin = open('inputs.txt','r')

n,m = map(int,input().split())
arr= list(map(int,input().split()))

# for i in range(len(arr)) :
#     for j in range(i,len(arr)) :
#         if arr[i] > arr[j] :
#             tmp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = tmp

arr = sorted(arr)

lt = 0
rt = n-1
while True :
    mid = (lt+rt)//2

    if arr[mid]==m :
        print(mid+1)
        break
    elif arr[mid] > m :
        rt= mid-1
    else :
        lt = mid+1

# print(time.time()-st)
    