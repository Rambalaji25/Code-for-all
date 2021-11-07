z=int(input())
l=list(map(int,input().split()))
k=[]
b=[]
for i in range(z):
    if l[i]%2==0:
        k.append(l[i])
    else:
        b.append(l[i])
k.sort()
b.sort()
print(*k,end=" ")
print(*b)
