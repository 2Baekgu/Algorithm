#include <stdio.h>
#define MAX_SIZE 1000
void bubbleSort(int a[], int n);
void bubbleSortImproved1(int a[], int n);
void bubbleSortImproved2(int a[], int n);
void copyArray(int a[], int b[], int n);
int main()
{
 int numTestCases;
 scanf("%d", &numTestCases);
 for (int i = 0; i < numTestCases; ++i)
 {
 int num;
 int a[MAX_SIZE], b[MAX_SIZE];
 scanf("%d", &num);
 for (int j = 0; j < num; j++)
 scanf("%d", &b[j]);
 copyArray(a, b, num);
 bubbleSort(a, num);
 copyArray(a, b, num);
 bubbleSortImproved1(a, num);
 copyArray(a, b, num);
 bubbleSortImproved2(a, num);
 printf("\n");
 }
 return 0;
}
void swap(int a, int b)
{
 int tmp = a;
 a = b;
 b = tmp;
}
/* BubbleSort 함수 */
void bubbleSort(int a[], int n)
{
 int countCmpOps = 0; // 비교 연산자 실행 횟수
 int countSwaps = 0; // swap 함수 실행 횟수
 // bubble sort 알고리즘 구현
 for(int pass=1; pass<n; pass++){
    for(int i=1; i<=n-pass; i++){ // pass = 1,2,…,n-1
        countCmpOps++;
        if(a[i-1]>a[i]){ // >: 비교연산자
            int tmp = a[i-1]; // A[i-1]와A[i]를교환
            a[i-1] = a[i];
            a[i] = tmp;
            countSwaps++;
        }
    }
 }
 printf("%d %d ", countCmpOps, countSwaps);
}

/* BubbleSort 함수 - Improved Version 1 */
void bubbleSortImproved1(int a[], int n)
{
 int countCmpOps = 0; // 비교 연산자 실행 횟수
 int countSwaps = 0; // swap 함수 실행 횟수
 // bubble sort의 개선된 알고리즘 (1) 구현
 for(int pass = 1; pass < n; pass++) 
 {
    bool swapped = false; // 이번 pass에서 데이터 교환했는지 유무
    for(int i = 1; i<=n-pass; i++){
        countCmpOps++;
        if(a[i-1] > a[i])
        {
            int tmp = a[i-1];
            a[i-1] = a[i];
            a[i] = tmp;
            swapped = true;
            countSwaps++;
        }
    }
    if(swapped == false) break; // 이번 pass에서 데이터를 교환하지 않았다면
 }  // 데이터가 정렬되어 있음. 따라서 종료함
 printf("%d %d ", countCmpOps, countSwaps);
}

/* BubbleSort 함수 - Improved Version 2 */
void bubbleSortImproved2(int a[], int n)
{
 int countCmpOps = 0; // 비교 연산자 실행 횟수
 int countSwaps = 0; // swap 함수 실행 횟수
 // bubble sort의 개선된 알고리즘 (2) 구현
 int lastSwappedPos = n; // 마지막으로 교환한 데이터의 위치
 while(lastSwappedPos > 0)
 {
    int swappedPos = 0; // 이번 pass에서 데이터 교환한 위치
    for(int i = 1; i< lastSwappedPos; i++){
        countCmpOps++;
        if(a[i-1] > a[i]){
            int tmp = a[i-1];
            a[i-1] = a[i];
            a[i] = tmp;
            swappedPos = i; // 데이터 교환한 위치
            countSwaps++;
        }
    }
    lastSwappedPos = swappedPos; // 이번 pass에서 교환한 마지막 데이터의 위치
 }                               // 다음 pass에서는 이 위치 바로앞까지만 실행하면됨
 printf("%d %d ", countCmpOps, countSwaps);
}

void copyArray(int a[], int b[], int n)
{
 for (int i = 0; i < n; i++)
 a[i] = b[i];
}