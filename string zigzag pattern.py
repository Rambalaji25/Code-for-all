
Given a string S and an integer N as the input, the program must split the string into groups whose size is N and print them as the output in separate lines in a zig zag manner. If the last group size is less than N then the remaining letters must be filled with asterisk as shown in the Example Input/Output.

Input Format:
The first line contains S.
The second line contains N.

Output Format:
LENGTH(S)/N + LENGTH(S)%N lines containing the desired pattern.

Boundary Conditions:
4 <= LENGTH(S) <= 500
2 <= N <= LENGTH(S)

Example Input/Output 1:
Input:
ENVIRONMENT
3

Output:
ENV
ORI
NME
*TN

Example Input/Output 2:
Input:
ENVIRONMENT
4

Output:
ENVI
MNOR
ENT*

Example Input/Output 3:
Input:
EVERYDAY
2

Output:
EV
RE
YD
YA

#Your code below
rb,f,d=list(input().strip()),int(input()),0
s=f
j=0
while len(rb)%f!=0:
    rb.append('*')
g=len(rb)
for i in range(0,g-f+1,f):
    if j%2==0:
        print(''.join(rb[d:f]))
    else:
        print(''.join(rb[d:f][::-1]))
    d+=s
    f+=s
    j+=1
    
    
