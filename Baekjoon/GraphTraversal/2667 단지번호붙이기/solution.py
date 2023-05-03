from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    home_cnt = 0 # 집개수
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    home_cnt += 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >=n:
                continue

            if graph[nx][ny] != 0:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                home_cnt += 1
    result.append(home_cnt)

n = int(input()) #지도의 크기 (가로 == 세로)
cnt = 0 # 단지수
result = []
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if  graph[i][j] != 0:
            bfs(i, j)
            cnt +=1

print(cnt)
result.sort()
for i in result: print(i)