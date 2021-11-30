"
The program must accept two arrays of size N and then for each element position, the program must print find the sum of odd elements till that position for both the arrays and then print the sum which is higher.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers representing the first array separated by a space.
The third line contains N integers representing the second array separated by a space.

Output Format:
The first line contains N integer values based on the given conditions.

Example Input/Output 1:
Input:
6
8 1 7 8 2 1
1 3 2 5 6 2

Output:
1 4 8 9 9 9

Explanation:
Here N = 6.
Till position 1:
Sum of odd integers in the 1st array is 0.
Sum of odd integers in the 2nd array is 1.
Here 1 is the maximum which is printed as the output.

Till position 2:
Sum of odd integers in the 1st array is 1.
Sum of odd integers in the 2nd array is 4.
Here 4 is the maximum which is printed as the output.

Till position 3:
Sum of odd integers in the 1st array is 8.
Sum of odd integers in the 2nd array is 4.
Here 8 is the maximum which is printed as the output.

Till position 4:
Sum of odd integers in the 1st array is 8.
Sum of odd integers in the 2nd array is 9.
Here 9 is the maximum which is printed as the output.

Till position 5:
Sum of odd integers in the 1st array is 8.
Sum of odd integers in the 2nd array is 9.
Here 9 is the maximum which is printed as the output.

Till position 6:
Sum of odd integers in the 1st array is 9.
Sum of odd integers in the 2nd array is 9.
Here 9 is the maximum which is printed as the output.

Example Input/Output 2:
10
9 16 3 26 14 19 181 6 29 12
17 11 13 24 30 10 2 156 22 20

Output:
17 28 41 41 41 41 212 212 241 241
"
z=int(input())
f=list(map(int,input().split()))
rb=list(map(int,input().split()))
x=0;y=0
for i in range(z):
    if f[i]%2==1:
        x+=f[i]
    if rb[i]%2==1:
        y+=rb[i]
    print(max(x,y),end=" ")
