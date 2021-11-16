The program must accept values of two string S1 and S2 as input. The program must print the uncommon alphabets in both S1 and S2.

Boundary Condition(s):
1 <= Length of string S1 and S2 <= 1000

Input Format:
The first line contains the value of string S1.
The second line contains the value of string S2.

Output Format:
The first line contains the uncommon alphabet(s) in S2.
The second line contains the uncommon alphabet(s) in S1.

Example Input/Output 1:
Input:
apple
pen

Output:
n
al

Explanation:
n is an uncommon alphabet in pen. So, n is printed
a and l are uncommon alphabets in apple. So, al is printed

Example Input/Output 2:
Input:
hello
world

Output:
wrd
he


a=input().strip()
b=input().strip()
d1={}
d2={}
for i in a:
    d1[i]=d1.get(i,0)+1
for i in b:
    if d1.get(i,0)==0:
        print(i,end='')
        d1[i]=-1
    d2[i]=d2.get(i,0)+1
print()
for i in a:
    if d2.get(i,0)==0:
        print(i,end='')
        d2[i]=-1
