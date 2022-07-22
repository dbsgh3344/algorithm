import sys
# sys.stdin=open('inputs.txt','r')

# n= int(input())
n= int(sys.stdin.readline())
nge= list(map(int, sys.stdin.readline().strip().split()))

ans= ['-1']*n
tmp =0
stack = [0]
i=1
for i in range(1,n) :

    while len(stack)>0 and nge[stack[-1]] < nge[i] :
        ans[stack.pop()] = str(nge[i])
            
    stack.append(i)

print(' '.join(ans))
# print(ans)
            