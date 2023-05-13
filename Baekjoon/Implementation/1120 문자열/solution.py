a, b = map(str, input().split())

min_str = 50
for i in range(len(b)-len(a)+1):
    num = 0
    for j in range(len(a)):
        if b[j+i] != a[j]: num += 1
    min_str = min(min_str, num)

print(min_str)