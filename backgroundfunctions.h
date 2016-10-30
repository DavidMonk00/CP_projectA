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

double** MAdd(double** a, double** b) {
   double** c = create2DArray(2, length(a[0]));
   if (length(a[0]) != length(b[0])) {
      printf("Arrays are not of equal order.\n");
      exit(1);
   }
   for (int i = 0; i < length(a[0]); i++) {
      c[0][i] = a[0][i] + b[0][i];
      c[1][i] = a[1][i] + b[1][i];
   }
}
