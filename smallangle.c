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

   double a[] = {0.11,0.12,0.13,0.21,0.22,0.23};
   double b[] = { 1011, 1012,1021, 1022,1031, 1032 };
   double c[] = { 0.00, 0.00,0.00, 0.00 };
   gsl_matrix_view A = gsl_matrix_view_array(a, 2, 3);
   gsl_matrix_view B = gsl_matrix_view_array(b, 3, 2);
   gsl_matrix_view C = gsl_matrix_view_array(c, 2, 2);
   gsl_blas_dgemm (CblasNoTrans, CblasNoTrans,1.0, &A.matrix, &B.matrix,0.0, &C.matrix);
   printf ("[ %g, %g\n", c[0], c[1]);
   printf ("  %g, %g ]\n", c[2], c[3]);

   return matrix[0];
}
