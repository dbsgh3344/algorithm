from collections import deque,Counter

def solution(picks,minerals) :
    iron_dict = {'diamond':5,'iron':1,'stone':1}
    stone_dict = {'diamond':25,'iron':5,'stone':1}

    minerals = deque(minerals)
    lists = []
    for _ in range(sum(picks)) :
        tmp = Counter([minerals.popleft() for _ in range(5) if minerals])
        lists.append(tmp)
    lists = sorted(lists , key=lambda x: (x['diamond'],x['iron'],x['stone'])) # 다중 조건 sort
    ans =0
    while lists :
        d = lists.pop()
        if picks[0] :
            picks[0] -= 1
            ans += sum(d.values())
        elif picks[1] :
            picks[1] -= 1
            ans += sum([iron_dict[k]*v for k,v in d.items()])
        elif picks[2] :
            picks[2] -= 1
            ans += sum([stone_dict[k]*v for k,v in d.items()])

    return ans


p = [0,1,1]
# p = [1,3,2]
# m = ["iron", "iron", "diamond", "iron", "stone", "diamond", "diamond", "diamond","iron","iron","diamond","diamond"]
# m = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
m = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(p,m))