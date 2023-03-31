import sys
sys.stdin = open('./AtCoder/Beginners_Selection/Traveling/inputs.txt')
from collections import deque

# n= int(input())
# t = [list(map(int,input().split())) for _ in range(n)]
# bfs =deque()
# bfs.append((0,0,0))
# xx= [1,0,-1,0]
# yy=[0,1,0,-1]
# ans= 'Yes'

# bfs풀이 시간초과
# for des_t,des_x,des_y in t:
#     while bfs:
#         cur_t,cur_x,cur_y = bfs.popleft()

#         if cur_t==des_t and cur_x==des_x and cur_y==des_y:
#             break

#         if cur_t>des_t:
#             ans='No'
#             break

#         for i in range(4):
#             ax= xx[i]+cur_x
#             ay= yy[i]+cur_y
#             if ax>=0 and ay>=0 and (ax!=0 or ay!=0):    
#                 tmp=(cur_t+1,ax,ay)
#                 bfs.append(tmp)
        

#     if ans=='No':
#         break

# print(ans)
# --------------------------------------

# 초기값 = x+y 에서 시작했을 때, t번째에 x,y에 도달할 수 있는 값은 (x+y)에서 2씩 증가한 값이다.
# ex) x+y =3 , 3,5,7,9,11..
# t = (x+y) + (2*i)
n= int(input())
t = [list(map(int,input().split())) for _ in range(n)]
ans= 'Yes'
for idx,(des_t,des_x,des_y) in enumerate(t):
    if idx==0:
        st = (des_t-(des_x+des_y))
    else :
        b_t,b_x,b_y =t[idx-1]
        cur_t,cur_x,cur_y= des_t-b_t,abs(des_x-b_x),abs(des_y-b_y)
        st= (cur_t -(cur_x+cur_y))

    if st<0 or st%2!=0:
        ans='No'
        break

print(ans)

# n이 주어졌을 때, n번째는 n-1번째의 시간과 위치에서부터 시작한다. n=0이면 (0,0)
