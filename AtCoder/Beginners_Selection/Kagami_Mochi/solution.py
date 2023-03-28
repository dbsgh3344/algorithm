import sys
sys.stdin = open('./AtCoder/Beginners_Selection/Kagami_Mochi/inputs.txt')

n= int(input())
ds = sorted([int(input()) for _ in range(n)])
max_d= ds.pop()
cnt=1
while ds:
    cur_d= ds.pop()
    if max_d>cur_d:
        cnt+=1
        max_d= cur_d

print(cnt)
    
        
    
    
