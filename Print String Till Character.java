A string S is passed as the input. Character C is also passed as the input. The program must print the string value S till C is encountered.

Input Format:
The first line denotes the value of S.
The second line denotes the value of C.

Output Format:
The first line contains the string value S till C is encountered.

Boundary Conditions:
Length of S is from 3 to 100.

Example Input/Output 1:
Input:
manager
e

Output:
manag

Example Input/Output 2:
Input:
Everest
e

Output:
Ev

Explanation:
As the input character C is e which is in lower case, the first letter in Everest< upper case E is ignored and the string S is printed till a lower case e is encountered.


import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner Sc = new Scanner(System.in);
		String str = Sc.next();
		char[] c = str.toCharArray();
		char ch = Sc.next().charAt(0);
		for(int i=0;i<str.length();i++){
		    if(c[i]==ch){
		        break;
		    }
		    else{
		        System.out.print(c[i]);
		    }
		}
	}
}
