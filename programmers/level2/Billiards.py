# 기울기를 통한 거리 구하기 실패. 다시 체크해볼 것
def calc_distance_eq_y(table_len,st_x,st_y,ed_x) :
    w = (table_len - st_y)/((ed_x-st_x)/2)
    b = st_y - w * st_x
    coord_var = w*ed_x+b
    val = (ed_x - st_x)**2 +  (st_y - coord_var)**2
    return val

def calc_distance_eq_x(table_len,st_x,st_y,ed_y) :
    w = ((st_y-ed_y)/2)/(st_x-table_len)
    b= st_y - w * st_x
    coord_var = (ed_y - b)/w
    val = (coord_var-st_x)**2+(st_y-ed_y)**2
    return val
    

def solution(m, n, startX, startY, balls) :
    anslist = []
    for i in balls :
        ex,ey = i
        sx,sy = startX,startY

        if sy == ey :
            # sd1 = calc_distance_eq_y(n,sx,sy,ex)            
            # sd2 = calc_distance_eq_y(0,sx,sy,ex)
            sd1 = (sx - ex)**2 + ((n - sy)*2)**2
            sd2 = (sx - ex)**2 + ((sy)*2)**2
            sd3 = ((0- sx) + (0 - ex))**2 if sx < ex else ((m - sx) + (m - ex))**2
            ans = min(sd1,sd2,sd3)
        
        elif sx == ex :            
            # sd1 = calc_distance_eq_x(0,sx,sy,ey)
            # sd2 = calc_distance_eq_x(m,sx,sy,ey)
            sd1 = (sx*2)**2 + (sy-ey)**2
            sd2 = ((m-sx)*2)**2 + (sy-ey)**2
            sd3 = ((0 - sy) + (0 - ey))**2 if sy < ey else ((n - sy) + (n - ey))**2
            ans = min(sd1,sd2,sd3)

        else :            
            sd1 = (sx-ex)**2 + ((n - sy) + (n - ey))**2
            sd2 = ((m - sx) + (m - ex))**2 + (sy - ey)**2
            sd3 = (sx-ex)**2 + (sy + ey)**2
            sd4 = (sx + ex)**2 + (sy - ey)**2
            ans = min(sd1,sd2,sd3,sd4)
        
        anslist.append(ans)

    return anslist


m=10
n=10
stx= 3
sty= 7
balls =[[7,7], [2, 7], [7, 3]]
print(solution(m,n,stx,sty,balls))