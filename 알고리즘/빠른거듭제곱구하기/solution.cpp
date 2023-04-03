#include <iostream>
using namespace std;

int getPower(int n, int m);

int main(){
    int t, n, m;
    cin >> t;
    for(int i = 0; i<t; i++){
        cin >> n >> m;
        cout << getPower(n, m) << endl;
    }
    return 0;
}
int getPower(int n, int m){
    if (m == 0) return 1;
    long long ans = getPower((long long)n * n % 1000, m/2);
    if (m % 2 == 1) {
        ans *= n;
        ans %= 1000;
    }
    return ans;
}