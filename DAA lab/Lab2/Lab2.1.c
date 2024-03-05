#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

int gcd(int m, int n) {
  int t = m > n ? n: m;
  int opcount = 0;
  while(m % t != 0 || n % t != 0) {
    opcount++;
    t--;
  }
  printf("Number of operations : %d\n", opcount);
  return t;
}

int main() {
  int n, m;
  printf("Enter m: ");
  scanf("%d", &n);
  printf("Enter n: ");
  scanf("%d", &m);
  clock_t start, endl;
  double cpu_time;
  start = clock();
  printf("The GCD of a %d and %d is %d", m, n, gcd(m, n));
  endl = clock();
  cpu_time = (double)(endl-start)/CLOCKS_PER_SEC;
  printf("\n time taken: %e", cpu_time);
  return 0;
}
