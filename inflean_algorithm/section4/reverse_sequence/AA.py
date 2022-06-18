import sys
import time
sys.stdin = open('inputs.txt','r')

n= int(input())
arr= list(map(int,input().split()))
arr= arr[::-1]
lists = []

# 초기방법
st= time.time()
for idx,num in enumerate(arr) :
    idx= len(arr)-idx
    lists.insert(num,str(idx))

print(time.time()-st)
# 초기방법 시간 0초

# 정석
# st = time.time()
# for i in range(n) :
#     cnt=0
        
#     # lists[idx+1]=i+1
#     for j in range(len(lists)) :
#         if cnt==arr[i] and lists[j]==0:
#             lists[j]=str(i+1)
#             break
#         if lists[j]==0:
#             cnt+=1
# print(time.time()-st)
# 정석 방법 시간 0.0010027885437011719초
print(' '.join(lists))





 