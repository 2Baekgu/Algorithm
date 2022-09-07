n = input()
answer = 1
for i in range(len(n)):
    if n[i] != '0':
        answer *= int(n[i])

print(answer)

data = input()
result = int(data[0])

# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <=1 or result <=1:
#         result += num
#     else:
#         result *= num
# print(result)