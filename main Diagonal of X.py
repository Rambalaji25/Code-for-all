The program must accept an integer matrix of size NxN and an integer X as the input. The program must print all the integers along the main diagonal of X in the matrix as the output.
Note: The integer X has occurred only once in the NxN matrix.

Boundary Condition(s):
2 <= N <= 50
1 <= Each integer value <= 10000

Input Format:
The first line contains N.
The next N lines each contain N integers separated by a space.
The (N+2)nd line contains X.

Output Format:
The first line contains all the integers along the main diagonal of X in the matrix separated by a space.

Example Input/Output 1:
Input:
4
77 48 51 82
13 53 76 68
64 71 45 52
87 87 64 24
53

Output:
77 53 45 24

Explanation:
The main diagonal of 53 is highlighted below.
77 48 51 82
13 53 76 68
64 71 45 53
87 87 64 24

Example Input/Output 2:
Input:
5
41 70 37 49 92
84 54 46 58 81
36 89 53 63 70
22 13 20 13 59
35 43 32 28 83
20

Output:
84 89 20 28



z=int(input())
l=[list(map(int,input().split())) for b in range(z)]
m=int(input())
f=[]
for b in range(z):
    if m in l[b]:
        y=l[b].index(m)
        rb=b
        break
v=min(rb,y)
rb-=v;y-=v
while rb<z and y<z:
    print(l[rb][y],end=' ')
    rb+=1; y+=1
