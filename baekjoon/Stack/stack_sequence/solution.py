import sys
sys.stdin = open('inputs.txt','r')

n= int(input())
ans = [int(input()) for _ in range(n)]
arr= list(range(n,0,-1))


result= []
lists= []
ans_str= ''

for i in range(len(ans)) :
    cur_val = ans[i]
    while len(arr)!=0:
        if len(lists)!=0 and lists[-1]==cur_val:
            result.append(lists.pop())
            ans_str+='-\n'
            break
        else :
            lists.append(arr.pop())
            ans_str+='+\n'

for _ in range(len(lists)):
    result.append(lists.pop())
    ans_str+='-\n'

if result == ans :
    print(ans_str)
else :
    print('NO')
