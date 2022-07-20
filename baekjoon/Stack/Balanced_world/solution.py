import sys
import re 
# sys.stdin = open('inputs.txt','r')

parenthesis = ['(','[']
pat = re.compile('[a-zA-Z.\n ]')
for line in sys.stdin:
    line = line.strip('.').strip('\n')
    if line=='':continue
    tmp =pat.sub('',line)
    stack =[]
    for char in tmp:
        if len(stack)==0 or char in parenthesis:
            stack.append(char)
        elif char==')':
            if stack[-1]=='(':
                stack.pop()
            else :
                break
        elif char ==']':
            if stack[-1]=='[':
                stack.pop()
            else :
                break
    # print(stack)
    if len(stack)==0:
        print('yes')
    else :
        print('no')
    