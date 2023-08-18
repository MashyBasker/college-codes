; <PROBLEM 2>

JMP start

; code
start: nop

LXI H, 885FH ; storing the source address
LXI D, 8870H ; storing the destination address
MVI C, 10H   ; storing the block size

; starting the loop
LOOP: MOV A, M
STAX D
DCX H
INX D
DCR C
JNZ LOOP

HLT
