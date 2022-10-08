#include <iostream>
using namespace std;

#define MAX(a,b) ((a)>(b)?(a):(b))
int maxSubsequenceSum(int a[],int low,int high);
int maxSum(int a[], int low, int mid, int high);
int max(int a, int b, int c);

int max(int a, int b, int c)
{
    return MAX(MAX(a, b), c);
}


int maxSum(int a[], int low, int mid, int high)
{
    int sumLeft = 0;
    int sumRight = 0;
    int s = 0;
    for (int i = mid; i >= low; i--)
    {
        s = s + a[i];
        sumLeft = MAX(sumLeft, s);
    }

    s = 0;
    for (int i = mid + 1; i <= high; i++)
    {
        s = s + a[i];
        sumRight = MAX(sumRight, s);
    }

    return sumLeft + sumRight;
}

int maxSubsequenceSum(int a[],int low,int high)
{
	if (low == high)
		return a[low];
	int mid = (low + high) / 2;
    int n1, n2, n3;
    n1 = maxSubsequenceSum(a, low, mid);
    n2 = maxSubsequenceSum(a, mid+1, high);
    n3 = maxSum(a, low, mid, high);
    if (max(n1, n2, n3)<=0)
        return 0;
    else{
        return max(n1, n2, n3);
    }
}

int main()
{
    int t, n;
    cin >> t;
    int a[101];
    for(int i=0; i<t; i++)
    {
        cin >> n;
        for(int j=0;j<n;j++)
        {
            cin >> a[j];
        }
	    int max_sum = maxSubsequenceSum(a, 0, n-1);
	    cout << max_sum << endl;
    }
	return 0;
}

