import sys
# sys.stdin = open('inputs.txt','r')
strs = input()

digitList= list(filter(lambda x : x.isdigit() ,strs))
digits = int(''.join(digitList))
print(digits)
cnt = 1
for i in range(1,digits//2 +1) :
    if digits%i ==0 :
        cnt+=1

print(cnt)


