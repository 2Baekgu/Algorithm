from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for _ in range(T):
    
    result = 0
    M, N, K = map(int, input().split())
    graph = [ [0]*M for _ in range(N) ]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                result +=1

    print(result)
