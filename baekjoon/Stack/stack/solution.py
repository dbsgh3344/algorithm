# import sys
# sys.stdin= open('inputs.txt','r')

n =int(input())
orders= [input() for _ in range(n)]
stacks= []
for order in orders:
    if 'push' in order :
        _,digit = order.split()
        stacks.append(digit)
    elif len(stacks)==0:
        if order =='empty':
            print('1')
        elif order == 'size' :
            print(len(stacks))
        else:
            print('-1')

    elif order =='pop':print(stacks.pop())
    elif order=='size' :print(len(stacks))
    elif order =='empty':print('0')
    else : print(stacks[-1])
        