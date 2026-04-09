global change_val

change_val:
    push ebp
    mov ebp, esp
    sub esp, 8
    mov dword [ebp-4], 50
    mov dword [ebp-8], 100

    fild dword [ebp-4]
    fild dword [ebp-8]
    fld qword [ebp+8]
    fmul
    fadd

    mov esp, ebp
    pop ebp
    ret