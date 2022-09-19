n = int(input())
drink = sorted(list(map(int, input().split())), reverse=True)
result = drink[0]
for i in range(1, n):
    result += drink[i]/2

print(result)
