from collections import deque
def solution(r1,r2) :
    cnt = 0
    
    lists= []
    for x in range(r2+1) :
        y = (r2**2-x**2)**0.5
        for i in range(int(y//1)+1) :
            lists.append((x,i))
    

    lists2= deque()
    for x in range(r1+1) :
        y = (r1**2 - x**2)**0.5
        # print(x,y)
        for i in range(int(y//1)+1) :
            lists2.append((x,i))

    while lists2 :
        a= lists2.popleft() 
        if a in lists :
            lists.remove(a)
        else :
            lists2.append(a)
        

    print(lists)
    # cnt+=8 
    
    return len(lists)
    

r1,r2 = 2,5
print(solution(r1,r2))