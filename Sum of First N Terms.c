"""
The program must accept an integer N as the input. The program must print the sum of the first N terms in the following series.
1 1 2 1 2 3 1 2 3 4 1 2 3 4 5 1 2 3 4 5 6 1 2 3 4 5 6 7 ... and so on.
The above series contains the integers 1, 1 to 2, 1 to 3, 1 to 4, 1 to 5, 1 to 6, ... and so on.

Boundary Condition(s):
1 <= N <= 10^6

Input Format:
The first line contains N.

Output Format:
The first line contains an integer representing the sum of the first N terms in the above-mentioned series.

Example Input/Output 1:
Input:
7

Output:
11

Explanation:
The first 7 terms are 1 1 2 1 2 3 1.
So their sum is 11 (1+1+2+1+2+3+1).

Example Input/Output 2:
Input:
10

Output:
20
Max Execution Time Limit: 50 millisecs

"""

#include<stdio.h>
#include<stdlib.h>

int main()
{

    int n,s=0,t=1;
    scanf("%d",&n);
    for(int i=1;i<=n;i+=t,t++){
        int diff=n-i+1;
        if (diff<t)
            s+=diff*(diff+1)/2;
        else
            s+=t*(t+1)/2;
    }
    printf("%d",s);

}
