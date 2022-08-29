N, K = map(int, input().split())
answer = 0
unit = []
for i in range(N):
    unit.append(int(input()))

while K>0:
    for i in range(len(unit)):
        if (unit[len(unit)-i-1] <= K):
            K -= unit[len(unit)-i-1]
            answer += 1
            break

print(answer)
