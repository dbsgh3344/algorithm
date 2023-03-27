import sys
sys.stdin = open('./AtCoder/Beginners_Selection/Shift_Only/inputs.txt')
n= int(input())
l = list(map(int,input().split()))
cnt=0
idx= 0
while True:
    cur_idx= idx%n
    if l[cur_idx]%2!=0:
        print(cnt)
        break
    else:
        l[cur_idx] = int(l[cur_idx]/2)
    
    if idx!=0 and cur_idx==n-1:
        cnt+=1
    idx+=1

        

