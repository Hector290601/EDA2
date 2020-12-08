#include <stdio.h>
#include <omp.h>

static long numSteps=10000000;
double step;

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
		for(i = 0; i <= (int)numSteps/thNums; i++){
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

