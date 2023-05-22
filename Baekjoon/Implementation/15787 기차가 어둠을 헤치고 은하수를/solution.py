def one(train, seat):
    arr[train-1][seat-1] = 1

def two(train, seat):
    arr[train-1][seat-1] = 0

def three(train):
    arr[train-1].insert(0, 0)
    arr[train-1].pop(len(arr[train-1])-1)

def four(train):
    arr[train-1].append(0)
    arr[train-1].pop(0)

n, m = map(int, input().split()) #기차의 수, 명령의 수
arr = [[0 for _ in range(20)] for _ in range(n)]
for i in range(m):
    command = 0
    train = 0
    seat = 0
    k = list(map(int, input().split()))
    if len(k) == 3:
        command = k[0]
        train = k[1]
        seat = k[2]
        if command == 1: one(train, seat)
        else: two(train, seat)
    else:
        command = k[0]
        train = k[1]
        if command == 3: three(train)
        else: four(train)

array = []
for i in range(n):
    a = list(map(str, arr[i]))
    array.append(''.join(a))

milky_way = list(set(array))
print(len(milky_way))
