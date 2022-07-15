import sys
# sys.stdin=open('inputs.txt','r')

a= input()
b= input()



def getList(words) :
    
    lists =[0]*52

    for i in range(len(words)):
        if words[i].isupper():
            lists[ord(words[i])-65]+=1
        else :
            lists[ord(words[i])-71]+=1

    return lists

alist = getList(a)
blist = getList(b)

if alist != blist :
    print('NO')
else:
    print('YES')

