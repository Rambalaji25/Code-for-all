You must implement the function printZigZagTrianglePattern(int N) which accepts an integer N as the input. The function must print the desired pattern as shown in the Example Input/Output section.

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
1
3*2
4*5*6
10*9*8*7

Example Input/Output 2:
Input:
7

Output:
1
3*2
4*5*6
10*9*8*7
11*12*13*14*15
21*20*19*18*17*16
22*23*24*25*26*27*28


void printZigZagTrianglePattern(int N)
{
    int p=1,d=1;
    for(int r=1;r<=N;r++){
        for(int c=1;c<=r;c++){
            printf("%d",p);
            p+=d;
            if(c!=r){
                printf("*");
            }
        }
        p+=(r+!(r%2));
        d=-d;
        printf("\n");
    }
    

}


