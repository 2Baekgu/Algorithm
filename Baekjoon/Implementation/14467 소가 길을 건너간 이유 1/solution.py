N = int(input())
answer = 0 # 소가 길을 건너간 횟수
dictionary = {}

for i in range(N):
    cow, road = map(int, input().split()) 
    if cow not in dictionary: # 딕셔너리에 소가 등록된 적이 없다면 추가
        dictionary[cow] = road
    else: # 소가 있다면 key 값을 이용해 value가 다를 시 answer += 1
        if dictionary[cow] != road:
            dictionary[cow] = road
            answer += 1

print(answer)