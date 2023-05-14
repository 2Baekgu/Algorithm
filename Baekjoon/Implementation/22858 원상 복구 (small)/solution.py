n, k = map(int, input().split())

s = list(map(int, input().split()))
d = list(map(int, input().split()))
sr = [ 0 for _ in range(n)]

for _ in range(k):
    for i in range(n):
        sr[d[i]-1] = s[i]
    
    for i  in range(n): s[i] = sr[i]

print(*s)