#include <stdio.h>
#include <omp.h>
#define NUM_THREADS 12
static long numSteps=10000000;
double step;

int main(){
	double start = omp_get_wtime();
	int i = 0;
	int thNums = omp_get_num_threads();
	double x, pi, sum = 0.0;
	step = 1.0/(double)numSteps;
	#pragma opm parallel
	{
		int i, id, nthrds;
		double x, sum = 0.0;
		id = omp_get_thread_num();
		nthrds = omp_get_num_threads();
		for(i = id; i <= numSteps; i+=nthrds){
			x = (i+0.5)*step;
			sum += 4.0/(1.0+x*x);
		}
		sum *= step;
		#pragma omp atomic
			pi += sum;
	}
	double end = omp_get_wtime();
	double time = end - start;
	printf("Time: %f\n", time);
	printf("Pi = %f\n", pi);
	return 0;
}
