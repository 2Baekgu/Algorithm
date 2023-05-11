import sys

def input():
    return sys.stdin.readline().rstrip()

r, s = map(int, input().split())
arr = [list(input()) for _ in range(r)]

min_length = r
for i in range(s):
    for j in range(r-1, -1, -1):
        if arr[j][i] == 'X':
            height = 0
            while arr[j+height+1][i] == '.':
                 height+=1
            min_length = min(min_length, height)
            break

for i in range(r-1, -1, -1):
    for j in range(s):
            if arr[i][j] == 'X':
                arr[i][j] = '.'
                arr[i+min_length][j] = 'X'
for i in arr:
    print(''.join(i))