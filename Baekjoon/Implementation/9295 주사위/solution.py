t = int(input())
arr = []
for dice in range(t):
    a, b = map(int, input().split())
    arr.append(a+b)

for case in range(t):
    print(f'Case {case+1}: {arr[case]}')