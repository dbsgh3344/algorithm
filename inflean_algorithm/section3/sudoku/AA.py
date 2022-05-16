import sys
sys.stdin = open('inputs.txt','r')

arr = [list(map(int, input().split())) for _ in range(9)]
for i in range(9) : 
    rowlist =[0]*10
    collist =[0]*10
    rectlist =[0]*10
    for j in range(9) :
        rowlist[arr[i][j]]=1
        collist[arr[j][i]]=1

        r= (j//3) + ((i//3)*3)
        c= (j%3) + ((i%3)*3)
        rectlist[arr[r][c]]=1

    if sum(rowlist)!= 9 or sum(collist)!=9 or sum(rectlist)!=9 :
        print('NO') 
        sys.exit()

print('YES')
    
    