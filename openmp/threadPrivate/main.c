#include <stdio.h>
#include <omp.h>

int counter = 1;

#pragma omp threadprivate(counter)

int incrementCounter(){
	return counter+=1;
}

void incrementCounter2(){
	counter += omp_get_thread_num() + 2;
}

int main(){
	printf("counter: %d\n", counter);
	#pragma omp parallel
	{
		incrementCounter2();
		printf("id: %d; counter: %d\n", omp_get_thread_num(), counter);
	}
	printf("counter: %d\n", counter);
	return 0;
}
