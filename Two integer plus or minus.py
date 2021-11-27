The program must accept two integers A,B separated by a string S (whose value is plus or minus). Based on the string value S, the program must print the sum or difference between the integers.

Input Format:
The first line contains A,S and B separated by a space.

Output Format:
The first line contains the integer value.

Example Input/Output 1:
Input:
3 plus 12

Output:
15

Example Input/Output 2:
Input:
100 minus 25

Output:
75

rb,h,z=input().strip().split()
rb=int(rb)
z=int(z)
if h=='plus':
    print(z+rb)
else:
    print(rb-z)
