# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# 처음 푼 방법
# n = input()
# answer = 0
# position = [False, False, False, False]
# row, col = 0, 0
# row_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# for i in range(8):
#     if n[0] == row_alpha[i]:
#         row = i+1

# col = int(n[1])

# if row+2 < 9:
#     position[0] = True
# elif row - 2 > 0:
#     position[1] = True
# elif col + 2 < 9:
#     position[2] = True
# elif col -2 > 0:
#     position[3] = True

# for i in position:
#     if i == True:
#         answer += 2

# print(answer)