#include <math.h>
#include <stdlib.h>
#include <stdio.h>

double** create2DArray(int rows, int columns) {
   double** array;
   array = malloc(rows*sizeof(double*));
   for (int i = 0; i < rows; i++) {
      array[i] = malloc(columns*sizeof(double));
   }
   return array;
}

double* create1DArray(int columns) {
   double* array;
   array = malloc(columns*sizeof(double));
   return array;
}

double *ser(int i, int max) {
   double** values = create2DArray(2,max);
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }
   for (i = 0; i < max; i++){
      values[0][i] = (double)i;
      values[1][i] = (double)(i+1);
   }
   return values[0];
}
