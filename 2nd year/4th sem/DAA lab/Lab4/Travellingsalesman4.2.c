#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
 
#define N 5
 
void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
 
int calculateDistance(int graph[N][N], int tour[N]){
    int total_distance = 0;
    int i=0;
    for(i=0; i<N-1;i++)
        total_distance += graph[tour[i]][tour[i+1]];
 
    total_distance += graph[tour[N-1]][tour[0]];
    return total_distance;
}
 
void tsp(int graph[N][N]) {
    int min_distance = INT_MAX;
    int min_tour[N];
    int i=0;
    int j;
    int tour[N];
    for( i=0; i<N; i++) tour[i] = i;
 
    clock_t start_time = clock();
    long long op_count = 0;
    do{
        int distance = calculateDistance(graph, tour);
        op_count++;
        if (distance < min_distance){
            min_distance = distance;
            for(i=0;i<N;i++) min_tour[i] = tour[i];
        }
    } while(next_permutation(tour, N));
    clock_t end_time = clock();
 
    printf("Input: \n");
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    printf("Shortest distance: %d\n", min_distance);
    printf("Shortest tour: ");
    for(i=0;i<N;i++) printf("%d ", min_tour[i]);
    printf("\n");
    printf("Time taken to process: %f seconds\n", (double)(end_time - start_time) / CLOCKS_PER_SEC);
    printf("Operation count: %lld\n", op_count);
 
    return;
}
 
//function to generate the next lexicographically greater permutation
void reverse(int a[], int i) {
    int j = N - 1;
    while (i < j) {
        swap(&a[i], &a[j]);
        i++;
        j--;
    }
}
 
int next_permutation(int a[], int n) {
    int i, j;
 
    for(i = n-2; i >= 0; i--) {
        if (a[i] < a[i+1])
            break;
    }
 
    if (i < 0)
        return 0;
 
    for(j = n-1; j > i; j--) {
        if(a[j] > a[i])
            break;
    }
 
    swap(&a[i], &a[j]);
 
    reverse(a, i + 1);
 
    return 1;
}
 
int main(){
    int graph[N][N];
    srand(time(NULL));
    int i, j;
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            if(i==j) graph[i][j] = 0;
            else graph[i][j] = rand() % 100;
        }
    }
 
    tsp(graph);
 
    return 0;
}
