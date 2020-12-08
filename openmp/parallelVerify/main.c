#include <stdio.h>
#include <omp.h>

int main(){
	omp_set_dynamic(0);
	int procs = omp_get_num_procs();
	printf("Procesadores: %d\n", procs);
	printf("Numero de hilos: %d", omp_get_max_threads());
	omp_set_num_threads(procs);
	printf("En paralelo: %d\n", omp_in_parallel());
	#pragma omp parallel
	{
		int ths = omp_get_num_threads();
		printf("Hilos: %d\n", ths);
		int id = omp_get_thread_num();
		printf("Hilo actual: %d\n", id);
		printf("En paralelo: %d\n", omp_in_parallel());
	}
}
