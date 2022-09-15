answer = ''
while True:
    code = input()
    if code == 'END': break
    answer += code[::-1]+'\n'

print(answer.rstrip('\n'))
