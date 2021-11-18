The program must accept an integer matrix of size NxN as the input. The program must replace the integers by the asterisk except for the integers in the innermost layer and the outermost layer of the matrix. Then the program must print the modified matrix as the output.

Boundary Condition(s):
3 <= N <= 100

Input Format:
The first line contains N.
The next N lines each contain N integers separated by a space.

Output Format:
The first N lines containing the modified matrix.

Example Input/Output 1:
Input:
5
1 6 4 1 3
9 2 4 8 2
4 8 9 1 8
0 3 5 4 3
6 9 6 1 1

Output:
1 6 4 1 3
9 * * * 2
4 * 9 * 8
0 * * * 3
6 9 6 1 1

Explanation:
In the given 5x5 matrix, the innermost layer and outermost layer are highlighted below.
1 6 4 1 3
9 2 4 8 2
4 8 9 1 8
0 3 5 4 3
6 9 6 1 1
After replacing the integers by the asterisk except for the integers in the innermost and the outermost layer of the matrix, it becomes
1 6 4 1 3
9 * * * 2
4 * 9 * 8
0 * * * 3
6 9 6 1 1

Example Input/Output 2:
Input:
8
3 7 6 8 1 9 4 4
6 5 9 1 4 8 2 3
7 0 1 8 2 5 4 3
4 3 6 1 6 2 1 0
6 9 8 3 8 1 5 8
9 0 2 5 9 7 6 5
1 5 4 8 6 9 0 2
1 9 3 7 2 8 3 8

Output:
3 7 6 8 1 9 4 4
6 * * * * * * 3
7 * * * * * * 3
4 * * 1 6 * * 0
6 * * 3 8 * * 8
9 * * * * * * 9
1 * * * * * * 2
1 9 3 7 2 8 3 8


#Your code below
s=int(input())
d=[list(map(int,input().split())) for i in range(s)]
z=s//2
v=[0,s-1]
for x in range(s):
    for h in range(s):
        if x in v or h in v:
            print(d[x][h],end=' ')
        elif x in [z,s-z-1]and h in [z,s-z-1]:
            print(d[x][h],end=' ')
        else:
            print('*',end=' ')
    print()
