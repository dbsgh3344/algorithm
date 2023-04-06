import sys
sys.stdin = open('./AtCoder/Beginner_Contest_042/Iroha_Grid/inputs.txt')

h,w,a,b = map(int,input().split())

mod = 10**9 +7
f = [1]*(2*10**5+1)
t = [1]*(2*10**5+1)
for i in range(1,2*10**5+1):
    f[i]=(f[i-1]*i)%mod
    t[i] =(t[i-1]*pow(i,-1,mod))%mod

print(t[:10])
# print(pow(2,-1,10000))
print(0.5%mod)