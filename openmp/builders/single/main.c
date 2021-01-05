#include <stdio.h>
#include <omp.h>
#include <unistd.h>
#define NUM_THREADS 24

int main(){
	omp_set_num_threads(NUM_THREADS);
	int id;
	#pragma omp parallel
	{
		#pragma omp single
		{
			id = omp_get_thread_num();
			printf("Single block thread %d \n", id);
		}
	id = omp_get_thread_num();
	printf("Parallel block thread %d\n", id);
  }
}

