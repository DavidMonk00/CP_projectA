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

double* eulerForward(double D, int steps) {
   double** values = create2DArray(2,steps);
   double** matrix = create2DArray(2,2);
   static double matrix_vals[4] = {1.0,5.0,-1.0,4.0};
   for (int j = 0; j < 2; j++) {
      for (int k = 0; k < 2; k++) {
         matrix[j][k] = matrix_vals[2*j + k];
      }
      matrix[j/2][j%2] = matrix_vals[j];
   }
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }
   for (int i = 0; i < steps; i++){
      values[0][i] = (double)i;
      values[1][i] = (double)(i+1);
   }
   return matrix[0];
}
