#include <iostream>
using namespace std;

#define MAX_SIZE 100
int num;
void merge(int a[], int low, int mid, int high)
{
    int i, j, k;
    int tmp[MAX_SIZE];
    for (i = low; i <= high; i++)
        tmp[i] = a[i];
    i = k = low;
    j = mid + 1;
    while (i <= mid && j <= high){
        num ++;
        if (tmp[i] <= tmp[j])
            a[k++] = tmp[i++];
        else
            a[k++] = tmp[j++];
    }
    while (i <= mid)
        a[k++] = tmp[i++];
    while (j <= high)
        a[k++] = tmp[j++];
}

void mergeSort(int v[], int low, int high)
{
    int mid;
    if(low == high)
        return;
    
    mid = (low + high) / 2;

    mergeSort(v, low, mid);
    mergeSort(v, mid+1, high);
    merge(v, low, mid, high);
}

int main()
{
    int t, n;
    cin >> t;
    int v[MAX_SIZE];
    for(int tc=0; tc<t; tc++)
    {
        cin >> n;
        for(int i = 0; i<n; i++){
            cin >> v[i];
        }
        num = 0;
        mergeSort(v, 0, n-1);
        cout << num << endl;
    }
}
