; <PROBLEM 1>

JMP start

; Code
start: nop

LXI H, 8850H ; storing the first address of the source block in D register
LXI D, 8870H ; storing the first address of the destination block in E register
MVI C, 10H   ; loading the length of the source block

; looping over memory addresses
LOOP: MOV A, M
STAX D
INX H
INX D
DCR C
JNZ LOOP

HLT

