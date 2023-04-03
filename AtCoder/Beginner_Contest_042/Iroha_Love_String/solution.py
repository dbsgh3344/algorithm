import sys
sys.stdin = open('./AtCoder/Beginner_Contest_042/Iroha_Love_String/inputs.txt')

n,l = map(int,input().split())
s= sorted([input() for _ in range(n)])
print(''.join(s))
