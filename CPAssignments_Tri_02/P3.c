
#include <stdio.h>

void mergesort(int ar1[], int ar2[], int size1, int size2) {
    int mergedarray[size1 + size2];
    int i = 0, j = 0, k = 0;

    while (i < size1 && j < size2) {
        if (ar1[i] < ar2[j])
            mergedarray[k++] = ar1[i++];
        else
            mergedarray[k++] = ar2[j++];
    }

    while (i < size1)
        mergedarray[k++] = ar1[i++];
    while (j < size2)
        mergedarray[k++] = ar2[j++];
    for (int m = 0; m < size1 + size2; m++)
        printf("%d ", mergedarray[m]);
}

int main() {
    int size1, size2;
    scanf("%d", &size1);  //array 1 size

    int ar1[size1];
    for (int i = 0; i < size1; i++)
        scanf("%d", &ar1[i]);

    scanf("%d", &size2);   //array 2 size
  
    int ar2[size2];
    for (int i = 0; i < size2; i++)
        scanf("%d", &ar2[i]);

    mergesort(ar1, ar2, size1, size2);

    return 0;
}