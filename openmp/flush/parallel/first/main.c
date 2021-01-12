#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#define N 10

double* A;

void fillRand(){
	for(int i = 0; i < N; i ++){
		A[i] = rand()%N;
	}
}

double sumArray(){
	double sum;
	for(int i = 0; i < N; i++){
		sum += A[i];
	}
	return sum;
}

int main(){
	double sum, runtime;
	int flag = 0;
	A = (double *) malloc(N*sizeof(double));
	runtime = omp_get_wtime();
	#pragma omp parallel sections num_threads(2)
	{
		#pragma omp section
		{
			fillRand();
			#pragma omp flush		//flush the array (espera a que termine la función anterior)
			flag = 1;
			#pragma omp flush(flag)
		}
		#pragma omp section
		{
			#pragma omp flush(flag)
			while(flag == 0){
				#pragma omp flush(flag)
			}
			#pragma omp flush
			sum = sumArray();
		}
	}
	runtime = omp_get_wtime() - runtime;
	printf("Sum = %lf\nRuntime = %lf\n", sum, runtime);
	return 0;
}
