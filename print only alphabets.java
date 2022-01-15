A string S is passed as the input. S can contain alphabets, numbers and special characters. The program must print only the alphabets in S.

Input Format:
The first line contains S.

Output Format:
The first line contains only the alphabets in S.

Boundary Conditions:
The length of the input string is between 1 to 1000.


Example Input/Output 1:
Input:
abcd_5ef8!xyz

Output:
abcdefxyz

Example Input/Output 2:
Input:
1239_-87

Output:

Explanation:
As there are no alphabets in the input value nothing
is printed as output.


import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
	Scanner sc=new Scanner(System.in);
	String s=sc.nextLine();
	for(int i=0;i<s.length();i++){
	    if(s.charAt(i)<'A'||s.charAt(i)>'Z' && s.charAt(i)<'a'||s.charAt(i)>'z'){
	        s=s.substring(0,i)+s.substring(i+1);
	        i--;
	    }
	}
	System.out.println(s);

	}
}
