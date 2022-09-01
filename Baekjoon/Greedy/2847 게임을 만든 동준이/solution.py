n = int(input())
stage = [int(input()) for i in range(n)] #stage 배열 생성
answer = 0 

stage.reverse() #깔끔하게 큰 스테이지 부터 역순
for i in range(len(stage)-1):
    if stage[i] <= stage[i+1]: #마지막 레벨보다 한 단계 작은 레벨이 점수가 크거나 같을 때
        stage[i+1], origin = stage[i]-1, stage[i+1] # 마지막레벨 점수-1 = 바꾼점수, 원래점수 저장
        answer += origin-stage[i+1] # 원래점수-바꾼점수 answer에 더함

print(answer)