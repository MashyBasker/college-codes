%{
    #include "calc.tab.h"
    #include <math.h>
    #include <stdlib.h>
    void yyerror(char *);
%}

%%

[a-z] {
        yylval = *yytext - 'a';
        return VARIABLE;
    }

[0-9]+ { 
        yylval = atoi(yytext);
        return INTEGER;
       }

[-+*/()=\n] { return *yytext; }

[ \t]   ; /* skip whitespace */

.          yyerror("Unknown Character");

%%

int yywrap(void) {
    return 1;
}

