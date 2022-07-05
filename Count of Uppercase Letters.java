
A string is passed as input. The program must print the count of uppercase letters.

Boundary Condition(s):
1 <= length of string <= 1000

Input Format:
The first line contains the string.

Output Format:
The first line contains the count of uppercase letters.

Example Input/Output 1:
Input:
aPpLe

Output:
2

Example Input/Output 2:
Input:
MoNGoDB

Output:
5

"
  import java.util.*;
public class Hello {
    public static void main(String[] args) {
        //Your Code Here
        Scanner sc=new Scanner(System.in);
        int u=0;
        String str=sc.nextLine();
        for(int i=0;i<str.length();i++){
            char ss=str.charAt(i); 
            if(ss>='A' && ss<='Z')
            u++;
            
        }
        System.out.print(u);
        
    }
    
}
  "
