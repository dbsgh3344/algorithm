import sys
# sys.stdin = open('inputs.txt','r')

n= int(input())
arr= [tuple(map(int,input().split())) for _ in range(n)]
sortarr= sorted(arr,key=lambda x:x[1])
et = 0
cnt = 0
for s,e in sortarr :
    if s >= et :
        et = e
        cnt+=1
        

print(cnt)
    