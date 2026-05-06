import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

async def reset_dut(dut):
    dut.rst_n.value = 0
    dut.ena.value   = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await Timer(20, units="ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)

async def load_b(dut, b_val):
    dut.ui_in.value  = b_val
    dut.uio_in.value = 0b00001000
    await RisingEdge(dut.clk)
    dut.uio_in.value = 0b00000000

@cocotb.test()
async def test_add(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    await reset_dut(dut)
    await load_b(dut, 10)
    dut.ui_in.value  = 5
    dut.uio_in.value = 0b000
    await Timer(1, units="ns")
    assert dut.uo_out.value == 15, f"ADD failed: got {dut.uo_out.value}"

@cocotb.test()
async def test_sub(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    await reset_dut(dut)
    await load_b(dut, 3)
    dut.ui_in.value  = 10
    dut.uio_in.value = 0b001
    await Timer(1, units="ns")
    assert dut.uo_out.value == 7, f"SUB failed: got {dut.uo_out.value}"

@cocotb.test()
async def test_zero_flag(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    await reset_dut(dut)
    await load_b(dut, 5)
    dut.ui_in.value  = 5
    dut.uio_in.value = 0b001
    await Timer(1, units="ns")
    assert dut.uio_out.value == 1, "Zero flag should be set"

@cocotb.test()
async def test_and(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    await reset_dut(dut)
    await load_b(dut, 0b11001100)
    dut.ui_in.value  = 0b10101010
    dut.uio_in.value = 0b010
    await Timer(1, units="ns")
    assert dut.uo_out.value == 0b10001000, f"AND failed: got {dut.uo_out.value}"

@cocotb.test()
async def test_not(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    await reset_dut(dut)
    dut.ui_in.value  = 0b11110000
    dut.uio_in.value = 0b101
    await Timer(1, units="ns")
    assert dut.uo_out.value == 0b00001111, f"NOT failed: got {dut.uo_out.value}"
