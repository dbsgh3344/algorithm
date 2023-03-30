import sys
sys.stdin = open('./AtCoder/Beginners_Selection/DayDream/inputs.txt')

## 다른 사람 풀이 
s= input()
t= ['eraser','erase','dream','dreamer']
# dicts= {}

s= s.replace('eraser','')
s= s.replace('erase','')
s= s.replace('dreamer','')
s= s.replace('dream','')

if len(s)!=0:
    print('NO')
else :
    print('YES')


## 처음 풀이
s= input()
t= ['eraser','erase','dreamer','dream']
for i in t:
    if i in s:
        s=s.replace(i,'')
 
if s=='':
    print('YES')
else :
    print('NO')


# def find_txt(cur_s) :
#     if cur_s in dicts and dicts[cur_s]=='YES':
#         return 'YES'

#     if len(cur_s)==0:
#         return 'YES'

#     for i in t:
#         if cur_s.startswith(i):            
#             if find_txt(cur_s[len(i):]) == 'YES':
#                 dicts[cur_s] = 'YES'
#                 return 'YES'
    
#     dicts[cur_s]='NO'
#     return 'NO'

# print(find_txt(s))

# list = ['dreamer','dream', 'erase', 'eraser']
# dict = {}
 
# def solution(x):
#     if x in dict and dict[x] == 'YES':
#         return 'YES'
 
#     if (len(x) == 0):
#         return "YES"
#     for word in list:
#         if x.startswith(word):
#             # print(x[len(word):],word)
#             if solution(x[len(word):]) == 'YES':
#                 dict[x] = 'YES'
#                 return 'YES'
#     dict[x] = 'NO'
#     return "NO"
 
 
# print(solution(input()))


