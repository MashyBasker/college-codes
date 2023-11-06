%{
  /* Definition section */
#include <stdio.h>
#include <stdlib.h>
#include "calc.tab.h"
extern int yylval;

%}
  
/* Rule Section */
%%
0 {yylval=0;return ZERO;}
1 {yylval=1;return ONE;}
   
[ \t] ;
\n return 0;
. return yytext[0];
%%
  
int yywrap()  
{  
  return 1;  
}  
