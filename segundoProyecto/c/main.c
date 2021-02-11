#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <omp.h>
#include <string.h>
#define THRS 12

long double factorialSerial(int n){
	long double fact = 1;
	for(int i = 1; i <= n; i++){
		fact *= i;
	}
	return fact;
}

long double factorialParalelo(int n){
	long double fact[THRS], factorial = (long double) 1;
	int i = 1;
	omp_set_num_threads(THRS);
	#pragma omp parallel for
	for(i = 1; i <= n; i++){
		fact[omp_get_thread_num()] = 1;
	}
	#pragma omp parallel for
	for(i = 1; i <= n; i++){
		fact[omp_get_thread_num()] *= i;
	}
	for(int i = 0; i < THRS; i++){
		factorial *= fact[i];
	}
	return factorial;
}

long double eulerSerial(int n){
	long double e = (long double) 0, div = (long double) 0, f = (long double) 0;
	for(int i = 0; i <= n; i++){
		f = factorialSerial(i);
		div = 1 / f;
		e += div;
	}
	return e;
}

long double eulerParalelo(int n){
	long double eArr [THRS], e = (long double) 0;
	int i = 0;
	#pragma omp parallel for
	for(i = 0; i < THRS; i++){
		eArr[i] = 0;
	}
	#pragma omp parallel for
	for(i = 0; i <= n; i++){
		long double div = (long double) 0, f = (long double) 0;
		f = factorialSerial(i);
		div = 1 / f;
		e += div;
	}
	for(i = 0; i < THRS; i++){
		e += eArr[i];
	}
	return e;
}

long double serial(int n){
	long double e = (double) 0.0, start, end;
	e = eulerSerial(n);
	return e;
}

int main(){
	long double e = 0.0, start, end;
	int size = 10;
	FILE* file = NULL;
	char *data, arr[sizeof(long double)];
	file = fopen("../dataC.csv", "w+");
	data = (char*) malloc(sizeof(char) * 5000000);
	fgets(data, 30, file);
	if(file != NULL){
		for(int i = 1; i <= 10000; i+=1){
			size = i;
			start = omp_get_wtime();
			e = eulerSerial(size);
			end = omp_get_wtime() - start;
			snprintf(arr, 50, "%Lf", e);
			strcat(data, arr);
			strcat(data, ",");
			snprintf(arr, 50, "%Lf", end);
			strcat(data, arr);
			strcat(data, ",");
			snprintf(arr, 50, "%d", size);
			strcat(data, arr);
			strcat(data, ",");
			strcat(data, "\n");
			start = omp_get_wtime();
			e = eulerParalelo(size);
			end = omp_get_wtime() - start;
			snprintf(arr, 50, "%Lf", e);
			strcat(data, arr);
			strcat(data, ",");
			snprintf(arr, 50, "%Lf", end);
			strcat(data, arr);
			strcat(data, ",");
			snprintf(arr, 50, "%d", size);
			strcat(data, arr);
			strcat(data, ",");
			strcat(data, "\n");
			printf("C: %d\n", i);
		}
		fputs(data, file);
	}
	return 0;
}
