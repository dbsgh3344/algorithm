import sys
sys.stdin = open('./AtCoder/Beginners_Selection/Coins/inputs.txt')
a= int(input())
b= int(input())
c= int(input())
x= int(input())
total_iter= (a+1)*(b+1)*(c+1)
lists= [0]*total_iter
cnt=0
for i in range(len(lists)):
    if i!=0 and i%((b+1)*(c+1))==0:
        cnt+=1
    lists[i] = 500*cnt

cnt=0
for i in range(len(lists)):
    cnt = (i//(c+1))%(b+1)
    lists[i] += 100*cnt
    

cnt=0
for i in range(len(lists)):
    cnt= i%(c+1)
    lists[i]+=50*cnt

cnt=0
for i in lists :
    if x==i:
        cnt+=1

print(cnt)
    