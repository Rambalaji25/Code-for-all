The program must accept a string S as the input. The program must print YES if the string S is formed using exactly three same substring values. 
Else the program must print NO as the output. Note: The length of S is always divisible by 3. 
Boundary Condition(s): 3 <= Length of S <= 99 
Input Format:
The first line contains S. 
Output Format: 
The first line contains YES or NO.
Example Input/Output 1: 
Input:
goldgoldgold 

Output:
YES

Example Input/Output 2:
Input: 
byebyeeye

Output: NO
 

s=input().strip()
t=len(s)//3
x=len(s)
s=[s[i:i+t] for i in range(0,x,t)]
if len(set(s))==1:
    print("YES")
else:
    print("NO")
