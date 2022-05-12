import sys
# sys.stdin = open('inputs.txt','r')

n= int(input())
# grid = []
max_row = 0
collist = [0]*n
right_diagonal =0
left_diagonal =0
for i in range(n) :
    row = list(map(int,input().split()))
    for j in range(len(row)):
        collist[j] +=row[j]
    right_diagonal+=row[i]
    left_diagonal+=row[n-i-1]
    
    if max_row < sum(row) :
        max_row = sum(row)
    # grid.append(row)

a= max(max(collist),right_diagonal,left_diagonal,max_row)
print(a)