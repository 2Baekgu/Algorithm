from collections import deque
import sys

def bfs():
    global d
    queue = deque()
    for i in range(len(ripeTomato)):
        queue.append(ripeTomato[i])
    
    while queue:
        x, y, days = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx >= n or nx < 0 or ny >= m or ny <0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny, days+1))
            d = days if d < days else d

m, n = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ripeTomato = []
d = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ripeTomato.append((i, j, 0))    

bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            sys.exit(0)

print(graph)
print(d)