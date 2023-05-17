room_num = int(input())
villain = int(input())
result = 0

room = [i+1 for i in range(room_num)]

for i in range(villain):
    a, b = map(int, input().split())
    for j in range(a-1, b-1):
        room[j] = 0
    
for i in room:
    if i != 0:
        result += 1

print(result)
