import datetime
from collections import deque

# 현재 시간을 계산 안하고 다음 과제의 시간을 그대로 갖다 써서 오류
def solution_runtimeerr(plans) :
    plans = deque(sorted(plans, key=lambda x: x[1]))
    n,t,r = plans.popleft()
    ans = []
    waiting =[]
    while plans :
        t = list(map(int,t.split(':')))
        t = t[0]*60 + t[1]
        r = int(r)
        
        next_dt = list(map(int,plans[0][1].split(':')))
        next_dt = next_dt[0]*60 + next_dt[1]
        remain_t = r - (next_dt - t)

        if remain_t > 0 :
            waiting.append([n,plans[0][1],remain_t])
            n,t,r = plans.popleft()
        elif remain_t < 0 :
            ans.append(n)
            if waiting :
                n,t,r = waiting.pop()
        else :
            ans.append(n)
            n,t,r = plans.popleft()

        if not plans :
            ans.append(n)
            break

    while waiting :
        ans.append(waiting.pop()[0])
    
    return ans


def solution(plans) :
    plans = deque(sorted(plans, key=lambda x: x[1]))
    n,t,r = plans.popleft()
    t = list(map(int,t.split(':')))
    cur_t = t[0]*60 + t[1]
    ans = []
    waiting =[]
    while plans :
        r = int(r)
        next_dt = list(map(int,plans[0][1].split(':')))
        next_dt = next_dt[0]*60 + next_dt[1]
        remain_t = cur_t + r - next_dt  # 현재시간 + 현재 과제 해결 시간 - 다음 과제 시간

        if remain_t > 0 :   # 양수일 경우 다음 과제 전까지 해결 x
            cur_t = next_dt
            waiting.append([n,remain_t])
            n,_,r = plans.popleft()
        elif remain_t < 0 : # 음수 일 경우 다음 과제 전까지 해결가능하며 시간 남음
            ans.append(n)
            if waiting :    # 밀린 과제가 있을 경우 밀린 과제 get
                cur_t += r
                n,r = waiting.pop()
            else :  # 밀린 과제가 없을 경우, 현재 시간을 다음 과제의 시간으로 바꾸고 다음 과제를 get 
                cur_t = next_dt
                n,_,r = plans.popleft()
        else :  # 0일 경우 현재 과제 해결한 시간이 다음 과제시작 시간과 동일
            cur_t += r
            ans.append(n)
            n,_,r = plans.popleft()

        if not plans :
            ans.append(n)
            break


    while waiting :
        ans.append(waiting.pop()[0])
    
    return ans



p = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
# p = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
print(solution(p))
