z,k=map(int,input().split())
l=[list(map(int,input().split())) for o in range(z)]
a=0
for o in range(z-1):
    for m in range(k-1):
        if l[o][m]==l[o+1][m]==l[o][m+1]==l[o+1][m+1]:
            a+=1
print(a)
