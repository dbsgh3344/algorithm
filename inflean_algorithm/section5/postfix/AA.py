import sys
from collections import deque
# sys.stdin = open('inputs.txt','r')

expn = input()
digits = ''
opers =[]
tmpoper=''
check=0
iter=0
# for iter in range(len(expn)) :
while iter<len(expn):
    if expn[iter].isdigit():
        digits+=expn[iter]
        iter+=1
    elif expn[iter]==')' :
        tmp = opers.pop()
        if tmp !='(' :
            digits+=tmp
        else:
            iter+=1
    else :
        if expn[iter]=='(':
            opers.append(expn[iter])
            iter+=1
        elif len(opers)==0:
            opers.append(expn[iter])
            iter+=1
        elif expn[iter] in ['+','-']:
            if opers[-1]!='(':
                digits+=opers.pop()
            else :
                opers.append(expn[iter])
                iter+=1
        else :
            if opers[-1] in ['*','/']:
                digits+=opers.pop()
            else :
                opers.append(expn[iter])
                iter+=1
            

print(digits+''.join(opers[::-1]))
            





