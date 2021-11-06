Print First N characters

The program accepts a string S and an integer N as the input.
  
Then the program must print the first N characters in the string S as the output.
  
Example Input/Output 1: 
Input:
SkillRack
3

Output: 
Ski

Program [java]

import java.util.Scanner;
public class Hello {
  public static void main(String[] args) { 
    Scanner sc = new Scanner(System.in);
    String str =sc.nextLine();
    int N =sc.nextInt();
    System.out.print(str.substring(0,N);
  }
}
