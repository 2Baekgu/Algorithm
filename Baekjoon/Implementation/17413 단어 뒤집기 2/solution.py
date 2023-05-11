s = input()
word = []
reverse = True
at = 0
for i in range(len(s)):
    if s[i] == '<' :
        word.append(s[i])
        reverse = False
    elif s[i] == '>':
        word.append(s[i])
        reverse = True
        at = i+1
    elif s[i] == ' ':
        word.append(s[i])
        at = i+1
    else:
        if reverse == True:
            word.insert(at, s[i])
        else:
            word.append(s[i])

for i in word: print(i, end='')