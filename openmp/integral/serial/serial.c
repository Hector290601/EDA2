#include <stdio.h>
#include <omp.h>

static long numSteps=10000000;
double step;

int main(){
	double start = omp_get_wtime();
	int i;
	double x, pi, sum = 0.0;
	step = 1.0/(double)numSteps;
	for(i = 0; i < numSteps; i++){
		x = (i+0.5)*step;
		sum = sum + 4.0/(1.0+x*x);
	}
	pi = step * sum;
	double end = omp_get_wtime();
	double time = end - start;
	printf("Time: %f\n", time);
	printf("Pi = %f\n", pi);
	return 0;
}

