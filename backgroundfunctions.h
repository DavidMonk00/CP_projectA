/* 20161104
 * David Monk
 *
 * This header file contains the matrix operation functions used
 * within the FDM methods implemented for both the single and
 * double pendulums.
 */

#include <gsl/gsl_blas.h>
#include <math.h>

int length(double* array) {
   return sizeof(array)/sizeof(double);
}

/* Function: create2DArray
 * ------------------------
 * Creates a two-dimensional pointer array in the heap
 *
 * rows:    number of rows in array
 * columns: number of columns in array
 *
 * returns: empty 2D double pointer array.
 */
double** create2DArray(int rows, int columns) {
   double** array;
   array = malloc(rows*sizeof(double*));
   for (int i = 0; i < rows; i++) {
      array[i] = malloc(columns*sizeof(double));
   }
   return array;
}

/* Function: create1DArray
 * ------------------------
 * Creates a one-dimensional pointer array in the heap
 *
 * columns: number of columns in array
 *
 * returns: empty 1D double pointer array.
 */
double* create1DArray(int columns) {
   double* array;
   array = malloc(columns*sizeof(double));
   return array;
}

/* Function: vectorMatrixOp
 * ------------------------
 * Pre-multiplies a two-vector by a 2x2 matrix
 *
 * matrix:  one-dimensional array of length 4
 * vector:  one-dimensional array of length 2
 *
 * returns: one-dimensional array of length 2.
 */
double* vectorMatrixOp(double* matrix, double* vector) {
   static double c[] = { 0.00, 0.00};
   gsl_matrix_view MATRIX = gsl_matrix_view_array(matrix, 2, 2);
   gsl_matrix_view VECTOR = gsl_matrix_view_array(vector, 2, 1);
   gsl_matrix_view C = gsl_matrix_view_array(c, 2, 1);
   gsl_blas_dgemm (CblasNoTrans, CblasNoTrans,
                   1.0, &MATRIX.matrix,
                   &VECTOR.matrix,0.0,&C.matrix);
   return c;
}

/* Function: vector4MatrixOp
 * ------------------------
 * Pre-multiplies a four-vector by a 4x4 matrix
 *
 * matrix:  one-dimensional array of length 16
 * vector:  one-dimensional array of length 4
 *
 * returns: one-dimensional array of length 4.
 */
double* vector4MatrixOp(double* matrix, double* vector) {
   static double c[] = {0.0, 0.0, 0.0, 0.0};
   gsl_matrix_view MATRIX = gsl_matrix_view_array(matrix, 4, 4);
   gsl_matrix_view VECTOR = gsl_matrix_view_array(vector, 4, 1);
   gsl_matrix_view C = gsl_matrix_view_array(c, 4, 1);
   gsl_blas_dgemm (CblasNoTrans, CblasNoTrans,1.0, &MATRIX.matrix, &VECTOR.matrix,0.0, &C.matrix);
   return c;
}

/* Function: invert2x2
 * ------------------------
 * inverts the 2x2 matrix
 *
 * matrix:  one-dimensional array of length 4
 *
 * returns: one-dimensional array of length 4.
 */
double* invert2x2(double* matrix) {
   static double c[] = {0.0,0.0,0.0,0.0};
   double det = matrix[0]*matrix[3] - matrix[1]*matrix[2];
   c[0] = matrix[3]/det;
   c[1] = -matrix[1]/det;
   c[2] = -matrix[2]/det;
   c[3] = matrix[0]/det;
   return c;
}

/* Function: vectorMatrixSineOp
 * ------------------------
 * Pre-multiplies a two-vector by a 2x2 matrix with the small-angle
 * approximation replaced by a sine operation. This operation is done
 * at the point matrix[1,0] or matrix[3] in 1D.
 *
 * matrix:  one-dimensional array of length 4
 * vector:  one-dimensional array of length 2
 *
 * returns: one-dimensional array of length 2.
 */
double* vectorMatrixSineOp(double* matrix, double* vector) {
   static double c[] = {0.0,0.0};
   c[0] = matrix[0]*vector[0] + matrix[1]*vector[1];
   c[1] = matrix[2]*sin(vector[0]) + matrix[3]*vector[1];
   return c;
}
