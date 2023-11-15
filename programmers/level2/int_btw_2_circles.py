


def solution(r1,r2) :
    cnt = 0
    for i in range(r2+1) :        
        for j in range(r2+1) :
            r = (i**2 + j**2)**0.5
            if r >= r1 and r <= r2 :
                cnt+=1
                # print(i,j)
                
    cnt*=4
    cnt-=8 
    
    return cnt
    



r1,r2 = 2,3
print(solution(r1,r2))