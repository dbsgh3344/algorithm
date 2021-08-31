import sys
sys.stdin = open('jongmanbook/input.txt')

c = int(input())

for _ in range(c) :
    n,l = map(int,input().split())
    cost = list(map(int,input().split()))
    showcnt = l

    tmp= 123124234
    while (showcnt <= n) :    
        for i in range((n)-showcnt+1) :
            costSum= sum(cost[i:i+showcnt])/showcnt
            
            if tmp > costSum :
                tmp = costSum
        
        showcnt+=1

    print(tmp)

