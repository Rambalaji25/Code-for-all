The program must accept two character matrices M1 and M2 as the input. The size of the matrix M1 is R*C and the size of the matrix M2 is K*K. The program must print M2 if the transpose of M2 is present in M1. Else the program must print -1 as the output.

Boundary Condition(s):
2 <= R, C <= 50
2 <= K <= Minimum value between R and C

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.
The (R+2)th line contains K.
The next K lines, each contains K characters separated by a space.

Output Format:
The first K lines, each contains K characters separated by a space or the first line contains -1.

Example Input/Output 1:
Input:
5 8
b m p r j r m l
i h x a d g n o
b i i b e h b g
a g h c f i l p
a m s p i b t d
3
a b c
d e f
g h i

Output:
a b c
d e f
g h i

Explanation:
The transpose of the matrix M2 is given below.
a d g
b e h
c f i
The transpose of the matrix M2 is present in the matrix M1, which is highlighted below.
b m p r j r m l
i h x a d g n o
b i i b e h b g
a g h c f i l p
a m s p i b t d

Example Input/Output 2:
Input:
5 8
b m p r j r m l
i h x a b c n o
b i i d e f b g
a g h g h i l p
a m s p i b t d
3
a b c
d e f
g h i

Output:
-1

Example Input/Output 3:
Input:
5 5
w I k s T
i E i k D
k Q R h k
T q T P k
G n K U h
4
E Q q n
i R T K
k h P U
D k k h

Output:
E Q q n
i R T K
k h P U
D k k h

v,x=map(int,input().split())
f=[list(input().strip().split()) for i in range(v)]
u=int(input())
d=[list(input().strip().split()) for i in range(u)]
count=0
for i in range(v-u+1):
    for j in range(x-u+1):
        if d[0][0]==f[i][j]:
            for b in range(u):
                for h in range(u):
                    if f[i+h][j+b]==d[b][h]:
                        count+=1
                    else:
                        count=0
                        break
            if count==u*u:
                for i in d:
                        print(*i)
                exit()
print(-1)
