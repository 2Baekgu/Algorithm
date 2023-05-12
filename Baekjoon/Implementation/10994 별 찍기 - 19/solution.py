n = int(input())
arr = ["*"]
for i in range(1, n*2-1):
    if i%2 != 0:
        for j in range(len(arr)):
            arr[j] = " "+arr[j]+" "
        arr.insert(0, " "*(i*2+1))
        arr.append(" "*(i*2+1))

    else:
        for j in range(len(arr)):
            arr[j] = "*"+arr[j]+"*"

        arr.insert(0, "*"*(i*2+1))
        arr.append("*"*(i*2+1))

for i in arr: print(i)