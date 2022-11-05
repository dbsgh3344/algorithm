import sys
sys.stdin = open('inputs.txt','r')

strarr = sys.stdin.readline().strip()
target_char = sys.stdin.readline().strip()
target_len = len(target_char)
stack =[]
for c in strarr :
    stack.append(c)
    if len(stack)<target_len :
        continue
    elif ''.join(stack[-target_len:])==target_char:
        [stack.pop() for _ in range(target_len)]


if len(stack)==0 :
    print("FRULA")
else :
    print(''.join(stack))
