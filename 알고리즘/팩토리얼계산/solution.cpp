#include <stdio.h>

int Factorial(int n);
int main()
{
 int numTestCases;
 scanf("%d", &numTestCases);
 for (int i = 0; i < numTestCases; ++i)
 {
 int num;
 scanf("%d", &num);
 printf("%d\n", Factorial(num)%1000);
 }
 return 0;
}

/* 피보나치 함수 */
int Factorial(int n)
{
int answer;
 if (n<=1)
    return 1;
 else
    answer = n*Factorial(n-1);
    while (answer % 10 == 0)
        answer /= 10;
    answer %= 1000000; 
    return answer;
}