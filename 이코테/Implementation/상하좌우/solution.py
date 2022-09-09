n = int(input())
arr = list(map(str, input().split()))
position = [1, 1]
for i in arr:
    if i == 'U' and position[0] != 1:
        position[0] -= 1
    elif i == 'D'and position[0] != n:
        position[0] += 1
    elif i == 'L' and position[1] != 1:
        position[1] -= 1
    elif i == 'R' and position[1] != n:
        position[1] += 1

for i in position: print(i, end=' ')
