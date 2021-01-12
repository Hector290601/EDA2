#include <stdio.h>
#include <omp.h>

int counter = 0;

#pragma omp threadprivate(counter)

int incrementCounter(){
	return counter++;
}

int main(){
	printf("%d\n", counter);
	#pragma omp parallel
	{
		printf("%d\n", incrementCounter());
	}
	return 0;
}
