
# 시간초과
def solution_timeover(s,k):
    ans=[0,10e9]
    for i in range(len(s)):        
        idx=[]
        idx.append(i)
        res = s[i]
        j = i
        while True :
            if res == k:
                idx.append(j)
                break
            elif res > k or j==len(s)-1:
                idx.pop()
                break

            j += 1
            res += s[j]

        if len(idx)==2:
            if idx[-1]-idx[0] < ans[1]-ans[0]:
                ans= idx

    return ans

# 다른사람 풀이 참조
# sum(s[st:end])식의 계산은 시간이 초과하니 그때그때 변수에 더하고 뺄 것
def solution(s,k):
    ans = [0,10e9]
    # ans =[]
    # max_index= s.index(k) + 1 if k in s else len(s)
    r = 0
    l = 0
    # if max(s) == k:
    #     tmp = s.index(max(s))
    #     return [tmp,tmp]

    seq_sum = s[l]
    while True :
        if r == len(s) - 1 :
            if seq_sum < k:
                break
                

        if seq_sum < k :
            r += 1
            seq_sum += s[r]
        elif seq_sum > k :
            seq_sum -= s[l]
            l += 1
        
        
        if seq_sum == k :
            if (r) - l < ans[1] - ans[0] :
                ans = [l, r]
            seq_sum -= s[l]
            l += 1
    
    return ans
            

# s= [1, 2, 3, 4, 5]
s= [1, 1, 1, 2, 3, 4, 5]
# s= [2, 2, 2, 2, 2]
k = 5

print(solution(s,k))
