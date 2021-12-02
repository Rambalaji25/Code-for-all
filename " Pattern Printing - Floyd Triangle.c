"
A number N indicating the number of rows in Floyd's triangle is passed as the input. The program must print the Floyd's triangle pattern.

Input Format:
The first line will contain N.

Output Format:
The first N lines will contain the Floyd's triangle pattern.

Boundary Conditions:
3 <= N <= 50

Example Input/Output 1:
7

Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28


Example Input/Output 2:
Input:
5

Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 "
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n,b=1;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++)
        printf("%d ",b++);
    printf("\n");
        
    }


}
