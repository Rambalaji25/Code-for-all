" The program must accept N integers as the input. For each integer X among the N integers, the program must print the output based on the following conditions.
- If X is even, the program must print the value of X + (Sum of all the even digits in the remaining integers).
- If X is odd, the program must print the value of X + (Sum of all the odd digits in the remaining integers).

Boundary Condition(s):
2 <= N <= 1000
1 <= Each integer value <= 10^4

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the N integer values separated by a space.

Example Input/Output 1:
Input:
4
32 25 16 71

Output:
40 37 20 80

Explanation:
The first integer 32 is an even integer, so the sum is 40 (32 + 2+6).
The second integer 25 is an odd integer, so the sum is 37 (25 + 3+1+7+1).
The third integer 16 is an even integer, so the sum is 20 (16 + 2+2).
The fourth integer 71 is an odd integer, so the sum is 80 (71 + 3+5+1).
Hence the output is 40 37 20 80

Example Input/Output 2:
Input:
3
234 46 1897

Output:
252 60 1900
"
def digit(w,v):
    g=0
    while w>0:
        if w%2==v:
            g+=w%10
        w//=10
    return g
s=int(input())
R=list(map(int,input().split()))
x=0;z=0
for i in R:
    for j in str(i):
        if int(j)%2==0:
            z+=int(j)
        else:
            x+=int(j)
for i in R:
    if i%2==0:
        g=digit(i,0)
        print(i+z-g,end=' ')
    else:
        g=digit(i,1)
        print(i+x-g,end=' ')
