from collections import deque

def solution(board) :
    
    bfs = deque()
    for i in range(len(board)) :
        if 'R' in board[i] :
            bfs.append((board[i].find('R')),i)
            break
    
    print(bfs)
    xx = [0,1,0,-1]
    yy = [-1,0,1,0]

    cur = 'R'
    while bfs :
        cur_x,cur_y = bfs.popleft()

        if cur=='R' or cur =='D' :
            for i in range(4) :
                x = cur_x + xx[i]
                y = cur_y + yy[i]
            
        else :
            



            # if x > 0 and x < len(board[0]) and y > 0 and y < len(board) :
            #     if board[y][x]



b = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
solution(b)