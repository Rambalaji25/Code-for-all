The program must accept a string S and an integer value N. Then the program must print the first N characters, then must print the next N characters in reverse direction and so on.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.
The second line contains N.

Output Format:
The first line contains a string value.

Example Input/Output 1:
Input:
abcdefghijk
3

Output:
abcfedghikj

Explanation:
Here N is 3.
So abc is printed.
Then def is reversed and printed.
Then ghi is printed.
The remaining characters kj are reversed and printed.

Example Input/Output 2:
Input:
mango
2

Output:
magno

g=input().strip()
c=int(input())
d=0
for i in range(0,len(g),c):
    f=''
    for j in range(i,min(len(g),i+c)):
        f+=g[j]
    if d%2==0:
        print(f,end='')
    else:
        print(f[::-1],end='')
    d+=1
