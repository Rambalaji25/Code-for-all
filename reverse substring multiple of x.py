The program must accept a string S and an integer X as the input. For each multiple M of X from 1 to the length of S, the program must reverse the substring of S which starts at the position 1 and ends at the position M. Then the program must print the modified string S as the output.

Boundary Condition(s):
1 <= Length of S <= 1000
1 <= X <= Length of S

Input Format:
The first line contains S.
The second line contains X.

Output Format:
The first line contains the modified string S.

Example Input/Output 1:
Input:
SkillRack
3

Output:
kcaikSllR

Explanation:
The multiples of 3 from 1 to 9 (length of "SkillRack") are 3, 6 and 9.
For the multiple 3, the substring Ski is reversed. Now the string becomes ikSllRack.
For the multiple 6, the substring ikSllR is reversed. Now the string becomes RllSkiack.
For the multiple 9, the substring RllSkiack is reversed. Now the string becomes kcaikSllR.
Hence the output is kcaikSllR

Example Input/Output 2:
Input:
HellO
5

Output:
OlleH

Example Input/Output 3:
Input:
AbCdEf#98
2

Output:
9#dCAbEf8

#Your code below

z=input().strip()
y=int(input())
for k in range(y,len(z)+1,y):
    z=z[:k][::-1]+z[k:]
print(z)
