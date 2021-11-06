The program must accept a list of integers as the input. The program must append 10, 20 and 30 to the end of the given list. Then the program must print all the integers in the list as the output. Please fill in the blanks with code so that the program runs successfully.

Boundary Condition(s):
1 <= Each integer value <= 10^8

Input Format:
The first line contains the list of integers separated by a space.

Output Format:
The first line contains the integers separated by a space based on the given condition.

Example Input/Output 1:
Input:
12 56 34

Output:
12 56 34 10 20 30

Example Input/Output 2:
Input:
7 4 5 9 1

Output:
7 4 5 9 1 10 20 30

PYTHON

numList = list(map(int, input().split()))
numList.append(10)
numList.append(20)
numList.append(30)
print(*numList)
                         
