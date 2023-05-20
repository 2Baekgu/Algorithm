T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    house_num = int(input())
    house = list(map(int, input().split()))
    num = 0
    for i in range(2, house_num-2):
        hangang = 255
        for j in range(1, 3):
            a = house[i] - house[i-j]
            b = house[i] - house[i+j]
            if a < 1 or b < 1:
                hangang = 0
                break
            hangang = min(min(a, b), hangang)
        num += hangang
    print('#'+str(test_case)+' '+str(num))