N, K = map(int, input().split())
answer = 0
unit = sorted([int(input()) for i in range(N)], reverse=True)

for i in unit:
    answer += K // i
    K %= i

print(answer)
