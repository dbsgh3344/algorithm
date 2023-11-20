
def solution(targets) :
    
    targets= sorted(targets,key=lambda x: x[1])
    result = 0
    e = 0
    print(targets)
    for target in targets :
        if target[0] >= e :
            result+=1
            e = target[1]
    
    return result
            

    
    


t =[[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
solution(t)



