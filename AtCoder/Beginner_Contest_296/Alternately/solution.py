import sys
sys.stdin = open('./AtCoder/Beginner_Contest_296/Alternately/inputs.txt')
from collections import deque

def stack_solution():
    n=int(input())
    s= deque(input())
    stack=[]
    stack.append(s.popleft())
    ans ='Yes'
    while s:
        cur_c= s.popleft()
        if stack.pop()!= cur_c:
            stack.append(cur_c)
        else :
            ans='No'
            break

    return ans
    

print(stack_solution())


    