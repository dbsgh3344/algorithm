import sys
from collections import deque
# sys.stdin = open('inputs.txt','r')


list1_len = int(input())
list1 = deque(map(int, input().split()))
list2_len = int(input())
list2 = deque(map(int,input().split()))

answer = []
while len(list1)!=0 and len(list2)!=0 :
    if list1[0] > list2[0] :
        answer.append(list2.popleft())
    else :
        answer.append(list1.popleft())
    
    if len(list1)==0:
        answer+=list2
        list2= []
    elif len(list2)==0 :
        answer+=list1
        list1 = []
  
mergelist = list(map(str,sorted(answer)))

print(' '.join(mergelist))
    
        
    