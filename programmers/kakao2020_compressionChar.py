def solution(s) :
    tmp = len(s)
    for i in range(int(len(s)/2)) :
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
            
        if cnt >1 :
            answer_chars+=str(cnt)+iter_chars

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
    ans = len(s)

    for i in range(int(len(s)/2)) :
        iter_chars = s[:i+1]
        
        cnt= 1
        ans_chars = ''
        tmp_s = s
        for j in range(i+1,len(s),i+1) :
            if iter_chars == tmp_s[j : 1+i+j] :
                cnt+=1
            else :
                if cnt>1 :
                    ans_chars+=str(cnt)+iter_chars
                    tmp_s = tmp_s[j:]
                else :
                    ans_chars+=iter_chars
                    tmp_s = tmp_s[j:]
                
                cnt=1
                iter_chars= s[j : 1+i+j]
        
        print(ans_chars)

        if ans > len(ans_chars) >0 :
            ans = len(ans_chars) 


    return ans           


        
        
           
    
        
        





if __name__=="__main__":
    s= "aabbaccc"
    ans= solution(s)
    print(ans)