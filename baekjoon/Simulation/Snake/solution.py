# 뱀의 머리가 꼬리뿐만아니라 몸통 어디에라도 부딪힐 수 있다는걸 간과했음.
import sys
sys.stdin= open('/home/song/code/algo/algorithm/baekjoon/Simulation/Snake/inputs.txt','r')
from collections import deque

n = int(input())
apple_len = int(input())
app_coord = [list(map(int,input().split())) for _ in range(apple_len)]
direc_len = int(input())
direc_info = deque([list(input().split()) for _ in range(direc_len)])

xx = [0,1,0,-1] # 북,동,남,서 방향
yy = [-1,0,1,0]

d = 1

bfs = deque([(0,0)])    # 시작위치 
cur_direc_info = direc_info.popleft()   # 첫번째 방향전환 값 get
t = 0

while True : 
    t += 1
    y,x = bfs[-1]   # 뱀 머리 좌표 get

    cur_x = x + xx[d]   # 뱀 머리 좌표 + 나아갈 좌표
    cur_y = y + yy[d]
    

    if t == int(cur_direc_info[0]) :    # 현재시간과 방향전환 시간 비교
        if cur_direc_info[1] == 'D' :
            d = 0 if d == 3 else d + 1
        else :
            d = 3 if d == 0 else d - 1
        cur_direc_info = direc_info.popleft() if direc_info else cur_direc_info


    if cur_x >= n or cur_x < 0 or cur_y >= n or cur_y < 0 or (cur_y,cur_x) in bfs:  # 벽, 뱀의 몸통에 닿는지 체크
        break 
    
    if [y+1,x+1] in app_coord : # 사과가 있는 좌표인지 체크
        app_coord.remove([y+1,x+1])
    else :
        bfs.popleft()   # 사과 없는 좌표면 꼬리 땡겨

    
    bfs.append((cur_y,cur_x))   # 머리가 도착할 좌표 append

print(t)