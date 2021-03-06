#include <stdio.h>
#include <omp.h>

void func(){
	int tmp = 2;
	#pragma omp parallel for private(tmp)
	for(int j = 0; j < 10; ++j){
		printf("%d:%d\n", omp_get_thread_num(), tmp);
		tmp += j;
	}
	printf("%d\n", tmp);
}

int main(){
	printf("Private\n");
	func();
	return 0;
}
