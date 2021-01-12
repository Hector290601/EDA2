#include <stdio.h>
#include <omp.h>
#define MAX 5

int main(){
	double ave = 0.0, A[MAX];
	int i;
	for(i = 0; i < MAX; i++){
		A[i] = i+1.0;
	}
	#pragma omp parallel for
	for(i = 0; i < MAX; i++){
		ave += A[i];
	}
	ave /= MAX;
	printf("%f\n", ave);
	return 0;
}
