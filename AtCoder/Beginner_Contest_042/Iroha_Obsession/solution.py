import sys
sys.stdin = open('./AtCoder/Beginner_Contest_042/Iroha_Obsession/inputs.txt')

def check_ans(a,n):
    while n :
        if n%10 in a:
            return False
        
        n//=10
    return True

def other_solution():
    n,k = map(int,input().split())
    a= list(map(int,input().split()))
    
    tmp =100000
    for i in range(n,tmp):
        if check_ans(a,i):
            print(i)
            return
    
    
other_solution()
