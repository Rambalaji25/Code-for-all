Given the values for X, A and B, the program must print the sum of multiples of X from A to B (inclusive of A and B).

Input Format:
The first line contains the value of X.
The second line contains the value of A.
The third line contains the value of B.

Output Format:
The first line contains the sum of multiples of X from A to B (inclusive of A and B).

Boundary Conditions:
1 <= X <= 100
1 <= A <= 100000
A <= B <= 1000000

Example Input/Output 1:
Input:
5
10
25

Output:
70

Explanation:
The multiples of 5 from 10 to 25 are, 10,15,20,25 and their sum is 70

a=int(input())
B=int(input())
C=int(input())
S=0
For i in range(b,c+1):
    If i%a==0:
          S+=i
Print(s)
