#include <iostream>
using namespace std;

void stringRv(char s[], int k);
int main()
{
 int numTestCases;
 scanf("%d", &numTestCases);
 for (int i = 0; i < numTestCases; ++i)
 {
 char s[100];
 int k; 
 int length = 0;
 cin >> s;
 for ( int j= 0; s[j] != '\0'; j++)
 {
    length++;
 }
 k = length;
 stringRv(s, k);
 }
 return 0;
}

void stringRv(char s[], int k)
{
    if(k == 1){
        cout << s[0] << endl;
    }
    else{
        cout << s[k-1];
        stringRv(s, k-1);
    }
}