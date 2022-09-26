#include <iostream>
using namespace std;

void permuteString(char *str, int begin, int end);
void swap(char *a, char *b);

int length;
int answer;
int main()
{
 int numTestCases;
 scanf("%d", &numTestCases);
 for (int i = 0; i < numTestCases; ++i)
 {
    char str[10];
    cin >> str;
    length = 0;
    answer = 0;
    for (int j=0; str[j] != '\0'; j++){
        length ++;
    }
    permuteString(str, 0, length);
    cout << answer << endl;
 }
 return 0;
}
void permuteString(char *str, int begin, int end)
{
    int m = -1;
    int range = end - begin;
    if(range == 1){
        int sum = 0;   
        int m = -1;
        for (int i = 0; i<end; i++){
            m *=-1;
            sum += m*(int(str[i])-97);
        }
        if(sum > 0)
            answer++;
    }
    else
    {
        for(int i = 0; i < range; i++)
        {
            swap(&str[begin], &str[begin+i]);
            permuteString(str, begin+1, end);
            swap(&str[begin], &str[begin+i]);
        }
    }
}
void swap(char *a, char *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}