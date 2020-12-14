"""Advent of Code 2020 Solutions
Author: Lari Unkari
"""

import io, math, re, modules.userInput

MASK_LENGTH = 36

def play(input_stream:io.TextIOWrapper, input_parameters, log_level):
    
    # Initialize and read input
    
    instructions = []

    cmd:str
    pos = None
    val = None

    parts:list
    for i in [line.strip() for line in input_stream.read().split('\n') if line.strip()]:
        parts = i.split(" = ")
        
        cmd = parts[0]
        if parts[0] == "mask":
            pos = None
            val = parts[1]
            if log_level >= 2: print(f"Operation {len(instructions)} is '{cmd}' = '{val}'")
        else:
            cmd = parts[0][:3]
            pos = int(parts[0][4:-1])
            val = int(parts[1])
            if log_level >= 2: print(f"Operation {len(instructions)} is '{cmd}[{pos}]' = '{val}'")
        
        instructions.append((cmd, pos, val))

    if log_level >= 1: print(f"Found {len(instructions)} instructions\n")

    # Run

    mask = ["X"] * MASK_LENGTH
    binary = ["0"] * MASK_LENGTH
    memory = {}
    s:str
    for index, instr in enumerate(instructions):
        cmd = instr[0]

        if cmd == "mask":
            val = instr[2]

            if log_level >= 1:
                s = "".join(mask)
                print(f"[{index}] Mask set to '{val}'\n[{index}]    Mask was '{s}'")

            for i in range(MASK_LENGTH):
                mask[i] = val[i]
        else:
            s = "{0:b}".format(instr[2])

            if log_level >= 2: print(f"Input value {instr[2]}, binary {s}")

            for i in range(MASK_LENGTH):
                pos = -1-i
                if mask[pos] != "X":
                    binary[pos] = mask[pos]
                elif i < len(s):
                    binary[pos] = s[pos]
                else:
                    binary[pos] = "0"
            
            pos = instr[1]
            s = "".join(binary)
            val = int(s, 2)

            if log_level >= 2: print(f"Final input value {val}, binary {s}")
            if log_level >= 1:
                if pos in memory:
                    print(f"[{index}] Mem[{pos}] set to {val}, was {memory[pos]}")
                else:
                    print(f"[{index}] Mem[{pos}] set to {val}, was not set")

            memory[pos] = val

    print(f"\nDone processing instructions, memory has {len(memory)} entries")

    sum = 0
    for key in memory.keys():
        val = memory[key]
        if log_level >= 1: print(f"Memory[{key}] = {val}")
        sum += val

    print(f"\nSum of all memory values is {sum}")