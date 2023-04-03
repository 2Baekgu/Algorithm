#include <iostream>
using namespace std;
// 연속된 서브 어레이의 최대 합을 찾는 함수
// 주어진 정수 어레이에서
int kadane(int arr[], int n)
{
    // 지금까지 찾은 최대 합 서브 어레이을 저장합니다.
    int max_so_far = 0;
 
    // 현재 위치에서 끝나는 서브 어레이의 최대 합을 저장합니다.
    int max_ending_here = 0;
    int k = 0;
    int start_idx = -1;
    int end_idx = -1;
    // 주어진 어레이 순회
    for (int i = 0; i < n; i++)
    {
        // 인덱스 `i`에서 서브 어레이 "끝"의 최대 합계를 업데이트합니다.
        // 이전 인덱스 `i-1`에서 끝나는 최대 합계까지의 현재 요소)
        max_ending_here = max_ending_here + arr[i];
 
        // 최대 합계가 음수이면 0으로 설정합니다(이는
        // 빈 서브 어레이)
        if (max_so_far < max_ending_here){
            max_so_far = max_ending_here;
            start_idx = k;
            end_idx = i;
        }
        else if(max_ending_here <= 0){
            k = i + 1;
            max_ending_here = 0;
        }
    }
    if (max_so_far < 0){
        max_so_far = 0;
        start_idx = -1;
        end_idx = -1;
    }
    cout << max_so_far << " " << start_idx << " " << end_idx << endl;
    return max_so_far;
}
 
int main()
{
    int t, n;
    int arr[101];
    cin >> t;
    for(int i = 0; i <t; i++)
    {
        cin >> n;
        for(int j = 0; j <n; j++)
            cin >> arr[j];
        kadane(arr, n);
    }
 
    return 0;
}