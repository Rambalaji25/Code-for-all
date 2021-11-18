The program must accept a string S containing multiple words as the input. The program must print the words starting with an upper case alphabet in S as the output. If there is no such word, the program must print -1 as the output.

Boundary Condition(s):
3 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the words starting with an upper case alphabet in S or -1.

Example Input/Output 1:
Input:
How are you? I am FINE

Output:
How I FINE

Explanation:
The words starting with an upper case alphabet are How, I and FINE.
Hence the output is How I FINE

Example Input/Output 2:
Input:
Cricket Match 1: India vs Pakistan

Output:
Cricket Match India Pakistan

Example Input/Output 3:
Input:
hi dora, is this your map?

Output:
-1

#Your code below
rb=input()
s=0
for i in rb.split():
    if i[0].isupper():
        print(i,end=" ")
        s=1
if s==0:
    print(-1)
        
