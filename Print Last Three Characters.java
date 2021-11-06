Print Last Three Characters
 
 The program accepts a string and prints the last three characters in the string.
 Example Input/Output 1:
 Input: 
 SkillRack
 
 Output: 
 ack 
 
 Example Input/Output 2:
 Input: 
 Programming 
 
 Output: 
 ing
 
 
 Java ( 12.0)
 
 import java.util.Scanner;
 public class Hello {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String str = sc.nextLine();
    System.out.print(str.string(sub.length()-3));
    }
 }
