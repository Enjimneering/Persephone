
import cocotb
from cocoutil import GenerateClock, Reset, RunProgram, posedge, SetDumpFile

# CPU  
#     inputs: 
#        clk, reset, [7:0] switches],
#     outputs:
#        [7:0] CPUOut, 

@cocotb.test()
async def TestMultiplicationAlgorithm(dut):
   
    SetDumpFile("test_multiplication", dut)
    dut.ui_in.value = 0

    await GenerateClock(dut)
    await Reset(dut)

    for regA in range(16):
        for regB in range(16):
            
            # set switches value
            dut.ui_in.value = (regA<<4|regB)
            
            #print(f"A: {regA} B: {regB}")
            await posedge(dut.clk)

            # run program in ROM (wait till PC wraps round)
            await RunProgram(dut)

            # assert that output = in1 * in2
            assert dut.uo_out.value == (regA * regB)

            #print(f" Multiplication Output: {dut.uo_out.value}")
        

    