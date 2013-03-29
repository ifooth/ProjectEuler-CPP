	.file	"euler.c"
	.def	___main;	.scl	2;	.type	32;	.endef
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB6:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	call	_problem3
	movl	$10, (%esp)
	call	_putchar
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE6:
	.section .rdata,"dr"
LC0:
	.ascii "sum=%d\0"
	.text
	.globl	_problem1
	.def	_problem1;	.scl	2;	.type	32;	.endef
_problem1:
LFB7:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$40, %esp
	movl	$0, -12(%ebp)
	movl	$3, -16(%ebp)
	jmp	L4
L7:
	movl	-16(%ebp), %eax
	movl	$3, %ecx
	cltd
	idivl	%ecx
	movl	%edx, %eax
	testl	%eax, %eax
	je	L5
	movl	-16(%ebp), %eax
	movl	$5, %ecx
	cltd
	idivl	%ecx
	movl	%edx, %eax
	testl	%eax, %eax
	jne	L6
L5:
	movl	-16(%ebp), %eax
	addl	%eax, -12(%ebp)
L6:
	incl	-16(%ebp)
L4:
	cmpl	$999, -16(%ebp)
	jle	L7
	movl	-12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE7:
	.globl	_problem2
	.def	_problem2;	.scl	2;	.type	32;	.endef
_problem2:
LFB8:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$40, %esp
	movl	$3, -12(%ebp)
	movl	$1, -24(%ebp)
	movl	$2, -16(%ebp)
	movl	$2, -20(%ebp)
	jmp	L10
L11:
	movl	-16(%ebp), %eax
	movl	%eax, -24(%ebp)
	movl	-12(%ebp), %eax
	movl	%eax, -16(%ebp)
	movl	-16(%ebp), %eax
	movl	-24(%ebp), %edx
	addl	%edx, %eax
	movl	%eax, -12(%ebp)
	movl	-12(%ebp), %eax
	andl	$1, %eax
	testl	%eax, %eax
	jne	L10
	movl	-12(%ebp), %eax
	addl	%eax, -20(%ebp)
L10:
	cmpl	$4000000, -12(%ebp)
	jle	L11
	movl	-20(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE8:
	.section .rdata,"dr"
LC1:
	.ascii "%lld=\0"
	.def	___divdi3;	.scl	2;	.type	32;	.endef
	.def	___moddi3;	.scl	2;	.type	32;	.endef
LC2:
	.ascii "%lld^%lld * \0"
	.text
	.globl	_problem3
	.def	_problem3;	.scl	2;	.type	32;	.endef
_problem3:
LFB9:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%ebx
	subl	$68, %esp
	.cfi_offset 3, -12
	movl	$-443946297, -16(%ebp)
	movl	$139, -12(%ebp)
	movl	$2, -24(%ebp)
	movl	$0, -20(%ebp)
	movl	-16(%ebp), %eax
	movl	-12(%ebp), %edx
	movl	%eax, 4(%esp)
	movl	%edx, 8(%esp)
	movl	$LC1, (%esp)
	call	_printf
	jmp	L14
L19:
	movl	$0, -32(%ebp)
	movl	$0, -28(%ebp)
	jmp	L15
L16:
	addl	$1, -32(%ebp)
	adcl	$0, -28(%ebp)
	movl	-24(%ebp), %eax
	movl	-20(%ebp), %edx
	movl	%eax, 8(%esp)
	movl	%edx, 12(%esp)
	movl	-16(%ebp), %eax
	movl	-12(%ebp), %edx
	movl	%eax, (%esp)
	movl	%edx, 4(%esp)
	call	___divdi3
	movl	%eax, -16(%ebp)
	movl	%edx, -12(%ebp)
L15:
	movl	-16(%ebp), %eax
	movl	-12(%ebp), %edx
	movl	-24(%ebp), %ecx
	movl	-20(%ebp), %ebx
	movl	%ecx, 8(%esp)
	movl	%ebx, 12(%esp)
	movl	%eax, (%esp)
	movl	%edx, 4(%esp)
	call	___moddi3
	orl	%edx, %eax
	testl	%eax, %eax
	je	L16
	cmpl	$0, -28(%ebp)
	js	L17
	cmpl	$0, -28(%ebp)
	jg	L21
	cmpl	$0, -32(%ebp)
	jbe	L17
L21:
	movl	-32(%ebp), %eax
	movl	-28(%ebp), %edx
	movl	%eax, 12(%esp)
	movl	%edx, 16(%esp)
	movl	-24(%ebp), %eax
	movl	-20(%ebp), %edx
	movl	%eax, 4(%esp)
	movl	%edx, 8(%esp)
	movl	$LC2, (%esp)
	call	_printf
L17:
	addl	$1, -24(%ebp)
	adcl	$0, -20(%ebp)
L14:
	movl	-16(%ebp), %eax
	xorl	$1, %eax
	orl	-12(%ebp), %eax
	testl	%eax, %eax
	jne	L19
	movl	$0, %eax
	addl	$68, %esp
	popl	%ebx
	.cfi_restore 3
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE9:
	.def	_putchar;	.scl	2;	.type	32;	.endef
	.def	_printf;	.scl	2;	.type	32;	.endef
