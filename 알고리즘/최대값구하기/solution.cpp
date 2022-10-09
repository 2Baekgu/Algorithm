#include <iostream>
using namespace std;

#define MAX_SIZE 100
#define MAX(a, b) ((a)>(b)? (a):(b))

int recurMax(int a[], int left, int right)
{
    int half;
    if (left == right)
        return a[left];
    else
    {
        half = (left+right)/2;
        return MAX(recurMax(a, left, half),
                   recurMax(a, half+1, right));
    }
}

int main()
{
    int t, n;
    cin >> t;
    for(int i = 0; i<t; i++)
    {
        int v[MAX_SIZE] = {0};
        cin >> n;
        for(int j = 0; j<n; j++)
        {
            cin >> v[j];
        }
        cout << recurMax(v, 0, n-1) << endl;
    }
}