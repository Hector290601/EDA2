#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <unistd.h>
#define NUM_VALUES 20

int NUM_BUCKETS = 0;

int takeNumber(){
	return rand()%NUM_BUCKETS;
}

int main(){
	int i;
	omp_set_dynamic(0);
	NUM_BUCKETS = omp_get_num_procs();
	omp_set_num_threads(NUM_BUCKETS);
	printf("Buckets: %d\n", NUM_BUCKETS);
	omp_lock_t hist_locks[NUM_BUCKETS];
	int hist[NUM_BUCKETS];
	#pragma omp parallel for
	for(i = 0; i < NUM_BUCKETS; i++){
		omp_init_lock(&hist_locks[i]);
		hist[i] = 0;
	}
	#pragma omp parallel for
	for(i = 0; i < NUM_VALUES; i++){
		int id = omp_get_thread_num();
		printf("Thread: %d\n", id);
		int val = takeNumber();
		omp_set_lock(&hist_locks[id]);
		hist[val] ++;
		omp_unset_lock(&hist_locks[id]);
	}
	for(i = 0; i < NUM_BUCKETS; i++){
		printf("hist[%d] = %d\n", i, hist[i]);
		omp_destroy_lock(&hist_locks[i]);
	}
	return 0;
}
