; PROGRAM 2: Fibonacci numbers

jmp start


;code
start: NOP
LXI H, 8C00H
MVI A, 00H
MVI C, 0AH
MOV M, A
INX H
INR A

LOOP: MOV M, A
DCX H
ADD M
INX H
INX H
DCR C
JNZ LOOP

HLT