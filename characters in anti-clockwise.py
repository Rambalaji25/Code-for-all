The program must accept a character matrix of size NxN as the input. The program must print all the characters spirally in the anti-clockwise direction from the character matrix as the output.

Boundary Condition(s):
2 <= N <= 50

Input Format:
The first line contains N.
The next N lines each contain N characters separated by a space.

Output Format:
The first line contains all the characters of the NxN character matrix as per the given condition.

Example Input/Output 1:
Input:
4
j l u z
i r f e
b q a n
o x k c

Output:
j i b o x k c n e z u l r q a f

Example Input/Output 2:
Input:
3
o j B
m i y
A s d

Output:
o m A s d y B j i

n=int(input())
l=[list(input().strip().split()) for i in range(n)]
t=[]
for ctr in range(n//2):
    for i in range(ctr,n-ctr):
        print(l[i][ctr],end=' ')
    for j in range(1+ctr,n-ctr):
        print(l[n-ctr-1][j],end=' ')
    for i in range(n-2-ctr,ctr-1,-1):
        print(l[i][n-ctr-1],end=' ')
    for j in range(n-2-ctr,ctr,-1):
        print(l[ctr][j],end=' ')
if n%2:
    print(l[n//2][n//2])
