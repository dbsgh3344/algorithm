from itertools import combinations,permutations
def solution(k,d) :
    limit = 1000001
    result = []
    for a in range(limit) :
        
        if a*k > d :
            break
        for b in range(limit) :
            t = ((a*k)**2+(b*k)**2)**(1/2)
            if t > d :
                break
            else :
                result.append(t)

def solution2(k,d) :

    lists= []
    for i in range(d+1) :    
        if i*k > d:
            break
        
        lists.append(i*k)

    result = 0
    for iter in lists :
        maxky = (d**2 - iter**2)**(1/2)  # k*y = sqrt(d^2 - (k*x)^2)
        y = int(maxky/k)+1
        cnt = len(range(y))
        result+=cnt
        
    return result
    
# 다른 사람 풀이
def solution(k, d):
    c = 0
    for y in range(0, d, k):
        x = (d**2 - y**2)**0.5
        c += x//k
    return c + d//k + 1
    
    

k,d = 1,5
print(solution2(k,d))
