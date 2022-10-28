import sys

# endCheck=True
def notsolved():
    for b in brackets :
        if len(stack)==0:
            stack.append(b)
        elif b=='(' or b=='[':
            stack.append(b)
        elif b==')':
            tmpcount=0
            tmp = stack.pop()
            while tmp!='(' and stack:
                if type(tmp)==int:
                    tmpcount+=tmp
                else :
                    break
                tmp= stack.pop()
            if tmp!='(':
                endCheck=False
                break
            else :
                if tmpcount==0:
                    stack.append(2)
                else :
                    stack.append(tmpcount*2)
        else :
            tmpcount=0
            tmp = stack.pop()
            while tmp!='[' and stack:
                if type(tmp)==int:
                    tmpcount+=tmp
                else :
                    break
                tmp= stack.pop()
            
            if tmp!='[':
                endCheck=False
                break
            else :
                if tmpcount==0:
                    stack.append(3)
                else :
                    stack.append(tmpcount*3)
                
    try:
        if not endCheck:print(0)
        else :print(sum(stack))
    except:
        print(0)


def bracket_loop(close_bracket):
    mp_val =2
    if close_bracket==')': open_bracket= '('
    else : 
        mp_val=3
        open_bracket='['
    tmp=0
    last_val = stack.pop()
    while last_val!=open_bracket:
        if type(last_val)==int:
            tmp+=last_val
        else :
            return 0

        if not stack:
            break
        last_val=stack.pop()

    return mp_val*tmp if tmp!=0 else mp_val

if __name__=='__main__':
    sys.stdin = open('inputs.txt','r')
    brackets= sys.stdin.readline()
    stack =[]
    for c in brackets :
        if c=='(' :
            stack.append(c)
        elif c=='[':
            stack.append(c)
        else:
            if len(stack)==0:
                break
            score=bracket_loop(c)
            if score==0:
                stack=[]
                break        
            stack.append(score)

    try :
        answer =sum(stack)
    except:
        answer=0

    print(answer)

            
