#include <stdio.h>
#include <omp.h>

int main(void){
        int mainId = omp_get_thread_num();
        printf("Main id: %d\n", mainId);
        #pragma omp parallel
        {
                int id = omp_get_thread_num();
                printf("Hola(%d)\n", id);
                printf("mundo(%d)\n", id);
        }
        return 0;
}
