n, m = map(int, input().split())
result = []
for i in range(n):
    arr = list(map(int, input().split()))
    result.append(min(arr))
print(max(result))