n = int(input())
answer = 0
words = [input() for _ in range(n)] #단어 배열

for i in range(n):
    checker = True # 그룹 단어x = False
    arr =[]

    if len(set(words[i]))==1: checker = True #모두 같은 문자면 True
    else:
        arr.append(words[i][0])
        for j in range(1, len(words[i])): #범위 문제 때문에 문자열 길이 -1 만큼 반복문
            if words[i][j-1] != words[i][j] and words[i][j] in arr: # 앞문자와 현재문자가 다르고 철자 배열안에 존재한다면
                checker = False
                break
            else: arr.append(words[i][j]) 
            
    # 그룹단어라면 answer ++
    if checker == True:
        answer += 1

print(answer)