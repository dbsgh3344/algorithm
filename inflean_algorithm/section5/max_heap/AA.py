from re import L
import sys
import heapq as hq

# sys.stdin=open('inputs.txt','r')

hqlist = []

while True :
    order = int(input())
    
    if order ==-1:
        break
    elif order ==0:
        print(hq.heappop(hqlist)*-1)
    else :
        hq.heappush(hqlist,order*-1)

        
