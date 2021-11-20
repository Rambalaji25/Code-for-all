The program must accept an integer N as the input. The program must print the count of 0's in N except the trailing 0's as the output.

Boundary Condition(s):
1 <= N <= 10^18

Input Format:
The first line contains N.

Output Format:
The first line contains the count of 0's in N except the trailing 0's.

Example Input/Output 1:
Input:
50200300

Output:
3

Explanation:
There are two trailing 0's in 50200300.
So the remaining three 0's are highlighted below.
50200300


#Your code below
c=0
f=int(input())
while f%10==0:
    f//=10
for d in str(f):
    if d=="0":
        c+=1
print(c)
