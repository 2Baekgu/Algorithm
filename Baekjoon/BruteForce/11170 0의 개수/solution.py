t = int(input()) #테스트 케이스 수
answer = []
for i in range(t):
    result = 0
    n, m = map(int, input().split())
    for zero in range(n, m+1):
        result += str(zero).count('0')
    answer.append(result)

for i in answer: print(i)