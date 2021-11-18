The program must accept N integers and a digit D as the input. The program must print the sum S of integers having at least one D among the N integers. If there is no such integer, the program must print -1 as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^7
0 <= D <= 9

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains D.

Output Format:
The first line contains S or -1.

Example Input/Output 1:
Input:
5
445 7891 545 309 154
4

Output:
1144

Explanation:
The integers with at least one 4 are 445, 545 and 154.
So their sum 1144 is printed as the output.

Example Input/Output 2:
Input:
4
999 456 215 328
7

Output:
-1

N=int(input())
arr=[(i) for i in input().split()]
k=input().strip()
final=[]
for i in arr:
    if k in i:
        final.append(i)
if not final:
    print(-1)
else:
    r=[int(i) for i in final]
    print(sum(r))
