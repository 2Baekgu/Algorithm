r, c = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def GW(dado, a, b):
    num = 0
    for i in range(4):
        nx = dx[i] + a
        ny = dy[i] + b
        if dado[nx][ny] == '.':
            num += 1
    if num >= 3:
        return(1)
    return(0)

dado = [input() for _ in range(r)]
count = []
dado.insert(0, '.'*c)
dado.append('.'*c)
for i in range(len(dado)):
    dado[i] = '.' + dado[i] + '.'

for i in range(r+2):
    for j in range(c+2):
        if dado[i][j] == 'X':
            if GW(dado, i, j) == 1:
                count.append([i, j])

for i in range(len(count)):
    s = list(dado[count[i][0]])
    s[count[i][1]] = '.'
    dado[count[i][0]] = ''.join(s)

for i, row in enumerate(dado):
    row = list(row)
    dado[i] = row

while True:
    if 'X' not in dado[0]:
        dado.pop(0)
    else: break

while True:
    if 'X' not in dado[-1]:
        dado.pop(-1)
    else: break

for i in range(len(dado[0])):   
    left = 0
    right = 0
    for j in range(len(dado)):
        if dado[j][0] == '.':
            left += 1
        if dado[j][-1]== '.':
            right += 1
    if left == len(dado):
        for k in range(len(dado)):
            dado[k].pop(0)
    if right == len(dado):
        for k in range(len(dado)):
            dado[k].pop(-1)
    

for i in dado:
    print(''.join(i))