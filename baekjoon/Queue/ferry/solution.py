import sys
sys.stdin = open('./inputs.txt')
from collections import deque

# 실패
# 하나의 큐에서 빼서 쓰면 좌,우측에 도착했을 때 태워야하는 승객을 못태운다.
# 큐를 left,right로 나눠서 관리해야함
def solution1():
    m,t,n = map(int,sys.stdin.readline().split())
    q= sorted([tuple(sys.stdin.readline().split()) for _ in range(n)],key= lambda x: int(x[0]),reverse=True)
    ferry = deque()
    total_t = 0
    ferry_loc = 'left'
    ans = []
    cur_t= int(q[-1][0])
    cur_loc =q[-1][1]
    while (q) :
        while total_t >= cur_t and ferry_loc==cur_loc and len(ferry)<m:
            ferry.append(total_t+t)
            q.pop()
            if not q:
                break
            cur_t= int(q[-1][0])
            cur_loc =q[-1][1]
            
        if len(ferry)>0:
            total_t+=t
            ferry_loc = 'right' if ferry_loc=='left' else 'left'
            ans+=ferry
            ferry=[]
        
        if total_t< cur_t:
            total_t=cur_t

        elif ferry_loc!=cur_loc:
            total_t+=t
            ferry_loc = 'right' if ferry_loc=='left' else 'left'


    print(*ans,sep='\n')

def solution2():
    m,t,n = map(int,sys.stdin.readline().split())
    q= [[i]+list(sys.stdin.readline().split()) for i in range(n)]
    total_t = 0
    ferry_loc = 0
    left_q= deque()
    right_q= deque()
    loc_q = [left_q,right_q]
    ferry=deque()
    ans = [0]*n
    i=0
    cnt=0

    def set_loc_q(total_t,loc_q,i):
        while i<n and int(q[i][1]) <= total_t:
            cur_loc = 0 if q[i][2]=='left' else 1
            loc_q[cur_loc].append(q[i][0])
            i+=1
        
        return i


    def put_on_ferry(loc_q,cur_loc,ferry):
        while loc_q[cur_loc] and len(ferry) < m:
            ferry.append(loc_q[cur_loc].popleft())

    def get_off_ferry(total_t,cnt,ans,ferry):
        while ferry:
            ans[ferry.popleft()] = total_t
            cnt+=1

        return cnt
        
            
    while cnt<n:
        i = set_loc_q(total_t,loc_q,i)
        put_on_ferry(loc_q,ferry_loc,ferry)

        if len(loc_q[0])==0 and len(loc_q[1])==0 and len(ferry)==0 and i <n :
            total_t = int(q[i][1])
            i = set_loc_q(total_t,loc_q,i)
            put_on_ferry(loc_q,ferry_loc,ferry)


        ferry_loc = 0 if ferry_loc==1 else 1
        total_t+=t

        cnt = get_off_ferry(total_t,cnt,ans,ferry)
        
    print(*ans,sep='\n')


solution1()



# 다른 사람 풀이
# import sys
# from collections import deque

# readl = sys.stdin.readline

# # 최대 m 명, 가는데 t 시간, N 손님.
# m, t, n = map(int, readl().split())
# order = [readl().split() for _ in range(n)]
# order = [[i, int(o[0]), o[1]] for i, o in enumerate(order)]


# # 해당 시간에 한쪽에 와서 있는 사람 전부 큐에 left, right 나눠서 넣음.
# def passanger_At_Stop(totalTime, stop, i):
#     while i < n and order[i][1] <= totalTime:
#         side = (order[i][2] == "right")
#         stop[side].append(order[i][0])
#         i += 1
#     return i

# # 배에 탄다.
# def take_ship(ship, stop, ship_side):
#     while len(ship) < m and stop[ship_side]:
#         ship.append(stop[ship_side].popleft())

# # 배에서 내림.
# def take_off_ship(totalTime, arr, ship, cnt):
#     while ship:
#         arr[ship.popleft()] = totalTime
#         cnt += 1
#     return cnt


# leftq = deque()
# rightq = deque()
# stop = [leftq, rightq]


# ship = deque()

# ship_side = 0 # 왼쪽에서 시작
# totalTime = 0
# i = 0
# cnt = 0

# arr = [0] * n # 해당 index 에 해당하는게 언제 도착하는지 알아야함

# while cnt < n:
#     # 지금 시간에 대해서 태우고
#     i = passanger_At_Stop(totalTime, stop, i)
#     take_ship(ship, stop, ship_side)

#     # 만약 배도 비어있고 양쪽에 기다리는 승객이 없으면
#     # totalTime 을 갱신하고 태움. (움직이지 않고 계속 기다리는걸 표현)
#     if len(ship) == 0 and len(stop[0]) == 0 and len(stop[1]) == 0 and i < n:
#         totalTime = order[i][1]
#         i = passanger_At_Stop(totalTime, stop, i)
#         take_ship(ship, stop, ship_side)

#     # totalTime 갱신.
#     ship_side = 0 if ship_side else 1
#     totalTime += t

#     # 내린다.
#     cnt = take_off_ship(totalTime, arr, ship, cnt)

# print(*arr, sep='\n')