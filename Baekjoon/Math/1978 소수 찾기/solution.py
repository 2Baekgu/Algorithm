n = int(input())
arr = list(map(int, input().split()))
result = 0
for i in range(n):
    sosu = True
    for j in range(2, int(arr[i]**0.5)):
        if arr[i]%j == 0:
            sosu = False
            break
    if sosu: result +=1

if 1 in arr: result -= 1
print(result)