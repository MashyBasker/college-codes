%{
#include <stdio.h>
#include <stdlib.h>
%}

%token ZERO ONE

%%
N: L {
    printf("%d\n", $$);
}
L: L B {
    $$ = $1 * 2 + $2;
}
 | B {
    $$ = $1;
}
B: ZERO {
    $$ = $1;
}
 | ONE {
    $$ = $1;
};
%%

int main() {
    while (yyparse()) {
        // continue parsing
    }
    return 0;
}

void yyerror(char *s) {
    fprintf(stdout, "%s\n", s);
}
