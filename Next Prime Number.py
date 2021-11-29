A number N is passed as the input. The program must print the next immediate prime number.

Input Format:
The first line will contain N.

Output Format:
The first line will contain the integer value of next immediate prime number.

Boundary Conditions:
1 <= N <= 999999

Example Input/Output 1:
Input:
11

Output:
13

Example Input/Output 2:
Input:
2

Output:
3





#Your code below
z=int(input())
while True:
    z+=1
    for j in range(2,n):
        if z%j==0:
            break
    else:
        print(z)
        break
