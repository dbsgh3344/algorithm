
def solution1(boards, moves) :
    basket = []
    cnt = 0

    for move in moves :
        while(boards[move-1]):
            catch_doll =boards[move-1].pop()
            if catch_doll!=0:
                break
                              
        if catch_doll!=0:
            basket.append(catch_doll)

        if len(basket)>1 and (basket[-2] == basket[-1]) :
            basket.pop()
            basket.pop()
            cnt+=2
        catch_doll=0

    return cnt





if __name__== '__main__' :
    b= [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    m = [1,5,3,5,1,2,1,4]
    a= solution1(b,m)
    print(a)
