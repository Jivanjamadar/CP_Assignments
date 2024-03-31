#include <stdio.h>
#include <stdbool.h>

int lowerb(int arr[], int size, int x) {
    int low = 0, high = size - 1, result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] >= x) {
            result = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return result;
}

int upperb(int arr[], int size, int x) {
    int low = 0, high = size - 1, result = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] > x) {
            result = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return result;
}

bool is_present(int arr[], int size, int x) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == x)
            return true;
        else if (arr[mid] < x)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return false;
}

int main() {
    int size, x;
    printf("Enter size of the array: ");
    scanf("%d", &size);

    int arr[size];
    printf("Enter elements of the sorted array: ");
    for (int i = 0; i < size; i++)
        scanf("%d", &arr[i]);

    printf("Enter the value of x: ");
    scanf("%d", &x);

    int lower = lowerb(arr, size, x);
    int upper = upperb(arr, size, x);
    bool present = is_present(arr, size, x);

    if (lower != -1)
        printf("Lower bound of %d is at index: %d\n", x, lower);
    else
        printf("No lower bound found for %d\n", x);

    if (upper != -1)
        printf("Upper bound of %d is at index: %d\n", x, upper);
    else
        printf("No upper bound found for %d\n", x);

    if (present)
        printf("True");
    else
        printf("False");

    return 0;
}
