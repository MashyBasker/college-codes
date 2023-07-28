
; *** Problem Statement ***
; Find the 2’s complement of the number stored in the memory location
; 8C00H, and place the result in memory location 8C01H.

jmp start


start:	nop
	lda 8C00H
	cma
	sta 8C00H
	adi 01
	sta 8C01H


	hlt