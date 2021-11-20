The program must accept N integers as the input. The program must print the sum of integers having odd number of digits in the given N integers. If there is no such integer, the program must print -1 as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^9

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the sum of integers having odd number of digits in the given N integers or -1.

Example Input/Output 1:
Input:
5
12 488 1 78 200

Output:
689

Explanation:
The integers with odd number of digits are 488, 1 and 200.
So their sum is 689 (488 + 1 + 200).

rb=0
f=int(input())
g=list(map(str,input().split()))
for i in g:
    if len(i)%2!=0:
        rb+=int(i)
if rb==0:
    print(-1)
    exit(0)
print(rb)
