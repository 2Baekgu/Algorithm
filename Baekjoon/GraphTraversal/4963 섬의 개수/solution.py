from collections import deque

dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
w = -1
h = -1

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >=h or ny <0 or ny >=w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

while w!=0 and h!=0:
    graph = []
    result = 0
    w, h = map(int, input().split())
    for _ in range (h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                graph[i][j] = 0
                bfs(i, j)
                result +=1

    if w==0 and h==0:
        break
    else: print(result)