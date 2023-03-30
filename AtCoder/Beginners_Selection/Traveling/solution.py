import sys
sys.stdin = open('./AtCoder/Beginners_Selection/Traveling/inputs.txt')
from collections import deque

n= int(input())
t = [list(map(int,input().split())) for _ in range(n)]
bfs =deque()
bfs.append((0,0,0))
xx= [1,0,-1,0]
yy=[0,1,0,-1]
ans= 'Yes'

for des_t,des_x,des_y in t:
    while bfs:
        cur_t,cur_x,cur_y = bfs.popleft()

        if cur_t==des_t and cur_x==des_x and cur_y==des_y:
            break

        if cur_t>des_t:
            ans='No'
            break

        for i in range(4):
            ax= xx[i]+cur_x
            ay= yy[i]+cur_y
            if ax>=0 and ay>=0 and (ax!=0 or ay!=0):    
                tmp=(cur_t+1,ax,ay)
                bfs.append(tmp)
        

    if ans=='No':
        break

print(ans)