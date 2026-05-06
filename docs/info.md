<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

---
# How it works

An 8-bit ALU supporting 7 operations selected by a 3-bit opcode.
Operand A is provided via ui_in. Operand B is loaded into a register
by asserting uio_in[3] (load_b) for one clock cycle while ui_in holds
the B value. The result appears on uo_out. A zero flag is set on
uio_out[0] when the result is zero.

Opcodes:
- 000: ADD (A + B)
- 001: SUB (A - B)
- 010: AND (A & B)
- 011: OR  (A | B)
- 100: XOR (A ^ B)
- 101: NOT (~A)
- 110: PASS (B)

# How to test

1. Reset the design (rst_n = 0, then rst_n = 1)
2. Load operand B: set ui_in to B value, set uio_in[3]=1, wait one clock, set uio_in[3]=0
3. Set ui_in to operand A value
4. Set uio_in[2:0] to desired opcode
5. Read result from uo_out
6. Check zero flag on uio_out[0]

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any
