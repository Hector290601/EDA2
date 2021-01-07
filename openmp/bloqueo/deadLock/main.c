#include <stdio.h>
#include <omp.h>
#define N 100

int main(){
	int A[N], B[N], i, threads;
	omp_lock_t locka, lockb;
	#pragma omp sections nowait
	{
		printf("Section one");
		#pragma omp section
		{
			omp_set_lock(&locka);
			printf("init a\n");
			for(i = 0; i < N; i++){
				A[i] = i;
			}
			omp_set_lock(&lockb);
			printf("init b\n");
			for(i = 0; i < N; i++){
				B[i] = N - A[i];
			}
			omp_unset_lock(&lockb);
			omp_unset_lock(&locka);
		}
		#pragma omp section
		{
			printf("Section two\n");
			omp_set_lock(&lockb);
			printf("Modify b\n");
			for(i = 0; i < N; i++){
				B[i] = N-i;
			}
			omp_set_lock(&locka);
			printf("Modify a\n");
			for(i = 0; i < N; i++){
				A[i] = B[i] + i;
			}
			omp_unset_lock(&locka);
			omp_unset_lock(&lockb);
		}
	}
	return 0;
}
