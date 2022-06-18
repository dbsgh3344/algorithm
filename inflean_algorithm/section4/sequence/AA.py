import time
import sys
sys.stdin= open('inputs.txt','r')

n= int(input())
arr= list(map(int,input().split()))

lt = 0
rt = n-1
seq = 0
res =''
st = time.time()
# while True :
#     mins =min(arr[lt],arr[rt]) if min(arr[lt],arr[rt]) > seq else max(arr[lt],arr[rt])
#     if mins >seq :
#         seq = mins
#         if arr.index(mins) == rt:
#             rt-=1
#             res+='R'
#         elif arr.index(mins) == lt :
#             lt+=1
#             res+='L'
#     else :
#         break

while lt <=rt :
    lists =[]
    lists.append((arr[lt],'L'))
    lists.append((arr[rt],'R'))
    lists =sorted(lists,key= lambda x: x[0])

    for num,p in lists :
        if num> seq:
            seq= num
            res+=p
            if p =='L': lt+=1
            else : rt-=1
            break
    if num < seq:
        break
    

print(time.time()-st)
print(len(res))
print(res)