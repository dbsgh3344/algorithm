import sys
# sys.stdin = open('inputs.txt','r')

n= int(input())
arr= list(map(int,input().split()))
m=int(input())
arr.sort()
for _ in range(m) :
    # maxval = arr.index(max(arr))
    # minval= arr.index(min(arr))
    # arr[maxval]-=1
    # arr[minval]+=1
    arr[-1]-=1
    arr[0]+=1
    arr.sort()

print(max(arr)-min(arr))
    