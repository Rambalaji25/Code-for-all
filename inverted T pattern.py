The program must accept two string values S1 and S2 as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Note: The first character of the string S2 is always present in the string S1.

Boundary Condition(s):
3 <= Length of S1, S2 <= 100

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
computer
purescience

Output:
---e----
---c----
---n----
---e----
---i----
---c----
---s----
---e----
---r----
---u----
computer

Example Input/Output 2:
Input:
chennai
agra

Output:
-----a-
-----r-
-----g-
chennai

Example Input/Output 3:
Input:
volleyball
loser

Output:
--r-------
--e-------
--s-------
--o-------
volleyball


z=input().strip()
c=input().strip()
b=z.index(c[0])
for i in range(len(c)-1):
    for j in range(len(z)):
        if b==j:
            print(c[-i-1],end='')
        else:
            print(end="-")
    print()
print(z)
