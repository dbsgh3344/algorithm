import sys
# sys.stdin=open('inputs.txt','r')

arr= input()

stack=[]
cnt=0
for i in range(len(arr)):
    if arr[i]=='(':
        stack.append(arr[i])
    else:
        if stack[-1]=='(':
            if arr[i-1]==')' :
                cnt+=1
                stack.pop()
            else :
                stack.pop()
                cnt+=len(stack)
        
print(cnt)
                
        