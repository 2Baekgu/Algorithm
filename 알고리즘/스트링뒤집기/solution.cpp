#include <iostream>
using namespace std;

void stringRv(string s, int k, string str);
int main()
{
 int numTestCases;
 scanf("%d", &numTestCases);
 for (int i = 0; i < numTestCases; ++i)
 {
 string s, str;
 int k;
 cin >> s;
 str = "";
 k = s.length();
 stringRv(s, k, str);
 }
 return 0;
}

void stringRv(string s, int k, string str)
{
    if(k == 1){
        str += s[0];
        cout << str << endl;
    }
    else{
        str += s[k-1];
        stringRv(s, k-1, str);
    }
}