A number ‘n’ is said to be Adam number if reverse of the square of the number ‘n’ is
reverse of square of ‘n’. For example, 12 is an Adam number. Reverse of 12 = 21 Square of 
21 = 441 which is reverse of square of 12 (i.e) 144. Write a function to reverse a number.

Input Format:
The first line will contain the number.
Output Format:
Print Adam Number or Not Adam Number

#Your code below
rb=int(input())
def f(rb):
    return(int(str(rb) [::-1]))
def adam(rb):
    if rb**2==f(f(rb)**2):
        return('Adam Number')
    else:
        return('Not Adam Number')
print(adam(rb))
        
