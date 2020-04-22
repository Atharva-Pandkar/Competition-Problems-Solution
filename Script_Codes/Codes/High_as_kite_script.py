#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

   int n=0;
int j=2;
scanf("%d",&n);
    for(int y=0;y<=2;y++)
    { 
    
    for (int p=0;p<n-1;p++)
    {
        
        for(int z=y;z<2;z++)
        {
            printf(" ");
           } 
        printf("/"); 
        
       for(int a=2;a>j;a--)
        {
        printf("  ");
           
        }
               
        printf("\\");
        for(int b=2;b>y;b--)
        {
        printf(" ");
        }
    }
        for(int z=y;z<2;z++)
        {
            printf(" ");
           } 
        printf("/"); 
        
       for(int a=2;a>j;a--)
        {
        printf("  ");
           
        }
               
        printf("\\");
        printf("\n");

        j--;
}
 j=2;
for(int f=0;f<=2;f++)
{

    for (int p=0;p<n-1;p++)
    {
for(int z=0;z<f;z++)
{ printf(" ");
}
printf("\\");
for(int a=0;a<j;a++)
        {
        printf("  ");
        }
printf("/");

      
for(int x=2;x>j;x--)
{
printf(" ");
}

} 
    for(int z=0;z<f;z++)
{ printf(" ");
}
printf("\\");
for(int a=0;a<j;a++)
        {
        printf("  ");
        }
printf("/");

  j--;
printf("\n");
}   
    return 0;
}

