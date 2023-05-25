m = int(input())
n = int(input())
num = []
for i in range(m, n+1):
    sosu = True
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            sosu = False
            break
    if sosu: num.append(i)

if 1 in num: num.remove(1)
if len(num) > 0:
    print(sum(num))
    print(num[0])
else:
    print(-1)

