#include <stdio.h>
#include <omp.h>

double getNumber(int id){
  return (double)(id%10);
}

double funcBig(double b){
  if(b != (double)0){
    return (double)(10%((int)b));
  }else{
    return 1;
  }
}

int main(){
  double A = 0, C = 0;
  #pragma omp parallel
  {
    double tmp, B;
    int id;
    id = omp_get_thread_num();
    B = getNumber(id);
    tmp = funcBig(B);
    C += tmp;
    printf("tmp: %f\n", tmp);
    #pragma omp atomic
    A+=tmp;
  }
  printf("A: %f\n", A);
  printf("C: %f\n", C);
  return 0;
}
