
A string S is passed as input. The program must print the value of the string after the index where the last character appears from the beginning of the string.

Input Format:
The first line contains the value of S.

Output Format:
The first line contains the value of the string as per the above mentioned condition.

Boundary Conditions:
5 <= Length of string S <= 50

Example Input/Output 1:
Input:
excitement

Output:
ement

Explanation:
The last character is t. t appears as the 5th character(letter). So the value from 6th position, ement printed as the output.


Example Input/Output 2:
Input:
area

Output:
rea

Example Input/Output 3:
Input:
reverance

Output:
verance


e=input().strip()
for f in range(len(e)):
    if e[-1]==e[f]:
        print(e[f+1:])
        exit()
        
        
        
        
        
        
