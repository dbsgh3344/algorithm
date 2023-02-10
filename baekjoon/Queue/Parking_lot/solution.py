import sys 
from collections import deque

sys.stdin = open('/home/song/code/algo/algorithm/baekjoon/Queue/Parking_lot/inputs.txt','r')
n,m = map(int,input().split())
parking_fee = [int(input()) for _ in range(n)]
car_w = [int(input()) for _ in range(m)]

empty_lot =[0]*n
waiting = deque([])
ans=0

for i in range(len(car_w)*2) :
    q= int(input())
    if q>0:
        try:
            idx=empty_lot.index(0)
            empty_lot[idx] = q
        except:
            waiting.append(q)
        
    else :
        idx= empty_lot.index(abs(q))
        empty_lot[idx]=0
        ans+=car_w[abs(q)-1]*parking_fee[idx]
        if len(waiting)>0:
            w_car=waiting.popleft()
            idx=empty_lot.index(0)
            empty_lot[idx] = w_car

print(ans)      
            

            

# 다른사람 풀이
# import sys
# from collections import deque

# N, M = map(int, input().split())

# stops = [False] * N
# stops_expense = []
# cars_expense = []
# cars_dict = {}
# for _ in range(N):
#     stop = int(sys.stdin.readline().rstrip())
#     stops_expense.append(stop)

# for _ in range(M):
#     car = int(sys.stdin.readline().rstrip())
#     cars_expense.append(car)

# tmp_stops = deque()
# for _ in range(2*M):
#     step = int(sys.stdin.readline().rstrip())
#     if step-1 >= 0:
#         for idx in range(N):
#             if stops[idx] is False:
#                 stops[idx] = True
#                 cars_dict[step-1] = idx
#                 break
#             elif idx == N-1 and stops[idx] is True:
#                 tmp_stops.append(step-1)

#     else:
#         if len(tmp_stops) == 0:
#             stops[cars_dict[-1 * step-1]] = False
#         else:

#             stops[cars_dict[-1 * step - 1]] = False
#             stops[cars_dict[-1 * step - 1]] = True
#             tmp_stop = tmp_stops.popleft()
#             cars_dict[tmp_stop] = cars_dict[-step - 1]

# answer = 0

# for key, val in cars_dict.items():
#     answer += cars_expense[key] * stops_expense[val]

# print(answer)    

    
    
