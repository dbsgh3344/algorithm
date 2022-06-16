import sys
from collections import deque
sys.stdin = open('inputs.txt','r')

n= int(input())
arr= list(map(int,input().split()))
arr= arr[::-1]
lists = []

for idx,num in enumerate(arr) :
    idx= len(arr)-idx
    lists.insert(num,str(idx))

print(' '.join(lists))





 