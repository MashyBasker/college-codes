%{
#include<stdio.h>
#include<string.h>

#define MAX_LIMIT 512

int yyerror(char str[MAX_LIMIT]);
int yylex(void);

extern int lineNum;

int L = 0, T = 0, IF_NO = 1, ErrorRecovered = 0;
char message[MAX_LIMIT];



char STMT_STACK[MAX_LIMIT][MAX_LIMIT];
int STACK_TOP = 0;

void STMT_STACK_push(char str[MAX_LIMIT]){
	strcpy(STMT_STACK[STACK_TOP++], str);
}

%}


%union{
    char STRING[256];
    float VALUE;
}

%token ID NUM RELOP ADDOP MULOP ASSIGN NOT STRBO STRBC END CURBO CURBC IF ELSE WHILE FOR DELIM LB RB

%type <VALUE> NUM 
%type <STRING> ID RELOP ADDOP MULOP ASSIGN Factor Term Simple_expression Expression Variable

%start Start

%%

Start: Stmt { strcpy(message, "Missing expression!"); }
| Start Stmt {	strcpy(message,"It's not the last line of the file!"); }
;

Stmt: Variable ASSIGN Expression END { char str[MAX_LIMIT]; sprintf(str,"%s = %s",$1,$3); STMT_STACK_push(str); strcpy(message,"Variable or expression missing. Cannot assign anything!"); }

| IF STRBO Expression STRBC END { char str[MAX_LIMIT], label[MAX_LIMIT]; IF_NO = 1; strcpy(label, "label"); sprintf(str, "%d", ++L); strcat(label,str); sprintf(str, "if !(%s) goto %s",$3,label); STMT_STACK_push(str); }
CURBO END Start CURBC END { char str[MAX_LIMIT],label[MAX_LIMIT]; strcpy(label,"label"); sprintf(str, "%d", ++L); strcat(label,str); sprintf(str,"goto %s",label); STMT_STACK_push(str); strcpy(label,"label"); sprintf(str, "%d", L-IF_NO); strcat(label,str); sprintf(str, "%s:", label); STMT_STACK_push(str); } 
ELSE END CURBO END Start CURBC END { char str[MAX_LIMIT],label[MAX_LIMIT]; strcpy(label, "label"); sprintf(str, "%d", L); strcat(label,str); sprintf(str, "%s:", label); STMT_STACK_push(str); IF_NO+=2; }

| WHILE { char str[MAX_LIMIT],label[MAX_LIMIT]; IF_NO = 1; strcpy(label,"label"); sprintf(str,"%d", ++L); strcat(label,str); sprintf(str, "%s:", label); STMT_STACK_push(str); }
STRBO Expression STRBC END { char str[MAX_LIMIT],label[MAX_LIMIT]; strcpy(label, "label"); sprintf(str, "%d", ++L); strcat(label,str); sprintf(str, "if %s is false goto %s",$4,label); STMT_STACK_push(str); }
CURBO END Start CURBC END { char str[MAX_LIMIT],label[MAX_LIMIT]; strcpy(label, "label"); sprintf(str, "%d", L-IF_NO); strcat(label,str); sprintf(str, "goto %s", label); STMT_STACK_push(str); strcpy(label, "label"); sprintf(str, "%d", L-IF_NO+1); strcat(label,str); sprintf(str, "%s:", label); STMT_STACK_push(str); IF_NO+=2; }
;

| FOR
STRBO Variable ASSIGN Expression { char str[MAX_LIMIT],label[MAX_LIMIT]; sprintf(str,"%s = %s",$3,$5); STMT_STACK_push(str); strcpy(message,"Variable or expression missing. Cannot assign anything!"); IF_NO = 1; strcpy(label,"label"); sprintf(str,"%d", ++L); strcat(label,str); sprintf(str, "%s: ", label); STMT_STACK_push(str); }
DELIM Expression DELIM { char str[MAX_LIMIT],label[MAX_LIMIT]; strcpy(label, "label"); sprintf(str, "%d", ++L); strcat(label,str); sprintf(str, "if %s is false goto %s",$8,label); STMT_STACK_push(str); }
Variable ASSIGN Expression STRBC END { char str[MAX_LIMIT]; sprintf(str,"%s = %s",$11,$13); STMT_STACK_push(str); strcpy(message,"Variable or expression missing. Cannot assign anything!"); }
CURBO END Start CURBC END { char str[MAX_LIMIT],label[MAX_LIMIT]; strcpy(label, "label"); sprintf(str, "%d", L-IF_NO); strcat(label,str); sprintf(str, "goto %s", label); STMT_STACK_push(str); strcpy(label, "label"); sprintf(str, "%d", L-IF_NO+1); strcat(label,str); sprintf(str, "%s:", label); STMT_STACK_push(str); IF_NO+=2; }
;

Variable: ID { strcpy($$,$1); strcpy(message,"Expecting something else!"); }
| Term { strcpy($$, $1); }
;

Expression: Simple_expression { strcpy($$,  $1); strcpy(message,"Missing expression!"); }

| Simple_expression RELOP Simple_expression { char str[MAX_LIMIT]; sprintf(str, "%s %s %s", $1, $2, $3); strcpy($$,  str); strcpy(message,"Conditional operation cannot be done"); }
;

Simple_expression: Term { strcpy($$, $1); }

| Simple_expression ADDOP Term { char str[MAX_LIMIT], result[MAX_LIMIT]; strcpy(result, "T"); sprintf(str, "%d", ++T); strcat(result,str); sprintf(str, "%s = %s %s %s", result, $1, $2, $3); STMT_STACK_push(str); strcpy($$, result); strcpy(message,"Additive operation cannot be done"); }
;

Term : Factor { strcpy($$, $1); }

| ID LB Term RB {char str[MAX_LIMIT], result[MAX_LIMIT];
    strcpy(result, "T");
    sprintf(str, "%d=", ++T);
    strcat(result, str);
	sprintf(str,"4 * %s", $3);
	strcat(result, str);
	STMT_STACK_push(result);
	int cop=T;
    sprintf(str, "T%d = %s[T%d]", ++T, $1, cop);
    STMT_STACK_push(str); 
	sprintf(str,"T%d",T);
	strcpy($$, str);
    strcpy(message, "Indexed assignment done!");
	}

| Term MULOP Factor { char str[MAX_LIMIT], result[MAX_LIMIT]; 
					  strcpy(result, "T"); sprintf(str, "%d", ++T); 
					  strcat(result,str); sprintf(str, "%s = %s %s %s", result,$1, $2,$3); 
					  STMT_STACK_push(str); strcpy($$, result); 
					  strcpy(message,"Multiplicative operation cannot be done!"); }
; 


Factor:ID { strcpy($$,$1); strcpy(message,"Expecting something else!"); }
				
| NUM { char str[MAX_LIMIT], result[MAX_LIMIT], num[MAX_LIMIT]; strcpy(result, "T"); sprintf(str, "%d", ++T); strcat(result,str); sprintf(num, "%.2f", $1); sprintf(str, "%s = %s", result, num); STMT_STACK_push(str); strcpy($$,result); strcpy(message,"Unrecognized number format!"); }

| STRBO Expression STRBC { strcpy(message,"'(' or ')' missing OR expression not found!"); }

| NOT Factor { char str[MAX_LIMIT], result[MAX_LIMIT], num[MAX_LIMIT]; strcpy(result, "T"); sprintf(str, "%d", ++T); strcat(result,str); sprintf(num, "%s", $2); sprintf(str, "%s = !%s", result, num); STMT_STACK_push(str); strcpy($$,result); strcpy(message,"Unrecognized number/ID format!"); }
; 				
%%



int main()
{
    yyparse();

	printf("\nOUTPUT : \n");
	for(int i=0;i<STACK_TOP;i++){
		printf("%d) %s\n",i+1,STMT_STACK[i]);
	}
	printf("\n");

    return 0;
}


int yyerror(char str[MAX_LIMIT]){
	if(ErrorRecovered==0){
	    printf("Error Found @ line #%d: ", lineNum+1);
	    if(strcmp(str,"Invalid character")==0 || strcmp(str,"Identifier greater than 5 characters")==0)						
            printf("%s!", str);
		else if(strlen(message))
			printf("%s\n",message);
		else printf("%s\n", str);
			printf("\n");
		ErrorRecovered = 1;
    }
	// return 0;
}
