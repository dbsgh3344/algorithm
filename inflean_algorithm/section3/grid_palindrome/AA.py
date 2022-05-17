import sys
# sys.stdin = open('inputs.txt','r')

arr = [list(map(int,input().split())) for _ in range(7)]
cnt =0
for i in range(7) :
    for j in range(7-5+1) :
        # rowlist = [0]*10
        # collist =[0]*10
        tmprow = arr[i][j:j+5]
        if tmprow==tmprow[::-1] :
            cnt+=1

        # tmpcol = [arr[iter][i] for iter in range(j,j+5)]

        for k in range(2) :
            if arr[j+k][i] != arr[j+4-k][i] :
                break
        else :
            cnt+=1

        # rowstack = 0
        # colstack = 0
        # for iter in range(2) :
        #     if tmprow[iter] == tmprow[4-iter] :
        #         rowstack +=1

        #     if tmpcol[iter] == tmpcol[4-iter] :
        #         colstack +=1

        # if rowstack==2:
        #     cnt+=1
        # if colstack==2 :
        #     cnt+=1            

print(cnt)
            

