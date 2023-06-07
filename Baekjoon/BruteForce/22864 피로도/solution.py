a, b, c, m = map(int, input().split())
n = 0
work = 0
fatigue = 0
while n < 24:
    n += 1
    if fatigue + a > m:
        fatigue -= c
        if fatigue < 0: fatigue = 0
    else:
        fatigue += a
        work += b

print(work)