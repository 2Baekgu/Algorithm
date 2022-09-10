color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result = ''
for i in range(3):
    resistance = input()
    for j in range(len(color)):
        if color[j] == resistance and i != 2:
            result += value[j]
        elif color[j] == resistance and i == 2:
            result += int(value[j])*'0'

print(int(result))
