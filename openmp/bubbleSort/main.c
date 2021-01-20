#include <stdio.h>
#include <omp.h>

#define TAM 2

int RA = TAM, CA = TAM, RB = TAM, CB = TAM;

void multiply(int a[RA][CA], int b[RB][CB], int c[RA][CB]){
	printf("C:\n");
	for(int i = 0; i < RA; i++){
		for(int j = 0; j < CB; j ++){
			for(int k = 0; k < CA; k++){
				c[i][j] += a[i][k] * b[k][j];
				printf("%d", c[i][j]);
				if(j+1 < TAM){
					printf(" , ");
				}else{
					printf("\n");
				}
			}
		}
	}
}

int main(){
	int a[RA][CA], b[RB][CB], c[RA][CB], cnt = 0;
	for(int i = 0; i < TAM; i++){
		for(int j = 0; j < TAM; j++){
			a[i][j] = cnt;
			b[i][j] = 4 + cnt;
			c[i][j] = 0;
			cnt+=1;
		}
	}
	printf("A:\n");
	for(int i = 0; i < TAM; i++){
		for(int j = 0; j < TAM; j++){
			printf("%d", a[i][j]);
			if(j+1 < TAM){
				printf(" , ");
			}else{
				printf("\n");
			}
		}
	}
	printf("B:\n");
	for(int i = 0; i < TAM; i++){
		for(int j = 0; j < TAM; j++){
			printf("%d", b[i][j]);
			if(j+1 < TAM){
				printf(" , ");
			}else{
				printf("\n");
			}
		}
	}
	printf("C:\n");
	for(int i = 0; i < TAM; i++){
		for(int j = 0; j < TAM; j++){
			printf("%d", c[i][j]);
			if(j+1 < TAM){
				printf(" , ");
			}else{
				printf("\n");
			}
		}
	}
	multiply(a, b, c);
	return 0;
}

