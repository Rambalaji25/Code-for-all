A number N is passed as the input. The program must print the largest possible number with the digits in the given number N.

Input Format:
The first line contains the value of N.

Output Format:
The first line contains the largest possible number with the digits in N.

Boundary Conditions:
1 <= N <= 9999999

Example Input/Output 1:
Input:
265

Output:
652


Example Input/Output 2:
Input:
9090

Output:
9900


Example Input/Output 3:
Input:
222

Output:
222


#Your code below
z=list(input().strip())
z.sort(reverse=1)
print(*z,sep="")
