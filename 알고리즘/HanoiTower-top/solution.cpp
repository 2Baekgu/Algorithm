#include <iostream>
using namespace std;
void Hanoi(int n, int a, int b, int c);
int k, m;
int disk[10] = {0};
int main()
{
    int t, numDisks;
    cin >> t;
    for(int i = 0; i<t; i++)
    {
        k = 0;
        disk[10] = {0};
        cin >> numDisks;
        m = numDisks;
        Hanoi(numDisks, 1, 2, 3);
    }
    return 0;
}
void Hanoi(int n, int a, int b, int c)
{
    if (n>0)
    {
        Hanoi(n-1, a, c, b);
        if (c == 3)
        {
            if (k == m-1 && n==1)
                cout << n << endl;
            else
            {
                cout << n << " ";
                disk[k] = n;
                k ++;
            }
        }
        else if(a == 3)
        {
            if (k == 1)
                cout << '0' << " ";
            else
                cout << disk[k-2] <<" ";
            k --;
        }
        Hanoi(n-1, b, a, c);
    }
}