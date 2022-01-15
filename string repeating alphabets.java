Given a string S as the input, print the distinct alphabets in S that occur more than once. The alphabets must be printed based on the order of their occurrence in S.

Input Format:
The first line contains S.

Output Format:
The first line contains the distinct alphabets in S that occur more than once.

Boundary Conditions:
2 <= LENGTH of S <= 200

Example Input/Output 1:
Input:
Apple

Output:
p

Example Input/Output 2:
Input:
environment

Output:
en


import java.util.*;
public class Hello {

    public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	String s=sc.nextLine();
	int c;
	char a[]=s.toCharArray();
	for(int i=0;i<a.length;i++){
	    c=1;
	    for(int j=i+1;j<a.length;j++){
	        if(a[i]==a[j] && a[i]!=' '){
	            c++;
	            a[j]='0';
	        }
	    }
	    if(c>1 && a[i]!='0')
	    System.out.print(a[i]);
	}

	}
}
