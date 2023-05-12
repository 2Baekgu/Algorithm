n = int(input())
arr = list(map(int, input().split()))
student = int(input())
for _ in range(student):
   gender, number = map(int, input().split())
   if gender == 1: # 남자
      for i in range(n):
         if (i+1)%number == 0:
            arr[i] = (1 if arr[i] == 0 else 0)

   else: #여자
    arr[number-1] = (1 if arr[number-1] == 0 else  0)
    for i in range(n):
         if number-2-i >= 0 and number+i < n:
            if arr[number-2-i] == arr[number+i]:
               if arr[number-2-i] == 0:
                  arr[number-2-i] = 1
                  arr[number+i] = 1
               else: 
                  arr[number-2-i] = 0
                  arr[number+i] = 0
            else: break
         else: break


for i in range(n): 
   if (i+1)%20 == 0: 
      print(arr[i])
   else:
      print(arr[i], end=' ')