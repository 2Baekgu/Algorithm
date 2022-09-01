n = int(input())
stage = [int(input()) for i in range(n)]
answer = 0
stage.reverse()
for i in range(len(stage)-1):
    if stage[i] <= stage[i+1]:
        stage[i+1], origin = stage[i]-1, stage[i+1]
        answer += origin-stage[i+1]

print(answer)