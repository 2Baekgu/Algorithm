#include <stdio.h>
#define MAX_SIZE 1000
void ShellSort(int a[], int n);
int main()
{
 int numTestCases;
 scanf("%d", &numTestCases);
 for (int i = 0; i < numTestCases; ++i)
 {
 int num;
 int a[MAX_SIZE];
 scanf("%d", &num);
 for (int j = 0; j < num; j++)
 scanf("%d", &a[j]);
 ShellSort(a, num);
 }
 return 0;
}

/* Shell Sort 함수 */
void ShellSort(int a[], int n)
{
 int countCmpOps = 0; // 비교 연산자 실행 횟수
 int countSwaps = 0; // swap 함수 실행 횟수
 // Shell sort 알고리즘 구현
 int i, j, tmp;
 int gap = n/2;
 while(gap>0)
 {
    for(i = gap; i<n; i++)
    {
        tmp = a[i];
        j = i;
        while (j>=gap){
            if (a[j-gap] > tmp){
                a[j] = a[j-gap];
                j -= gap;
                countSwaps++;
                countCmpOps++;
            }
            else{
                countCmpOps++;
                break;
            }
        }
        a[j] = tmp;
    }
    gap /= 2;
 }
 
 printf("%d %d\n", countCmpOps, countSwaps);
}