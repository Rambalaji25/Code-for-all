Define class Professor

The program must accept the details of three professors as given below. 
1st professor - Accpet the name (consider "N/A" as department and 10000 as salary). 
2nd professor - Accpet the name and department (consider 15000 as salary).
3rd professor - Accpet the name, department and salary. 
The program must print the name, department and salary of the three professors as shown in the

 Example Input/Output 1:
 Input: 
Hector 
Arun ECE
Catherine CSE 25000

Output: 
Name: Hector 
Department:N/A
Salary: 10000 
Name: Arun 
Department: ECE 
Salary: 15000 
Name: Catherine 
Department: CSE 
Salary: 25000 

Example Input/Output 2: 
Input: Rachel Babloo
 Physics Pavithra EEE
 30000

 Output: Name: Rachel 
Department: N/A 
Salary: 10000
 Name: Babloo
 Department: Physics
 Salary: 15000 
Name: Pavithra D
epartment: EEE
 Salary: 30000

program (JAVA)
   
 import java.util.Scanner;
 class Professor {
     public String r,d;
public int money;
public Professor(String r){
    this.r=r;
    this.d="N/A";
    this.money=10000;
}
public Professor(String r,String d){
    this.r=r;
    this.d=d;
    this.money=15000;
    
}
public Professor(String r,String d,int money){
    this.r=r;
    this.d=d;
    this.money=money;
}
public String getName(){
    return this.r;
}
public String getDept(){
    return this.d;
    
}
public int getSalary(){
    return this.money;
}
}
 // End of Professor
 class public class Hello{
     
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        Professor prof1 = new Professor(sc.nextLine().trim());
        Professor prof2 = new Professor(sc.next(), sc.nextLine().trim());
        Professor prof3 = new Professor(sc.next(), sc.next(), sc.nextInt());
        display(prof1);
        display(prof2);
        display(prof3);
 }
 // End of main function
 private static void display(Professor prof) {
     
    System.out.println("Name: " + prof.getName());
    System.out.println("Department: " + prof.getDept()); 
    System.out.println("Salary: " + prof.getSalary()); 
    
}
 // End of display function
 } // End of Hello class 
