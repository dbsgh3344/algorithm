import sys
sys.stdin=open('inputs.txt','r')

arr= input()
m = int(input())
# orders= [ for _ in range(m)]

cursor = len(arr)
for i in range(m):
    order = input()
    if order =='L':
        cursor -=1
    elif order =='D':
        cursor+=1
    elif 'P' in order:
        
    