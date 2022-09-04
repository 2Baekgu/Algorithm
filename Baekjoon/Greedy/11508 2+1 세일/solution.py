n = int(input())
# 내림차순으로 정렬
arr = sorted([int(input()) for _ in range(n)], reverse=True)
answer = 0
for i in range(0,len(arr),3): # 3번째 순으로 있는 값만 안더해줌
    answer += sum(arr[i:i+2])

print(answer)

