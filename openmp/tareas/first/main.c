#include <stdio.h>
#include <omp.h>

int flag = 0;

void doIt(){
	printf("doIt task: id:%d; flagNxt: %d; flag: %d\n", omp_get_thread_num(), omp_get_thread_num(), flag);
	flag = omp_get_thread_num();
}

void endIt(){
	printf("endIt task: id: %d; flag: %d\n", omp_get_thread_num(), flag);
	flag = 1;
}

int main(){
	#pragma omp parallel
	{
		#pragma omp task
			doIt();
		#pragma omp barrier
		#pragma omp single
		{
			#pragma omp task
				endIt();
		}
	}
	printf("Final flag: %d\n", flag);
	return 0;
}
