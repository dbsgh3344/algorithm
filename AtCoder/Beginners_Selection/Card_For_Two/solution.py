import sys
sys.stdin = open('./AtCoder/Beginners_Selection/Card_For_Two/inputs.txt')
n = int(input())
cards=sorted(map(int,input().split()))

alice=[]
bob= []
b= True
while cards:
    cur_card = cards.pop()
    if b:
        alice.append(cur_card)
        b=False
    else :
        bob.append(cur_card)
        b=True

print(sum(alice)-sum(bob))


