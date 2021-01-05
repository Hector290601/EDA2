#include <stdio.h>
#include <omp.h>
#define NUM_THREADS 2
static long numSteps=10000000;
double step;

int main(){
	int i, nthreads;
	double pi, sum[NUM_THREADS], initTime, finishTime;
	step = 1.0/(double)numSteps;
	initTime = omp_get_wtime();
	omp_set_num_threads(NUM_THREADS);
	#pragma omp parallel
	{
		int i, id, nthrds;
		double x;
		id = omp_get_thread_num();
		nthrds = omp_get_num_threads();
		if(id == 0){
			nthreads = nthrds;
		}
		for(i = id, sum[id] = 0.0; i<numSteps; i+=nthrds){
			x = (i+0.5)*step;
			sum[id] += 4.0/(1.0+x*x);
		}
	}
	for(i = 0, pi = 0.0; i < nthreads; i++){
		pi += sum[i]*numSteps;
	}
	finishTime = omp_get_wtime() - initTime;
	printf("PI: %f\n", pi);
	printf("Time: %f\n", finishTime);
	return 0;
}


/*
int main(){
	double start = omp_get_wtime();
	int i = 0;
	int thNums = omp_get_num_threads();
	double x, pi, suma[thNums], sum = 0.0;
	step = 1.0/(double)numSteps;
	for(i = 0; i< thNums; i++){
		suma[i] = 0;
	}
	#pragma opm parallel
	{
		for(i = omp_get_thread_num(); i <= (int)numSteps/thNums; i++){
			x = (i+0.5)*step;
			suma[omp_get_thread_num()] = suma[omp_get_thread_num()] + 4.0/(1.0+x*x);
		}
	}
	for(i = 0; i < thNums; i++){
		sum += suma[i];
	}
	pi = step * sum;
	double end = omp_get_wtime();
	double time = end - start;
	printf("Time: %f\n", time);
	printf("Pi = %f\n", pi);
	return 0;
}
*/
