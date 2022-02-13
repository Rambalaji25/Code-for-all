

Products - Total Price
There are four products A, B, C and D in a shop. The price of the four products are given below.
A - Rs.40 each or Rs.100 for a pack of 4
B - Rs.60 each
C - Rs.55 each or Rs.200 for a pack of 6
D - Rs.95 each
The program must accept a string S representing the products in a cart. The program must print the total price for the entire cart based on the given price list.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the total price for the entire cart based on the given price list.

Example Input/Output 1:
Input:
ABACDBAAA

Output:
410

Explanation:
A - quantity 5 - (100 + 40)
B - quantity 2 - (60 + 60)
C - quantity 1 - 55
D - quantity 1 - 95
Total price - 410

Example Input/Output 2:
Input:
CACCCDAADCCCCCCCBC

Output:
770


rb=input().strip();z=0;q=set(rb)
for i in q:
    x=rb.count(i)
    if i=="A":
        while x>=4:
            k=x//4
            z+=k*100
            x=x%4
            
        else:
            for i in range(x):
                z+=40
    elif i=="B":
        for i in range(x):
            z+=60
    elif i=="C":
        while x>=6:
            g=x//6
            z+=g*200
            x=x%6
        else:
            for i in range(x):
                z+=55
    elif i=="D":
        for i in range(x):
            z+=95
print(z)

