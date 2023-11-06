%{
#include "addrss.tab.h"
%}

%%
[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[=+\-*/]    { return yytext[0]; }
[a-zA-Z]+   { yylval = yytext[0]; return ID; }
"while"     { return WHILE; }
"("         { return yytext[0]; }
")"         { return yytext[0]; }
"{"         { return yytext[0]; }
"}"         { return yytext[0]; }
[ \n \t]       { /* ignore whitespace */ }
.           { /* ignore other characters */ }
%%

int yywrap() {
    return 1;
}
