
The program must accept two integers X and Y as the input. The program must remove the first digit and the last digit of both X and Y. Then the program must print the sum of X and Y as the output.

Boundary Condition(s):
100 <= X, Y <= 10^8

Input Format:
The first line contains X and Y separated by a space.

Output Format:
The first line contains the sum of X and Y.

Example Input/Output 1:
Input:
9874 156

Output:
92

Explanation:
After removing the first digit and the last digit of 9874, the integer X becomes 87.
After removing the first digit and the last digit of 156, the integer Y becomes 5.
So the sum of 87 and 5 is 92.

Example Input/Output 2:
Input:
10105 5700

Output:
80


n,m=input().strip().split()
n=n[1:-1];m=m[1:-1]
print(int(n)+int(m))
