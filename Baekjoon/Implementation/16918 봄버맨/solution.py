import copy

r, c, n = map(int, input().split())
arr_1 = [list(input()) for _ in range(r)]
arr_2 = [['O' for _ in range(c)] for _ in range(r)]
arr_3 = copy.deepcopy(arr_2)
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

if n%4 == 1:
    for i in arr_1: print(''.join(i))

elif n%4 == 2 or n%4 == 0:
    for i in arr_2: print(''.join(i))

elif n%4 == 3:
    for i in range(r):
        for j in range(c):
            if arr_1[i][j] == 'O':
                for k in range(4):
                    arr_3[i][j] = '.'
                    if i+x[k] <0 or j+y[k] <0 or i+x[k] >= r or j+y[k] >= c:
                        continue
                    else: arr_3[i+x[k]][j+y[k]] = '.'
    for i in arr_3: print(''.join(i))
