import sys
sys.stdin = open('./AtCoder/Beginner_Contest_296/Chessboard/inputs.txt')

for i in range(8,0,-1):
    s= input()
    if '*' in s:
        a=s.index('*')
        ascii_code = chr(97+a)
        print(ascii_code+str(i))
