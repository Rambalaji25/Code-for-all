
An integer value N is passed as the input. The program must print the first N terms in the Fibonacci sequence.

Input Format:
The first line denotes the value of N.

Output Format:
The first N terms in the Fibonacci sequence (with each term separated by a space)

Boundary Conditions:
3 <= N <= 50

Example Input/Output 1:
Input:
5

Output:
0 1 1 2 3

Example Input/Output 2:
Input:
10

Output:
0 1 1 2 3 5 8 13 21 34

import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
	Scanner sc=new Scanner(System.in);
	long n=sc.nextInt();
	long i,f=0,s=1;
	for(i=1;i<=n;i++){
	    System.out.print(f+" ");
	    long d=f+s;
	    f=s;
	    s=d;
	}


	}
}
