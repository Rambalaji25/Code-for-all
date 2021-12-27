Given an array of N positive integers, print the integer having the least number of factors.

Note: If multiple numbers have the least factor count, print the largest number among them.

Input Format:
The first line contains N
The second line contains N positive integers, each separated by a space.

Output Format:
The first line contains the integer which has the least number of factors

Boundary Conditions:
1 <= N <= 1000

Example Input/Output 1:
Input:
5
15 12 18 15 10

Output:
15

Example Input/Output 2:
Input:
6
1 7 9 11 19 23

Output:
1

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n, a=-999, c=999;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);
    for(int i=0;i<n;i++)
    {
        int x=0;
        for(int j=1;j<=arr[i];j++)
        {
            if (arr[i]%j==0)
                x++;
        }
        if (x<c)
        {
            c=x;
            a=arr[i];
        }
        else if (x==c)
        {
            a=arr[i]>a?arr[i]:a;
        }
    }
    printf("%d",a);
}
