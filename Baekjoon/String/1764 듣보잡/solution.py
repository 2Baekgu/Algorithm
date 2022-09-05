n, m = map(int, input().split())
# 집합 자료형을 사용
name_1 = set([input() for _ in range(n)])
name_2 = set([input() for _ in range(m)])      
# 교집합을 출력함
arr = sorted(name_1 & name_2)
print(len(arr))
for i in arr: print(i)
