// quick sort algorithm in c
#include<stdio.h>
void swap(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
int partition(int arr[],int l,int h){
    int pivot=arr[l];
    int i=l,j=h;
    do{
        do{i++;}while(arr[i]<=pivot);
        do{j--;}while(arr[j]>pivot);
        if(i<j){
            swap(&arr[i],&arr[j]);
        }
    }while(i<j);
    swap(&arr[l],&arr[j]);
    return j;
}
void quickSort(int arr[],int l,int h){
    int j;
    if(l<h){
        j=partition(arr,l,h);
        quickSort(arr,l,j);
        quickSort(arr,j+1,h);
    }
}
int main(){
    int n, i;
    printf("Enter size of array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter array elements: ");
    for(i=0;i<n;i++)
        scanf("%d", &arr[i]);
    quickSort(arr,0,n);
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    return 0;
}
// Time Complexity: O(nlogn)