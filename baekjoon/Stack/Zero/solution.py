import sys
sys.stdin= open('inputs.txt','r')
k = int(input())
digits = [int(input()) for _ in range(k)]
stacks=[]
for i in range(len(digits)) :
    if digits[i]==0:stacks.pop()
    else :stacks.append(digits[i])
print(sum(stacks))