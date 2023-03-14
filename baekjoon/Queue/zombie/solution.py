import sys
from collections import deque
l = int(sys.stdin.readline())   # input() 함수로는 시간초과걸림 
ml,mk = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())
# zombie_q = deque([int(sys.stdin.readline()) for _ in range(l)])
idx_q= deque([i+1 for i in range(ml)])
c_term = 0
used_c = 0
ans= 'YES'
for _ in range(l) :
    z_hp = int(sys.stdin.readline())
    idx=idx_q.popleft()
    if c_term!=0:
        idx-=used_c
        c_term-=1
    else :
        used_c=0

    damaged = z_hp-(idx*mk)    
    if damaged>0 :
        if c!=0:
            c-=1
            c_term=ml-1
            used_c+=1
            if used_c>ml:
                used_c=ml
        else:
            ans='NO'
            break
    
    damage_idx= len(idx_q)+1
    idx_q.append(damage_idx)
    
print(ans)