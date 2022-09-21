#include <stdio.h>

int Fibo(int n);
int main()
{
 int numTestCases;
 scanf("%d", &numTestCases);
 for (int i = 0; i < numTestCases; ++i)
 {
 int num;
 scanf("%d", &num);
 printf("%d\n", Fibo(num));
 }
 return 0;
}
/* 피보나치 함수 */
int Fibo(int n)
{
    if (n <= 1) 
        return n;
    else
        return Fibo(n-1) + Fibo(n-2);
}