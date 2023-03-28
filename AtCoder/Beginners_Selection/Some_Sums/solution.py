import sys
sys.stdin = open('./AtCoder/Beginners_Selection/Some_Sums/inputs.txt')
n,a,b = map(int,input().split())

ans=0
for i in range(n+1):
    s= str(i)
    lists=list(map(int,s))
    sums = sum(lists)
    
    if a <= sums and sums <=b:
        ans+=int(s)

print(ans)