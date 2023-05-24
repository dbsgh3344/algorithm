
# import sys
# sys.stdin= open('/home/song/code/algo/algorithm/baekjoon/Simulation/Robot_Cleaner/inputs.txt','r')
from collections import deque

n,m = map(int,input().split())
r,c,d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(n)]

xx = [0,1,0,-1]
yy = [-1,0,1,0]
cnt = 0

bfs = deque()
bfs.append((r,c))

while bfs :
    y,x = bfs.popleft()
    if room[y][x] == 0 :
        room[y][x] = 2
        cnt += 1

    chk_clean = False
    for k in range(4) : # 동서남북 청소할 곳 체크
        cur_x = x + xx[k]
        cur_y = y + yy[k]

        if cur_x <= m and cur_x >= 0 and cur_y <= n and cur_y >= 0 and room[cur_y][cur_x] == 0 :
            chk_clean = True

    if chk_clean :  # 청소할 곳이 있다면
        while True :
            d = 3 if d == 0 else d - 1
            ny = y + yy[d]
            nx = x + xx[d]
            if room[ny][nx] == 0 :
                bfs.append((ny,nx))
                break
            
    else :  # 청소할 곳이 없다면
        ny = y - yy[d]
        nx = x - xx[d]
        if room[ny][nx] != 1 :  # 후진한 곳이 벽이 아니라면
            bfs.append((ny,nx))
        else :  # 후진한 곳이 벽이면
            break
            
print(cnt)
            