import sys
sys.stdin = open('inputs.txt','r')
brackets= sys.stdin.readline()
stack =[]
endCheck=True
for b in brackets :
    if len(stack)==0:
        stack.append(b)
    elif b=='(' or b=='[':
        stack.append(b)
    # elif b==')':
        
try:
    if not endCheck:print(0)
    else :print(sum(stack))
except:
    print(0)