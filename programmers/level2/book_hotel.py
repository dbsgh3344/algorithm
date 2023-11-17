from collections import deque
from datetime import datetime,timedelta
import time


def solution(book_time) :
    st= time.time()
    book_time= deque(sorted(book_time,key=lambda x: x[0]))
    ed_list = []
    room = 1
    ed_time = datetime.strptime(book_time.popleft()[1],"%H:%M") + timedelta(minutes=10)
    ed_list.append(ed_time)

    while book_time :
        st_time,ed_time = book_time.popleft()
        st_time = datetime.strptime(st_time,"%H:%M")
        ed_time = datetime.strptime(ed_time,"%H:%M") + timedelta(minutes=10)
        if st_time < ed_list[-1] :
            room+=1    
        else :
            ed_list.pop()
        
        ed_list.append(ed_time)
        ed_list = sorted(ed_list,reverse=True)
    
    print(time.time()- st)
    return room

# 다른 사람 풀이
def solution(book_time):
    st = time.time()
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        # for i in range(start_minutes, end_minutes):
        #     time_table[i] += 1
    
        time_table[start_minutes] +=1
        time_table[end_minutes] -=1
    cnt = 0
    for i in range(len(time_table)) :
        cnt += time_table[i]
        time_table[i] = cnt
        

    # print(time.time() - st)
    
    return max(time_table)

            
book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
# book_time = [["10:20", "12:30"], ["10:20", "23:59"], ["10:20", "12:30"]]
print(solution(book_time))



