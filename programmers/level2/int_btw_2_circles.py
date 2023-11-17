import math
from math import sqrt
def solution(r1,r2) :
    cnt = 0

    for x in range(r2+1) :
        r2y = (r2**2-x**2)**0.5
        if x > r1 :
            r1y = 0
        else :
            r1y = (r1**2-x**2)**0.5 

        r2_p = math.floor(float(r2y))
        r1_p = math.ceil(float(r1y))
        
        print(x,r2_p,r1_p)

        a = r2_p - r1_p + 1
        cnt+=a

    
    return (cnt-(r2-r1+1))*4
    

# 다른 사람 풀이
def solution(r1, r2):
    quar = 0
    for i in range(0, r1):
        quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        quar += int(sqrt(r2**2 - i**2))
    return quar * 4


r1,r2 = 2,3
print(solution(r1,r2))