.686
.model flat

public _quantileA

.data
sto qword 100.0
piecdziesiat qword 50.0

; double quantileA(double)

.code
_quantileA PROC
	push ebp
	mov ebp, esp

	fld qword ptr [ebp+8]
	fld sto
	fmul
	fld piecdziesiat
	fadd

	pop ebp
	ret
_quantileA ENDP
END
