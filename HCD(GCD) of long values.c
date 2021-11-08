The program must accept two long values X, Y and print their HCF (GCD).

Input Format:
The first line contains X and Y separated by a space.

Output Format:
The first line contains the HCF (GCD) of X and Y.

Boundary Condition(s):
1 <=  X, Y <= 10^18

Example Input/Output 1:
Input:
20 30

Output:
10

Example Input/Output 2:
Input:
999999999999 151515151515

Output:
30303030303

#include<stdio.h>
#include<stdlib.h>
#define ull unsigned long long int
ull hcd(ull a,ull z){
    if(z==0)return a;
    else{
        return hcd(z,a%z);
    }
}
int main()
{
    ull x,y;
    scanf("%llu %llu",&x,&y);
    printf("%llu",hcd(x,y));

}
