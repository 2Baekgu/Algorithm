n, m = map(int, input().split())

books = []
if n != 0: books  = list(map(int, input().split()))

weight, answer = 0, 0
for book in books:
    if weight + book < m:
        weight += book
    elif weight + book == m:
        weight = 0
        answer += 1
    elif weight + book > m:
        weight = 0
        weight += book
        answer += 1

if weight > 0: print(answer+1)
else: print(answer)
