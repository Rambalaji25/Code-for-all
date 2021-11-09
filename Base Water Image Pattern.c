You must implement the function printRepeatNextPattern(int N) which accepts an integer N as the input. The function must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
2 <= N <= 100

Input Format:
The first line contains the value of N.

Output Format:
The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
4

Output:
4
55
666
7777
7777
666
55
4

Example Input/Output 2:
Input:
7

Output:
7
88
999
10101010
1111111111
121212121212
13131313131313
13131313131313
121212121212
1111111111
10101010
999
88
7

#include<stdio.h>
void printBaseWaterImagePattern(int N)
{
    for(int i=0;i<N;i++){
        for(int j=-1;j<i;j++)
            printf("%d",i+N);
        printf("\n");
    }
    for(int i=N-1;i>=0;i--){
        for(int j=-1;j<i;j++)
            printf("%d",i+N);
        printf("\n");
    }
}
int main(){
    int n;
    scanf("%d",&n);
    printBaseWaterImagePattern(n);
    return 0;
}

