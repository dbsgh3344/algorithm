import sys
sys.stdin = open('./AtCoder/Beginner_Contest_296/Simultaneous_Swap/inputs.txt')
# from collections import Counter
from itertools import permutations
from copy import deepcopy

n = int(input())
a= list(map(int,input().split()))
b= list(map(int,input().split()))

def solution_timelimit(n,a,b):
    a_list =[]
    b_list =[]
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            c = deepcopy(a)
            tmp = c[i]
            c[i] = c[j]
            c[j] = tmp
            a_list.append((c,i))

        for j in range(i+1,len(b)) :
            c= deepcopy(b)
            tmp = c[i]
            c[i] = c[j]
            c[j] = tmp
            b_list.append((c,i))

    ans = 'No'
    for i in a_list :
        if i in b_list :
            ans ='Yes'

    print(ans)


a= [100,3,2,1,50]
print(set(a))
    

        

