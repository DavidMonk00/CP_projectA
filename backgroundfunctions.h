#include <gsl/gsl_blas.h>

int length(double* array) {
   return sizeof(array)/sizeof(double);
}

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

double* vectorMatrixOp(double* matrix, double* vector) {
   static double c[] = { 0.00, 0.00};
   gsl_matrix_view MATRIX = gsl_matrix_view_array(matrix, 2, 2);
   gsl_matrix_view VECTOR = gsl_matrix_view_array(vector, 2, 1);
   gsl_matrix_view C = gsl_matrix_view_array(c, 2, 1);
   gsl_blas_dgemm (CblasNoTrans, CblasNoTrans,1.0, &MATRIX.matrix, &VECTOR.matrix,0.0, &C.matrix);
   return c;
}
