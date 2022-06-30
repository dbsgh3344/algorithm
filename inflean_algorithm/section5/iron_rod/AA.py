import sys
sys.stdin= open('inputs.txt','r')

arr= input().replace('()','.')

cntlist =[]
ans = 0
for i in range(len(arr)) :
    if arr[i] =='(':
        cntlist.append(0)
    elif arr[i] =='.':
        
        cntlist =[cntlist[iter]+1 for iter in range(len(cntlist))]
    else :
        tmp = cntlist.pop()+1
        ans+=tmp 

print(ans)
# lists= []
# ans = 0
# for i in range(len(arr)):
#     if arr[i]=='(' :
#         lists.append(arr[i])
    
#     else :
#         if arr[i-1]=='(':
#             lists.pop()
#             ans+=len(lists)
#         else :
#             lists.pop()
#             ans+=1
# print(ans)
