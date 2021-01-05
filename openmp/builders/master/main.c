#include <stdio.h>
#include <omp.h>
#include <unistd.h>
#define NUM_THREADS 256

int main(){
  omp_set_num_threads(NUM_THREADS);
  int id;
  #pragma omp parallel
  {
	#pragma omp master
	{
		id = omp_get_thread_num();
		printf("Master block thread %d \n", id);
	}
	id = omp_get_thread_num();
	printf("Parallel block thread %d\n", id);
  }
}

