N, K = map(int, input().split())
answer = 0
unit = [int(input()) for i in range(N)]
unit.sort(reverse=True)

for i in unit:
    answer += K // i
    K %= i

print(answer)
