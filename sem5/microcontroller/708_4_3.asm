; PROGRAM 2: ADDITION AND SUBTRACTION THROUGH PORTS

jmp start


;code
start: nop


;ADDITION
IN 00H
MOV B, A
IN 01H
ADD B
OUT 02H

;SUBTRACTION
IN 01H
SUB B
OUT 03H

HLT