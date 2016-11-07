#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "backgroundfunctions.h"
#include <gsl/gsl_blas.h>

double* leapfrog(double* start, double R, double G, int steps, double h) {
   double** values = create2DArray(4,steps);
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }

   double identity[] = {1.0,0.0,0.0,0.0,
                        0.0,1.0,0.0,0.0,
                        0.0,0.0,1.0,0.0,
                        0.0,0.0,0.0,1.0};
   double function[] = {0.0,0.0,1.0,0.0,
                        0.0,0.0,0.0,1.0,
                        -(R+1),R,-G,0.0,
                        R+1,-(R+1),G*(1-(1/R)),-G/R};
   double* matrix = create1DArray(16);
   double* matrix_euler = create1DArray(16);
   for (int i = 0; i < 4; i++) {
      matrix[i] = h*function[i];
      matrix_euler[i] = identity[i] + h*function[i];
   }

   for(int j = 0; j < 4; j++) {values[j][0] = start[j];}
   double* prev_i = create1DArray(2);
   double * x_i  = vector4MatrixOp(matrix_euler, start);
   for(int j = 0; j < 4; j++) {values[j][1] = x_i[j];}
   for (int i = 2; i < steps; i++){
      double* prev = create1DArray(4);
      for(int j = 0; j < 4; j++) {prev[j] = values[j][i-2];}
      double* vector = create1DArray(4);
      for(int j = 0; j < 4; j++) {vector[j] = values[j][i-1];}
      double* x = vectorMatrixOp(matrix,vector);
      for(int j = 0; j < 4; j++) {values[j][i] = 2*x[j] + prev[j];}
   }
   return values[0];
}

double** rk4(double* start, double R, double G, int steps, double h) {
   double** values = create2DArray(4,steps);
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }

   double function[] = {0.0,0.0,1.0,0.0,
                        0.0,0.0,0.0,1.0,
                        -(R+1),R,-G,0.0,
                        R+1,-(R+1),G*(1-(1/R)),-G/R};
   double* matrix = create1DArray(16);
   for (int i = 0; i < 16; i++) {
      matrix[i] = function[i];
   }

   for(int j = 0; j < 4; j++) {values[j][0] = start[j];}

   for (int i = 1; i < steps; i++){
      double** k = create2DArray(4,4);
      double* prev_i = create1DArray(4);
      for(int j = 0; j < 4; j++) {prev_i[j] = values[j][i-1];}
      double* x_i = vector4MatrixOp(matrix,prev_i);
      for(int j = 0; j < 4; j++) {k[j][0] = h*x_i[j];}
      double* prev_ii = create1DArray(4);
      for(int j = 0; j < 4; j++) {
         prev_ii[j] = values[j][i-1] + 0.5*k[j][0];
      }
      double* x_ii = vector4MatrixOp(matrix, prev_ii);
      for(int j = 0; j < 4; j++) {k[j][1] = h*x_ii[j];}
      double* prev_iii = create1DArray(4);
      for(int j = 0; j < 4; j++) {
         prev_iii[j] = values[j][i-1] + 0.5*k[j][1];
      }
      double* x_iii = vector4MatrixOp(matrix, prev_iii);
      for(int j = 0; j < 4; j++) {k[j][2] = h*x_iii[j];}
      double* prev_iv = create1DArray(4);
      for(int j = 0; j < 4; j++) {
         prev_iv[j] = values[j][i-1] + k[j][2];
      }
      double* x_iv = vector4MatrixOp(matrix, prev_iv);
      for(int j = 0; j < 4; j++) {k[j][3] = h*x_iv[j];}

      for(int j = 0; j < 4; j++) {
         values[j][i] = prev_i[j] + (k[j][0] + 2*k[j][1] + 2*k[j][2] + k[j][3])/6.0;
      }
   }
   return values;
}
