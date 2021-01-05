#include <stdio.h>
#include <omp.h>
#include <unistd.h>

void sectionA(int id){
	printf("Section A thread %d\n", id);
	sleep(id);
}

void sectionB(int id){
	printf("Section B thread %d\n", id);
	sleep(id);
}

void sectionC(int id){
	printf("Section C thread %d\n", id);
	sleep(id);
}

int main(){
	#pragma omp parallel
	{
		int id;
		#pragma omp sections
		{
			#pragma omp section
			sectionA(omp_get_thread_num());
			#pragma omp section
			sectionB(omp_get_thread_num());
			#pragma omp section
			sectionC(omp_get_thread_num());
		}
		id = omp_get_thread_num();
		printf("Parallel block thread %d\n", id);
	}
	return 0;
}
