import sys
# from collections import deque
sys.stdin=open('inputs.txt','r')

n= int(input())
# arr= deque([input() for _ in range(n)])
# for i in range(n-1):
#     del_char =input()
#     for j in range(len(arr)):
#         cur_val= arr.popleft()
#         if cur_val!=del_char:
#             arr.append(cur_val)
    

# print(arr.popleft())

arr= {input():1 for _ in range(n)} 

for i in range(n-1):
    del_word = input()
    if del_word in arr.keys():
        arr[del_word]=0

for k,v in arr.items():
    if v!=0:
        print(k)
        break