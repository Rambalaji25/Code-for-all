Given a R*C matrix (R - rows and C- Columns), print the sum of the values in each row as the output.

Input Format:
First line will contain R and C separated by a space.
Next R lines will contain C values, each separated by a space.

Output Format:
R lines representing the sum of elements of rows 1 to R.

Boundary Conditions:
2 <= R, C <= 50

Example Input/Output 1:
Input:
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:
10
26
42
58

 

import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
	Scanner sc=new Scanner(System.in);
	int r=sc.nextInt();
	int c=sc.nextInt();
	int s=0;
	int[][]arr=new int[r][c];
	for(int i=0;i<r;i++){
	    for(int j=0;j<c;j++){
	        arr[i][j]=sc.nextInt();
	    }
	}
	for(int i=0;i<arr.length;i++){
	    s=0;
	    for(int j=0;j<arr[0].length;j++){
	        s=s+arr[i][j];
	    }
	    System.out.println(s);
	}

	}
}
