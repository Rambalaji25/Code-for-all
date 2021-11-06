Print Last N Characters 
The program accepts a string and an integer N as the input. 
The program must print the last N characters of the string as the output. 
Example Input/Output 1:
Input:
SkillRack 
4 

Output:
Rack 

Java ( 12.0) 
import java.util.Scanner;
public class Hello {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str =sc.nextLine();
    int N = sc.nextInt();
    System.out.print(str.substring(str.length()-N);
    }
}
