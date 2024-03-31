/*Given an empty list and a stream of N numbers. Print min, max, sum, average and
mode (optional and if there are multiple modes then print any) after insertion of each
element from the stream to the list.

Example Input:
5
2 4 3 2 -3

Example output
▪ min, max, sum, average and mode after addition of 2 is 2, 2, 2, 2, 2.
▪ min, max, sum, average and mode after addition of 4 is 2, 4, 6, 3, 4.
▪ min, max, sum, average and mode after addition of 3 is 2, 4, 9, 3, 4.
▪ min, max, sum, average and mode after addition of 2 is 2, 4, 11, 2.75, 2.
▪ min, max, sum, average and mode after addition of -3 is -3, 3, 8, 1.6, 2.
*/

#include<iostream>
using namespace std;

void insertionSort(int arr[], int n){
    for(int i=1; i<n; i++){
        int current = arr[i];
        int j = i-1;
        while(arr[j]>current && j>=0){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = current;
    }
}

int findMode(int array[], int size) {
    int mode = array[0];
    int maxCount = 1;

    int current = array[0];
    int currentCount = 1;

    for (size_t i = 1; i < size; ++i) {
        if (array[i] == current) {
            ++currentCount;
        } else {
            if (currentCount > maxCount) {
                maxCount = currentCount;
                mode = current;
            }

            current = array[i];
            currentCount = 1;
        }
    }

    // Check for the last element
    if (currentCount > maxCount) {
        mode = current;
    }

    return mode;
}

int main(){
    int n;
    cin>>n;

    int arr[n];
    float sum = 0;
    for(size_t i=0; i<n; i++){
        cin>>arr[i];
        sum += arr[i];

        insertionSort(arr, n);

        // after sorting, arr[0] will be min and element at current index will be max
        int min = arr[0];
        int max = arr[i];

        float avg = sum/(i+1);

        int mode = findMode(arr, n);

        cout<<"min, max, sum, average and mode after insertion of "<<arr[i]<<" is : "<<arr[0]<<", "<<max<<", "<<sum<<", "<<avg<<", "<<mode<<endl;
    }

}

    