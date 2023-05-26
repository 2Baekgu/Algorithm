n = input()
n = n.replace('9', '6')
arr = [i for i in range(9)]
arr.append(6)

result = 1
for i in range(len(n)):
    if int(n[i]) in arr:
        arr.remove(int(n[i]))
    else:
        for j in range(9):arr.append(j)
        arr.append(6)
        arr.remove(int(n[i]))
        result += 1
print(result)