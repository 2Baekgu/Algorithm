bgMap=[list(map(int, input().split())) for _ in range(5)]
bgNumber=[list(map(int, input().split())) for _ in range(5)]
count = 0
def bingo():
    result = 0
    #가로
    for i in range(5):
        if sum(bgMap[i]) == 0:
            result += 1
    
    #세로
    for i in range(5):
        num = 0
        for j in range(5):
            num +=bgMap[j][i]
        if num == 0: result += 1

    #대각선
    temp_left = []
    temp_right = []

    for i in range(5):
        temp_left.append(bgMap[i][i])
        temp_right.append(bgMap[i][4-i])

    if sum(temp_left) == 0:
        result += 1
    if sum(temp_right) == 0:
        result += 1
    
    return result

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if  bgNumber[i][j] == bgMap[k][l]:
                    bgMap[k][l] = 0
                    count += 1
                if count >=12:
                    if bingo() >= 3:
                        print(count)
                        exit()