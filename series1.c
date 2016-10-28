#include <math.h>

double *ser(double start, double max_count) {
   static double values[20];
   int i;
   for (i = 0; i<20; i++){
      values[i] = (double)i;
   }
   return values;
   /*double total = start;
   double counter = 1.;
   while (counter < max_count) {
      total+=1./(pow(counter,3));
      counter++;
   }
   return total;*/
}
