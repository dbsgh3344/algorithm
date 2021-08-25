from collections import deque

def solution1(boards, moves) :
    basket = []
    moves = deque(moves)
    cnt = 0

    while(moves) :
        cur_doll =0
        for i in range(len(boards)) :        
            if boards[i][moves[0]-1] !=0 :                                
                cur_doll=boards[i][moves[0]-1]
                boards[i][moves[0]-1] = 0                     
                break
        

        moves.popleft()
            
        if (len(basket)>=1) and (basket[-1]==cur_doll):
            basket.pop()
            cnt+=2
        else :
            if(cur_doll!=0) :
                basket.append(cur_doll)
        
                
    return cnt



if __name__== '__main__' :
    b= [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]
    m = [1,5,3,5,1,2,1,4]
    a= solution1(b,m)
    print(a)
