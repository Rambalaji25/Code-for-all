A year Y will be passed as input. The program must find if the given year is a leap year or not.
- If it is leap year, the program must print yes else it should print no

Note: A year is a leap year if it is divisible by 4. If it is a century then it should be divisible by 400.
The pseudocode is as given below.
if year is divisible by 400 then is_leap_year
else if year is divisible by 100 then not_leap_year
else if year is divisible by 4 then is_leap_year
else not_leap_year

Example Input/Output:
If 2000 is the input, the program must print yes
If 2100 is the input, the program must print no
If 2013 is the input, the program must print no

Input Format:
A year as a number is passed to the standard input.

Output Format:
The  string value as per the conditions above printed to the standard output.

Boundary Conditions:
0 < Y  <= 8000

  ------------------------------
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
	Scanner sc=new Scanner(System.in);
	int d=sc.nextInt();
	if(d%400==0){
	    System.out.println("yes");
	}
	else if(d%100==0){
	    System.out.println(" no");
	    
	}
	else if(d%4==0){
	    System.out.println(" yes");
	}
	else{
	    System.out.println(" no");
	}

	}
}
