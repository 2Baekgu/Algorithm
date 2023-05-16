picture = int(input())
recommend_num = int(input())
recommend = list(map(int, input().split()))
result = []

for i in range(recommend_num):
    if len(result) == 0:
        result.insert(0,[1, recommend[i]])

    elif picture > len(result) > 0:
        is_exist = False
        for j in range(len(result)):
            if recommend[i] == result[j][1]:
                result[j][0] += 1
                is_exist = True
            
        if not is_exist:
            result.insert(0,[1, recommend[i]])
    else: 
        k = 0
        is_ok = True
        for j in range(len(result)):
            if recommend[i] == result[j][1]:
                result[j][0] += 1
                is_ok = False
                break
        if is_ok:
            min_num = 1e9
            for p in range(len(result)):
                if min_num >= result[p][0]:
                    min_num = result[p][0]
                    k = p
            result.pop(k)
            result.insert(0, [1, recommend[i]])


result.sort(key=lambda x:x[1])
for i in range(len(result)):
    print(result[i][1], end=' ')