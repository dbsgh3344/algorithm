def solution(absolutes,s) :
    return sum([absolutes[i] if s[i]==True else -absolutes[i] for i in range(len(absolutes))])

    



abs=[4,7,12]
signs = [True,False,True]
a= solution(abs,signs)
print(a)