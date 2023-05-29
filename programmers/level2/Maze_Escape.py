from collections import deque
# 차원 하나를 추가해서 lever를 거쳤는지를 확인
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    maps2 = [[[0]*M for _ in range(N)] for _ in range(2)]
    st_r = None
    st_c = None
    for r in range(len(maps)) :
        if 'S' in maps[r] :
            st_c = maps[r].index('S')
            st_r = r
        
        if 'E' in maps[r] :
            ed_c = maps[r].index('E')
            ed_r = r


    xx = [0,1,0,-1]
    yy = [-1,0,1,0]
    
    bfs = deque([(0,st_r,st_c)])

    while bfs :
        chk,r,c = bfs.popleft()
        for d in range(4) :
            cur_x = c + xx[d]
            cur_y = r + yy[d]

            if cur_x < M and cur_x >= 0 and cur_y < N and cur_y >=0 and maps[cur_y][cur_x] != 'X' and not maps2[chk][cur_y][cur_x] :
                if maps[cur_y][cur_x] == 'L' : 
                    maps2[1][cur_y][cur_x] = maps2[chk][r][c] + 1
                    bfs.append((1,cur_y,cur_x))
                else :
                    maps2[chk][cur_y][cur_x] = maps2[chk][r][c] + 1
                    bfs.append((chk,cur_y,cur_x))
                
    return maps2[1][ed_r][ed_c] if maps2[1][ed_r][ed_c] else -1



# m = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
m = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
print(solution(m))