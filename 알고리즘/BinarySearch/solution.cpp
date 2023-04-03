#include <iostream>

using namespace std;
int binarySearch(int start, int end, int array[], int k);

int binarySearch(int start, int end, int array[], int k){
    
    if (start > end){
        return -1;
    }else{
        int mid = (start + end) / 2;
    
        if (array[mid] == k) {
            return mid;
        } else if (array[mid] > k){
            return binarySearch(start, mid - 1, array, k);
        } else {
            return binarySearch(mid + 1, end, array, k);
        }
    }
}


int main(){
    int t;
    int n, k;
    int answer = 0;

    cin >> t;
    for(int i = 0; i < t; i++){
        cin >> n >> k;
        int *arr1 = new int[n];
        for(int j = 0; j < n; j++){
            cin >> arr1[j];
        }
        answer = binarySearch(0, n-1, arr1, k);
        cout << answer << endl;

    }
    return 0;
}
