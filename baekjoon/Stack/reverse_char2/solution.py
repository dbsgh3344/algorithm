import sys
import os
sys.stdin = open('/home/song/code/algo/algorithm/baekjoon/Stack/reverse_char2/inputs.txt')

def pop_stack():
    while stacks :
        ans.append(stacks.pop())

str_input= sys.stdin.readline()
stacks =[]
ans =[]
strs= ''
chk_tag=False
tags=[]
idx=0

while idx < len(str_input):
    cur_char =str_input[idx]
    if cur_char=='<' :
        if len(stacks)!=0:
            # while stacks :
            #     ans.append(stacks.pop())
            pop_stack()
        while str_input[idx]!='>':
            tags.append(str_input[idx])     
            idx+=1
        tags.append(str_input[idx])
        ans.append(''.join(tags))
        tags=[]

    else :
        if cur_char!=' ':
            stacks.append(cur_char)
        else :
            # while stacks:
            #     ans.append(stacks.pop())
            pop_stack()
            ans.append(cur_char)


    idx+=1

if stacks:
    pop_stack()

a=''.join(ans)
print(a)
