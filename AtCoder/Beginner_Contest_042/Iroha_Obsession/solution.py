import sys
sys.stdin = open('./AtCoder/Beginner_Contest_042/Iroha_Obsession/inputs.txt')

# x= [i for i in range(10) if i not in a]
# tmp_n = n
# nod= 10
# i=0
# ans= 0

def check_digit(n,nod,i):
    ans= []
    # for d in x:
    #     digit = 
    
    return ans

def solution():
    n,k = map(int,input().split())
    a= list(map(int,input().split()))
    # cur_n = n
    while chk :
        chk =True
        str_n = str(n)[::-1]
        
        for i in range(len(str_n)):
            for d in a:
                if str_n[i] in a:
                    n+=1
                    chk=False
                    break
                
        
    
    print(n)

# solution()



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
