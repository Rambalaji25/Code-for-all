
The program must accept two integers X and Y and print the odd integers between them.

Input Format:
The first line denotes the value of X.
The second line denotes the value of Y.

Output Format:
The first line contains the odd integers between X and Y separated by a space.

Boundary Conditions:
-999999 <= X <= 9999999
X < Y <= 9999999

Example Input/Output 1:
Input:
1
11

Output:
3 5 7 9

Example Input/Output 2:
Input:
24
30

Output:
25 27 29

import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Her
	Scanner sc=new Scanner(System.in);
	int d=sc.nextInt();
	int g=sc.nextInt();
	for(int i=d+1;i<=g-1;i++){
	    if(i%2!=0){
	        System.out.print(i+" ");
	    }
	}

	}
}
