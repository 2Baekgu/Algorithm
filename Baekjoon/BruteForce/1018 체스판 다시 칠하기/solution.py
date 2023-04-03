import copy
n, m = map(int, input().split())

chess_o=[]

for i in range(n):
    chess_o.append(list(input()))

min = 999
for k in range(2):
    for r in range(m-7):
        for c in range(n-7):
            count = 0
            count_c = 0
            chess = copy.deepcopy(chess_o)
            if k == 1:
                chess[0][0] == "W"
            for col in range(c, c+8):
                for row in range(r, r+8):
                    if row == r and col == c:
                        continue
                    elif row == r and col != c:
                        if chess[col-1][row] == chess[col][row]:
                            count += 1
                            if chess[col-1][row] == "B":
                                chess[col][row] = "W"
                            else:
                                chess[col][row] = "B"
                    else:
                        if chess[col][row] == chess[col][row-1]:
                            count +=1
                            if chess[col][row-1] == "B":
                                chess[col][row] = "W"
                            else:
                                chess[col][row] = "B"

        if count < min:
            min = count

print(chess)
print(min)