from collections import deque
duck = [[]]
quack = input()
result = 0

for i in range(len(quack)):
    ducktf = False
    if quack[i] == 'q':
        for j in range(len(duck)):
            if duck[j] == []:
                duck[j].append('q')
                ducktf = True
                break
        if ducktf == False:
            duck.append(['q'])
            ducktf = True
    elif quack[i] == 'u':
        for j in range(len(duck)):
            if len(duck[j]) == 1 and duck[j][0] == 'q':
                duck[j].append('u')
                ducktf = True
                break
    elif quack[i] == 'a':
        for j in range(len(duck)):
            if len(duck[j]) == 2 and duck[j][1] == 'u':
                duck[j].append('a')
                ducktf = True
                break
    elif quack[i] == 'c':
        for j in range(len(duck)):
            if len(duck[j]) == 3 and duck[j][2] == 'a':
                duck[j].append('c')
                ducktf = True
                break
    elif quack[i] == 'k':
        for j in range(len(duck)):
            if len(duck[j]) == 4 and duck[j][3] == 'c':
                duck[j].append('k')
                ducktf = True
                break

    for j in range(len(duck)):
        if  ''.join(duck[j]) == 'quack':
            duck[j] = []

    if ducktf == False:
        print(-1)
        exit()

for i in duck:
    if i == []:
        result +=1
    else:
        print(-1)
        exit()
print(result)