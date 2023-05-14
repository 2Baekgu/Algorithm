arr = [list(map(int, input().split())) for _ in range(19)]

def omok(color, a, b):
    #가로
    num = 0
    i = 0
    while True:
        if b+i > 18: break
        if arr[a][b+i] == color:
            num += 1
        else: break
        i += 1
    i = 1
    while True:
        if b-i < 0: break
        if arr[a][b-i] == color:
            num += 1
        else: break
        i += 1
    if num == 5:
        print(color)
        print(a+1, end=' ')
        print(b+1)
        exit()

    #세로
    num = 0
    i = 0
    while True:
        if a+i >18 : break
        if arr[a+i][b] == color:
            num += 1
        else: break
        i += 1
    i = 1 
    while True:
        if a-i <0 : break
        if arr[a-i][b] == color:
            num += 1
        else: break
        i += 1
    if num == 5:
        print(color)
        print(a+1, end=' ')
        print(b+1)
        exit()

    #대각선
    num = 0
    i = 0
    while True:
        if a+i >18 or b+i >18: break
        if arr[a+i][b+i] == color:
            num += 1
        else: break
        i += 1
    i = 1
    while True:
        if a-i < 0 or b-i <0: break
        if arr[a-i][b-i] == color:
            num += 1
        else: break
        i += 1
    if num == 5:
        print(color)
        print(a+1, end=' ')
        print(b+1)
        exit()

    #대각선2
    num = 0
    i = 0
    while True:
        if a-i <0 or b+i >18: break
        if arr[a-i][b+i] == color:
            num += 1
        else: break
        i += 1
    i = 1
    while True:
        if a+i > 18 or b-i <0: break
        if arr[a+i][b-i] == color:
            num += 1
        else: break
        i += 1
    if num == 5:
        for i in range(5):
            if a+1 >18 or b-1 <0: break
            if arr[a+1][b-1] == color:
                a = a+1
                b = b-1
        print(color)
        print(a+1, end=' ')
        print(b+1)
        exit()
  
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            omok(1, i, j)
        
        if arr[i][j] == 2:
            omok(2, i, j)

print(0)