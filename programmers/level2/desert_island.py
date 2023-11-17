from collections import deque
def solution(maps) :
    len_r = len(maps[0])
    len_c = len(maps)
    grid = [[0]*len_r for _ in range(len_c)]
    
    direc_r = [0,1,0,-1]
    direc_c = [-1,0,1,0]

    
    bfs = deque()
    result = []
    for c in range(len_c) :
        for r in range(len_r) :
            if maps[c][r].isdigit() and grid[c][r] != 1 :
                food_cnt = 0
                bfs.append([r,c])
                grid[c][r] = 1
                while bfs :
                    direction = bfs.popleft()
                    cur_r,cur_c = direction[0],direction[1]
                    
                    food_cnt += int(maps[cur_c][cur_r])
                    for i in range(4) :
                        rr = cur_r + direc_r[i]
                        cc = cur_c + direc_c[i]
                        
                        if rr >= 0 and rr < len_r and cc >= 0 and cc < len_c and grid[cc][rr] != 1 and maps[cc][rr].isdigit():
                            bfs.append([rr,cc])
                            grid[cc][rr] = 1

                if food_cnt:   
                    result.append(food_cnt)

    result.sort()
    return result if result else [-1]

maps= ["X591X","X1X5X","X231X", "1XXX1"]
maps = ["XXX","XXX","XXX"]
print(solution(maps))


