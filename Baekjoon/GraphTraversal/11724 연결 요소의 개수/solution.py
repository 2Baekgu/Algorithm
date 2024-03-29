from collections import deque
import sys
input = sys.stdin.readline()

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        result +=1

print(result)