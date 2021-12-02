The program must accept a string S containing only lower case alphabets as the input. The program must rotate the repeated vowels in the string S by 1 position in the clockwise direction. Then the program must print the modified string S as the output.

Boundary Condition(s):
4 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the modified string S.

Example Input/Output 1:
Input:
administration

Output:
idminastritaon

Explanation:
The repeated vowels in the given string are highlighted below.
administration
After rotating those repeated vowels by 1 position in the clockwise direction, the string becomes "idminastritaon".
Hence output is idminastritaon

Example Input/Output 2:
Input:
correspondent

Output:
cerrospendont

Example Input/Output 3:
Input:
deal

Output:
deal

#Your code below
c=input().strip()
rb=''
f={'a':0,'e':0,'o':0,'i':0,'u':0}
for i in c:
    if i in 'aeiou':
        f[i]+=1
        if f[i]>1:
            rb+=i
temp=''
for i in c:
    if i in rb:
        temp+=i
if temp:
    temp=temp[1:]+temp[0]
x=0;res=''
for i in c:
    if i in rb:
        res+=temp[x]
        x+=1
    else:
        res+=i
print(res)
