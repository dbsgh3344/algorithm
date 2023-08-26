from collections import deque

def solution(players, callings):
    
    p_map = {c:idx+1 for idx,c in enumerate(players) }
    r_map = {idx+1:c for idx,c in enumerate(players) }
    
    for call in callings :
        p_map[call] -= 1
        tmp = r_map[p_map[call]] 
        p_map[tmp] +=1
        r_map[p_map[call]] = call
        r_map[p_map[call]+1] = tmp
    
    

    
    return list(r_map.values())



p = ["mumu", "soe", "poe", "kai", "mine"]
c= ["kai", "kai", "mine", "mine"]
print(solution(p,c))