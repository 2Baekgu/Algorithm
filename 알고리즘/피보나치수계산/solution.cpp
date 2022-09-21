#include <stdio.h>

void Fibo(int n);
int main()
{
 int numTestCases;
 scanf("%d", &numTestCases);
 for (int i = 0; i < numTestCases; ++i)
 {
 int num;
 scanf("%d", &num);
 Fibo(num);
 }
 return 0;
}
/* 피보나치 함수 */
void Fibo(int n)
{
 int first = 0;
 int second = 1;
 for(int i = 0; i<n; i++)
 {
    int tmp = first;
    first = second;
    second = tmp + second;
 }
 printf("%d\n",first);
}