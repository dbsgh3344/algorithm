import sys
# sys.stdin = open('inputs.txt','r')

card = list(range(1,21))

for i in range(10) :
    a,b = map(int,input().split())
    a,b = a-1,b-1
    iter = b-a+1

    for j in range(iter//2):
        front =card[a+j]
        end = card[b-j]
        card[a+j] = end
        card[b-j] = front

print(' '.join(list(map(str,card))))        