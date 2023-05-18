while True:
    n = 0
    arr = list(input())
    if arr == ['0']: break
    while True:
        palindrome = True
        for i in range(0, len(arr)//2):
            if arr[i] != arr[-(i+1)]:
                palindrome = False
                arr[-1] = str(int(arr[-1])+1)
                n += 1
                for j in range(-1, -len(arr), -1):
                    if int(arr[j]) > 9:
                        arr[j] = '0'
                        arr[j-1] = str(int(arr[j-1]) + 1)
                break
        if palindrome: break
    print(n)
