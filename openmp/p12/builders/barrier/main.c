#include <stdio.h>
#include <omp.h>
#include <unistd.h>
#define NUM_THREADS 4

int big_call1(int id){
  sleep(id);
  printf("Big Call1 %d\n", id);
  return id;
}

int big_call2(int id){
  sleep(id);
  printf("Big Call2 %d\n", id);
  return id;
}

int main(){
  omp_set_num_threads(NUM_THREADS);
  int A[NUM_THREADS], B[NUM_THREADS], id;
  #pragma omp parallel
  {
    id = omp_get_thread_num();
    A[id] = big_call1(id);
    #pragma omp barrier
    B[id] = big_call2(id);
  }
}

