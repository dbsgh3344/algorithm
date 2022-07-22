### 시간초과 unsolved
import sys
sys.stdin = open('inputs.txt','r')

# n= int(input())
n= int(sys.stdin.readline().strip())
strs = sys.stdin.readline().strip()
idx= 2
hashdicts = {}
while idx!=(len(strs)//2)+1:
    for i in range(len(strs)-idx+1):
        
        tmp=strs[i:i+idx]
        if tmp in hashdicts.keys():
            hashdicts[tmp]+=1
        else:
            hashdicts[tmp]=1
    idx+=1

# print(hashdicts)
ans =0
for k,v in hashdicts.items():
    if v>=2:
        if ans <len(k):
            ans= len(k)

print(ans)

        