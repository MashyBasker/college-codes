%{
#include <stdio.h>
#include <string.h>

int number=0;
int plus=0;
int minus=0;
int multiplication=0;
int division=0;
int lparen=0;
int rparen=0;
int equal=0;
int decimal_num=0;
%}
   
%%
[(] {lparen++;printf("<LPAREN>");} /* Identifying left parentheses */
[)] {rparen++;printf("<RPAREN>");} /* Identifying right parentheses */
[=] {equal++;printf("<EQUAL>");}   /* Identifying equal sign */
[/] {division++;printf("<DIV>");}  /* Identifying division symbol */
[*] {multiplication++;printf("<MULT>");} /* Identifying multiplication symbol */
[+] {plus++;printf("<PLUS>");}    /* Identifying plus symbol */
[-] {minus++;printf("<MINUS>");}  /* Identifying minus symbol */
[0-9]* {number++;printf("<NUMBER>");} /* Identifying numbers */
[0-9]*[.][0-9]* {decimal_num++;printf("<DECIMAL NUMBER>");} /* Identifying decimal numbers */
%% 
  
/*** use code section ***/
  
int main()                                              
{
   
  yylex(); 
  printf("+--------------+\n");
  printf("LPAREN = %d\n", lparen);
  printf("RPAREN = %d\n", rparen);
  printf("EQUAL = %d\n", equal);
  printf("PLUS = %d\n", plus);
  printf("MINUS = %d\n", minus);
  printf("DIVISION = %d\n", division);
  printf("NUMBER = %d\n", number);
  printf("MULTIPLICATION = %d\n", multiplication);
  printf("+--------------+\n");
  return 0; 
}