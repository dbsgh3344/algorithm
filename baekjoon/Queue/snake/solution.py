import sys
from collections import deque
sys.stdin = open('inputs.txt')

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
appleaxis = [tuple(map(int,sys.stdin.readline().split())) for _ in range(k)] 
l = int(sys.stdin.readline())
directions = [tuple(sys.stdin.readline().split()) for _ in range(l)]

ar= [0,1,0,-1]
ac = [1,0,-1,0]

arr = [[0]*n for _ in range(n)]
q= deque([(0,0)])
for r,c in appleaxis:
    arr[r-1][c-1] =1

tmp_direction = 'D'
for i in range(n) :
    for j in range(n):
        if tmp_direction=='D':
            q.append((i,j))
            if arr[i][j]!=1:
                q.popleft()
            
        else :
            

    
            
