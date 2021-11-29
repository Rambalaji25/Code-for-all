Alen and Tim both own a tennis grass court and they decide to mow the lawn in and around the court which will cost them Rs.5 per square feet. Given the amount they spent to mow the lawn and the width of the court, find the difference between the length of the courts.

Input Format:
First line will contain the amount spent (in Rs) by Alen and Tim separated by space.
Second line will contain the width (in feet) of the courts of Alen and Tim separated by space.

Output Format:
The value (in feet) which is the difference between the length of the courts rounded off upto two decimal points.

Example Input/Output 1:
Input:
100000 80000
100 80

Output:
0.00

Explanation:
Area of Alen's court = 100000/5 = 20000 sq.ft. Length = 20000/100 = 200
Area of Tim's court = 80000/5 = 16000 sq.ft. Length = 16000/80 = 200
Hence the difference = 200-200 = 0 which when rounded off to decimal places is 0.00

Example Input/Output 2:
Input:
17500 40000
50 80

Output:
30.00

Explanation:
Area of Alen's court = 17500/5 = 3500 sq.ft. Length = 3500/50 = 70
Area of Tim's court = 40000/5 = 8000 sq.ft. Length = 8000/80 = 100
Hence the difference = 100-70 = 30.00



#Your code below
a=input().split(" ")
al=int(a[0])/5
t=int(a[1])/5
court=input().split(" ")
al=al/int(court[0])
t=t/int(court[1])
c=abs(al-t)
c="{:.2f}".format(c)
print(c)
