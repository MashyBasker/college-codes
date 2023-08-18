
; PROGRAM 1: Sort 5 numbers

jmp start



;code
start: NOP

BEGIN: LXI H, 9000H
MVI C, 04H
MVI D, 00H

; Begin loop for sorting
LOOP: MOV A, M
INX H
CMP M
JNC next
MOV B, M
MOV M, A

DCX H
MOV M, B
INX H
MVI D, 01H
next: DCR C
JNZ LOOP
MOV A, D
RRC 
JC BEGIN
HLT
