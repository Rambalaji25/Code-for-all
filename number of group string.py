
The program must accept a string S as the input. One or more characters of the same value occurring continuously are called as a group. The program must print the number of groups in the given string S as the output.

Boundary Condition(s):
2 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the number of groups in the string S.

Example Input/Output 1:
Input:
aabccc

Output:
3

Explanation:
'a' occurs continuously for 2 times and it is the first group.
'b' occurs once and it is the second group.
'c' occurs continuously for 3 times and it is the third group.
Hence the output is 3

Example Input/Output 2:
Input:
hjjhhl33

Output:
5


#Your code below
rb=input().strip()
z=1
for p in range(len(rb)-1):
    if rb[p]==rb[p+1]:
        continue
    z+=1
print(z)
