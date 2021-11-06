

There is a large rectangular grid of length L and breadth B. The side which represents the breadth is perpendicular to X axis. A painter paints N smaller rectangular grids which are within the above large rectangular grid with different colours. The co-ordinates of the smaller rectangular grids which are painted are passed as the input to the program. The top-left, bottom-left, top-right, bottom-right co-ordinates can be passed in any order and the x and y co-ordinates positions are relative to the bottom-left position of the larger rectangular grid. The program must finally print the painted unit rectangular grids represented by an asterisk * and the unpainted rectangular grids by a hash #

Boundary Condition(s):
1 <= L, B, N <= 100

Input Format:
The first line contains L and B separated by a space.
The second line contains N.
The next N*4 lines contain the co-ordinates of the smaller rectangular grids being painted.

Output Format:
B lines containing L columns represented by * or #

Example Input/Output 1:
Input:
10 10
2
2 5
2 10
7 5
7 10
3 6
3 2
6 6
6 2

Output:
##*****###
##*****###
##*****###
##*****###
##*****###
###***####
###***####
###***####
##########
##########


Program [Python]


R,B=map(int,input().split())
ni=int(input())
l=[['#' for m in range(R)]for p in range(B)]
for z in range(ni):
    tl1,tl2=map(int,input().split())
    bl1,bl2=map(int,input().split())
    tr1,tr2=map(int,input().split())
    br1,br2=map(int,input().split())
    if tl2!=bl2:
        f,j=sorted([tl2,bl2])
    elif tl2!=tr2:
        f,j=sorted([tl2,tr2])
    else:
        f,j=sorted([tl2,br2])
    if bl1!=tr1:
        fo,jo=sorted([bl1,tr1])
    elif bl1!=br1:
        fo,jo=sorted([bl1,br1])
    else:
        fo,jo=sorted([bl1,tl1])
    for p in range(f,j):
        for m in range(fo,jo):
            l[p][m]='*'
for p in l[::-1]:
    print(*p,sep='')
