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

   int i, j;
   gsl_matrix * m = gsl_matrix_alloc (10, 3);
   for (i = 0; i < 10; i++){
      for (j = 0; j < 3; j++){
         gsl_matrix_set (m, i, j, 0.23 + 100*i + j);
      }
   }
   for (i = 0; i < 10; i++){
      for (j = 0; j < 3; j++){
         printf ("m(%d,%d) = %g\n", i, j, gsl_matrix_get (m, i, j));
      }
   }
   gsl_matrix_free (m);

   return matrix[0];
}
