#include <stdio.h>
#include <omp.h>
#include <unistd.h>
#define TAM 5

int work1(int id){
  sleep(id);
  return id;
}

int work2(int i, int* A){
  sleep(i);
  return A[i];
}

int work3(int* C, int i){
  return (C[i]) + i;
}

int work4(int id){
  return 0-id;
}

int main(){
  int arrayLen;
  arrayLen = omp_get_num_threads();
  int A[arrayLen], B[arrayLen], C[arrayLen], id, i;
  #pragma omp parallel shared(A, B, C) private(id)
  {
    id = omp_get_thread_num();
    A[id] = work1(id);
    printf("Thread %d finish work1\n", id);
    #pragma omp barrier
    #pragma omp for
    for(i = 0; i<TAM; i++){
      C[i] = work2(i, A);
    }
    printf("Thread %d finish work2\n", id);
    #pragma omp nowait
    for(i = 0; i < TAM; i++){
      B[i] = work3(C, i);
    }
    printf("Thread %d finish work3\n", id);
    A[id] = work4(id);
    printf("Thread %d finish work4\n", id);
  }
  return 0;
}
