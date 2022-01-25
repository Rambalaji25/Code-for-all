The program must accept a string S and two positions X and Y as the input. The program must print the vowels from the Xth position to the Yth position (inclusive of X and Y) in reverse order as the output.
Note: At least one vowel is always present between the two positions.

Boundary Condition(s):
2 <= Length of S <= 100
1 <= X < Y <= Length of S

Input Format:
The first line contains S.
The second line contains X and Y separated by a space.

Output Format:
The first line contains the vowels from the Xth position to Yth position in reverse order.

Example Input/Output 1:
Input:
Education
3 8

Output:
oiau

Example Input/Output 2:
Input:
BASEBALL
1 4

Output:
EA

Example Input/Output 3:
Input:
GoldCoin
4 6

Output:
o




#include<stdio.h>
#include<stdlib.h>
int isVowel(char ch){
    ch=tolower(ch);
    return ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u';
}
int main()
{
    char s[101];
    scanf("%s",s);
    int x,y;
    scanf("%d%d",&x,&y);
    for(int i=y-1;i>=x-1;i--){
        if(isVowel(s[i])){
            printf("%c",s[i]);
        }
    }

}
