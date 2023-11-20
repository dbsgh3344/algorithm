from collections import deque
import time

def solution(numbers) :
    result = [-1]*len(numbers)
    stack = []
    numbers = deque(numbers)
    idx= 0
    stack.append((numbers.popleft(),0))
    t = time.time()
    while numbers :
        current_num = numbers.popleft()
        idx += 1        
        while len(stack) and current_num > stack[-1][0]:
            before_num = stack.pop()
            result[before_num[1]] = current_num
             
        stack.append((current_num,idx))
        
    print(time.time() - t)
    return result

def solution(numbers) :
    result = [-1]*len(numbers)
    stack = []
    for i in range(len(numbers)) :
        current_num = numbers[i]

        while stack and numbers[stack[-1]] < current_num :
            result[stack.pop()] = current_num

        stack.append(i)
            
    return result

a= [2, 3, 3, 5]
# a= [9, 1, 5, 3, 6, 2,23,4,34,5,65,66,7,78,89,0,9809,90]
a= [9,1,5,3,6]
print(solution(a))