import sys
from collections import deque

sys.stdin = open('inputs.txt')

n= int(sys.stdin.readline())
lists = deque([])

for order in sys.stdin.readlines():
    order = order.strip().split()
    if len(order)>1 :
        lists.append(order[1])
    elif len(lists)==0:
        if order[0]=='empty':
            print('1')
        elif order[0]=='size':
            print(len(lists))
        else:
            print('-1')
    elif order[0]=='front':
        print(lists[0])
    elif order[0]=='back':
        print(lists[-1])
    elif order[0]=='size':
        print(len(lists))
    elif order[0]=='empty':
        print('0')
    else:
        print(lists.popleft())

    