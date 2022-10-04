#include <iostream>
using namespace std;

int gcd(int a, int b);

int main(){
    int t, a, b;
    cin >> t;
    
    for(int i = 0; i<t; i++){
        cin >> a >> b;
        cout << gcd(a, b) << endl;
    }
    return 0;
}

int gcd(int a, int b)
{
    if (b == 0) return a;
    else return gcd(b, a%b);
}