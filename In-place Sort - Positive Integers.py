The program must accept N integers as the input. The program must sort positive integers among their given positions and keep the negative integers in their same positions. Then the program must print the N modified integers as the output. If zero occurs consider it along with the positive integers.

Boundary Condition(s):
2 <= N <= 100
-10^5 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the N modified integers separated by a space.

Example Input/Output 1:
Input:
7
12 -5 7 -8 20 2 -1

Output:
2 -5 7 -8 12 20 -1

Explanation:
In the given 7 integers, the positive integers are 12 7 20 2. After sorting those positive integers in their positions, the integers become 2 -5 7 -8 12 20 -1.
Hence the output is 2 -5 7 -8 12 20 -1

Example Input/Output 2:
Input:
11
58 2 -69 89 64 43 -29 -79 0 18 -30

Output:
0 2 -69 18 43 58 -29 -79 64 89 -30




#Your code below
R=int(input())
A=list(map(int,input().split()))
m=[]
for i in A:
    if i>=0:
        m.append(i)
m.sort()
z=0
for i in A:
    if i>=0:
        print(m[z],end=" ")
        z+=1
    else:
        print(i,end=" ")
