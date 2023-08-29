jmp start

start: nop

lda 2000H
mov b, a
lda 2001H
mov c, a
mvi a, 00H

next: add c
dcr b
jnz next

sta 2002H

hlt


