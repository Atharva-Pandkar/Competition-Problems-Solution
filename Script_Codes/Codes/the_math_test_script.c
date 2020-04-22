#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n=0;
   scanf("%d",&n);
   if(n%2==0)
   {
       for (int j=0;j<n;j+=2)
       {
           printf(" %d %d",j+1,j);
       }
   }
   else{
       printf("Fail");
   } 
    
    
    
    return 0;
}
