#include<stdio.h>


void bubblesort(int arr[], int n){
    int i ,j, temp;
    for(i=0;i<n-1; i++){
        for(j=0;j<n-i-1;j++){
           if(arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
           }
        }
    }
}

int main(){
    int n;
    printf("Enter size of array: ");
    scanf("%d", &n);

    int arr1[n];
    printf("Enter elements: \n");
    for(int i=0; i<n; i++)
        scanf("%d", &arr1[i]);

    bubblesort(arr1, n);

    for(int i=0; i<n; i++)
        printf("%d ", arr1[i]);

    return 0;
}
