n, k = map(int, input().split())
cnt = 0
while n>1:
    if n%k == 0:
        n //= k
        cnt += 1
    else: 
        n-= 1
        cnt += 1
print(cnt)

# while True:
#   target = (n//k)*k
#   result += (n-target)
#   n = target
#   if n<k:
#       break
#   result +=1
#   n//=k
#   
# result += (n-1)
# print(result)
# 이런식으로 하면 코드 시간 줄어들음