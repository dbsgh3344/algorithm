
# 반례 찾기 위주의 풀이.
def solution(board):    
    xx = [0,1,1,1,0,-1,-1,-1]
    yy = [-1,-1,0,1,1,1,0,-1]
    dicts = {'O':0,'X':0}
    win_dict = {'O':0,'X':0}

    for r in range(3) :
        for c in range(3) :
            for ox in ['O','X'] :
                if board[r][c] == ox :
                    dicts[ox] += 1

                    for i in range(8) :
                        nc = c + xx[i]
                        nr = r + yy[i]
                        cnt = 0

                        for _ in range(2) :
                            if nc <= 2 and nc >= 0 and nr <= 2 and nr >= 0 and board[nr][nc] == ox :
                                nc += xx[i]
                                nr += yy[i]
                                cnt += 1
                            else :
                                break
                        
                        if cnt == 2 :
                            win_dict[ox] += 1

    if dicts['O'] < dicts['X'] or dicts['O'] - 1 > dicts['X'] : return 0
    if win_dict['O'] > 0 and win_dict['X'] > 0 : return 0
    if win_dict['O'] > win_dict['X'] and dicts['O'] - 1 != dicts['X'] : return 0
    if win_dict['O'] < win_dict['X'] and dicts['O'] != dicts['X'] : return 0
        
    return 1
            

# board = ["OOO", "...", "XXX"]
# board = ["O.X", ".O.", "..X"]
# board = ["...", "...", "..."]
# board = ["...", ".X.", "..."]
board = ['OXO','XOX','OXO']
print(solution(board))