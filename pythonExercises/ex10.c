#include <stdio.h>

int main(void)
{
    int i =1;
    char array[7] = {' ','/','-','|','\\','|'};
    
    while(i) 
    {
        if(i>6)
        {
            i=1;
        }
        printf("%c\r",array[i]);
        i++;
    }
    return 0;
}
