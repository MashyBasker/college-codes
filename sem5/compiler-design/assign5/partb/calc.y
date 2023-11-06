%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    int yylex();
    void yyerror(char *);
    double variables[26] = {0}; // Assuming variables are single letters.
%}

%token VARIABLE INTEGER

%left '+' '-'
%left '*' '/'

%%

stmt_list: stmt '\n'
        | stmt_list stmt '\n'
        ;

stmt: VARIABLE '=' expr
    {
        variables[$1] = $3;
        printf("%c = %lf\n", $1 + 'a', variables[$1]);
    }
    | expr
    {
        printf("Result: %lf\n", $1);
    }
    ;

expr: INTEGER
    {
        $$ = $1;
    }
    | VARIABLE
    {
        $$ = variables[$1];
    }
    | expr '+' expr
    {
        $$ = $1 + $3;
    }
    | expr '-' expr
    {
        $$ = $1 - $3;
    }
    | expr '*' expr
    {
        $$ = $1 * $3;
    }
    | expr '/' expr
    {
        if ($3 != 0) {
            $$ = $1 / $3;
        } else {
            yyerror("Division by zero");
            exit(EXIT_FAILURE);
        }x
    }
    | '(' expr ')'
    {
        $$ = $2;
    }
    ;

%%

void yyerror(char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    yyparse();
    return 0;
}
