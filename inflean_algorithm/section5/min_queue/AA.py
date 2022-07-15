import sys
import heapq as hq
# sys.stdin=open('inputs.txt','r')

hplist = []
while True:
    digit = int(input())

    if digit == -1:
        break
    elif digit ==0:
        if len(hplist)==0:
            print('-1')
        else:
            print(hq.heappop(hplist))
    else:
        hq.heappush(hplist,digit)



