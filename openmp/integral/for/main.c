#include <stdio.h>
#include <omp.h>

static long numSteps = 1000000000;
double step;

/*
int main(){
	int i;
	double x, pi, sum = 0.0;
	step = 1.0/(double)numSteps;
	for(i =0; i < numSteps; i++){
		x = (i+0.5)*step;
		sum = sum + 4.0/(1.0+x*x);
	}
	pi = step*sum;
	printf("Pi: %f\n", pi);
	return 0;
}
*/

int main(){
	int i;
	float init, end;
	double pi, sum = 0.0, x;
	step = 1.0/(double)numSteps;
	init = omp_get_wtime();
	#pragma omp parallel for reduction(+:sum) private(x)
	for(i =0; i < numSteps; i++){
		//double x;
		x = (i+0.5)*step;
		sum = sum + 4.0/(1.0+x*x);
	}
	end = omp_get_wtime() - init;
	pi = step*sum;
	printf("Pi: %f\n%f s\n", pi, end);
	return 0;
}
