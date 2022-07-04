import sys
# sys.stdin=open('inputs.txt')

arr= input()
stack =[]
for i in range(len(arr)) :
    if arr[i].isdigit():
        stack.append(arr[i])
    else :
        a= stack.pop()
        b= stack.pop()
        tmp =0
        exec(f'tmp ={b}{arr[i]}{a}')
        stack.append(tmp)

print(stack.pop())