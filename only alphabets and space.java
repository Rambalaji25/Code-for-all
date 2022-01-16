Given a String S, remove all the special characters and numbers from S and print.

Input Format:
The first line contains the string S

Output Format:
The first line contains the string with only alphabets and spaces.

Boundary Conditions:
1 < Length of S < 1000

Example Input/Output 1:
Input:
Hello #$ World!

Output:
Hello  World

Example Input/Output 2:
Input:
Grand2017

Output:



import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
	Scanner sc=new Scanner(System.in);
	String str=sc.nextLine();
	str=str.replaceAll("[^A-Za-z\\s]","");
	System.out.println(str);

	}
}
