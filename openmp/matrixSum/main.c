#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#define NTH 2

int main(){
	int A [2][2] = {1, 2, 3, 4}, B[2][2] = {5, 6, 7, 8}, C[2][2] = {0, 0, 0, 0};
	int id;
	omp_set_num_threads(NTH);
	#pragma omp parallel
	{
		id = omp_get_thread_num();
		#pragma omp for
			for(int i = 0; i < 2; i++){
				for(int j = 0; j < 2; j++){
					C[i][j]+= A[i][j] + B[i][j];
				}
			}
	}
	printf("Suma:\n");
	for(int i = 0; i < 2; i++){
		for(int j = 0; j < 2; j++){
			printf("%d, ", C[i][j]);
		}
		printf("\n");
	}
	return 0;
}
