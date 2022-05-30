import sys
import time
sys.stdin = open('inputs.txt','r')

n= int(input())
arr= [tuple(map(int,input().split())) for _ in range(n)]
arr = sorted(arr,reverse=True)

cnt = n
mw= 0
# idx= 0

# while idx!=n:
#     sw=arr[idx][1]
#     for i in range(idx+1,n):
#         if sw<arr[i][1]:
#             cnt-=1
#             break
        
    # idx+=1    
st = time.time()
for s,w in arr :
    if w > mw:
        mw = w
    else :
        cnt-=1
print(time.time()-st)
print(cnt)