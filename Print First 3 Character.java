Print First 3 Character
the program accepts a string and prints the first three characters as the output.
Note: The length of the string is always greater than or equal to three.
Example Input/Output 1: 
Input:
Hello
Output:
Hel

program [Java] 

import java.util.Scanner;
public class Hello {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.nextLine();
    System.out.print(str.substring(0,3));
