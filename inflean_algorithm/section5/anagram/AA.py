import sys
from collections import deque
# sys.stdin = open('inputs.txt','r')

def savechar(chars):
    dicts = {}
    for char in chars:
        dicts[char]= dicts.get(char,0)+1
    return dicts


a= input()
b= input()

aa= savechar(a)
bb = savechar(b)

if aa==bb:
    print('YES')
else :
    print('NO')
# print(aa,bb)
# for k,v in aa.items():
#     if k in bb:
#         if v!=bb[k]:
#             print('NO')
#             break
#     else :
#         print('NO')
#         break
# else :
#     print('YES')