%{
#include <stdio.h>
#include <string.h>
#include "assign6.tab.h"

void yyerror(char *);

#define MAX_LIMIT 512
char identifier[MAX_LIMIT][MAX_LIMIT];
int total_id = 0;
extern YYSTYPE yylval;
int lineNum = 0;

%}

digit  [0-9]
letter [a-zA-Z]
mulop	[*/%]
addop	[+-]


%%
"if" { return IF; }
"else" { return ELSE; }
"while" { return WHILE; }
"for" { return FOR; }

[a-zA-Z_]([^-+[*/=.(), \t\n])*|[a-zA-Z]+"["([a-z]|[0-9]+)"]"  {
	int i;
    int flag=0; 
    for (i = 0; i<total_id; i++){
	    if (strcmp(identifier[i], yytext)==0){
	        flag=1;
	        break;
	    }
    }
	strcpy(yylval.STRING, yytext);
			 
	if(flag==0){
		strcpy(identifier[total_id++],yylval.STRING);
	}
	return ID;
}
{digit}+|({digit}+("."){digit}+) { yylval.VALUE = atof(yytext); return NUM;} 
"=="|">="|"<="|">"|"<"|"!=" { strcpy(yylval.STRING, yytext); return RELOP; }
{addop}|("||") { strcpy(yylval.STRING, yytext); return ADDOP; }
{mulop}|("&&") { strncpy(yylval.STRING, yytext, strlen(yytext)); return MULOP; }
"="	{ return ASSIGN; }
"!"	{ return NOT; }
"(" { return STRBO; }
")"	{ return STRBC; }
"{"	{ return CURBO; }
"}"	{ return CURBC; }
";" { return DELIM; }
"[" { printf("read LB"); return LB; }
"]" { printf("read RB"); return RB; }
"\n" { lineNum++; return END; }
[ \t]+ { /*ignore*/ }
%%

int yywrap(){
	
}
