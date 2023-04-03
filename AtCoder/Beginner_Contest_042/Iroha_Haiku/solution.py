import sys
sys.stdin = open('./AtCoder/Beginner_Contest_042/Iroha_Haiku/inputs.txt')
from collections import Counter
a = list(map(int,input().split()))
b= Counter(a)
if 5 in b and b[5]==2 and 7 in b and b[7]==1:
    print('YES')
else :
    print('NO')
