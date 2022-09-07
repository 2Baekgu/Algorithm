n, m, k = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
answer = 0
for i in range(m):
    if (i+1) % k == 0:
        answer += arr[1]
    else: answer += arr[0]
print(answer)