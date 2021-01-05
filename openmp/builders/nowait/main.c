#include <stdio.h>
#include <unistd.h>
#include <omp.h>

#define TAM 12
#define THN 12


int work1(int id){
	sleep(id);
	return (int)(id%10);
}

int work2(int id, int* A){
	sleep(id);
	int res = 0;
	for(int i = 0; i<= id; i++){
		res += A[i];
	}
	return res;
}

int work3(int* C, int id){
	return (int)(id);
}

int work4(int id){
	sleep(id);
	return 0;
}
int main(){
	int A[THN + 1], B[TAM + 1], C[TAM + 1], id;
	omp_set_num_threads(THN);
	#pragma omp parallel shared(A, B, C), private(id)
	{
		int i;
		id = omp_get_thread_num();
		A[id] = work1(id);
		printf("Thread %d finish work1\n", id);
		#pragma omp barrier
		#pragma omp for
		for(i = 0; i<TAM; i++){
			C[i] = work2(i, A);
		}
		printf("Thread %d finish work2\n", id);
		#pragma omp for nowait
		for(i = 0; i < TAM; i++){
			B[i] = work3(C, i);
		}
		printf("Thread %d finish work3\n", id);
		A[id] = work4(id);
		printf("Thread %d finish work4\n", id);
	}
	return 0;
}
