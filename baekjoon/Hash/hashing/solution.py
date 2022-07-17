import sys
# sys.stdin = open('inputs.txt','r')
m= 1234567891
r= 31
l = int(input())
ans=0
for idx,alpha in enumerate(input()):
    ans+= (ord(alpha)-96)*r**idx
print(ans%m)

# sys.stdin.readline() 안됨

