/* 20161104
 * David Monk
 *
 * This file contains the numerical methods used to approximate the
 * motion of a single pendulum. Each returns a two-dimensional pointer
 * array of the postion and velocity at each timestep.
 */

#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "backgroundfunctions.h"
#include <gsl/gsl_blas.h>

/* Function: eulerForward
 * ------------------------
 * Implements the Euler forward method for a single pendulum
 *
 * start:   one-dimensional array of length 2 (position,velocity)
 * D:       damping coefficient
 * steps:   number of steps for the iteration
 * h:       timestep of method
 *
 * returns: two-dimensional array of positions and velocities at each
 * point in time.
 */
double** eulerForward(double* start, double D, int steps, double h) {
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
   return values;
}

/* Function: leapfrog
 * ------------------------
 * Implements the leapfrog method for a single pendulum
 *
 * start:   one-dimensional array of length 2 (position,velocity)
 * D:       damping coefficient
 * steps:   number of steps for the iteration
 * h:       timestep of method
 *
 * returns: two-dimensional array of positions and velocities at each
 * point in time.
 */
double** leapfrog(double* start, double D, int steps, double h) {
   double** values = create2DArray(2,steps);
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }

   double identity[] = {1.0,0.0,0.0,1.0};
   double function[] = {0.0,1.0,-1.0,-D};
   double* matrix = create1DArray(4);
   double* matrix_euler = create1DArray(4);
   for (int i = 0; i < 4; i++) {
      matrix[i] = h*function[i];
      matrix_euler[i] = identity[i] + h*function[i];
   }

   values[0][0] = start[0];
   values[1][0] = start[1];
   double* prev_i = create1DArray(2);
   double * x_i  = vectorMatrixOp(matrix_euler, start);
   values[0][1] = x_i[0];
   values[1][1] = x_i[1];
   for (int i = 2; i < steps; i++){
      double* prev = create1DArray(2);
      prev[0] = values[0][i-2];
      prev[1] = values[1][i-2];
      double* vector = create1DArray(2);
      vector[0] = values[0][i-1];
      vector[1] = values[1][i-1];
      double* x = vectorMatrixOp(matrix,vector);
      values[0][i] = 2*x[0] + prev[0];
      values[1][i] = 2*x[1] + prev[1];
   }
   return values;
}

/* Function: rk4
 * ------------------------
 * Implements the Runge-Kutta 4 method for a single pendulum
 *
 * start:   one-dimensional array of length 2 (position,velocity)
 * D:       damping coefficient
 * steps:   number of steps for the iteration
 * h:       timestep of method
 *
 * returns: two-dimensional array of positions and velocities at each
 * point in time.
 */
double** rk4(double* start, double D, int steps, double h) {
   double** values = create2DArray(2,steps);
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }

   double function[] = {0.0,1.0,-1.0,-D};
   double* matrix = create1DArray(4);
   for (int i = 0; i < 4; i++) {
      matrix[i] = function[i];
   }

   values[0][0] = start[0];
   values[1][0] = start[1];

   for (int i = 1; i < steps; i++){
      double** k = create2DArray(2,4);
      double* prev_i = create1DArray(2);
      prev_i[0] = values[0][i-1];
      prev_i[1] = values[1][i-1];
      double* x_i = vectorMatrixOp(matrix,prev_i);
      k[0][0] = h*x_i[0];
      k[1][0] = h*x_i[1];
      double* prev_ii = create1DArray(2);
      prev_ii[0] = values[0][i-1] + 0.5*k[0][0];
      prev_ii[1] = values[1][i-1] + 0.5*k[1][0];
      double* x_ii = vectorMatrixOp(matrix, prev_ii);
      k[0][1] = h*x_ii[0];
      k[1][1] = h*x_ii[1];
      double* prev_iii = create1DArray(2);
      prev_iii[0] = values[0][i-1] + 0.5*k[0][1];
      prev_iii[1] = values[1][i-1] + 0.5*k[1][1];
      double* x_iii = vectorMatrixOp(matrix, prev_iii);
      k[0][2] = h*x_iii[0];
      k[1][2] = h*x_iii[1];
      double* prev_iv = create1DArray(2);
      prev_iv[0] = values[0][i-1] + k[0][2];
      prev_iv[1] = values[1][i-1] + k[1][2];
      double* x_iv = vectorMatrixOp(matrix, prev_iv);
      k[0][3] = h*x_iv[0];
      k[1][3] = h*x_iv[1];

      values[0][i] = prev_i[0] + (k[0][0] + 2*k[0][1] + 2*k[0][2] + k[0][3])/6.0;
      values[1][i] = prev_i[1] + (k[1][0] + 2*k[1][1] + 2*k[1][2] + k[1][3])/6.0;
   }
   return values;
}

/* Function: implicitEuler
 * ------------------------
 * Implements the implicit Euler method for a single pendulum
 *
 * start:   one-dimensional array of length 2 (position,velocity)
 * D:       damping coefficient
 * steps:   number of steps for the iteration
 * h:       timestep of method
 *
 * returns: two-dimensional array of positions and velocities at each
 * point in time.
 */
double** implicitEuler(double* start, double D, int steps, double h) {
	double** values = create2DArray(2,steps);
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }

   double identity[] = {1.0,0.0,0.0,1.0};
   double function[] = {0.0,1.0,-1.0,-D};
   double* pre_inv_matrix = create1DArray(4);
   for (int i = 0; i < 4; i++) {
      pre_inv_matrix[i] = identity[i] - h*function[i];
   }
   double* matrix = invert2x2(pre_inv_matrix);

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
   return values;
}

/* Function: leapfrogSine
 * ------------------------
 * Implements the leapfrog method for a single pendulum without using
 * a small-angle approximation
 *
 * start:   one-dimensional array of length 2 (position,velocity)
 * D:       damping coefficient
 * steps:   number of steps for the iteration
 * h:       timestep of method
 *
 * returns: two-dimensional array of positions and velocities at each
 * point in time.
 */
double** leapfrogSine(double* start, double D, int steps, double h) {
   double** values = create2DArray(2,steps);
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }
   double identity[] = {1.0,0.0,0.0,1.0};
   double function[] = {0.0,1.0,-1.0,-D};
   double* matrix = create1DArray(4);
   double* matrix_euler = create1DArray(4);
   for (int i = 0; i < 4; i++) {
      matrix[i] = h*function[i];
      matrix_euler[i] = identity[i] + h*function[i];
   }

   values[0][0] = start[0];
   values[1][0] = start[1];
   double* prev_i = create1DArray(2);
   double * x_i  = vectorMatrixSineOp(matrix_euler, start);
   values[0][1] = x_i[0];
   values[1][1] = x_i[1];
   for (int i = 2; i < steps; i++){
      double* prev = create1DArray(2);
      prev[0] = values[0][i-2];
      prev[1] = values[1][i-2];
      double* vector = create1DArray(2);
      vector[0] = values[0][i-1];
      vector[1] = values[1][i-1];
      double* x = vectorMatrixSineOp(matrix,vector);
      values[0][i] = 2*x[0] + prev[0];
      values[1][i] = 2*x[1] + prev[1];
   }
   return values;
}

/* Function: rk4Sine
 * ------------------------
 * Implements the Runge-Kuntta 4 method for a single pendulum without
 * using the small-angle approximation.
 *
 * start:   one-dimensional array of length 2 (position,velocity)
 * D:       damping coefficient
 * steps:   number of steps for the iteration
 * h:       timestep of method
 *
 * returns: two-dimensional array of positions and velocities at each
 * point in time.
 */
double** rk4Sine(double* start, double D, int steps, double h) {
   double** values = create2DArray(2,steps);
   if (values == NULL)  {
       printf(" Out of memory!\n");
       exit(1);
   }

   double function[] = {0.0,1.0,-1.0,-D};
   double* matrix = create1DArray(4);
   for (int i = 0; i < 4; i++) {
      matrix[i] = function[i];
   }

   values[0][0] = start[0];
   values[1][0] = start[1];

   for (int i = 1; i < steps; i++){
      double** k = create2DArray(2,4);
      double* prev_i = create1DArray(2);
      prev_i[0] = values[0][i-1];
      prev_i[1] = values[1][i-1];
      double* x_i = vectorMatrixSineOp(matrix,prev_i);
      k[0][0] = h*x_i[0];
      k[1][0] = h*x_i[1];
      double* prev_ii = create1DArray(2);
      prev_ii[0] = values[0][i-1] + 0.5*k[0][0];
      prev_ii[1] = values[1][i-1] + 0.5*k[1][0];
      double* x_ii = vectorMatrixSineOp(matrix, prev_ii);
      k[0][1] = h*x_ii[0];
      k[1][1] = h*x_ii[1];
      double* prev_iii = create1DArray(2);
      prev_iii[0] = values[0][i-1] + 0.5*k[0][1];
      prev_iii[1] = values[1][i-1] + 0.5*k[1][1];
      double* x_iii = vectorMatrixSineOp(matrix, prev_iii);
      k[0][2] = h*x_iii[0];
      k[1][2] = h*x_iii[1];
      double* prev_iv = create1DArray(2);
      prev_iv[0] = values[0][i-1] + k[0][2];
      prev_iv[1] = values[1][i-1] + k[1][2];
      double* x_iv = vectorMatrixSineOp(matrix, prev_iv);
      k[0][3] = h*x_iv[0];
      k[1][3] = h*x_iv[1];

      values[0][i] = prev_i[0] + (k[0][0] + 2*k[0][1] + 2*k[0][2] + k[0][3])/6.0;
      values[1][i] = prev_i[1] + (k[1][0] + 2*k[1][1] + 2*k[1][2] + k[1][3])/6.0;
   }
   return values;
}
