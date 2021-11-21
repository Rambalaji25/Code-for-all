The program must accept an integer N as the input. The program must print the minimum number of integers that give the sum N based on the following conditions.
- Each integer must be less than or equal to N.
- Each integer must be formed using 0's and 1's.

Boundary Condition(s):
1 <= N <= 10^8

Input Format:
The first line contains N.

Output Format:
The first line contains an integer representing the minimum number of integers that give the sum N.

Example Input/Output 1:
Input:
32

Output:
3

Explanation:
Here N = 32.
The possible integers that we can use to represent 32 as a sum are given below.
0 1 10 11
Here we can represent the integer 32 as the sum of 10, 11 and 11 (All other combinations have more than 3 integers).
So 3 is printed as the output.

Example Input/Output 2:
Input:
1043

Output:
4

Explanation:
Here N = 1043.
The possible integers that we can use to represent 1043 as a sum are given below.
0 1 10 11 100 101 110 111 1000 1001 1010 1011
One of the possible combinations that gives the sum 1043 is given below.
10 11 11 1011

Example Input/Output 3:
Input:
8

Output:
8


#Your code below
z=input().strip()
j=0
for v in z:
    if int(v)>j:
        j=int(v)
print(j)

