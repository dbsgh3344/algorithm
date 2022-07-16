# import sys
# sys.stdin = open('inputs.txt','r')

n= int(input())

parentheses = [input() for _ in range(n)]

for i in range(len(parentheses)) :
    stack = []
    for j in range(len(parentheses[i])) :
        
        if len(stack)==0:
            if parentheses[i][j]==')': 
                print('NO')
                break
            else :
                stack.append(parentheses[i][j])
        elif parentheses[i][j]=='(' :
            stack.append(parentheses[i][j])
        elif parentheses[i][j]==')':
            tmp =stack.pop()
            if tmp!='(':
                print('NO')
                break
        
    else :
        if len(stack)==0:
            print('YES') 
        else :
            print('NO')