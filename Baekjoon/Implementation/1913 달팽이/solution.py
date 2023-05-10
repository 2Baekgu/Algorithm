N = int(input())
n = N #기존의 n값 저장
m = int(input())
arr = [[0 for j in range(n)] for i in range(n)]
number = n*n
row = -1
col = 0
while number > 0:
    for i in range(n):
        row += 1
        arr[row][col] = number
        number -= 1

    n -= 1
    for i in range(n):
        col += 1
        arr[row][col] = number
        number -= 1

    for i in range(n):
        row -= 1
        arr[row][col] = number
        number -= 1

    n -= 1
    for i in range(n):
        col -= 1
        arr[row][col] = number
        number -= 1
        
for i in arr:
    for j in i:
        print(j, end=' ')
    print('')

for i in range(N):
    for j in range(N):
        if arr[i][j] == m:
            print(i+1, end=' ')
            print(j+1)