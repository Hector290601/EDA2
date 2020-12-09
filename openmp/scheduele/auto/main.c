#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <unistd.h>

#define THREADS 4
#define N 8

int main(void){
	int i;
	#pragma omp parallel for schedule(auto) num_threads(THREADS)
		for(i = 0; i<N; i++){
			sleep(i);
			printf("Thread: %d, Itertion: %d.\n", omp_get_thread_num(), i);
		}
	return 0;
}
