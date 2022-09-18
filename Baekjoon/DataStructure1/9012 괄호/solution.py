t = int(input())
result = []
for i in range(t):
    vps = input()
    stack = []
    for j in range(len(vps)):
        stack.append(vps[j])
        if len(stack) >= 2 and stack[-2] + stack[-1] == '()':
            stack.pop()
            stack.pop()

    if len(stack)>0: result.append('NO')
    else: result.append('YES')

for i in result: print(i)
