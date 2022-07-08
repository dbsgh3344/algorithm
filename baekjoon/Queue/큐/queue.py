import sys
from collections import deque
# sys.stdin=open('inputs.txt','r')


n= int(input())
lists = deque([])
order = [input() for _ in range(n)]


for odr in order:
    # order = input()
    if 'push' in odr :
        tmp = odr.split()
        lists.append(tmp[1])
    else :
        if odr=='size':
            print(len(lists))
        elif len(lists)==0:
            if odr=='empty' :
                print('1')
            else :
                print('-1')
        elif odr=='empty':
            print('0')
        elif odr =='front':
            print(lists[0])
        elif odr=='back':
            print(lists[-1])
        else :
            print(lists.popleft())
