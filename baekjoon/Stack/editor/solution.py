# sys.stdin=open('inputs.txt','r')

import sys

arr= list(sys.stdin.readline().strip())
stash =[]
for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().strip()
    if order =='L' and len(arr)!=0:
        stash.append(arr.pop())
    elif order =='D' and len(stash)!=0:
        arr.append(stash.pop())
    elif 'P' in order:
        _,char = order.split()
        arr.append(char)
    elif order == 'B' and len(arr)!=0:
        arr.pop()

# for _ in range(len(stash)): arr.append(stash.pop())
arr.extend(reversed(stash))
print(''.join(arr))
    