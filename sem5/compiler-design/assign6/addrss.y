%{
#include <stdio.h>
int yylex();
void yyerror(const char* s);
%}

%token NUMBER
%token ID
%token EOL
%token WHILE

%left '+' '-'
%left '*' '/'

%%
program:
    | program statement EOL
    ;

statement:
    assignment
    | while_loop
    ;

assignment:
    ID '=' expression
    ;

expression:
    NUMBER
    | ID
    | expression '+' expression
    | expression '-' expression
    | expression '*' expression
    | expression '/' expression
    ;

while_loop:
    WHILE '(' condition ')' '{' program '}' 
    ;

condition:
    expression '>' expression
    | expression '<' expression
    | expression ">=" expression
    | expression "<=" expression
    | expression "==" expression
    ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char* s) {
    printf("Error: %s\n", s);
}

int yywrap() {
    return 1;
}
