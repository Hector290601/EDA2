#include <stdio.h>
#include <omp.h>

float bigJob(int i){
  printf("i: %d\n", i);
  return (float) i;
}

float consume(float b){
  printf("b: %f\n", b);
  return (float)b;
}

int main(){
  int niters = 10;
  float res = 0.0;
  #pragma omp parallel
  {
    float B;
    int i, id, nthrds;
    id = omp_get_thread_num();
    nthrds = omp_get_num_threads();
    for(i = id; i<niters; i+=nthrds){
      B=bigJob(i);
      #pragma omp critical
      res += consume(B);
    }
    printf("res= %f\n", res);
  }
  return 0;
}
