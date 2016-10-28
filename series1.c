#include <math.h>

double *ser(int i, int max) {
   static double values[20];
   for (i = 0; i<max; i++){
      values[i] = (double)i;
   }
   return values;
}
