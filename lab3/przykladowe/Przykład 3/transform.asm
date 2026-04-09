.686
.model FLAT
public _transform
.data
sto qword 100.0f
a qword 50.0f
res qword 0.0f
.code
_transform PROC
push ebp
mov ebp,esp
finit
push esi
lea esi,[ebp]
fld QWORD PTR [esi+8]; st(0)=N
fld sto; st(0)=100, st(1)=N
fmulp
fld a
faddp
;
;fstp res
;mov eax,res
pop esi
pop ebp
ret
_transform ENDP
END