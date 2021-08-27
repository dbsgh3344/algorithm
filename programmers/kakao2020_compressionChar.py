def solution(s) :
    tmp = len(s)
    for i in range(len(s)) :
        answer_chars=''
        iter_chars= s[:1+i]

        cnt=1
        for j in range(1+i,len(s)+1,i+1) :
            if iter_chars == s[j:1+i+j] :
                cnt+=1
            else :
                if cnt>1:
                    answer_chars+= str(cnt)+iter_chars                
                else :
                    answer_chars+=iter_chars
                
                iter_chars= s[j:1+i+j]
                cnt=1
                continue
            
            # if (j>=len(s)-1) :
            #     if cnt>1:
            #         answer_chars+= str(cnt)+iter_chars                
            #     else :
            #         answer_chars+=iter_chars
                
        print(answer_chars)        
        if 0< len(answer_chars) < tmp :
            tmp = len(answer_chars)
    
    return tmp
            
def solution2(s) :


    for i in range(len(s)) :
        iter_chars = s[:i+1]
        
        





if __name__=="__main__":
    s= "aabbaccc"
    ans= solution(s)
    print(ans)