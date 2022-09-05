import math
answer = []

while True:
    n = input()
    if n == '0': break
     #ceil은 3.5 -> 4 위의 숫자로 올려줌
    elif n[0:len(n)//2] == n[:math.ceil(len(n)/2)-1:-1]:
        answer.append('yes')
    else: answer.append('no')

for i in answer: print(i)
