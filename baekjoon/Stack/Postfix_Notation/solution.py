import sys
sys.stdin = open('inputs.txt','r')
txt = sys.stdin.readline()
oper_stack=[]
ans =''
for i in range(len(txt)):
    if txt[i].isalpha():
        ans+=txt[i]
    elif txt[i]=='(':
        oper_stack.append(txt[i])
    elif txt[i]==')' :        
        tmp_oper= oper_stack.pop()
        while tmp_oper!='(' :
            ans+=tmp_oper
            tmp_oper=oper_stack.pop()
    
    elif txt[i] in ['+','-'] :
        while len(oper_stack) and oper_stack[-1] !='(':            
            ans+=oper_stack.pop()
        oper_stack.append(txt[i])
    else :
        while len(oper_stack) and oper_stack[-1] in ['*','/']:
            ans+=oper_stack.pop()
        oper_stack.append(txt[i])
    
while len(oper_stack) :
    ans+=oper_stack.pop()

print(ans)
    