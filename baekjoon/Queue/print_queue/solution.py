import sys
from collections import deque
# sys.stdin = open('inputs.txt','r')

testcaseIter =int(input())

for _ in range(testcaseIter) :
    n,m = map(int,input().split())
    arr= list(map(int,input().split()))
    importance = deque([(impo,idx) for idx,impo in enumerate(arr)])
    cnt=0 
    while True :
        cur_val = importance.popleft()
        if len(importance)==0 or cur_val[0] >= max(list(map(lambda x: x[0], importance))):
            cnt+=1
            if cur_val[1]==m :
                break
        else :
            importance.append(cur_val)
        
    print(cnt)            
        
