n, money = map(int, input().split())
value = [int(input()) for _ in range(n)]
for i in range(1, len(value)):
    if value[i-1] < value[i]:
        coin = money//value[i-1]
        money -= coin*value[i-1]
        money += coin*value[i]
print(money)