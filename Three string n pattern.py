The program must accept three string values S1, S2 and S3 containing only lower case alphabets as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Note:
 There is only one possible way to rearrange the three string values for the N pattern.
 The length of S1, S2 and S3 are always equal.

Boundary Condition(s):
3 <= Length of S1, S2, S3 <= 100

Input Format:
The first line contains S1, S2 and S3 separated by a space.

Output Format:
The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
hello order range

Output:
o***e
lr**g
l*d*n
e**ea
h***r

Example Input/Output 2:
Input:
google amazon errata

Output:
e****n
lr***o
g*r**z
o**a*a
o***tm
g****a

#Your code below
v,g,k=input().split()
if g[0] not in [v[-1],k[-1]]:
    if g[-1]==v[0]:
        v,g,k=g,v,k
    else:
        v,g,k=g,k,v
elif k[0] not in [v[-1],g[-1]]:
    if k[-1]==v[0]:
        v,g,k=k,v,g
    else:
        v,g,k=k,g,v
else:
    if v[-1]==k[0]:
        g,k=k,g
rb=len(v)
d=[['*' for j in range(rb)]for _ in range(rb)]
for i in range(rb):
    d[i][0]=v[rb-i-1]
    d[i][i]=g[i]
    d[i][-1]=k[rb-i-1]
for i in d:
    print(*i,sep='')
