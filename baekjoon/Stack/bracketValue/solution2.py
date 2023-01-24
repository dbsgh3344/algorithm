import sys
import os
sys.stdin=open('/home/song/code/algo/algorithm/baekjoon/Stack/bracketValue/inputs.txt','r')

# brackets= sys.stdin.readline()
brackets= input()

## solved 마지막 괄호 처리가 안되어있어서 fail이었음
def bracket_loop(close_bracket):
    mp_val =2
    if close_bracket==')': open_bracket= '('
    else : 
        mp_val=3
        open_bracket='['
    tmp=0
    last_val = stack.pop()
    while last_val!=open_bracket:
        if type(last_val)==int:
            tmp+=last_val
        else :
            return 0

        if not stack:
            return 0
        last_val=stack.pop()

    return mp_val*tmp if tmp!=0 else mp_val


stack =[]
for c in brackets :
    if c=='(' :
        stack.append(c)
    elif c=='[':
        stack.append(c)
    else:
        if len(stack)==0:
            break
        score=bracket_loop(c)
        if score==0:
            stack=[]
            break        
        stack.append(score)
    print(stack)
try :
    answer =sum(stack)
except:
    answer=0

print(answer)
