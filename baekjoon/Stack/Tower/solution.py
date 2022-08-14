import sys

# sys.stdin = open('inputs.txt')
n= int(sys.stdin.readline())
tower = list(map(int,sys.stdin.readline().split()))
stack =[]
cnt=[0]*len(tower)
while len(tower)!=0:
    idx= len(tower)-1
    stack.append((tower.pop(),idx))
    if len(tower)==0:break
    
    while len(stack)>0:    
        if stack[-1][0] < tower[-1]:    
            _,idx = stack.pop()
            cnt[idx]= str(len(tower))
        else :
            break
    
        
if len(stack)>0:
    for _,idx in stack :
        cnt[idx] = str(0)

print(' '.join(cnt))
