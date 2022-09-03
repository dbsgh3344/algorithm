import sys
import heapq

sys.stdin = open('inputs.txt','r')

a,b,n = map(int,sys.stdin.readline().split())
q= []
heapq.heapify(q)
blist=[]
rlist=[]
r_t,b_t=0,0
for _ in range(n) :
    t,color,num=  sys.stdin.readline().split()
    t,num = int(t),int(num)

    if color=='B' and b_t > t:
        t= b_t
    elif color=='R' and r_t >t:
        t= r_t
    
    for i in range(num):
        if color=='B':
            heapq.heappush(q,(t+a*i,color))
        else : 
            heapq.heappush(q,(t+b*i,color))

    if color=='B' : b_t = t+a*(i+1)
    else : r_t = t+b*(i+1)

cnt=1
print(q)
for i in range(len(q)):
    v = heapq.heappop(q)
    # print(v)
    if v[1]=='B':
        blist.append(str(i+1))
    else :
        rlist.append(str(i+1))

print(len(blist))
print(' '.join(blist))
print(len(rlist))
print(' '.join(rlist))