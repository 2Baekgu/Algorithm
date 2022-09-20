#include <stdio.h>
#define MAX_SIZE 1000
void combSort(int a[], int n);
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
 combSort(a, num);
 }
 return 0;
}

/* comb sort 함수 */
void combSort(int a[], int n)
{
 int countCmpOps = 0; // 비교 연산자 실행 횟수
 int countSwaps = 0; // swap 함수 실행 횟수
 // comb sort 알고리즘 구현
 float shrink = 1.3;
 int j, tmp, gap = n, swapped = 1;

 while(gap > 1 || swapped){
    if((gap/=shrink)<1) gap = 1;
    for(j = swapped = 0; j<n-gap; j++){
        if(a[j] <= a[j+gap]) {
            countCmpOps++;
            continue;
        }
        swapped = 1;
        tmp = a[j];
        a[j] = a[j+gap];
        a[j+gap] = tmp;
        countSwaps++;
        countCmpOps++;
    }
 }
 printf("%d %d\n", countCmpOps, countSwaps);
}