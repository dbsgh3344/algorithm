import sys
sys.stdin = open('./AtCoder/Beginners_Selection/Otoshidama/inputs.txt')
N,Y = map(int,input().split())
ans='-1 -1 -1'
for i in range(N+1) :
    for j in range(N-i+1):
        k=N-i-j
        cur_yen=10000*i+5000*j+1000*k
        if cur_yen==Y:
            ans =f'{i} {j} {k}'

print(ans)


    
    

