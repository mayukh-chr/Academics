#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
#define MAX_N 10


 
int cost_matrix[MAX_N][MAX_N];
int best_assignment[MAX_N];
int min_cost = 1e9;
 
void init_cost_matrix(int n) {
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cost_matrix[i][j] = rand() % 100;
        }
    }
}
 
void print_cost_matrix(int n) {
    printf("Cost matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", cost_matrix[i][j]);
        }
        printf("\n");
    }
}
 
void assign(int n, int worker, int *assignment, int cost, int *opcount) {
    (*opcount)++;
    if (worker == n) {
        if (cost < min_cost) {
            min_cost = cost;
            for (int i = 0; i < n; i++) {
                best_assignment[i] = assignment[i];
            }
        }
        return;
    }
    for (int i = 0; i < n; i++) {
        if (assignment[i] == -1) {
            assignment[i] = worker;
            assign(n, worker + 1, assignment, cost + cost_matrix[worker][i], opcount);
            assignment[i] = -1;
        }
    }
}
 
int main() {
    int n = 5;
    init_cost_matrix(n);
    print_cost_matrix(n);
    int assignment[MAX_N];
    for (int i = 0; i < n; i++) {
        assignment[i] = -1;
    }
    int opcount = 0;
    clock_t start = clock();
    assign(n, 0, assignment, 0, &opcount);
    clock_t end = clock();
    double time_taken = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Best assignment: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", best_assignment[i]);
    }
    printf("\nMinimum Cost: %d\n", min_cost);
    printf("Time taken: %f seconds\n", time_taken);
    printf("Number of operations: %d\n", opcount);
    return 0;
}
