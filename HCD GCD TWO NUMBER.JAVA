
The program must accept two numbers X and Y and then print their HCF/GCD.

Input Format:
The first line denotes the value of X.
The second line denotes the value of Y.

Output Format:
The first line contains the HCF of X and Y.

Boundary Conditions:
1 <= X <= 999999
1 <= Y <= 999999


Example Input/Output 1:
Input:
30
40

Output:
10

Example Input/Output 2:
Input:
15
10

Output:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
	Scanner sc=new Scanner(System.in);
	int a=sc.nextInt();
	int b=sc.nextInt();
	int gcd=1;
	for(int i=1;i<=a && i<=b;i++){
	    if(a%i==0 && b%i==0)
	    gcd=i;
	}
	 System.out.println(gcd);
	}
}
