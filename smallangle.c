#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "backgroundfunctions.h"
#include <gsl/gsl_blas.h>

double* eulerForward(double* start, double D, int steps, double h) {
   double** values = create2DArray(2,steps);
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }

   double identity[] = {1.0,0.0,0.0,1.0};
   double function[] = {0.0,1.0,-1.0,-D};
   double* matrix = create1DArray(4);
   for (int i = 0; i < 4; i++) {
      matrix[i] = identity[i] + h*function[i];
   }

   values[0][0] = start[0];
   values[1][0] = start[1];
   for (int i = 1; i < steps; i++){
      double* prev = create1DArray(2);
      prev[0] = values[0][i-1];
      prev[1] = values[1][i-1];
      double* x = vectorMatrixOp(matrix,prev);
      values[0][i] = x[0];
      values[1][i] = x[1];
   }
   return values[0];
}
