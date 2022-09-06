coins = (500, 100, 50, 10, 5, 1)
count = 0
money = 1000 - int(input())

for coin in coins:
    count += money // coin
    money %= coin

print(count)
