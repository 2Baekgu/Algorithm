n, k = map(int, input().split())
t = list(map(int, input().split()))
answer = []
for i in range(n-k+1):
    a = 0
    for j in range(k):
        a += t[i+j]
    answer.append(a)
print(max(answer))

# temp = sum(temperature_list[i:i+k])