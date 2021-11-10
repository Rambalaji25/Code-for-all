The program must accept two integers N and X as the input. The program must invert the last X bits in the binary representation of N. Then the program must print the modified value of N as the output.

Boundary Condition(s):
1 <= N < 2^31
1 <= X <= 31

Input Format:
The first line contains N and X separated by a space.

Output Format:
The first line contains the modified value of N.

Example Input/Output 1:
Input:
21 3

Output:
18

Explanation:
The binary representation of 21 is 10101.
After inverting the last 3 bits in 10101, the binary representation becomes 10010.
Now the decimal equivalent of 10010 is 18.
Hence the output is 18

Example Input/Output 2:
Input:
70 4

Output:
73

Example Input/Output 3:
Input:
3 5

Output:
28

Explanation:
The binary representation of 3 is 11.
After inverting the last 5 bits in 00011 (3 leading zeros are padded as we need to invert the last 5 bits), the binary representation becomes 11100.
Now the decimal equivalent of 11100 is 28.
Hence the output is 28

rb,c=map(int,input().split())
v=bin(rb)[2:]
if len(v)<c:
    v='0'*(c-len(v))+v
t=v[:-c]
for i in v[-c:]:
    if i=='0':
        t+='1'
    else:
        t+='0'
print(int(t,2))
