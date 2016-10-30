#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "backgroundfunctions.h"
#include <gsl/gsl_blas.h>

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
   double a[] = {0.0,1.0,-1.0,D};
   double b[] = { 5.1, 2.3};

   double* x = vectorMatrixOp(a,b);
   printf ("[ %g\n", x[0]);
   printf ("  %g]\n", x[1]);

   return matrix[0];
}
