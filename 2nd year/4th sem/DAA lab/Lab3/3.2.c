#include<stdio.h>
#include<time.h>
#include<stdlib.h>

unsigned int opcount= 0;
void selectionsort(int arr[], int n){
    int i ,j, temp, minindex;
    for(i=0;i<n-1; i++){
            minindex = i;
        for(j=i+1;j<n-i;j++){
           if(arr[j] <arr[minindex]){
                opcount++;
                minindex = j;
           }

        }
        if (minindex != i){
            opcount++;
        int temp = arr[i];
        arr[i] = arr[minindex];
        arr[minindex]= temp;


    }
    }
}




int main(){
    long long int n;

    clock_t start, endl;
  double cpu_time;
    printf("Enter size of array: ");
    scanf("%d", &n);
    srand(time(NULL));
    int arr1[n];
    printf("Enter elements: \n");
    for(int i=0; i<n; i++)
        //arr1[i] = (rand()%1000) +1;
        scanf("%d", &arr1[i]);
    start = clock();
    selectionsort(arr1, n);
    endl = clock();
    cpu_time = (double)(endl-start)/CLOCKS_PER_SEC;
    for(int i=0; i<n; i++)
        printf("%d ", arr1[i]);

    printf("%e    %d", cpu_time, opcount);

    return 0;
}
