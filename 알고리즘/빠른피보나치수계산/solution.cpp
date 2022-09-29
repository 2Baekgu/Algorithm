#include <iostream>
using namespace std;
const int M = 1000;
const int P = 15*(M/10);
int arr[P];

int main()
{
    int testCase, n;
    cin >> testCase;
    for(int i = 0; i<testCase; i++){
        cin >> n;
        if(n == 0) cout << "0" << endl;
        else if (n == 1) cout << "1" << endl;
        else{
            arr[0] = 0;
            arr[1] = 1;
            for (int j = 2; j < P; j++){
                arr[j] = (arr[j-1] + arr[j-2])% M;
            }
            cout << arr[n%P] << endl;
        }
    }
}